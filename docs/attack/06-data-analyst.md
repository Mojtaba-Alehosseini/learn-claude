# Attack: working with data
Written as someone who is working with data, at 2026-08-27. Site version: 22e4532.

I am an analyst. SQL, spreadsheets, notebooks. I have one hour. Everything below was run
against the live site or against `data/items.json`, which is byte-identical to the
deployed data. I show every command.

---

## 1. The first 60 seconds

The home page asks me two questions in one sentence. I answer them honestly.

```
I'm working with data and I've never used Claude.
```

The site answers:

> **1 resource match so far.**

One. Out of 353. And it cannot even count to one in English.

I clicked "Show me" anyway. The browser tab said:

> **Browse 1 Claude resources — Learn Claude**

Under the single card, the site's advice to me was:

> **1 resource. Remove a filter to see more.**

So the first screen asks me two questions, I answer both truthfully, and the second
screen tells me to un-answer one of them. That is the whole 60 seconds. I have learned
nothing about Claude and I have learned that the site does not want my answer.

Evidence, live, in my own browser tab:

```js
// https://mojtaba-alehosseini.github.io/learn-claude/
role = document.querySelector('#roleOptions [data-value="data-analyst"]'); role.click();
// -> tally: "37 resources match so far."
document.querySelector('#levelOptions [data-value="never-used"]').click();
// -> tally: "1 resource match so far."
```

Source of the grammar fault: `assets/js/home.js:209` glues `LC.countText(n)` (which
returns `"1 resource"`) to the literal `" match so far."`, and `assets/js/browse.js:215`
builds the tab title from `out.length + " Claude resources"` with no singular case at
all.

---

## 2. Does the front door work for me       (all four levels, with counts)

```
$ python docs/attack/role-view.py data-analyst --counts
data-analyst: 37 total
  never-used       1
  basic           17
  confident       12
  builder          7
  tiers:   {'ai-reviewed': 8, 'previewed': 24, 'listed': 5}
  formats: {'article': 9, 'docs': 2, 'video': 11, 'repo': 8, 'hands-on': 4, 'course': 3}
  free:    27
  no date: 22
  only this role: 20
```

Live, clicking the four level chips in order:

| I answer | site says | is that an answer? |
|---|---|---|
| never used Claude | "1 resource match so far." | no |
| used it a little | "17 resources match so far." | yes |
| used it a lot | "12 resources match so far." | yes |
| built things with it | "7 resources match so far." | no — see 9.6 |

**On the one card.** The task asked whether one card is a legitimate answer to a question
the site asked. It is not, for three reasons.

1. The card is not about data. It is `Claude 101`, from Anthropic Academy. Its "For:"
   line is *"People who have never opened Claude and want the basics fast."* Nothing in
   it touches a CSV, a query, or a sheet. It is shared with four other roles
   (`business-founder`, `non-technical`, `researcher`, `writer-marketer`). The role chip
   I pressed changed nothing.
2. The card advertises a route I am locked out of. It carries the line
   *"Step 3 of 6 in Your first week with Claude."* That path names four roles and
   `data-analyst` is not one of them (`docs/attack/00-facts.md`, Paths section). The
   card is selling me a ticket to a train I am not on, and does not say so.
3. The site does not admit it has nothing. It has an empty state that says
   *"We have not covered this role yet. It's on the list."* (`assets/js/browse.js:198`).
   That state only fires at zero. At one, it goes quiet and blames my filter instead.

An honest site with one card would say "we have almost nothing for you at this level,
start here instead". This one says "Remove a filter."

The front door works at `basic` and `confident`. It does not work at either end.

---

## 3. What the catalogue actually gives me  (are these really for me?)

### 3.1 "Working with data" is three different people in one chip

I read all 37 `who_for` lines. They do not describe one job.

```
$ python - <<'PY'   # classify the 37 by the tool their who_for/summary/prerequisites assume
...
Excel / spreadsheets         10
Python / notebook            12
SQL / warehouse / database    5
terminal / Claude Code       10
R / RStudio                   1
API key                       4
No tool named at all         10
PY
```

Read the lines side by side and the split is obvious:

- *"Excel-primary analysts on paid Claude plans. Assumes Excel familiarity, no coding."*
  (`Use Claude for Excel`)
