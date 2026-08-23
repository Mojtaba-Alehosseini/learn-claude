#!/usr/bin/env python3
"""
Write the hidden search layer onto every item in data/items.json, using Gemini.

The hidden fields are never shown on the site. They exist so that a visitor can type
a sentence and get the right resource back, with no AI call at query time. Gemini does
the thinking once, offline; the browser only matches text.

Fields written (see docs/specs/2026-08-19-directory-spec.md section 9):
    keywords       10-30 strings, including beginner words and likely misspellings
    questions      3-8 real questions this resource answers, phrased as a person asks
    prerequisites  what you must already know
    teaches        concrete abilities you have afterwards, not topics

Usage:
    export GEMINI_API_KEY=...              # or put it in .env
    python3 scripts/enrich-items.py                 # enrich anything missing
    python3 scripts/enrich-items.py --force         # redo everything
    python3 scripts/enrich-items.py --limit 20      # try a small batch first
    python3 scripts/enrich-items.py --model gemini-flash-latest

Safe to interrupt and re-run. Saves after every batch, and skips items already done.
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error

ITEMS = "data/items.json"
MODEL = "gemini-flash-latest"   # lite is the fallback, not the default
BATCH = 10         # items per request. Bigger batches drift and drop fields.
PAUSE = 3.0        # seconds between requests. The free tier is about 10 rpm —
                   # going faster earns a 429 and costs more time than it saves.

FIELDS = ["keywords", "questions", "prerequisites", "teaches"]

INSTRUCTIONS = """You write the hidden search metadata for a directory of Claude learning resources.

Nobody ever reads what you write. It is only used to match what a visitor types against
the right resource. So it must be exhaustive and plain, not tidy or elegant.

For EACH resource you are given, return:

"keywords": 12-25 short strings.
  - The tools, features and product names it actually covers.
  - The tasks someone would be doing when they need it.
  - The problems it solves, in the words a frustrated person would use.
  - Plain beginner words as well as correct terms. Someone who has never used Claude
    types "ai chat thing" and "make it write emails", not "prompt engineering".
  - Include obvious misspellings and spacing variants of product names where a real
    person would type them, for example "claude code", "claudecode", "MCP", "anthropic".
  - Lowercase. No duplicates. No punctuation.

"questions": 3-8 real questions this resource answers.
  - Written the way a person types into a search box, not as headings.
  - Good: "how do i get claude to read my pdfs". Bad: "PDF ingestion capabilities".
  - Lowercase, no question marks needed.

"prerequisites": 0-4 short strings. What you must already know or have before this is
  useful. Empty array if genuinely none.

"teaches": 3-6 short strings. Concrete abilities you have after finishing.
  Abilities, not topics. Good: "set up an MCP server that reads your local files".
  Bad: "MCP".

Rules:
- Base everything on the title, summary, who_for and skip_if you are given. Do not
  invent capabilities the resource does not claim.
- If the summary is thin, stay general rather than guessing specifics.
- Never repeat the title verbatim as a keyword.

