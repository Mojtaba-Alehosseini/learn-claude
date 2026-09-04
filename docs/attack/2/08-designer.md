# Attack 2: a designer
Written as a working designer, 2026-09-05. Chrome at 1440x950 and emulated 375x812. Live site
only: `https://mojtaba-alehosseini.github.io/learn-claude/`.

---

## 1. First 60 seconds

Landed on `index.html`. A hand-drawn mug the size of a dinner plate, and a Mad Libs sentence:
**"I'm a [role] and I've [level]."** The illustration swaps as you hover — mug, easel, browser
window, paintbrush. It is the single largest object on the screen and it carries zero
information.

Under it: **"635 resources, checked by hand."**

I clicked "a designer". Sentence completed, **"47 resources match so far"** appeared, paintbrush
loaded. That is a nice piece of interaction — the count moving as you choose is the best thing on
the page.

Then I read the tagline again — "635 resources, checked by hand" — and later found that **zero of
the 635 carry the tier the site defines as a person checking**. That is where the hour went.

---

## 2. The front door, all four levels

Two questions, sequential — role first, level appears after. Selecting a level auto-navigates;
the "Show me" button is vestigial for chip users.

| Level | URL | Resources | Picks block | Tiers in pool |
|---|---|---|---|---|
| never used Claude | `?role=designer&level=never-used` | **7** | 3 | 7 x Skimmed |
| used it a little | `?role=designer&level=basic` | 10 | 3 | 8 Skimmed, 2 Read by AI |
| used it a lot | `?role=designer&level=confident` | 19 | 3 | 13 Skimmed, 6 Read by AI |
| built things with it | `?role=designer&level=builder` | 11 | 3 | 11 x Skimmed |

**The "never used" cell.** Seven results. Three of them are then labelled "Start with these
three", and the next heading reads **"Everything else for you (4)"**. Being "curated" from seven
down to three is not curation, it is arithmetic. And every one of the seven is **Skimmed** — so
the default sort, "Best checked first", has nothing to sort by. Four of the seven are genuinely
about design; the other three are generic Claude orientation.

**Designer coverage overall: 47 items of 635 (7.4%).** "running a business" gets 235. A designer
is a rounding error in this catalogue.

Craft note on the hero: the display sentence is a `<p class="display">`; the actual `<h1>` is the
12px grey line "Find what's worth your time." There is a source comment defending it on
screen-reader grounds and the reasoning is sound — but visually the page has no headline, just a
caption and a form.

---

## 3. What the catalogue gives me

**Formats:** docs 307, article 124, video 101, course 58, repo 32, hands-on **7**, podcast 6.
Nearly **half the catalogue is documentation pages**. Seven hands-on items out of 635.

**Topics — the whole taxonomy:** `chat and prompting, Claude Code, Cowork, Skills, connectors,
agents, API, limits and safety`. Eight topics, every one of them an Anthropic product surface.
There is no topic for design, writing, research, or anything a reader actually does. And Topic is
hidden behind a "More filters +" toggle, so on first load I get Role, Level, Time and nothing
else.

**Card craft.** Measured on `browse.html?role=designer&level=never-used`:

- `.card-for` — Styrene 16px, `rgb(108,107,102)` (grey)
- `.card-skip` — Tiempos 20px, `rgb(20,20,19)` (near-black)

The **warning is 25% larger and at full contrast; the recommendation is smaller and greyed out**.
On a card whose stated job is "who it helps, and who should skip it", the hierarchy is inverted.
On the phone that means ten lines of black serif telling me not to read it, above four lines of
grey sans telling me why I should.

Card box: `#FAF9F5` on a `#F0EEE6` page, `0.8px solid #CCCBC8`, 24px radius, no shadow. At 375px
the border is invisible; the card stops reading as an object at all.

Real titles and lines I read:

> "Good from Afar, But Far from Good: AI Prototyping in Real Design Contexts"
> "Skip if: It will not teach you to drive any of the tools, and it is a year old - re-reviewed
> 2026-08-19, but the tools move faster than that."
> "Where can I access Claude? (country availability)" — "Skip if: The title is wrong for what
> this is. It promises somewhere to access Claude and delivers geography"
> "Skip if: You've already used Claude for a few weeks — this stays at 'what is a prompt' level
> and won't teach you anything new."