- *"Data scientists/researchers who write Python and want a real-world workflow. Assumes coding."*
  (`Claude Code is secretly an excellent data analysis tool`)
- *"BI analysts on Tableau Cloud/Server. Assumes a Tableau account and PAT/OAuth setup."*
  (`Tableau MCP (official)`)
- *"R users and quantitative researchers wanting reproducible, auditable analysis. Assumes R/RStudio."*
  (`ClaudeR (R + RStudio MCP)`)

A finance person in Excel, a Python data scientist, a Tableau BI analyst and an R
statistician are not one audience. They share a word, not a job. The site knows this —
it wrote the distinction into every `who_for` line — and then throws it away, because
the filter axes are role, level, time, topic, format and cost (`assets/js/browse.js:17-24`)
and none of them is *what tool do you actually use*. The `Topic` axis offers "chat and
prompting", "Claude Code", "Cowork", "Skills", "connectors", "agents", "API" and
"limits and safety". Not one of those separates Excel from Postgres.

Result: to find the 10 Excel items I have to read 37 cards. There is no shortcut, and
the site built the data that would give me one.

### 3.2 Ten of my 37 are general Claude material with a data label stuck on

These name no data tool anywhere in the title, summary, `who_for` or prerequisites:

```
never-used  Claude 101
basic       Introduction to Claude Cowork
basic       Complete Guide to Claude Cowork (Claude Code for Everyone)
basic       Prompting 101 | Code w/ Claude
basic       The ONLY Claude Cowork Tutorial You'll Ever Need in 2026
confident   Reduce hallucinations
confident   4 Lines You Should Include in Your Claude Skill
confident   How to Use Claude for CSV Data Analysis (The Honest Guide)
confident   AI prompt engineering: A deep dive
confident   How Model Context Protocol (MCP) actually works
```

Some of those are fair (`Reduce hallucinations` is exactly my problem). Three Cowork
overviews at `basic` is not. `Prompting 101 | Code w/ Claude` carries the Skip line
*"Skip if you only use the Claude chat app, because the session is framed around API
calls and system prompts"* — which describes most analysts, and it is still in my basic
list.

### 3.3 `docs 2`, `podcast 0` — the format mix is upside down

From `00-facts.md`: video 11, article 9, **repo 8**, hands-on 4, course 3, **docs 2**,
podcast 0.

I get four times as many GitHub repos as pieces of documentation. The two docs are
`Use Claude for Excel` and `Reduce hallucinations`. That is the entire reference layer
for the person whose job is being correct about numbers. Meanwhile the Format filter
still shows me a "podcast" chip that returns zero:

```
$ python - <<'PY'
Format:  video 11 | course 3 | docs 2 | article 9 | hands-on 4 | podcast 0 <- DEAD | code 8
Cost:    free 27 | free, sign-up needed 7 | pay once 0 <- DEAD | subscription 3
Filter chips offered to me that return zero: 2 of 27
PY
```

Two of the 27 chips offered to me are dead. Small, but it is two more clicks that end in
*"Nothing matches all of those. Try removing one filter — time is usually the one to
loosen."* — advice that is wrong, because time was not the problem.

### 3.4 "Go read this repo" is not teaching

Eight of my 37 are `repo` (`00-facts.md`), and the Format chip labels them **"code"**
(`assets/js/ui.js` — `LC.FORMAT.repo = "code"`). Seven of the eight sit at `builder`,
which is the entire builder level.

A GitHub README is a product page. It tells me the flags and the install command. It
does not tell me what a good analysis loop looks like, when Claude gets a SUM wrong, or
how to check its work. Four of those seven are tier `listed` — the site's own words for
that badge are *"We found it and sorted it. Nobody has looked at the content yet."*

So the top of my ladder is: five links to software nobody at this site has opened, with
no publish date, and no teaching in any of them. Compare the how-we-check page's own
promise:

> "We would rather have 70 resources we can vouch for than 700 we cannot."

At builder, for me, they vouch for none of it.

---

## 4. Paths

I have no path. That is already known and I will not spend a line arguing it.

What is **not** already known is what the Paths page does instead of telling me.

**It says nothing. It shows me other people's paths, in full, as if they were mine.**

