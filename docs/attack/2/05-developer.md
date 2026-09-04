# Attack 2: a developer
Written as a developer, 2026-09-05, about one hour. Live site only:
`https://mojtaba-alehosseini.github.io/learn-claude/`.

---

## 1. First 60 seconds

Fast. 258 ms to first byte, no layout jump, no cookie banner, no newsletter modal. That buys
goodwill immediately.

Then the sentence: **"I'm a [role] and I've [level]."** I like it. It is a real question, not a
hero headline.

Two things went wrong inside the first minute.

**A chip that looks chosen is not.** Sitting still on the home page, one role chip at a time
lights up with a filled background — "a designer", then "running a business", then "a writer",
one every ~2.6 s. I dumped the DOM at 900 ms intervals for 8 ticks:

```
sentence: "I'm a [role] and I've [level]."
tick 1: a designer          [aria-pressed=false]
tick 3: running a business  [aria-pressed=false]
tick 6: a writer            [aria-pressed=false]
```

The highlight is a `data-showing` attribute. `aria-pressed` stays `false` on all ten. So a
sighted person sees a selection that does not exist, and a screen-reader user gets no signal at
all that the illustration is changing. I clicked "Show me" on my first pass assuming "a student"
was selected. It was not.

**395 KB to print one number.** The home page pulls `data/items.js` — 765 KB raw, 202 KB gzipped,
the entire 635-item catalogue — plus five self-hosted font files, and uses it to render "635
resources, checked by hand." That is ~395 KB over the wire before a single illustration loads. On
a train, that page is blank for a while for a sentence and a count.

---

## 2. The front door, all four levels

| Level | Result |
|---|---|
| never used Claude | **7** |
| used it a little | **20** |
| used it a lot | **45** |
| built things with it | **64** |

The "never used" cell is worse than thin — it is mis-stocked. Three of the seven are the picks
block. Here is the entire "Everything else for you (4)":

- **"Tokens: why some inputs cost more than others"**
- **"Using the Blender Connector in Claude"** — *For: Blender users who want Claude to work with
  their live open scene.*
- **"Using the ICD-10 Connector in Claude"** — *For: Medical coders and billing specialists
  validating diagnosis and procedure codes.*
- **"What are skills?"**

I told the site I am a developer who has never used Claude. It handed me a 3D-modelling connector
and a medical-billing connector. Nothing about the API, nothing about the Messages API, nothing
about claude.ai. Half of my non-pick results are for people who are not me.

The three levels above it are fine — 64 items at builder level is a real catalogue. The problem
is entirely at the entry point, which is the one place a stranger lands.

Worth noting the other end: **student + "built things with it" returns 0.** The front door lets
you answer both questions and walk into "We have nothing for this combination yet." The empty
state is honest and offers a way out, but the front door should not offer the dead end in the
first place.

---

## 3. What the catalogue gives me

The cards are the best-written thing here. Real, specific, opinionated:

> **"Skip if:** Skip if you do not write shell scripts. Every example is a bash file, and without
> that you cannot use any of it." — *Completely understand hooks in less than 20 minutes*

> **"Skip if:** Skip it if you do not have an API key with credits - the notebooks call the paid
> API, and reading them without running them gives you far less than the time costs." — *Claude
> Cookbooks*

> **"Skip if:** Skip if you need Zero Data Retention or a HIPAA BAA. Managed Agents is stateful by
> design and is not eligible for either." — *Claude Managed Agents overview*

That last one is genuinely useful information that I would otherwise find out three weeks into a
project. Whoever wrote these knows the material.

**Then I looked at where the 635 come from.** Host breakdown:

```
 291  academy.claude.com   (24 courses, 118 tutorials, 148 use-cases)
  72  youtube.com
  31  github.com
  31  support.claude.com
  19  claude.com
  13  anthropic.com
```

