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

AND THE SAME RULE, IN THE DOCUMENTS A READER READS

FIX-31 wrote a paragraph into THE-PROJECT.md part 11 and found the section beside it
saying "598 resources" when there were fewer, with picks and publisher figures two rounds
old. Every one of those was covered by the CLAUDE.md rule from August - numbers a reader
will read are generated or measured, never typed - and no check had ever looked at `docs/`.
A rule with no gate behind it is the same shape as the pipe that hid every gate in
build.sh, and this is the other half of it.

So the check reaches THE-PROJECT.md, README.md, START-HERE.md and docs/specs/. The test
there is different from the picks test, and it is FIX-32's wording:

    A count on a line that carries a month or a year is history, and passes.
    A count on a line without one is a live claim, and fails.

"353 resources in August 2026" is a record of what was true then and stays true forever.
"353 resources" is a promise about now that nothing regenerates. The fix is never to
update the number - that only restarts the clock - it is to point at STATUS.md, which the
build writes.

The round records under docs/attack/ are outside this. They are dated by construction: a
FIX-NN file is a record of one round, read as history by anyone who opens it, and freezing
their numbers is the whole point of keeping them.
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
    # The bare count, with no anchor at all: "Two candidates cover this exact subject".
    # Missed by everything above, and found by the stale-cell re-read instead.
    re.compile(r"\b%s\b[\w -]{0,24}?%s\b" % (NUM, POOL), re.I),
]


# "fifteen minutes in the pool" is a duration standing next to a pool word, not a count of
# the pool. The resource's own numbers stay - see the header.
DURATION = re.compile(r"\b(minutes?|hours?|days?|weeks?|months?|years?|min\b)", re.I)


def offences(text):
    out = []
    for rx in PATTERNS:
        for m in rx.finditer(text or ""):
            frag = m.group(0)
            if DURATION.search(frag):
                continue
            if frag not in out:
                out.append(frag)
    return out


# --- the documents a reader reads -------------------------------------------------

DOCS = ["docs/THE-PROJECT.md", "README.md", "docs/START-HERE.md"]
DOC_GLOBS = ["docs/specs/*.md"]

# What the catalogue counts. A number beside one of these words is a claim about the
# data; a number beside anything else is about the world and is none of this check's
# business.
# Deliberately narrower than "every noun with a number in front of it", and the
# narrowing is a judgement worth arguing with. These are the quantities the build
# MEASURES and writes into STATUS.md, so a typed one goes stale the next time the data
# moves. The site's fixed vocabulary is left out on purpose - "four levels", "ten roles",
# "the two front-door questions", "four tiers" are design facts, not measurements, and a
# check that demanded a date beside "four levels" would be teaching people to ignore it.
# If one of those ever becomes a live claim it should be caught by reading, not here.
COUNTED = (r"resources?|rows?|entries|publishers?|hosts?|cells?|picks?|paths?|"
           r"steps?|links?|cards?")
# (?<![\w-]) so that the 30 in "FIX-30" and the 27 in "FIX-27" are not read as
# counts. A round name is not a quantity, and the first run flagged two of them.
DOC_CLAIM = re.compile(r"(?<![\w-])(?:%s|\d[\d,]*)\s+(?:\w+\s+){0,2}?(?:%s)\b"
                       % (WORD, COUNTED), re.I)
# A line that names when it was true is history. Months, years, and the ISO dates the
# project writes everywhere.
DATED = re.compile(r"\b(?:january|february|march|april|may|june|july|august|september|"
                   r"october|november|december|20\d\d)\b", re.I)
# Anything inside backticks is a path, a field name, a command or a code fragment.
CODE = re.compile(r"`[^`]*`")
FENCE = re.compile(r"^\s*(```|~~~)")
# A markdown table row of generated figures is how STATUS.md itself is written; a doc that
# quotes one is quoting the generated file rather than typing a claim.
TABLE = re.compile(r"^\s*\|")


def doc_files():
    import glob
    out = [os.path.join(ROOT, p) for p in DOCS]
    for g in DOC_GLOBS:
        out.extend(sorted(glob.glob(os.path.join(ROOT, g))))
    return [p for p in out if os.path.exists(p)]


def doc_offences(path):
    """Every live count in one file: (line number, the line, what was matched)."""
    out = []
    infence = False
    for n, raw in enumerate(io.open(path, encoding="utf-8"), 1):
        if FENCE.match(raw):
            infence = not infence
            continue
        if infence or TABLE.match(raw) or DATED.search(raw):
            continue
        line = CODE.sub(" ", raw)
        hits = [m.group(0).strip() for m in DOC_CLAIM.finditer(line)]
        if hits:
            out.append((n, raw.strip(), hits))
    return out


def check_docs():
    bad, read = [], 0
    for path in doc_files():
        read += 1
        for n, line, hits in doc_offences(path):
            bad.append((os.path.relpath(path, ROOT).replace("\\", "/"), n, line, hits))
    print("Typed numbers in the documents: %d file(s) read." % read)
    if not bad:
        print("No live count typed into a document a reader reads.")
        return 0
    print()
    for rel, n, line, hits in bad:
        print("%s:%d" % (rel, n))
        print("   counts: %s" % " | ".join(hits))
        print("   %s" % line[:150])
        print()
    print("%d line(s) state a count with no date beside it, which reads as a claim about "
          "now." % len(bad))
    print("Point at docs/STATUS.md, or say when it was true. See this file's header.")
    return 1


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
        return check_docs()

    print()
    for key, kind, url, hits, reason in bad:
        print("%-28s %-10s %s" % (key, kind, url[-46:]))
        print("   counts: %s" % " | ".join(hits))
        print("   %s" % reason[:220])
        print()
    print("%d reason(s) count a pool that will move without them." % len(bad))
    print("State the comparison, not the count. See this file's header.")
    check_docs()
    return 1


if __name__ == "__main__":
    sys.exit(main())
