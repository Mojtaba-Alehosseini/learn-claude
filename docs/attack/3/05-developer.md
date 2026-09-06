# Attack 3: a developer
Written as a developer, 2026-09-06. Site version: 9deb0db.

I ship code. I use Claude Code every day. I am past the tutorials. I want mechanism:
what a hook receives, what a turn costs, how to stop the agent touching things. I will
leave a site that gives me a listicle.

All counts below were read off the live site or come from `docs/STATUS.md`. Where I
measured something myself I say the URL and the method.

---

## 1. The first 60 seconds

The home page is one sentence with two blanks: **"I'm a [role] and I've [level]."** Under
it, ten role chips. Under that, a text box: "Or describe what you want to do..." and a
**Show me** button.

Under the fold, three promises:

- "We say when to skip — Every entry has a Skip if: line. A link with no judgment is just
  a list, and lists are what made this hard in the first place."
- "We say how we checked — Four levels, and we do not round up. If nobody has opened it,
  the card says so."
- "We show the date — Claude changes every few months. You can see when we last looked,
  and whether the thing is old."

That is a good pitch at me. It is a claim about method, not about enthusiasm. The strap
line under the chips is **"588 resources, each with a reason to skip it and the date we
last looked."** I checked that claim later and it holds numerically (section 10, F4).

Two seconds of doubt: no sign-up wall, no cookie banner, no newsletter modal. Good.

**What I watched while doing nothing.** I left the page alone for 10 seconds and took
frames at 3s, 6s and 10s. A different role chip lights up each time (I caught
"running a business", then "a student") and the hand-drawn picture on the right swaps
(easel, house, mug, book). But the sentence never fills in. I read the DOM: the two
blanks are `<span id="roleText">a [role]</span>` and `<span id="levelText">[level]</span>`,
and they still hold those literal strings after the loop has run.

So the demo highlights the answer and never shows the result. The one thing the loop
exists to teach — that this sentence becomes *"I'm a developer and I've built things with
it"* — is the one thing it does not do. Ten seconds of watching taught me nothing I did
not already see in the first frame.

## 2. Does the front door work for me (all four levels, with what I was shown)

I clicked **a developer** (128 resources match so far), then each level in turn, then
**Show me**. Counts are the live "N resources match so far" line and the Browse heading.

| I answered | site said | Browse gave me |
|---|---|---|
| a developer + never used Claude | 6 resources match so far | "6 resources. Remove a filter to see more." |
| a developer + used it a little | 20 resources match so far | 20 resources |
| a developer + used it a lot | 43 resources match so far | 43 resources |
| a developer + built things with it | 59 resources match so far | 59 resources |

The four add to 128, which is the count for `a developer` with no level. The front door
is fast, the counts are live before you commit, and the numbers on the button match the
numbers on the page. That part works.

**never used Claude (6).** Two of the six are not developer material at any level:

- *"Using the Blender Connector in Claude"* — Anthropic Academy, 15 min. "For: Blender
  users who want Claude to work with their live open scene."
- *"Tokens: why some inputs cost more than others"* — whose Skip line spends its whole
  length arguing about embeddings and RAG.

A developer who has never opened Claude, given six things, is handed a Blender add-on
tutorial. That is one sixth of everything the site has for that person.

**used it a little (20)** and **used it a lot (43)** are sensible: docs, best practices,
CLI material.

**built things with it (59)** is the one I care about, and it is section 3.

**The thin-cell handling is inconsistent.** At `developer|never-used` (6) I got the flat
line "6 resources. Remove a filter to see more." — no link, no number, no suggestion. At
`browse.html?role=teacher&level=builder` (2) the site does something much better:

> "Only 2 at "built things with it" for a teacher. The level below, "used it a lot", has
> 8. **Add "used it a lot" too**"

Named, numbered, one click. The machinery exists. It fires at 2 and not at 6, and the
fallback advice at 6 ("Remove a filter") is the wrong move — removing the level filter
gives me 128 and removing the role filter gives me the whole shelf.

## 3. What the catalogue actually gives me (are these really for me?)

Yes, mostly. `developer|builder` is genuinely advanced. This is not a course listing.
Reading down the 59 I find hooks, the Agent SDK, MCP internals, sandboxing, evals,
worktrees, headless CI, context engineering, orchestration. Real examples:

