# Attack 2: working with data
Written as someone who works with data, 2026-09-05. Live site only:
`https://mojtaba-alehosseini.github.io/learn-claude/`.

I have a spreadsheet, a deadline, and somebody who will ask where the number came from.

---

## 1. First 60 seconds

Big serif headline: **"I'm a [role] and I've [level]."** Under it, "Who are you?" and ten
chips. I found mine on the second row: **"working with data"**. That is faster than any
directory I have used.

Then the tagline: *"Find what's worth your time."* and *"635 resources, checked by hand."*
The three promises underneath are the right three: *"We say when to skip"*, *"We say how we
checked"*, *"We show the date"*.

First doubt inside 60 seconds: an animated mug drawing cycles beside the headline while I
read. It is decoration. I do not need a mug. I need to know if there is anything here about a
CSV.

---

## 2. The front door, all four levels

| I've... | Resources |
|---|---|
| never used Claude | **7** |
| used it a little | **21** |
| used it a lot | **23** |
| built things with it | **37** |

**The "never used" cell (7) is not thin. It is empty of the thing I came for.** Here is all
of it:

1. Upload files to Claude (Help Center)
2. How long do you store my data?
3. Claude 101 (DataCamp)
4. Claude 101 (Anthropic Academy)
5. How does Claude handle mathematical equations and calculations?
6. AI capabilities and limitations
7. Tokens: why some inputs cost more than others

Of those seven, **one** — the DataCamp course — has anything about a spreadsheet, Excel, CSV
or a chart in what it teaches. Six of the seven are published by Anthropic. So the answer
this site gives a data analyst on day one is: read a file-upload help page, then read a
data-retention policy, then read a page about token pricing.

That is not a curriculum. That is onboarding paperwork.

The jump to level 2 makes it worse, not better. Move one notch to **"used it a little"** and
suddenly there is *"Use Claude for Excel"*, *"Getting started with Claude in Excel"*, *"15
Claude Tips for Everyday Data Analysis"*, *"Master Claude for Excel in 10 Minutes: Financial
Modeling"*. All the spreadsheet material lives one level above the beginner. **The level
filter is hiding the exact content the beginner came for**, on the theory that a person who
has not used Claude has also never used Excel. I have used Excel for eleven years. I have not
used Claude. That is the normal case in my job, and the site has no cell for it.

---

## 3. What the catalogue gives me

The card format is the best thing here. Every card carries a tier badge, **`For:`**, **`Skip
if:`**, format/time/cost chips, `Checked <date>` and a publish-date line, and sometimes `Step
3 of 5 in <path name>`.

The `Skip if:` lines are frequently excellent and specific. Best one I saw, on *Use Claude
for Excel*:

> "Skip if: You are on a free plan - the add-in needs Pro, Max, Team or Enterprise... it says
> outright not to use it for audit-critical calculations without verification, and it carries
> an explicit prompt-injection warning - a downloaded template or a vendor's workbook can
> contain hidden instructions that push Claude into extracting or destroying data, and
> testing has produced exactly that."

That is a warning I would forward to my team. Nobody else writes that.

Where the filter falls down: the role filter leaks. In my **working with data** list I got
*"Prompting 101 | Code w/ Claude"* whose own `For:` line says **"Developers writing their
first production prompts"**, and *"Analyze patterns in user feedback (use case)"* whose `For:`
says **"Designers and product managers"**. If the card itself tells me it is for someone else,
it should not be in my filter.

---

## 4. Paths

There is a route for me: **"Analysing your own data without getting the numbers wrong"** —
*"For working with data · 5 steps · about 2 hours · free"*. Sub-line: *"Analysts with a
spreadsheet, a deadline, and somebody who will ask where the number came from."* That sentence
is my job description. Good.

I read every step reason. **Each one explains its position, not just its content.** This is
real editorial work and it is rare:

- Step 2: *"Second, and second on purpose. The writing path puts disclosure last because a
  writer discloses at publication, after the craft. An analyst decides at upload, before
  anything: once somebody else's data is pasted, reading the retention terms afterwards
  changes nothing."*
