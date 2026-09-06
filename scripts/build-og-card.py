#!/usr/bin/env python3
"""
The one social card image, drawn from the site's own tokens and its own typeface.

    python3 scripts/build-og-card.py

WHY IT IS GENERATED

`og:image` needs a raster: Slack, Teams, iMessage and Twitter will not render an SVG.
Hand-exporting a PNG would put a binary in the repository that nothing regenerates and
nobody could diff, and the first time a colour token moved it would be wrong and silent.
So it is built from `assets/css/tokens.css` and `assets/fonts/tiempos`, and a token change
redraws it.

One image for every page in this round. A card per format - a different one for a video,
a repo, a course - is worth doing and was not worth blocking the share chain on. See
docs/specs/2026-09-07-share-chain.md, section 5.
"""

import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKENS = os.path.join(ROOT, "assets", "css", "tokens.css")
FONT = os.path.join(ROOT, "assets", "fonts", "tiempos", "Tiempos Fine Light.otf")
OUT = os.path.join(ROOT, "assets", "og-card.png")
W, H = 1200, 630


def token(name, fallback):
    css = open(TOKENS, encoding="utf-8").read()
    m = re.search(r"--%s:\s*(#[0-9a-fA-F]{3,8})" % re.escape(name), css)
    return m.group(1) if m else fallback


def main():
    paper = token("ivory-medium", "#f0eee6")
    ink = token("slate-dark", "#141413")
    clay = token("clay", "#d97757")
    muted = token("cloud-dark", "#87867f")

    img = Image.new("RGB", (W, H), paper)
    d = ImageDraw.Draw(img)

    big = ImageFont.truetype(FONT, 78)
    small = ImageFont.truetype(FONT, 34)
    tiny = ImageFont.truetype(FONT, 26)

    d.rectangle([0, 0, W, 10], fill=clay)
    d.text((84, 96), "Learn Claude", font=small, fill=muted)
    d.text((84, 172), "Find what's worth", font=big, fill=ink)
    d.text((84, 262), "your time.", font=big, fill=ink)
    d.text((84, 404),
           "Every entry says who it is for, when to skip it,", font=tiny, fill=ink)
    d.text((84, 444),
           "and the date we last looked.", font=tiny, fill=ink)
    d.line([84, 516, W - 84, 516], fill=token("stone", "#cccbc8"), width=1)
    d.text((84, 540), "An independent directory. Not affiliated with Anthropic.",
           font=tiny, fill=muted)

    img.save(OUT, "PNG", optimize=True)
    print("og card: %s, %d x %d, %.0f KB, colours read from tokens.css"
          % (os.path.relpath(OUT, ROOT), W, H, os.path.getsize(OUT) / 1024.0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
