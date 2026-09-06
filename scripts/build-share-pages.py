#!/usr/bin/env python3
"""
One served page per thing a person can send.

    python3 scripts/build-share-pages.py

WHY THIS EXISTS

Every resource page served `<title>Resource — Learn Claude</title>` and the same
`og:title`, on 588 pages, each with a Copy link button. Browse served one constant, Paths
another. The correct per-page title was written by JavaScript, which no crawler runs.

All ten Attack 3 agents found it without being told to look at metadata; four called it
their worst finding; three named fixing it as the one thing that would bring them back.
The site has no analytics, no accounts and no newsletter - one person sending another a
link is the whole distribution mechanism, and the preview at the end of it said nothing.

The scheme is settled in docs/specs/2026-09-07-share-chain.md and not re-argued here.

WHAT IT WRITES

    r/<id>/index.html            one per live resource
    c/<role>/<level>/index.html  one per cell
    p/<slug>/index.html          one per path

Each is the matching hand-written shell with three changes: a real head, every relative
reference re-pointed by depth, and one inline script seeding `window.LC_ROOT` and
`window.LC_ROUTE` so the page's own JavaScript reads its input exactly as it always has.

Generated directories are removed and rewritten on every run, so a resource that leaves
the catalogue does not leave a page behind claiming it is still here.
"""

import io
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://mojtaba-alehosseini.github.io/learn-claude/"
IMAGE = SITE + "assets/og-card.png"
OUT_DIRS = ("r", "c", "p")

# A description short enough to waste the preview. The For: line alone is often one
# clause; the site's product is that line AND the skip line, so below this the first
# sentence of Skip if: is appended. See section 2 of the spec.
SHORT = 120

# What a preview actually shows, measured on opengraph.xyz against the built pages
# rather than taken from memory: X and LinkedIn truncate a title past about 60
# characters, and most previews cut a description around 200. Over those limits the
# reader sees an ellipsis where the judgement should be.
TITLE_MAX = 60
DESC_MAX = 200