- Step 4: *"Fourth, because step 3 is only half of it: Claude has that code-running mode and
  does not always reach for it."*
- Step 5: *"This one needs a terminal, so stop here if that is not your working day — the four
  steps above stand on their own."*

Two things break it.

**(a) The maths on the page does not add up.** The step chips read `15 min · 15 min · 15 min ·
1 hour · 1 hour` = 165 minutes. The header says **"about 2 hours"**. Two numbers on one
screen, 45 minutes apart, and I am the person who will be asked why the estimate was wrong.
Across the seven paths the labelling rule is not a rule at all: 93 minutes is called *"about 2
hours"*, 126 minutes is also *"about 2 hours"*, 270 minutes is rounded **down** to *"about 4
hours"*, and 81 minutes is printed raw as **"about 81 minutes"**. Nobody says "about 81
minutes."

**(b) Step 3 is a page the site itself says is dead.** *"Introducing the analysis tool in
Claude.ai"*, published 24 Oct 2024. Its own card in Browse says:

> "Read the update notice before the article: the analysis tool this post introduces is being
> replaced by code execution... **So this is history rather than instruction - useful for
> understanding why Claude runs code at all, useless as a guide to doing it today. Go to the
> code execution documentation for the current feature.**"

The path knows the current documentation exists and still routes me to the obsolete page
instead. Step 3 of 5, in the middle of the run.

---

## 5. The card and the resource page

I clicked through three. Structure is good: **What it teaches** (three bullets), **Who it's
for**, **Skip it if**, **Where this fits**, **How we checked this one**, then a footer line and
a *"Something wrong with this one?"* link.

Would I click through from a card? Sometimes. The card already carries `For:`, `Skip if:`,
tier, time and cost. The detail page adds "What it teaches" — and **takes information away**
(see section 7, finding 3). A detail page that shows less than the summary card is a detail
page I stop opening.

The `Skip it if` heading is also mislabelled on some entries. On *"How to Use Claude for CSV
Data Analysis"* the block reads:

> "Skip it if — One idea makes it worth the unknown byline: Claude handles a CSV two different
> ways, and only one of them actually runs the arithmetic. If a total has ever come back
> wrong, this explains why."

That is a reason to **read** it, printed under a heading that says skip. Same pattern on *"Use
Claude Cowork safely"*: **"Skip if: Nothing — worth reading before your first real Cowork task
regardless of experience level."** At least eleven entries do this. The one field the whole
site is built around is being used for the opposite of its label.

---

## 6. The picks block

Labelled **"Start with these three"**, with **"picked by AI · 5 Sep 2026"** beside it, one
sentence per card, and everything else pushed below a heading **"Everything else for you
(18)"**. Nothing hidden. That is the honest way to do it.

**Is it the first three rows?** No. I checked all 37 populated role-by-level cells against the
page's own default "Best checked first" order: **only one cell's picks match the default top
three**, and nine cells share zero items with it. Somebody actually chose.

**Does each reason add something the title did not?** Mostly yes, and they argue against the
pool rather than describing the item:

- *"The pool's one non-Anthropic voice, and the course that goes on to tour Projects, Skills
  and connectors where the official twin stays at chat basics."*
- *"The bridge nobody else in the pool builds: a non-coder taking 78 years of weather data
  through Claude Code to a finished report."*
- *"Fourteen connector pages in this pool, and this is the one self-serve one - no invitation,
  no sales call."*
- *"The one candidate that ends with something reusable for any dataset... where thirty of
  thirty-three candidates run one predefined workflow."*

Those are comparative judgments. They tell me what the alternatives were. I trust them more
than the titles.

**Do I trust "picked by AI" more or less?** Slightly less than a name, but the label is doing
its job — it warns me and it is consistent with the badges. What kills the trust is not the
label, it is what the label is attached to.

**My level-3 picks, ranked #1: an article on `qwe.edu.pl`, published by "QWE AI Academy".**
The site's own words for it: *"One idea makes it worth **the unknown byline**"*. Tier:
`Skimmed` — nobody read it. No publish date. And it is simultaneously **step 4 of 5 in my
path**. The single most load-bearing item on my entire journey is an anonymous domain that
nobody on this site has read to the end.

