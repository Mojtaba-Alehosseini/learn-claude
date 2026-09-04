# Attack 2: a writer
Written as a working writer and marketer, 2026-09-05, one hour. Live site only:
`https://mojtaba-alehosseini.github.io/learn-claude/`.

---

## 1. First 60 seconds

Landing page. Serif headline, a hand-drawn mug, and a sentence with two holes in it:

> **I'm a [role] and I've [level].**

I like the idea. On desktop it reads as an invitation. On a phone it is the first thing above the
fold at enormous size and it reads as a template that failed to render — square brackets are what
broken CMS output looks like.

Under it: **"635 resources, checked by hand."**

That line is the reason I kept reading, and it is the line the rest of the site spends an hour
disproving.

Three promises follow, and the middle one is the pitch:

> **We say when to skip** — "Every entry has a Skip if: line. A link with no judgment is just a
> list, and lists are what made this hard in the first place."

Correct. That is the whole product. It is also the thing most visibly broken.

Verdict at 60 seconds: I would stay. The voice is confident and the premise is right. Nobody else
does "who should skip this."

---

## 2. The front door, all four levels

I picked **a writer** and ran all four. Counts are the site's own, on
`browse.html?role=writer-marketer&level=<level>`:

| I've... | Resources | Picks block | Tier ceiling |
|---|---|---|---|
| never used Claude | **19** | 3 picks, "picked by AI · 4 Sep 2026" | Skimmed (0 read) |
| used it a little | **36** | 3 picks, "picked by AI · 5 Sep 2026" | 11 Read by AI |
| used it a lot | **8** | 3 picks, "picked by AI · 31 Aug 2026" | 2 Read by AI |
| **built things with it** | **3** | **none** | **all three Skimmed** |

The fourth row is where the site falls over, and it is my row.

`browse.html?role=writer-marketer&level=builder` returns:

> **3 resources. Remove a filter to see more.**

Three. No "Start with these three." No path. Nothing at "Read by AI", nothing at "Read in full."
The three are:

1. **How I Use Claude Cowork to Write With AI in My Voice** — a personal blog on a domain called
   `ranthebuilder.cloud`
2. **avoid-ai-writing (Claude Code / agent skill)** — a GitHub repo
3. **Claude Skills for Journalism, Media & Academia** — another GitHub repo

Two of the three say **"No publish date given."** All three say **"Skimmed."** Nobody read any of
them.

I checked `data/picks.js` directly: 37 of the 40 role-by-level cells have a picks block. The three
missing are `student|builder`, `teacher|builder` and **`writer-marketer|builder`**. So the site did
the editorial work for 37 audiences and skipped mine.

**The harm:** the site asks me a question, I answer it honestly at the top of the ladder, and it
punishes me for it. The level filter is exact match, not "this and below" — I verified it in
`browse.js` (`a.key === "levels" ? [it.level]`). Answering "built things with it" *hides* the 63
other writer resources rather than ranking them. The honest answer is the worst answer. "Remove a
filter to see more" is the site admitting it, and it is the only place the site tells me its own
interface is working against me.

---

## 3. What the catalogue gives me

The card format is: badge, title, publisher, chips, **For:**, **Skip if:**, dates. Good bones.

The prose inside is two different writers stapled together.

**The good.** When it lands, it lands. These are real editorial sentences:

> **Skip if:** "The free tier stops at five Projects, and the larger knowledge base that makes one
> useful for a whole topic only arrives on a paid plan — if you are planning around Projects, plan
> around that first."

> **Skip if:** "It costs $995 and that is not the whole price: it also expects a Claude Pro or Team
> subscription... Its own page cannot decide whether you need Python or R — one section says no
> programming experience is needed and another says a working knowledge of a statistical language —
> so assume the stricter one."

> **Skip if:** "The plan limits in this article have moved more than once — how many Projects you
> get on free versus paid has changed between versions of the page — so take the number from the app
> rather than from here."

That third one is genuinely useful and I have not seen it anywhere else.

**The filler.** 161 of 635 cards (25%) repeat the label they sit under. The card prints "Skip if:"
and then the sentence starts "Skip if". On one screen of results I counted **thirteen consecutive
cards** opening this way:

