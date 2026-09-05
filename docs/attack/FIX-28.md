# Fix prompt — the search diagnosis, the catalogue-wide tag sweep, and two small decisions

Paste everything below the line into Claude Code, in the project folder.

---

The stemming result is the round's real finding: on 598 rows, merging word forms made
search worse, and the suite caught it. Keep that. The number, though, is 24 of 57, half
of the movement came from re-grading, and the spec's diagnosis of `data-analyst` was
wrong — three causes fixed, zero of five moved. So search gets a diagnosis this round,
not a sixth mechanism.

# Search — rulings, then a table

1. **The suite measures the top three.** That is what the reader sees and what the
   agents scored. But re-measure "before" at the pre-rebuild commit under the same
   rule, so the comparison is honest. Report both pairs: first-result before/after,
   top-three before/after.
2. **A re-graded expectation keeps the original.** The five rows "re-recorded on merit"
   go back to the agent's fragment as one accepted answer, with the new one as an
   alternate — `accept: [a, b]`, each with a one-line reason citing the card. A query
   passes if any accepted answer is in the top three. The attack's judgment is not
   overwritten by ours.
3. **The phrase map is measured by removal.** Build without the 4,059 phrases, run the
   suite, measure the size. Unchanged suite → drop it, and the commit says what it
   saved. Moved → keep, and the commit names the queries that need it.
4. **The gate is per commit.** A step that breaks an `ok` query is not committed until
   it does not. Write that into the spec's section 7.

Then **the failure table**, one row per query still not passing under top three:
the query and its role; the row in the catalogue that should answer it, found by hand,
or "none"; that row's rank today; the words the query used that the row's indexed
fields lack; and the cause — *vocabulary* (a synonym or spelling would fix it),
*ranking* (the row is found but sits low), *content gap* (the catalogue holds nothing),
or *not a search question* (the catalogue cannot answer it and should say so).
`data-analyst`'s five come first. No fixes this round — the table decides the next one.
If one cause dominates, say so in one sentence at the top.

# Rule B over the whole catalogue

Rule B has only ever run on the gallery. Outside it: 62 rows carry a tag their card
denies, 60 fit no role. Same rules, page decides:

- **A tag the card denies** is trimmed, unless the page supports it and the card is
  what is wrong — then the card is rewritten to what the page says. Log each.
- **"Fits no role"** splits two ways. Role-neutral — *"anyone who…"* — is left alone,
  as FIX-16 ruled. A card written for a job off the roster: tag it if the page serves
  one of the ten, otherwise remove it — except a row that is a pick or a path step,
  which is flagged to me with the evidence and left in place.
- **Checkpoint at 30**, with the counts: trimmed, rewritten, tagged, removed, flagged.
  If removals are under a fifth, finish without stopping. If not, stop and show me
  what is being removed.

Pools will move. Let the stale machinery fire — the sentence re-read is a step now —
and re-pick what it names.

# D13 — the site names its "we"

One paragraph on `how-we-check.html`, through the copy deck: this site is made by one
person, a researcher at DTU, not affiliated with Anthropic; Claude did the reading at
the tiers the labels say, wrote the cards and chose the picks; a person has read
nothing in full yet, and the label on every card says which. *(Veto point: the
sentence works with or without my name. Default is without; tell me if you want it.)*

# D9 — price is a field

Optional, on the paid items only: amount, currency, `price_checked` date. Open every
paid item's page and record what it prints today; nothing printed → no field. Shown on
the card as "from $995" only when present, beside the cost chip. The typed-number check
already reaches items; a price without a date is an error.

# Not yours

STATUS.md "Needs a person" and part 10. The human test. The content-gap list.

# Commits

The four search rulings and the table, Rule B, the re-picks, D13, D9 — one job each.
`FIX-28.md` with the round. Push. Finish with what surprised you, what you got wrong,
whether it was in CLAUDE.md — and which cause dominates the failure table.

---

# The round, as run

## Search, graded honestly

Ruling 1 said re-measure "before" under the same rule. Doing that properly means the same
accepted answers on both sides, or the round takes credit for its own grading:

| grading | before | after |
|---|---|---|
| first result, each side's own recorded answers | 22 of 57 | 26 of 57 |
| top three, each side's own recorded answers | 22 of 57 | 35 of 57 |
| **top three, same accepted answers both sides** | **32 of 57** | **35 of 57** |

**The last line is the round's honest number: the rebuild moved three queries.** The rest of
the +13 is the grading rule and the eleven promotions, both of which were changes to how we
count, not to what a reader gets.

| role | before | after | content gaps |
|---|---|---|---|
| business-founder | 4 of 6 | 4 of 6 | 0 |
| data-analyst | 2 of 5 | 2 of 5 | 1 |
| designer | 4 of 7 | 5 of 7 | 2 |
| developer | 3 of 7 | 3 of 7 | 2 |
| non-technical | 4 of 5 | 4 of 5 | 0 |
| pm | 3 of 7 | 3 of 7 | 4 |
| researcher | 4 of 5 | 4 of 5 | 0 |
| student | 3 of 5 | 4 of 5 | 0 |
| teacher | 2 of 6 | 3 of 6 | 0 |
| writer-marketer | 3 of 4 | 3 of 4 | 1 |
| **total** | **32 of 57** | **35 of 57** | **10** |

## The failure table

23 queries do not pass. **One cause dominates and it is not a ranking problem.**

| cause | queries |
|---|---|
| content gap - the catalogue holds nothing | 10 |
| vocabulary - the row exists and its fields do not use the reader's words | 9 |
| ranking - the row is found and sits below third | 4 |
| not a search question | 0 |

Three findings from writing it. One row - "Write in my voice" - is the answer to three
failures in three different roles, and contains neither "email" nor "customer". "Using AI
for Writing Feedback" answers both teacher failures and contains none of marking, grading
or essays, so FIX-27's grading/marking synonym row could never reach it. And the four
ranking failures sit at 5, 5, 5 and 21 - near misses, except the 21, which is Vanderbilt's
AI-detector page for a student asking whether their university will know.

## Rule B outside the gallery

The third bucket was two buckets. Of 60 rows that "fit no role", **41 name a situation**
rather than a job - "Complete beginners who have never opened Claude" - and FIX-16 already
settled those. **19 name a job off the roster.**

Batch 1, 34 rows: 11 trimmed, 4 rewritten because the page supported the tag and the card
was wrong, 7 rewritten and retagged. **The checkpoint fired**: 12 removals in 34 rows is
over a third, so nothing was removed and the twelve are listed in the Rule B log for a
decision. None is a pick or a path step.

Ten pools moved and were re-picked. No pick changed hands: eight cells only lost
candidates, and the two arrivals were checked against the claims they could have broken.

## D13 and D9

The site says who "we" is: one person at DTU, not affiliated with Anthropic, Claude doing
the reading at the tiers the labels claim, and nobody having read anything end to end. No
name, which was the default.

Price is a field on 4 of the 26 paid rows - the four whose pages print a number that is
the same for every reader. Udemy showed EUR 11.99 on a countdown against a EUR 25.99 list
price because it prices by country and by sale, and a number true for the machine that
fetched it is worse than none. The validator refuses a price without the day it was read.

## Still open

- The 12 proposed removals, and the rest of the Rule B sweep behind them.
- `data-analyst` is 2 of 5 on both sides of the rebuild. Three of its five failures are
  vocabulary and ranking; one is a content gap.
- The vocabulary cause has no mechanism yet. The synonym table exists and the rows it
  needs - feedback, email, customer - are not in it.
