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

### The final size, FIX-31

|  | at this spec's close | now |
|---|---|---|
| `data/search-keywords.json`, raw | 507 KB | 567 KB |
| the same file gzipped, which is what a phone downloads | 146 KB | **166 KB** |
| indexed words | 4,878 | 4,971 |
| stem groups | 1,000 covering 2,491 words | 1,017 covering 2,564 words |
| spelling forms mapped | 76 | 81 |
| synonym words | 52 | 92 |
| phrases | 4,059 | 5,201 |

The index grew past the 150 KB figure this section set. Almost none of the growth is
machinery: stem groups, spelling forms and synonyms together added a few dozen entries.
The phrases grew by more than a thousand, and every one of those is a `questions[]`
string, because the phrase map keeps each question whole. Those questions were rewritten
and then lengthened over two rounds; the index grew with the catalogue's own prose.

### Amendment 8: the budget is a time, and the size is only what produced it

**A number nobody has measured is not a budget.** 150 KB was typed into this spec, never
tested against a reader, and the round that exceeded it nearly cut content to satisfy it.
What a reader feels is not bytes; it is how long they wait after typing. So the budget is
restated as that wait, measured in the browser on the live site.

**Measured on `browse.html`, live, 6 September 2026.**

| | |
|---|---|
| bytes the server actually sends for the index | **176,934** (`encodedBodySize`, compressed) |
| the same file uncompressed | 580,840 |
| typing pause before anything runs | 150 ms, from `TYPING_PAUSE` in `browse.js` |
| parsing the index | **26 ms** cold, 4 ms on a repeat |
| keystroke to results, index already loaded | **159, 164, 164, 166, 159 ms** over five queries |
| so ranking and redrawing 588 rows | **9-16 ms** |

The steady-state cost of a keystroke is the typing pause plus about twelve milliseconds.
Every keystroke after the first is effectively instant, and no plausible index size
changes that, because the index is already in memory.

**The first keystroke is the only one that pays for the file**, and only once per visit.
Modelled at 1.6 Mbit/s with a 150 ms round trip - a slow 4G phone - over the bytes
measured above:

    150 ms typing pause + 1,035 ms network + 26 ms parse + ~14 ms rank and draw
    = about 1.2 seconds to a ranked answer, once, on the first search of a session.

**The budget is: under 1.5 seconds to a ranked answer on a slow 4G phone, on the first
search of a session, and under 200 ms on every keystroke after it.** Both are met at
176,934 bytes. That size is recorded as what produced the time, not as a limit of its own.

Nothing is cut. **If the time were bad, what would be cut is the phrase map** - it is
in September 2026 it was 5,201 entries holding every `questions[]` string whole, the largest single part of
the file, and amendment 6 already argues on ranking grounds that two of its three
candidate repairs would shrink or remove it. That is the lever, and it is named here so
that nobody reaches for the catalogue's content instead.

### What the measurement found that the size never would have

Until the index lands, `browse.js` falls back to plain substring matching over title,
summary, `who_for` and source, so that typing is never dead. On a fast connection nobody
sees it. On the modelled slow phone it is what the reader looks at for about a second, and
**it is usually not the answer.**

Measured over twelve queries taken from the suite, comparing the fallback's first result
with the ranked first result:

| | |
|---|---|
| queries where the fallback shows **nothing at all** | **5 of 12** |
| queries where the fallback's top result **differs** from the ranked one | **8 of 12** |

"grading", "write emails for me", "make a lesson plan", "how much does claude cost" and
"can claude read my csv" all render **`0 resources`** for that second before the real
answer replaces it. A reader on a train who types a question and reads `0 resources` has
been told the site does not have it, and some of them will stop there.

That is a bigger cost than the file size and it was invisible while the budget was a
number. It is a finding, not a fix: the repair might be a spinner, a held render, or
shipping a tiny always-loaded first-pass index, and choosing between those needs the
attack's evidence about what readers actually do. Recorded here; not built.

