# Every content gap, re-checked against the pages

FIX-30: *"A content gap is a claim. Re-check every remaining gap: list the three closest
rows by search and by hand, open their pages, and either find the answer we already own
or record why each one does not answer it."*

Seven queries in the suite carried the verdict `content-gap`. Every one of them was
written from cards. Every one of them is wrong.

The cards were not lies. They were summaries, and a summary drops the thing you did not
know you would need. *Package your brand guidelines in a skill* has a labelled
**Typography** field on the page; our card said "colors, fonts, spacing" in a summary that
the index does not read. The official PM plugin ships a command called
`/stakeholder-update`; our card said the page "teaches installing a plugin and running
slash commands", which is true and misses the point entirely.

## The seven

| query | verdict was | verdict now | the page that settles it |
|---|---|---|---|
| pivot table | content-gap | ok | [Claude in Excel for HR: Headcount planning](https://academy.claude.com/tutorials/how-to-use-claude-in-excel-for-hr-headcount-planning) |
| roadmap prioritisation | content-gap | ok | [Lenny's Product Skills](https://github.com/refoundai/lenny-skills) |
| stakeholder update | content-gap | ok | [Product Management Plugin](https://claude.com/plugins/product-management) |
| prioritisation | content-gap | ok | [Lenny's Product Skills](https://github.com/refoundai/lenny-skills) |
| prioritization | content-gap | ok | [Lenny's Product Skills](https://github.com/refoundai/lenny-skills) |
| will ai design replace me | content-gap | ok | [Good from Afar, But Far from Good](https://www.nngroup.com/articles/ai-prototyping/) |
| typography | content-gap | ok | [Package your brand guidelines in a skill](https://academy.claude.com/use-cases/package-your-brand-guidelines-in-a-skill) |

### pivot table — data-analyst

**Recorded reason:** "Three rows mention pivot tables in passing and none is about them
… there is nothing here."

**Closest by search:** *Claude Code for Data Analysis: Excel-Free Answers From CSVs*,
*Compare products across sites*, *Choosing between Claude Cowork or Chat*.
**Closest by hand** (every row whose indexed text carries pivot / spreadsheet / excel):
*Use Claude for Excel*, *Claude in Excel for HR: Headcount planning*, *Master Claude for
Excel in 10 Minutes*, and about forty more.

**Pages opened.**

- [Claude in Excel for HR: Headcount planning](https://academy.claude.com/tutorials/how-to-use-claude-in-excel-for-hr-headcount-planning)
  — its own worked prompt is "Create a pivot table showing headcount by department and
  level, then add a stacked bar chart to visualize it." Not in passing. It is a step.
- [Claude Code for Data Analysis](https://ccforeveryone.com/guides/claude-code-for-data-analysts)
  — "From accounts_merged.csv, keep only customers who signed up in 2026, then build a
  pivot of total revenue by month and region", set against the Excel way: "Rebuild the
  PivotTable by hand each month."

**Verdict:** two answers. The HR card already *taught* pivot tables and no question said
the words, so it sat seventh of seven. Fixed from the page; it now leads.

### roadmap prioritisation, prioritisation, prioritization — pm

**Recorded reason:** "one PM skill pack whose card Attack 2 read and found is not about
prioritisation. Nothing here is about prioritising a roadmap."

**Closest by search:** *Feedback synthesis to prioritized themes*, *Lenny's Product
Skills*, *knowledge-work-plugins: product-management*.
**Closest by hand** (every row carrying prioriti- or roadmap): those three plus *Claude
Code for Product Managers*, *PM Operating System*, *Product Management Plugin*, *Plan your
literature review*, *Quickly prep for your week*, *Work through grant options in chat*.

**Pages opened.**

- [Lenny's Product Skills](https://github.com/refoundai/lenny-skills) — ships a skill
  named **Roadmap Prioritization**: "Transform a chaotic backlog into a high-ROI strategic
  plan based on evidence and appetite." Also **Evaluating Trade-Offs** and **Goal Setting
  and OKRs**. This is the "skill pack … not about prioritisation".
- [Product Management Plugin](https://claude.com/plugins/product-management) — one of six
  commands is `/roadmap-update`, which "Plans and reprioritizes roadmaps", supporting
  Now/Next/Later, quarterly themes and OKR-aligned formats.
- [knowledge-work-plugins: product-management](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management)
  — the readable source of the same plugin. Same commands.

**Verdict:** three answers for a subject we recorded as absent. All three spellings of the
query already returned Lenny's in the top three; the shelf was full and the note said
empty.

### stakeholder update — pm

**Recorded reason:** "the closest, the official PM plugin, teaches installing a plugin and
running slash commands … a plugin page, not an answer."

**Closest by search:** *Product Management Plugin*, *Product-Manager-Skills (Dean
Peters)*, *knowledge-work-plugins: product-management*.
**Closest by hand:** those three plus *Generate project status reports* and *Create a
company newsletter*.

**Page opened.** [Product Management Plugin](https://claude.com/plugins/product-management)
— `/stakeholder-update`, "Generates tailored stakeholder updates", "for executives,
engineering, or customers."

**Verdict:** the row we called not-an-answer is the answer, and it was already first. The
card described the *installation*; the page describes the *command*.

### will ai design replace me — designer

**Recorded reason:** "zero rows contain 'replace me' or 'replace design' in any field …
not one of them is on the subject."

That reason is a string search, not a check. A page can answer a question without
containing its words — which is the whole argument behind the questions field.

**Closest by search:** *avoid-ai-writing*, *Good from Afar, But Far from Good*, *Teaching
AI Fluency*.
**Closest by hand:** *Good from Afar, But Far from Good*, *AI Can't Replace Real Research
in Empathy Mapping*, *Claude for Designers in 2026: Where AI Actually Helps*.

**Page opened.** [Good from Afar, But Far from Good](https://www.nngroup.com/articles/ai-prototyping/)
— NN/g tested AI-generated designs against a human designer's work on a real project and
ends where the query starts: "The real work of design remains in the judgment, empathy,
and intent that only human designers can provide", and "This is what sets human designers
apart from AI tools: the ability to balance nuance, create sophisticated solutions, and
back every decision with a clear rationale."

**Verdict:** answered, and honestly the weakest of the seven. No page in this catalogue is
*about* designers being displaced. This one answers the question with evidence, which is
what somebody typing it at eleven at night wants, and it is second. If a page that is
about the subject turns up, it should displace this.

### typography — designer

**Recorded reason:** "One row mentions typography anywhere … and it mentions it in the
summary, which is not indexed. A design directory that cannot answer 'typography' has a
hole in its shelves, not in its search."

The mechanism was right and the conclusion was backwards.

**Closest by search:** nothing. The query returned zero results.
**Closest by hand:** *Encode the brand as a skill*, *Package your brand guidelines in a
skill* — the only two rows whose text carries typograph- / font / type scale.

**Page opened.** [Package your brand guidelines in a skill](https://academy.claude.com/use-cases/package-your-brand-guidelines-in-a-skill)
— the page carries a labelled field: "**Typography:** Headings (24pt and larger): Poppins
font, bold weight / Body text: Lora font, regular weight / Fallbacks: Arial for headings
if Poppins unavailable, Georgia for body if Lora unavailable", plus follow-up prompts that
change the heading size. Typography is one of the two pillars of the skill it builds.

**Verdict:** the hole was in the card. `teaches` now says what the page says, and the
query returns the row.

## What changed because of this

- Seven suite rows re-graded from `content-gap` to `ok`, each with the page evidence in
  its reason.
- Two cards re-read against their pages: *Package your brand guidelines in a skill* (a
  `teaches` line naming typography) and *Claude in Excel for HR* (a question saying pivot
  table, which its own page's prompt says).
- `test-search.py` now refuses to run a `content-gap` row that does not carry
  `ruled_out` — the pages opened, each as "URL - what the page says".
  `scripts/test-gap-claims.py` proves the refusal fires and runs in the build.

## The thing worth remembering

Not one of the seven survived. The failure was not carelessness in any single row; it was
that a gap was allowed to be declared from the same summaries the search was already
failing on. The card is a claim about the page. A gap is a claim about every card at once.
Neither can be settled by reading cards.