Live, in my tab:

```js
// https://mojtaba-alehosseini.github.io/learn-claude/paths.html?role=data-analyst
document.body.innerText.toLowerCase().includes('working with data')  // false
document.body.innerText.toLowerCase().includes('analyst')            // false
```

The word "analyst" does not appear on the Paths page. Neither does "working with data".
The `?role=` parameter is read by nothing: `assets/js/paths.js` calls `LC.param("id")`
and never `LC.param("role")`. The page has exactly two states — a list of every path, or
"this path isn't ready" for a bad id. There is no third state for "you have no path".

So I get three headers, and I have to work out on my own that none is mine:

- **Your first week with Claude** — *"Anyone who has just opened Claude and does not know what to do next."*
- **Getting good at Claude Code** — *"Developers who have installed Claude Code and are getting mediocre results."*
- **Using Claude for research without embarrassing yourself** — *"Researchers and academics who want the speed without the retraction."*

Each path *has* a `roles` list in `data/paths.json`. The page never prints it. So I
cannot tell by reading whether "Your first week with Claude" is for me. I have to guess
from a one-line "for:" that says "anyone".

And it gets worse, because two of my 37 cards are steps inside those paths:

```
$ python - <<'PY'   # cross-reference data/paths.json steps against data-analyst items
PATH: Your first week with Claude | roles: ['non-technical','student','teacher','business-founder']
   3. Claude 101  <-- data-analyst
PATH: Using Claude for research without embarrassing yourself | roles: ['researcher','student']
   1. Reduce hallucinations  <-- data-analyst
PY
```

My **only** never-used card is step 3 of a path that excludes my role. Its resource page
says, in a section headed "Where this fits":

> "This is step 3 of 6 in Your first week with Claude. The order matters — the path says why."

I follow that link, because the order matters and I want the order. I land on a route
built for four other roles, and nothing on the way tells me. That is not a missing
feature. That is the site sending me somewhere it decided I do not belong, without
saying so.

---

## 5. The card and the resource page

I opened three. All live, all confirmed in the browser.

### 5.1 `Postgres MCP Pro (crystaldba/postgres-mcp)` — the repo one

`resource.html?id=r-9878646d22`. This is the card that matters most to me: it is the one
that connects Claude to a real database. Here is the whole page:

```
Found only
Postgres MCP Pro (crystaldba/postgres-mcp)
GitHub · Crystal DBA
code | one hour | free
The recommended PostgreSQL MCP server: configurable read/write access, EXPLAIN-plan
analysis, index tuning, and health checks, letting Claude query a database in natural
language.
Open on GitHub | Copy link
What it teaches
 — install and configure postgres mcp pro with appropriate read/write permissions
 — query postgres tables using natural language prompts in claude
 — inspect query execution plans and database indexes through claude
Who it's for
 Analysts connecting Claude to Postgres. Assumes DB credentials and comfort editing MCP config.
Skip it if
 You don't use PostgreSQL.
Before this
 — postgresql database credentials
 — comfort editing json mcp configurations
How we checked this one
 Found only. We found it and sorted it. Nobody has looked at the content yet. How we check.
Checked 19 Aug 2026 · No publish date given · Found through GitHub
```

The page tells me to hand a language model my production database credentials, and in the
same breath admits nobody at this site has looked at the thing. "Skip it if: You don't
use PostgreSQL" is the only judgment offered, and it is a restatement of the title.

Now here is what is in `data/items.json` for that exact record, in a field called `notes`:

> "Active, ~3.2k stars, 80 commits, no releases listed. **Use read-only/least-privilege
> role. Replaces the archived, vulnerable @modelcontextprotocol/server-postgres.**"

That is the single most useful sentence anywhere in my 37 cards. It is a security
instruction. It never reaches the page. See 9.2 and 9.3.

### 5.2 `Claude 101` — my only never-used card

`resource.html?id=r-6b31501da8`. Well made, honest, badged "Skimmed", dated, with a real
Skip line: *"You've already used Claude for a few weeks — this stays at 'what is a
prompt' level and won't teach you anything new."*

It is also step 3 of a path I am not in (section 4), and it is `free-account` — the chip
reads "free, sign-up needed". That is the honest label and I give the site credit for it.