**The phrase map was measured by removal, and it stays.** It is the largest section after
the postings - in September 2026, 4,059 entries at 123 KB raw and 35 KB gzipped, a quarter of the transferred
file - and building without it takes the suite from 24 to 23. One query needs it:
`is claude free`, from the non-technical reader, where the phrase "is claude free" is
matched whole against the plan page's own question list. No query is hurt by it.

So the ratio is stark and it is written down rather than argued: 35 KB over the wire for
one query in fifty-seven. It stays because the ruling was measure-then-decide and the
measurement moved. If the budget is ever exceeded this is still the first thing to weigh,
and the next round now has the number instead of an opinion.

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

### The final numbers, FIX-31

Three rounds later, and on a stricter definition than the table above used: `tmp/measure.py`
grades **top three, today's accepted answers, both columns** - the round-start commit's own
ranker and index on one side and today's on the other, so the only thing that differs is
the work being measured.

| role | FIX-29 close | FIX-31 close |
|---|---|---|
| business-founder | 4 of 6 | 5 of 6 |
| data-analyst | 3 of 5 | 5 of 5 |
| designer | 5 of 7 | 7 of 7 |
| developer | 5 of 7 | 5 of 7 |
| non-technical | 5 of 5 | 5 of 5 |
| pm | 6 of 7 | 7 of 7 |
| researcher | 4 of 5 | 4 of 5 |
| student | 5 of 5 | 5 of 5 |
| teacher | 4 of 6 | 4 of 6 |
| writer-marketer | 4 of 4 | 4 of 4 |
| **total** | **45 of 57** | **50 of 57** |

**The target set in this section - 40 of 57 and no role below half - is met, and so is the
second half of it:** the lowest role is `teacher` at 4 of 6, and `data-analyst`, the role
this spec said had to move most, is 5 of 5.

Two cautions belong beside that number and not underneath it.

**It is not the same measurement as the 22 and the 24 above.** Those were counted when six
rows were graded `content-gap` and excluded; every one of those gaps was re-checked in
FIX-30 against the pages and every one was false, so all of them are graded now. A number
that grades more rows is not comparable to one that graded fewer, which is why the columns
name their commits.

**Part of the earlier numbers was contamination.** FIX-29 found that the `questions` field
had been written by somebody who had read the suite; FIX-30 rewrote it blind and the number
fell before it rose. Some of what looks like improvement here is that debt being repaid.

### The failure table stays

Seven queries still return the wrong thing at the top, each traced to a cause:
`docs/attack/2/SEARCH-FAILURES.md`. Two are spec amendment 6, two are spec amendment 7,
two are gap candidates awaiting the page-opening the gap rule now demands, and one is the
ranking working correctly on a query where two matched words beat one.

---

## 6. What this will not fix, plainly

**Amendment 4: these become a list, not a paragraph.** A query that fails because the
catalogue holds nothing is marked `content-gap` in the suite — a third verdict, distinct
from `ok` and `bad`, because "search cannot find it" and "we do not have it" are different
problems with different owners. `measure.py` writes them into STATUS.md under **Questions
the catalogue cannot answer**, with the role that asked. That list is the harvest target,
it is generated, and nobody types it.

- **`em dash` returns nothing because the catalogue holds nothing.** No row mentions it in
  any indexed field. A synonym cannot conjure a resource. Several rows discuss AI writing
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

**The gate is per commit.** A step that breaks a query that used to pass is not committed
until it does not. FIX-27 committed step 1 with four `ok` queries broken, disclosed it, and
repaired them four commits later - which meant the gate was down for five commits and the
repair arrived tangled with three other changes. A gate checked at the end of a round is
not a gate; it is a hope. If a step cannot hold the line on its own, it is not finished,
and the honest move is to keep working on it rather than to write the breakage into the
message.

---

## 8. Amendment 6, proposed by FIX-30 and not built this round

**The phrase bonus pays the vaguer keyword.** `build-search-index.py` keeps every
multi-word `keywords` and `questions` string whole, and `rank()` adds a flat +6 when
`phrase in q` — when the row's stored string is a **substring of the query**. So a row is
paid for writing *less* than the reader typed and paid nothing for writing *more*.

FIX-30 was asked to find out why the hooks guide harvested last round is sixth for "claude
code hooks". The arithmetic, from `tmp/trace2.py`:

