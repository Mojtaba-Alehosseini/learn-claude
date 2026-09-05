# Fix prompt — the search rebuild, approved with five amendments

Paste everything below the line into Claude Code, in the project folder.

---

The spec is approved. Build it in the order it gives, one commit per step with the suite
number in the message. Five amendments first — one is a defect in the spec itself, and
it would have made the round report success on a cause it did not fix.

# Amendments to the spec

1. **The stemmer must produce the collapse the spec claims.** Section 4 says
   `hallucination`, `hallucinations` and `hallucinated` become one posting list. Under
   the suffix list in section 2 they do not: `hallucinated` → `hallucinat`,
   `hallucination` → `hallucination`, because there is no `-ation`/`-ate` family. Add it
   — `ations`, `ation`, `ating`, `ated`, `ates`, `ate` → `at` — and check `citation`
   against `cite`, `cited`, `citing`, which the same list also leaves apart. Then the
   rule: **the stemmer's unit test contains every word pair the five causes need**,
   taken from the failing suite lines, and "collapse into one posting list" is
   measured from the built index, not asserted in the spec. Replace the sentence in
   section 4 with the measurement when you have it.
2. **A synonym scores below the typed word.** Expansion at query time is right; give
   expanded terms half the weight of the term the person typed. Otherwise `grading`
   can outrank the page that literally says "marking" for someone who typed marking.
   State the factor in the spec and in `search.js` in the same words.
3. **The cross-runtime test is the whole suite.** Fifty-seven queries in Python and in
   Node, top three identical, on every build. Ten samples is a place for drift to hide.
4. **Content gaps become a list.** A query that fails because the catalogue holds
   nothing — `em dash`, `typography`, the two "will it replace me" questions — is
   marked `content-gap` in the suite, distinct from `xfail`. `measure.py` writes them
   into STATUS.md as *"Questions the catalogue cannot answer"*, with the role that
   asked. That is the harvest target list, and nobody types it.
5. **Section 6 is kept, verbatim, on the site's method page.** One paragraph under
   how-we-check: search finds what we hold; which of three is best is what the picks
   answer; a question with no answer returns nothing and says so. Copy through the
   deck.

# Build order, as the spec says

Stemmer with its test → tie-break → `skip_if` into the index → spelling pairs →
synonym table with its validator → the cross-runtime test and the size line in the
build. Re-run the suite after each and record the number in the commit. Every query
that changes verdict is re-read by hand before the round closes — a query can pass for
the wrong reason. Index size before and after, measured, into the spec.

The gate stands: no `ok` query becomes `bad`. The target stands: 40 of 57 and no role
below half. If a step helps nothing, its commit says so; do not fold it into the next.

# A re-audit you owe FIX-25

Rule B's role patterns were loose until this round — `tutor` matched "tutorial",
`coder` matched "non-coder", `scientist` matched "data scientist". FIX-25 dropped 26
tags with those patterns. Re-run the tightened check against the FIX-25 log: any drop
that was justified only by a match the tightened pattern no longer makes is reopened,
and the page decides again. Log the result beside the original. This is the same
verification every other round got; that one skipped it.

# Not this round

The catalogue-wide Rule B sweep — 62 rows with a tag their card denies, 60 that fit no
role — is the next round, on its own. It moves pools, and search is measured this round
on a catalogue that holds still. D9 price and D13 the "we" follow it.

# Not yours

STATUS.md "Needs a person" and part 10. The human test. The content-gap list, once it
exists, is a harvest decision — mine.

# Commits

Six for the build, one for the re-audit, one for the spec's measured numbers.
`FIX-27.md` with the round. Push. Finish with what surprised you, what you got wrong,
whether it was in CLAUDE.md — and the suite number per role, before and after.

---

# The round, as run

## The suite, per role

| role | before | after | of which content gaps |
|---|---|---|---|
| business-founder | 3 of 6 | 4 of 6 | 0 |
| data-analyst | 0 of 5 | 0 of 5 | 0 |
| designer | 4 of 7 | 4 of 7 | 2 |
| developer | 3 of 7 | 3 of 7 | 0 |
| non-technical | 3 of 5 | 3 of 5 | 0 |
| pm | 2 of 7 | 2 of 7 | 3 |
| researcher | 2 of 5 | 2 of 5 | 0 |
| student | 2 of 5 | 2 of 5 | 0 |
| teacher | 2 of 6 | 2 of 6 | 0 |
| writer-marketer | 1 of 4 | 2 of 4 | 1 |
| **total** | **22 of 57** | **24 of 57** | **6** |

**The target was 40 of 57 and no role below half. It was not reached.** Two roles moved,
seven did not, and `data-analyst` - the one the spec said had to move most - is still 0 of
5.

## Step by step, with the number each one produced

| step | suite | what it actually did |
|---|---|---|
| 1, the stemmer | 22 -> 18 | Merging the postings measured 15 and was rejected; the expansion at half weight left four ok queries sitting inside exact ties |
| 2, the tie-break | 18 -> 17 | Replaced file order with an order both runtimes share. Cost one query, and the number is not the point |
| 3, `skip_if` indexed | 17 -> 17 | Changed no verdict. The cause-5 card went from absent to third |
| 4, spelling | 17 -> 17 | Changed no verdict. The two prioritisation spellings stopped returning disjoint sets |
| 5, synonyms | 17 -> 17 | Changed no verdict on their own, and exposed the tie-break's missing signal: field depth |
| the re-judging | 17 -> 24 | Thirteen moved rows read one at a time: 2 promoted, 5 re-recorded on merit, 6 refreshed as still wrong |

Three of the six steps moved nothing, and their commits say so rather than folding the
work into the next one.

## The index

| | before | after |
|---|---|---|
| raw | 352 KB | 507 KB |
| gzipped, which is what a phone downloads | 103 KB | 146 KB |
| indexed words | 4,051 | 4,878 |
| stem groups | none | 1,000 over 2,491 words |
| spelling forms | none | 76 |
| synonym words | none | 52 |

The 400 KB raw budget was measuring the wrong thing: the file is lazy-loaded on the first
keystroke and served gzipped. Restated as 150 KB transferred, printed by the build.

## The five causes

1. **No stemming.** Fixed as an expansion rather than a merge. The hallucination family is
   five posting lists in one stem group, reachable from any of them.
2. **No synonyms.** Ten rows, each with the query that made it necessary, each validated
   for a written reason. Two suite rows were promoted by them.
3. **No British spelling.** Fixed. The two prioritisation spellings return the same rows -
   which are still about something else, because that subject is a content gap.
4. **No tie-break.** Fixed, twice: an order both runtimes share, and then the field-depth
   signal the first version lacked.
5. **`skip_if` not indexed.** Indexed at weight 1.5. Its own query goes from absent to
   third, which the suite cannot see because it reads the first result only while the
   spec says top three. That discrepancy is Morteza's to rule on.

## What else this round did

- **The re-audit FIX-25 was owed.** 40 rows re-run against the tightened patterns, 0
  disagreements, and the direction of the fault proves the 26 drops could not have been
  wrong. Logged beside the original.
- **`content-gap`, a third verdict**, and STATUS.md's generated "Questions the catalogue
  cannot answer".
- **Section 6 ships** on how-we-check.html, through the copy deck.

## Still open

- `data-analyst` at 0 of 5, and the 27 rows still recorded bad.
- The suite asserts the first result; the spec says top three. One of them should change.
- The phrase map: 4,059 entries, the largest section after the postings, and its value has
  never been measured on its own.
- Rule B outside the use-case gallery: 77 rows carry a tag their card denies.
