#!/usr/bin/env python3
"""
Fetch each publisher's own mark, once, into assets/icons/publishers/.

The path step card has a badge for the publisher's own logo. There is no fallback for a
publisher we do not hold a mark for — the real logo or no badge. A lettered square was
built and rejected: it is not a mark, it is an apology for not having one.

"Real" means a file we hold. Fetched here, at build time, into
assets/icons/publishers/<slug>.png, committed, never requested at render. A favicon
service called per card would send every reader's browsing to a third party each time the
page loads; running this script once and shipping the result does not.

Sourcing, in order: the publisher's own SVG mark, then the largest apple-touch-icon their
own <head> advertises, then favicon.ico. A guessed path (/apple-touch-icon.png) 404s or
redirects to a login wall on several of these hosts — coursera.org, datacamp.com,
learning.northeastern.edu, udemy.com all serve their real icon from a different, versioned
CDN path that only the page's own <head> names. So this reads the head rather than
guessing the path.

If nothing at least 32px square exists for a host, that host is dropped rather than
shipped blurred — a 16px favicon stretched into a 28px badge looks broken, and a broken
badge is worse than none.

THE_TARGETS below is the one place the mapping lives. It drives both what this script
fetches and, through data/publisher-marks.json, which hosts a card badges at render time —
so a host added here and a host recognised by the site can never drift apart.

    python3 scripts/fetch-publisher-marks.py                 # (re)fetch every slug
    python3 scripts/fetch-publisher-marks.py youtube github   # just these, to refresh them

Requires Pillow, like the other icon scripts in this directory (normalise-icon.py,
make-fillable-icon.py) — the only scripts here that are not standard-library-only.
"""

import io
import json
import os
import re
import sys
import urllib.request
from urllib.parse import urljoin

from PIL import Image

DEST = "assets/icons/publishers"
MANIFEST = "data/publisher-marks.json"
MIN_SIZE = 32

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36")

# slug -> (page to read <head> from, every hostname that should badge with this mark).
# Measured against data/items.json on 2026-08-28: youtube.com 72 entries, github.com 31,
# the seven Anthropic hosts 87 together, then these five to 61% of the 354-entry
# catalogue. See docs/design/path-card-spec.md for the running total.
TARGETS = {
    "youtube":      ("https://www.youtube.com/",
                      ["youtube.com", "youtu.be"]),
    "github":       ("https://github.com/",
                      ["github.com"]),
    "anthropic":    ("https://claude.com/",
                      ["claude.com", "support.claude.com", "anthropic.com",
                       "anthropic.skilljar.com", "code.claude.com",
                       "platform.claude.com", "academy.claude.com"]),
    "coursera":     ("https://www.coursera.org/",
                      ["coursera.org"]),
    "northeastern": ("https://learning.northeastern.edu/",
                      ["learning.northeastern.edu"]),
    "datacamp":     ("https://www.datacamp.com/",
                      ["datacamp.com"]),
    "medium":       ("https://medium.com/",
                      ["medium.com"]),
    "udemy":        ("https://www.udemy.com/",
                      ["udemy.com"]),
    "linkedin":     ("https://www.linkedin.com/",
                      ["linkedin.com"]),
}

LINK_RE = re.compile(
    r'<link[^>]+rel=["\'](?:shortcut\s+)?'
    r'(icon|apple-touch-icon(?:-precomposed)?|mask-icon)["\'][^>]*>', re.I)
HREF_RE = re.compile(r'href=["\']([^"\']+)["\']', re.I)
SIZES_RE = re.compile(r'sizes=["\']([^"\']+)["\']', re.I)


def fetch_bytes(url, accept="*/*"):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    return urllib.request.urlopen(req, timeout=20).read()