> Skip if: **Skip it if** you need current implementation detail...
> Skip if: **Skip if** a single well-shaped prompt already solves your problem...
> Skip if: **Skip it if** you need current interface detail...
> Skip if: **Skip if** you need Zero Data Retention or a HIPAA BAA... **Skip also if** you want full
> control...
> Skip if: **Skip if** you only make single-turn API calls...
> Skip if: **Skip if** you connect two or three MCP servers...
> Skip if: **Skip if** you only consume other people's tools and never write your own.
> Skip if: **Skip if** you do not know the OWASP Top 10...

Meanwhile 104 other cards get it right and just say "You...". Two incompatible conventions, side by
side, in the same list. Any copy editor kills this in ten minutes with find-and-replace. Nobody
has.

**The label is a lie on some cards.** "Skip if:" is being used as a general caveat bin:

> **Skip if: Nothing** — worth reading before your first real Cowork task regardless of experience
> level.

A "Skip if" that says do not skip. And:

> **Skip if:** "Two rules here catch people out at other publishers too: a reviewer may not put a
> manuscript through a public AI tool at all, and the reference list has to be excluded from any AI
> editing."

That is a **reason to read it**, printed under a heading that means the opposite. Same on the
Elsevier card. The site's single differentiating feature is being used to store text that
contradicts its own label.

**House style.** Across all reader-facing prose I counted **766 spaced hyphens (` - `) against 91 em
dashes**. Both appear on the same screen. Spelling is split too: `organisation` 8 / `organization`
10, `behaviour` 7 / `behavior` 8, `licence` 3 / `license` 3. A directory whose product is editorial
judgment has no house style.

---

## 4. Paths

This is the best thing on the site and it is also where the seam shows.

Live, on `paths.html`, in a column with six siblings:

> Your first week with Claude — 6 steps · **about 4 hours** · free
> Getting good at Claude Code — 6 steps · **about 3 hours** · free
> **Using Claude on work you put your name to — 4 steps · about 81 minutes · free**
> Product work without waiting for engineering — 5 steps · **about 2 hours** · free

**"About 81 minutes."** No human wrote that. "About" and "81" cannot share a sentence. Every sibling
rounds to hours; mine prints a raw sum. I checked the sibling at 93 minutes — it prints "about 2
hours". So the threshold is somewhere in the 80s and my path fell under it. The build script is
speaking in its own voice on a page about craft.

**The four steps and their reasons:**

> **1. Claude, Editor** — "First, decide what job it has. This is a writer using Claude as an editor
> rather than a ghostwriter, and settling that question now is what makes every later step a craft
> problem instead of an ethics problem."
> **2. Wikipedia:Signs of AI writing** — "Second, learn the symptoms before trying to treat them...
> you cannot prompt your way out of a tell you cannot name."
> **3. How to Stop Claude Writing Like an AI** — "Only now is this useful. It is the treatment for
> the symptoms in step 2 — read in the other order it is a list of fixes for problems you have not
> learned to see yet."
> **4. The Ethics of Using AI** — "Last, and last on purpose: everything above makes the work harder
> to detect, which is exactly why disclosure has to be the step you finish on. Craft is what you owe
> the page. This is what you owe the reader."

Step 4 is the best sentence on this website. "Craft is what you owe the page. This is what you owe
the reader." Step 1's "a craft problem instead of an ethics problem" is doing real work too.

**Does the sequence read as if something is missing?** Yes, and the tell is the ordinal ladder.
Every other path on the site numbers its reasons in words: *Second... Third... Fourth... Last*. Mine
goes **First -> Second -> [no ordinal] -> Last**. Step 3 opens "Only now is this useful" and step 4
opens "Last". There is a hole where "Third" should be, and step 3 has been rewritten to bridge it. It
reads like a five-step path with the middle removed and the joint sanded over. It still *works* — step
3 genuinely earns its position by pointing back at step 2 — but the rhythm is broken and I can hear
it.

Second problem: **the path is filed at level "basic."** I answered "built things with it." So the one
path written for my exact job is not offered to me. A writer at builder level gets three GitHub repos
and no route through them.

Third: on the index, sibling titles truncate mid-word — "The new rules of context engineering for
Cla...", "Claude Code for Data Analysis: Excel-Free An...". Fixed character count, no word boundary.