46% of the catalogue is one host. 148 of those are `academy.claude.com/use-cases/` — Anthropic's
prompt-recipe gallery, 143 of them tagged "15 min". Titles: **"Account research"**, **"Account
tracking"**, **"Recap your ad performance"**, **"Call prep sheet"**, **"Sprint retro handoff"**,
**"Design a local foraging guide"**. Plus 31 `support.claude.com` Help Centre FAQs like "What is
the Team plan?" and "How long do you store my data?".

That is ~297 entries, 47% of the catalogue, harvested from three Anthropic sub-sites. The home
page argues: *"A link with no judgment is just a list, and lists are what made this hard in the
first place."* Half the catalogue is a list — Anthropic's own — re-listed one card at a time. 635
is a padded number.

**And the level axis is broken by it.** 78 of those 148 fifteen-minute recipes are filed `level:
builder` — "built things with it." Example, in full:

> **Account tracking** · 15 min · builder
> *Cowork scores account health as red/yellow/green from usage data, open support tickets, NPS and
> the success plan.*

That is not an advanced resource. It is a recipe with a lot of prerequisites. The level filter is
measuring integration setup, not how much Claude I know — which is exactly what the front door
asks me.

---

## 4. Paths

Best thing on the site. I followed **"Getting good at Claude Code"** and read every step reason:

1. *"Anthropic's own course. Do this before reading anyone's tips, so you know which behaviours
   are the tool and which are the person writing about it."*
2. *"Densest thing written about Claude Code, and everything after this assumes you have read
   it."*
3. *"Read this third and not later, because it invalidates a lot of 2025-era advice you will
   otherwise absorb."*
4. *"Now that your setup is right, this is where the speed comes from — knowing which commands
   quietly destroy your prompt cache mid-session."*
5. *"It only makes sense once you have felt a long session degrade."*
6. *"Last, because orchestration is worth nothing until single sessions are reliable."*

Every one earns its position. Nobody else does this. I would follow it.

Two problems.

**The path contradicts itself.** Step 3's whole justification is that it *"invalidates a lot of
2025-era advice you will otherwise absorb."* Step 5 is **"Effective context engineering for AI
agents", published 29 Sep 2025**. The path spends step 3 inoculating me against 2025 advice and
then feeds me 2025 advice two steps later, with no note reconciling them.

**Every one of the six steps is Anthropic.** All `official: true`. Meanwhile the picks block for
developer/confident recommends *"Claude Code (Frontend Masters)"* on the grounds that it is *"the
only course in the pool that covers the newer features most 2025-era tutorials never mention"* —
and it is not in the path. The site's two recommendation engines disagree about what a developer
should read.

