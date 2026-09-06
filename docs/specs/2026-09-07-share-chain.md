# The share chain — served titles for the three things people send

**Decided 2026-09-07 (FIX-33). URLs are a one-way door, so the scheme is settled here
before any code is written.**

## 1. What is broken

Every resource page serves the same `<title>` and the same `og:title`, and the count is in [STATUS.md](../STATUS.md):

    <title>Resource — Learn Claude</title>
    <meta property="og:title" content="Resource — Learn Claude">

Browse serves `Browse — Learn Claude` for every filter combination. Paths serves
`Paths — Learn Claude`. There is no `og:image`, no `og:url`, no `canonical`. The correct
per-page title is written by JavaScript, which no crawler runs.

Every one of those pages carries a **Copy link** button.

**All ten Attack 3 agents found this without being told to look at metadata.** Four called
it their single worst finding. Three named fixing it as the one thing that would bring them
back. The closing answers are the argument: ten readers said they would return, and every
one named a bookmark, a cell or a shelf rather than the site — *"a raid not a home"*, *"one
page, not the site"*. On a site with no analytics, no accounts and no newsletter, one person
sending another person a link is the entire distribution mechanism.

## 2. The scheme

Ids are already `r-<sha1 prefix>`, derived from the URL by `stable-ids.py` and stable across
renames and reorderings. That is what makes a permanent path possible.

| pattern | count | what it is |
|---|---|---|
| `/r/<id>/` | one per live resource | the resource page |
| `/c/<role>/<level>/` | 40 | one per role-and-level cell |
| `/p/<slug>/` | 7 | one per path |

Each is a directory with an `index.html`, so the trailing slash is the URL and there is no
extension to leak an implementation detail into something people paste.

### What each page serves

**`/r/<id>/`**

- `<title>` and `og:title`: the resource's own title, then ` — Learn Claude`.
- `og:description` and `<meta name="description">`: the `For:` line. **If that is under 120
  characters, the first sentence of `Skip if:` is appended**, because the two together are
  the site's actual product — who it is for and when to skip it — and a short `For:` line
  alone wastes the preview.
- `og:url` and `<link rel="canonical">`: the absolute `/r/<id>/` URL.
- `og:type`: `article`.

**`/c/<role>/<level>/`**

- `<title>` and `og:title`: the site's own words for the cell, built from the same maps the
  interface uses — *Claude for a teacher who has never used it — Learn Claude*.
- `og:description`: the cell's picks, by title, comma-separated, prefixed with *Start with*.
  Where a cell is short of picks or has none, the description says what the cell says.
- The teacher's closing answer was *"send the beginner cell to colleagues"*. A cell is a
  share unit, so it gets a page.

**`/p/<slug>/`**

- `<title>` and `og:title`: the path's title, then ` — Learn Claude`.
- `og:description`: the path's own opening line.

**`og:image`** is one site image for every page in this round. A per-format image — a
different card for a video, a repo, a course — is a later round and is not designed here.

### The old URLs

`resource.html?id=`, `browse.html?role=&level=` and `paths.html?id=` keep working. Nothing
that was ever pasted anywhere breaks. Each one **replaces itself** with the canonical URL
using `location.replace`, so the reader lands on the canonical page and the back button does
not trap them in a redirect.

The browse redirect is deliberately narrow: it fires only when the URL carries **exactly one
role and one level and no other filter and no query**. Any other filter combination is a
view, not a cell, and stays on `browse.html`.

`Copy link` copies the canonical URL. `sitemap.xml` lists canonical URLs only.

## 3. What the build generates

`scripts/build-share-pages.py`, after `build-data-js.py` and before the sitemap, because the
sitemap now reads what it produced.

For each page it takes the matching shell — `resource.html`, `browse.html`, `paths.html` —
and rewrites three things:

1. **The head.** `<title>`, `description`, `og:title`, `og:description`, `og:type`,
   `og:url`, `og:image`, `twitter:card`, and `<link rel="canonical">`.
2. **Every relative path**, by depth. `/r/<id>/` and `/p/<slug>/` are two deep, so
   `assets/css/site.css` becomes `../../assets/css/site.css`; `/c/<role>/<level>/` is three
   deep. Anything already absolute, a fragment, or `mailto:` is left alone.
3. **One inline script** before the page's own scripts:
   `window.LC_ROOT = "../../"; window.LC_ROUTE = {id: "r-…"};`

`LC.param(name)` falls back to `window.LC_ROUTE[name]` when the query string has no such
key, so every page script keeps reading its input exactly as it does today and none of them
needs to know whether it was reached by a query or by a path.

`LC.ROOT` prefixes every internal link the scripts emit. There are twenty of those across
five files; each one is a one-word change and the alternative — `<base href>` — breaks the
skip link and every in-page fragment, and breaks `file://` besides, which CLAUDE.md requires
to keep working.

**Size.** 635 generated files at roughly 2.5 KB each: **about 1.6 MB added to the deploy**,
none of it downloaded by a reader who does not visit that page. The largest cost is 635
extra files in the artifact, not bytes on any reader's connection.

## 4. How it is proved

**A real unfurl.** One resource, one cell and one path URL pasted into a preview debugger,
with the screenshots in the round record. Reading the served HTML is not the same as
watching a crawler read it, and this round is about what a crawler does.

**A gate.** `test-gates.py` plants a missing `og:title` in a generated page and asserts the
build goes red. A share chain that silently stops generating is the same failure this spec
exists to fix, one layer down.

**A check in the build.** `check-share-pages.py`: every live resource has a page, every page
has a non-generic `og:title`, every canonical URL is absolute and matches its own path, and
the sitemap lists canonical URLs only.

## 5. What this does not do

- **No per-format `og:image`.** One site image. A card that looks different for a video and
  a repo is worth doing and is not worth blocking this on.
- **No server-side redirect.** GitHub Pages has none; the old URLs redirect in the browser,
  which means a crawler following an old link sees the old page's generic title. Anything
  already pasted keeps its old preview. Only new links get the new one.
- **No change to how the pages render.** The same JavaScript reads the same data and draws
  the same page. This spec changes what a crawler is told, not what a reader sees.