---

## 5. The card and the resource page

I opened three. Two yes, one no.

**Yes: "Claude Code overview and install guide."** The summary paragraph is good:

> "It gives the exact install command for every surface — terminal on macOS, Linux, Windows
> PowerShell and CMD, Homebrew, WinGet, VS Code, JetBrains, desktop app and browser..."

Correct capitalisation. Correct commas. Then, **three centimetres below it on the same page**, under
"What it teaches":

> — Install Claude **code** across **macos linux and windows** environments
> — Configure Claude **code** in **vs code** and JetBrains editors
> — Run initial Claude **code** commands for **tests bug fixes and git** workflows
> — Navigate to Claude **code** docs for **ci** scheduling and integrations

The same page spells "macOS, Linux, Windows" correctly in one paragraph and "macos linux and
windows" in the next. It capitalises "JetBrains" and leaves "vs code" lowercase **in the same line**.
And it cannot spell **Claude Code** — the product this entire website exists to teach — in four
consecutive bullets.

This is not an accident, it is architecture. The shipped `ui.js` carries a hardcoded list of ~36
proper nouns to re-capitalise, with a comment saying "all 970 of its bullets came out of a model in
lower case." Anything off the list stays lowercase forever. So across the catalogue you get "query
**tableau** datasources in plain **english**", "run the setup-bedrock wizard to connect Claude code
to **aws**", "install and configure **postgres** MCP **pro**", "use the Claude add-in directly within
**microsoft** Excel".

Of 1,365 "What it teaches" bullets, **113 contain a comma.** The other 1,252 are unpunctuated strings
of nouns. "for tests bug fixes and git workflows." That is not writing. That is a model's first
draft, shipped.

**No: "Disclosing the Use of AI" (Princeton).** See section 7 — the badge and the prose contradict
each other so completely that I stopped trusting the page.

Resource-page layout is otherwise clean. On the Claude Code page the heading "Skip it if" is
immediately followed by the sentence "Skip it if Claude Code is already installed and working." The
label, twice, two lines apart.

---

## 6. The picks block

Format: **"Start with these three"** (or "Start with these two"), a small grey **"picked by AI · 5
Sep 2026"**, then three cards each with one sentence under it.

**Is it real judgment or the first three rows?** Real judgment. This is the strongest editorial work
on the site and it is not the top of the list — I checked the pick URLs against the sort order and
they are pulled from across the pool. My three at "used it a little":

> **Claude, Editor** — "The pool's one candidate about the decision that shapes every later one —
> editor or ghostwriter — and step 1 of the writing path for exactly that reason."
> **Wikipedia:Signs of AI writing** — "The only candidate written by the people trained to catch AI
> writing rather than produce it — you cannot prompt your way out of a tell you cannot name, and this
> is the catalogue of names."
> **Claude Cowork: The Ultimate AI Agent for Writers** — "The one candidate about scale —
> consistency of voice and plot across many files — which is the problem chat-window writing advice
> cannot touch."

"The catalogue of names" is a good phrase. Each sentence names a discriminator instead of praising.
That is the right instinct.

**But as writing, it is a formula.** I pulled all 109 pick sentences on the site:

- **66** contain the word "candidate"
- **48** contain "the only"
- **39** contain "only candidate"
- **35** refer to "the pool"
- **28** begin with the exact words "The only"
- **15** more begin "The one"
- **97 of 109** hang on a dash

Forty-three of 109 open with the identical rhetorical move. Read three cards and you have read the
machine. Worse, "the pool" is internal vocabulary — I am a reader, I do not know there is a pool, I
have never seen the pool, and the sentence is arguing against candidates I cannot see. It is a judge
showing me the verdict in the language of the deliberation room.

And "the catalogue of names" appears **twice** — once in the picks block, once in the path step
reason for the same item. The good line got reused.

**Does "picked by AI" read as honesty or as a disclaimer?** As a disclaimer, and here is why: it is
set in small grey type, beside the heading, in a slot where a byline would go — and there is no
byline anywhere else on this site. If the picks are labelled "picked by AI", the unlabelled prose
implies a person. There is no person. The tier ladder tops out at "Read by AI." The home page says
"checked by hand." So "picked by AI" is not the site being honest about one component; it is the one
place the site slips and tells the truth about all of it. That is a disclaimer's job, not
disclosure's.

