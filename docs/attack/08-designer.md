# Attack: a designer
Written as someone who is a designer, at 2026-08-27. Site version: 22e4532.

Known before I started, so one line and no more: designers get 29 resources, the fewest
of any role; one of them is for a person who has never used Claude; there is no path.
Everything below is what sits under that.

Method note up front. Four other agents shared the browser window. Every attempt to
resize it to phone width failed — `resize_window` reported success and `innerWidth`
stayed 1536, twice. So the phone pass in section 7 was measured a different way: I
loaded `browse.html` into a 390x844 same-origin iframe inside my own tab and measured
the real layout inside it, with the media query at 390px and `.filter-rail` computed to
`display:none`. Those numbers are real. I say so where I use them.

---

## 1. The first 60 seconds

The page loads. The largest thing on it is a drawing of a coffee mug, 440x440.

I pick "a designer". The mug becomes a **paintbrush**. Not a cursor, not an artboard,
not a frame, not a pen tool. A decorator's paintbrush, the kind you buy to do a hallway.
That is what this site thinks I do. I have not opened Figma with a paintbrush in my
life. At `built things with it` the same brush gets a drip of paint added to it.

Measured on the live home page at 1536x730 (`getBoundingClientRect`, JS in page):

| element | size | share of viewport |
|---|---|---|
| hero art (`.hero-art`) | 440 x 440 at (936,194) | **17.3%** |
| the answer line (`p.display`) | 716 x 150, 68px Tiempos | 8.6% |
| "3 resources match so far" | 716 x 24, **16px**, `rgb(108,107,102)` | 1.5% |

The paintbrush has **11.3x the pixel area of the only number on the page**. The number is
the whole product. The brush is decoration.

And the typography is upside down. The `<h1>` of the home page is:

```
H1  16px / 400  ::  Find what's worth your time.
H2  16px / 500  ::  Who are you?
H2  16px / 500  ::  How much Claude do you know?
```

The 68px sentence I actually read — "I'm a designer and I've never used Claude." — is a
`<p class="display">`. The document heading is the smallest text in the hero. A designer
notices this in the first ten seconds, because it is the same mistake as styling a
caption to look like a title and shipping it.

One more thing, in the first minute, on the site's own front door:

> **1 resource match so far.**

"1 resource match". Not "matches". The count line is generated, so this is not a typo in
a data file — it is the copy shipping without a singular case. It is the first sentence
of English the site writes about me and it is wrong.

---

## 2. Does the front door work for me (all four levels, with counts)

I clicked all four on the live site and read the count line each time. Matches
`00-facts.md` exactly.

| I say I've… | live count line | 00-facts |
|---|---|---|
| never used Claude | "1 resource match so far." | 1 |
| used it a little | "8 resources match so far." | 8 |
| used it a lot | "17 resources match so far." | 17 |
| built things with it | "3 resources match so far." | 3 |

Also verified with `python docs/attack/role-view.py designer --counts`:

```
designer: 29 total
  never-used     1
  basic          8
  confident     17
  builder        3
  tiers:   {'ai-reviewed': 8, 'previewed': 21}
  formats: {'docs': 5, 'article': 13, 'video': 4, 'course': 2, 'repo': 3, 'podcast': 2}
  free:    22
  no date: 22
  only this role: 22
```

**The shape of that curve is the finding, not the total.** 17 of 29 sit at "used it a
lot". The site's own front door asks how much Claude I know, and then rewards the
answer "a lot" with six times more than the answer "never". A directory built to help
people start has put 59% of my shelf behind a door marked *already competent*.

Why the curve looks like that:

```
$ python -c "... 'designer' in roles ..."   (full command in section 9.2)
total designer 29
title says Claude Code: 14
title says Claude Design: 7
topics histogram: [('claude-code', 22), ('mcp', 12), ('chat-prompting', 10), ...]
by level, claude-code in title or summary:
  never-used  1  -> 0
  basic       8  -> 4
  confident  17  -> 13
  builder     3  -> 1
```

**22 of my 29 resources are tagged `claude-code`.** Claude Code is a terminal. The
site's answer to "I am a designer" is, in four cases out of five, "open a command line".
That is the whole explanation of the confident-heavy curve: the catalogue is not
designer-shaped, it is developer-shaped with a designer label on it, and command-line
work needs you to already be confident.

And the never-used door. One card. Section 8 takes it apart.

---

