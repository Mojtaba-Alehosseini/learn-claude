#!/usr/bin/env python3
"""
Check 3, the attackers' way: does a pick's own card contradict the cell it sits in?

    python3 scripts/audit-pick-contradictions.py

Advisory. It prints and never fails a build, for the same reason the copy-openings report
prints and never fails: a build that goes red on a judgement call teaches people to edit
the judgement until the build is green.

WHY THIS EXISTS
---------------
The FIX-15 picks audit ran check 3 - "does any pick contradict itself?" - and reported
zero. Attack 2 then found two, by reading something that audit never read: each pick's own
`who_for` and `skip_if` AGAINST THE CELL it is recommended in, rather than against the
pick's own reason.

    researcher|never-used  "How long do you store my data?"
      skip_if: "...if your data sits on Team, Enterprise or the API the answers are
                different and THIS IS THE WRONG PAGE."
      University researchers are overwhelmingly on institutional Team or Enterprise.

    pm|builder             "Build an 'Ask the Company' agent"
      who_for: "Engineering teams tired of re-answering the same onboarding and
                ownership questions."
      One of exactly two things the site told a product manager to start with.

Both were fixed on 2026-09-05, along with a third instance of the first. The displaced
picks are recorded as runners-up with cause `contradicted-its-own-card`, so the next audit
starts from a record rather than from somebody remembering.

WHAT IT WILL NOT DECIDE FOR YOU
-------------------------------
A `who_for` that opens "Anyone who..." is deliberately role-neutral and serves every role
- FIX-16 settled that, and treating it as a fault would push the catalogue back towards
naming one persona per card, which is the Puckett fault wearing the other face. Those
openings are skipped. What is left still needs reading: this tool finds candidates, a
person decides.
"""

import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Words that name a reader. Deliberately generous: a miss here is a contradiction that
# ships, a false positive is thirty seconds of reading.
ROLE_WORDS = {
    "business-founder": ("business owner", "founder", "entrepreneur", "small business",
                         "small-team owner", "shop owner", "solo", "owner"),
    "pm": ("product manager", "product owner", "product team", "product people",
           "pm,", "pm ", " pm", "product lead"),
    "teacher": ("teacher", "instructor", "faculty", "educator", "lecturer", "classroom",
                "school"),
    "student": ("student", "undergrad", "coursework", "learner"),
    "researcher": ("researcher", "academic", "postdoc", "scholar", "phd", "scientist"),
    "developer": ("developer", "engineer", "programmer", "coder", "devops"),
    "designer": ("designer", "design team", "ux ", "ui "),
    "data-analyst": ("analyst", "data scientist", "data team"),
    "writer-marketer": ("writer", "marketer", "copywriter", "journalist", "editor",
                        "content"),
    "non-technical": ("anyone", "non-technical", "not a coder", "office", "everyone"),
}

# A card that opens for everybody is not naming somebody else. See FIX-16.
NEUTRAL_OPENER = re.compile(r"^\s*(anyone|any\b|someone|somebody|people who|everyone|"
                            r"whoever|those who|a reader)", re.I)

# A skip_if that turns this reader away, as opposed to warning them about something.
EXCLUDES = re.compile(
    r"(this is the wrong page|it is not about claude|not one instruction here"
    r"|none of it applies|does not apply to you|is not for you)", re.I)


def load(name):
    with io.open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def main():
    items = load("items.json")
    picks = load("picks.json")["cells"]
    by_url = {x["url"]: x for x in items}

    flagged = []
    for key in sorted(picks):
        role = key.split("|")[0]
        mine = ROLE_WORDS.get(role, ())
        for p in picks[key]["picks"]:
            it = by_url.get(p["url"])
            if it is None:
                flagged.append((key, "(missing from the catalogue)", p["url"], ""))
                continue
            who = (it.get("who_for") or "")
            skip = (it.get("skip_if") or "")
            low = who.lower()

            names_mine = any(w in low for w in mine)
            others = [r for r, words in ROLE_WORDS.items()
                      if r != role and any(w in low for w in words)]
            wrong_reader = (others and not names_mine
                            and not NEUTRAL_OPENER.match(who))

            excl = EXCLUDES.search(skip)
            if wrong_reader:
                flagged.append((key, "who_for names %s, not %s" % (", ".join(others), role),
                                it["title"], who))
            if excl:
                flagged.append((key, "skip_if turns this reader away (%r)" % excl.group(0),
                                it["title"], skip))

    for key, why, title, quote in flagged:
        print("\n%s" % key)
        print("  %s" % title[:78])
        print("  %s" % why)
        print("    %s" % quote[:190])

    print()
    print("%d pick(s) worth reading. Nothing here is a fault until a person says so."
          % len(flagged))
    return 0


if __name__ == "__main__":
    sys.exit(main())