Would I click through? Yes. Would it teach me anything about data? No. It teaches
*"attach and query documents and files in chat"*. I want to know whether Claude adds up a
column correctly. Different question.

### 5.3 `How to Use Claude for CSV Data Analysis (The Honest Guide)`

`confident`. The best-matched item for my second search. Its publisher line reads:

> **Pl**

The URL is `https://www.qwe.edu.pl/tutorial/claude-csv-data-analysis/`. The `source` field
in the data is literally the string `"Pl"` — the country TLD. The `author` field says
"QWE AI Academy" but `LC.authorLine` suppresses it when the author contains the source or
vice versa, so on the card I see "Pl" and nothing else. The resource page's own button
reads **"Open on Pl"**, and the footer says **"Found through Pl"**.

The card's Skip line is *"You want a named, established author or institution."* — which
is the site quietly admitting it does not trust the source, while displaying a source
name it generated by grabbing the last piece of a domain. Same fault on
`vincent.codes.finance`, which shows as **"Finance"**. Site-wide the same pattern
produces sources named `Au`, `To`, `Vc`, `Ac`, `Eu`, `Gov`, `Ed`, `Jhu`, `Syr`, `Kit`,
`World`, `Cloud`, `bri`.

---

## 6. Search, in my words

I typed three sentences the way I would actually type them. **This is where the site
breaks worst, and it breaks in a way nobody would find by testing search alone.**

### 6.1 The trap: the search box on the home page does not use search

The home page's field says *"Or describe what you want to do…"*. It submits to
`browse.html?q=…` (`assets/js/home.js`, submit handler). The ranked index is loaded
**only** from the `input` event handler on the Browse search box
(`assets/js/browse.js:265`). Arriving with `?q=` in the URL fires no `input` event. So the
index never loads, and `browse.js:87` falls back to a plain AND-of-substrings over
title + summary + who_for + source.

Live proof, same URL, one keystroke apart:

```js
// https://.../browse.html?role=data-analyst&q=analyse%20this%20csv%20for%20me
// on arrival:
{ before_count: "0 resources for working with data", before_cards: 0, indexLoaded: false }
// then I type a space and delete it:
{ after_count: "6 resources for working with data...", after_cards: 6, indexLoaded: true,
  first3: ["Introducing the analysis tool in Claude.ai",
           "Introduction to Claude Analysis",
           "Claude Code for Data Analysis: Excel-Free Answers From CSVs"] }
```

Zero, then six. Same URL. The only difference is that I touched the box.

### 6.2 My three sentences

Reproduced with `python scripts/test-search.py` (the ranked path — what I get *only* if I
type into the Browse box) and with a script that reproduces `browse.js:87` exactly (the
fallback — what I get from the home page):

| what I typed | ranked (`test-search.py`) | from the home page box |
|---|---|---|
| `connect Claude to my postgres database` | **5** — top hit `Postgres MCP Pro`, score 62.9 | **0** |
| `will it get the numbers wrong` | **4** — top hit `How to Use Claude for CSV Data Analysis (The Honest Guide)`, score 42.0 | **0** |
| `analyse this csv for me` | **8** — top hit `Introducing the analysis tool in Claude.ai` | **0** |

The ranking, when it runs, is genuinely good. `will it get the numbers wrong` shares no
word with any of those titles and it still finds the right three. That is real work and
it is being thrown away by a load order.

### 6.3 It is not my phrasing. It is the site's own test suite.

`scripts/test-search.py` ships nine benchmark sentences that the author wrote to prove
search works. I ran all nine through the home-page fallback:

```
$ python - <<'PY'   # reproduces assets/js/browse.js:83-87
"help me write my thesis faster"           -> 0
"i keep getting generic answers"           -> 1
"how do i make claude read my pdfs"        -> 0
"where do i even start"                    -> 0
"stop claude inventing fake citations"     -> 0
"build an agent that uses my own tools"    -> 0
"teach my class to use ai honestly"        -> 0
"clean up a messy spreadsheet"             -> 0
"how do i build an mcp server"             -> 2
7 of 9 of the site's own benchmark sentences return 0 when typed on the home page
PY
```

Seven of nine. The site's own acceptance tests fail through its own front door.

### 6.4 The count line lies while it does it