**Structural failure:** in `browse.js`, `picksCell()` returns `null` the moment `q.trim()` is
non-empty, and requires exactly one role, one level, and zero other filters. So the best editorial
work on the site **disappears the instant anyone searches**, or adds a time filter. All five of my
searches — the natural way a writer arrives — showed zero picks. The site hides its judgment from
anyone who asks a question in words.

**Layout:** the pick sentence renders *after* the whole card, below "Checked 29 Aug 2026 / No publish
date given." The argument for the pick sits underneath the fine print.

---

## 7. Dates and tier badges

**Dates.** The number is **489 of 635 — 77%** show "No publish date given." Three in four, as
advertised.

Three cards show month-only updates: "Updated 2026-06", "Updated 2026-02", "Updated 2026-05"
(**Real-World AI for Everyone**, **Claude AI Comprehensive Guide**, **Claude Design Fundamentals**).
Eighteen cards print "Published 23 Apr 2026 / Updated 23 Apr 2026" — the same date twice, on two
lines, saying nothing.

**Maintained or abandoned?** Maintained, and I want to be fair about this. Every single one of the
635 items carries a `checked` date in **August or September 2026** — 415 in August, 220 in the five
days of September. Nothing is stale on the site's own side. That is genuinely rare.

The rot is elsewhere. Because 77% have no publish date, the staleness warning **cannot fire on
them**. Only **17 of 635** carry "Published over a year ago — may not match Claude today." The home
page's third promise —

> "**We show the date.** Claude changes every few months. You can see when we last looked, and
> whether the thing is old."

— is structurally impossible for three quarters of the catalogue. The site can tell me when *it*
looked. It cannot tell me whether the thing is old. Half of that promise is undeliverable and the
page states it as fact.

**Tier badges.**

- **Read by AI** — "AI read all of it. No person has checked the notes yet." — 98 items
- **Skimmed** — "We read the outline or a free sample. We have not seen the whole thing." — 501 items
- **Found only** — "We found it and sorted it. **Nobody has looked at the content yet.**" — 36 items

**What they say about the work behind this: 85% of the catalogue was never read.**

And then the badges collide with the prose. Live, on the Princeton page:

> **Found only.** We found it and sorted it. **Nobody has looked at the content yet.**

On the same page, above it:

> "Princeton's page on when and how to disclose AI use in research and scholarship, aimed slightly
> higher up the ladder than undergraduate coursework guides."
> **What it teaches** — Determine when research scholarship requires formal AI disclosure / Apply
> institutional standards to thesis writing documentation
> **Skip it if** — You are writing ordinary coursework. **The Melbourne, Warwick or Tulane pages give
> you more usable templates for that.**

A page nobody looked at, summarised in detail, positioned "higher up the ladder", and **compared
against three other named institutions**. Either somebody looked at it or the description is
invented. There is no third option.

This is not one card. **All 36 "Found only" items have a full summary, a "who it's for", a "skip if",
and 93 "What it teaches" bullets between them.** Another: **Hooks reference (Claude Code)**, badged
Found only, summarised as "The complete reference for Claude Code hooks: every lifecycle event, the
JSON input and output schema, exit codes, and the async, HTTP, prompt and MCP-tool hook variants" and
judged "it is enormous."

The badge is the site's central honesty mechanism. On 36 cards it is provably false, in both possible
directions.

---

## 8. Search, in my words

Default sort "Best checked first". All five run live.

**Q1 — `make my writing not sound like ai`** -> **10 results**
1. **How to Stop Claude Writing Like an AI** (Will Francis, Read by AI, updated 21 Jul 2026) —
   exactly right
2. **Create on-brand content (use case)** (Anthropic Academy) — fine
3. **Claude Code for Data Analysis** — "Analysts/researchers comfortable in a terminal who want
   reproducible pipelines. Assumes Python." **Skip if: You never touch a terminal.**

**Verdict: 2 of 3.** A Python pipeline article at #3 for a question about prose. And
**Wikipedia:Signs of AI writing** — the site's own pick for this reader, its own step 2, described in
its own words as "the catalogue of names" — **is not in the top ten.** The editorial layer knows the
answer. The search layer has never met it.