def candidates(html, base_url):
    """Every plausible mark for this publisher, best kind first.

    Four tiers, tried in order — this is sourcing PRIORITY, not a size sort, because a
    declared apple-touch-icon beats a bigger plain favicon even when the favicon's own
    `sizes` attribute claims to be larger:

      1. apple-touch-icon links the page's own <head> declares, largest first.
      2. /apple-touch-icon.png at the site's root. Two of nine targets (github.com,
         claude.com) serve a real 120-180px icon here that their own <head> never
         mentions — Apple's convention does not require a <link> tag, and several
         sites only serve the file, not the reference.
      3. plain `icon` links the head declares, largest first. Often an .ico of unknown
         interior sizes, or an SVG that raster tools cannot open — best_mark() below
         skips whichever candidate fails to decode and moves to the next.
      4. /favicon.ico at the root, the last resort.

    mask-icon is excluded outright: the spec reserves that relation for a monochrome
    silhouette, and using one sight-unseen risks shipping a solid black square.
    """
    apple, plain = [], []
    for m in LINK_RE.finditer(html):
        rel, tag = m.group(1).lower(), m.group(0)
        if rel == "mask-icon":
            continue
        href = HREF_RE.search(tag)
        if not href:
            continue
        sizes = SIZES_RE.search(tag)
        side = 0
        if sizes and "x" in sizes.group(1).lower():
            try:
                side = int(sizes.group(1).lower().split("x")[0])
            except ValueError:
                pass
        url = urljoin(base_url, href.group(1))
        (apple if rel.startswith("apple-touch-icon") else plain).append((side, url))
    apple.sort(reverse=True)
    plain.sort(reverse=True)

    tiers = (
        [u for _, u in apple],
        [urljoin(base_url, "/apple-touch-icon.png"),
         urljoin(base_url, "/apple-touch-icon-precomposed.png")],
        [u for _, u in plain],
        [urljoin(base_url, "/favicon.ico")],
    )
    seen, ordered = set(), []
    for tier in tiers:
        for url in tier:
            if url not in seen:
                seen.add(url)
                ordered.append(url)
    return ordered


def best_mark(slug, homepage):
    html = fetch_bytes(homepage, accept="text/html").decode("utf-8", "replace")
    for url in candidates(html, homepage):
        try:
            data = fetch_bytes(url, accept="image/*")
            im = Image.open(io.BytesIO(data)).convert("RGBA")
        except Exception as e:               # noqa: BLE001 - one bad candidate, try the next
            print(f"    ({url} -> {type(e).__name__}, trying the next)")
            continue
        if min(im.size) < MIN_SIZE:
            continue
        return im, url
    return None, None


def main():
    os.makedirs(DEST, exist_ok=True)
    only = sys.argv[1:] or list(TARGETS)
    unknown = [s for s in only if s not in TARGETS]
    if unknown:
        sys.exit("not in TARGETS: " + ", ".join(unknown))

    for slug in only:
        homepage, _ = TARGETS[slug]
        try:
            im, url = best_mark(slug, homepage)
        except Exception as e:               # noqa: BLE001 - a network fault must not
            print(f"  {slug:14} FAILED to fetch {homepage}: {e}")   # kill the whole run
            continue
        if im is None:
            print(f"  {slug:14} no icon >= {MIN_SIZE}px found in <head> - dropped, "
                  f"no badge will show for its hosts")
            continue
        im.save(os.path.join(DEST, slug + ".png"))
        print(f"  {slug:14} {im.width}x{im.height}  {url}")

    # The manifest is written from every slug that has a file on disk, not only the ones
    # this run touched - so `fetch-publisher-marks.py youtube` refreshes one mark without
    # dropping the badge on the other eight.
    manifest = {}
    for slug, (_, hosts) in TARGETS.items():
        if not os.path.exists(os.path.join(DEST, slug + ".png")):
            continue
        for h in hosts:
            manifest[h] = slug
    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, sort_keys=True, ensure_ascii=False)
        f.write("\n")
    print(f"\n{len(manifest)} hosts -> {len(set(manifest.values()))} marks. "
          f"Wrote {MANIFEST}.")
    print("Run scripts/build-data-js.py to mirror it for the browser.")


if __name__ == "__main__":
    main()
