#!/usr/bin/env python3
"""
Normalise a generated role icon so all ten match exactly.

Nano Banana will never hit an exact hex or an exact margin. Do not fight it in the
prompt. Generate freely, then run this.

What it does:
  1. Snaps every colour to the four brand colours (nearest wins).
  2. Crops to the drawing, then re-pads so the art fills 93% of the frame,
     the same as Anthropic's own icons.
  3. Writes a clean PNG. Optionally also a transparent version.

Usage:
    python3 scripts/normalise-icon.py <in.jpg|png> [more...] -o assets/icons/
    python3 scripts/normalise-icon.py in.png -o out/ --transparent
    python3 scripts/normalise-icon.py in.png -o out/ --size 512
"""

import sys
import os
from PIL import Image

# Anthropic palette. See docs/specs/2026-08-19-directory-spec.md section 14.
BG     = (0xF0, 0xEE, 0xE6)   # ivory medium — page canvas
LIGHT  = (0xFA, 0xF9, 0xF5)   # ivory light  — unaccented shapes
ACCENT = (0xE3, 0xDA, 0xCC)   # oat warm     — the accented shape
INK    = (0x14, 0x14, 0x13)   # slate dark   — the outline

PALETTE = [BG, LIGHT, ACCENT, INK]
FILL_RATIO = 0.93             # how much of the frame the drawing occupies
OUT_SIZE = 1024


def nearest(px):
    r, g, b = px[:3]
    return min(PALETTE, key=lambda c: (r-c[0])**2 + (g-c[1])**2 + (b-c[2])**2)


def snap(im):
    """Quantise every pixel to the four brand colours."""
    im = im.convert("RGB")
    cache = {}
    out = Image.new("RGB", im.size)
    src, dst = im.load(), out.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            p = src[x, y]
            if p not in cache:
                cache[p] = nearest(p)
            dst[x, y] = cache[p]
    return out


def bounds(im):
    """Box around everything that is not background."""
    px = im.load()
    w, h = im.size
    minx, miny, maxx, maxy = w, h, 0, 0
    for y in range(h):
        for x in range(w):
            if px[x, y] != BG:
                if x < minx: minx = x
                if x > maxx: maxx = x
                if y < miny: miny = y
                if y > maxy: maxy = y
    if maxx <= minx:
        return None
    return (minx, miny, maxx + 1, maxy + 1)


def reframe(im, size=OUT_SIZE):
    """Crop to the drawing, then centre it in a square at the target fill ratio."""
    box = bounds(im)
    if box is None:
        return im.resize((size, size), Image.LANCZOS)
    art = im.crop(box)
    target = int(size * FILL_RATIO)
    scale = target / max(art.size)
    art = art.resize(
        (max(1, round(art.width * scale)), max(1, round(art.height * scale))),
        Image.LANCZOS,
    )
    canvas = Image.new("RGB", (size, size), BG)
    canvas.paste(art, ((size - art.width) // 2, (size - art.height) // 2))
    return canvas


def transparent(im):
    """Same image with the background knocked out, for use on any surface."""
    rgba = im.convert("RGBA")
    px = rgba.load()
    w, h = rgba.size
    for y in range(h):
        for x in range(w):
            if px[x, y][:3] == BG:
                px[x, y] = (BG[0], BG[1], BG[2], 0)
    return rgba


def report(im, label):
    box = bounds(im)
    if box:
        wide = 100 * (box[2] - box[0]) / im.width
        tall = 100 * (box[3] - box[1]) / im.height
        print(f"    {label}: art fills {wide:.0f}% wide, {tall:.0f}% tall")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)

    outdir = "."
    size = OUT_SIZE
    want_alpha = "--transparent" in args
    if "-o" in args:
        i = args.index("-o")
        outdir = args[i + 1]
        del args[i:i + 2]
    if "--size" in args:
        i = args.index("--size")
        size = int(args[i + 1])
        del args[i:i + 2]
    files = [a for a in args if not a.startswith("-")]
    os.makedirs(outdir, exist_ok=True)

    for path in files:
        name = os.path.splitext(os.path.basename(path))[0]
        im = Image.open(path)
        print(f"{os.path.basename(path)}  {im.size[0]}x{im.size[1]}")
        report(im.convert("RGB"), "before")

        # Snap, reframe, then snap again. The resize inside reframe interpolates and
        # reintroduces in-between colours, so the second snap is what actually
        # guarantees four flat colours — and it cuts the file size by about 90%.
        im = snap(reframe(snap(im), size))
        report(im, "after ")

        dest = os.path.join(outdir, f"{name}.png")
        im.save(dest)
        print(f"    -> {dest}")

        if want_alpha:
            dest_a = os.path.join(outdir, f"{name}-alpha.png")
            transparent(im).save(dest_a)
            print(f"    -> {dest_a}")


if __name__ == "__main__":
    main()
