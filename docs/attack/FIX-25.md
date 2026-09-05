# Fix prompt — Attack 2 rulings, part 2: the gallery, the tags, the levels

Paste everything below the line into Claude Code, in the project folder.

---

The prose was true and the tier was the lie — and `notes` had been saying so the whole
time in the one field nobody renders. Good round. Four small rulings on what you
handed back, then the one structural decision the measurement made unavoidable.

# Small rulings

1. **D2's first sentence.** "Checked" is the word Attack 2 caught as false; do not put it
   back on the first screen, and no subtraction there either. It ships as: *"635
   resources, each with a reason to skip it and the date we last looked."* Number
   generated. True for all 635, the three stripped ones included. The 632/3 split
   belongs on `how-we-check.html`, beside the tier tally.
2. **D11 reverts on cards, stays on the resource page.** One stop per card was a
   deliberate decision seven agents praised. The card link's `aria-describedby`
   carries the tier's one-line meaning, so a reader still hears it. The badge on
   `resource.html` stays a link.
3. **The five corrected clauses stand.** That was verification with the page quoted.
4. **Fix the validator's lie.** "3 picks could span 3 formats" was computed without the
   publisher cap. Compute the spread over sets the cap allows, and add
   `constraints-jointly-unsatisfiable` to the two-pick cause vocabulary if it is not
   there. Then **re-pick the 13 stale cells** — the promoted rows are eligible now and
   some may deserve a slot.
5. **A provenance note must agree with the tier.** `notes` saying "not reviewed",
   "not watched", "not read", "metadata only", "summaries only" on an `ai-reviewed`
   row is an error. Warning on `previewed`, printed. The field that told the truth
   gets to enforce it.

# The decision — D12 and D5 are one problem

The measurement says: 148 rows from one gallery, 43% of the `builder` level, 9 picked,
1 path step. The sample cards read *"Sales reps prepping for a call"*, *"Account
managers"*, *"Marketers"* — jobs that are not among the ten roles. And every one needs
Cowork plus connectors, which is using Claude a lot, not building with it.

So the two attack findings — the role filter returns other people's jobs, and the top
level is a monoculture — are the same 148 rows, filed at the wrong level under the
wrong tags. Ruling, in three rules, applied to every row in the catalogue, gallery
first:

**Rule A — the level means what the words say.** "Built things with it" is: wrote code
against the API, built a skill, agent, connector or automation, or set up Claude Code.
Running a recipe in Cowork with connectors attached is "used it a lot". Write this
definition into `ux-copy.md` beside the level vocabulary, then re-level every row whose
card says which it is. *"Encode the brand as a skill"* stays `builder`. *"Account
tracking"* moves to `confident`.

**Rule B — a role tag must be true of the card** (D5, as recorded). Extend the Puckett
check: a `who_for` naming a persona outside the tagged roles is a warning. Sweep the
list with the FIX-16 test — the card and the page decide, not the cell that wants the
row. A sales recipe loses `pm`. If it fits no role at all, it says so in the log and
goes to Rule C.

**Rule C — rows that fit no role become one card per job family.** A recipe for sales
reps has no reader on this site, but a founder with a sales team does. Collapse the
roleless gallery rows into collection entries — one per family the gallery itself
uses: sales, marketing, support, legal, HR, finance, operations, and whatever else it
has — each a real URL to the gallery's own family page, tagged to the role most likely
to run that team, with a `skip_if` that says what it is: *a menu of fifteen recipes,
not a lesson; open only if you run that function.* The individual rows are removed;
their `skip_if` lines are kept in `notes` on the collection card so the writing is
not lost. Same tier rules, same provenance.

**Checkpoint.** Do Rule A over the whole catalogue first and show me the counts per
level before and after. Then do Rules B and C for **one family — sales** — end to end,
and stop. Show me the collection card, the rows it absorbed, the rows that stayed
because they fit a role, and every cell count that moved. If it reads right at one
family, finish the rest without stopping. If it does not, I would rather stop at one.

