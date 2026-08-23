#!/usr/bin/env python3
"""
Test search against real sentences a visitor would type.

This mirrors assets/js/search.js exactly — same index, same IDF, same admit gate, same
floor. If the ranking is wrong here it is wrong on the site, and vice versa. Run it
after any change to the enrichment or the index.

    python3 scripts/test-search.py
    python3 scripts/test-search.py "how do i stop claude making things up"

No API key and no network. An earlier version embedded the query through Gemini and
blended 55% semantic with 45% keyword, which measured well but could never be what the
site does: a static page cannot hold an API key. Testing a pipeline the browser cannot
run told us nothing useful, so both sides now run the same algorithm.
"""

import json
import math
import re
import sys

ITEMS = "data/items.json"
KW = "data/search-keywords.json"

STOP = set("""a an and are as at be but by can do does for from get go had has have how i
if in into is it its me my not of on or our so than that the their them then there these
this to up us was we were what when where which who why will with you your""".split())

MIN_IDF_SCORE = 0.05   # below this a word is in almost everything and means nothing
MIN_IDF_ADMIT = 0.7    # below this a word may rank a resource but not admit it
FLOOR_FRACTION = 0.30
FLOOR_ABSOLUTE = 2.0
PREFIX_WEIGHT = 0.3


def words(s):
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 1]


def rank(query, kw):
    n = len(kw["ids"])
    scores = [0.0] * n
    exact = [False] * n
    q = query.lower()

    for w in words(query):
        posts = kw["words"].get(w)
        if posts:
            idf = math.log(n / len(posts))
            if idf >= MIN_IDF_SCORE:
                for i, weight in posts:
                    scores[i] += weight * idf
                    if idf > MIN_IDF_ADMIT:
                        exact[i] = True
        if len(w) > 5:
            head = w[:5]
            for k, p2 in kw["words"].items():
                if k != w and k[:5] == head:
                    for i, weight in p2:
                        scores[i] += weight * PREFIX_WEIGHT

    for phrase, ids in kw["phrases"].items():
        if phrase in q:
            for i in ids:
                scores[i] += 6
                exact[i] = True

    best = max(scores) if scores else 0
    if not best:
        return []
    floor = max(best * FLOOR_FRACTION, FLOOR_ABSOLUTE)
    keep = [i for i in range(n) if exact[i] and scores[i] >= floor]
    keep.sort(key=lambda i: -scores[i])
    return [(kw["ids"][i], scores[i]) for i in keep]


def main():
    items = json.load(open(ITEMS, encoding="utf-8"))
    kw = json.load(open(KW, encoding="utf-8"))
    by_id = {x["id"]: x for x in items}

    stale = [i for i in kw["ids"] if i not in by_id]
    if stale:
        sys.exit(f"Index is stale: {len(stale)} indexed ids are not in items.json. "
                 "Run scripts/build-search-index.py")

    queries = sys.argv[1:] or [
        "help me write my thesis faster",
        "i keep getting generic answers",
        "how do i make claude read my pdfs",
        "where do i even start",
        "stop claude inventing fake citations",
        "build an agent that uses my own tools",
        "teach my class to use ai honestly",
        "clean up a messy spreadsheet",
        "how do i build an mcp server",
    ]
    for q in queries:
        hits = rank(q, kw)
        print(f'\n"{q}"   {len(hits)} result(s)')
        if not hits:
            print("   nothing — this is a gap in the hidden keywords")
        for iid, s in hits[:3]:
            x = by_id[iid]
            print(f"   {s:6.1f}  [{','.join(x['roles'][:2]):22}] {x['title'][:56]}")


if __name__ == "__main__":
    main()
