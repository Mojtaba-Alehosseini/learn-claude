# The search failure table

**Date:** 6 September 2026, after FIX-27's rebuild and FIX-28's re-grading.
**Rule:** a query passes when an accepted answer is in the top three. 34 of 57 pass.
**This table is the 23 that do not.** No fixes this round; the table decides the next one.

**One cause dominates, and it is not the one the spec assumed.** Ten of the twenty-three
are things this catalogue does not hold, and of the thirteen that search could fix, nine
are vocabulary: the row that answers the question exists, and its indexed fields do not
use the words the reader typed. Four are ranking. The spec's five mechanisms were built
for stemming, spelling and synonyms - and what is left is mostly a synonym table that
needs rows nobody has written yet, plus cards whose own words do not match their readers'.

| role | query | the row that should answer it | its rank | words its indexed fields lack | cause |
|---|---|---|---|---|---|
| data-analyst | can claude read my csv | How to Use Claude for CSV Data Analysis (The Honest Guide) | 5 | none | ranking |
| data-analyst | sql | Postgres MCP Pro (crystaldba/postgres-mcp) | 5 | none | ranking |
| data-analyst | pivot table | none | — | — | content gap |
| data-analyst | claude excel formulas | *passes* — Use Claude for Excel at 3 | 3 | none | — |
| data-analyst | stop claude making up numbers | *passes* — Reduce hallucinations at 2 | 2 | none | — |
| non-technical | write emails for me | Write in my voice | not returned | emails | vocabulary |
| student | will my university know i used ai | Guidance on AI detection, and why we're disabling Turnitin's AI detector | 21 | know, used | ranking |
| researcher | does claude make up citations | Reduce hallucinations | 29 | citations | vocabulary |
| teacher | make a lesson plan | Create custom course materials | not returned | make, lesson, plan | vocabulary |
| teacher | marking essays | Using AI for Writing Feedback | not returned | marking, essays | vocabulary |
| teacher | grading | Using AI for Writing Feedback | not returned | grading | vocabulary |
| developer | claude code hooks | none — the reference is here, the guide it points at is not | — | — | content gap |
| developer | how do i stop claude touching my tests | Hooks reference (Claude Code) | not returned | stop, touching, tests | vocabulary |
| developer | reduce token usage | How context affects Claude's performance and cost | not returned | reduce | vocabulary |
| developer | claude code permissions | none | — | — | content gap |
| pm | stakeholder update | none | — | — | content gap |
| pm | roadmap prioritisation | none | — | — | content gap |
| pm | prioritisation | none | — | — | content gap |
| pm | prioritization | none | — | — | content gap |
| designer | typography | none | — | — | content gap |
| designer | will ai design replace me | none | — | — | content gap |
| business-founder | write customer emails | Write in my voice | not returned | customer, emails | vocabulary |
| business-founder | keep my own voice | Write in my voice | 5 | keep | ranking |
| writer-marketer | em dash | none | — | — | content gap |

## The counts

| cause | queries | what would fix them |
|---|---|---|
| content gap | 10 | Harvesting. Not a search job, and the list is generated into STATUS.md. |
| vocabulary | 9 | Synonym rows, or cards rewritten in the reader's words. |
| ranking | 4 | The scoring itself: three of the four have the right row inside the results and below third. |
| not a search question | 0 | — |

## Three things the table shows that the numbers did not

**One row answers three failures.** "Write in my voice" is the answer to "write emails for
me", "write customer emails" and "keep my own voice", and its indexed fields contain
neither "email" nor "customer". One card rewritten in its reader's words closes three
queries in three different roles.

**"Using AI for Writing Feedback" answers both teacher failures** and contains none of
marking, grading or essays. The FIX-27 synonym table has a grading/marking row and it
cannot reach this card, because the card's word is "feedback" and that is in no row.

**The ranking failures are near misses, not disasters.** Ranks 5, 5, 5 and 21. Three of
the four are two places out of sight. The one at 21 is Vanderbilt's AI-detector page for a
student asking whether their university will know - the highest-stakes query in the suite,
and the row was made reachable at all only in FIX-26.

---

## After FIX-29

Three of the table's rows are closed and one is reclassified.

| query | was | now |
|---|---|---|
| writer-marketer, em dash | content gap | **passing** - and it was never a gap. Wikipedia's Signs of AI writing, already in the catalogue, has a section headed "Overuse of em dashes". The card never used the words. |
| developer, claude code permissions | content gap | **passing** - the settings page was harvested from the Claude Code docs. |
| teacher, marking essays | vocabulary | **passing** - the grading synonym row gained `feedback`, and synonyms were allowed to admit. |
| developer, claude code hooks | content gap | **ranking** - the guide was harvested and comes sixth for its own question while the reference stays first. |

### What is left

| role | query | first result today |
|---|---|---|
| non-technical | write emails for me | Claude AI for Teachers: Complete Beginner's Guide to Getti |
| student | will my university know i used ai | Generative AI and Academic Integrity |
| researcher | does claude make up citations | 3 Mind Blowing Claude & Consensus Research Workflows | No  |
| teacher | make a lesson plan | Claude for K-12 teachers - product page with worked prompt |
| teacher | grading | Teaching AI Fluency (Anthropic Academy) |
| developer | claude code hooks | Hooks reference (Claude Code) |
| developer | how do i stop claude touching my tests | Red Green Refactor is OP With Claude Code |
| developer | reduce token usage | A Guide to Claude Code 2.0 and getting better at using cod |
| data-analyst | can claude read my csv | Upload files to Claude (Help Center) |
| data-analyst | sql | Answer the ad-hoc data question |
| business-founder | write customer emails | Claude AI for Teachers: Complete Beginner's Guide to Getti |
| business-founder | keep my own voice | Using AI for Writing Feedback |