## 3. What the catalogue actually gives me (are these really for me?)

**hands-on: 0.** That is the number I would put on a poster.

Formats for a designer: article 13, docs 5, video 4, repo 3, course 2, podcast 2,
**hands-on 0** (`00-facts.md`). Eighteen of twenty-nine are things to read. My job is
making. This site's response to a maker is a reading list.

Compare: `data-analyst` gets 4 hands-on out of 37, `developer` 1 of 94, `researcher` 1
of 41 (`00-facts.md`). Nobody gets many. But a designer gets **zero**, and a designer is
the one role whose entire craft is "do it and look at it". Handing me 13 articles about
design is the exact failure mode we complain about in our own onboarding docs.

Then, are these actually mine? Three are not, and the site says so in its own words:

- **"Introduction to Claude Cowork"** — position 8 of 8 in my `basic` list.
  Who it's for: *"Owners and ops people who want Claude to do real multi-step work, not
  just chat."* Not designers. Not even close.
- **"Claude Code for Product Managers with Sachin Rekhi"** — position 7 of 17 in
  `confident`. Who it's for: *"Experienced product managers who want the strategic case
  for AI in product work from credible practitioners."*
- **"Claude Code for Product Managers (Maven, Aman Khan and Eric Xiao)"** — position 8
  of 17. Who it's for: *"A PM who learns best live…"*

Two consecutive cards in the middle of my best-populated level are titled *for Product
Managers* and their own "For:" line names a PM. The site tagged them `designer` and then
printed a description that tells me they are not. 3 of 29 — over 10% of my shelf — are
openly addressed to somebody else. Not a judgment call: the site's own copy says it.

What is genuinely designer-shaped is narrow: Figma MCP setup (4 titles say Figma),
Claude Design onboarding (7 titles), design systems as skills, UX writing. That is four
subjects. Four subjects is a blog category, not a directory.

Nothing in the 29 answers the question every designer I know is actually asking. See 6.

---

## 4. Paths

There is no path for a designer. Known. Here is what is not known.

I opened `https://mojtaba-alehosseini.github.io/learn-claude/paths.html?role=designer`.

I got three paths. All three. Unfiltered. Identical to `paths.html` with no query at
all. Under the heading: *"A short list, in order. Start at the top."*

- **Your first week with Claude** — "Anyone who has just opened Claude and does not know
  what to do next."
- **Getting good at Claude Code** — "Developers who have installed Claude Code…"
- **Using Claude for research without embarrassing yourself** — "Researchers and
  academics…"

Nothing on that page tells me none of them are mine. The first one says *"Anyone"*. I am
anyone. I would start it, and I would be in the wrong place.

The reason:

```
$ grep -n "role" assets/js/paths.js paths.html
(no output)
```

Zero occurrences of the word `role` in the Paths page or its script. The `?role=`
parameter is accepted by the URL and thrown away.

Now the part that stings:

```
$ python -c "... data/paths.json ..."
first-week          |roles= ['non-technical','student','teacher','business-founder'] | Your first week with Claude
claude-code-start   |roles= ['developer']                                            | Getting good at Claude Code
research-with-claude|roles= ['researcher','student']                                 | Using Claude for research…

$ grep -rn "roles" assets/js/*.js | grep -i path
(no output)
```

**Every path in the data already carries a `roles` array. No JavaScript on the site ever
reads it.** The sentence "There is no path for a designer yet" is one `if` statement
away and the data for it has been sitting in `paths.json` the whole time. Instead the
page shows me three doors and lets me find out the hard way.

Silence would be better. Three paths that all say "Anyone / Developers / Researchers"
with no explanation is the site actively wasting my time, which is the one thing it
promises not to do.

---

## 5. The card and the resource page

### The card puts the rejection above the recommendation

Measured on the live browse card (JS, `getComputedStyle`):

| part | size | face | weight | colour |
|---|---|---|---|---|
| `.card-title` | 24px / 31.2px | Tiempos | 600 | `rgb(20,20,19)` |
| `.card-skip` — "Skip if: …" | **20px / 28px** | **Tiempos** | 400 | `rgb(20,20,19)` |
| "For: …" | **16px / 24px** | **Styrene** | 400 | `rgb(108,107,102)` |
| `.badge` / `.chip` | 12px / 16.8px | Styrene | 500 / 400 | `rgb(108,107,102)` |