**Q2 — `do i have to say i used ai`** -> **18 results**
1. **Referencing AI and Acknowledging AI Use** (Warwick Library) — for "a student", "the departmental
   section is Warwick-only"
2. **How to Spot AI Writing, According to Wikipedia** — answers "how do I get caught", not "must I
   disclose"
3. **Using AI in education settings: support materials (UK DfE)** — "School and college staff **in
   England**"

**Verdict: 0 of 3.** Three academic-integrity pages for a freelance writer with a client. The site
owns the right answer — **The Ethics of Using AI**, step 4 of my own path, the step it calls "the one
with consequences" — and does not surface it. I am a marketer, not an undergraduate at Warwick, and
nothing in the top three knows that even though I told the site my role on the previous screen.

**Q3 — `keep my own voice`** -> **26 results**
1. **Using AI for Writing Feedback** (Northeastern) — **Found only** · **"Published over a year ago
   — may not match Claude today"** · for "A student who has finished a draft and has nobody to read it
   before the deadline" · its own Skip-if says *"You have access to a writing centre or a tutor. Human
   feedback... is still better."*
2. **Create on-brand content (use case)** — good
3. **Write in my voice** (Anthropic Academy) — **the literal title of my query, at number three**

**Verdict: worst result of the five.** The #1 slot went to the lowest-trust badge on the site,
flagged as over a year old, aimed at a student, on a card that tells me to go find a human instead.
The exact-title match is buried under it.

This exposes a control that lies. The sort dropdown says **"Best checked first."** In `browse.js`,
when a query is present, relevance overrides tier entirely. So the dropdown displays "Best checked
first" while ranking a "Found only" item above two "Skimmed" ones.

**Q4 — `em dash`** -> **0 results**

> **No match for "em dash".**
> Try fewer words, or browse by role instead.

Zero. The most famous AI-writing tell in the English language. On a site that stocks
**Wikipedia:Signs of AI writing**, **How to Stop Claude Writing Like an AI**, **How to Spot AI
Writing, According to Wikipedia**, and a repo literally named **avoid-ai-writing** — all four of
which are about exactly this.

And the empty state advises "Try fewer words." I typed two. The advice cannot be followed.

**Verdict: total failure**, and the most embarrassing one, because it is the query a writer is most
likely to type.

**Q5 — `ghostwriting for clients disclosure`** -> **12 results**
1. **IEEE — Author Guidelines for AI-Generated Text** — for IEEE conference submissions
2. **Equipping agents for the real world with Agent Skills** — "Anyone writing their first SKILL.md"
3. **Referencing AI and Acknowledging AI Use** (Warwick) — student again
4. **Skill authoring best practices** — another developer doc

**Verdict: 0 of 3.** Two of the top four are Claude Code skill-authoring documentation. The mechanism
is visible in the shipped `search.js`: whole-word matching on an index where **"clients" means MCP
clients**, not paying customers. I asked about the people who pay me and got software architecture.

**Scorecard: 5 queries, 15 top-three slots, 5 useful.** One query returned nothing at all.

The shipped source comment claims: *"Measured on the eight benchmark sentences... keyword matching
alone puts the right resource first in seven of them."* Eight sentences is not a benchmark. It is a
sample size that guarantees you will believe your search works.

---

## 9. On a phone (375 x 812)

Better than I expected, and I was hoping for something to hate.

**Works:** filters collapse into a sticky bottom **"Filters"** button that does not overlap content.
Cards reflow to one column. Chips stay tappable. No horizontal scroll. Type stays readable. The
picks block keeps its heading and its "picked by AI · 5 Sep 2026" line.

**Does not:**
- The home page above the fold is header + **"I'm a [role] and I've [level]."** at display size + ten
  chips, with **"Show me" cut off at the bottom edge**. The two square-bracket placeholders are, at
  that scale, the loudest thing on the screen and they look like a rendering failure. First
  impression on the device most people arrive on.
- The mug — the one piece of personality — is pushed below the fold entirely.
- Long titles stack badly: **"Building a Claude Project for Teaching & Learning (recording)"** takes
  five lines and pushes everything else off screen.

**Verdict: pass, with the front door as the weak point.** The place a phone user is most likely to
bounce is the only place a phone user starts.

