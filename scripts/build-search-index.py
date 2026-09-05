#!/usr/bin/env python3
"""
Build the search index the browser uses. Two files, both static:

    data/search-keywords.json   small, loaded with the page
    data/search-vectors.json    larger, loaded only when the visitor starts typing

Stage one is the keyword index: every word from keywords, questions, teaches and the
title, mapped to the items that contain it, with a weight per field. Pure code, no API,
handles exact and partial word matches.

Stage two is embeddings: one vector per item from gemini-embedding-001, quantised to
int8 so the file stays small. This is what understands a sentence we never listed.

Embedding quota is generous — 100 requests a minute, 1000 a day — so 253 items costs
almost nothing.

Usage:
    python3 scripts/build-search-index.py              # both stages
    python3 scripts/build-search-index.py --keywords   # keyword index only, no API
    python3 scripts/build-search-index.py --resume     # only embed what is missing
"""

import json
import math
import os
import re
import sys
import time
import urllib.request
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stem import stem  # noqa: E402

ITEMS = "data/items.json"
KW_OUT = "data/search-keywords.json"
VEC_OUT = "data/search-vectors.json"
MODEL = "gemini-embedding-001"
DIMS = 768
PAUSE = 0.7          # 100 rpm allowed; stay comfortably under

# How much a match in each field is worth. A question match means the person asked
# almost exactly what this resource answers, so it outranks everything.
WEIGHTS = {"questions": 5, "keywords": 3, "teaches": 2, "title": 2, "who_for": 1}

STOP = set("""a an and are as at be but by can do does for from get go had has have how i
if in into is it its me my not of on or our so than that the their them then there these
this to up us was we were what when where which who why will with you your""".split())


def words(s):
    """Tokenise. Raw words, not stems - see build_keywords for where stemming happens."""
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 1]


def load_key():
    """First usable key. .env may hold one key or a comma-separated list, under either
    name — accept both so this never silently finds nothing."""
    sources = [os.environ.get("GEMINI_API_KEYS", ""), os.environ.get("GEMINI_API_KEY", "")]
    if os.path.exists(".env"):
        for line in open(".env", encoding="utf-8"):
            if line.startswith(("GEMINI_API_KEY=", "GEMINI_API_KEYS=")):
                sources.append(line.split("=", 1)[1])
    for src in sources:
        for k in src.split(","):
            if k.strip().startswith("AIza"):
                return k.strip()
    sys.exit("No GEMINI_API_KEY in environment or .env")


def build_keywords(items):
    """word -> [[item index, weight], ...]"""
    idx = {}
    phrases = {}
    for i, x in enumerate(items):
        seen = {}
        for field, w in WEIGHTS.items():
            val = x.get(field, "")
            texts = val if isinstance(val, list) else [val]
            for t in texts:
                for word in words(str(t)):
                    seen[word] = max(seen.get(word, 0), w)
            # keep multi-word keywords whole as well — "claude code" should beat
            # "claude" plus "code" appearing separately
            if field in ("keywords", "questions"):
                for t in texts:
                    t = str(t).lower().strip()
                    if " " in t and len(t) < 40:
                        phrases.setdefault(t, []).append(i)
        for word, w in seen.items():
            idx.setdefault(word, []).append([i, w])
    return idx, phrases


TIER_RANK = {"reviewed": 0, "ai-reviewed": 1, "previewed": 2, "listed": 3}


def build_tiebreak(items):
    """One integer per item: its place in the order equal scores fall back on.

    Tier first, because "best checked first" is already the default sort a reader was
    shown; then the more recently checked, because a stale look is weaker evidence than a
    fresh one; then the title, which decides nothing but decides it the same way twice.

    Precomputed here so that no comparison is written twice in two languages. A tie broken
    differently by Python and by the browser is the same bug as no tie-break at all.
    """
    order = sorted(range(len(items)), key=lambda i: (
        TIER_RANK.get(items[i].get("tier"), 9),
        items[i].get("checked") and (10 ** 9 - int(str(items[i]["checked"]).replace("-", "")))
        or 10 ** 9,
        str(items[i].get("title", "")).lower(),
    ))
    rank = [0] * len(items)
    for place, i in enumerate(order):
        rank[i] = place
    return rank


def build_stems(idx):
    """stem -> [the words that share it], for stems that hold more than one word.

    A second, smaller map beside the raw one. The query side reads the raw word at full
    weight and this at half, so `hallucinations` can reach a page that only says
    `hallucinated` without `design` and `designer` becoming the same word for ranking.

    Stems holding a single word are skipped: the raw lookup already covers them, and they
    are three quarters of the vocabulary.
    """
    groups = {}
    for word in idx:
        groups.setdefault(stem(word), []).append(word)
    # Member words, not postings. Duplicating the postings under the stem cost 106 KB and
    # bought nothing the query side cannot do by unioning the raw lists it already has.
    out = {s: sorted(m) for s, m in groups.items() if len(m) > 1}
    return out, out


