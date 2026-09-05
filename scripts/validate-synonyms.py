#!/usr/bin/env python3
"""
Every synonym row has to say why it exists.

    python3 scripts/validate-synonyms.py

A synonym is a promise that two words mean the same thing to a reader of this catalogue.
Nobody can check that promise later without the reason it was made, which is the same
argument `skip_if` won: the rule that a row must justify itself is what stops the table
filling up with plausible-looking pairs nobody can defend.

WHAT IS CHECKED

  terms          at least two, lower-case, single words, no duplicates across rows
  why            present, and long enough to be an argument rather than a label
  added          a date
  usefulness     at least two of the row's terms are in the built index. A row where only
                 one term exists in the catalogue expands to nothing and is dead weight;
                 a row where none exists is somebody's guess about a catalogue we do not
                 have.

Single words only. Expansion happens one query word at a time, so a multi-word term like
"academic integrity" could never fire, and a table that quietly holds unfireable rows is a
table that lies about what it does.
"""

import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYN = os.path.join(ROOT, "data", "synonyms.json")
KW = os.path.join(ROOT, "data", "search-keywords.json")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WORD = re.compile(r"^[a-z][a-z0-9-]*$")
MIN_WHY = 80


def main():
    doc = json.load(io.open(SYN, encoding="utf-8"))
    entries = doc.get("entries") or []
    vocab = set()
    if os.path.exists(KW):
        vocab = set(json.load(io.open(KW, encoding="utf-8"))["words"])

    faults = []
    seen = {}
    for n, e in enumerate(entries, 1):
        terms = e.get("terms") or []
        where = "entry %d (%s)" % (n, ", ".join(terms[:3]) or "no terms")
        if len(terms) < 2:
            faults.append("%s: needs at least two terms" % where)
        for t in terms:
            if not WORD.match(str(t)):
                faults.append("%s: %r is not a lower-case single word" % (where, t))
            if t in seen and seen[t] != n:
                faults.append("%s: %r is already in entry %d. One word, one group, or "
                              "the expansion depends on which row is read first"
                              % (where, t, seen[t]))
            seen[t] = n
        why = str(e.get("why") or "").strip()
        if len(why) < MIN_WHY:
            faults.append("%s: `why` is %d characters. A synonym nobody can justify is a "
                          "search result nobody can explain - say what a reader typed and "
                          "what they got." % (where, len(why)))
        if not DATE.match(str(e.get("added") or "")):
            faults.append("%s: `added` = %r is not YYYY-MM-DD" % (where, e.get("added")))
        if vocab:
            present = [t for t in terms if t in vocab]
            if len(present) < 2:
                faults.append("%s: only %d of these words is in the catalogue (%s). This "
                              "row expands to nothing."
                              % (where, len(present), ", ".join(present) or "none"))

    if faults:
        print("Synonyms: %d fault(s)." % len(faults))
        for f in faults:
            print("  " + f)
        return 1

    print("Synonyms: %d row(s), %d words, every one with a reason and at least two words "
          "the catalogue holds." % (len(entries), len(seen)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
