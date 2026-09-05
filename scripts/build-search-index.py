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
# `skip_if` joined at weight 1 in FIX-27, below every field that says what a resource
# teaches. A skip line is what a thing is NOT for, so it should be able to find a page for
# somebody who typed their problem in the resource's own words - "stop claude inventing
# pixel values" is a phrase that exists only in a skip line - and it should never outrank
# a page that teaches the thing.
WEIGHTS = {"questions": 5, "keywords": 3, "teaches": 2, "title": 2, "who_for": 1,
           "skip_if": 1.5}

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
        depth = {}
        for field, w in WEIGHTS.items():
            val = x.get(field, "")
            texts = val if isinstance(val, list) else [val]
            hit = set()
            for t in texts:
                for word in words(str(t)):
                    seen[word] = max(seen.get(word, 0), w)
                    hit.add(word)
            for word in hit:
                depth[word] = depth.get(word, 0) + 1
            # keep multi-word keywords whole as well — "claude code" should beat
            # "claude" plus "code" appearing separately
            if field in ("keywords", "questions"):
                for t in texts:
                    t = str(t).lower().strip()
                    if " " in t and len(t) < 40:
                        phrases.setdefault(t, []).append(i)
        for word, w in seen.items():
            # A third element only where it says something: the number of fields this
            # word appeared in. It never touches the score - it breaks ties, where
            # "figma in six fields" beats "figma in three" and max weight cannot tell
            # them apart.
            f = depth.get(word, 1)
            idx.setdefault(word, []).append([i, w] if f < 2 else [i, w, f])
    return idx, phrases


# The two families that cannot be applied blindly. Left alone, "-or/-our" turns `for`
# into `four` and "-re/-er" turns `here` into `heer`.
OUR_OR = ["color", "behavior", "favor", "flavor", "honor", "humor", "labor",
          "neighbor", "rumor", "savor", "endeavor", "harbor", "vapor", "armor"]
RE_ER = ["center", "meter", "theater", "fiber", "liter", "caliber", "somber",
         "specter", "luster"]


def spelling_variants(word):
    """Every other spelling of this word an English-speaking reader might type."""
    out = set()
    if word.endswith("ize"):
        out.add(word[:-3] + "ise")
    if word.endswith("ise"):
        out.add(word[:-3] + "ize")
    if word.endswith("ization"):
        out.add(word[:-7] + "isation")
    if word.endswith("isation"):
        out.add(word[:-7] + "ization")
    if word.endswith("yze"):
        out.add(word[:-3] + "yse")
    if word.endswith("yse"):
        out.add(word[:-3] + "yze")
    if word.endswith("yzing"):
        out.add(word[:-5] + "ysing")
    if word.endswith("ysing"):
        out.add(word[:-5] + "yzing")
    for stem_ in OUR_OR:
        if word.startswith(stem_):
            out.add(word.replace(stem_, stem_[:-2] + "our", 1))
        if word.startswith(stem_[:-2] + "our"):
            out.add(word.replace(stem_[:-2] + "our", stem_, 1))
    for stem_ in RE_ER:
        if word.startswith(stem_):
            out.add(word.replace(stem_, stem_[:-2] + "re", 1))
        if word.startswith(stem_[:-2] + "re"):
            out.add(word.replace(stem_[:-2] + "re", stem_, 1))
    # modelling/modeling, travelled/traveled, labelling/labeling. Only the -el- pattern:
    # a blind single-l rule produced "assemblling" from "assembling" and "bilers" from
    # "billers" on the first run, which is what the printed list is for.
    for tail in ("ing", "ed", "er", "ers"):
        if word.endswith("ell" + tail):
            out.add(word[:-len(tail) - 3] + "el" + tail)
        elif word.endswith("el" + tail):
            out.add(word[:-len(tail) - 2] + "ell" + tail)
    out.discard(word)
    return out


def build_spelling(idx):
    """any form a reader might type -> every indexed form that means the same thing.

    Groups, not corrections. `prioritisation` and `prioritization` are both in this
    catalogue, in two posting lists, so a reader typing one of them sees half the
    material - which is cause 3 - and a map that skipped pairs already indexed would skip
    the whole fault.
    """
    groups = {}
    for word in idx:
        forms = {word} | spelling_variants(word)
        key = min(forms)
        groups.setdefault(key, set()).update(forms)
    # A form is only worth mapping when the group holds something the raw lookup misses:
    # either another indexed spelling, or the typed form is not indexed at all.
    out = {}
    for forms in groups.values():
        indexed = sorted(f for f in forms if f in idx)
        if not indexed:
            continue
        for f in sorted(forms):
            if f in indexed and len(indexed) < 2:
                continue          # only itself: the raw lookup already does this
            out[f] = indexed
    return out


SYN_FILE = "data/synonyms.json"


def load_synonyms(idx):
    """word -> the other words in its group, for words this catalogue actually holds.

    The table is written and justified by hand in data/synonyms.json and checked by
    scripts/validate-synonyms.py. Here it is only flattened: a term the index has never
    seen is dropped, because expanding to a word with no postings is work that produces
    nothing.
    """
    if not os.path.exists(SYN_FILE):
        return {}
    doc = json.load(open(SYN_FILE, encoding="utf-8"))
    out = {}
    for entry in doc.get("entries") or []:
        terms = [t for t in entry.get("terms") or [] if t in idx]
        if len(terms) < 2:
            continue
        for t in terms:
            out[t] = [o for o in terms if o != t]
    return out


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
    spelling = build_spelling(idx)
    synonyms = load_synonyms(idx)
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
        "spelling": spelling,
        "synonyms": synonyms,
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

    # Written out as well as indexed, so a wrong pair is a line in a file somebody can
    # read rather than a regex somebody has to re-derive.
    with open("data/spelling-pairs.json", "w", encoding="utf-8") as f:
        json.dump({"generated": "scripts/build-search-index.py",
                   "pairs": dict(sorted(spelling.items()))}, f,
                  ensure_ascii=False, indent=1)
        f.write("\n")
    both = sum(1 for v in spelling.values() if len(v) > 1)
    print(f"  spelling: {len(spelling)} forms mapped, {both} of them to a group this "
          f"catalogue holds under more than one spelling -> data/spelling-pairs.json")
    for k in sorted(spelling, key=lambda k: (-len(spelling[k]), k))[:6]:
        print("    %-18s -> %s" % (k, ", ".join(spelling[k])))
    print(f"  synonyms: {len(synonyms)} words expand at query time "
          f"(data/synonyms.json, every row with its reason)")

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