### Still content gaps

| role | query |
|---|---|
| data-analyst | pivot table |
| pm | roadmap prioritisation |
| pm | stakeholder update |
| pm | prioritisation |
| pm | prioritization |
| designer | will ai design replace me |
| designer | typography |

Walked in FIX-29 and empty: the Help Centre's Claude-in-Excel articles hold no pivot tables; the Academy's use-case gallery, Product department, holds neither roadmap nor stakeholder. Typography and "will ai design replace me" were not walked this round.

The vocabulary failures that remain are the ones the questions rewrite is for, and that rewrite is waiting at its checkpoint.


---

# The final table — FIX-31

The search work started in FIX-27 with a spec and ends here. Seven queries of the
fifty-seven still return the wrong thing at the top; every one has been traced rather than
guessed at, and every trace is reproducible with `tmp/trace2.py`.

Three that were in this table are gone, each promoted on the previous entry's own terms
rather than on a new judgement: **write emails for me** (its reason said the row that
answers it "is still not in the results" - it leads them now), **will my university know i
used ai** (the objection was that the answer was a card nobody had opened; D1 re-tiered it
and it is `previewed`), and **can claude read my csv** (the recorded accepted answer is
first). The content gaps are gone too, and not because they were solved: every one of them
was a claim made from a card, and the pages said otherwise - `GAP-RECHECK.md`.

| role | query | what leads | where the answer sits | cause |
|---|---|---|---|---|
| developer | claude code hooks | Hooks reference (Claude Code) | *Automate actions with hooks* 6th of 49 | the phrase bonus. Both match `hooks` identically; the entire gap is a flat +6 for holding a string that is a **substring of the query**, plus which field holds "claude" and "code". Spec amendment 6. |
| developer | reduce token usage | A Better (and Cheaper) Figma MCP | *Maximizing the value of your Claude Code sessions* 8th of 10 | vocabulary. The page that explains what a turn costs says "cost", "budget" and "cache"; the reader says "reduce token usage". Its own page's words are not the reader's here, and the round did not invent a bridge. |
| teacher | grading | Teaching AI Fluency | *Using AI for Writing Feedback* reaches the query **only** through the synonym row | the expansion ceiling. The leader holds the literal word `grading` in keywords: 15.8. The answer holds no form of it and arrives on the synonym alone, at half weight: 6.2. Nothing in the current design can close nineteen points with an expansion. Spec amendment 7. |
| researcher | does claude make up citations | 3 Mind Blowing Claude & Consensus Research Workflows | *Reduce hallucinations* 29th of 43 | the same ceiling. The citation synonym lifted it into the results and cannot lift it to the top, because the leader holds the reader's own words in its questions. |
| business-founder | keep my own voice | Understanding Claude's Personalization Features | *Write in my voice* 13th of 70 | one common verb. Both rows hold `voice` in a question at weight 5 - 17.2 each, identical. The whole difference is `keep`, which the personalisation page happens to hold in a question and the row named *Write in my voice* does not. This is the ranking working: two matched words beat one. |
| business-founder | write customer emails | Anthropic Just Dropped Claude for Small Businesses | *Write in my voice* 2nd of 27 | probably not a ranking fault at all. Nothing here is a page **about** writing to a customer; the leader lists customer email among a dozen prebuilt skills and the runner-up is about voice. **Gap candidate** - and under the FIX-30 rule a gap is a claim, so it needs its pages opened before it can be recorded as one. |
| teacher | make a lesson plan | How Teachers Can Create Interactive Classroom Activities | *Agent Skills for K-12 Teachers* 2nd of 70, shipping a `k12-lesson-planning` skill | also a gap candidate. The closest rows are a skills repository and an argument **against** the lesson-plan-in-one-prompt habit. Neither is a page that helps a teacher write one. Same rule: open the pages first. |

## What the table says as a whole

Two of the seven are one general fault, already written up as **spec amendment 6**: the
phrase bonus pays a row for holding a string shorter than what the reader typed, and pays
nothing for a longer, more exact one.

Two more are a second general fault, which becomes **spec amendment 7**: an expansion -
stem or synonym - scores at half weight and never admits, so a row that reaches a query
only through one can never beat a row holding the literal word. That rule is right for a
synonym, which is somebody else's word. It is doubtful for an inflection: `remember` and
`remembers`, `formula` and `formulas` are the same word, and FIX-31 had to repair two rows
by hand for exactly that reason. The amendment asks whether an inflection should be
treated as the word itself.

Two are gap candidates that cannot be recorded as gaps until their pages are opened, which
is the rule FIX-30 wrote after every previous gap turned out to be false.

**One is not a fault.** *keep my own voice* loses on a matched verb, which is the ranking
doing its job. Fixing it would mean writing the query's words into a card, and the guard
that refuses that exists for a reason.