`assets/js/browse.js:172-176` decides to write "N resources for `<role>`" when a role is
picked and no other **axis** is picked. It does not check `q`. So with a query active I
was shown:

> **0 resources for working with data**

Read that as an analyst arriving from the home page. It does not say "no match for your
sentence". It says the directory has nothing for people who work with data. There are 37.

---

## 7. On a phone

I did not resize the shared browser window — four other agents were working in it. I
loaded the live Browse page inside a 375px iframe in my own tab, which gives a genuine
narrow viewport to the media queries without touching anyone else's window.

```js
{ innerWidth: 372, mq768: true, horizontalOverflow: false,
  railHidden: "none", filterBar: {w:357, h:69},
  searchBox: {w:325,h:48}, sortSelect: {w:199,h:48} }
```

The layout is fine. No horizontal overflow. The filter rail is replaced by a pinned
"Filters" bar at the bottom. Touch targets are 48px, above the site's own 44px rule. That
is better than most sites and I will not pretend otherwise.

The problem is density, not layout:

```js
// role=data-analyst&level=builder  (all 7 of my builder cards)
cardHeights:   [539, 475, 399, 391, 416, 417, 365]
totalResultsPx: 3098
pageScrollH:   4230   viewportH: 809   ->  5.2 screens
```

The first card is 539px tall on an 809px screen. **One card is two-thirds of my phone.**
Seven cards — my entire top level — is 5.2 screens of thumb work. Each card repeats the
badge, title, source, three chips, a "For:" paragraph, a "Skip if:" paragraph, an
optional path line, and two date lines. On a desktop that density reads as care. On a
phone, with seven near-identical GitHub repos, it reads as seven identical grey walls.

At `never-used` the phone shows one 500px card and a bottom bar telling me to remove a
filter. That is the mobile experience for a data person who has never used Claude.

---

## 8. Content quality — the three worst entries I was shown, quoted

**Worst: `ClaudeR (R + RStudio MCP)`** — builder, tier `listed`.

> Skip if: **You don't use R.**

Sixteen characters. The title already says R. This card carries zero information beyond
its own title. The site's home page promises *"Every entry has a **Skip if:** line. A
link with no judgment is just a list, and lists are what made this hard in the first
place."* This is a list. Nobody opened it (`listed`), it has no publish date, and its one
piece of judgment is a tautology.

**Second: `Sales Analysis with Claude: Data Driven Sales Analytics`** — basic, tier
`listed`, Coursera, `subscription`.

> Skip if: **You want depth; it's shallow and requires a Claude Pro subscription.**

The site is telling me a resource is shallow and paid — and keeping it in my basic list
anyway, at tier "Found only", meaning nobody checked whether it is shallow. That
judgment came from somewhere other than reading it. Its hidden `notes` field adds
*"Does not visibly emphasize verification."* — for a course about sales numbers. Also
never shown.

**Third: `How to Use Claude for CSV Data Analysis (The Honest Guide)`** — confident.

> Skip if: **You want a named, established author or institution.**

Publisher shown: **"Pl"**. This is my top-ranked result for "will it get the numbers
wrong", which is the single most important question an analyst has. The site's answer is
an anonymous page on a `.edu.pl` domain, credited to a two-letter country code, with a
Skip line that amounts to "skip this if you have standards". Its own hidden note says
*"Lesser-known source but technically accurate on the two-modes trap — the core
correctness risk."* Which is the sentence that would have made me trust it. Hidden.

**Runner-up worth naming**: `CLAUDE CODE Full Course For Beginners (DATA DOMAIN Edition)`
is 6 hours 47 minutes long (from its own `notes`), sits at level `basic`, and is bucketed
as "several days". Its Skip line is one of the good ones — *"Skip if you only have one
evening"* — which is honest, and which means the site knows it is putting a 6h47m video
in front of a beginner.

---

## 9. Everything that is broken, ranked

### 9.1 The search box on the home page returns nothing, for almost any sentence

The only search field a first-time visitor sees is on the home page. It submits
`browse.html?q=…`. `assets/js/browse.js:265` loads the ranked index **only** inside the
`input` handler, so a `?q=` arrival never loads it and falls to the substring AND-match
at `browse.js:87`.