The writing is good. Better than the interface it sits in.

---

## 4. Paths

**Seven paths for ten roles.** There is exactly one for me: **"Judging AI's design output"**, and
its own intro says:

> "This covers about a fifth of a designer's job — deciding whether to trust what Claude just
> produced — and says nothing about the other four fifths."

I followed all five steps. **Every step reason explains its position, not just its merit.** This
is the only place on the site where the editorial voice earns the premise:

- Step 1: "Start here because the temptation is to assume a slick AI-generated screen is finished
  work."
- Step 2: "Read this while step 1's skepticism is still fresh, before you drift back to trusting
  output by default."
- Step 3: "its own skip_if says to read the findings first, which by now you have."
- Step 4: "Fourth, on a live task instead of someone else's write-up."
- Step 5: "Last, to widen the lens from one task to daily practice."

That is real sequencing. Nothing else on the site does this.

Two problems. **All five steps are tier "Skimmed"** — a recommended learning path where nobody
read any step in full (6 of the 7 paths have `weakest_tier: previewed`). And the design of the
path card is *better than the browse card* — thumbnail, "Step 1 · Article" kicker, rule, reason, a
"Start with this" CTA — which means the site has two card systems and put the weaker one on its
primary surface. On the path card the "Skimmed" badge and dates sit *below* the CTA, so you are
asked to click before you are told how thoroughly it was checked.

`paths.html` copy bug: **"4 steps · about 81 minutes"**. Everything at or above 93 minutes rounds
to hours; 81 stays raw with "about" bolted on front. It reads as a script output on a page selling
human judgment.

---

## 5. The card and the resource page

Three resource pages, and I would click through on two of them.

**`resource.html?id=r-50ce9b31c6`** (NN/g) — good page. Summary, three "What it teaches" bullets,
Who it's for, Skip it if, "Where this fits: This is step 1 of 5 in Judging AI's design output"
linking to `paths.html?id=judging-ai-design-work`. That is a proper deep link. Yes, I would click.

**`resource.html?id=r-dfee5f2159`** (Claude Code for Designers, Builder.io) — "Read by AI". Skip
it if: "It ends by selling you Builder's own tooling." Honest. Yes.

**`resource.html?id=r-bcd03ac245`** (Sales Analysis with Claude) — no, and it broke my trust in
the whole site. See section 12.

Three things wrong on resource pages:

1. **The path signpost is a dead end on the browse card.** On the card it is `<span
   class="card-path">Step 1 of 5 in Judging AI's design output</span>` — a plain span, `cursor:
   auto`, not a link. It is the only filled tan pill in the card's reading column, so it is the
   most eye-catching element, and it goes nowhere. The detail page links the same text correctly.
   Two different affordances for the same string.

2. **The detail page shows fewer dates than the list.** Browse card for the NN/g piece: "Checked 5
   Sep 2026 · Published 24 Oct 2025 · Updated 19 Aug 2026". Detail page: "Checked 5 Sep 2026 ·
   Published 24 Oct 2025 · Found through Nielsen Norman Group". `assets/js/resource.js` contains
   **zero references to `updated`** — the field is rendered only by the card. For "Claude Design
   Fundamentals" (`r-a494e31b55`) the detail page reads "No publish date given" while the card says
   "Updated May 2026". **44 items have an Updated date and no Published date; on their detail pages
   the only freshness signal disappears.**

3. **"What it teaches" is machine text with the product name mis-cased.** Live on
   `resource.html?id=r-f772cf9bea`, the H1 reads "Claude Code for Data Analysis: Excel-Free Answers
   From CSVs" and two inches below: "— Clean, dedupe, join, and pivot CSV files using **Claude
   code**." The source data is all-lowercase and `LC.sentence` in `ui.js` fixes single words from a
   `PROPER` map — `csv -> CSV` works, `claude code` does not, because `code` is not in the map.
   **164 bullets across 112 resource pages** render "Claude code", "Claude skills", "Claude
   projects". `ui.js` calls these bullets "generated", 2,201 of them.

