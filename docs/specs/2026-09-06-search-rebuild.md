# D3 — the search rebuild

**Date:** 6 September 2026
**Status:** approved 6 September 2026, with five amendments, all folded in below and
marked where they sit. Built in FIX-27.
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
index is built and when a query is parsed. Suffixes in order, longest first:

    ational → ate      ization/isation → ize      iveness → ive
    fulness → ful      ousness → ous
    ations ation ating ated ates ate → (removed)
    ing  edly  ed  ies → y  es  s  e

**Amendment 1, and it is a defect in this spec rather than a refinement.** The first draft
had no -ate family at all, and section 4 nonetheless claimed the stemmer would collapse
`hallucination`, `hallucinations` and `hallucinated` into one posting list. It would not:
`hallucinated` reaches `hallucinat` through the `ed` rule and `hallucination` does not move
at all, so cause 1 would have been reported fixed while the two words stayed in separate
posting lists and the index still shrank for unrelated reasons. The family is added.

**It is `→ (removed)`, not `→ at`.** Removing the suffix collapses `hallucinate`,
`hallucinated`, `hallucinating`, `hallucination` and `hallucinations` onto `hallucin`.
Mapping it to `at` collapses those five onto `hallucinat` equally well, but it leaves
`citation` at `citat` while `cite`, `cited` and `citing` reach `cit`, and cause 1's other
half is exactly a citation query. Removal plus a trailing-`e` rule brings all four to
`cit`.

**Minimum stem length 3, not 4.** `citation` → `cit` is three characters, and at a
minimum of 4 the whole citation family fails to collapse. The cost of 3 is more collisions
(`site` and `sit` become one term), so the build prints the largest collision groups and
the vocabulary count before and after, and a person reads them once.

A short irregular list sits beside the rules — `made/making → make`, `wrote/writing →
write`, `ran/running → run` — because no suffix rule reaches those and the suite needs
three of them.

**The unit test contains every word pair the five causes need**, taken from the failing
suite lines rather than invented: hallucination/hallucinations/hallucinated/hallucinate,
citation/citations/cite/cited/citing, prioritise/prioritisation/prioritize/prioritization,
grade/grading/graded, mark/marking/marked, invent/inventing/invented, cheat/cheating,
write/writing/wrote. Each asserts that the members reach one stem, and that a listed
non-pair does not.

No Porter implementation, no dependency: the whole point is that the same twenty-odd lines
run in Python and in the browser and can be read in one sitting.

**Synonyms — a table in `data/`, with a written reason per row.** `data/synonyms.json`,
one object per entry: `{"terms": ["grading", "marking", "assessment"], "why": "...",
"added": "2026-09-06"}`. The `why` is required and validated, exactly like `skip_if`: a
synonym nobody can justify is a search result nobody can explain. Expansion happens at
query time, not index time, so the index does not grow and a bad row can be deleted
without a rebuild.

**Amendment 2: an expanded term scores at half the weight of the term the person typed.**
`SYNONYM_WEIGHT = 0.5`, stated in this sentence and in `search.js` in the same words.
Without it, somebody who types *marking* can be handed the page that says *grading* above
the page that says *marking*, and the site would be overruling the reader's own word. Half
is enough to surface a page that uses the other word and never enough to outrank an exact
hit. First rows, all from the suite: grading/marking, essay/paper/assignment,
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
  expansion and the tie-break. **Amendment 3: the cross-runtime test is the whole suite** —
  all 57 queries, run in Python and in Node, top three identical, on every build. Ten
  samples is a place for drift to hide, and the drift this test exists to catch is exactly
  the kind that shows up on the queries nobody chose as a sample.
- **The suite is the gate.** No query that is `ok` today may become `bad`.

---

## 4. What it cost — measured, and not what this section first claimed

|  | before | after |
|---|---|---|
| `data/search-keywords.json`, raw | 352 KB | 507 KB |
| the same file gzipped, which is what a phone downloads | 103 KB | 146 KB |
| indexed words | 4,051 | 4,878 |
| stem groups | none | 1,000, covering 2,491 words |
| spelling forms mapped | none | 76 |
| synonym words | none | 52 |
| phrases | 4,059 | 4,059 |

**Stemming did not shrink the index, and the sentence that said it would was wrong twice
over.** Amendment 1 caught the first half: the suffix list could not have collapsed the
hallucination family at all. The second half only appeared when it was built. Collapsing
the postings works, and it takes the suite from 22 useful to 15, because `design`,
`designer`, `designs` and `designing` in one posting list stop distinguishing anything and
five queries come out as exact ties with the right answer second. So the raw words stay
separate and a second map groups them, consulted at half weight. That grows the index
instead of shrinking it.

The family does now reach itself. Measured from the built index, `hallucinate`,
`hallucinated`, `hallucinating`, `hallucination` and `hallucinations` are five separate
posting lists in one stem group, and a query for any of them scores the union once.

**The 400 KB budget was measuring the wrong thing.** The file is fetched lazily, on the
first keystroke, and served gzipped; raw bytes are not what a phone downloads or waits for.
Stated properly, the budget is **150 KB transferred**, and the index is at 146 KB against
103 KB before this round. The build prints both numbers on every run.

If that is ever exceeded, the first cut is the phrase map: 4,059 phrases for a +6 bonus, the
largest single section after the postings themselves, and the one whose value has never
been measured on its own.

---

## 5. How it will be judged

`scripts/test-search.py`, unchanged in shape: 57 queries, each with the role that typed it,
the verdict, and the fragment that must appear in the top three.

- **Before: 22 of 57 useful (39%).**
- **Target: 40 of 57 (70%), and no role below half.**
- **After: 24 of 57 (42%), and the target was not reached.** Six queries turned out to be
  content gaps rather than search faults, so 51 of the 57 are questions search could in
  principle answer, and 24 of those 51 land.

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

`data-analyst` is still 0 of 5, which is what the spec said had to move most and did not.
Every query that changed verdict was re-read by hand before the round closed, because a
query can pass for the wrong reason; thirteen were, and the judgement on each is written
into its suite row.

---

## 6. What this will not fix, plainly

**Amendment 4: these become a list, not a paragraph.** A query that fails because the
catalogue holds nothing is marked `content-gap` in the suite — a third verdict, distinct
from `ok` and `bad`, because "search cannot find it" and "we do not have it" are different
problems with different owners. `measure.py` writes them into STATUS.md under **Questions
the catalogue cannot answer**, with the role that asked. That list is the harvest target,
it is generated, and nobody types it.

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

**Amendment 5: section 6 ships.** One paragraph of it is kept verbatim on
`how-we-check.html`, under the method: search finds what we hold; which of three found
rows is best is what the picks answer; a question with no answer in the catalogue returns
nothing and says so. It goes through `docs/design/ux-copy.md` like every other string on
the site. A limit a reader can discover for themselves should be written down where they
are already reading about how the site works.

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
