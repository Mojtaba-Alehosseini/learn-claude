#!/usr/bin/env python3
"""
Every row has to be findable by its own questions.

    python3 scripts/check-self-retrieval.py            # the list, always exit 0
    python3 scripts/check-self-retrieval.py --strict   # exit 1 if any row fails

WHY THIS EXISTS

`questions[]` is the highest-weighted field in the index, and its whole job is to be the
sentence a reader types. FIX-30 rewrote it across the catalogue and, writing "in the
reader's words", replaced pages' own nouns with smoother near-synonyms - essay became
draft, peer review became review, cite became citation. Eight suite queries fell out of
the top three as a direct result.

The suite found eight because the suite happens to cover those subjects. It has
fifty-seven queries for hundreds of rows, so most of the catalogue could suffer the same
damage in silence. This check needs no suite: it asks each row's own questions and looks
for that row in the answer. A row its own questions cannot retrieve has questions that do
not describe it, and no query anybody types will find it either.

WHAT COUNTS AS FOUND

Top three, the same rule the suite grades on, and any one of the row's questions is
enough. A row is expected to be findable by the question that names its subject; the
reader's-words questions may legitimately be answered better by another row, because a
reader's phrasing describes a need rather than a page.

WHY IT WARNS RATHER THAN FAILS

Rows genuinely compete. Three rows about synthesising customer feedback cannot all be
first for "find themes in our feedback", and the loser is not thereby wrong. The list is
for reading, not for a machine to enforce - see `--strict` when you want the machine to
decide, and expect it to be wrong about collisions.
"""

import importlib.util
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITEMS = os.path.join(ROOT, "data", "items.json")
TOP = 3


def ranker():
    spec = importlib.util.spec_from_file_location(
        "ts", os.path.join(ROOT, "scripts", "test-search.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    strict = "--strict" in sys.argv
    ts = ranker()
    by, kw = ts.load()
    items = json.load(io.open(ITEMS, encoding="utf-8"))

    asked = 0
    missed = []          # rows no question of their own retrieves
    weak = []            # rows only one of their questions retrieves
    for x in items:
        qs = x.get("questions") or []
        if not qs:
            continue
        hits = []
        for q in qs:
            asked += 1
            top = [i for i, _s in ts.rank(q, kw)[:TOP]]
            if x["id"] in top:
                hits.append(q)
        if not hits:
            missed.append((x, qs))
        elif len(hits) == 1 and len(qs) > 2:
            weak.append((x, hits[0]))

    print("Self-retrieval: %d question(s) asked across %d row(s) that carry them."
          % (asked, sum(1 for x in items if x.get("questions"))))

    if missed:
        print()
        print("NOT FOUND BY ITS OWN QUESTIONS (%d row(s)). Each of these asks the "
              "catalogue its own questions and does not come back in the top %d - so a "
              "reader typing any of them lands somewhere else:" % (len(missed), TOP))
        for x, qs in missed:
            print("  %s" % x["title"][:72])
            for q in qs:
                top = [by[i]["title"] for i, _s in ts.rank(q, kw)[:TOP]]
                print("      %-46s -> %s" % (q[:46], (top[0][:40] if top else "(nothing)")))

    if weak:
        print()
        print("FOUND BY ONLY ONE OF ITS OWN QUESTIONS (%d row(s)) - read, do not fix "
              "blind. A reader's-words question may be answered better by another row, "
              "which is the catalogue working:" % len(weak))
        for x, q in weak[:25]:
            print("  %-56s only \"%s\"" % (x["title"][:56], q[:40]))
        if len(weak) > 25:
            print("  ... and %d more" % (len(weak) - 25))

    if not missed:
        print("Every row that carries questions is findable by at least one of them.")

    return 1 if (strict and missed) else 0


if __name__ == "__main__":
    sys.exit(main())