Smaller: the path header says **"free"**; step 1's own chip says **"sign-up needed"** (`cost:
free-account`). For a site whose method page says "we do not round up," that is rounding up. And
the writer path is labelled **"about 81 minutes"** where every other path says "about 2 hours" /
"about 3 hours" — the rounder gives up below 90 minutes and prints the raw integer.

---

## 5. The card and the resource page

Would I click through? On the well-checked ones, yes. The resource page for *Building effective
agents* has: summary, "What it teaches" (4 bullets), "Who it's for", "Skip it if", "Before this"
(prerequisites), how-we-checked, dates, and a report link. That is more than the source page tells
me about itself.

**But the card throws away the date exactly when I need it.** The home page promises: *"We show
the date. Claude changes every few months."* On the browse card, *Building effective agents* says:

> Checked 5 Sep 2026 · **Published over a year ago — may not match Claude today**

No date. The data has `published: "2024-12-19"`, and the **resource page shows "Published 19 Dec
2024"**. So the one card where age is the deciding factor is the one card that hides the number,
and I have to click through to get it. Dec 2024 vs Jan 2026 is a completely different decision.

**The time chip lies on at least five entries.** `resource.html?id=r-bcd03ac245`:

> chips: `hands-on` · **`half a day`** · `subscription`
> summary: *"Guided **1.5-hour** project analyzing sales data with Claude"*
> skip if: *"**Ninety guided minutes**, and you need Claude Pro on top of the Coursera side."*

Same screen, three different answers. Others: **"Complete Claude Code Course In 2 Hours For
Developers"** — filed "half a day". **"AI capabilities and limitations"** — filed "half a day",
its own text says 15 minutes. Time is one of only four primary filters.

---

## 6. The picks block

**This is the part that made me stop being cynical.** Real judgment, real comparison. It is not
the first three rows — two of the three developer/builder picks are `previewed` tier and would
sort below ~30 `ai-reviewed` items under the default "Best checked first."

Each reason does work the title cannot:

> *"The canonical context-engineering piece in this pool says in its own notes that this one
> reverses several of its recommendations on Claude 5 models — so the follow-up takes the slot the
> classic would otherwise hold."*

> *"Its who_for is this cell almost word for word — installed, used daily, still getting mediocre
> results — and it is corrective by design, which its own card says only works once you have your
> own bad habits to match it against."*

> *"The decision layer the pool's twelve single-feature intros each lack: when to reach for
> CLAUDE.md versus a skill versus a hook versus a subagent, written for people whose CLAUDE.md is
> already a mess."*

That third one is why I would trust "picked by AI" *up*, not down. It names what the alternatives
failed to do.

**Then I checked the facts inside the reasons, and three of them are wrong.**

Developer/builder, pick 2:
> *"The deepest **non-Anthropic** material in the pool ... by the SDK's own engineer"*

The title on the card directly above it is **"Claude Agent SDK [Full Workshop] — Thariq Shihipar,
Anthropic."** It calls an Anthropic engineer's talk non-Anthropic material and credits the
Anthropic engineer in the same sentence.

Data-analyst/never-used and pm/never-used both pick **"Claude 101 (DataCamp)"**, whose author
field reads **"Created by Anthropic, adapted for the DataCamp platform"**, and describe it as:
> *"The pool's one **non-Anthropic voice**"* and *"from the pool's **strongest non-Anthropic
> voice**"*

This is systematic, not a typo: the generator is reading `official: false` (= "not published on an
Anthropic domain") as "not from Anthropic." Independence is the exact axis these reasons are
selling. Three of 37 cells argue for a pick on a ground the site's own data denies.

Also: **3 of 40 cells have no picks block** — `student|builder`, `teacher|builder`,
`writer-marketer|builder`.

---

## 7. Dates and tier badges

**Dates.** Measured from the shipped data:

- 489 of 635 (77%) have `published: "UNVERIFIED"`
- **445 of 635 (70.1%) have neither a publish date nor an updated date** — the card just says "No
  publish date given"
- 96 have `updated`; 44 of those have no publish date, so the card reads "No publish date given"
  with "Updated 2 Sep 2026" underneath
- 3 have month-only updates ("Updated May 2026")

The `checked` dates are all recent and clustered: 276 on 2026-08-29, 211 on 2026-09-05, 66 on
2026-08-21. That reads as three bulk passes, not continuous maintenance — but it is recent, and it
is real.

**Maintained or abandoned?** Maintained, but shallowly. The `checked` dates prove somebody ran a
job in the last week. What they do not prove is that a person looked. And the sitemap says
otherwise (see section 12).

The reasoning behind the date rule is sound — I read `LC.freshness`, it takes the later of
published/updated, it floors month-only dates to the 1st so ambiguity always reads *older*. That is
careful. It is undermined by the card refusing to print the actual number when the answer is "over
a year."

**Tier badges.**

```
Skimmed     501  (79%)   "We read the outline or a free sample"
Read by AI   98  (15%)   "AI read all of it. No person has checked the notes yet."
Found only   36  ( 6%)   "We found it and sorted it. Nobody has looked at the content yet."
Read in full  0
```

Four-fifths of the site is somebody's skim. Publishing that honestly is the single most
respectable decision here. But see finding 2 below.

---

## 8. Search, in my words

**Q1 — `claude code hooks`** (62 hits)
1. Hooks reference (Claude Code) — score **34.64**
2. Claude Code: A Highly Agentic Coding Assistant (DeepLearning.AI) — **34.64**
3. Completely understand hooks in less than 20 minutes — **34.64**

**Verdict: fails.** Three-way tie to two decimal places, so the order is whatever the data file
happened to be in — there is no tie-break. #1 is a reference page whose own card says *"Read the
hooks guide first. This is a lookup reference, not a tutorial, and it is enormous."* #2 is not
about hooks at all. The actual hooks tutorial — **"Hooks in Claude Code — Full Theory + Practical
Use | CampusX"** — ranks **5th**, below **"CLAUDE CODE Full Course For Beginners (DATA DOMAIN
Edition)"** at #4.

**Q2 — `how do i stop claude touching my tests`** (30 hits)
1. Red Green Refactor is OP With Claude Code (Matt Pocock)
2. Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents
3. Head of Claude Code: What happens after coding is solved (Boris Cherny)

**Verdict: half-credit.** #2 is the right answer. #1 is adjacent. #3 is a career podcast whose own
card says *"Skip if you want technique. There is almost nothing here you can copy into your
terminal."* The site knows the result is useless for my question and shows it third anyway.

**Q3 — `mcp server oauth`** (18 hits)
1. Build an MCP Server from Scratch in 2026 | Local, Remote, OAuth & Claude Skills
2. **Tableau MCP (official)**
3. Introduction to Model Context Protocol

**Verdict: pass, with junk at #2.** #2 is a Tableau connector repo tagged `data-analyst` that
matched because its skip-if says *"a personal access token or OAuth configured before you begin."*
Substring luck.

**Q4 — `reduce token usage`** (8 hits)
1. A Guide to Claude Code 2.0 and getting better at using coding agents
2. **A Better (and Cheaper) Figma MCP or How To Let Claude Design**
3. How to select the right effort setting for Claude Cowork and Chat

**Verdict: fails.** Eight results total. #1's own card says *"Skip it if you need current detail —
it documents Claude Code 2.0 as of December 2025."* #2 is a designer's Figma article ("cheaper").
#6 is **"Reduce hallucinations"** — matched on the word "reduce." Meanwhile the catalogue contains
**"How context affects Claude's performance and cost"** and **"Code execution with MCP: building
more efficient agents"**, and neither appears in the eight.

**Q5 — `claude.md`** (25 hits)
1. Best practices for Claude Code — **17.83**
2. Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents — **17.83**
3. knowledge-work-plugins/design/skills (source)

**Verdict: pass by accident.** The tokenizer splits `claude.md` into `claude` + `md`, and `claude`
is dropped as noise, so this is a one-word search for "md". Right answers, tied again.

**Bonus:** `claude code permissions` -> **#3 is "Using Databricks for Data Analysis."** `how much
does claude code cost` -> **#3 is "Getting Started with Claude for Financial Services"**, in a
three-way 36.55 tie.

**Summary: 2 of 5 pass.** The ranker cannot separate *about X* from *mentions X*, and it has no
tie-break, so the top slots on common queries are arbitrary among equals.

---

## 9. On a phone (375x812)

Better than most. Layout reflows properly, 44 px minimum tap targets are enforced in CSS (`button,
.btn, .nav-link, .filter-option { min-height: var(--tap-min) }`), no horizontal scroll, the filter
rail collapses into a sticky "Filters" bar at the bottom that does not cover content.

Complaints:
- The self-cycling chip highlight is **worse** on touch. There is no hover on a phone, so a filled
  chip has exactly one meaning: selected. It is not.
- The hero illustration — 40 hand-drawn PNGs, ~869 KB total, the visible craft investment of the
  whole site — is pushed below the chips and the search field. On a phone I never saw it before
  answering.
- 520 KB over the wire for a browse page on mobile, of which 202 KB is a catalogue I will filter
  down to 7 items.

---

## 10. Keyboard walk

**What is right:**
- Skip link is the first stop.
- **Focus ring is a solid 2 px black rectangle** (`--focus-ring: 2px solid #141413`) applied via
  `:focus-visible` globally.