---

## 10. Keyboard walk

I tabbed the full Browse page. The craft here is real and then it is undone by one decision.

**Good:**
- **Tab 1 is "Skip to content"** — present and correct, hidden at `left: -9999px` until focused.
- Focus rings are visible on every stop, drawn with `outline` (not `box-shadow`), and the stylesheet
  pins `outline-color: CanvasText` under forced-colors. Somebody thought about Windows High Contrast.
- Focusing a card *title* rings the **whole card**, not the link — genuinely nice.
- Filter options are `<button role="checkbox">` with real text content, so they announce properly;
  `aria-checked` carries state and the decorative check glyph is `aria-hidden`.
- The picks block uses `aria-labelledby` pointing at its own heading, and "Everything else for you"
  sits **outside** the section so a screen reader does not hear the whole catalogue as part of the
  picks. That is a detail almost nobody gets right.

**The problem — tab order fights the layout.** The full sequence to the first result:

> 1 Skip to content · 2 Learn Claude · 3 Browse · 4 Paths · 5 How we check · 6 Clear all · **7-16
> ten role checkboxes** · **17-20 four levels** · **21-24 four times** · 25 More filters · **26
> Search** · 27 Sort · 28-29 filter chips · **30 first result**

The search box sits at the **top of the visible page** and is the **26th tab stop**. The first result
is the 30th. A keyboard or switch user looking at a search field at the top of their screen has to
press Tab twenty-five times to reach it, passing through eighteen checkboxes they did not ask for. On
the unfiltered page it is 26 stops to the first card.

**Verdict:** the accessibility work here is above average and clearly deliberate — and then the
single most-used control on the page was put last in the DOM.

---

## 11. How we check

**Less. Considerably less, and it is this page that does it.**

I went in wanting to trust it. The register is right — short sentences, no hedging, no marketing.
Then I read it against the data.

**Line 1:**
> **"We would rather have 70 resources we can vouch for than 700 we cannot."**

The site has **635**. Zero at the top tier. Thirty-six at "Nobody has looked at the content yet."
They chose the 700. The opening sentence is a boast the catalogue refutes on the very next click.
This is the single worst sentence on the website, and it is worse *because* it is well written — it
is a good line defending a decision that was not made.

**Line 2:**
> **"What we do:** We find material, **read it**, and write two things: who it helps, and who should
> skip it."