**My level-4 picks are two publishers, and both are Anthropic.** `GitHub · Anthropic`
(claude-cookbooks), `Anthropic Academy`, `Anthropic Academy`. That is not narrowness of taste
— it is narrowness of stock: the whole 37-item pool is **Anthropic Academy (30) + GitHub (7)**
and nothing else. The picker had no third voice to pick.

---

## 7. Dates and tier badges

**489 of 635 cards (77%) say "No publish date given."** For a directory whose third promise is
*"We show the date"*, that promise is kept on 23% of the catalogue.

**Finding: the same item shows different dates on two pages.**

- `browse.html?q=Comprehensive%20Guide` -> card reads `Checked 5 Sep 2026 / No publish date
  given / **Updated Feb 2026**`
- `resource.html?id=r-158b800917` -> same item reads `Checked 5 Sep 2026 · No publish date
  given · Found through Coursera`. **The Updated line is gone.**

Reproduced on a second item with a full date: *Upload files to Claude (Help Center)*. Card:
`Updated 23 Jul 2026`. `resource.html?id=r-5a7be113ab`: no Updated line. 96 items carry an
Updated date; the detail page drops it on all of them.

**Finding: "No publish date given" is sometimes false.** I fetched 28 randomly sampled items
labelled "No publish date given". **Five carry a machine-readable publish date in their own
HTML** (`article:published_time` / `datePublished`) — including *Claude Code is secretly an
excellent data analysis tool* (2025-07-09) and *3 Claude Skills Every Data Scientist Needs in
2026* (2026-05-21). Separately:
`https://www.qwe.edu.pl/tutorial/claude-csv-data-analysis/` — the #1 pick for my level —
carries `article:published_time = 2026-04-25`. The site says it has no date. That is roughly
one label in five being wrong, on the field the site names as a core promise.

**Finding: the staleness warning deletes the date.** 17 cards read **"Published over a year
ago — may not match Claude today"** *instead of* a date — including *Building effective
agents*, *Claude Code best practices*, *Prompting 101*. Meanwhile *"Introducing the analysis
tool in Claude.ai"* shows a plain **"Published 24 Oct 2024"** with no warning at all. From my
seat: the older item looks safe, the newer one looks risky, and neither card tells me why.

**Maintained or abandoned?** Maintained. `Checked 5 Sep 2026` is today. Picks are dated 31 Aug
to 5 Sep 2026. Whoever runs this was here this week. The date problem is not neglect — it is a
checking process that stops before reading a `<meta>` tag.

**Tier badges.** Vocabulary is honest and the definitions are printed:

- `Read in full` — "We went through all of it and a person checked the notes." — **0 items**
- `Read by AI` — 98
- `Skimmed` — "We read the outline or a free sample." — 501
- `Found only` — "Nobody has looked at the content yet." — 36

**79% of this catalogue has been skimmed, not read.** The "How we check" page explains why:
*"Paid courses usually stop here, because we cannot see inside them."* That explanation covers
**46 of the 501 Skimmed items. The other 455 (91%) are free.** There was no paywall. They just
were not read. The tier is honest; the excuse attached to it is not.

Worst combination, and it is my cell: **"working with data" + "built things with it" = 37
items, of which 33 are `Skimmed` and 4 are `Found only`. Zero `Read by AI`. Zero with a publish
date.** And the four `Found only` entries — *Tableau MCP (official)*, *Postgres MCP Pro*,
*MotherDuck / DuckDB MCP Server*, *ClaudeR (R + RStudio MCP)* — are the four things a working
analyst would most want, and they are the four nobody opened.

---

## 8. Search, in my words