- *"Claude Code Headless Automation & Agent Workflows"* — "For: Developers and DevOps
  people who want Claude to run on a trigger, not on a person typing. Skip if: You have no
  CI system. Without a pipeline to put it in, headless mode has nowhere to go."
- *"Code execution with MCP: building more efficient agents"* — "For: Developers whose
  agent has become slow and expensive because it is wired to dozens of MCP servers."
- *"Claude Code Task System: ANTI-HYPE Agentic Coding (Advanced)"* — "Skip if: You have not
  used subagents yet. The video starts where most tutorials end and will not slow down for
  you."

Those three lines told me more in ten seconds than most directories tell me in ten
minutes. **This is the site's real product and it works.**

Two things spoil it.

**(a) The default order buries the reference material.** The default sort is "Best checked
first". I read all 59 in default order and recorded the badge and the `Checked` date on
each. The rule is: tier first, then most-recently-checked first. That produces this at the
bottom of the page:

| position | card |
|---|---|
| 48 | anthropics/claude-agent-sdk-python |
| 49 | anthropics/claude-code-action |
| 50 | anthropics/skills: example Agent Skills and the skill spec |
| 51 | Choose a sandbox environment for Claude Code |
| 53 | **Hooks reference (Claude Code)** |
| 54 | MCP Python SDK |
| 55 | MCP reference servers |
| 56 | Orchestrate teams of Claude Code sessions |
| 57 | Skill authoring best practices |

Every one of those is `Skimmed`, checked 21 Aug 2026. Every one of them is a primary
source I would keep open in a tab. They rank 48th to 57th of 59 because the site last
*looked at them* two weeks before it looked at a Traversy Media video (#32, checked
5 Sep 2026), which is one rank position per day of the curator's own admin calendar.
Nothing about the resources changed.

**(b) Four cards at `builder` are recipes, not building.** In the 59 I found three whose
`Skip if:` line opens "Needs …" and names other people's SaaS:

- *"Build an 'Ask the Company' agent"* — "Skip if: Needs Cowork with Confluence, GitHub
  and optionally Snowflake connected…"
- *"On-call handoff brief"* — "Skip if: Needs PagerDuty, Slack and GitHub connected plus
  the prior week's handoff file already saved…"
- *"Support incident postmortem"* — "Skip if: Needs Slack, Zendesk and GitHub connected
  plus an existing customer-postmortem template…"

Plus *"Build interactive diagram tools"*, which is a medical-anatomy reference app. Those
are prepared Cowork workflows you connect and run. Connecting Zendesk is not building.

## 4. Paths

There is one for me and it is good, with one flaw.

`paths.html` lists 7 paths (STATUS.md: "Learning paths | 7, 36 steps"). Mine is
**"Getting good at Claude Code" — "Developers who have installed Claude Code and are
getting mediocre results." For a developer. 6 steps · about 3 hours · free.**

What makes it worth reading is that every step says why it is *there* and *in that order*:

- Step 1 *Claude Code 101*: "Do this before reading anyone's tips, so you know which
  behaviours are the tool and which are the person writing about it."
- Step 4 *Maximizing the value of your Claude Code sessions*: "Now that your setup is
  right, this is where the speed comes from — knowing which commands quietly destroy your
  prompt cache mid-session."
- Step 6 *A harness for every task*: "Last, because orchestration is worth nothing until
  single sessions are reliable."

That is real editorial work and I have not seen it done this well elsewhere.

**But there is no path at my level.** The path is tagged "For a developer" with no level.
It starts at "Claude Code 101" (a course, marked `sign-up needed`) and "Best practices for
Claude Code". Steps 1–2 are for someone who installed Claude Code last week. I have to
work out for myself that my entry point is step 3. No step carries a level chip, and the
path list page gives no way to filter or enter partway. Every one of the 7 paths starts at
its beginning; there is no advanced route on this site.

**And the path contradicts the rest of the site about two specific documents.** Step 3 is
*"The new rules of context engineering for Claude 5 generation models"* (Published 24 Jul
2026), with the note: "Read this third and not later, because it invalidates a lot of
2025-era advice you will otherwise absorb."

