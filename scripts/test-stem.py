#!/usr/bin/env python3
"""
The stemmer's unit test: every word family the five causes need.

    python3 scripts/test-stem.py

The families are taken from the failing lines of `scripts/test-search.py`, not invented.
Each one is a group that must reach a single stem, with the query it comes from named, so
a rule change that breaks a family says which visitor it breaks it for.

The second half is as important as the first: pairs that must NOT collapse. A stemmer with
a minimum stem of 3 merges aggressively, and a test that only checks merging will happily
approve one that maps everything to a single letter.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stem import stem  # noqa: E402

# (the query this comes from, the words that must reach one stem)
FAMILIES = [
    ("does claude make up citations / hallucinations",
     ["hallucination", "hallucinations", "hallucinated", "hallucinate", "hallucinating"]),
    ("how do i cite claude in my references",
     ["citation", "citations", "cite", "cited", "citing"]),
    ("prioritisation / prioritization",
     ["prioritise", "prioritize", "prioritisation", "prioritization"]),
    ("marking essays / grading",
     ["grade", "grades", "grading", "graded"]),
    ("marking essays",
     ["mark", "marks", "marking", "marked"]),
    ("stop claude inventing pixel values",
     ["invent", "invents", "inventing", "invented", "invention"]),
    ("is it cheating to use claude for my essay",
     ["cheat", "cheats", "cheating", "cheated"]),
    ("write emails for me / keep my own voice",
     ["write", "writes", "writing", "wrote", "written"]),
    ("systematic literature review",
     ["review", "reviews", "reviewing", "reviewed"]),
    ("make a lesson plan",
     ["make", "makes", "making", "made"]),
]

# NOT here: analyse/analyze. The -ise/-ize rule in the stemmer catches the verb suffix
# (prioritise), but "analyse" ends in -yse, which is a British spelling rather than a
# suffix, and no stemming rule should be asked to know that. It belongs to the
# spelling-pairs step and its test lives there.

# Words that must stay apart. Different meanings, similar shapes.
MUST_DIFFER = [
    ("claude", "cloud"),
    ("prompt", "promote"),
    ("skill", "skim"),
    ("agent", "agenda"),
    ("teach", "team"),
    ("cost", "course"),
]


def main():
    failures = []
    for query, family in FAMILIES:
        stems = {w: stem(w) for w in family}
        distinct = set(stems.values())
        if len(distinct) == 1:
            print("  ok    %-46s -> %s" % (family[0] + " family", distinct.pop()))
        else:
            failures.append((query, stems))
            print("  FAIL  %-46s -> %d stems" % (family[0] + " family", len(distinct)))

    for a, b in MUST_DIFFER:
        if stem(a) == stem(b):
            failures.append(("%s / %s must stay apart" % (a, b),
                             {a: stem(a), b: stem(b)}))
            print("  FAIL  %-20s and %-20s both -> %s" % (a, b, stem(a)))
        else:
            print("  ok    %-20s /= %-20s (%s /= %s)" % (a, b, stem(a), stem(b)))

    print()
    if failures:
        print("%d stemmer fault(s):" % len(failures))
        for what, stems in failures:
            print("  %s" % what)
            for w, s in sorted(stems.items()):
                print("      %-18s -> %s" % (w, s))
        return 1
    print("%d families collapse, %d pairs stay apart."
          % (len(FAMILIES), len(MUST_DIFFER)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
