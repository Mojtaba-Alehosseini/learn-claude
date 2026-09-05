# D3 — the search rebuild

**Date:** 6 September 2026
**Status:** spec, awaiting Morteza's approval. No code has been written.
**Measure:** `scripts/test-search.py`, 57 queries. **22 useful today (39%).**

---

## 1. What is broken, and the query that proves each

Attack 2 named five causes. Each is one line of the suite, and each is reproducible today.

| # | Cause | The query | What happens |
|---|---|---|---|
| 1 | No stemming | `does claude make up citations` / `hallucinations` | `hallucinated references` and `hallucinations` return **disjoint** sets. "Reduce hallucinations" is #1 for one and absent from the other. |
| 2 | No synonyms | `marking essays` vs `grading` | `marking essays` → 2 results, both written for students. `grading` → 3, top one is "Demystifying evals for AI agents". |
| 3 | No British spelling | `prioritisation` vs `prioritization` | One result each, different rows, neither about prioritising anything. |
| 4 | No tie-break | `claude code hooks` | Top three all score **34.64**. Order is file order, and the real hooks tutorial is fifth. |
| 5 | `skip_if` is not indexed | `stop claude inventing pixel values` | The card whose `skip_if` contains "invented pixel values" is not returned. |

One correction to the attack's wording, checked in `scripts/build-search-index.py`:
`who_for` **is** indexed, at weight 1. `skip_if` is not indexed at all. Cause 5 is real and
its scope is smaller than reported.

Per role, useful in the top three today:

| role | useful | role | useful |
|---|---|---|---|
| designer | 4 of 7 | student | 2 of 5 |
| business-founder | 3 of 6 | teacher | 2 of 6 |
| developer | 3 of 7 | researcher | 2 of 5 |
| non-technical | 3 of 5 | writer-marketer | 1 of 4 |
| pm | 2 of 7 | data-analyst | **0 of 5** |

---

## 2. The approach, cause by cause

**Stemming — a suffix list, not a library.** One function, applied identically when the
index is built and when a query is parsed. Suffixes in order, longest first: `ational →
ate`, `ization/isation → ize`, `iveness → ive`, `fulness → ful`, `ousness → ous`, `ing`,
`edly`, `ed`, `ies → y`, `es`, `s`. Minimum stem length 4, so `is` and `use` survive. A
short irregular list beside it — `made/making → make`, `wrote/writing → write`,
`ran/running → run` — because the suffix rules cannot reach those and the suite needs
three of them. No Porter implementation, no dependency: the whole point is that the same
twenty lines run in Python and in the browser and can be read in one sitting.

**Synonyms — a table in `data/`, with a written reason per row.** `data/synonyms.json`,
one object per entry: `{"terms": ["grading", "marking", "assessment"], "why": "...",
"added": "2026-09-06"}`. The `why` is required and validated, exactly like `skip_if`: a
synonym nobody can justify is a search result nobody can explain. Expansion happens at
query time, not index time, so the index does not grow and a bad row can be deleted
without a rebuild. First rows, all from the suite: grading/marking, essay/paper/assignment,
citation/reference/bibliography, spreadsheet/excel/csv, cheating/academic integrity/
plagiarism, roadmap/prioritisation/backlog, bookkeeping/accounting/invoicing.

**British and American spelling — pairs, generated, not typed.** A short rule set
(`-ise/-ize`, `-isation/-ization`, `-our/-or`, `-re/-er`, `-ll-/-l-`) applied to the index
vocabulary at build time, producing pairs only where both forms are real English. The
generated list is written to `data/spelling-pairs.json` and printed at build so a wrong
pair is visible rather than buried in a regex.

**Tie-break — deterministic and stated.** When scores are equal within 0.001: better tier
first (`reviewed` → `ai-reviewed` → `previewed` → `listed`), then more recently checked,
then title A→Z. Never file order. The site already sorts "best checked first" by default,
so this is the same ordering the reader has already been shown once.

**`skip_if` in the index, at a lower weight than title and `teaches`.** Weight 1, the same
as `who_for` — below `questions` (5), `keywords` (3), `teaches` (2) and `title` (2). A skip
line is what a resource is *not* for, so it should find a page for somebody who typed the
problem in the resource's own words and never outrank a page that teaches the thing.

---

## 3. What stays exactly as it is

- **No API and no library.** Every part of this is code in this repository.
- **Instant, client-side, on a phone.** The index loads with the page and search runs on
  keypress. If a change cannot hold that, the change does not ship.
- **One algorithm, two runtimes.** `scripts/test-search.py` and `assets/js/search.js` must
  agree. Today they share the index; after this they must also share stemming, synonym
  expansion and the tie-break, and a test asserts that ten sample queries produce the same
  top three in both.
- **The suite is the gate.** No query that is `ok` today may become `bad`.

---

## 4. What it costs

Measured today, before any change:

| | size |
|---|---|
| `data/search-keywords.json` | 352 KB (598 records, 4,051 words, 4,059 phrases) |
| `data/search-keywords.js` (what the browser loads) | 352 KB |

Two of the five changes touch the index. Stemming **shrinks** it: `hallucination`,
`hallucinations` and `hallucinated` collapse into one posting list. Adding `skip_if` grows
it — roughly 598 more short fields, mostly words already in the vocabulary, so the growth
is in posting lists rather than new terms. Spelling pairs and synonyms cost nothing at
index time because both are query-side.

**The estimate is a guess until it is measured, and the plan says so.** The build will
print the before and after size, and the spec's number is replaced by the measurement.

**The budget: 400 KB.** Above that, the first cut is `summary`, which is indexed at 300
characters and is the field the index builder's own comment calls "the marketing summary"
— the one field written to persuade rather than to describe. If that is not enough, the
second cut is phrases for `skip_if` (keep single words only).

---

## 5. How it will be judged

`scripts/test-search.py`, unchanged in shape: 57 queries, each with the role that typed it,
the verdict, and the fragment that must appear in the top three.

- **Before: 22 of 57 useful (39%).**
- **Target: 40 of 57 (70%), and no role below half.** `data-analyst` at 0 of 5 is the one
  that must move most; four of its five failures are causes 1, 2 and 5.
- Every query that changes verdict is re-read by hand before the round closes, because a
  query can pass for the wrong reason.

---

## 6. What this will not fix, plainly

- **`em dash` returns nothing because the catalogue holds nothing.** No row mentions it in
  any indexed field. A synonym cannot conjure a resource. Four rows discuss AI writing
  tells generally, and the honest fix is either an editorial note on one of them or an
  admission that we do not cover it.
- **`typography` returns almost nothing for the same reason.** One row mentions it. A
  design directory that cannot answer "typography" has a content gap, not a search bug.
- **Questions with no answer in the catalogue** — `will ai design replace me`,
  `will my university know i used ai` — will keep returning something adjacent. Search can
  stop returning the *wrong* thing; it cannot invent the right one. The honest end state is
  a zero-result page that says so, which the empty state already does.
- **Ranking by quality.** This spec makes search find what the site holds. Which of three
  found rows is best is what "Start with these three" answers, and it only exists in cells,
  not in search results.

---

## 7. Order of work, once approved

1. Stemmer, shared, with its own unit test. Re-run the suite; record the number.
2. Tie-break. Re-run; record.
3. `skip_if` into the index at weight 1. Re-run; record the number and the index size.
4. Spelling pairs, generated and printed. Re-run; record.
5. Synonym table with reasons, plus its validator. Re-run; record.
6. The cross-runtime test, and the before/after size in the build output.

One commit each, each with its suite number in the message, so a change that helps nothing
is visible as one that helped nothing.
