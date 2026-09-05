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
