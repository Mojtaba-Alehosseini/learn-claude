#!/usr/bin/env python3
"""
Cards whose own prose states a duration the time chip disagrees with.

    python3 scripts/audit-time-chips.py

Advisory. Prints and never fails a build, like the copy-openings report and the pick
contradiction audit, for the same reason: a build that goes red on a judgement call
teaches people to edit the judgement until it is green.

WHY
---
The no-typed-numbers rule already covers docs, path intros, UI strings and commit
messages. It did not cover the catalogue, and Attack 2 found the gap three times over -
the sharpest being a card whose chip says "half a day" and whose own Skip if, forty
pixels below, says "at 15 minutes across 13 short lectures, this is a primer". Filter to
"15 min" and the fifteen-minute course disappears; filter to "half a day" and you get a
primer. Three agents found it independently.

WHAT IT COMPARES
----------------
The chip is a bucket, not a duration - `LC.TIME` renders four labels and nothing finer.
So this does not demand the prose match a number; it asks whether the stated duration
could reasonably wear the label a reader sees:

    15 min        up to 15 minutes
    1 hour        15 to 60 minutes
    half a day    1 to 7 hours
    several days  over 7 hours

Rounding is up, which is the site's rule everywhere: a ninety-minute course wears "half a
day" and that is right. A card is flagged only when its own words put it in a LOWER bucket
than its chip - when the chip oversells the commitment, which is the case that hides a
fifteen-minute course from someone filtering for fifteen minutes.

WHAT THE 2026-09-05 RUN FOUND
-----------------------------
Eight flags. One real:

    AI capabilities and limitations (r-59f8585925) - chip "half a day", skip_if "at 15
    minutes across 13 short lectures". Its own notes record five hours read off the page
    and the bucket moved for that reason. The chip was right; the sentence was the
    leftover guess. Three Attack 2 agents read the sentence and filed the chip. Fixed.

Seven judged and left alone, written down rather than tuned away - no rule catches these
without also catching a real one, and quietening a checker is how this catalogue would
lose the next real fault:

    r-d248774363  Maven PM course. "5 hours live plus 5 hours projects PER WEEK", over
                  several weeks. multi-day is right.
    r-e3ed1d9671  Academic Research seminar. The words "half-day" appear inside a note
                  explaining why the bucket MOVED from half-day to multi-day.
    r-5ef57a95ef  AI Fluency for Educators. "About 3 hours including roughly 35 minutes
                  of video" - the 35 minutes is the video inside the three hours.
    r-9d3aadf6a3  Claude Code for Beginners. Four and a half hours total; the flagged
                  number is a part of it.
    r-c05fa5a028  FULL Claude Tutorial. "You only have ten minutes" is a condition on
                  the reader, not a length.
    r-143f1aa35d  FULL Claude Tutorial (FULL COURSE). "The first half hour will be
                  familiar" - a part of an almost-two-hour course.
    r-fce9525592  SOX & controls. The PAGE contradicts itself: its chip says 10 minutes
                  and its subtitle says under an hour. The card records both deliberately
                  and rounds up. That is the rule working, not failing.
"""

import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIELDS = ("summary", "skip_if", "who_for", "notes")

LABEL = {"under-15min": "15 min", "under-1hr": "1 hour",
         "half-day": "half a day", "multi-day": "several days"}

# The buckets as the site actually uses them. Rounding is UP, always: anything over an
# hour is "half a day" rather than "1 hour", because the site would rather overstate a
# commitment than understate it. So a ninety-minute course wearing "half a day" is
# correct and is not a fault - my first cut had that band starting at two hours and
# flagged nine cards that were right.
#
# The deliberate exception stays unflagged too: "Teaching AI Fluency" is half-day and its
# notes say five to six hours, because "several days" would overstate by more than
# "half a day" understates. RUN-LOG-2 unit 3 has the reasoning.
BAND = {"under-15min": (0, 15),
        "under-1hr": (15, 60),
        "half-day": (60, 420),
        "multi-day": (420, 10 ** 6)}