Step 5 is *"Effective context engineering for AI agents"* (Published 29 Sep 2025). The
path's note on it says only: "Context engineering is the skill that separates people who
get good output from people who get plausible output."

Everywhere else, the site says that document is superseded:

- Its own Browse card and its own resource page: "**Read the July 2026 follow-up first if
  you are on Claude 5 generation models, because it reverses several recommendations
  here.**"
- The picks block reason on step 3's article: "The canonical context-engineering piece in
  this pool says in its own notes that this one reverses several of its recommendations on
  Claude 5 models - so the follow-up takes the slot the classic would otherwise hold."

So the picks block demotes the 2025 piece for being reversed, and the path serves it to me
two steps later with no warning at all. A reader following the path in order reads
reversed advice and is not told.

## 5. The card and the resource page

I opened three.

**`resource.html?id=r-42516bb950` — "Effective context engineering for AI agents".** This
is a good page. It has a one-paragraph summary written by the site, three "What it
teaches" bullets, "Who it's for", "Skip it if", "Before this" (two prerequisites), "Where
this fits" ("This is step 5 of 6 in Getting good at Claude Code"), and a "How we checked
this one" block that spells the tier out in visible text: "Skimmed. We read the outline or
a free sample. We have not seen the whole thing." Then "Checked 5 Sep 2026 · Published
29 Sep 2025 · Found through Anthropic". The outbound link is labelled **"Open on
Anthropic"** and points at the real URL. **Yes, I would click through.**

**`resource.html?id=r-d24581da69` — "Ralph: PRD skill plus autonomous implementation
loop"**, one of the three stripped `listed` cards. It carries a title, the source
("GitHub · snarktank, based on Geoffrey Huntley's Ralph pattern"), "Open on GitHub", and
one line: "**Skip it if: You want something we have read. We have not opened this one
yet.**" No summary, no For line.

**That reads honest, not broken.** It names the reader, states the condition and gives the
reason in nine words. I would still click the GitHub link, because I now know exactly what
the site's opinion is worth here: nothing, and it said so. That is the correct behaviour.

One wrinkle: the same card still asserts `code`, `half a day` and `free`. If nobody opened
it, "half a day" is a guess wearing the same chip as a measured one.

**`resource.html?id=r-d91d3354ec` — "Mastering Claude Cowork & AI Agents in 5 hours"
(Udemy).** This one I do not trust, and section 10 F2 explains why.

## 6. Search, in my words

Typed into the Browse search box at `browse.html` with no filters set. I confirmed the
box behaves identically whether I type into it or set the value programmatically (same
count, same top 3 for query 2).