---

## 6. The picks block

I measured it rather than eyeballed it. `getComputedStyle` on the wrapper and both card types:

```
.picks wrapper : background rgba(0,0,0,0) | border 0px none | padding 0px | radius 0px
pick card      : rgb(250,249,245) | 0.8px solid rgb(204,203,200) | 24px | none | 24px | class "card"
list card      : rgb(250,249,245) | 0.8px solid rgb(204,203,200) | 24px | none | 24px | class "card"
identical      : true
```

**There is no block.** No container, no tint, no rule, no numbering, no ordinal. The picks are
three ordinary cards with a grey paragraph hanging off the bottom of each. And the heading "Start
with these three" is Tiempos **24px / 600** — byte-identical to every card title on the page,
including the titles inside it. The section header has no hierarchy over its own contents.

Worse, the reason sits *outside and below* the card, `.pick-reason`, Styrene 16px grey, in the page
gutter. Reading order per pick: badge -> title -> source -> chips -> For -> Skip if -> dates ->
**then why we picked it, last**. The editorial judgment — the entire reason this site exists — is
the afterthought at the bottom of the stack, styled like a footnote.

**Does each reason add something?** Sometimes. Often it is the card's own "Skip if:" line with a
superlative glued to the front. Four of my twelve designer picks do this; across the whole site,
**15 of 109 picks share three or more verbatim six-word runs with the same card's own notes**. Two
examples, reason and note sitting about 4cm apart on one screen:

> **Reason:** "...the only one whose notes name concrete failure modes - **invented pixel values,
> and Claude calling 3:1 contrast acceptable when it is not**."
> **Skip if (same card):** "...including **invented pixel values and Claude calling 3:1 contrast
> acceptable when it is not**."

> **Reason:** "...the only guide in the pool straight about **where designers actually get stuck:
> git, pull requests, keeping code and Figma in step**."
> **Skip if (same card):** "...unusually straight about **where designers actually get stuck - git,
> pull requests, keeping code and Figma in step**."

Eleven shared six-word runs on that second one. When the reason *does* add something it is
genuinely sharp — "Chosen over the two longer written walkthroughs of the same product because our
notes say it is a designer's critique of output quality rather than a feature tour" — but you
cannot tell which kind you are getting until you have read both.

**Label:** "picked by AI · 4 Sep 2026". Which AI, against what criteria, from what pool — never
stated. And **the picks block silently disappears** on 3 of the 40 role-by-level cells:
`writer-marketer|builder` (3 results) and `teacher|builder` (2 results) show a bare list with no
explanation that anything is missing. `student|builder` has 0 results and a decent empty state.

---

## 7. Dates and tier badges

**Dates.** 489 of 635 items (77%) have no publish date. 445 of those have no update date either —
so **70% of the catalogue has no age signal at all beyond "we looked at it recently."** 44 have an
Updated with no Published. 3 have a month with no day.

On one card in my seven-result list:

> **"Checked 5 Sep 2026   No publish date given   Updated May 2026"**

Three date facts, none of which answers "does this still match Claude?" The site's own home page
promises: *"Claude changes every few months. You can see when we last looked, and whether the thing
is old."* For 70% of entries you can only see the former.

Visually the repeated grey line is fine — 13px, `#6C6B66`, 5.07:1, three gapped fields, no
separators. It is inert, and on a page of 700px-tall cards it is the last thing you would notice.
**"No publish date given" appearing on three cards in four does not read as scrupulous. It reads as
a scraper that could not find a date and a directory that shipped anyway.**

One date bug I can point at: on the NN/g card, `Skip if:` says "re-reviewed **2026-08-19**" and the
footer three lines below says "Updated **19 Aug 2026**". **The same date, twice, in two formats, on
one card.** Raw ISO leaking into prose on a site that formats every other date.

**Tier badges.** Four rungs, in `LC.TIER`:

| Badge | Definition | Count |
|---|---|---|
| Read in full | "We went through all of it, and a person checked the notes." | **0** |
| Read by AI | "AI read all of it. No person has checked the notes yet." | 98 (15%) |
| Skimmed | "We read the outline or a free sample. We have not seen the whole thing." | 501 (79%) |
| Found only | "We found it and sorted it. Nobody has looked at the content yet." | 36 (6%) |