Read that again. The reason **not** to open a resource is set 4px larger, in the display
serif, in full-strength black. The reason **to** open it is 4px smaller, in the UI sans,
in grey. On every card, at every level, the second-loudest voice is the rejection.

Live example, top card of my `confident` list:

> **Claude Code and Figma: Set up the MCP server**
> For: UX/UI and design-system designers who want Claude Code to read and write Figma files.
> **Skip if: You don't use Figma.**

Scan that page as a designer and the vertical rhythm is: title, title, title, and a
column of black serif sentences all starting with the word **Skip**. Skimming 17 cards
reads as being turned away 17 times. The editorial idea — "we tell you when to skip" —
is the best thing about this site (see 11) and the typography has turned it into the
site's dominant emotional tone. That is a design error, not an editorial one.

The grey used for "For:" is `rgb(108,107,102)` on `rgb(240,238,230)`. WCAG relative
luminance gives **4.60:1**. AA for body text is 4.50. The most useful line on the card
clears the legal minimum by a tenth of a point, while the line telling me to go away is
at full contrast.

The card title is a `<div class="card-title">`. Not `<h3>`, not `<h2>`. The browse page
heading outline is `H1 Browse`, then `H2 Filters`, then six `H3` filter groups — and
then 17 results with no heading at all. There is no way to move through the results by
heading.

### The resource page

I opened `resource.html?id=r-1cab275cb5` — my one never-used card.

**The time chip says "one hour".**

The site's own `notes` field for that record says: `"14K views, 15:50, verified
2026-08-22"`. It is a **sixteen minute video**. The page tells me it will cost me an
hour.

Source of the lie, `assets/js/ui.js:29`:

```js
"under-15min": "15 minutes", "under-1hr": "one hour",
"half-day": "a half day", "multi-day": "several days"
```

Every bucket is an upper bound and every label is printed as a flat figure. `under-1hr`
— meaning *less than an hour* — renders as **"one hour"**.

How much of my shelf this ruins:

```
$ python -c "... Counter(i['time'] for i in designer_items) ..."
designer time buckets: Counter({'under-1hr': 18, 'under-15min': 10, 'multi-day': 1})
  under-1hr but notes say '31:58' :: Claude Design: The Complete Guide
  under-1hr but notes say '15:50' :: Claude Design Tutorial for Designers | First Look…
  under-1hr but notes say '1:00'  :: Claude Code for Product Managers with Sachin Rekhi
```

**18 of my 29 resources are labelled "one hour".** The site holds exact runtimes for
three of them: 15:50, 31:58, 1:00. Two of the three are nowhere near an hour, and all
three get the same word. I have one hour. This site's headline is *"Find what's worth
your time."* It then tells me that 62% of everything available to me costs my entire
hour, and it is wrong about that most of the time.

**The primary button.** 445 x 52px, filled orange, reading:

> **Open on Nehmat Gereige | AI-Design Professor**

`href` is `https://www.youtube.com/watch?v=o7HSVPHCX8I`. The word YouTube is nowhere on
the page. The biggest, loudest, most-clicked control on the page uses a person's
self-chosen channel name — with a pipe character in it — as the destination. A pipe
character inside a button label. I would not ship that in a prototype.

Also: the footer of that page says *"Found through Nehmat Gereige | AI-Design
Professor"*. The source is the author. It says the video was found through the person
who made it.

Finally, the label is `Skip if:` on the card and `Skip it if` as the heading on the
resource page. Same field, two different names, two pages apart.

---

## 6. Search, in my words

I ran three real sentences. I ran each one twice: once by arriving at a `?q=` URL the
way the home page sends you, and once by typing it into the search field.

| my sentence | arriving via `?q=` URL | typed into the field |
|---|---|---|
| generate UI mockups from a description | **0 resources** | **17** |
| does it understand figma | **0 resources** | **16** |
| will this replace me | **0 resources** | **4** |

Live evidence for the first one — `browse.html?q=generate+UI+mockups+from+a+description`:

> **0 resources**
> **No match for "generate UI mockups from a description".**
> Try fewer words, or browse by role instead.

`window.LCSearch.ready()` returned `false`. I then typed one character into the field
and the same page rendered **17 cards**, top hit *"Claude Design: The Complete Guide"*.

The cause, in the shipped code:

- `assets/js/browse.js:47` — `q = p.get("q") || "";` reads the query out of the URL.
- `assets/js/browse.js:263` — the index load is triggered **only inside the input event
  handler** (`q = e.target.value` at line 257).
