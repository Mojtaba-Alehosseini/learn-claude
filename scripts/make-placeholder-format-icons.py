#!/usr/bin/env python3
"""
Draw stand-in format icons so nothing on a card is missing while the real ones are made.

These are placeholders and are meant to be replaced. They are drawn in code from the
four brand colours with a thick black outline, so they sit quietly next to the 40
hand-drawn role icons instead of looking broken — but they are geometric, not drawn,
and a person will see the difference at a glance. That is deliberate: a placeholder
that is too convincing never gets replaced.

The prompts for the real ones are in docs/design/format-icon-prompts.md.

Overwrite any file here with the real drawing and nothing else needs to change — the
filenames are what the site already asks for.

    python3 scripts/make-placeholder-format-icons.py
"""

import os
from PIL import Image, ImageDraw

OUT = "assets/icons/formats"
SIZE = 512
INK = (20, 20, 19)          # --slate-dark
PAPER = (250, 249, 245)     # --ivory-light
OAT = (227, 218, 204)       # --oat-warm
CLAY = (217, 119, 87)       # --clay
W = 15                      # outline weight


def box(d, xy, fill=PAPER, r=18):
    d.rounded_rectangle(xy, radius=r, fill=fill, outline=INK, width=W)


def video(d):
    box(d, (70, 150, 360, 380))                       # camera body
    d.polygon([(360, 230), (450, 180), (450, 350), (360, 300)], fill=OAT, outline=INK)
    d.line([(360, 230), (450, 180), (450, 350), (360, 300)], fill=INK, width=W, joint="curve")
    d.ellipse((150, 220, 280, 350), fill=OAT, outline=INK, width=W)
    d.ellipse((196, 266, 234, 304), fill=INK)


def course(d):
    d.polygon([(256, 120), (452, 210), (256, 300), (60, 210)], fill=OAT, outline=INK)
    d.line([(256, 120), (452, 210), (256, 300), (60, 210), (256, 120)], fill=INK,
           width=W, joint="curve")
    d.line([(430, 220), (430, 330)], fill=INK, width=W)
    d.ellipse((412, 330, 448, 366), fill=CLAY, outline=INK, width=W)
    box(d, (120, 320, 392, 400), r=10)


def docs(d):
    box(d, (70, 110, 442, 400), r=14)
    d.line([(256, 125), (256, 385)], fill=INK, width=W)
    d.rectangle((96, 150, 232, 360), fill=OAT)
    d.rectangle((96, 150, 232, 360), outline=INK, width=W)
    d.line([(330, 110), (330, 250)], fill=CLAY, width=26)
    d.line([(330, 110), (330, 250)], fill=INK, width=W, joint="curve")


def article(d):
    d.polygon([(110, 80), (330, 80), (410, 160), (410, 430), (110, 430)], fill=PAPER)
    d.line([(110, 80), (330, 80), (410, 160), (410, 430), (110, 430), (110, 80)],
           fill=INK, width=W, joint="curve")
    d.polygon([(330, 80), (410, 160), (330, 160)], fill=OAT, outline=INK)
    d.line([(330, 80), (330, 160), (410, 160)], fill=INK, width=W)
    for y in (230, 285, 340):
        d.line([(160, y), (360, y)], fill=INK, width=12)


def repo(d):
    box(d, (55, 120, 457, 392), r=16)
    d.rectangle((70, 135, 442, 195), fill=OAT)
    d.line([(55, 195), (457, 195)], fill=INK, width=W)
    for cx in (110, 155, 200):
        d.ellipse((cx - 11, 154, cx + 11, 176), fill=INK)
    d.line([(140, 250), (200, 300), (140, 350)], fill=INK, width=W, joint="curve")
    d.line([(240, 350), (370, 350)], fill=CLAY, width=20)


def hands_on(d):
    d.ellipse((156, 156, 356, 356), fill=OAT, outline=INK, width=W)
    d.ellipse((216, 216, 296, 296), fill=PAPER, outline=INK, width=W)
    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        d.rectangle((256 + dx * 175 - 26, 256 + dy * 175 - 26,
                     256 + dx * 175 + 26, 256 + dy * 175 + 26), fill=OAT, outline=INK, width=W)


def podcast(d):
    box(d, (196, 70, 316, 300), r=60)
    d.rounded_rectangle((214, 88, 298, 200), radius=42, fill=OAT, outline=INK, width=10)
    d.arc((146, 190, 366, 380), start=0, end=180, fill=INK, width=W)
    d.line([(256, 350), (256, 420)], fill=INK, width=W)
    d.line([(180, 428), (332, 428)], fill=CLAY, width=24)
    d.line([(180, 428), (332, 428)], fill=INK, width=W)


DRAW = {"video": video, "course": course, "docs": docs, "article": article,
        "repo": repo, "hands-on": hands_on, "podcast": podcast}


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, fn in DRAW.items():
        im = Image.new("RGB", (SIZE, SIZE), PAPER)
        d = ImageDraw.Draw(im)
        fn(d)
        path = os.path.join(OUT, f"{name}-alpha.png")
        im.save(path, optimize=True)
        print(f"  {name:10} -> {path} ({os.path.getsize(path)//1024} KB)")
    print(f"\n{len(DRAW)} placeholders. Replace each with the real drawing when ready;")
    print("the filenames are already what the site asks for.")


if __name__ == "__main__":
    main()