Evidence: live, `?role=data-analyst&q=analyse this csv for me` → `0 resources for working
with data`, `indexLoaded: false`. I typed one space and deleted it → `6 resources`,
`indexLoaded: true`, correct top hits. Same URL.

Breadth: all three of my sentences return 0. **7 of the 9 benchmark sentences in the
site's own `scripts/test-search.py` return 0** through this path. The good ranking exists,
is well built, and never runs for the people who use the obvious box.

### 9.2 The site sends me to a database connector nobody opened, and hides its own security warning

`resource.html?id=r-9878646d22`, `Postgres MCP Pro`. Tier `listed` — *"Nobody has looked
at the content yet."* Prerequisites: *"postgresql database credentials"*. Teaches:
*"install and configure postgres mcp pro with appropriate read/write permissions"*.

The record's `notes` field says: *"Use read-only/least-privilege role. Replaces the
archived, vulnerable @modelcontextprotocol/server-postgres."* That sentence is in
`data/items.json`, is shipped to my browser inside `data/items.js`, and is rendered
nowhere. `resource.js` never references `notes`. I checked:

```
$ grep -rn "notes" assets/js/ *.html | grep -v footer-note
assets/js/ui.js:49    tip: "We went through all of it, and a person checked the notes."
assets/js/ui.js:51    tip: "AI read all of it. No person has checked the notes yet."
how-we-check.html:70  We went through all of it and a person checked the notes.
how-we-check.html:74  AI read all of it. No person has checked the notes yet.
```

The only four hits for the word "notes" are badge tooltips telling me the notes were
checked. The notes themselves are unreachable. A page that talks about the notes it
will not show me is worse than a page with no notes.

### 9.3 42 KB of the best writing on the site is downloaded by every visitor and never displayed

```
$ python - <<'PY'
data-analyst items with a non-empty notes field: 34 of 37
"notes" key present in shipped items.js: True
bytes of notes text shipped and never rendered: 43271 (42.3 KB)
PY
```

What is in there, for my role alone:

- `Use Claude for Excel` — *"Notably lists 'audit-critical calculations without verification' as a non-use."*
- `Claude Code for Data Analysis: Excel-Free Answers From CSVs` — *"Cites Raymond Panko's spreadsheet-error research ('94% of spreadsheets have errors') to justify human checking."*
- `How I Use Claude Code as a Data Analyst (10 Real Use Cases)` — *"the description promotes the creators' paid community and consulting"*
- `Create Claude Skills for Data Tasks` — *"DataCamp content is quality but promotes its own platform."*
- `Reduce hallucinations` — *"The most important item for the 'silently incorrect analysis' failure mode."*
- `MotherDuck / DuckDB MCP Server` — *"latest release v1.0.7 (Jun 9, 2026)"*
- Every video's exact runtime: `6:47:47`, `1:58:34`, `58:36`, `46:29`, `24:52`, `9:58`, `7:58`, `7:10`.

Conflict-of-interest disclosures. Release dates on repos with no publish date. Exact
runtimes. The one sentence naming the correctness failure mode I care about. All written,
all shipped, all invisible. `data/items.js` is 610 KB raw / 174 KB gzipped and blocks
rendering on all four pages; 42 KB of it is dead weight.

### 9.4 The result count drops the query from its own sentence

`assets/js/browse.js:172-176`: `onlyRole` checks the five other filter axes and not `q`.
With a query active and a role picked I was shown, verbatim, **"0 resources for working
with data"**. There are 37. The sentence states a fact about the catalogue and it is
false. Combined with 9.1, this is what an analyst arriving from the home page actually
reads as their second screen.

### 9.5 Two generations of `Skip if:` writing, split by date, and my role got the old one

`Skip if:` is the site's entire pitch. It was rewritten and 22 of my 37 cards missed it.

```
$ python - <<'PY'
checked date -> n cards, median Skip-if length, how many <=40 chars
  2026-08-19  n=22  median= 38 chars  <=40 chars: 12
  2026-08-20  n= 2  median=115 chars  <=40 chars: 0
  2026-08-21  n= 3  median=169 chars  <=40 chars: 0
  2026-08-22  n=10  median=127 chars  <=40 chars: 0
PY
```

