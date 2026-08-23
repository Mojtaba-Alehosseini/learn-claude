#!/usr/bin/env python3
"""
Turn one drawn icon into a fillable icon.

The problem this solves: four separately generated hourglasses are four different
hourglasses. The waist moves, the bars change width, and side by side they read as
different objects instead of one object filling up.

The fix: draw the shape once. Knock a hole in its interior. Put a coloured layer behind
it and change that layer's height. The outline never moves, so the four states are
guaranteed to match, and the change can animate.

Output per icon:
  <name>-frame.png   the drawing with its interior removed. Everything else opaque.
  <name>-fill.png    only the interior, solid accent. Useful for checking.

How the browser uses it: a beige box, then <name>-frame.png on top. The frame is opaque
ivory everywhere except the interior, so the beige only shows through the hole.

Usage:
    python3 scripts/make-fillable-icon.py in.png --name hourglass -o assets/icons/level
    python3 scripts/make-fillable-icon.py in.png --name moon -o out/ --seed 512,512

--seed is one or more points inside the shape, "x,y" or "x,y;x,y". Defaults to the
centre of the drawing. Give it explicitly when the centre falls on the outline, as it
does on an hourglass waist. Give several when an internal line divides the interior
into separate closed regions — a drawn sand line inside an hourglass does exactly this.
"""

import sys
import os
from collections import deque
from PIL import Image

BG     = (0xF0, 0xEE, 0xE6)
LIGHT  = (0xFA, 0xF9, 0xF5)
ACCENT = (0xE3, 0xDA, 0xCC)
INK    = (0x14, 0x14, 0x13)


def interior(im, seed):
    """Flood fill from a point inside the shape. Stops at the ink outline.

    Returns a set of pixel coordinates that are inside. Because it stops at ink and
    never starts outside, it cannot escape a closed outline.
    """
    px = im.load()
    w, h = im.size
    inside = set()
    q = deque([seed])
    seen = {seed}
    while q:
        x, y = q.popleft()
        if px[x, y] == INK:
            continue
        inside.add((x, y))
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in seen:
                seen.add((nx, ny))
                q.append((nx, ny))
    return inside


def touches_edge(inside, w, h):
    """True if the fill reached the frame edge, meaning the outline had a gap."""
    for x, y in inside:
        if x == 0 or y == 0 or x == w - 1 or y == h - 1:
            return True
    return False


def centre_of_drawing(im):
    px = im.load()
    w, h = im.size
    xs, ys = [], []
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            if px[x, y] != BG:
                xs.append(x)
                ys.append(y)
    if not xs:
        return (w // 2, h // 2)
    return ((min(xs) + max(xs)) // 2, (min(ys) + max(ys)) // 2)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)

    outdir, name, seed, clip = ".", None, None, None
    if "--clip-below" in args:
        i = args.index("--clip-below")
        clip = int(args[i + 1])
        del args[i:i + 2]
    for flag, setter in (("-o", "outdir"), ("--name", "name"), ("--seed", "seed")):
        if flag in args:
            i = args.index(flag)
            val = args[i + 1]
            if setter == "outdir":
                outdir = val
            elif setter == "name":
                name = val
            else:
                seed = [tuple(int(v) for v in p.split(",")) for p in val.split(";")]
            del args[i:i + 2]

    src = [a for a in args if not a.startswith("-")][0]
    name = name or os.path.splitext(os.path.basename(src))[0]
    os.makedirs(outdir, exist_ok=True)

    im = Image.open(src).convert("RGB")
    w, h = im.size
    if seed is None:
        seed = [centre_of_drawing(im)]
        print(f"seed not given, using centre of drawing {seed[0]}")

    px = im.load()
    inside = set()
    for s in seed:
        if px[s] == INK:
            print(f"ERROR: seed {s} is on the outline. Pick a point inside the shape.")
            sys.exit(1)
        region = interior(im, s)
        print(f"  seed {s}: {100*len(region)/(w*h):.1f}% of frame")
        inside |= region
    if clip is not None:
        # Keep only the part below this line. An hourglass fills from the bottom, so
        # the upper chamber must stay empty even though it connects at the waist.
        inside = {(x, y) for x, y in inside if y >= clip}
        print(f"  clipped to y >= {clip}")

    print(f"interior: {len(inside)} px = {100*len(inside)/(w*h):.1f}% of frame")

    if touches_edge(inside, w, h):
        print("ERROR: the fill escaped to the frame edge.")
        print("  The outline has a gap in it. Close the gap or use a different drawing.")
        sys.exit(1)

    frame = im.convert("RGBA")
    fill = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    fp, gp = fill.load(), frame.load()
    for x, y in inside:
        gp[x, y] = (0, 0, 0, 0)
        fp[x, y] = ACCENT + (255,)

    frame.save(os.path.join(outdir, f"{name}-frame.png"))
    fill.save(os.path.join(outdir, f"{name}-fill.png"))
    print(f"-> {outdir}/{name}-frame.png")
    print(f"-> {outdir}/{name}-fill.png")


if __name__ == "__main__":
    main()