| # | what I typed | top 3 I was shown | verdict | why |
|---|---|---|---|---|
| 1 | how do I stop claude code from running git push without asking | 1. Claude Code settings and permission rules · 2. Agent-native Product Management (Every's guide) · 3. Git Worktrees Explained — Run Multiple AI Agents in Parallel (Claude Code Tutorial) | ok | #1 is exactly right and it is first. #2 and #3 are noise — #3 matched on the word "git". 32 results for a question this specific is too many, but I only read the top. |
| 2 | what does a hook actually receive and can it block a tool call | 1. Hooks reference (Claude Code) · 2. Hooks in Claude Code — Full Theory + Practical Use \| CampusX · 3. Anthropic courses: API fundamentals, prompting, evals and tool use | ok | Best result on the site, and the only one of my five where all of the top two are right. The reference page is precisely where the event payloads and exit codes live. |
| 3 | how much does a long claude code session cost in tokens | 1. How context affects Claude's performance and cost · 2. A Guide to Claude Code 2.0 and getting better at using coding agents · 3. Claude Code Essentials (ExamPro full course) | ok | #1 answers it. But the site holds a card whose own path note is "knowing which commands quietly destroy your prompt cache mid-session" — *Maximizing the value of your Claude Code sessions* — and it is not in the top three. The best answer lost to a more general one. |
| 4 | should I use the agent sdk or just call the messages api myself | 1. You Can Build The Craziest Things with Claudes Agent SDK · 2. Building agents with the Claude Agent SDK · 3. Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic | ok | Right answer, wrong rank. #2's own For line is "Developers deciding whether to build an agent on the Agent SDK rather than wiring their own tool loop over the Messages API" — that is my question restated. It lost to a YouTube video whose own Skip line says "this one stops before the hard parts". The site's own text knows the answer and the ranker ignored it. |
| 5 | how do I run claude code in CI without a human approving each step | 1. Claude Code in Action · 2. Claude Code Headless Automation & Agent Workflows · 3. Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship | ok | #2 is the answer ("For: Developers and DevOps people who want Claude to run on a trigger, not on a person typing"). #1 is a generic overview. 78 of 588 returned; positions 70–78 include "Claude Code for Beginners Tutorial [Full Course]" and "Claude, Claude Projects and Claude Code for Non-Coders". |

**The same question asked two ways.** I asked query 1 again in words that share nothing
with it: **"deny list for shell commands the agent is allowed to run"**. Top result:
**"Claude Code settings and permission rules"** — the same #1 as
*"how do I stop claude code from running git push without asking"*. **The site agreed
with itself.**

For my own information I tried a third wording of the same intent, **"block a dangerous
command before the agent executes it"**, and the permission-rules card fell out of the top
three entirely (1. What is Claude Code? 2. Hooks reference 3. Agent SDK overview). So the
agreement holds across the two wordings I was asked to test, and it is thinner than that
result alone suggests.

Overall: 5 of 5 `ok`. Search is the strongest engineering on this site. Recall is good and
a plain English sentence lands. **Ranking is the weak half** — in 2 of 5 the exactly-right
card sat at #2 behind something the site's own copy grades lower.

## 7. On a phone

I set my tab to 375×812 and walked the same route.

Good, and better than I expected:

- No horizontal overflow anywhere. `document.documentElement.scrollWidth` equals
  `innerWidth` (375) on both the home page and Browse.
- Every tap target on the home page measures 44px tall — the ten role chips, the four
  level chips, the three nav links. "Show me" is 139×52.
- On Browse the desktop filter rail is hidden (`display: none` at 767px, `block` at 800px)
  and replaced by a pinned **Filters** button at the bottom of the viewport. Tapping it
  opens a full-screen sheet with **all eight groups** — Role, Level, Time, Topic, Format,
  Cost, How well checked, Source — and a "Show 59 resources" button at the foot.
- The mobile sheet actually shows *more* than the desktop rail does by default: on desktop
  Topic, Format, Cost, "How well checked" and Source are hidden behind a **"More
  filters +"** toggle that ships collapsed (`aria-expanded="false"`).

Cards reflow to one column and stay readable. I have no mobile complaint. This is the part
of the site that has clearly been tested.

## 8. What changed since Attack 2 — my verdict on each

**`builder` now means you built something.** Mostly true, and it was worth doing. 59 cards
at `developer|builder`, and the top of the list is hooks, the Agent SDK, MCP internals and
evals — genuinely advanced, not a course listing. **But four cards are still recipes**:
"Build an 'Ask the Company' agent", "On-call handoff brief", "Support incident postmortem"
(all three Skip lines open "Needs … connected") and "Build interactive diagram tools".
Connecting PagerDuty and running a prepared prompt is not building. **Verdict: 55 of 59
right.**

**Every role tag now has to be true of the card.** Works on the two tests I could run. The
five collection cards (Use cases for Sales / Legal / HR / Finance / Operations) are
**correctly absent** from all 128 developer cards — I checked, zero of them appear. I did
not trip over them once. **Verdict: works.**

**Five collection cards.** Not aimed at me, but I read them. Each says plainly what it is:
"This is a menu, not a lesson: every recipe needs Cowork with Salesforce or HubSpot
connected, and none of them teaches you anything about Claude itself." That last clause is
the honest bit. **Verdict: clear.**

**Search was rebuilt.** Section 6. 5 of 5 useful, ranking off in 2 of 5. **Verdict: good
recall, mediocre ranking.**

**Cards that were stripped.** Honest, not broken. Section 5. The chips (`half a day`,
`free`) are the one thing that undercuts the honesty. **Verdict: honest.**

**How well checked, as a filter — can I find out what my badge means without a mouse?**
Partly, and not on the page where it matters. On a Browse card the badge is
`<span class="badge badge-ai-reviewed" title="AI read all of it. No person has checked the
notes yet.">Read by AI</span>`. Its `tabIndex` is `-1`, so I cannot focus it, and a `title`
attribute only appears on mouse hover. The card's link carries
`aria-describedby="tierdesc-ai-reviewed"` pointing at a `visually-hidden` bank at the foot
of `<body>`, so a screen reader is told. A **sighted keyboard user gets nothing on the
card** and has to leave for `how-we-check.html`. On a *resource* page the definition is in
plain visible text. **Verdict: solved for screen readers, unsolved for keyboard, solved
one click away.**

**The thin-level offer.** Read it at `teacher|builder` and it is good — see section 2. It
does not fire at my thin cell (6). **Verdict: right idea, wrong threshold.**

**Date lines.** Maintained, not abandoned, and clearly so. All 59 `Checked` dates in my
cell fall between 20 Aug 2026 and 6 Sep 2026 — nothing older than 17 days. 3 of the 59
carry "· over a year ago, may not match Claude today" beside the publish date. 32 of 59
(54%) say "No publish date given", which is high, but on a site that also says
"UNVERIFIED" out loud I read it as candour rather than neglect. **Verdict: maintained.**
The one place the dates hurt is the sort control (F3) and the `Checked` claim on blocked
hosts (F2).

**Prices.** No. I read the cost chip off all 588 cards: 536 `free`, 26 `sign-up needed`,
16 `subscription`, 10 `pay once` — which matches STATUS.md exactly. So **26 rows cost
money and exactly 4 carry a price**: "from $49", "from $995", "from $2,999", "from
$3,000". **Verdict: for 22 paid rows I still do not know what I would pay before I
click.**

**Who "we" is.** **Raises my trust, and it is the single most persuasive thing on the
site.** `how-we-check.html` says: "One person makes this site - a researcher at the
Technical University of Denmark, working on it outside their job… The reading is done by
Claude, at the level each card's label claims and no further… A person sets the rules,
decides what the labels are allowed to say, and reads the arguments - **and has not yet
read a single resource end to end**, which is why the strongest label has the count you
can see above it."

I have never seen a directory disclose its own provenance that precisely. It converts
"Read by AI" from a badge into a fact I can discount correctly. A directory that judges
other people's work and hides who is judging is worth nothing; this one told me before I
asked. **Verdict: raises it, a lot.**

**The picks block.** `developer|builder` ships three with reasons, and the reasons are
arguments rather than blurbs — the Cookbooks pick says "The only candidate you run rather
than read - a defensible starting point per capability instead of a blank file, which is
worth more to a builder than another explanation." **Yes, I would open all three.**
**Verdict: works.**

**The social preview title.** Broken. F1 below.

**The home attract loop.** Broken. Section 1.

**The sort control.** Broken. F3 below.

**Paths above beginner level.** None exist. Section 4.

## 9. Content quality — the three worst entries I was shown, quoted

**1. "Tokens: why some inputs cost more than others"** — Anthropic Academy, docs, 15 min.
Shown to me at `browse.html?role=developer&level=never-used`, one of only 6.

> Skip if: Framed entirely around cost and rate limits, not embeddings for semantic search
> or RAG - it teaches byte-pair encoding for pricing intuition, despite the URL slug's
> mention of embeddings.

Read that after the words "Skip if:". It is not a condition, it is a footnote about a URL
slug. A developer who has never used Claude does not know what RAG is and is not choosing
between this and an embeddings tutorial. The line answers a question nobody asked, in the
cell with the fewest options on the whole site.

**2. "Build interactive diagram tools"** — Anthropic Academy, docs, 15 min. Shown to me at
`developer|builder`.

> For: Someone building a reference app from an existing structured data/SVG source.
>
> Skip if: Filed under 'Personal' despite being a medical-education reference app - and
> its own tip says to spot-check the anatomy content against a real textbook before
> studying from it, since it isn't a verified medical source.

An anatomy-app Cowork recipe, in the pool for developers who build things. The For line is
so generic it could describe anything; the Skip line is a warning about medical accuracy,
which tells me the site knows this is a medical page and filed it under developers anyway.

**3. "Using the Blender Connector in Claude"** — Anthropic Academy, docs, 15 min. Shown to
me at `developer|never-used`, one of 6.

> For: Blender users who want Claude to work with their live open scene.
>
> Skip if: Blender and Claude must be running on the same machine - it works through a
> local add-on, not the browser, so claude.ai in a browser tab will not reach it at all.

The For line names Blender users, not developers. The Skip line, again, describes the
resource rather than the reader. A developer opening Claude for the first time gets this
as 1 of 6 things the site has for them.

All three share the same defect and it is the site's own headline promise. See F4.

## 10. Everything that is broken, ranked (evidence for each)

Ranked by what it costs a reader, not by effort to fix.

---

**F1 — Every shared link previews as "Resource — Learn Claude". (worst)**

- **URL:** `https://mojtaba-alehosseini.github.io/learn-claude/resource.html?id=r-42516bb950`
- **What I did:** read the page's meta tags, the way Slack, Teams, iMessage and every
  other unfurler does.
- **What I saw:** `<title>` is correct — "Effective context engineering for AI agents —
  Learn Claude". But `og:title` is the literal string **"Resource — Learn Claude"** and
  `og:description` is **"What this resource teaches, who it is for, who should skip it,
  and how thoroughly we checked it."** Both are hard-coded. Browse is the same:
  `browse.html?role=developer&level=builder` has `<title>` "Browse 59 Claude resources"
  but `og:title` **"Browse — Learn Claude"** and `og:description` "Filter every checked
  Claude resource by role, level, time, topic, format and cost."
- **Expected:** the resource's own title and its Skip line, so the preview says what I am
  sending.
- **Who it harms:** everyone, and worst the people the site most needs. Sharing is how a
  directory like this spreads. I paste a card into a team channel to make a point about
  context engineering; my colleagues see a grey box saying "Resource — Learn Claude" and
  scroll past. All 588 resource pages preview identically, and so does every filtered
  Browse link. The site's whole value is one specific judgment about one specific thing,
  and the shareable unit of that judgment is anonymous.

---

**F2 — "Checked 5 Sep 2026" on hosts the site itself cannot check.**

- **URL:** `https://mojtaba-alehosseini.github.io/learn-claude/resource.html?id=r-d91d3354ec`
  ("Mastering Claude Cowork & AI Agents in 5 hours", Udemy)
- **What I did:** read the footer line on the resource page, then read the site's own
  generated `docs/STATUS.md`.
- **What I saw:** the page says **"Checked 5 Sep 2026 · No publish date given · Found
  through Udemy"**, tier `Skimmed`, with a full summary, three "What it teaches" bullets,
  a "Who it's for" and a "Skip it if". STATUS.md lists this exact course under **"Pages no
  machine can read (9)"** and lists `udemy.com` under "Hosts that block the weekly check"
  with **4 items, last confirmed by a person: never**. Nothing on the page says any of
  this. `how-we-check.html` never mentions blocked hosts either, and it states "We do not
  list something whose page we cannot open."
- **Expected:** if a host refuses the check, the card should say so where the date is,
  not leave a fresh date standing.
- **Who it harms:** anyone deciding whether to pay. The date is the site's third headline
  promise ("We show the date… You can see when we last looked"). Here it shows a date for
  a look that could not happen. 21 of 588 rows sit on hosts in this state (STATUS.md link
  table) and a visitor cannot tell which.

---

**F3 — "Newest first" is not newest first, and buries half the pool without saying so.**

- **URL:** `browse.html?role=developer&level=builder&sort=newest`
- **What I did:** set the sort control to "Newest first" and recorded the date line of
  every card in order.
- **What I saw:** the sort uses `published` and ignores `updated`, while the card shows
  both.
  - Position 4: "I Built an Agentic Software Factory with Codex and Claude Code · Published
    25 Jul 2026"
  - Position 8: "A harness for every task: dynamic workflows in Claude Code · Published
    2 Jun 2026 · **Updated 20 Aug 2026**"
  - Position 21: "Code execution with MCP · Published 4 Nov 2025" (no update)
  - Position 23: "Building agents with the Claude Agent SDK · Published 29 Sep 2025 ·
    **Updated 6 Jul 2026**"

  A document last touched 20 Aug 2026 ranks below one last touched 25 Jul 2026. A document
  updated 6 Jul 2026 ranks below one untouched since 4 Nov 2025. Separately, **32 of the
  59 cards (54%) say "No publish date given"** and all 32 are dumped at the end of the
  list with no heading and no explanation.
- **Expected:** "Newest" to mean the most recent date the card shows me, and a divider
  where the dated items end.
- **Who it harms:** anyone using the control for its only purpose — finding what still
  matches today's Claude. On a subject that turns over every few months, this control
  hands me an answer that is wrong by a year and does it silently.

---

**F4 — 71 `Skip if:` lines are requirements, not skip conditions, and 119 never mention
the reader.**

- **URL:** `https://mojtaba-alehosseini.github.io/learn-claude/browse.html` (unfiltered,
  all 588 cards rendered)
- **What I did:** pulled the `Skip if:` line off all 588 cards and counted two patterns —
  lines that begin "Needs", and lines that contain no "you"/"your" and do not begin with
  the word "Skip".
- **What I saw:** all 588 cards do have a Skip line, so the promise is numerically kept.
  But **71 of 588 begin with "Needs …"** and **119 of 588 (20%) never mention the reader
  at all.** Read as written:
  - "Skip if: **Needs** the PubMed connector connected, so it only reaches PubMed's
    biomedical literature…"
  - "Skip if: **Needs** PagerDuty, Slack and GitHub connected plus the prior week's
    handoff file already saved…"
  - "Skip if: **Framed entirely around cost and rate limits**, not embeddings…"
  - "Skip if: **Zero written content** - config options and multi-file directory layout
    exist only inside the 4-minute video…"
  - "Skip if: **Video only**, with no transcript or written comparison to skim…"

  "Skip if: Needs Slack" means, literally, *skip this because it needs Slack*. The intent
  is the opposite: skip it if **you do not have** Slack. A reader scanning at speed reads
  the inverse of the truth.
- **Expected:** every line to complete the sentence "Skip if **you** …", which is what the
  home page sells: "Every entry has a Skip if: line. A link with no judgment is just a
  list."
- **Who it harms:** everyone, in the one place the site claims to be different. A caveat
  is not a judgment. One in five of these lines is a caveat wearing a judgment's label,
  and 71 of them invert.

---

**F5 — "Best checked first" ranks by the curator's calendar, and it is the default.**

- **URL:** `browse.html?role=developer&level=builder` (no sort parameter)
- **What I did:** recorded badge, `Checked` date and position for all 59 cards in the
  default order.
- **What I saw:** the order is tier, then `Checked` date descending. Inside the `Skimmed`
  tier every card checked 5 Sep 2026 outranks every card checked 21 Aug 2026. Result:
  "Hooks reference (Claude Code)" is **53rd of 59**; "Skill authoring best practices" is
  57th; "MCP reference servers" 55th; "anthropics/skills: example Agent Skills and the
  skill spec" 50th; "Choose a sandbox environment for Claude Code" 51st. Above all of them
  at #32 sits a Traversy Media video whose own Skip line reads "You already decided to use
  the SDK… this one stops before the hard parts."
- **Expected:** "Best" to be about the resource. The label gives no hint that "checked"
  means "when we last looked".
- **Who it harms:** a builder specifically. The reference docs and source repos are the
  things I actually want, and the default view puts every one of them in the last fifth
  of a 59-card page for a reason that has nothing to do with them.

---

**F6 — On a Browse card, the tier badge is mouse-only for a sighted keyboard user.**

- **URL:** `browse.html?role=developer&level=builder`
- **What I did:** inspected the badge element and its tab order.
- **What I saw:** `<span class="badge badge-ai-reviewed" title="AI read all of it. No
  person has checked the notes yet.">Read by AI</span>`, `tabIndex` `-1`, no href. The
  definition reaches a screen reader through `aria-describedby="tierdesc-ai-reviewed"` on
  the card's link, pointing into a `visually-hidden` bank. A `title` shows on hover only.
- **Expected:** the badge to be focusable, or to carry a visible definition, or to link to
  `how-we-check.html`.
- **Who it harms:** keyboard users and anyone on a touch screen, where hover does not
  exist. The badge is the site's main quality signal and on the busiest page it is the one
  thing you cannot interrogate without a pointer. Mitigated: the resource page states it
  in plain text, and "How we check" is in the nav.

---

**F7 — The path serves advice the site knows is reversed.** Section 4. A developer
following "Getting good at Claude Code" in order hits, at step 5, a document that the same
site flags twice elsewhere as superseded by step 3. The path's own note on step 5 does not
mention it. Harm: I follow a 3-hour path precisely because I trust the ordering, and the
ordering hands me stale advice with no flag.

**F8 — The attract loop never completes its own sentence.** Section 1. `#roleText` stays
"a [role]" and `#levelText` stays "[level]" while chips light up behind them. Harm: small
— ten seconds of a visitor's attention spent on a demonstration that demonstrates nothing.

**F9 — The thin-level offer does not fire at 6.** Section 2. `developer|never-used` gets
"Remove a filter to see more" instead of the "The level below has N. Add it too" line the
site already builds for `teacher|builder`. Harm: small, and it lands on the newest
visitor.

**F10 — 22 paid rows carry no number.** Section 8. Counting cost chips across all 588
cards: 16 `subscription` + 10 `pay once` = 26 rows cost money, and exactly 4 of them show
a figure. Harm: small for me (my pools are almost all free), real for anyone else.

## 11. The one thing that would make me leave and not come back

Not one of the ten above, on its own. The thing that would lose me is **F4 plus F5
together**, because between them they undo the two reasons I stayed.

I came for the Skip line. One in five Skip lines is not a skip line — it is a note about
the resource, and 71 of them are requirements written as if they were conditions, which
means they read backwards. Once I catch that twice, I stop trusting the line, and once I
stop trusting the line this is a list of links with dates on it.

Then I look at the default order and find the Hooks reference at 53 of 59, below a video
the site itself calls shallow, because somebody re-checked the video more recently. Now
the ranking is not about me either.

A directory earns its existence by having an opinion. If the opinion line is unreliable
and the order is administrative, there is nothing left that I could not get from a search
engine in less time.

## 12. What is genuinely good (honest, brief)

- **The Skip line when it is a real skip line**, which is most of the time. "Skip if: You
  have not used subagents yet. The video starts where most tutorials end and will not slow
  down for you." That is worth more than a star rating.
- **`how-we-check.html`'s "Who we is" section.** One person, at DTU, outside their job,
  with Claude doing the reading, and a person who "has not yet read a single resource end
  to end". Publishing that raises my trust more than any badge could.
- **The path step reasons.** Not "read this next" but *why this, in this position*. Step 6:
  "Last, because orchestration is worth nothing until single sessions are reliable."
- **Search recall.** Five plain English sentences, five useful answers in the top three,
  and the same #1 for two completely different wordings of the same intent.
- **The picks reasons.** Arguments, not blurbs, and one of them openly demotes a famous
  article for being superseded.
- **The mobile filter sheet.** All eight groups, one tap, "Show 59 resources" at the foot.
  Better than the desktop rail, which hides five groups behind a collapsed toggle.
- **The stripped `listed` cards.** Nine words that tell me the site's opinion is worth
  nothing here. More directories should do this.
- **No accounts, no tracking, no modal, no newsletter.** I noticed, and it is why I stayed
  past the first screen.

## 13. Would I come back, and what one thing would make me?

Yes — but not to the home page. I would bookmark
`browse.html?role=developer&level=builder` and come back to that, maybe once a month, to
see what is new. I would not share it with my team yet, and that is the whole problem:
I paste links into Slack all day, and every one of these previews as "Resource — Learn
Claude". A directory that cannot be shared cannot grow, and a directory that cannot grow
dies.

The one thing: **make the Skip line always finish the sentence "Skip if you…".** Not
"Skip if: Needs PagerDuty connected" — "Skip if you do not have PagerDuty connected."
Seventy-one lines currently read backwards. That line is the only reason this site exists
instead of a bookmark folder, and right now one in five of them is a footnote in a
judgment's clothing. Fix that and I will trust the other 469 enough to send them to
someone else.

Second on my list, and much cheaper: put the resource's own title in `og:title`.

## Checklist
- [x] I opened the live site
- [x] I tried all four levels
- [x] I quoted at least 5 real titles or lines from the site
- [x] Every number I used is in 00-facts.md, STATUS.md, or quoted from the site
- [x] I looked at a phone width
- [x] I read no file under scripts/ or data/
- [x] I found at least one thing nobody has mentioned before