The old batch, verbatim: *"You don't use R."* / *"You don't use Excel."* /
*"You don't use Tableau."* / *"You don't use PostgreSQL."* / *"You are not using
Skills."* / *"You don't use DuckDB or a warehouse."* — six tautologies that restate the
title.

The new batch, verbatim: *"Skip if you only have one evening. At 6:47 it needs a real
schedule, and a shorter course will teach you the same basics faster."* — a real
judgment, with a reason.

Same site. Same feature. Three days apart. **Twelve of my 37 cards have a `Skip if:` of
40 characters or fewer.** The rewrite is good; it just never reached the 19 August batch,
which is 59% of everything I am shown.

### 9.6 My top level is seven GitHub links, four of which nobody opened

```
$ python docs/attack/role-view.py data-analyst builder
builder formats: {'repo': 7}          <- all seven
builder tiers:   {'listed': 4, 'previewed': 3}
builder with a publish date: 0 of 7
builder skip_if lengths: [16, 22, 25, 28, 36, 54, 163]
```

Seven cards. Seven repos. Zero teaching material. Four at *"Nobody has looked at the
content yet."* Five with a Skip line under 40 characters. This is a bookmark folder with
a badge on it. (The "0 reviewed site-wide" and "no publish date" facts are already known;
what is new is that they concentrate at 100% in one role's top level.)

### 9.7 My one never-used card advertises a path that excludes me, and Paths never says so

`Claude 101` shows *"Step 3 of 6 in Your first week with Claude"* on the card and
*"This is step 3 of 6 in Your first week with Claude. The order matters — the path says
why."* on the resource page. That path's `roles` are
`['non-technical','student','teacher','business-founder']`. `Reduce hallucinations` does
the same thing with the research path (`['researcher','student']`).

`assets/js/paths.js` reads `LC.param("id")` and nothing else. `paths.html?role=data-analyst`
renders all three paths and never prints a `roles` list, so there is no way to tell from
the page that a path is not for me. Live check: the words "analyst" and "working with
data" appear zero times on that page.

Net effect: the site invites me into other people's routes without telling me, and
offers no acknowledgement anywhere that mine does not exist.

### 9.8 It cannot count to one

`"1 resource match so far."` (`home.js:209` + `ui.js:113`) and
`"Browse 1 Claude resources — Learn Claude"` (`browse.js:215`, no singular case).
Both confirmed live. `data-analyst` at `never-used` is one of only two role/level answers
in the whole site where a visitor sees this, so it reads as a bug aimed at me personally.

### 9.9 At one result the advice is to un-answer the question the site just asked

`browse.js:178` appends `". Remove a filter to see more."` whenever `0 < n <= 6` and any
filter is set. With role + level that is exactly the two answers the home page demanded.
There is a good empty-state string sitting unused two lines away —
*"We have not covered this role yet. It's on the list."* (`browse.js:198`) — that only
fires at zero.

### 9.10 There is no way to say which kind of data person I am

Ten of my 37 assume Excel, twelve assume Python or a notebook, five assume SQL or a
warehouse or Tableau, one assumes R. The `who_for` lines make the distinction precisely.
The filter axes (`browse.js:17-24`) do not carry it, and the `Topic` list has no entry
for a tool. The information exists; it is not filterable. So an Excel analyst reads 37
cards to find 10.

### 9.11 Publisher names are domain fragments

`source: "Pl"` for `qwe.edu.pl`; `source: "Finance"` for `vincent.codes.finance`. Both
appear in my list. The resource page renders these as **"Open on Pl"** and
**"Found through Pl"**. Site-wide the same fault produces `Au`, `To`, `Vc`, `Ac`, `Eu`,
`Gov`, `Ed`, `Jhu`, `Syr`, `Kit`, `World`, `Cloud`, `bri`. On a directory whose value is
"we judged the source", a source called "Pl" is self-defeating.

### 9.12 Two filter chips are dead ends for my role

`podcast` (0 items) and `pay once` (0 items), out of 27 non-role chips. Clicking either
gives *"Nothing matches all of those. Try removing one filter — time is usually the one
to loosen."* — which names the wrong axis.

### 9.13 Exact runtimes exist and are thrown away for four buckets

The `time` chips are "15 minutes", "one hour", "a half day", "several days". Twenty of my
37 sit in "one hour". The `notes` field holds the real numbers — `24:52`, `46:29`,
`58:36` are all "one hour". I have an hour. The difference between 25 minutes and 59
minutes decides what I do with it, and the site has both numbers and shows neither.

---

## 10. The one thing that would make me leave and not come back

I type my question into the box on the front page, because that is what the box is for,
and the site tells me there are **0 resources for working with data**.

Not "no match for that sentence". Not "try shorter words". A flat statement that the
directory has nothing for me. There are 37, and the correct six were one keystroke away.

I would close the tab and never learn that typing into a *different* box on the *next*
page would have worked. Nobody debugs a directory. They leave.

Everything else on this list I would have forgiven if the first thing I typed had
returned something.

---

## 11. What is genuinely good                          (be honest, but brief)

- **The ranked search is real work and it is good.** `will it get the numbers wrong`
  finds `How to Use Claude for CSV Data Analysis (The Honest Guide)` and
  `Introducing the analysis tool in Claude.ai` without sharing a single word with either
  title. That is the hardest thing on the site and it was done well. It is being wasted,
  not missing.
- **The new `Skip if:` lines are the best thing here.** *"Skip if you want polished
  production and tight editing. The delivery is live and repeats itself, so two hours
  holds about ninety minutes of content."* Nobody else on the internet writes that
  sentence. Fifteen of my 37 have one this good.
- **The tier badges do not flatter.** "Found only — nobody has looked at the content yet"
  is a genuinely uncomfortable thing to print, and it is printed. I trusted the site more
  for it, even while it was showing me four of them in a row.
- **`free-account` is labelled "free, sign-up needed"** rather than rounded up to free.
  Small, and it is the kind of small that says someone cared.
- **The phone layout is competent.** 48px targets, no horizontal overflow, a bottom
  filter bar where a thumb is. It seems better thought through than the desktop density.
- **The two docs entries are the right two.** `Reduce hallucinations` and
  `Use Claude for Excel` are exactly what an analyst should read first. There should be
  twenty more like them and instead there are eight GitHub repos.

---

## Checklist — every line ticked or the file is not finished
- [x] I opened the live site — my own Chrome tab (1973161671, created and closed by me),
      plus `curl` against `https://mojtaba-alehosseini.github.io/learn-claude/`. Confirmed
      the deployed `browse.js`, `home.js` and `paths.js` are byte-identical to the repo
      (`diff` against files fetched from the live host).
- [x] I tried all four levels — 1 / 17 / 12 / 7, read off the live tally line by clicking
      the real chips, and matching `00-facts.md` exactly.
- [x] I quoted at least 5 real titles or lines from the site — `Claude 101`,
      `Postgres MCP Pro (crystaldba/postgres-mcp)`, `ClaudeR (R + RStudio MCP)`,
      `Tableau MCP (official)`, `MotherDuck / DuckDB MCP Server`,
      `How to Use Claude for CSV Data Analysis (The Honest Guide)`,
      `Sales Analysis with Claude: Data Driven Sales Analytics`,
      `CLAUDE CODE Full Course For Beginners (DATA DOMAIN Edition)`, plus verbatim
      `Skip if:` lines, the live tally strings, and the how-we-check promise.
- [x] Every number I used is in 00-facts.md or I show the command — `role-view.py`,
      `scripts/test-search.py`, the `browse.js:87` fallback reproduction, `curl -sI`,
      `grep -rn "notes"`, and live `javascript_tool` reads.
- [x] I looked at a phone width — 372px viewport in an iframe (the shared browser window
      was left alone because four other agents were using it): no overflow, 48px targets,
      first card 539px of an 809px screen, 5.2 screens to scroll my seven builder cards.
- [x] I found at least one thing nobody has mentioned before — several. The biggest three:
      the home-page search box never loads the ranked index so 7 of the site's own 9
      benchmark sentences return zero (9.1); 42.3 KB of `notes` — including the
      *"use read-only/least-privilege role"* warning on a database connector — is shipped
      to every browser and rendered nowhere (9.2, 9.3); and `Skip if:` exists in two
      generations split cleanly on the `checked` date, with 22 of my 37 cards stuck on the
      old tautological one (9.5).
