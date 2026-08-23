# Prompt for a new Claude Code session

Open Claude Code in `C:\Projects\Claude teaching website` and paste everything below
the line.

---

I'm continuing work on **Learn Claude**, a curated directory of the best places to learn
Anthropic's Claude. Read `CLAUDE.md` and `README.md` first — they hold my working rules
and the five rules that are easy to break and expensive to fix.

**The site already exists and works. Do not rebuild it.** It is plain HTML, CSS and
vanilla JavaScript, hand-written, no framework and no build step. Open `index.html` to
see it — no server needed, the data loads through `<script>` tags on purpose.

## Where it stands

- **353 resources**, 0 dead links, every one with a link, a summary, who it's for,
  **who should skip it**, and the date we checked
- **5 pages**: `index.html` (two questions), `browse.html` (filters + search),
  `paths.html`, `resource.html`, `how-we-check.html`
- **47 hand-drawn icons**: 10 roles × 4 levels, plus one per format
- **Search** with no API call — keyword matching over hidden fields, weighted by IDF
- **3 learning paths**, each step carrying the reason it sits at that position
- Git initialised, 2 commits, clean tree

## How to work on it

```
./build.sh          # after any change to data/*.json — regenerates ids, sources,
                    # paths, the search index, and the .js mirrors
python3 scripts/test-search.py     # runs the exact algorithm the browser runs
```

To see a change in the browser, hard-reload — the CSS caches aggressively.

## Rules I will hold you to

1. **Never invent a resource.** Real URL, opened, with a checked date. If it is not
   verified it does not ship.
2. **`skip_if` may never be empty.** `scripts/validate-report.py` rejects entries
   without one. It is the product, not a field.
3. **Only a person may write `tier: reviewed`.** No automated step may claim a human
   read something.
4. **Every value comes from `assets/css/tokens.css`.** No hardcoded colour, size or
   radius anywhere.
5. **No box-shadow, no gradient.** Elevation is tone plus a 1px hairline. Body copy is
   serif at 20px. Clay appears once per page, on one filled button.
6. **Measure before you change a design value.** Last session I nearly narrowed the card
   text until I measured it at 72 characters per line — inside the comfort range.

## Traps that already cost me time

- **A headless test passing does not mean the page looks right.** Four real problems
  survived every automated check and were only visible in a browser. Open it.
- **Ids come from the URL, never from list position.** An earlier version numbered items
  by row; when the catalogue grew, every learning path silently re-pointed at different
  resources while still printing confident explanations. See `scripts/stable-ids.py`.
- **Do not strip the query string when normalising a URL.** A YouTube video's identity
  lives in `?v=`. Stripping it collapsed 70 videos into one.
- **Never dilate icon strokes to even out their weight.** I tried it once; it swallowed
  the fine detail and ruined a batch of drawings. Regenerate instead.
- **Animation timings live in two places.** If a JS timeout is shorter than its CSS
  transition, two things animate at once. Keep them equal.

## What is actually left, in the order I care about

1. **Deploy it.** Never done. Static host — GitHub Pages, Cloudflare Pages or Netlify.
   `docs/design/reference/icon-drafts/` is 29 MB and must not ship; it is already
   gitignored.
2. **An accessibility pass.** Never run. Contrast is designed for but unverified in the
   browser; check focus order, the mobile filter sheet, and that the result count
   announces.
3. **Thin spots in the catalogue.** `designer` has 29 resources and `never-used` has 52.
   Beginners are the main audience, so 52 is the number that bothers me most.
4. **171 of 353 resources publish no date.** Mostly documentation, which genuinely
   prints none. The cards say "No publish date given" rather than implying freshness.
   Leave it honest unless you can find real dates.
5. **Nothing is `reviewed`.** Nobody has finished a course end to end. This is the
   honest gap in the site's promise and only I can close it.

Ask me before doing anything large. Short, direct answers — I don't have time to read
long explanations.