Return ONLY a JSON array, one object per resource, in the same order you received them:
[{"id": "<the id given>", "keywords": [...], "questions": [...], "prerequisites": [...], "teaches": [...]}]
No markdown fence, no prose."""


def load_keys():
    """All keys, best first. Free-tier quota is per key, so rotating through several
    keys multiplies how much we can do before the day resets."""
    keys = []
    env = os.environ.get("GEMINI_API_KEYS") or os.environ.get("GEMINI_API_KEY", "")
    keys += [k.strip() for k in env.split(",") if k.strip()]
    if os.path.exists(".env"):
        for line in open(".env", encoding="utf-8"):
            if line.startswith(("GEMINI_API_KEY=", "GEMINI_API_KEYS=")):
                v = line.split("=", 1)[1].strip()
                keys += [k.strip() for k in v.split(",") if k.strip()]
    seen, out = set(), []
    for k in keys:
        if k.startswith("AIza") and k not in seen:
            seen.add(k); out.append(k)
    if not out:
        sys.exit("No usable GEMINI_API_KEY in .env")
    return out


def call(keys, model, payload_text, tries=3):
    """Try every key before waiting. A 429 on one key is not a 429 on the next."""
    body = json.dumps({
        "contents": [{"parts": [{"text": payload_text}]}],
        "systemInstruction": {"parts": [{"text": INSTRUCTIONS}]},
        "generationConfig": {"temperature": 0.4, "responseMimeType": "application/json"},
    }).encode()
    last = None
    for attempt in range(tries):
        for key in keys:
            url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
                   f"{model}:generateContent?key={key}")
            try:
                req = urllib.request.Request(
                    url, data=body, headers={"Content-Type": "application/json"})
                r = json.load(urllib.request.urlopen(req, timeout=90))
                return r["candidates"][0]["content"]["parts"][0]["text"]
            except urllib.error.HTTPError as e:
                last = e
                if e.code in (429, 500, 503):
                    continue
                raise
            except Exception as e:
                last = e
                continue
        if attempt < tries - 1:
            wait = 20 * (attempt + 1)
            print(f"    all {len(keys)} keys busy, waiting {wait}s", flush=True)
            time.sleep(wait)
    raise last


def parse(text):
    """Gemini occasionally wraps the array or trails a comma. Recover what we can."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.M).strip()
    try:
        return json.loads(text)
    except Exception:
        m = re.search(r"\[.*\]", text, re.S)
        if not m:
            raise
        return json.loads(re.sub(r",(\s*[}\]])", r"\1", m.group(0)))


def clean_list(v, lower=False):
    if not isinstance(v, list):
        return []
    out = []
    for s in v:
        if not isinstance(s, str):
            continue
        s = s.strip().strip(".?")
        if lower:
            s = s.lower()
        if s and s not in out:
            out.append(s)
    return out


def main():
    args = sys.argv[1:]
    force = "--force" in args
    model = MODEL
    limit = None
    if "--model" in args:
        model = args[args.index("--model") + 1]
    if "--limit" in args:
        limit = int(args[args.index("--limit") + 1])

    keys = load_keys()
    items = json.load(open(ITEMS, encoding="utf-8"))
    for i, x in enumerate(items):
        x.setdefault("id", f"item-{i:04d}")

    todo = [x for x in items if force or not x.get("keywords")]
    if limit:
        todo = todo[:limit]
    print(f"{len(items)} items, {len(todo)} need enriching, model={model}")

    by_id = {x["id"]: x for x in items}
    done = failed = 0

    for i in range(0, len(todo), BATCH):
        chunk = todo[i:i + BATCH]
        payload = json.dumps([{
            "id": x["id"],
            "title": x.get("title", ""),
            "format": x.get("format", ""),
            "level": x.get("level", ""),
            "topics": x.get("topics", []),
            "summary": x.get("summary", ""),
            "who_for": x.get("who_for", ""),
            "skip_if": x.get("skip_if", ""),
        } for x in chunk], ensure_ascii=False)

        try:
            got = parse(call(keys, model, payload))
        except Exception as e:
            failed += len(chunk)
            print(f"  batch {i//BATCH+1}: FAILED {str(e)[:70]}", flush=True)
            continue

        n = 0
        for row in got:
            x = by_id.get(row.get("id"))
            if not x:
                continue
            x["keywords"] = clean_list(row.get("keywords"), lower=True)[:30]
            x["questions"] = clean_list(row.get("questions"), lower=True)[:8]
            x["prerequisites"] = clean_list(row.get("prerequisites"))[:4]
            x["teaches"] = clean_list(row.get("teaches"))[:6]
            if len(x["keywords"]) >= 8 and x["questions"]:
                n += 1
            else:
                x.pop("keywords", None)      # too thin — leave it for a retry
        done += n
        print(f"  batch {i//BATCH+1}/{(len(todo)+BATCH-1)//BATCH}: {n}/{len(chunk)} ok",
              flush=True)
        json.dump(items, open(ITEMS, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
        time.sleep(PAUSE)

    have = sum(1 for x in items if x.get("keywords"))
    print(f"\nenriched {done}, failed {failed}")
    print(f"items with hidden search data: {have}/{len(items)}")


if __name__ == "__main__":
    main()