- `assets/js/browse.js:86` — *"Until the index has loaded, fall back to plain substring
  so typing is never dead."*

So a query that arrives in the URL is matched by raw substring against titles. No
sentence survives that. And `assets/js/home.js:305`:

```js
location.href = "browse.html" + (p.toString() ? "?" + p.toString() : "");
```

**The home page's own "Or describe what you want to do…" box builds exactly the URL that
returns zero.** The site invites me to type a sentence, then routes that sentence into
the one code path that cannot answer it, then blames me: *"Try fewer words."* The words
were fine. There were 17 matches.

Reproduced offline, identical ranking:

```
$ python scripts/test-search.py "generate UI mockups from a description"
"generate UI mockups from a description"   17 result(s)
     40.3  [designer,non-technical] Claude Design: The Complete Guide
     34.1  [designer              ] Building AI-driven workflows powered by Claude Code and
     28.9  [designer              ] Using Claude Design for prototypes and UX
```

The search itself is good. Typed, it is the best thing here. It is wired to the front
door backwards.

**Third sentence, separately.** "will this replace me" returns 4 results and none of
them are about that:

```
$ python scripts/test-search.py "will this replace me"
     23.9  [designer    ] How to Use Claude Code for UX Writing
     22.4  [data-analyst] Claude Code for Data Analysis: Excel-Free Answers From CSVs
     22.4  [pm          ] Claude Code for Product Managers
```

A designer asks whether the tool takes their job and gets an article about reading CSVs
in a terminal. Searching every field of all 29 designer records for
`replace|job|career|redundan|displace|obsolete|threat` returns **1 record**, and that one
is a UX-writing tutorial. The single most common question a designer has about AI in
2026 has no answer anywhere in my 29.

---

## 7. On a phone

Measured at 390x844 inside a same-origin iframe (media query live, `.filter-rail`
computed `display:none`, `innerWidth` 390). Method explained at the top.

| measurement | value | the site's own standard |
|---|---|---|
| card title measure | **23 characters per line** (20px Tiempos) | 45 cpl floor |
| card body / "Skip if:" measure | **34 cpl** (18px Tiempos) | 45 cpl floor |
| top of the first card | **538px** down an 844px screen | — |
| first screen that is not a result | **64%** | — |
| document height, 17 cards | **8,775px** | — |
| average height per card | **485px** | — |
| screens to reach card 17 | **10.4** | — |

**23 characters per line.** That is a newspaper column rule broken in half. "From Claude
Code to Figma: Turning Production Code into Editable Figma Designs" is 77 characters. At
23 cpl that is four lines of ragged serif before I learn anything. Every card title on
the phone is a poem.

The title measure is 246px inside a 343px card — the format icon in the top-right corner
takes a column off every title, on the width where there is no width to give.

**64% of my first phone screen is chrome.** Header, the word "Browse" set at display
size, a search field, a Sort dropdown that gets a full row of its own, two filter chips,
and "17 resources". Then, at the very bottom edge, the top of card one. I have to scroll
before I see a single thing I came for. On a device where the fold is the whole product.

To reach the last of my 17 results I scroll **8,775px** — over ten full screens — of
485px cards, each one ending in a black serif sentence telling me to skip it.

For balance, two mobile bugs that the 2026-08-24 audit found are now fixed in the CSS I
read: the fixed bottom bar no longer covers the footer's last line
(`body:has(.mobile-filter-bar) .site-footer .wrap { padding-bottom: var(--space-100) }`)
and footer links now have `min-height: 44px`. Credit where it is due.

---

## 8. Content quality — the three worst entries I was shown, quoted

### 8.1 The one door for a designer who has never used Claude

The entire never-used level, in full:

> **Claude Design Tutorial for Designers | First Look + Full Walkthrough!**
> Nehmat Gereige | AI-Design Professor · video · **one hour** · free · checked 2026-08-22 · published 2026-04-18
> For: Designers who want an unvarnished first impression from someone who teaches design, before committing time to learning the tool.
> **Skip if: Skip if you want a clean reference tutorial - this is exploratory and occasionally meanders. Recorded at launch, so some rough edges shown have since been fixed.**

Take that apart:

- It is the **only** thing behind the never-used door. There is no second option, so
  "Skip if" is not advice, it is an eviction. If I skip it I have nothing.
