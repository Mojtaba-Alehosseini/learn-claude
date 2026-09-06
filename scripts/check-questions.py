#!/usr/bin/env python3
"""
No suite query may appear in a resource's questions[].

    python3 scripts/check-questions.py

`questions[]` is the highest-weighted field in the search index, and the suite is how the
site's search is judged. Writing a suite query into a row's questions is not a fix, it is
a pass bought with the answer sheet - and it would be invisible in the number, which is the
worst shape a mistake can have here.

WHAT IS COMPARED

Not raw strings. Case, punctuation, apostrophes and repeated spaces are stripped from both
sides before comparing, because retyping "is it cheating to use claude for my essay" as
"Is it cheating to use Claude for my essay?" is the same act with a capital letter.

Near-misses are printed as a warning rather than an error: a question sharing every
significant word with a suite query, in any order, is worth a person's eye. It is not
automatically wrong - a reader really might type both - but it is where copying would hide.

WHAT THIS DOES NOT CHECK

Whether the questions are any good. A validator cannot tell "how do i stop repeating the
same background every time" from "what is claude projects"; only reading them can, which
is why the rewrite has a checkpoint that a person reads.
"""

import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITEMS = os.path.join(ROOT, "data", "items.json")
SUITE_FILE = os.path.join(ROOT, "scripts", "test-search.py")

STOP = set("a an and are as at be but by can do does for from get go had has have how i "
           "if in into is it its me my not of on or our so than that the their them then "
           "there these this to up us was we were what when where which who why will with "
           "you your".split())


def flatten(s):
    s = str(s).lower().replace("’", "'")
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return " ".join(s.split())


def significant(s):
    return frozenset(w for w in flatten(s).split() if w not in STOP and len(w) > 2)


def suite_queries():
    """Read the queries out of the suite without importing it - importing runs its loader,
    and this check has to work on a repository whose index is mid-rebuild."""
    text = io.open(SUITE_FILE, encoding="utf-8").read()
    body = text[text.index("SUITE = ["):]
    return re.findall(r'^\s*\("[a-z-]+",\s*"([^"]+)"', body, re.M)


def main():
    items = json.load(io.open(ITEMS, encoding="utf-8"))
    queries = suite_queries()
    exact = {flatten(q): q for q in queries}
    bysig = {}
    for q in queries:
        sig = significant(q)
        if len(sig) > 1:             # one shared word is a coincidence, not a copy:
            bysig.setdefault(sig, []).append(q)   # "claude.md" and "what can claude do
                                                  # for hr" both reduce to {claude}

    faults, warnings = [], []
    n = 0
    for x in items:
        for q in x.get("questions") or []:
            n += 1
            f = flatten(q)
            if f in exact:
                faults.append((x["title"], q, exact[f]))
                continue
            sig = significant(q)
            if len(sig) > 1 and sig in bysig:
                warnings.append((x["title"], q, bysig[sig][0]))

    if faults:
        print("Questions: %d fault(s)." % len(faults))
        for title, q, query in faults:
            print("  %s" % title[:64])
            print("      question %r" % q)
            print("      is the suite query %r" % query)
        print()
        print("A pass earned by writing the test into the data is not a pass. Rewrite the")
        print("question in the words a reader would use, or delete it.")
        return 1

    print("Questions: %d read across the catalogue, none is a suite query." % n)
    if warnings:
        print("%d share every significant word with one, which is worth a look:"
              % len(warnings))
        for title, q, query in warnings[:8]:
            print("  %-44s %r ~ %r" % (title[:44], q, query))
    return 0


if __name__ == "__main__":
    sys.exit(main())
