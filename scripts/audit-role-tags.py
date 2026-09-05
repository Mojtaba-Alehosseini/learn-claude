#!/usr/bin/env python3
"""
Rule B: does the card support each role tag it carries?

    python3 scripts/audit-role-tags.py                  # what would change
    python3 scripts/audit-role-tags.py --apply          # drop the tags the card denies
    python3 scripts/audit-role-tags.py --gallery-only   # limit to the use-case gallery

THE TEST

A tag holds when the card's `who_for` names that role's reader, or when it names nobody in
particular. FIX-16 settled the second half: "Anyone who keeps re-pasting the same
background into new chats" genuinely serves every role, and a rule that punished it would
push the catalogue back towards one persona per card, which is the Puckett fault wearing
the other face.

Everything else is a tag the card denies. "In-house counsel or legal ops triaging a high
volume of standard NDAs" does not name a product manager, and that row was tagged `pm`.
Twelve of the 58 cards in pm|builder named another job outright; Attack 2's PM agent
called it the finding that would make them leave, because a role filter that returns other
people's work makes every other filter suspect too.

ADDING A TAG

Mostly it does not. A card naming a designer while carrying no designer tag is a good
question and guessing at it from a phrase is how a catalogue acquires tags nobody checked,
so those are printed for a person to decide.

The question is asked of `skip_if` as well as `who_for`. Vanderbilt's page on AI-detector
false accusations singles out non-native English writers - the people most often falsely
accused - carries `teacher` alone, and was unreachable from the student filter. Attack 1
filed it; Attack 2 filed it again; a check that can only subtract was never going to fix
it.

The two directions do not share their evidence. Dropping stays on `who_for` alone, because
`skip_if` is who should not bother, and "skip this if you are a developer" must not be
allowed to keep a `developer` tag. Adding is a warning either way: a persona named
anywhere on a card is one the card serves or excludes on purpose, and both are worth a
person's look.

The exception is a row whose every current tag fails while its card plainly names a role
it does not carry. Eight marketing recipes were in that state - "Marketers", "Content
marketers", "Marketing teams", tagged `business-founder, pm` - and without the addition
they would have been swept into a collection card when the fix was a tag they should
always have had. Refusing to add would have caused a deletion.

FITS NO ROLE

A row fits no role when its card names none - not when its current tags happen to be
wrong. Those are Rule C's, printed at the end grouped by the gallery's own family.
"""

import io
import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "data", "items.json")
FAM = os.path.join(ROOT, "data", "use-case-departments.json")
GALLERY = "https://academy.claude.com/use-cases/"

# The reader each role names. Generous, because a false drop deletes a real audience and
# a false keep only leaves the status quo.
ROLE_WORDS = {
    "business-founder": r"business owner|founder|entrepreneur|small[- ]business|"
                        r"solo|freelanc|executive director|owner|proprietor|"
                        r"running a business|smb\b",
    "pm": r"product manager|product owner|product team|product people|product lead|\bpm\b|"
          r"product marketing",
    # \btutor\b, not tutor: "tutorial" is not a teacher.
    "teacher": r"teacher|instructor|faculty|educator|lecturer|classroom|professor|"
               r"school|\btutor\b",
    "student": r"student|undergrad|coursework|learner|pupil",
    # (?<!data )scientist: a data scientist is this site's data-analyst.
    "researcher": r"researcher|academic|postdoc|scholar|\bphd\b|(?<!data )scientist|"
                  r"principal investigator",
    # (?<!non-)coder: "non-coder" is the opposite of the reader this names.
    "developer": r"developer|engineer|programmer|(?<!non-)coder|devops|\bsre\b|on-call|"
                 r"technical team|software team",
    "designer": r"designer|design team|design system|\bux\b|\bui\b",
    "data-analyst": r"analyst|data scientist|data team|analytics",
    # content only where it is a job, not wherever the word appears.
    "writer-marketer": r"writer|marketer|copywriter|journalist|editor|"
                       r"content (marketer|designer|writer|strateg|team)|"
                       r"content marketing|communications|marketing team",
    "non-technical": r"anyone|everyone|non-technical|not a coder|office|"
                     r"somebody|no technical background",
}
ROLE_WORDS = {k: re.compile(v, re.I) for k, v in ROLE_WORDS.items()}