The badges themselves are well made — 12px Styrene, quiet, tooltipped with the full definition, and
the tooltip is exposed to screen readers via `title`. They are worth reading. What they say is the
problem.

**"Skimmed" is doing enormous work and never says who skimmed.** There is a separate tier for "Read
by AI", which strongly implies "Skimmed" means a person. The site never confirms it, and the home
page's "checked by hand" is the only thing filling that gap.

---

## 8. Search, in my words

| # | Query | Count | Top three | Verdict |
|---|---|---|---|---|
| 1 | `claude for figma` | 17 | 1. Claude Code and Figma: Set up the MCP server [Read by AI] · 2. From Claude Code to Figma [Read by AI] · 3. Claude Code for Designers (Builder.io) [Read by AI] | **Good.** All three on target, all three the best-checked tier. |
| 2 | `will ai design replace me` | 47 | 1. How to Use Claude Code for UX Writing · 2. Claude Code for Data Analysis: Excel-Free Answers From CSVs · 3. Claude Code for Product Managers | **Failure.** The highest-intent query a designer types, answered with a CSV tutorial. The catalogue *contains* the answer: "Good from Afar, But Far from Good" ranks **5th**, and "AI Can't Replace Real Research in Empathy Mapping" — which has the word *Replace* in its title — ranks **32nd of 47**. |
| 3 | `design system` | 47 | 1. Set up your design system in Claude Design [Read by AI] · 2. Claude Design: The Complete Guide · 3. Building AI-driven workflows powered by Claude Code | **Good.** Right three. 47 results for a two-word query is loose, but the head of the list is correct. |
| 4 | `accessibility` | **4** | 1. Design plugin (official) · 2. Design Systems in 2026: Turn Your System into a Claude Skill · 3. knowledge-work-plugins/design/skills (source) | **Thin.** Four items in 635. The results are defensible, but a design directory with four accessibility hits has a hole where half my job lives. |
| 5 | `design critique` | 18 | 1. Design plugin (official) · 2. knowledge-work-plugins/design/skills (source) · 3. Claude Design: The Complete Guide | **OK.** Same two plugin entries again at the top for a third query. The plugin repo is becoming the answer to everything. |
| 6 | `typography` | **0** | — "No match for "typography". Try fewer words, or browse by role instead." | **Failure, plus a copy bug.** Zero results for *typography* on a design directory. And the empty state tells me to "**Try fewer words**" — I typed one word. The advice is impossible to follow. |
| 7 | `stop claude inventing pixel values` | 30 | 1. 3 Mind Blowing Claude & Consensus Research Workflows · 2. Writing effective tools for agents · 3. Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents | **Failure.** The card containing the literal phrase "invented pixel values" — "Claude for Designers in 2026" — is not in the top three. `assets/js/search.js` says the index is built from `keywords`, `questions` and `teaches` only; the `skip_if` and `who_for` notes, which are the best writing on the site, are **not searchable**. |

Search is competent on nouns and useless on sentences — which is exactly backwards from the
placeholder's promise, *"Title, topic, or what you want to do"*.

---

## 9. On a phone

375x812, `browse.html?role=designer&level=never-used`. Measured, not estimated.

- **First card starts at y = 609px.** You scroll 75% of a screen past a stacked header, an enormous
  "Browse" H1, Search, Sort, filter pills and two headings before any content.
- **Card heights: 711, 545, 422, 633, 748, 499, 626 px.** The tallest card is **92% of the
  viewport**. One card is one screen. You cannot see two results at once anywhere on this site, so
  you cannot compare anything.
- **Total document: 6,006px for seven results.** 7.4 screens for seven items. There is no compact
  mode, no collapse, no way to hide the "Skip if" prose.
- A permanent full-width **"Filters"** bar is pinned at the bottom, 69px tall on an 812px screen,
  and it clips the bottom of the card behind it.
- Corner-radius language breaks inside 400px of screen: search field and Filters button are
  pill-rounded, the active filter pills ("a designer x") are square rectangles.
