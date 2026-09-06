#!/usr/bin/env python3
"""
Which bucket a card falls into, tested on the sentences that were getting it wrong.

    python3 scripts/test-role-buckets.py

Rule B routes every card to one of four places, and one of them ends in the row being
removed. The routing is done by regular expressions over a sentence somebody wrote by hand,
which is exactly the kind of code that is right until it meets a sentence nobody imagined.

The three situation examples are Morteza's own, from FIX-29's ruling 2: "complete
beginners", "someone who has just been cut off", "anyone about to trust Claude". None of
them names a job, all three describe a state a reader is in, and none may be routed towards
removal. The attributive pair is the same fault in a different shape - "patient data" is
what the work is about, not who it is for.

The occupation half of the test matters as much: a guard loose enough to call everything a
situation would pass the first half and quietly stop the sweep working at all.
"""

import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location(
    "rb", os.path.join(ROOT, "scripts", "audit-role-tags.py"))
rb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rb)


def bucket(who):
    """Where Rule B would send a card with this who_for and no role words in it."""
    if not who or rb.NEUTRAL.match(who):
        return "neutral"
    named = {r for r, rx in rb.ROLE_WORDS.items() if rx.search(who)}
    if named:
        return "names a role: " + ",".join(sorted(named))
    plain = rb.ATTRIBUTIVE.sub(" ", who)
    if rb.SITUATION.search(who):
        return "neutral"
    jobs = [f for f, rx in rb.OFF.items() if rx.search(plain)]
    return ("off-roster: " + "/".join(jobs)) if jobs else "neutral"


SITUATIONS = [
    "Complete beginners who have never opened Claude and want a calm walkthrough.",
    "Someone who has just been cut off mid-task and wants to know what the limits are.",
    "Anyone about to trust Claude with patient data for the first time.",
    "A first-timer with no experience of AI tools who wants one honest hour.",
    "Anyone who keeps re-pasting the same background into new chats.",
]

ATTRIBUTIVE = [
    "A researcher checking clinician notes for consistency before publishing.",
    "Anyone summarising patient records who needs the summary checked.",
]

OCCUPATIONS = [
    ("Payer clinical reviewers wanting a starting point.", "off-roster"),
    ("In-house counsel triaging a high volume of standard NDAs.", "off-roster"),
    ("Account executives preparing for a first call.", "off-roster"),
    ("Regulatory affairs staff at a pharma company.", "off-roster"),
    ("A product manager writing a PRD from a problem statement.", "names a role"),
    ("School teachers with no computer-science background.", "names a role"),
]


def main():
    failures = []
    for who in SITUATIONS:
        b = bucket(who)
        if b != "neutral":
            failures.append((who, b, "a situation must not fire"))
            print("  FAIL  %-62s -> %s" % (who[:62], b))
        else:
            print("  ok    situation stays neutral: %s" % who[:52])
    for who in ATTRIBUTIVE:
        b = bucket(who)
        if b.startswith("off-roster"):
            failures.append((who, b, "an attributive job word is subject matter"))
            print("  FAIL  %-62s -> %s" % (who[:62], b))
        else:
            print("  ok    attributive stays out of Rule C: %s" % who[:46])
    for who, want in OCCUPATIONS:
        b = bucket(who)
        if not b.startswith(want):
            failures.append((who, b, "expected %s" % want))
            print("  FAIL  %-62s -> %s" % (who[:62], b))
        else:
            print("  ok    %-46s -> %s" % (who[:46], b))

    print()
    if failures:
        print("%d routing fault(s):" % len(failures))
        for who, got, why in failures:
            print("  %r" % who)
            print("      went to %r; %s" % (got, why))
        return 1
    print("%d situations, %d attributive uses and %d occupations all routed correctly."
          % (len(SITUATIONS), len(ATTRIBUTIVE), len(OCCUPATIONS)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
