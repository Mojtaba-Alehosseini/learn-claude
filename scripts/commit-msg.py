#!/usr/bin/env python3
"""
A commit message describes the job. Counts live in the round record.

Installed as .git/hooks/commit-msg by scripts/install-hooks.py.

WHY THIS EXISTS

CLAUDE.md has said since August that numbers a reader will read are generated or measured,
never typed, and it names commit messages in the sentence. Three rounds broke it in a row,
every time in prose about measurement:

  FIX-26  "Forty rows changed tags, twenty-three had their cards rewritten" - measured 15
          and 18.
  FIX-27  the round report said the rebuild moved +12; on the same footing it was +3.
  FIX-28  "two of the five agents' answers are still in the top three" - it was four.

Each was caught before pushing, twice by amending, which means the discipline was working
and the habit was not. A number in a commit message is written from memory a minute after
the measurement, it is never regenerated, and nothing downstream reads it. The round record
and STATUS.md are both generated from the data, so that is where a count belongs.

WHAT IS REJECTED

A number standing next to a word for a thing this repository counts: rows, queries, items,
cells, picks, resources, files, checks, and the "N of M" shape. Both digits and the words
for them, because "twenty-three had their cards rewritten" is the same lie as "23 had".

WHAT PASSES

Dates, version numbers, commit hashes, ids like r-4f2a9c, weights and thresholds
(`weight 1.5`, `0.5`), section and step numbers, ticket and round names (FIX-29, D9),
percentages of a rate rather than a count, and prose with no number in it at all.

Nothing here stops a person writing a number they have measured into the round record,
which is the point: put it where it will be re-derived next time somebody builds.
"""

import io
import os
import re
import sys

WORDS = (r"one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|"
         r"fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|"
         r"fifty|sixty|seventy|eighty|ninety|hundred")
NUM = r"(?:%s|\d[\d,]*)" % WORDS

# The nouns this repository counts. A number beside one of these is a measurement being
# retyped from memory.
COUNTED = (r"rows?|quer(?:y|ies)|items?|cells?|picks?|runners?-up|resources?|files?|"
           r"checks?|tests?|entries|entry|records?|candidates?|pages?|words?|synonyms?|"
           r"stems?|failures?|faults?|gaps?|removals?|trims?|rewrites?|tags?|steps?")

PATTERNS = [
    # "23 rows", "twenty-three rows", "26 cells closed"
    re.compile(r"\b%s\s+(?:[a-z-]+\s+){0,2}(?:%s)\b" % (NUM, COUNTED), re.I),
    # "rows: 23", "queries — 12"
    re.compile(r"\b(?:%s)\b[^\n]{0,3}[:—-]\s*%s\b" % (COUNTED, NUM), re.I),
    # "35 of 57", "four of the five"
    re.compile(r"\b%s\s+of\s+(?:the\s+)?%s\b" % (NUM, NUM), re.I),
    # "suite 22 -> 24"
    re.compile(r"\b%s\s*(?:->|→)\s*%s\b" % (NUM, NUM)),
]

# Anything that looks like a count but is not one.
EXEMPT = re.compile(
    r"20\d\d-\d\d-\d\d"          # dates
    r"|\b20\d\d\b"               # years
    r"|\bFIX-\d+\b|\bD\d+\b|\bR\d+\b"   # round and ruling names
    r"|\br-[0-9a-f]{6,}\b"       # item ids
    r"|\b[0-9a-f]{7,40}\b"       # commit hashes
    r"|\bstep \d+\b|\bsection \d+\b|\bpart \d+\b|\bphase \d+\b"
    r"|\bweight[s]? \d"          # weights and thresholds
    r"|\bv?\d+\.\d+"             # versions, 1.5, 0.001
    r"|\bclaude \d", re.I)


def offences(text):
    out = []
    for line in text.split("\n"):
        if line.startswith("#"):
            continue                      # git's own comment lines
        stripped = EXEMPT.sub(" ", line)
        for rx in PATTERNS:
            for m in rx.finditer(stripped):
                frag = m.group(0).strip()
                if frag not in out:
                    out.append(frag)
    return out


def main():
    if len(sys.argv) < 2:
        print("commit-msg: no message file given", file=sys.stderr)
        return 1
    path = sys.argv[1]
    with io.open(path, encoding="utf-8") as f:
        text = f.read()
    if os.environ.get("LC_ALLOW_COUNTS"):
        print("commit-msg: counts allowed by LC_ALLOW_COUNTS for this commit.")
        return 0
    hits = offences(text)
    if not hits:
        print("commit-msg: no counts in the message.")
        return 0
    print("commit-msg: this message states a count.", file=sys.stderr)
    for h in hits:
        print("    %r" % h, file=sys.stderr)
    print("", file=sys.stderr)
    print("Commit messages describe the job. Counts live in the round record and in", file=sys.stderr)
    print("docs/STATUS.md, both generated from the data - a number typed here is written", file=sys.stderr)
    print("from memory, never regenerated, and read by nothing.", file=sys.stderr)
    print("", file=sys.stderr)
    print("Rewrite the sentence, or set LC_ALLOW_COUNTS=1 for a count that genuinely", file=sys.stderr)
    print("belongs in history and cannot be generated.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
