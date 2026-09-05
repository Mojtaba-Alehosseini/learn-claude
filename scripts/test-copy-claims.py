#!/usr/bin/env python3
"""
Four sentences the site is not allowed to say again.

    python3 scripts/test-copy-claims.py

Attack 2 (2026-09-05) found the same fault in four places: a sentence claiming a level of
checking the site's own generated counts show as zero. Ten of ten agents hit at least one
of them; eight put it in their top two. The worst part was structural - `how-we-check.html`
computes its tier tally from the live data, so the page published a boast and its own
refutation side by side and refreshed both on every build.

D2 rewrote all four. This is what stops them coming back, and what Attack 3 re-reads.

A killed sentence is banned by substring across every file a reader can reach. A
replacement is required to be present, because deleting a claim and saying nothing is not
the same as saying the true thing - and a check that only bans is a check that passes on
an empty page.
"""

import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def surfaces():
    """Every shipped file a killed sentence could come back in.

    This used to be ten paths typed by hand, which covered the pages and scripts that
    existed the day it was written and nothing since. A list of files to check is a list
    somebody has to remember to update, and the copy deck - where the killed sentences are
    written down for re-use - was never on it.

    data/*.js are generated mirrors of items.json and are skipped: the catalogue's own
    prose is one build step away from being rewritten, and validate-catalogue.py owns it.
    """
    found = []
    for name in sorted(os.listdir(ROOT)):
        if name.endswith(".html"):
            found.append(name)
    js = os.path.join(ROOT, "assets", "js")
    if os.path.isdir(js):
        for name in sorted(os.listdir(js)):
            if name.endswith(".js"):
                found.append(os.path.join("assets", "js", name))
    deck = os.path.join("docs", "design", "ux-copy.md")
    if os.path.exists(os.path.join(ROOT, deck)):
        found.append(deck)
    return found


SURFACES = surfaces()

# (the banned substring, why it was killed)
BANNED = [
    ("checked by hand",
     "the tier meaning a person checked the notes has a count of zero, and "
     "how-we-check.html says so two clicks from the front page"),
    ("70 resources we can vouch for",
     "it described a site that does not exist; the generated count beneath it "
     "refuted it on every build"),
    ("We find material, read it",
     "false for every row below `ai-reviewed`, which is most of the catalogue"),
    ("do not list something we cannot open",
     "it sat six lines above the Skimmed definition, which explains that paid "
     "courses are listed precisely because we cannot see inside them"),
]

# (the required substring, which file it belongs on)
REQUIRED = [
    # Was "Every one checked and given a reason to " until 2026-09-06. "Checked" is the
    # exact word Attack 2 caught carrying the false claim, and putting it back in a
    # smaller sentence was the same fault in a smaller size. The line also subtracted
    # three in front of the reader - "632 of them opened" - which made a visitor do
    # arithmetic to discover what the missing three were. What is required now claims
    # only what is true of all 635 without a caveat.
    # Stops before the string break in home.js - the sentence is concatenated over
    # two literals and a substring test does not see across that.
    ("each with a reason to skip it and the date",
     os.path.join("assets", "js", "home.js")),
    ("We would rather read fewer resources in full", "how-we-check.html"),
    ("read as far as the label says", "how-we-check.html"),
    ("something whose page we cannot open", "how-we-check.html"),
    # The split the front screen gave up. Required here so "it moved to the method page"
    # cannot quietly become "it went away".
    ("have been opened; the", "how-we-check.html"),
]


def read(rel):
    with io.open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def main():
    failures = []

    for phrase, why in BANNED:
        for rel in SURFACES:
            body = read(rel)
            if phrase in body:
                line = next((i + 1 for i, l in enumerate(body.splitlines())
                             if phrase in l), 0)
                failures.append(
                    "%s:%d says %r again.\n      It was removed because %s."
                    % (rel, line, phrase, why))

    for phrase, rel in REQUIRED:
        if phrase not in read(rel):
            failures.append(
                "%s no longer contains %r.\n      D2 replaced a false claim with a true "
                "one; deleting the replacement puts the page back to saying nothing."
                % (rel, phrase))

    if failures:
        print("Copy claims: %d fault(s)." % len(failures))
        for f in failures:
            print("  " + f)
        print()
        print("These four sentences were rewritten under D2 on 2026-09-05 after ten of ten")
        print("Attack 2 agents found at least one of them. If a rewrite is genuinely")
        print("wanted, change this file in the same commit and say why.")
        return 1

    print("Copy claims: %d file(s) read, %d banned sentence(s) absent, "
          "%d replacement(s) present." % (len(SURFACES), len(BANNED), len(REQUIRED)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
