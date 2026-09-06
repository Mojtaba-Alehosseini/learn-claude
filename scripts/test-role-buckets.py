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

# The shadow the FIX-29 lookbehinds left. Each of these cards is real, each names its
# reader plainly to a person, and after the lookbehinds landed the patterns read every one
# of them as naming nobody - which is the leave-alone bucket, so nothing on the site went
# wrong and nothing said anything either. FIX-30 found them by re-running the rescue
# branch. Four are situations: a card that says which job it is not for has not said which
# job it is for. The fifth names a job, and the hyphen was hiding it.
BLINDED_SITUATIONS = [
    "Non-developers whose work sits in folders of documents and spreadsheets instead of "
    "in a chat window.",
    "Non-coders deciding whether Cowork is worth switching to, who want to see failure "
    "modes as well as demos.",
    "Non-developers who want real prompting technique without any API or code talk.",
    "Non-developers who want prompt templates and a folder setup they can copy today.",
]

BLINDED_ROLES = [
    ("Design-system owners who want Claude to respect their system consistently.",
     "designer"),
]

# And the matches those fixes must not bring back. A lookbehind that stops working is how
# this started.
STILL_BLOCKED = [
    ("Non-developers whose work sits in folders of documents and spreadsheets.",
     "developer"),
    ("Non-coders deciding whether Cowork is worth switching to.", "developer"),
    ("Medical coders, billers, and prior authorization specialists.", "developer"),
    ("Design-system owners who want Claude to respect their system.", "business-founder"),
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

    for who in BLINDED_SITUATIONS:
        b = bucket(who)
        if b != "neutral":
            failures.append((who, b, "not-a-developer is a state, not a job"))
            print("  FAIL  %-62s -> %s" % (who[:62], b))
        else:
            print("  ok    stays a situation: %s" % who[:52])
    for who, want in BLINDED_ROLES:
        named = {r for r, rx in rb.ROLE_WORDS.items() if rx.search(who)}
        if want not in named:
            failures.append((who, ",".join(sorted(named)) or "(nobody)",
                             "must name %s" % want))
            print("  FAIL  %-62s names %s"
                  % (who[:62], ",".join(sorted(named)) or "(nobody)"))
        else:
            print("  ok    names %-12s %s" % (want, who[:46]))
    for who, blocked in STILL_BLOCKED:
        named = {r for r, rx in rb.ROLE_WORDS.items() if rx.search(who)}
        if blocked in named:
            failures.append((who, blocked, "must NOT name %s" % blocked))
            print("  FAIL  %-62s still names %s" % (who[:62], blocked))
        else:
            print("  ok    never %-11s %s" % (blocked, who[:46]))

    print()
    if failures:
        print("%d routing fault(s):" % len(failures))
        for who, got, why in failures:
            print("  %r" % who)
            print("      went to %r; %s" % (got, why))
        return 1
    print("%d situations, %d attributive uses, %d occupations, %d cards the lookbehinds "
          "had blinded and %d matches that must stay blocked, all correct."
          % (len(SITUATIONS) + len(BLINDED_SITUATIONS), len(ATTRIBUTIVE),
             len(OCCUPATIONS) + len(BLINDED_ROLES), len(BLINDED_SITUATIONS)
             + len(BLINDED_ROLES), len(STILL_BLOCKED)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