| | Hooks reference (Claude Code) | Automate actions with hooks (Claude Code) |
|---|---|---|
| `hooks` exact | questions, w5 × 3.74 = **18.7** | questions, w5 × 3.74 = **18.7** |
| `hooks` stem | +9.0 | +9.0 |
| `code` exact | questions, w5 × 1.10 = **5.5** | keywords, w3 × 1.10 = **3.3** |
| `code` stem | +2.6 | +1.6 |
| `claude` exact + stem | +0.5 | +0.3 |
| phrase bonus | `claude code hooks` fires: **+6.0** | nothing fires: **0** |
| **total** | **42.4** | **32.9** |

Both rows match `hooks` identically. The whole 9.5-point gap is made of things that
have nothing to do with the subject: 6.0 of it is the phrase bonus, and 3.4 is the
difference between holding "claude" and "code" in `questions` rather than in `keywords`.

The reference page earns the bonus because its keyword is the string `claude code hooks`,
which is what the reader typed. The guide earns nothing - and it is not because its
keywords are worse. Its keyword is `claude code hooks guide`: the query plus one word, the
same subject said slightly more precisely. Being longer than the query is the whole of its
disqualification. The other rows on this query that hold a phrase containing it -
`claude code hooks and skills`, `claude code hooks in twenty minutes`, `claude code hooks
reference` - and every one of those strings earns nothing.

**It is general, not one row's wording, and it is two faults rather than one.**
`tmp/phrasescan.py` walks the suite; seven of the fifty-seven queries have this shape.

*Fault A - a phrase longer than the query is worth nothing.*

- **"claude code hooks"** — above. The guide's `claude code hooks guide` pays zero.
- **"peer review"** — *Nature Portfolio's AI editorial policy* holds `peer review ai
  policy` and fires no phrase at all. *Peer and AI Review of Student Writing* holds the
  bare `peer review`, is paid +6, and wins. This is a recorded suite failure whose
  accepted answer is the Nature page.
- **"design system"** — *Design system drift review* holds `design system drift review`
  and `design system drift claude`, fires neither, and is paid nothing. The rows holding
  the bare `design system` are paid +6.

*Fault B - the bonus is flat and additive, so short keywords stack.*

- **"claude code permissions"** — *Claude Code Essentials (ExamPro full course)* holds
  both `claude code` and `claude code permissions`, so it fires twice and collects **+12**.
  *Claude Code settings and permission rules*, which is the page about the subject, holds
  `claude code permissions` and collects +6. Twelve against six, and the course takes
  first place. The course is not wrong for the query; it is winning on arithmetic that
  rewards holding a vague keyword *as well as* a precise one.



**What the amendment should be, argued rather than assumed.** The obvious repair —
also pay a phrase that *contains* the query — is not obviously right, because "claude code
hooks in twenty minutes" containing "claude code hooks" is a good sign while "build it from
our actual design system" containing "design system" is noise. Three candidates, for the
next round to measure rather than for this one to pick:

1. **Symmetric containment, scaled by overlap, and paid once.** Pay
   `6 × (words in common ÷ words in the longer string)`, taking each row's best phrase
   only. "claude code hooks guide" against "claude code hooks" pays 4.5; "claude code"
   against the same query pays 4.0; "build it from our actual design system" against
   "design system" pays 1.7. Fault A and fault B both close, and nothing needs a new list.
2. **Pay the longest matching phrase only, per row.** The smallest change that closes
   fault B on its own, and it also fixes the em-dash shape where one row holds both
   "em dash" and "em dashes" and is paid for both.
3. **Drop the flat +6 and let the field weights decide.** The bonus was added before
   `skip_if` was indexed and before the stem expansion; it may be paying for a problem two
   later mechanisms already solved. Removal is measurable in one line.

**The gate is the same as every other step here: no `ok` query becomes `bad`, and the
number is recorded per commit.** Whichever candidate is built, the suite is the judge, and
if none of the three improves the number then the finding is written down and the bonus
stays as it is. FIX-30 deliberately changed nothing here: tuning a weight to move one
query is how a search stops being measurable.