- Sort sits above the results and below Search, eating ~130px. Sort should never outrank content on
  a phone.
- Tap targets are fine — everything interactive clears 44px except the 40px wordmark.

No horizontal overflow at any width I tried. The mobile problem is not breakage, it is density:
this is a reading site pretending to be a directory.

---

## 10. Keyboard walk

`browse.html?role=designer&level=never-used`, Tab from `document.body`, `activeElement` logged at
each step.

Order is correct and sane. The skip link works and reveals itself (`.skip-link:focus { left:
var(--space-8) }`). `:focus-visible` is used properly — no rings on mouse clicks. And there is a
genuinely elegant touch: `.card:has(.card-title a:focus-visible) { outline: var(--focus-ring) }`
puts the ring around the whole card when the title link is focused, rather than around the text.
Someone thought about this.

**And then the main control surface breaks it.** With focus on the "a student" filter button
(`:focus-visible` confirmed true), the rendered indicator is **two horizontal black rules and no
box**:

```
button.filter-option  x=144  right=398
.filter-rail          x=144  right=408   overflow-y: auto
outline: 2px solid #141413, outline-offset: 2px
-> outline draws at x=142.4, clipped by the rail
```

The button's left edge is flush with its scrolling parent, so the ring's left side is clipped away.
What you see is a line **under "not a coder"** and a line **under "a student"** — a keyboard user
reading quickly attributes focus to the wrong row. This affects every button in Role, Level, Time,
Topic, Format, Cost and Source.

Second issue: the filter rail is a nested scroller (`clientHeight 682`, `scrollHeight 1047`) inside
a page that also scrolls. Tabbing into it scrolls the inner region while the page stays put.

The hidden mobile sheet is correctly `display: none`, so its 40 duplicate controls stay out of the
tab order. Good.

---

## 11. How we check

**Less. Considerably less, and the page does it to itself.**

It opens with:

> **"We would rather have 70 resources we can vouch for than 700 we cannot."**

The site ships **635**, and by its own definitions it can vouch for **zero** of them.

Then, under "How thorough we were — Four levels, and we do not round up", the four badges are
listed. **"Read in full" is rendered as the only solid-black, full-contrast badge on the page** —
the strongest visual element in the whole document. It has zero members. The page teaches me a
ladder and gives top billing to the rung nobody is standing on, without ever saying so.

Then "What we do": *"We find material, read it, and write two things."* By the site's own tiers,
"read it" is false for the 501 Skimmed and impossible for the 36 Found only — **537 of 635**.

There is also a wording drift: "Skimmed" is defined as *"We read the outline or a free sample. We
have not seen the whole thing"* in the tooltip, and *"We read the outline or a free sample. Paid
courses usually stop here, because we cannot see inside them"* on this page. Two explanations for
one badge, and the second one is a much softer claim.

And the disclosure that is not here. The shipped `assets/js/search.js` states in its own header
comment:

> "The index is built offline by scripts/build-search-index.py from the hidden fields **Gemini
> wrote for every resource**: `keywords`, `questions` and `teaches`."

`teaches` is what `resource.js` renders on every resource page as **"What it teaches"**. So the
learning-outcome bullets on 635 pages were written by a third-party model, and the page titled "How
we check" — which lists four levels of scrutiny and a "What we will not do" section — never mentions
it. The only AI the reader is told about is the 98 "Read by AI" cards and the "picked by AI" line.

What the page gets right: "We do not take money to rank a resource", "We are not affiliated with
Anthropic", the honest note that the report link "needs a GitHub account, which is a real barrier
and we know it", and the genuinely useful paragraph about Claude certification being
Partner-Network-only. That is a page written by someone with integrity. The catalogue underneath it
does not hold up the claims.

---

## 12. Everything broken, ranked

### 1. A tier that says nobody looked at it, on a page full of claims about the content — CRITICAL