def embed(key, text, task):
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
           f"{MODEL}:embedContent?key={key}")
    body = json.dumps({
        "model": f"models/{MODEL}",
        "content": {"parts": [{"text": text[:8000]}]},
        "taskType": task,
        "outputDimensionality": DIMS,
    }).encode()
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, data=body,
                                         headers={"Content-Type": "application/json"})
            r = json.load(urllib.request.urlopen(req, timeout=60))
            return r["embedding"]["values"]
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 503) and attempt < 3:
                time.sleep(10 * (attempt + 1))
                continue
            raise
        except Exception:
            if attempt < 3:
                time.sleep(3)
                continue
            raise


def doc_text(x):
    """What we embed. Deliberately the hidden fields, not the marketing summary —
    they are written in the words a visitor would actually type."""
    return " | ".join(filter(None, [
        x.get("title", ""),
        x.get("who_for", ""),
        " ".join(x.get("questions", [])),
        " ".join(x.get("keywords", [])),
        " ".join(x.get("teaches", [])),
        x.get("summary", "")[:300],
    ]))


def quantise(vec):
    """float32 -> int8. Normalise first so cosine similarity survives the squeeze."""
    n = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [max(-127, min(127, round(v / n * 127))) for v in vec]


def main():
    args = sys.argv[1:]
    items = json.load(open(ITEMS, encoding="utf-8"))
    for i, x in enumerate(items):
        x.setdefault("id", f"item-{i:04d}")

    idx, phrases = build_keywords(items)
    stems, groups = build_stems(idx)
    tiebreak = build_tiebreak(items)
    # Postings are integer positions because that keeps the file small, but a position
    # is only meaningful against the exact list it was built from. Shipping the id list
    # alongside lets the browser check it is reading the index it thinks it is — the
    # same drift that silently scrambled the learning paths would otherwise be possible
    # here, and would show up as quietly wrong search results.
    json.dump({
        "version": 2,
        "count": len(items),
        "ids": [x["id"] for x in items],
        "weights": WEIGHTS,
        "words": idx,
        "stems": stems,
        "tiebreak": tiebreak,
        "phrases": phrases,
    }, open(KW_OUT, "w", encoding="utf-8"), separators=(",", ":"))
    print(f"keyword index: {len(idx)} words, {len(phrases)} phrases "
          f"-> {KW_OUT} ({os.path.getsize(KW_OUT)/1024:.0f} KB)")

    # A minimum stem of 3 merges hard, so what it merged is printed rather than trusted.
    big = sorted(groups.items(), key=lambda kv: -len(kv[1]))
    print(f"  stems: {len(stems)} groups over {len(idx)} words "
          f"({sum(len(v) for v in groups.values())} words are in a group)")
    for s, members in big[:6]:
        print("    %-12s %s" % (s, ", ".join(members)))

    if "--keywords" in args:
        return

    key = load_key()
    old = {}
    if "--resume" in args and os.path.exists(VEC_OUT):
        prev = json.load(open(VEC_OUT, encoding="utf-8"))
        old = dict(zip(prev["ids"], prev["vectors"]))

    ids, vecs = [], []
    fails = 0
    for i, x in enumerate(items):
        if x["id"] in old:
            ids.append(x["id"]); vecs.append(old[x["id"]]); continue
        try:
            v = quantise(embed(key, doc_text(x), "RETRIEVAL_DOCUMENT"))
            ids.append(x["id"]); vecs.append(v)
        except Exception as e:
            fails += 1
            print(f"  {i}: FAILED {str(e)[:50]}", flush=True)
        if (i + 1) % 25 == 0:
            print(f"  embedded {len(vecs)}/{len(items)}", flush=True)
            json.dump({"version": 1, "model": MODEL, "dims": DIMS, "quantised": "int8",
                       "ids": ids, "vectors": vecs},
                      open(VEC_OUT, "w", encoding="utf-8"), separators=(",", ":"))
        time.sleep(PAUSE)

    json.dump({"version": 1, "model": MODEL, "dims": DIMS, "quantised": "int8",
               "ids": ids, "vectors": vecs},
              open(VEC_OUT, "w", encoding="utf-8"), separators=(",", ":"))
    print(f"vectors: {len(vecs)}/{len(items)} ({fails} failed) "
          f"-> {VEC_OUT} ({os.path.getsize(VEC_OUT)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