- Its own note says the tool has changed since it was filmed: *"Recorded at launch, so
  some rough edges shown have since been fixed."* Published 2026-04-18. That is over
  four months of a fast-moving product ago, and the site says so, and still offers it as
  the only front door.
- Its own note says it **"occasionally meanders"**. So the single entry point for every
  designer on earth who has never used Claude is an unrehearsed, out-of-date video that
  wanders.
- The `Skip if` begins **"Skip if you want…"** on a card whose label already reads
  **"Skip if:"**. The rendered line is *"Skip if: Skip if you want a clean reference
  tutorial"*. The word is printed twice, in two typefaces.
- It is labelled **"one hour"**. It is 15:50 (see 5).
- Tier: **Skimmed** — *"We read the outline or a free sample. We have not seen the whole
  thing."* Nobody at this site has watched the only video they offer a beginner.

That card is not a recommendation. It is an apology with a link on it.

### 8.2 A sold-out course, for a different job, that already started

> **Claude Code for Product Managers (Maven, Aman Khan and Eric Xiao)** — position 8 of 17 in my `confident` list
> Maven · course · multi-day · paid-once · checked 2026-08-21 · published UNVERIFIED
> For: **A PM** who learns best live, with office hours three times a week and a peer cohort…
> Skip if: **You need it now or you need a price — the cohort was sold out on 2026-08-21 with no price shown, only a waitlist.** The sales page is also almost entirely testimonial quotes, several of which lean on replacing colleagues, which is worth reading sceptically.

And in the record's own `notes`, not shown to me anywhere on the site:

> *"Sold out on 2026-08-21; price not displayed. … Listed schedule showed Week 1 starting
> 10 August 2026, so a past cohort."*

The site knows this course is **for product managers**, **sold out**, **price unknown**,
and **already finished**. It shows it to me anyway, in the top half of my largest level.
It is also the only `multi-day` item in my entire 29. Four disqualifying facts, all of
them written down in the record, and it still ships.

### 8.3 A card that tells me to read something I am not allowed to see

> **Kris Puckett - Becoming an AI-native designer (Dive Club)**
> Dive Club / Ridd · podcast · **under-1hr** · free · **published 2026-03-02**
> Skip if: **"You have already read the Cat Wu article — the video covers the same ground, and I could not confirm its runtime or publication date."**

Two separate failures in one sentence.

**One.** *"I could not confirm its runtime or publication date."* The card, in the same
breath, prints a runtime (**one hour**) and a publication date (**2026-03-02**). The
site displays two facts it admits on the same line it could not verify. That is not a
missing date — that is a stated date next to a written confession that the date is
unknown.

**Two.** The "Cat Wu article" it tells me to compare against is
*"Product management on the AI exponential"*:

```
$ python -c "... find 'Cat Wu' in items.json ..."
Product management on the AI exponential | ['pm'] | confident | article
```

**`roles: ['pm']`.** It is not in my 29. It is not in my browse list at any level. The
card's skip advice hinges on a resource a designer cannot see, cannot find by filter,
and is never told exists. The advice is unusable by the person it is shown to.

---

## 9. Everything that is broken, ranked

Ranked by what it costs me, a designer with one hour, not by how hard it is to fix.

**9.1 — The home page's own search box routes every sentence into zero results.**
Type "generate UI mockups from a description" into the box on the front page, press Show
me, and the site says *"0 resources. No match … Try fewer words."* The same query typed
into the browse field returns **17**. Verified live three times: 0 / 0 / 0 by URL versus
17 / 16 / 4 typed. Cause: `browse.js:47` reads `?q=`, but the search index only loads
from the input handler at `browse.js:263`; `home.js:305` builds that exact URL. Evidence
in section 6. This is the single worst bug on the site. It breaks the front door's most
inviting feature and then tells the visitor they asked badly.

**9.2 — 22 of 29 designer resources are about a command-line tool.**
```
$ python -c "
import json,re
items=json.load(open('data/items.json',encoding='utf-8'))
d=[i for i in items if 'designer' in i.get('roles',[])]
from collections import Counter
c=Counter()
for i in d:
    for t in i.get('topics',[]): c[t]+=1
print(len(d), Counter({k:v for k,v in c.items()}))
print('titles with Claude Code:', len([i for i in d if re.search(r'claude code',i['title'],re.I)]))
"
29 Counter({'claude-code': 22, 'mcp': 12, 'chat-prompting': 10, 'skills': 9, 'agents': 4, 'cowork': 3})
titles with Claude Code: 14
```
`claude-code` on 22 of 29; 14 of 29 titles say the words. This is why 17 of 29 sit at
`confident` and one sits at `never-used`. The role is not thin because designer content
is scarce — it is thin because the shelf was filled from the developer shelf.

