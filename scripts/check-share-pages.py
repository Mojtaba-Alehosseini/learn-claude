#!/usr/bin/env python3
"""
Every shareable thing has a served page, and every served page says what it is.

    python3 scripts/check-share-pages.py

WHY THIS EXISTS

The share chain is invisible from inside a browser: the tab title is correct on every page
because JavaScript writes it, and the thing a crawler reads is the thing nobody looks at.
That is exactly how 588 pages shipped for months serving one title. A generator that
silently stops producing pages, or produces them with the shell's placeholder head, would
fail the same silent way.

So this reads the built HTML rather than trusting the builder, and it is a gate:
`test-gates.py` plants a missing og:title in a generated page and asserts the build
goes red.
"""

import io
import json
import html as htmllib
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://mojtaba-alehosseini.github.io/learn-claude/"
PLACEHOLDERS = ("Resource — Learn Claude", "Browse — Learn Claude",
                "Paths — Learn Claude")


def load(name):
    with io.open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def meta(html, prop):
    m = re.search(r'<meta property="%s" content="([^"]*)"' % re.escape(prop), html)
    return m.group(1) if m else None


def main():
    # The generator's own list. Recomputing it here would test this file's idea of the
    # catalogue against itself; reading the manifest tests what was actually written.
    share = load("share-pages.json")["pages"]
    expected = [(p["rel"], p["title"]) for p in share]

    # And the manifest has to match the catalogue, or a resource could quietly stop
    # having a page and both sides would agree about it.
    live = {"r/%s/" % x["id"] for x in load("items.json") if x.get("status") == "live"}
    listed = {p["rel"] for p in share if p["kind"] == "resource"}

    faults = []
    for rel, title in expected:
        path = os.path.join(ROOT, rel.replace("/", os.sep), "index.html")
        if not os.path.exists(path):
            faults.append("%s has no served page" % rel)
            continue
        html = io.open(path, encoding="utf-8").read()

        og = meta(html, "og:title")
        t = re.search(r"<title>(.*?)</title>", html, re.S)
        t = t.group(1).strip() if t else None
        for label, value in (("og:title", og), ("<title>", t)):
            if not value:
                faults.append("%s has no %s" % (rel, label))
            elif value in PLACEHOLDERS:
                faults.append("%s serves the shell's placeholder %s: %r"
                              % (rel, label, value))
        if title and og and title[:40] not in htmllib.unescape(og):
            faults.append("%s says %r, which is not its own title" % (rel, og[:60]))

        if not meta(html, "og:description"):
            faults.append("%s has no og:description" % rel)
        if not meta(html, "og:image"):
            faults.append("%s has no og:image" % rel)

        want = SITE + rel
        if meta(html, "og:url") != want:
            faults.append("%s has og:url %r, expected %r"
                          % (rel, meta(html, "og:url"), want))
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', html)
        if not canon or canon.group(1) != want:
            faults.append("%s canonical is %r, expected %r"
                          % (rel, canon and canon.group(1), want))

    for rel in sorted(live - listed):
        faults.append("%s is live in the catalogue and not in the manifest" % rel)
    for rel in sorted(listed - live):
        faults.append("%s is in the manifest and not live in the catalogue" % rel)

    img = os.path.join(ROOT, "assets", "og-card.png")
    if not os.path.exists(img):
        faults.append("assets/og-card.png is missing, so every preview has no image")

    sm = os.path.join(ROOT, "sitemap.xml")
    if os.path.exists(sm):
        text = io.open(sm, encoding="utf-8").read()
        for old in ("resource.html?id=", "paths.html?id="):
            if old in text:
                faults.append("sitemap lists %s, which redirects - canonical URLs only"
                              % old)

    if faults:
        print("%d fault(s) in the share chain:" % len(faults))
        for f in faults[:40]:
            print("  " + f)
        if len(faults) > 40:
            print("  ... and %d more" % (len(faults) - 40))
        return 1

    print("Share pages: %d served, each with its own title, description, image, "
          "canonical and og:url." % len(expected))
    return 0


if __name__ == "__main__":
    sys.exit(main())