| # | I typed | Results | Top three | Verdict |
|---|---|---|---|---|
| 1 | `claude excel formulas` | 16 | 15 Claude Tips for Everyday Data Analysis (LinkedIn Learning, subscription) · Use Claude for Excel · Master Claude for Excel in 10 Minutes | **Pass, barely.** A paywalled video outranks the free official Excel doc. The word "formulas" is ignored — the one item that actually writes formulas (*How to use Claude in Excel for HR: Headcount planning*, "need Claude to actually **write formulas** into it") sits at #6. |
| 2 | `can claude read my csv` | 22 | Upload files to Claude · **Pull metrics from analytics dashboards** · **Introducing the analysis tool in Claude.ai** | **Fail.** #1 is right. #2 is about Claude in Chrome reading Amplitude and Stripe — nothing to do with a CSV. #3 is the page the site itself calls "useless as a guide to doing it today". The article literally titled *"How to Use Claude for CSV Data Analysis"* ranks **6th**, behind a Figma MCP setup guide at #7. |
| 3 | `sql` | 7 | Anthropic's Prompt Engineering Interactive Tutorial · Introduction to Claude (code-along) · Claude Code for Product Managers | **Fail.** A generic prompting tutorial and a PM course beat *Postgres MCP Pro* (#5) and *MotherDuck / DuckDB MCP Server* (#6) for the query "sql". Both of those are `Found only`. |
| 4 | `pivot table` | 3 | Claude Code for Data Analysis: Excel-Free Answers From CSVs · How to Use Claude Code as a Product Manager · **avoid-ai-writing (Claude Code / agent skill)** | **Fail, and dishonest about it.** There is nothing here on pivot tables. Instead of saying so, it returns three items, one of which is a skill for making Claude stop writing like an AI. The site has a good empty state and refuses to use it. |
| 5 | `stop claude making up numbers` | 37 | **Claude for Education Is Made for Learning** · Reduce hallucinations · 3 Mind Blowing Claude & Consensus Research Workflows | **Half a pass.** #2 is exactly right. #1 is a marketing page about education, returned first for a question about wrong numbers. |

Three of five queries put an irrelevant result in the top three. Two of five bury the
obviously-correct answer below it. The search box invites *"Title, topic, or what you want to
do"* — the "what you want to do" half is where it breaks.

---

## 9. On a phone

At 375px this is fine, and better than most. Filters collapse into a sticky **Filters** button
pinned to the bottom of the screen. The applied chips (`working with data x`, `used it a
little x`) stay visible above the count. Search and Sort are full width. Cards stack cleanly,
the tier badge and publisher mark stay legible, nothing overflows sideways, nothing needs a
pinch. The picks block keeps its heading and its `picked by AI · 5 Sep 2026` line.

No complaint. This part was done properly.

---

## 10. Keyboard walk

Tab order on `browse.html?role=data-analyst&level=basic` is clean and in visual order:

1. `Skip to content` — appears on first Tab with a visible ring, correct
2. wordmark -> Browse -> Paths -> How we check
3. `Clear all`
4. ten role filters, four level filters, four time filters, `More filters`
5. search box -> sort dropdown -> the two `Remove filter:` chips
6. every result title, in order
7. footer

Every filter exposes a proper accessible name and state — `<button role="checkbox">` with
`aria-checked="true"` on *working with data* and *used it a little*, `aria-checked="false"` on
the rest. The remove chips announce as **"Remove filter: working with data"**, not as a bare
"x". Focus is drawn with `outline`, never `box-shadow`, and the card title's ring is moved
onto the whole card so it does not clip.

Nothing to report against it. This is the most carefully built part of the site.

---

## 11. How we check

**Down.** The page is honest and its own honesty is the problem.

The percentages first, since I checked them:

- *"635 resources — 98 read by ai, 501 skimmed, 36 found only."* -> 98 + 501 + 36 = **635.
  Correct.**
- *"390 of those 635 (61%) are Anthropic's own"* -> 390 / 635 = 61.4% -> **61%. Correct.**

The arithmetic is fine. **What the numbers mean is not what the sentences around them claim.**

**The page opens by promising the opposite of what it then reports.** First line: *"We would
rather have 70 resources we can vouch for than 700 we cannot."* Six paragraphs later:
*"Nothing is read in full yet, and the cards say so."* They shipped 635 they cannot vouch for.
The headline sentence is contradicted by the page's own count, on the same screen.

**The Anthropic sentence answers the wrong question.** *"...the rest are here because they
passed the same check, not a lower one."* It steers me to worry about the non-Anthropic 245.
The data says worry about the other half:

