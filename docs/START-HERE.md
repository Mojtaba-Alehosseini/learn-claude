# Prompt for a new Claude Code session

Open Claude Code in `C:\Projects\Claude teaching website` and paste everything below
the line.

---

I'm continuing work on **Learn Claude**, a curated directory of the best places to learn
Anthropic's Claude.

**Read `docs/THE-PROJECT.md` first.** It is the whole project in one file — what the site
is, what it holds, what is decided, what is open, and every number measured from the data
rather than remembered. Then `CLAUDE.md` for how I work and `README.md` for the rules that
are easy to break and expensive to fix.

**This file deliberately carries no numbers.** It used to say "353 resources, 3 paths" and
was wrong within a week, because a second copy of a figure is how one stale file becomes
two. Counts live in THE-PROJECT.md, and THE-PROJECT.md says how it measured them.

**The site already exists and works. Do not rebuild it.** Plain HTML, CSS and vanilla
JavaScript, hand-written, no framework and no build step for the browser. Open
`index.html` — no server needed; the data loads through `<script>` tags on purpose.

## How to work on it

```
python3 scripts/install-hooks.py   # once per clone - see below
./build.sh          # after any change to data/*.json — regenerates ids, sources,
                    # paths, the search index, and the .js mirrors
python3 scripts/validate-catalogue.py     # the catalogue's own rules
python3 scripts/validate-picks.py         # the "start with these three" rules
python3 scripts/test-search.py            # the exact algorithm the browser runs
```

The hook is worth the one command. It refuses to commit a control character in a
tracked text file — a literal backspace, which is what a `\b` becomes when a regex goes
through a shell heredoc — and it runs the catalogue validator locally, so a failure
arrives before the commit rather than after the push.

To see a change in the browser, hard-reload — the CSS caches aggressively.

## Rules I will hold you to

1. **Never invent a resource.** Real URL, opened, with a checked date. If it is not
   verified it does not ship.
2. **`skip_if` may never be empty.** It is the product, not a field.
3. **Only a person may write `tier: reviewed`.** No automated step may claim a human read
   something. The allowance is a file, and it is 0.
4. **Nothing may be edited to satisfy a checker.** Not a title, not a role tag, not a
   pick. If a check fires, either the data is wrong or the check is — fix whichever it
   is, and say which.
5. **A constraint may reject a set of picks; it may never pull an item into one.**
6. **Every value comes from `assets/css/tokens.css`.** No hardcoded colour, size or
   radius. No box-shadow, no gradient. Body copy is serif at 20px. Clay appears once per
   page, on one filled button.
7. **Measure before you change a design value.**

## Traps that already cost me time

- **A headless test passing does not mean the page looks right.** Real problems have
  survived every automated check and were only visible in a browser. Open it. (The
  reverse also happens: the preview pane can serve a stale frame. When a screenshot and
  the DOM disagree, read the DOM.)
- **Ids come from the URL, never from list position.** An earlier version numbered items
  by row; when the catalogue grew, every learning path silently re-pointed at different
  resources while still printing confident explanations. See `scripts/stable-ids.py`.
- **Do not strip the query string when normalising a URL.** A YouTube video's identity
  lives in `?v=`. Stripping it collapsed 70 videos into one.
- **`lstrip("www.")` strips a set of characters, not a prefix.** It turned `wotai.co` into
  `otai.co` and quietly silenced two duplicate checks. One shared helper now, in
  `stable-ids.py`.
- **Never dilate icon strokes to even out their weight.** It swallows fine detail.
  Regenerate instead.
- **Animation timings live in two places.** If a JS timeout is shorter than its CSS
  transition, two things animate at once. Keep them equal.

## What is left

In THE-PROJECT.md, part 10 (open right now) and part 11 (what is weak). Read those rather
than a list here that will rot.

Ask me before doing anything large. Short, direct answers — I don't have time to read
long explanations.