**9.3 — Every time label is an upper bound printed as a fact.**
`assets/js/ui.js:29` maps `under-1hr` to the string **"one hour"**. 18 of my 29 carry
that label, including a 15:50 video whose exact runtime is recorded in the site's own
`notes` field. On a site headlined "Find what's worth your time", 62% of my catalogue
reports a time cost that is wrong, and always wrong in the direction that makes me not
click. Evidence in section 5.

**9.4 — The Paths page has the data to tell me I am excluded and throws it away.**
`grep -n "role" assets/js/paths.js paths.html` → no output. `data/paths.json` carries a
`roles` array on all three paths. `grep -rn "roles" assets/js/*.js | grep -i path` → no
output. So `paths.html?role=designer` silently shows me three paths, the first of which
says *"Anyone who has just opened Claude"*, and never says that none of them include me.
Evidence in section 4.

**9.5 — Every resource link on this site previews as "Resource — Learn Claude".**
```
$ curl -s ".../resource.html?id=r-1cab275cb5" | grep -iE "<title>|og:"
<title>Resource — Learn Claude</title>
<meta property="og:title" content="Resource — Learn Claude">
<meta property="og:description" content="What this resource teaches, who it is for, who should skip it, and how thoroughly we checked it.">

$ curl -s ".../resource.html?id=r-1cab275cb5" | grep -ci "og:image"   → 0
$ curl -s ".../resource.html?id=r-1cab275cb5" | grep -ci "noscript"   → 0
$ curl -s -o /dev/null -w "%{http_code} %{size_download}" ".../browse.html?role=designer"
200 4189
$ curl -s ".../browse.html?role=designer" | grep -c "designer"        → 0
```
All 353 resource pages ship one identical `og:title`, one identical description, **zero
`og:image`**, and **zero `<noscript>`**. `browse.html?role=designer` is served as 4,189
bytes of HTML in which the word "designer" occurs **zero times**.

I share links all day — into Slack, into Figma comments, into a design-team channel.
Every link from this site arrives as a grey rectangle saying "Resource — Learn Claude".
A directory's only growth engine is people passing links around, and this one has
disabled the preview on every page it owns. Nobody has raised this.

**9.6 — The card typography promotes the rejection over the recommendation.**
`.card-skip` is 20px Tiempos at full black. The "For:" line is 16px Styrene at
`rgb(108,107,102)` — **4.60:1** contrast, one tenth of a point over the AA floor. The
second-loudest element on every card is the sentence telling me to leave. Numbers in
section 5.

**9.7 — hands-on: 0.** Thirteen of my twenty-nine are articles. Zero are things I do.
For the one role on this site whose craft is entirely making, that is the wrong medium
end to end (`00-facts.md`).

**9.8 — Three of my 29 cards name a different job in their own "For:" line.**
"Introduction to Claude Cowork" (*"Owners and ops people…"*), "Claude Code for Product
Managers with Sachin Rekhi" (*"Experienced product managers…"*), "Claude Code for
Product Managers (Maven…)" (*"A PM who learns best live…"*). The last two are adjacent,
at positions 7 and 8 of my 17-card `confident` list. Section 3.

**9.9 — A `Skip if:` cross-references a resource this role cannot reach.**
The Dive Club podcast tells me to skip it if I have read "the Cat Wu article". That
article is `roles: ['pm']`. It is invisible at every designer filter. Section 8.3.

**9.10 — A card prints a runtime and a date on the same line as its own admission that
neither could be confirmed.** Same card. "under-1hr" and "published 2026-03-02" beside
*"I could not confirm its runtime or publication date."* Section 8.3.

**9.11 — On a phone, card titles wrap at 23 characters per line and 64% of the first
screen is not a result.** Measured at 390x844: title measure 23 cpl, body 34 cpl, first
card top at 538px of 844, document 8,775px for 17 cards. The 2026-08-24 audit set the
site's own floor at 45 cpl and measured the desktop browse card at 92.7 cpl — so the
same component is 2x too wide on a laptop and 2x too narrow on a phone. Section 7.