| | `Read by AI` | `Skimmed` | No publish date |
|---|---|---|---|
| Anthropic's own (390) | 12% | 87% | **89%** |
| Everything else (245) | 21% | 67% | 58% |

**The Anthropic material was checked less thoroughly and dated less often than the independent
material.** The page invites me to inspect the wrong half.

**"We show the date"** is the third promise on the home page. It holds for 146 of 635 items.
The "older than 12 months" flag can fire on 17 cards in the whole catalogue — 2.7% — because
77% have no date to age.

Credit where due: the certification paragraph is the sharpest thing on the site. *"Anthropic
runs a real certification, but it is open to members of the Claude Partner Network, not to the
public. A lot of sites sell preparation for an exam most readers cannot sit. If you find one of
those, that is why it is not in here."* That is a real editorial decision, stated, with a
reason. More of that.

---

## 12. Everything broken, ranked

**1 — The entry-level cell for my role contains no analysis content.**
`browse.html?role=data-analyst&level=never-used`. Saw: 7 results; picks are *Upload files to
Claude (Help Center)*, *How long do you store my data?* and *Claude 101 (DataCamp)*. Six of the
seven are Anthropic; one mentions Excel. Expected: a first lesson on getting a number out of a
spreadsheet. **Harms:** every analyst who is new to Claude — the largest slice of the audience
the tagline courts. They conclude the site has nothing and leave in 90 seconds.

**2 — The advanced cell is vendor sales collateral, unread and undated.**
`browse.html?role=data-analyst&level=builder`. Saw: 37 results from exactly two publishers —
Anthropic Academy (30) and GitHub (7). 24 of the 30 are financial-services connector pages:
*"Using Moody's for financial analysis"*, *"Using PitchBook for investment research"*, *"Using
LSEG for financial market data analysis"*, *"Draft investment memos"*, *"SOX & controls
documentation"*. 33 `Skimmed`, 4 `Found only`, **0 `Read by AI`, 0 with a publish date**.
**Harms:** the experienced analyst, who is the reader most likely to recommend the site onward
and most able to spot that this is a product catalogue.

**3 — The detail page shows fewer date facts than the summary card.**
`browse.html?q=Comprehensive%20Guide` card: `No publish date given / **Updated Feb 2026**`.
`resource.html?id=r-158b800917`: `No publish date given` — Updated line absent. Reproduced on
`resource.html?id=r-5a7be113ab`. Affects all 96 items that carry an Updated date. **Harms:**
anyone deciding whether a doc is current — the exact decision the click-through exists to
support.

