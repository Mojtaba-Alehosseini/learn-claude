# Can designer or data-analyst support a path yet?

Re-measured 2026-08-27, after adding four resources. **data-analyst: yes. designer: no.**
Neither path is built — that is the next conversation.

## The shape a path has to have

Measured from the five that exist, so this is not an invented standard:

| path | steps | time | levels |
|---|---|---|---|
| first-week | 6 | about 2 hours | 3 never-used, 3 basic |
| claude-code-start | 6 | about 3 hours | 1 basic, 2 confident, 3 builder |
| writing-you-sign | 5 | about 2 hours | 5 basic |
| pm-without-engineering | 5 | about 2 hours | 5 basic |
| research-with-claude | 5 | about 2 hours | 2 basic, 3 confident |

Five or six steps, about two hours, and a first step a reader can actually take.

## data-analyst — yes, and the thing that changed is small

45 resources: 5 never-used, 21 basic, 12 confident, 7 builder.

The role was never short of material. It was short of a **first step**. All three of its
never-used entries were general Claude courses — Claude 101, Claude 101 (DataCamp), AI
capabilities and limitations. None of them was about data. A path for a data analyst that
opens with "take a general introduction to Claude" is a path that has not started.

Both additions are first steps and both are about this reader's own work:

- **Upload files to Claude** — how your spreadsheet gets in front of Claude at all
- **How long do you store my data?** — whether it should, before you upload company data

A spine now exists: get the file in, know what happens to it, then the analysis tool,
then the two-modes trap (Claude reads a CSV two ways and only one runs the arithmetic),
then a practical tips course. Five steps, under two hours, all free.

The weak point to name when the path is built: the strongest correctness material in this
role — the CSV honest guide, Panko's 94% — sits at `confident`, and the honest opening
sits at `never-used`. The path will have a level jump in the middle. That is a real
weakness and it belongs in the path's own text rather than being smoothed over.

## designer — no, and the additions did not change it

33 resources: 3 never-used, 9 basic, 18 confident, 3 builder. The counts look adequate.
They are not, because of what the basic tier contains:

| basic designer resource | what it is really about |
|---|---|
| Using Claude Design for prototypes and UX | Claude Design |
| Get started with Claude Design (Help Center) | Claude Design |
| How to Use Claude Design for UX/UI | Claude Design |
| Claude Design: The Complete Guide | Claude Design |
| A designer's first attempt at building with Claude Code | Claude Code |
| How to use Claude Code for non-engineering use cases | Claude Code |
| Introduction to Claude Cowork | general |
| Claude for Designers in 2026: Where AI Actually Helps | a map, not a method |
| **Analyze patterns in user feedback** | **research synthesis** ← the new one |

Four of nine are prototype generation and three are Claude Code. Exactly one is design
work that is neither, and it is the one added today.

A path built from this would read: weak general opener, Claude Design, Claude Design,
Claude Design, Claude Code. That is a Claude Design tutorial wearing the word "path". A
designer who does critique, research and systems work would finish it having learned to
generate mockups.

The never-used tier is worse. Three entries: a listed course about AI limits that is not
about design, a roundup article of other people's courses, and a Claude Design first-look
video. One of the three is tightly scoped. None is a starting point for a designer.

## What designer actually needs, stated precisely

Not "more designer content". Three specific things, all of them **basic** level and none
of them prototype generation:

1. **Design critique.** Give Claude a screenshot or a Figma frame and get useful feedback.
   Everything found in this space is a Claude Code skill on GitHub, which is `builder`.
2. **Design systems**, below `confident`. Both current entries assume you already maintain
   one and can write a SKILL.md.
3. **A never-used starting point** that is about design work rather than about Claude
   Design the product.

The 2026 search space for all three is genuinely poor: Claude Design articles, GitHub
skills, and skill-directory aggregator sites that list the same skills with generated
blurbs. If these do not exist, the honest position is that designer stays a browse role
without a path, and the site says so rather than shipping a path that misleads.

---

# Re-measured 2026-08-28, after searching the three named gaps

**data-analyst: path built** (`numbers-you-can-defend`, 5 steps, ~2 hours, free).

**designer: still no — but the gap is now small and specific, and it is not "more
content".**

## What the search found, and the mistake it exposed

Last round I searched *Claude + design critique* and got GitHub skills and skill-directory
aggregators, and concluded the material did not exist. It does. **Nielsen Norman Group has
a whole AI topic area** and I never saw it, because NN/g does not write about Claude — it
writes about design. Searching for the tool hid the work.

Three added, all NN/g, all free, all named authors, all `previewed`:

| level | resource | what it is |
|---|---|---|
| never-used | Good from Afar, But Far from Good | original research: heuristic evaluation of AI-generated designs vs a human designer's, ten tools including Claude, three grades of prompt |
| basic | Testing AI with Real Design Scenarios | the method behind it — six copyable prompts and four judging criteria |
| never-used | AI Can't Replace Real Research in Empathy Mapping | the line: it can organise research you collected, it cannot invent a user |

One rejected after reading it twice: **The Core Skill of Design in the AI Era: Critique**.
The title is the gap and the article is not — it is about designing AI-*powered products*
and evaluating model outputs, with a worked example of a "repetitiveness judge" for a
calendar assistant. Right word in the title, wrong job.

## The count, and why it still is not enough

Categorising every designer entry by what it is actually about:

| level | Claude Design | Claude Code | the work |
|---|---|---|---|
| never-used | 2 | 0 | **2** (was 0) |
| basic | 4 | 2 | **4** (was 3) |
| confident | 1 | 13 | 4 |

A path is now constructible and I got as far as writing it out:

1. Good from Afar — what AI prototyping actually does and does not do
2. Claude for Designers in 2026 — where it helps
3. Analyze patterns in user feedback — do one real piece of synthesis
4. AI Can't Replace Real Research — the boundary on that work
5. Testing AI with Real Design Scenarios — judge what comes back

Five steps, about two hours, free, not one Claude Design tutorial. It passes the stated
test: every step teaches design work.

**It still fails the test that matters.** Ask what a designer could do differently on
Monday: two real skills — synthesise feedback, test a tool against a real task — and three
judgements. Compare the writing path, which is four skills in five steps. Every other path
on the site has a *making* spine and this one has research synthesis and nothing else.

It would be a path about **judging AI's design output**. That is a real and useful thing.
It is not a designer's path; it is one fifth of one, and shipping it under the role's name
would tell a designer this is what Claude is for them.

## What would change the answer

Two resources, and they are the same two named a day ago:

1. **Design critique of your own work at `basic`.** Give Claude a screenshot or a Figma
   frame and get feedback worth having. The new step 4 is evaluation criteria for testing
   a *tool*; it is not a method for critiquing a *mockup*. Still nothing.
2. **Design systems below `confident`.** Both current entries assume you already maintain
   one and can write a SKILL.md.

Accessibility review is a third, and it is the closest to solved — `accessibility-review`
inside the official design plugin runs a full WCAG 2.1 AA audit, but it sits at `builder`
in a source repo.

Two more like the three added today and the answer flips. That is a shopping list, not a
hope.
