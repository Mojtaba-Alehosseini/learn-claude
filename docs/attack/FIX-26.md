# Fix prompt — close the gallery round, then the search spec

Paste everything below the line into Claude Code, in the project folder.

---

Push the eleven commits. Then add one line to `CLAUDE.md` under Working rules, word for
word: *A round ends pushed. Local commits are not done.* The deploy runs on push, and a
live site that lags the repo by a round is a site that lies about what we fixed.

# The 25 rows you did not invent a card for — ruled

**16 gallery rows with no family.** The gallery's own filter does not list them; the
page still does. Apply Rule B on the page: if a role's reader is genuinely served, keep
the row with that tag. If the page belongs to the gallery's "general" tab, it joins a
sixth collection card — *Use cases, general* — tagged `non-technical`, same shape as
the five. Roleless and in no family: remove, and the `skip_if` goes into the Rule B log
so the writing is kept. A card for nobody is noise.

**9 roleless rows in on-roster families.** The family is evidence, the way the gallery
URL was evidence for Rule A. Open the page; if it serves the family's role, tag it and
keep it. If it does not, it joins that family's collection card. Log each.

# Rule B runs both directions

It drops a tag the card denies. It never adds the one the card names. The Vanderbilt
page on AI-detector false accusations singles out non-native English writers, carries
`teacher` only, and is unreachable from the student filter — Attack 1 filed it, Attack 2
filed it again. Extend the check: a persona named in `who_for` or `skip_if` that maps to
a role not tagged is a printed warning. Sweep the list once, page decides, log each.
Vanderbilt is the test case; it must come out tagged `student`.

# Three instruments this round earned

1. **The typed-number check reaches `picks.json`.** Every reason and every runner-up
   line. Then the 75: a count in a reason is either re-measured from the pool at build
   time or removed. Prefer removal — *"the only one not tied to a publisher"* is a
   reason, *"the only one of 78"* is a number that rots.
2. **A stale cell re-reads its own sentences.** Reasons containing pool claims —
   "only", "every", "all", "none of", "the one" — are listed on every stale event, and
   the re-pick step cannot close the cell until each is re-verified or rewritten. You
   did this by hand for 30 cells; make it the step.
3. **The copy-claims check scans every shipped file.** HTML, every JS file, the copy
   deck. Prove it: plant one banned sentence in `home.js`, watch it fail, remove it.
   Then confirm the live home page does not ship it.

# Record the decision where decisions live

Write `docs/specs/2026-09-06-gallery-collections.md`: what the measurement showed,
Rules A, B and C as applied, the level definition now in the copy deck, and a pointer
to STATUS.md for every number. Then THE-PROJECT.md: part 11's composition paragraph is
false now — 61% decided knowingly, builder a monoculture — rewrite it to what is true
and point at the spec. Part 10 loses D12.

# Verify on the live site, not the local one

After the push deploys: the five collection cards, the "How well checked" filter
round-tripping through the URL, the thin-level offer on `teacher` + `builder`, one
re-picked cell, on desktop and at 375px. The last two rounds were verified locally.

# D3 — the search spec, and stop

Search is a rebuild, and the rule is spec before build. Write
`docs/specs/2026-09-06-search-rebuild.md` and **stop for my approval**. It covers:

- the five causes from Attack 2, each with its failing query from the suite
- the approach per cause: stemming (a suffix list, not a library), a synonym table in
  `data/` with a written reason per row, British/American pairs, a deterministic
  tie-break (checked date, then title), and `skip_if`/`who_for` in the index at a
  lower weight than title and `teaches`
- what stays: no API, no library, instant on a phone, the same algorithm in
  `test-search.py` and the browser
- the cost: index size before and after, measured; if it grows past what a phone loads
  instantly, say what gets cut
- the measure: the 57-query suite, useful-top-three share per role before, and the
  target after
- what it will not fix, said plainly

Two pages. No code until I say go.

# Not this round

D9 price and D13 the "we" follow the search build.

# Not yours

STATUS.md "Needs a person" and part 10. The human test.

# Commits

The CLAUDE.md line, the 25 rows, Rule B both ways, the three instruments, the spec and
docs, the search spec — one job each. `FIX-26.md` with the round. **Push.** Finish with
what surprised you, what you got wrong, and whether it was in CLAUDE.md.

---

# The round, as run

Measured against `fdae55e`, the commit FIX-25 ended on.

## The catalogue

| | before | after |
|---|---|---|
| resources | 600 | 598 |
| official Anthropic | 355 (59.2%) | 353 (59.0%) |
| rows whose tags changed | — | 15 |
| rows whose card was rewritten | — | 18 |
| rows removed | — | 2 |

Role counts that moved: business-founder 183->178, designer 49->50, non-technical 156->153, pm 129->126, researcher 80->82, student 78->80, writer-marketer 76->84.

## The 25 rows

All 25 pages were fetched and read. 18 kept with the card rewritten to what the page says,
5 left alone because the page names nobody in particular, 2 removed. Four more tags fell
out of the rewrites: once a card says who a page is for, a tag the page does not serve has
nowhere to hide.

The gallery now has **zero** rows carrying a tag their card denies and **zero** rows
fitting no role. Every decision is in `docs/attack/2/RULE-B-LOG.md`.

## Rule B in the other direction

Fifty-eight rows named a role they did not carry. Nine survived their page. Vanderbilt's
AI-detector page gains `student` — a student searching "detector" now finds it, which
neither Attack 1 nor Attack 2 could do.

Four role patterns were tightened first: `tutor` matched "tutorial", `coder` matched
"non-coder", `scientist` matched "data scientist", `content` matched the word anywhere.

## The three instruments

1. **`scripts/check-typed-numbers.py`** reads all 212 reason lines in `picks.json` and
   fails on a count of the pool. Twenty counts removed across two passes. "One" is
   deliberately allowed: it is a uniqueness claim, and instrument 2 owns those.
2. **A stale cell lists its own pool claims and cannot close without `claims_checked_on`.**
   It found two false claims on its first run, both made false by tags added an hour
   earlier in this same round.
3. **The copy-claims check finds its own surfaces** — 12 files, including the copy deck,
   which turned out to be prescribing a killed sentence and quoting another one verbatim.
   Proved by planting "checked by hand" in `home.js`, watching the build exit 1, and
   removing it.

## Where the decisions live now

`docs/specs/2026-09-06-gallery-collections.md` holds what the measurement showed and the
three rules as applied. THE-PROJECT.md part 11 is rewritten from measurement and points at
it; part 10 no longer carries the 61%-Anthropic acceptance, because that decision was
taken about rows the measurement then showed were not doing the work their tags claimed.

`docs/specs/2026-09-06-search-rebuild.md` is written and stops for approval.

## Still open

Rule B has only ever been applied to the use-case gallery. Run over the whole catalogue it
reports 62 rows outside the gallery carrying a tag their card denies, and 60 more that fit
no role. That is a round of its own.