**9.12 — The `<h1>` of the home page is 16px; the 68px line is a `<p>`.**
Heading outline read live: `H1 16px :: Find what's worth your time.` The browse page
gives its 17 results no heading at all — card titles are `<div class="card-title">`.
Section 1 and 5.

**9.13 — "1 resource match so far."** No singular case in the count copy. Live on the
home page whenever a designer picks "never used Claude" — which is every designer who
has never used Claude, on the first screen they see.

**9.14 — The primary CTA is 445px of orange reading "Open on Nehmat Gereige | AI-Design
Professor" and links to YouTube.** A pipe character inside a button label. The
destination platform is never named. Section 5.

**9.15 — 290,766 bytes of PNG to draw 28px checkboxes.**
Measured on a cold load of `browse.html` via `performance.getEntriesByType('resource')`:
13 PNG requests, **290,766 bytes**. Each role icon fetches at **1024x1024, 23,573
bytes**, and `.filter-icon` renders it at **28x28** — a 36x downscale. The icon path
embeds the selected level, so every level change asks for ten new files. Worse than the
weight: at 28px these detailed line drawings collapse. In my own screenshot of the rail,
"a student" is a featureless grey lozenge and "a developer" and "a teacher" are the same
rectangle. Beautiful 1024px art, unreadable at the only size anyone sees it.

**9.16 — 22 of my 29 have no publish date.** Site-wide it is 171 of 353, which is
already known. For a designer it is **22 of 29 — 76%**, against a 48% site average
(`role-view.py designer --counts`: `no date: 22`). The thinnest role is also the least
dated. In a field where a four-month-old screenshot is wrong, three quarters of my shelf
will not tell me when it was made.

---

## 10. The one thing that would make me leave and not come back

I type what I want into the box on the front page — the box the site puts there, under
the words *"Or describe what you want to do…"* — and the site tells me there is nothing.

> **0 resources**
> **No match for "generate UI mockups from a description".**
> Try fewer words, or browse by role instead.

There are seventeen. The site has them. It ranked them correctly in 40 milliseconds the
moment I touched a key. It just never loads the index for a query that arrives in the
URL, which is the only way its own front door ever sends one.

I would not know that. I would read "No match" and conclude that a directory of 353
Claude resources has nothing about generating UI from a description, which is the single
most obvious thing a designer would ask an AI directory. Then I would close the tab and
tell one other designer it was empty.

Everything else here is repairable and some of it is good. This one converts the best
feature into proof that the site is useless, at the exact moment a new visitor is
deciding.

---

## 11. What is genuinely good (be honest, but brief)

- **`Skip if:` is the best editorial idea I have seen in a directory.** Every other list
  tells you why to click. This one tells you when not to. *"You don't use Figma."*
  *"You're on an enterprise-locked setup or uneasy giving an LLM browser access."* That
  is real judgment, and it is the whole reason the site deserves to exist. It is only
  the typography that has turned it into the loudest thing on the page.
- **The honesty is unusual and I want to say so.** "Skimmed. We read the outline or a
  free sample. We have not seen the whole thing." A note admitting a course was sold
  out with no price. A note warning that testimonials "lean on replacing colleagues,
  which is worth reading sceptically". Most directories would have quietly taken the
  affiliate link.
- **The search, when you type into it, is very good.** "does it understand figma" →
  "Guide to the Figma MCP server" first. Sentences work. No API, no key, static file.
  That seems like the hardest thing here and it is the thing that works best.
- **The answer sentence on the home page is a genuinely nice piece of interaction
  writing.** "I'm a designer and I've never used Claude." Reading your own answer back
  as a sentence, and being able to click any part of it to change it, is better than a
  form. Whoever wrote that understood something.
- **The restraint in the visual system is real.** One warm paper ground, one clay accent,
  no shadows, no gradients, a serif that carries the reading and a sans that carries the
  interface. Token-clean throughout, per the 2026-08-24 audit. It probably looks better
  than it works, which is an unusual failure and a recoverable one.
- **Two of the four mobile bugs from 2026-08-24 are already fixed in the shipped CSS.**
  Somebody is reading their own audits.

---

## Checklist — every line ticked or the file is not finished
- [x] I opened the live site
- [x] I tried all four levels
- [x] I quoted at least 5 real titles or lines from the site
- [x] Every number I used is in 00-facts.md or I show the command
- [x] I looked at a phone width
- [x] I found at least one thing nobody has mentioned before