**4 — "No publish date given" is wrong on roughly one in five of the items it labels.**
I fetched 28 sampled items carrying that label; 5 carry a publish date in their own HTML meta.
Plus the site's #1 pick for my level, `qwe.edu.pl`, which publishes `article:published_time =
2026-04-25`. **Harms:** everyone, because the staleness warning can only fire on items with
dates — a wrong "no date" permanently exempts an item from ageing.

**5 — "Skimmed" is explained by a paywall that does not exist for 91% of the items wearing it.**
`how-we-check.html`: *"Paid courses usually stop here, because we cannot see inside them."* 501
items are `Skimmed`; **455 of them are free**. **Harms:** anyone weighing how much confidence a
badge carries — the entire premise of the tier system.

**6 — The path's own numbers contradict each other.**
`paths.html?id=numbers-you-can-defend`. Header: *"5 steps · about 2 hours"*. Step chips on the
same page: `15 + 15 + 15 + 60 + 60` = 165 minutes. Across the seven paths: 93 min -> "about 2
hours", 126 min -> "about 2 hours", 270 min -> "about 4 hours" (rounded down), 81 min -> **"about
81 minutes"**. **Harms:** anyone budgeting time — which is the site's stated purpose.

**7 — Search returns off-topic results in the top three and hides the on-topic one.**
`?q=can+claude+read+my+csv` -> #2 *Pull metrics from analytics dashboards*, #3 a page the site
calls "useless as a guide to doing it today"; the CSV article is #6. `?q=sql` -> a prompting
tutorial above *Postgres MCP Pro*. `?q=pivot+table` -> 3 results, one of which is
*avoid-ai-writing*. **Harms:** everyone who types a question instead of browsing.

**8 — A path routes readers to a page the site itself calls obsolete.**
Step 3 of `numbers-you-can-defend` is *Introducing the analysis tool in Claude.ai*; its Browse
card says *"Go to the code execution documentation for the current feature."* **Harms:** the
beginner who follows the path in order.

**9 — "Skip if:" is used for recommendations on at least 11 entries.**
*"Skip if: Nothing — worth reading before your first real Cowork task regardless of experience
level."* / *"Skip it if — One idea makes it worth the unknown byline..."* **Harms:** skimmers,
who read only the `Skip if:` line and take a recommendation for a warning.

**10 — The staleness flag replaces the date it is warning about.**
17 cards read *"Published over a year ago"* with no date, while *"Published 24 Oct 2024"*
appears unflagged elsewhere. **Harms:** anyone comparing two old items.

**11 — The role filter admits its own mismatches.**
In `role=data-analyst&level=basic`: *Prompting 101 | Code w/ Claude* (`For: Developers...`) and
*Analyze patterns in user feedback* (`For: Designers and product managers`). **Harms:** trust in
the filter, which is the site's main navigation.

**12 — "How we check" points the reader's suspicion at the better-checked half.**
Anthropic items: 12% `Read by AI`, 89% undated. Everything else: 21% `Read by AI`, 58% undated.
**Harms:** readers calibrating trust, who are steered to inspect the wrong 245 items.

---

## 13. The one thing that would make me leave

**Step 4 of my path — the step the site calls the point of the whole thing — is an anonymous
website nobody read.**

The reason line: *"Fourth, because step 3 is only half of it... it is the step that explains
every total that has ever come back confidently wrong."* That is the most important claim on
this site for a person in my job. And the source is `qwe.edu.pl · QWE AI Academy`, described by
the site itself as **"the unknown byline"**, badged **`Skimmed`** — *"We read the outline or a
free sample. We have not seen the whole thing"* — on a free article with no paywall, labelled
**"No publish date given"** when the page publishes `2026-04-25` in its own meta tags.

So: the thing standing between me and a wrong number in front of my director is an unattributed
page that this site did not finish reading, did not date correctly, and then promoted to #1 pick
and step 4. If somebody asks me where the number came from, that is my answer. I close the tab.

---

## 14. What is genuinely good

- **`Skip if:` as a mandatory field.** No other directory does this. The prompt-injection
  warning on *Use Claude for Excel* is worth the visit on its own.
- **Path step reasons that argue their position.** *"Second, and second on purpose..."*, *"This
  one needs a terminal, so stop here if that is not your working day."* That is editing, not
  listing.
- **Picks are a real selection.** 36 of 37 cells differ from the default top three; the reasons
  compare against the pool (*"Fourteen connector pages in this pool, and this is the one
  self-serve one"*).
- **The tier vocabulary is honest and 0 items claim more than they earned.**
- **Empty state.** `?role=student&level=builder` -> *"We have nothing for this combination yet.
  It's on the list. Loosen the level, or browse everything."* Search should behave like this
  too.
- **Mobile and keyboard are both done properly** — sticky filter sheet, real `aria-checked`
  state, named remove-chips, visible focus rings, forced-colors handling.
- **The certification paragraph** — a stated exclusion with a stated reason.

---

## Checklist
- [x] I opened the live site at all four levels of my role — 7 / 21 / 23 / 37
- [x] I quoted at least 5 real titles or lines from the site — 25+
- [x] Every number I used is computed from the shipped data or fetched from the source page
- [x] I looked at a phone width — 375px
- [x] I did one full keyboard walk — browse, tab order recorded
- [x] Five search queries in my own words, each with its verdict
- [x] I read the picks block and tested whether it is the top three rows — 36 of 37 cells differ
- [x] I found at least one thing nobody has mentioned before — "No publish date given" is
      demonstrably false on about one item in five, verified by fetching the source pages'
      `article:published_time`; and the "paid courses" excuse for Skimmed covers 46 of 501