# A card that names nobody in particular serves everybody. See FIX-16.
NEUTRAL = re.compile(r"^\s*(anyone|any\b|someone|somebody|people who|everyone|whoever|"
                     r"those who|a reader|teams?\b)", re.I)


def load(path):
    with io.open(path, encoding="utf-8") as f:
        return json.load(f)


def main():
    apply = "--apply" in sys.argv
    gallery_only = "--gallery-only" in sys.argv
    items = load(P)
    fam = load(FAM) if os.path.exists(FAM) else {}

    dropped, roleless, rescued, suggested = [], defaultdict(list), [], []

    for it in items:
        if gallery_only and not it["url"].startswith(GALLERY):
            continue
        who = str(it.get("who_for") or "")
        if not who or NEUTRAL.match(who):
            continue

        # Two questions, two pieces of evidence. See ADDING A TAG above.
        named = {r for r, rx in ROLE_WORDS.items() if rx.search(who)}
        card = who + " " + str(it.get("skip_if") or "")
        named_anywhere = {r for r, rx in ROLE_WORDS.items() if rx.search(card)}
        tags = it.get("roles") or []
        keep = [r for r in tags if r in named]
        lose = [r for r in tags if r not in named]
        add = sorted(named - set(tags))
        add_anywhere = sorted(named_anywhere - set(tags))

        if not named:
            slug = (it["url"][len(GALLERY):].rstrip("/")
                    if it["url"].startswith(GALLERY) else None)
            roleless[fam.get(slug) or "(not in the gallery)"].append((it, lose))
            continue
        if not keep and add:
            # Every tag fails and the card names something else. Not adding here would
            # delete the row from the site over a tagging mistake.
            rescued.append((it, lose, add))
        elif lose:
            dropped.append((it, lose, keep))
        if keep and add_anywhere:
            suggested.append((it, add_anywhere,
                              [r for r in add_anywhere if r not in add]))

    print("TAGS THE CARD DENIES, where at least one tag survives (%d rows)" % len(dropped))
    for it, lose, keep in dropped[:40]:
        print("  %-44s -%-22s keeps %s" % (it["title"][:44], ",".join(lose), ",".join(keep)))
    if len(dropped) > 40:
        print("  ... and %d more" % (len(dropped) - 40))

    print()
    print("EVERY TAG FAILS AND THE CARD NAMES ANOTHER ROLE (%d rows) - the tag is "
          "corrected rather than the row deleted" % len(rescued))
    for it, lose, add in rescued:
        print("  %-44s -%-22s +%s" % (it["title"][:44], ",".join(lose), ",".join(add)))

    print()
    print("NAMES A ROLE IT DOES NOT CARRY (%d rows) - printed only; adding is a "
          "judgement. A role marked (skip_if) is named in the skip line rather than the "
          "who line" % len(suggested))
    for it, add, from_skip in suggested:
        marked = ",".join(r + ("(skip_if)" if r in from_skip else "") for r in add)
        print("  %-44s +%s" % (it["title"][:44], marked))
        print("       who:  %s" % (it.get("who_for") or "")[:104])
        if from_skip:
            print("       skip: %s" % (it.get("skip_if") or "")[:104])

    total_roleless = sum(len(v) for v in roleless.values())
    print()
    print("FITS NO ROLE AT ALL (%d rows) - Rule C's, by the gallery's own family"
          % total_roleless)
    for f in sorted(roleless):
        print("\n  %s (%d)" % (f, len(roleless[f])))
        for it, lose in roleless[f]:
            print("     %-46s was %s" % (it["title"][:46], ",".join(lose)))
            print("        %s" % (it.get("who_for") or "")[:112])

    if apply:
        for it, lose, keep in dropped:
            it["roles"] = [r for r in it["roles"] if r not in lose]
        for it, lose, add in rescued:
            it["roles"] = sorted(add)
        with io.open(P, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(items, ensure_ascii=False, indent=2) + "\n")
        print()
        print("applied: %d rows lost a tag the card denies, %d had every tag replaced "
              "by the role their card actually names. The %d roleless rows are "
              "untouched - removing their last tag would hide them with no card to "
              "replace them." % (len(dropped), len(rescued), total_roleless))
    return 0


if __name__ == "__main__":
    sys.exit(main())