- Tab order matches visual order on every page I tried. Resource page is 14 stops, clean, no
  traps.
- The mobile filter sheet is a **correct** modal: `role="dialog" aria-modal="true"`, focus moves to
  Close on open, `body { overflow: hidden }`, **Escape closes it**, focus returns to the opener,
  and Tab is trapped by a handler that re-reads the stop list on every keypress rather than caching
  it. Most teams ship none of that.
- Hidden panels are `display: none !important`, so the four level buttons are genuinely out of the
  tab order when collapsed. Verified: `getClientRects().length === 0`, `.focus()` does not take.

**What is wrong:**
- **`#roleOptions` has no group role.** Ten `<button aria-pressed>` in a bare `<div
  class="chip-row">`. No `role="radiogroup"`, no `role="group"`, no `aria-labelledby` pointing at
  the "Who are you?" heading. A screen reader hears ten disconnected toggle buttons with no clue
  they are alternatives to one question. The browse page gets this right (`role="group"
  aria-label="Role"`), so the site knows how; the front door just does not do it.
- **The `data-showing` highlight is invisible to assistive tech.** The visual says "designer is
  selected"; `aria-pressed` says nothing is.
- 10 tab stops to answer question one, 14 to answer both. Arrow-key navigation within the group
  would make this two.