"Read it" is false for the 36 marked "Found only" (the page's own definition: nobody looked) and
partial for the 501 marked "Skimmed." **537 of 635 — 85% — were not read.** Stated as flat fact,
present tense, no qualifier.

**Line 3, six lines below line 2:**
> **"What we will not do:** We do not copy anyone's description. **We do not list something we cannot
> open.** We do not take money to rank a resource."

And in the tier ladder immediately above it:
> **"Skimmed** — We read the outline or a free sample. **Paid courses usually stop here, because we
> cannot see inside them.**"

The page says it will not list things it cannot open, and then explains its second-largest tier as
*listing things it cannot see inside*. **501 items.** Two contradictory sentences, on the same page,
inside one scroll. Nobody has read this page aloud.

**And the "we" is never named.** The word appears throughout. There is no byline, no about, no name
anywhere on this site. It says "We are not affiliated with Anthropic" — which tells me who they are
*not* — and never once who they are. Meanwhile the picks are labelled "picked by AI", the tier ceiling
is "Read by AI", 635 items were checked inside five weeks (415 in a single month), and the shipped
`search.js` says in plain text that the index was built from *"the hidden fields **Gemini** wrote for
every resource."*

I am a writer. My name goes on my work; that is the entire premise of the path this site built **for
me**. It calls that path "Using Claude on work you put your name to." It ends that path on disclosure
and tells me: *"Craft is what you owe the page. This is what you owe the reader."*

The site does not do the thing it tells me to do. It will not put a name on its own work, and it will
not say plainly which parts a machine wrote. It discloses AI exactly where disclosure flatters it — a
small "picked by AI" badge that reads as scrupulous — and stays silent everywhere disclosure would
cost it, starting with **"635 resources, checked by hand."**

That is the disclosure standard it holds me to, failed by the page that exists to explain its
standards.

---

## 12. Everything broken, ranked by reader harm

| # | Finding | Evidence | Who it harms |
|---|---|---|---|
| **1** | **"Found only" cards make detailed content claims.** Badge: "Nobody has looked at the content yet." All 36 such items still ship a summary, a who-it's-for, a skip-if and 93 "What it teaches" bullets. Princeton's page is compared to "Melbourne, Warwick or Tulane". | `resource.html?id=...` (Princeton, Northeastern, Hooks reference) | **Everyone.** The badge is the site's honesty mechanism. If it is false, no badge on the site can be trusted, including "Read by AI". |
| **2** | **"Checked by hand" is false.** Home: "635 resources, checked by hand." Data: 501 Skimmed, 36 never opened, **0** at the "a person checked the notes" tier. 635 items checked in five weeks. | `index.html`; `how-we-check.html`; `data/items.js` | **Everyone.** It is the claim that earns the first click. |
| **3** | **"How we check" contradicts itself twice.** "We would rather have 70... than 700" over a 635-item catalogue. "We do not list something we cannot open" six lines under "Paid courses usually stop here, because we cannot see inside them" (501 items). | `how-we-check.html` | **Everyone**, and worst for the careful reader who went looking for the methodology. |
| **4** | **Search fails a writer's plain-English queries.** 5 of 15 top-three slots useful. `em dash` -> **0 results**. `ghostwriting for clients disclosure` -> SKILL.md docs. `keep my own voice` -> a "Found only", year-old, student-facing page at #1. | `browse.html?q=...`, all five reproduced | **Everyone who types instead of filtering** — the majority arrival path, and the one the home page invites with "Or describe what you want to do..." |
| **5** | **The picks block vanishes on search.** `picksCell()` returns null when `q` is non-empty or any extra filter is set. The best editorial work is invisible to anyone who asks a question. | `assets/js/browse.js`; all 5 queries showed none | **Everyone who searches.** The site hides its only real differentiator from its most engaged users. |
| **6** | **The staleness warning cannot fire on 77% of items.** 489/635 "No publish date given" -> only 17 ever show "Published over a year ago". The home page promises "whether the thing is old". | `data/items.js`; every card | **Everyone.** Silent failure — an unflagged card reads as current when it is simply undated. |
| **7** | **"Built things with it" is a dead end for writers.** 3 resources, all Skimmed, 2 undated, no picks block, no path. 37 of 40 cells have picks; mine is one of the 3 that do not. | `browse.html?role=writer-marketer&level=builder`; `data/picks.js` | **Experienced writers** — the readers most able to judge the site, given the least. Same dead end for students and teachers at that level. |
| **8** | **Sort control lies under search.** Dropdown reads "Best checked first"; with a query, relevance overrides tier, so "Found only" outranks "Skimmed". | `browse.js` + Q3 reproduced live | **Anyone trusting the sort.** |
| **9** | **1,252 of 1,365 "What it teaches" bullets are unedited machine output.** "Install Claude **code** across **macos linux and windows** environments" three centimetres below a paragraph that writes "macOS, Linux, Windows" correctly. 113 bullets contain a comma. | `resource.html?id=r-4d17281029`, and ~36 known lowercase proper nouns catalogue-wide | **Everyone.** Visible carelessness on the product-detail page destroys the "we read this" claim faster than any missing date. |
| **10** | **161 of 635 cards repeat their own label.** "Skip if: Skip if you..." under a heading reading "Skip it if". 104 other cards use the correct convention. Thirteen consecutive offenders on one screen. | Live on `browse.html` and `resource.html` | **Everyone.** It is the site's flagship feature, printed wrong on a quarter of the catalogue. |
| **11** | **"Skip if:" is used for text that is not a skip reason.** "Skip if: **Nothing** — worth reading..."; "Skip if: Two rules here catch people out at other publishers too..." (a reason to read). | Use Claude Cowork safely; IEEE; Elsevier cards | **Skimmers**, who read the label and act on the opposite of what it says. |
| **12** | **"about 81 minutes."** Every sibling path rounds to hours; the writer's path prints a raw sum. | `paths.html`, live | **Writers**, on the page written for them. |
| **13** | **The picks formula.** 66/109 sentences use "candidate", 43 open "The only"/"The one", 35 argue against "the pool" the reader cannot see. 97/109 hang on a dash. | `data/picks.js`, all 109 | **Anyone reading more than three.** The judgment stops sounding like judgment and starts sounding like a template. |
| **14** | **Search is the 26th tab stop**, first result the 30th, while the search box sits at the top of the screen. 18 checkboxes come first in the DOM. | Live tab walk on `browse.html` | **Keyboard and switch users.** |
| **15** | **No house style.** 766 spaced hyphens vs 91 em dashes; organisation/organization, behaviour/behavior, licence/license all split roughly evenly. | All reader-facing prose | **Nobody's day is ruined** — but on a site selling editorial judgment it is the tell that no editor exists. |
| **16** | **Redundant date lines.** 18 cards print "Published 23 Apr 2026 / Updated 23 Apr 2026" — same date, two lines. | Browse cards | **Scanners.** |
| **17** | **Square-bracket placeholders dominate the phone front door.** "I'm a [role] and I've [level]." at display size, with "Show me" cut off below the fold. | 375x812, `index.html` | **Mobile first-time visitors** — reads as a broken template in the first second. |

---

## 13. The one thing that would make me leave

Not the search. Not the dates. This:

I clicked **"Found only"** expecting it to mean *we have not got to this one yet* — and found a full
review underneath it. Summary, audience, a skip reason, four things it teaches, and a comparison
against three named universities, all sitting under the words **"Nobody has looked at the content
yet."**

The moment I saw that, every other badge on the site became worthless to me. "Read by AI" now means
whatever "Found only" means, which is nothing. And once the badges are gone, this is a list of links —
which is precisely what the site says it exists to not be: *"A link with no judgment is just a list,
and lists are what made this hard in the first place."*

The badge ladder is the entire product. If it does not hold, nothing does. Fix that before you fix
search.

---

## 14. What is genuinely good

- **The premise.** "Who should skip this" is the right idea and nobody else does it.
- **Individual sentences.** *"Craft is what you owe the page. This is what you owe the reader."* — the
  best line here, in the right place, at the end of the path where it does the most work. Also *"you
  cannot prompt your way out of a tell you cannot name"* and *"the catalogue of names."*
- **The picks are real picks.** Not the first three rows — I checked. Each one names a discriminator
  instead of praising. The instinct is exactly right; only the phrasing has calcified.
- **Path step reasons argue for position, not just inclusion.** *"Only now is this useful... read in
  the other order it is a list of fixes for problems you have not learned to see yet."*
- **The catalogue is actually maintained.** All 635 items carry a check date inside five weeks.
- **Real accessibility craft.** Skip link, visible `outline`-based focus, forced-colors handling,
  whole-card focus rings, `aria-labelledby` on the picks region and "Everything else" deliberately
  placed outside it.
- **Honest cost lines.** *"It costs $995 and that is not the whole price..."*, *"some paid steps"*,
  *"The free tier stops at five Projects."* No affiliate-flavoured mush.
- **"We do not track your progress. Nothing here needs an account."** Nine words. Better than most
  privacy policies.
- **My three builder cards are the best-written on the site** — contractions, correct em dashes, no
  doubled labels. Whoever hand-edited those should edit the rest.

The bones are good. The problem is that a directory whose product is trust has shipped a trust badge
that contradicts the text beside it, a methodology page that contradicts itself twice, and a
front-page number that its own data disproves — and has not put a name on any of it.

---

## Checklist
- [x] I opened the live site at all four levels of my role — 19 / 36 / 8 / 3
- [x] I quoted at least 5 real titles or lines from the site — 35+
- [x] Every number I used is computed from the shipped data
- [x] I looked at a phone width — 375x812
- [x] I did one full keyboard walk — 30 stops to the first result
- [x] Five search queries in my own words, each with its verdict — 5 of 15 slots useful
- [x] I read the picks block and tested whether it is the top three rows — it is not; and I counted
      the formula across all 109 pick sentences
- [x] I found at least one thing nobody has mentioned before — the writer path's ordinal ladder goes
      First, Second, [nothing], Last, so the sequence reads as a five-step path with the middle
      removed; and 1,252 of 1,365 "What it teaches" bullets carry no punctuation at all
