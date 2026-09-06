# The unfurl proof — FIX-33

One resource, one cell, one path, pasted into a preview debugger against the live site
on 2026-09-07. Each scan below is a link you can re-run: opengraph.xyz keeps the result
at a URL made from the scanned page, so nothing here has to be taken on trust.

The debugger is [opengraph.xyz](https://www.opengraph.xyz/). It fetches the page as a
social platform would, renders the card, and grades the head.

---

## 1 — a resource

Scanned: `https://mojtaba-alehosseini.github.io/learn-claude/r/r-e925795001/`
Re-run: <https://www.opengraph.xyz/url/https%3A%2F%2Fmojtaba-alehosseini.github.io%2Flearn-claude%2Fr%2Fr-e925795001%2F>

The card renders: the site's own image, the domain `MOJTABA-ALEHOSSEINI.GITHUB.IO`, and
the title **"Proposed Revisions to SPJ's Code of Ethics (2026)"** — the resource, not the
site.

What the inspector said, in its words:

| check | verdict |
|---|---|
| `og:title` present | ✅ "Proposed Revisions to SPJ's Code of Ethics (2026)" — 49 characters |
| `og:title` length | ✅ 49 characters — within the 60-character target |
| `og:description` | ⚠️ **128 characters — social previews often show ~125 characters and may truncate on mobile** |
| `<title>` present | ✅ |
| `meta description` | ✅ |
| `og:image` loads | ✅ 41 KB image/png |
| `og:image` dimensions | ✅ 1200×630 — matches what every major platform expects |
| `twitter:card` | ✅ `summary_large_image` is set |
| `og:site_name` | ✅ "Learn Claude" |
| `og:image` conversion text | ⚠️ no call-to-action detected (a marketing note, not a fault) |

---

## 2 — a cell

Scanned: `https://mojtaba-alehosseini.github.io/learn-claude/c/writer-marketer/basic/`
Re-run: <https://www.opengraph.xyz/url/https%3A%2F%2Fmojtaba-alehosseini.github.io%2Flearn-claude%2Fc%2Fwriter-marketer%2Fbasic%2F>

Title: **"Claude for a writer who has used it a little — Learn Claude"** — the cell says
who it is for, in the roster's own words, before anyone opens it.

Description: *"Start with Wikipedia:Signs of AI writing, Claude, Editor, Claude Cowork:
The Ultimate AI Agent for Writers (Full Tutorial)."*

| check | verdict |
|---|---|
| `og:title` present | ✅ 59 characters |
| `og:title` length | ✅ 59 characters — within the 60-character target |
| `og:description` | ✅ 123 characters — within the recommended range |
| `og:image` | ✅ 41 KB, 1200×630 |
| `twitter:card` | ✅ `summary_large_image` |
| errors | 0 |

---

## 3 — a path

Scanned: `https://mojtaba-alehosseini.github.io/learn-claude/p/writing-you-sign/`
Re-run: <https://www.opengraph.xyz/url/https%3A%2F%2Fmojtaba-alehosseini.github.io%2Flearn-claude%2Fp%2Fwriting-you-sign%2F>

Title: **"Using Claude on work you put your name to — Learn Claude"**.

| check | verdict |
|---|---|
| `og:title` present | ✅ 56 characters |
| `og:title` length | ✅ 56 characters — within the 60-character target |
| `og:description` | ✅ 97 characters — within the recommended range |
| `og:image` | ✅ 41 KB, 1200×630 |
| `twitter:card` | ✅ `summary_large_image` |
| errors | 0 |

---

## What the proof found

**The description cap is set to the wrong number, and the comment beside it claims a
measurement that was never taken.** `build-share-pages.py` caps a description at 200
characters and its comment says "most previews cut a description around 200". The
debugger says ~125, and it flagged the resource page for exactly that.

Measured across the built pages: 549 of 632 descriptions run past 125 characters. The
longest is 203.

The trade is real in both directions, so it is a decision rather than a fix:

- The `For:` line alone has a median length of 104 characters, and 156 of 585 rows run
  past 125. Cap at 125 and roughly three rows in four keep their whole `For:` line — but
  the `Skip if:` sentence the spec appends almost never fits any more, so the second
  half of the ruled description disappears.
- Keep 200 and the description keeps both sentences on desktop, where more is shown, and
  is cut mid-sentence on a phone.

Nothing here was changed on that basis. The comment was corrected to say what the
debugger actually reports; the constant is left at 200 until the trade is ruled.

**A note on what is not in this file.** These are the debugger's own words and its
re-runnable links, not pictures of them: the screenshots were taken and read, and the
in-app browser this round could not write them to disk. Every claim above can be
re-checked by opening the three links.
