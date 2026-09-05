# The use-case gallery: what the measurement showed, and the three rules that answered it

**Date:** 6 September 2026
**Status:** applied. FIX-25 and FIX-26 carried it out; this file is the record.
**Numbers:** every count in this file is measured. The current ones live in
[STATUS.md](../STATUS.md), which is rewritten on every build. Where a number here is
historical — what a thing was before a rule moved it — it is dated.

---

## 1. What the measurement showed

Attack 2 sent ten hostile role-agents at the live site. Eight of the ten reported the same
shape of fault from different directions, and D12 was the instruction to stop arguing and
measure it: how much of this catalogue is the Anthropic Academy use-case gallery, and what
is it doing to the filters?

The measurement, taken 5 September 2026:

- 148 of 635 rows were single-recipe pages from `academy.claude.com/use-cases`.
- They were 23% of the catalogue and a far larger share of some cells: `pm|builder` held
  58 candidates, 49 of them gallery recipes.
- Almost all of them were tagged `business-founder` or `pm`, and their own `who_for`
  lines named nobody of the kind — "Sales reps preparing for a renewal call", "In-house
  counsel or legal ops triaging a high volume of standard NDAs".

Two separate faults were tangled together in that, and they had to be untangled before
either could be fixed:

**The level was wrong.** A recipe that says "open Cowork, connect Salesforce, run this
prompt" was filed at `builder`, the level whose own words are *built things with it*.
Two thirds of `builder` was recipe-running.

**The role was wrong.** A row whose card names a sales rep was reachable from the product
manager filter. Attack 2's PM agent called this the finding that would make them leave:
a role filter that returns other people's work makes every other filter suspect.

The `notes` field had been saying so the whole time. It is the one field the site does not
render.

---

## 2. Rule A — the level means what the words say

`docs/design/ux-copy.md` now carries the definition beside the level vocabulary:

> **built things with it** means you wrote code against the API, authored a skill, an
> agent, a connector or an automation, or set up Claude Code. Running somebody else's
> recipe in Cowork with connectors attached is **used it a lot**.

`scripts/audit-levels.py` applies it. Two design decisions inside it are worth keeping:

**It moves only on positive evidence.** The first cut moved 119 rows because its default
was to move on the *absence* of evidence of building, and it swept up "Building effective
agents", "Effective context engineering for AI agents" and "Code execution with MCP" —
canonical builder material. Silence now leaves a row where it is.

**The gallery URL is evidence, not proof.** A page filed under the publisher's own
use-case gallery is presumptively a recipe, but a card that describes authoring a skill
file, an SDK, an MCP server or the API overrides that. "Encode the brand as a skill" is a
gallery page and stays `builder`, because the thing you end with is a skill.

77 rows changed level: 67 down out of `builder`, 10 up into it.

## 3. Rule B — a role tag has to be true of the card

`scripts/audit-role-tags.py`. A tag holds when the card's `who_for` names that role's
reader, or when it names nobody in particular. The second half is FIX-16's ruling and it
still stands: "Anyone who keeps re-pasting the same background into new chats" genuinely
serves every role, and punishing that pushes the catalogue back towards one persona per
card, which is the Puckett fault wearing the other face.

Three refinements came out of applying it:

**It adds where refusing to add would delete.** Eight marketing recipes said "Marketers",
"Content marketers", "Marketing teams" while tagged `business-founder, pm`. Every tag
failed. Without the addition they would have been swept into a collection card when the
fix was a tag they should always have carried.

**"Fits no role" means the card names none** — not that its current tags happen to be
wrong. That distinction is what kept those eight rows alive.

**It runs both directions** (FIX-26). Until then the check could only subtract, and the
cost was visible: Vanderbilt's page on AI-detector false accusations singles out
non-native English writers, carried `teacher` alone, and could not be reached from the
student filter. Attack 1 filed it; Attack 2 filed it again. The sweep now reads `skip_if`
as well as `who_for` when asking which roles a card names, and prints every named role the
row does not carry. Dropping still uses `who_for` alone — "skip this if you are a
developer" must not be allowed to keep a `developer` tag.

## 4. Rule C — a row that fits no role becomes part of a card that does

A row whose card names a job this site has no role for is not a row this site can file. It
becomes one card per job family, pointing at the gallery's own department page — a real
URL, opened and counted on the day — tagged to the role most likely to run that team, with
a `skip_if` saying plainly what it is.

Five collection cards exist: Sales, Legal, HR, Finance and Operations. A sixth was ruled
for the gallery's General tab and never built, because no roleless row turned out to be on
it. 40 individual rows were absorbed. Every absorbed row's
`skip_if` is kept in the card's `notes`, because those lines were the best writing on those
cards and the only part of them that was ours.

**The cost, recorded rather than smoothed over.** Five of the absorbed recipes were not
listed on their department page the day it was read, although all five still answer at
their own address. A reader can no longer reach those five from this site. Their addresses
are on the card. The alternative was keeping a role tag the card denies, which is the fault
the round exists to fix.

**And two rows were removed outright.** Both are fundraising craft written for a
development director — a gift pyramid, and the retention-versus-acquisition argument. This
site has no fundraising role, the gallery files them under no department, and they are not
on the General tab. There was nothing for them to join, and a card for nobody is noise.
Their cards are kept in `docs/attack/2/RULE-B-LOG.md`.

---

## 5. What it cost, and who decides that

The catalogue went from 635 rows to 598. The share that is Anthropic's own writing went
from 61.4% to 59.0%, and it fell for one reason: every row Rule C removed was Anthropic's.
Nothing independent was added or taken away.

This reverses a decision made knowingly in August, when 61% was recorded in the backlog as
a deliberate acceptance. That decision was made about a catalogue where those 148 rows were
believed to be doing work for the readers they were tagged for. The measurement showed they
were not. A composition figure that improves because rows nobody could use were removed is
not a win to celebrate; it is an accounting correction, and it belongs in the record as one.

**Live numbers: [STATUS.md](../STATUS.md).** Nothing in this file is a number to quote
tomorrow.

---

## 6. What the round left open

- **The rest of the catalogue has never been swept.** Rule B was applied to the use-case
  gallery only. Run over everything, the drop side reports 62 rows outside the gallery
  carrying a tag their card denies and 60 more that fit no role. That is a round of its own.
- **`student|builder` is still empty**, and `non-technical|builder` holds two items from
  one publisher, both Anthropic's. Rule A made that worse by moving recipe-running out of
  `builder`, which is the honest state rather than a new problem.
- **16 gallery rows have no family** in `data/use-case-departments.json` because the
  gallery's own filter does not list them. FIX-26 ruled all of them against their pages;
  the log is in `docs/attack/2/RULE-B-LOG.md`.