def load(name):
    with io.open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def esc(s):
    return (str(s or "").replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def fit(text, limit):
    """Cut on a word boundary, and only when there is something to cut."""
    text = " ".join(str(text or "").split())
    if len(text) <= limit:
        return text
    cut = text[:limit - 1]
    if " " in cut:
        cut = cut[:cut.rindex(" ")]
    return cut.rstrip(" ,;:.") + "\u2026"


def suffixed(title):
    """`… — Learn Claude` where it fits, and the bare title where it does not.

    og:site_name already carries "Learn Claude", so the suffix is a courtesy rather than
    information - and spending fifteen of sixty characters on it is how a title that
    named the thing ends up truncated before it gets there."""
    full = "%s — Learn Claude" % title
    return full if len(full) <= TITLE_MAX else fit(title, TITLE_MAX)


def first_sentence(s):
    s = str(s or "").strip()
    m = re.search(r"(?<=[.!?])\s", s)
    return (s[:m.start() + 1] if m else s).strip()


def shell(name):
    return io.open(os.path.join(ROOT, name), encoding="utf-8").read()


REL = re.compile(r'(\s(?:href|src)=")(?!https?:|//|#|mailto:|data:)([^"]+)(")')


def repoint(html, depth):
    """Every relative href and src, moved `depth` directories down."""
    prefix = "../" * depth
    return REL.sub(lambda m: m.group(1) + prefix + m.group(2) + m.group(3), html)


HEAD = re.compile(r"<title>.*?</title>.*?<meta property=\"og:type\"[^>]*>", re.S)


def head_block(title, description, url, og_type):
    return (
        "<title>{t}</title>\n"
        '<meta name="description" content="{d}">\n'
        '<link rel="canonical" href="{u}">\n'
        '<meta property="og:title" content="{t}">\n'
        '<meta property="og:description" content="{d}">\n'
        '<meta property="og:url" content="{u}">\n'
        '<meta property="og:site_name" content="Learn Claude">\n'
        '<meta property="og:image" content="{i}">\n'
        '<meta property="og:type" content="{k}">'
    ).format(t=esc(title), d=esc(description), u=esc(url), i=esc(IMAGE), k=og_type)


ROUTE = re.compile(r"(\n<script src=\")")


def write_page(rel_dir, html, depth, title, description, url, route, og_type="website"):
    html = HEAD.sub(lambda _m: head_block(title, description, url, og_type), html, count=1)
    html = html.replace('<meta name="twitter:card" content="summary">',
                        '<meta name="twitter:card" content="summary_large_image">')
    html = repoint(html, depth)
    seed = ('\n<script>window.LC_ROOT = "%s"; window.LC_ROUTE = %s;</script>'
            % ("../" * depth, json.dumps(route)))
    html = ROUTE.sub(lambda m: seed + m.group(1), html, count=1)

    out = os.path.join(ROOT, rel_dir)
    os.makedirs(out, exist_ok=True)
    with io.open(os.path.join(out, "index.html"), "w", encoding="utf-8",
                 newline="\n") as f:
        f.write(html)


def resource_description(x):
    who = str(x.get("who_for") or "").strip()
    skip = first_sentence(x.get("skip_if"))
    if who and len(who) < SHORT and skip:
        return "%s Skip if: %s" % (who, skip)
    return who or skip or "A checked resource for learning Claude."


def main():
    items = [x for x in load("items.json") if x.get("status") == "live"]
    paths = load("paths.json")
    picks = load("picks.json")["cells"]
    ui = io.open(os.path.join(ROOT, "assets", "js", "ui.js"), encoding="utf-8").read()

    def label_map(name):
        """The interface's own words, imported rather than copied.

        A generated title that says "a teacher" while the site has started saying
        something else is exactly the drift this project keeps finding. The maps are
        already valid JSON in ui.js, so they are read, not restated.
        """
        m = re.search(r"LC\.%s = (\{.*?\});" % name, ui, re.S)
        if not m:
            raise SystemExit("ui.js no longer defines LC.%s" % name)
        return json.loads(m.group(1))

    roles = label_map("ROLE")
    levels = label_map("LEVEL")

    for d in OUT_DIRS:
        shutil.rmtree(os.path.join(ROOT, d), ignore_errors=True)

    res_shell, br_shell, pa_shell = (shell("resource.html"), shell("browse.html"),
                                     shell("paths.html"))

    for x in items:
        write_page("r/%s" % x["id"], res_shell, 2,
                   suffixed(x["title"]),
                   fit(resource_description(x), DESC_MAX),
                   "%sr/%s/" % (SITE, x["id"]),
                   {"id": x["id"]}, og_type="article")

    n_cells = 0
    for role, role_label in roles.items():
        for level, level_label in levels.items():
            cell = picks.get("%s|%s" % (role, level))
            names = [p["url"] for p in (cell or {}).get("picks") or []]
            titles = [x["title"] for x in items if x["url"] in names]
            desc = ("Start with " + ", ".join(titles) + "."
                    if titles else
                    "Everything we have checked for %s who has %s."
                    % (role_label, level_label))
            write_page("c/%s/%s" % (role, level), br_shell, 3,
                       suffixed("Claude for %s who has %s"
                                % (role_label, level_label)),
                       fit(desc, DESC_MAX),
                       "%sc/%s/%s/" % (SITE, role, level),
                       {"role": role, "level": level})
            n_cells += 1

    for p in paths:
        write_page("p/%s" % p["id"], pa_shell, 2,
                   suffixed(p["title"]),
                   fit(p.get("for"), DESC_MAX),
                   "%sp/%s/" % (SITE, p["id"]),
                   {"id": p["id"]})

    # The manifest, so that the sitemap and the checker do not each keep their own idea
    # of which pages exist. Three copies of that list is three chances to disagree, and
    # the first symptom would be a page nobody checks or a sitemap entry that 404s.
    manifest = {"generated": "scripts/build-share-pages.py",
                "pages": ([{"rel": "r/%s/" % x["id"], "kind": "resource",
                            "title": x["title"], "lastmod": x.get("checked") or ""}
                           for x in items] +
                          [{"rel": "c/%s/%s/" % (r, l), "kind": "cell", "title": None,
                            "lastmod": ""}
                           for r in roles for l in levels] +
                          [{"rel": "p/%s/" % p["id"], "kind": "path",
                            "title": p["title"], "lastmod": ""} for p in paths])}
    with io.open(os.path.join(ROOT, "data", "share-pages.json"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n")

    total = sum(os.path.getsize(os.path.join(dp, f))
                for d in OUT_DIRS
                for dp, _dn, fn in os.walk(os.path.join(ROOT, d))
                for f in fn)
    print("share pages: %d resources, %d cells, %d paths — %.1f MB of served titles"
          % (len(items), n_cells, len(paths), total / 1024.0 / 1024.0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