- `.card-title a:focus-visible { outline: none }` with the ring restored via `.card:has(...)`.
  Correct in a current browser; in anything without `:has()` the focus ring silently disappears on
  every result card.

---

## 11. How we check

**Less.** And this is the finding I would lead with.

The page opens:

> **"We would rather have 70 resources we can vouch for than 700 we cannot."**

Three paragraphs down, generated from the live data:

> **"Right now: 635 resources — 98 read by ai, 501 skimmed, 36 found only. Nothing is read in full
> yet, and the cards say so."**

635 resources. Zero a person has vouched for. The page states its principle and then prints, in its
own words, that it did the opposite. Meanwhile the home page says **"635 resources, checked by
hand."**

And "What we do" says: **"We find material, read it, and write two things..."** — not true for
**537 of 635 (85%)**.

The self-generated counts are the right instinct — they cannot rot. But wiring live numbers under a
hand-written headline means the page now automatically publishes its own contradiction and updates
it on every build.

Small tell in the same paragraph: **"98 read by ai"**, lowercase, because the generator lowercases
the whole label. Right there in the trust sentence.

Everything else on the page is good and I would credit it: "we do not take money to rank a
resource," "not affiliated with Anthropic," the note that the report link *"needs a GitHub account,
which is a real barrier and we know it,"* and the Claude-certification section explaining why
exam-prep spam is excluded.

---

## 12. Everything broken, ranked

### 1 — CRITICAL · The trust page contradicts itself, and the home page contradicts both
`/how-we-check.html`, `/index.html`. Home: **"635 resources, checked by hand."** How we check: **"We
would rather have 70 resources we can vouch for than 700 we cannot,"** then **"Right now: 635
resources — 98 read by ai, 501 skimmed, 36 found only. Nothing is read in full yet,"** then **"We
find material, read it..."** — untrue for 537 of 635 (85%).
**Harms:** every reader deciding whether to trust the judgments.

### 2 — CRITICAL · "Found only" cards ship content-level judgments about content nobody opened
`/resource.html?id=r-bcd03ac245`. Badge: **"Found only. We found it and sorted it. Nobody has
looked at the content yet."** Same page: a **"What it teaches"** list of three specific outcomes,
and **"Skip it if: Nothing in it visibly tells you to check Claude's arithmetic, which for a
project built on sales numbers is the omission that matters. Ninety guided minutes..."**
Reproducible across all 36 "Found only" items — every one has `summary`, `who_for`, `skip_if` and
`teaches` populated.
**Harms:** the badge system is the site's main trust device. If "Found only" still ships confident
inside-knowledge, no badge means anything, including "Skimmed."

### 3 — HIGH · Pick reasons state facts the site's own cards deny
> *"The deepest **non-Anthropic** material in the pool ... by the SDK's own engineer"* — card
> title: **"Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic"**
> *"the pool's **strongest non-Anthropic voice**"* — card author: **"Created by Anthropic, adapted
> for the DataCamp platform"** (used for both pm/never-used and data-analyst/never-used)