*(Veto point: this changes the composition you decided knowingly in August. The
official ratio will fall, `builder` cells will shrink to what is actually building,
and picks in nine cells will re-run. If you want to keep the 148 as they are, delete
this section and Rule B still runs on its own.)*

# Two small ones, same round

**D10 — "How well checked" is a filter.** Four tiers, same machinery as the other five
axes. It is the differentiator; make it filterable.

**D4 — a thin level says so and offers the level below.** Fewer than five results with
role and level set: one line saying so, one click to include the level below, exact
match stays the default. Copy in the deck.

# Not this round

D3 search rebuild is its own round, spec first. D9 price and D13 the "we" follow it.

# Not yours

STATUS.md "Needs a person" and part 10. The human test.

# Commits

The five small rulings, Rule A, the sales family, the remaining families, D10, D4 —
one job each. `FIX-25.md` with the round. Finish with what surprised you, what you got
wrong, whether it was in CLAUDE.md — and the official ratio before and after.

---

# The round, as run

Every number below is measured from `data/items.json` at 2026-09-06 against the same file at
`45fafac`, the commit this round started from.

## The catalogue

| | before | after |
|---|---|---|
| resources | 635 | 600 |
| official Anthropic | 390 (61.4%) | 355 (59.2%) |
| use-case gallery rows | 148 | 108 |
| never used Claude | 106 | 106 |
| used it a little | 178 | 177 |
| used it a lot | 169 | 223 |
| built things with it | 182 | 94 |

**The official ratio went from 61.4% to 59.2%.** Every one of the 40 rows Rule C
removed was Anthropic's, so the share of the catalogue that is Anthropic's own writing
fell by removing Anthropic's own writing. Nothing independent was added or taken away
this round.

## What each rule moved

**Rule A — the level means what the words say.** 77 rows changed level: 67 down from
`builder` to `confident`, 10 up. The definition went into `docs/design/ux-copy.md` beside
the level vocabulary: *built things with it* means wrote code against the API, authored a
skill, agent or connector, or set up Claude Code. Running someone else's recipe in Cowork
with connectors is *used it a lot*. `builder` fell from 182 to 94, which is the size of the
mistake: two thirds of that level was recipe-running filed as building. The first cut of
the audit moved 119 rows including "Building effective agents" and "Code execution with
MCP", because its default was to move on the absence of evidence; it was rewritten to move
only on positive evidence, and silence now leaves a row alone.

**Rule B — a role tag has to be true of the card.** 40 rows had their tags changed. 26
lost a tag their own `who_for` denies while keeping one that holds. 14 had every tag fail
while the card plainly named a role they did not carry - eight marketing recipes saying
"Marketers" while tagged `business-founder, pm` - and those were given the tag they should
always have had. Refusing to add would have deleted them.

**Rule C — rows that fit no role become one card per job family.** 40 gallery rows
absorbed into 5 collection cards: sales, legal, HR, finance, operations. Each card points
at the gallery's own department page, opened and counted on the day. Every absorbed row's
`skip_if` is kept in `notes`.

Five of the 40 were not listed on their department page that day, although all five still
answer at their own address. A reader can no longer reach those five from this site. That
is a real cost and it is written on the card with the addresses. The alternative was
keeping a role tag the card denies, which is the fault the round exists to fix.

## The picks

30 cells went stale. In 28 the three that ship are still the three: nearly every arrival
is a single-task gallery recipe, and a recipe does not beat an orientation at "open this
first". The format rule did the work of refusing the swap in four cells on its own.

`student|confident` had a fault rather than a staleness - 'Verify statistics from raw
data' lost its `student` tag, so it could not ship. `teacher|confident` re-checked with
the corrected format rule and stays at two picks.

Eleven reasons counted a pool that had moved underneath them - "the only candidate of 78",
"thirty of thirty-three", "every safety candidate in this pool is Anthropic Academy's".
That last one was simply false. Each is re-measured or reworded.

## Still open

D3, the search rebuild, is its own round and wants a spec first. D9 and D13 follow it.
16 gallery rows have no family in `data/use-case-departments.json` and 9 roleless rows
sit in families this site does have a role for; both are named in the Rule B log and
neither was invented a card.
