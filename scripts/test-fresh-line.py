#!/usr/bin/env python3
"""Every surface that draws a resource asks for the freshness line. None builds one.

    python3 scripts/test-fresh-line.py

WHY THIS EXISTS

A resource carries three facts about its freshness: when we checked it, what its
publication date means, and when the page itself was last revised. Three surfaces show
them, and each used to assemble the line itself - in its own order, with its own markup,
and dropping whichever part its author forgot.

That is not a hypothetical. Attack 2 found the resource page dropping the Updated date
and it was fixed there, on that surface, as M1. The path page kept the same bug for two
more rounds until Attack 3's analyst found it - on the one surface built for a reader who
cannot judge a resource for themselves, which made it the worst place to hide the
freshest date the site holds.

A fix applied to one of three copies is not a fix. So the assembly lives in LC.freshParts
and this file holds the list of surfaces: if a new one starts drawing resources, it goes
in SURFACES, and if any surface goes back to naming the parts itself, this fails.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS = os.path.join(ROOT, "assets", "js")

# The surfaces that draw a resource for a reader. The card is drawn by ui.js and appears
# on the home page and on browse; the path step and the resource page draw their own.
SURFACES = {
    "ui.js": "the card, on the home page and on browse",
    "paths.js": "a step inside a path",
    "resource.js": "the resource's own page",
}

# Where the line is assembled. The only file allowed to name the parts.
SOURCE = "ui.js"

PART = re.compile(r"\bfresh(?:ness)?\s*\.\s*(checked|note|cls|updatedNote)\b")
ASKS = re.compile(r"\bLC\.fresh(?:Parts|Spans)\s*\(")


def main():
    problems = []

    src = io.open(os.path.join(JS, SOURCE), encoding="utf-8").read()
    for name in ("LC.freshParts", "LC.freshSpans"):
        if name + " = function" not in src:
            problems.append("%s does not define %s" % (SOURCE, name))

    for f, what in sorted(SURFACES.items()):
        p = os.path.join(JS, f)
        if not os.path.exists(p):
            problems.append("%s is listed as a surface and does not exist" % f)
            continue
        text = io.open(p, encoding="utf-8").read()
        code = "\n".join(strip_comments(text))
        if not ASKS.search(code):
            problems.append("%s (%s) never asks for the freshness line" % (f, what))
        hand = PART.findall(code) if f != SOURCE else []
        if hand:
            problems.append("%s (%s) names the parts itself: %s — it should ask "
                            "LC.freshParts instead" % (f, what, ", ".join(sorted(set(hand)))))

    # A surface nobody listed. Any other file under assets/js that draws a resource is a
    # surface this list has not been told about.
    for f in sorted(os.listdir(JS)):
        if not f.endswith(".js") or f in SURFACES:
            continue
        code = "\n".join(strip_comments(io.open(os.path.join(JS, f), encoding="utf-8").read()))
        if PART.search(code) or ASKS.search(code):
            problems.append("%s draws a freshness line and is not in SURFACES" % f)

    for f, what in sorted(SURFACES.items()):
        print("ok    %-14s %s" % (f, what))

    if problems:
        print()
        for m in problems:
            print("   " + m)
        sys.exit("the freshness line is assembled in more than one place.")
    print("\nOne freshness line, asked for by every surface that shows one.")


def strip_comments(text):
    """Block and line comments out, so a comment quoting `fresh.note` is not a fault."""
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return [re.sub(r"//.*$", "", ln) for ln in text.splitlines()]


if __name__ == "__main__":
    main()