**URL:** `resource.html?id=r-bcd03ac245`. Badge **"Found only"**. Below it: "What it teaches —
Identify key trends and patterns in raw sales spreadsheets / Create visual summaries of sales
performance using Claude / Generate strategic business recommendations based on dataset findings".
"Skip it if — **Nothing in it visibly tells you to check Claude's arithmetic**, which for a project
built on sales numbers is the omission that matters. Ninety guided minutes...". Then, at the foot:
"How we checked this one — **Found only. We found it and sorted it. Nobody has looked at the content
yet.**"
**Expected:** If nobody looked at the content, the page cannot tell me what is and is not in the
content. **Reproduced on all 36 "Found only" items.**
**Harms:** everyone. Either the badge is lying or the note is invented, and the reader has no way to
tell which.

### 2. "checked by hand" / "we can vouch for" vs zero verified items — CRITICAL

Home: "**635 resources, checked by hand.**" How we check: "**We would rather have 70 resources we
can vouch for than 700 we cannot**", with "Read in full — We went through all of it and a person
checked the notes" rendered as the only solid-black badge on the page.
**Measured:** `previewed` 501, `ai-reviewed` 98, `listed` 36, `reviewed` **0**.
**Harms:** a beginner deciding what to spend four hours on.

### 3. Time chip contradicts the card's own text, inside the picks block — HIGH

`browse.html?role=designer&level=never-used`. In one card: chips `course · **half a day** · free`.
Directly below: "Skip if: You want depth — **at 15 minutes** across 13 short lectures, this is a
primer". Directly below the card: "picked by AI" reason — "...and **at 15 minutes** across 13 short
lectures it is sized for someone who has not yet decided whether to invest at all."
**Harms:** anyone filtering by time. Filter "15 min" and you never see the course the site picked
*for being 15 minutes*. The whole Time facet is unreliable.

### 4. Focus ring on every filter control renders as two loose lines — HIGH

Tab x8 from the top. `activeElement = button.filter-option "a student"`, `:focus-visible` true.
Saw: two horizontal black rules — one directly under "not a coder", one under "a student" — no box.
Left edge clipped: button `x=144`, `.filter-rail` `x=144` with `overflow-y: auto`, ring drawn at
`x=142.4`.
**Harms:** keyboard and low-vision users, on the primary control surface of the primary page. The
visible line sits under the *previous* item's label, so it actively misreports where you are.

### 5. Search fails the sentences it invites — HIGH

"will ai design replace me" -> 47 results; the on-topic NN/g piece 5th, "AI Can't **Replace** Real
Research in Empathy Mapping" 32nd. "stop claude inventing pixel values" -> 30 results, and the card
literally containing "invented pixel values" is not in the top three. "typography" -> 0.
**Cause:** `search.js` indexes `keywords`, `questions`, `teaches` only. The `skip_if` and `who_for`
notes — the site's best writing — are unsearchable.
**Harms:** anyone who types a worry instead of a noun.

### 6. The picks block is not a block — HIGH (design)

`.picks` wrapper — `background rgba(0,0,0,0)`, `border 0px none`, `padding 0px`, `radius 0px`. Pick
card and list card computed signatures **identical**. "Start with these three" is Tiempos 24px/600 —
the same as every card title on the page.
**Harms:** every reader. The most valuable content on the page has no visual claim on it, and the
reason for each pick is the last thing you read, in grey, outside the card.

### 7. The detail page hides the freshness date the list shows — MEDIUM

Card "Checked 5 Sep 2026 · No publish date given · **Updated May 2026**"; detail page "Checked 5 Sep
2026 · No publish date given · Found through Coursera". `assets/js/resource.js` contains **no
reference to `updated`**. Affects all 44 items that have an Updated and no Published date.

### 8. "Skip if:" outranks "For:" typographically — MEDIUM (design)

`.card-skip` Tiempos 20px `#141413` vs `.card-for` Styrene 16px `#6C6B66`. The reason not to read is
louder than the reason to read, on every one of 635 cards.

### 9. Path signpost is a dead span on the card — MEDIUM

`<span class="card-path">Step 1 of 5 in Judging AI's design output</span>` — the only filled tan pill
in the card body, `cursor: auto`, not a link. The same string on the resource page links correctly.

### 10. Product name mis-cased on 112 resource pages — MEDIUM (craft)