Cause is systematic: `official: false` (not on an Anthropic domain) is being read as "not from
Anthropic."
**Harms:** anyone weighing independence — the axis that matters most on a site where 58% of entries
are on Anthropic hosts.

### 4 — HIGH · The sitemap is half-empty and advertises 35 dead pages
`/sitemap.xml`. 353 resource URLs for a 635-item catalogue — **317 items missing (50%)**. **35 of
the 353 point at IDs no longer in `items.js`**, and the **first resource URL listed**
(`resource.html?id=r-af6ef6455e`) renders **"Not found — We could not find that resource"** at HTTP
200. Every `lastmod` says `2026-08-23`; content changed 2026-09-04/05. Only 3 of 7 paths are listed.
**Harms:** half the catalogue is invisible to search, and Google gets 35 soft-404s from the site's
own index.

### 5 — HIGH · Developer + "never used Claude" serves Blender artists and medical coders
`/browse.html?role=developer&level=never-used`. 7 results; the 4 non-pick cards are "Tokens",
**"Using the Blender Connector"**, **"Using the ICD-10 Connector"**, "What are skills?".
**Harms:** the exact visitor the site is designed to capture, on the first click after the front
door.

### 6 — HIGH · Search cannot separate "about X" from "mentions X", and has no tie-break
Five queries in section 8. `claude code hooks` -> top three all score **34.64**, real hooks tutorial
at #5. `claude code permissions` -> #3 **"Using Databricks for Data Analysis."** `reduce token
usage` -> 8 hits, #2 a Figma article.
**Harms:** everyone who takes up "Or describe what you want to do..."

### 7 — MEDIUM · The catalogue is padded with a scraped gallery
291/635 (46%) from `academy.claude.com`, incl. **148 `/use-cases/`**, **118 `/tutorials/`**, plus
**31 `support.claude.com`** Help Centre FAQs. **368/635 (58%) on Anthropic-owned hosts.**
**Harms:** every count on the site, and the credibility of "curated."

### 8 — MEDIUM · The level filter measures setup complexity, not experience
78 of the 148 fifteen-minute use-case recipes are `level: builder`. "Account tracking" (15 min,
needs Salesforce + Intercom connectors) is filed as "built things with it."
**Harms:** the front door's second question.

### 9 — MEDIUM · The card hides the publish date exactly when age decides
Card: **"Published over a year ago."** Resource page for the same item: **"Published 19 Dec 2024."**
**Harms:** anyone triaging a results list.

### 10 — MEDIUM · The time filter contradicts the cards it filters
5 items labelled "half a day" whose own text says 2 hours or less, incl. **"Complete Claude Code
Course In 2 Hours For Developers"**.

### 11 — MEDIUM · Weight
`browse.html` = **520 KB over the wire, 1.43 MB uncompressed**. `index.html` = **395 KB** before
illustrations. `data/items.js` is **765 KB raw / 202 KB gz** and loads on all four page types,
including the home page (one count) and how-we-check (a tally). 869 KB of role PNGs behind the
attract loop.

### 12 — MEDIUM · Nothing is server-rendered; all 635 resource pages share one title and description
`view-source:.../resource.html?id=anything` -> `<div id="content"></div>` and **`<title>Resource —
Learn Claude</title>`** with one generic `og:description`.
**Harms:** anyone who shares a resource link in Slack or a PR; plus search engines; plus anyone
with JS off.

### 13 — MEDIUM · The home page shows a selection that is not one
Verified over 8 samples: chip carries `data-showing` and a filled background, cycling every ~2.6 s,
while `aria-pressed="false"` on all ten.

### 14 — LOW · The developer path argues against its own step 5
Step 3 justified as *"it invalidates a lot of 2025-era advice."* Step 5 is **published 29 Sep
2025**. Also: all 6 steps are Anthropic, while the picks block praises a non-Anthropic course the
path omits.

### 15 — LOW · Generated-text artefacts in the copy that is asking for trust
**"98 read by ai"** (lowercase, in the trust sentence). **"about 81 minutes."** **"Claude pro
subscription."** Path header **"free"** over a step chip reading **"sign-up needed."**

### 16 — LOW · Home page role chips have no group semantics
Ten bare `<button aria-pressed>` in a `<div class="chip-row">`. The browse filters do it correctly;
the front door does not.

### 17 — LOW · Three of 40 role-by-level cells have no picks
`student|builder` (0 items -> dead end), `teacher|builder`, `writer-marketer|builder`.

### 18 — LOW · Anthropic's licensed brand fonts, self-hosted, on a site that disclaims affiliation
162 KB of `Tiempos Fine` (Klim) and `Styrene B` (Commercial Type) served from the repo, next to a
footer reading *"Learn Claude is an independent directory. It is not affiliated with Anthropic."*
Worth a licence check before this gets traffic.

### 19 — LOW · Engineering commentary shipped to production
`site.css` 41.7 KB and `home.js` 13.9 KB are substantially comments — including a note that a stale
figure in another comment *"said 176 of 353 and had been wrong for some time."* Nobody sees it; it
is still 60 KB of prose in the critical path.

### 20 — LOW · External links open in a new tab with no indication
`target="_blank" rel="noopener noreferrer"` is right; there is no visible or announced "opens in a
new tab." The "Copy link" button swaps its own text to confirm, with no live region.

---

## 13. The one thing that would make me leave

**"We would rather have 70 resources we can vouch for than 700 we cannot"** sitting above **"Right
now: 635 resources... Nothing is read in full yet."**

Not the empty cells, not the search, not the weight. Those are work-in-progress and I would forgive
all of them. But this site's entire pitch is *we exercised judgment so you do not have to*, and its
own trust page states the principle and then reports, in generated numbers it cannot fudge, that it
did the opposite at scale. The moment I read those two sentences together I stopped reading the
Skip-if lines as verdicts and started reading them as generated text — which meant the best thing
on the site stopped working for me.

Fixing the copy would be a lie. Fixing the number means cutting to 70, or getting a person through
a few hundred. Either is fine. Shipping 635 under a headline that says you would rather not is the
thing that lost me.

---

## 14. What is genuinely good

- **The Skip-if lines.** *"Skip if you do not know the OWASP Top 10. The video explains the Claude
  parts, not the vulnerabilities."* Nobody else writes these.
- **The path step reasons.** Six steps, six explanations of *why here* rather than *why at all*.
- **The pick reasons compare.** *"The decision layer the pool's twelve single-feature intros each
  lack."* That names the alternatives and what they failed to do.
- **The mobile filter sheet is a correct modal.** Focus moves in, Escape closes, focus returns to
  the opener, Tab is trapped by a handler that re-reads its stop list every keypress.
- **Publishing the tier mix at all.** "Nothing is read in full yet, and the cards say so" is a hard
  thing to print.
- **Counts are generated, never typed.** Every figure on the trust page reads from the live data.
  That is why I could catch the contradiction — and that is a feature.
- **Links are alive.** 45 of 46 sampled external URLs returned 200 (the 46th was GitHub rate-
  limiting me). No console errors on any page. No analytics, no account, no cookie banner.
- **The date logic is more careful than it needs to be** — age measured from the later of
  published/updated, month-only dates floored to the 1st so ambiguity always reads *older*.

---

## Checklist
- [x] I opened the live site at all four levels of my role — 7 / 20 / 45 / 64
- [x] I quoted at least 5 real titles or lines from the site — 30+
- [x] Every number I used is computed from the shipped data or measured over the wire
- [x] I looked at a phone width — 375x812, transfer sizes measured
- [x] I did one full keyboard walk — browse and resource, plus the modal
- [x] Five search queries in my own words, with scores, plus two bonus queries
- [x] I read the picks block and tested whether it is the top three rows — it is not
- [x] I found at least one thing nobody has mentioned before — the sitemap lists 353 of 635 and 35
      of those IDs no longer exist; and three pick reasons call Anthropic material non-Anthropic
      because `official: false` is being read as "not from Anthropic"