WORD = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
        "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "fifteen": 15,
        "twenty": 20, "thirty": 30, "forty": 40, "forty-five": 45, "fifty": 50,
        "sixty": 60, "ninety": 90, "half": 0.5}

# Boundaries at both ends, and the bare "a"/"an" dropped. Without the left boundary
# "twenty-three minutes" matched as "three minutes" and "thirty-two minutes" as "two
# minutes", so three cards that were already right were reported as faults; without
# the right one the bare "a" matched inside "examine" and reported one minute.
# \b alone was not enough on the left: a hyphen is itself a word boundary, so
# "twenty-three" still offered "three" to the match. The lookbehind refuses a
# preceding hyphen as well, which reads a compound number as one number or not at
# all.
NUM = r"(?<![-\w])(\d+(?:\.\d+)?|one|two|three|four|five|six|seven|eight|nine|ten|eleven|" \
      r"twelve|fifteen|twenty|thirty|forty|forty-five|fifty|sixty|ninety|half)\b"
MIN_RE = re.compile(NUM + r"[\s-]*(?:guided\s+)?(?:minute|min\b)", re.I)
HOUR_RE = re.compile(NUM + r"[\s-]*(?:guided\s+)?(?:hour|hr\b)", re.I)
DAY_RE = re.compile(NUM + r"[\s-]*(?:full[\s-]*)?day", re.I)


def value(tok):
    tok = tok.lower()
    try:
        return float(tok)
    except ValueError:
        return WORD.get(tok)


# "four and a half hours" is one number. Without this the match lands on "half hours"
# and reports thirty minutes for a four-and-a-half-hour course.
HALF = re.compile(r"\b(\d+|one|two|three|four|five|six|seven|eight|nine|ten)"
                  r"\s+and\s+a\s+half\s+(hour|hr)", re.I)


def durations(text):
    """Every duration the prose states, in minutes, with its surrounding sentence."""
    def _whole(m):
        n = value(m.group(1))
        return "%s hours" % (n + 0.5) if n else m.group(0)
    text = HALF.sub(_whole, text)
    out = []
    for rx, mult in ((MIN_RE, 1), (HOUR_RE, 60), (DAY_RE, 60 * 6)):
        for m in rx.finditer(text):
            v = value(m.group(1))
            if v:
                lo = max(0, m.start() - 70)
                out.append((v * mult, m.group(0).strip(), text[lo:m.end() + 40]))
    return out


def main():
    with io.open(os.path.join(ROOT, "data", "items.json"), encoding="utf-8") as f:
        items = json.load(f)

    flagged = []
    for it in items:
        band = BAND.get(it.get("time"))
        if not band:
            continue
        text = " ".join(str(it.get(f) or "") for f in FIELDS)
        outside = []
        for m, phrase, where in durations(text):
            if m < band[0]:
                # The card says it is SHORTER than the chip claims. This is the whole
                # finding: filter to "15 min" and a fifteen-minute course disappears
                # because its chip reads "half a day".
                outside.append((m, phrase, "shorter than the chip"))
            # The other direction - a five-hour course chipped "1 hour" - is real too and
            # is NOT attempted here. Catalogue prose is full of durations that belong to
            # the subject rather than the resource: a 90-day plan, a 24-hour message
            # sweep, the five-hour usage window. Nothing short of reading the sentence
            # tells those apart, and a run of 50 flags with 3 real ones is an advisory
            # nobody reads twice. Under-claiming here is deliberate.
        if outside:
            flagged.append((it, outside))

    for it, outside in flagged:
        print("\n%s" % it["title"][:78])
        print("  id %s   chip %r (%s)" % (it["id"], LABEL[it["time"]], it["time"]))
        for m, phrase, why in outside:
            print("  its own words say %-20r = %-5d min  (%s)"
                  % (phrase, int(m), why))

    print()
    print("%d card(s) whose prose and chip disagree." % len(flagged))
    return 0


if __name__ == "__main__":
    sys.exit(main())