H1 "Claude **Code** for Data Analysis" and, inches below, "using Claude **code**". **164 bullets,
112 pages.**

### 11. Empty-state copy that cannot be followed — LOW

"No match for "typography". **Try fewer words**, or browse by role instead." One word was typed.

### 12. "about 81 minutes" — LOW

Rounding applies above 90 minutes and not below.

### 13. Picks silently absent on three cells — LOW

`writer-marketer|builder` (3 results) and `teacher|builder` (2) render no "Start with these" block
and no explanation.

### 14. The one flash of colour is a vendor endorsement — LOW (design)

`.publisher-official { background: var(--surface-feature) }` — a filled tan pill. **390 of 635 items
carry it, and every single one is Anthropic** (Anthropic Academy 292, Anthropic 53, Claude Help
Center 31, Claude Code docs 7, Claude Platform docs 5, Claude Privacy Center 2). Independent
publishers get grey text. On a site that states "We are not affiliated with Anthropic", the visual
system says otherwise.

### 15. Pick dates predate the checks on their own pools — LOW

`designer|never-used` is labelled "picked by AI · 4 Sep 2026" while **6 of its 7 candidates were
checked on 5 Sep 2026**. 27 of 37 cells show the same pattern. Not proof the picks are wrong; it
does mean the label's date cannot be read as "current as of".

---

## 13. The one thing that would make me leave

**"Found only. We found it and sorted it. Nobody has looked at the content yet"** — printed under a
page that has just told me, in confident detail, what is inside the thing.

Everything else I could forgive. A directory that admits it only skimmed is more honest than most.
But a page that simultaneously says *nobody looked* and *here is what is missing from what nobody
looked at* has told me its notes are not reports. Once I believe that about one card, I have to
assume it about the 501 "Skimmed" ones too — because I have no way to tell which notes came from
reading and which came from a model filling in a template. At that point every "Skip if:" on the
site, however well written, is decoration. I close the tab.

The near-miss runner-up: **"635 resources, checked by hand"** on the front door, with zero
hand-checked resources behind it.

---

## 14. What is genuinely good

- **The paths.** "Judging AI's design output" is the real product. Every step says *why it sits
  there*: "Read this while step 1's skepticism is still fresh." Nothing else in this category does
  that. The path card design is better than the browse card.
- **The Mad Libs front door.** Two questions, illustration follows the hover, "47 resources match so
  far" updates live. It is charming and it works.
- **The "Skip if:" line as an idea.** "The title is wrong for what this is. It promises somewhere to
  access Claude and delivers geography." That is a real editor's sentence.
- **Honesty where it costs something.** The design path admits it covers "about a fifth of a
  designer's job". The report link admits GitHub "is a real barrier and we know it". The empty state
  says "It's on the list." The certification section explains why exam-prep sites are excluded.
- **Focus handling, mostly.** Proper `:focus-visible`, a working skip link, and `.card:has(.card-title
  a:focus-visible)` to ring the whole card. It is a shame the filter rail clips it.
- **Type and palette.** Tiempos over Styrene on `#F0EEE6` is a good, restrained pairing, and every
  text colour I sampled clears AA (5.07:1 body grey, 4.60:1 pick reason). The hand-drawn icons are
  lovely at 2x — they just do not survive 24px.

---

## Checklist
- [x] I opened the live site at all four levels of my role — 7 / 10 / 19 / 11
- [x] I quoted at least 5 real titles or lines from the site — 20+
- [x] Every number I used is measured with `getComputedStyle`, `getBoundingClientRect`, or counted
      from the shipped data
- [x] I looked at a phone width — 375x812, every card height measured
- [x] I did one full keyboard walk — and photographed the clipped focus ring
- [x] Seven search queries in my own words, each with its verdict
- [x] I read the picks block and measured it — there is no block; the wrapper has no background,
      border, padding or radius, and the pick card is byte-identical to a list card
- [x] I found at least one thing nobody has mentioned before — the focus ring on every filter button
      is clipped by its own scrolling rail and renders as two loose horizontal lines under the wrong
      labels; and the only coloured pill in the whole design system marks Anthropic material, on a
      site that disclaims affiliation
