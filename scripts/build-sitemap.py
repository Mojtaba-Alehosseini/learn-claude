#!/usr/bin/env python3
"""
Write sitemap.xml from the data, instead of by hand.

    python3 scripts/build-sitemap.py

The file this replaces was typed once and never touched again. By the time an agent
opened it in Attack 2 it listed **353** resource URLs for a 635-item catalogue - 282
pages a crawler could not find - and **35** of the 353 pointed at ids that no longer
exist, so the site's own index was handing search engines soft 404s. Its first resource
URL rendered "Not found" at HTTP 200. Every lastmod in it read 2026-08-23 while 211
resources had been checked on 5 September.

Ids derive from URLs, so any row whose URL changed took its id with it and left a dead
entry behind. That is the same failure the README warns about for ids and build-paths.py
warns about for path steps: a hand-maintained list of generated values goes wrong
silently and stays wrong. So this generates it, `lastmod` comes from each row's own
`checked` date, and build.sh runs it.
"""

import io
import json
import os
import sys
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://mojtaba-alehosseini.github.io/learn-claude/"
PAGES = ["", "browse.html", "paths.html", "how-we-check.html"]
OUT = os.path.join(ROOT, "sitemap.xml")


def load(name):
    with io.open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        d = json.load(f)
    if isinstance(d, dict):
        for k in ("items", "paths", "resources"):
            if k in d:
                return d[k]
    return d


def main():
    items = load("items.json")
    paths = load("paths.json")

    checked = sorted(x["checked"] for x in items if x.get("checked"))
    newest = checked[-1] if checked else ""

    rows = []
    for p in PAGES:
        rows.append((BASE + p, newest))
    for p in paths:
        rows.append((BASE + "paths.html?id=" + p["id"], newest))
    for x in items:
        # resource.html is one page; the id is what a crawler needs to see them all.
        rows.append((BASE + "resource.html?id=" + x["id"], x.get("checked") or newest))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, mod in rows:
        lines.append("  <url><loc>%s</loc><lastmod>%s</lastmod></url>"
                     % (escape(loc), escape(mod)))
    lines.append("</urlset>")
    lines.append("")

    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))

    print("sitemap.xml: %d urls (%d pages, %d paths, %d resources), newest lastmod %s"
          % (len(rows), len(PAGES), len(paths), len(items), newest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
