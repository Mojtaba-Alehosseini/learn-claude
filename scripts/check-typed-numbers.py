#!/usr/bin/env python3
"""
A pick's reason may not count its own pool.

    python3 scripts/check-typed-numbers.py          # fail on any counted pool claim

WHY THIS EXISTS

CLAUDE.md has said since August that numbers a reader will read are generated or
measured, never typed. `picks.json` was outside every check that enforced it, and a pick's
reason is read on the card by every visitor to that cell.

FIX-25 found what that cost. Eleven reasons counted a pool that had moved underneath them:
"the only candidate of 78" in a pool of fourteen, "thirty of thirty-three candidates run
one predefined workflow" where the answer was nought of fourteen, and - worst - "every
safety candidate in this pool is Anthropic Academy's" when four different publishers had
one. Each was true on the day it was written. Rules A, B and C moved the pools and the
sentences stayed.

WHY REMOVAL RATHER THAN RE-MEASUREMENT

A reason is prose. There is no honest way to regenerate "four of the ten candidates are
about Claude Design" at build time, because the clause it sits in was written around that
number. The choice is a number that rots or an argument that does not, and the argument
was always the point:

    "the only one not tied to a single publisher"     is a reason.
    "the only one of 78"                              is a number that rots.

So: state the comparison, not the count. Where a quantity is genuinely load-bearing, say
it in words that stay true as the pool moves - "most of this pool", "everything else
here" - or move the number to the notes, which no reader sees on a card.

WHAT COUNTS AS A COUNTED POOL CLAIM

A quantity sitting next to a word for the pool: candidates, this pool, the pool, these N,
of N. Durations, prices, dates, model versions, path step numbers and counts that describe
the resource itself ("forty-three worked answers", "a 4.1 rating from 33 reviews") are
about the world rather than the pool, and they stay.
"""

import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PICKS = os.path.join(ROOT, "data", "picks.json")

# "one" is missing on purpose. "The pool's one candidate that hands you the thing" is a
# uniqueness claim, not a count: it says this row is unlike the others, and it stays true
# or false on what arrives, not on how many. Those are instrument 2's - every stale event
# lists the reasons containing only/every/all/none/the one, and the re-pick cannot close
# the cell until each has been re-read. Banning them here would only push the same claim
# into the word "only".
WORD = (r"two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|"
        r"fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|"
        r"fifty|sixty|seventy|eighty|ninety|hundred")
NUM = r"(?:%s|\d+)" % WORD
POOL = r"(?:candidates?|pool|publishers?|pages?|videos?|servers?|courses?|tours?)"

# A number that quantifies the pool, in the three shapes the catalogue actually writes:
#   "four of the ten candidates"      NUM ... of ... NUM? ... POOL
#   "Six MCP servers sit in this pool"  NUM ... POOL ... in this/the pool
#   "the only candidate of 65"        POOL ... of NUM
PATTERNS = [
    re.compile(r"\b%s\b(?:\s+of\s+(?:the\s+|these\s+)?)(?:%s\s+)?%s\b" % (NUM, NUM, POOL),
               re.I),
    re.compile(r"\b%s\b[^.]{0,40}?%s\b[^.]{0,30}?\bin (?:this|the) pool\b" % (NUM, POOL),
               re.I),
    re.compile(r"\b%s\b[^.]{0,24}?\b%s\b\s+(?:here|in this pool|in the pool)" % (NUM, POOL),
               re.I),
    re.compile(r"\b%s\b\s+of\s+%s\b" % (POOL, NUM), re.I),
    re.compile(r"\bthe pool's %s\b" % NUM, re.I),
]


def offences(text):
    out = []
    for rx in PATTERNS:
        for m in rx.finditer(text or ""):
            frag = m.group(0)
            if frag not in out:
                out.append(frag)
    return out


def main():
    cells = json.load(io.open(PICKS, encoding="utf-8"))["cells"]
    bad = []
    lines = 0
    for key in sorted(cells):
        for kind in ("picks", "runners_up"):
            for p in cells[key].get(kind) or []:
                lines += 1
                hits = offences(p.get("reason"))
                if hits:
                    bad.append((key, kind, p["url"], hits, p["reason"]))

    print("Typed numbers: %d reason line(s) read." % lines)
    if not bad:
        print("No reason counts its own pool.")
        return 0

    print()
    for key, kind, url, hits, reason in bad:
        print("%-28s %-10s %s" % (key, kind, url[-46:]))
        print("   counts: %s" % " | ".join(hits))
        print("   %s" % reason[:220])
        print()
    print("%d reason(s) count a pool that will move without them." % len(bad))
    print("State the comparison, not the count. See this file's header.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
