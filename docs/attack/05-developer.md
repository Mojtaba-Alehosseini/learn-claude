# Attack: a developer
Written as someone who is a developer, at 2026-08-27. Site version: 22e4532.

## 1. The first 60 seconds

I have an hour. I installed Claude Code yesterday, it wrote something stupid, and I want
to know how to drive it properly before standup tomorrow.

The front door says **"Find what's worth your time."** and then a fill-in-the-blank
sentence: *I'm [a role] and I've [level].* Fine. Two clicks. That is genuinely fast and I
did not have to read a manifesto first.

Two things happen in that first minute that I did not like.

First, the search box **disappears**. `assets/js/home.js` line ~200 does
`el.go.classList.toggle("answered", !!(state.role && state.level) && !el.q.value.trim())`
and `index.html` does `.search-row.answered .input { visibility: hidden; max-width: 0 }`.
So the moment I answer both questions, the field labelled "Or describe what you want to
do…" collapses to zero width. The natural order for me is: say who I am, *then* type my
actual problem. The site takes the second option away for doing the first one right.

Second, nowhere on that screen does it tell me there is a path for developers. I checked
the submit handler: it builds `browse.html?role=…&level=…` and nothing else. Paths exists
only as a nav link at the top, next to "How we check". The one curated route written for
me is not connected to the one screen that knows I am a developer.

Then I land on Browse with 43 cards and no idea which one to open.

## 2. Does the front door work for me       (all four levels, with counts)

```
$ python docs/attack/role-view.py developer --counts
developer: 94 total
  never-used       3
  basic           16
  confident       32
  builder         43
```

Matches `00-facts.md`. 94 total, the biggest role on the site by a distance.

Live, from the browser, `browse.html?role=developer&level=<L>`, reading
`document.getElementById('count').textContent`:

| level | on-screen count line |
|---|---|
| never used Claude | `3 resources. Remove a filter to see more.` |
| used it a little | `16 resources` |
| used it a lot | `32 resources` |
| built things with it | `43 resources` |

**The inversion is real and it is backwards.** A developer who has *never touched Claude*
gets 3 cards and a nag telling them to remove a filter. A developer who has already built
things with it gets 43. That is the wrong way round for a teaching site. The person at 43
does not need you — they already found this stuff, that is how they became a builder. The
person at 3 is the one who came here to be taught, and the site tells them to go away and
un-answer a question it just asked them.

And the 3 are these, in the real on-screen order:

```
$ python docs/attack/role-view.py developer never-used
 1. [Read by AI] Claude Code overview and install guide   (docs, one hour, free)
 2. [Skimmed]    What is Claude Code?                     (video, 15 minutes, free)
 3. [Skimmed]    Claude Code Essentials (ExamPro full course)  (course, half day, free)
```

An install page, a three-minute "what is it" video, and a half-day video course. That is
not an on-ramp, it is a shrug. There is nothing in between "run this command" and
"surrender your afternoon to a video".

Worse: there is **no path for me at this level**. `data/paths.json` tags
`claude-code-start` as `level: basic`, and its own `for` field reads *"Developers who
have installed Claude Code and are getting mediocre results."* The other two paths name
non-technical, student, teacher, business-founder and researcher. So the developer at
`never-used` — the only one who actually needs an order — is the one person the paths
system does not serve.

The count line also nags at the wrong moment. `browse.js` renderCount:
`if (n > 0 && n <= 6 && anyFilters()) text += ". Remove a filter to see more."` The only
filters applied are the two answers the site itself just asked me for. It is telling me
to undo its own front door.

## 3. What the catalogue actually gives me  (are these really for me?)

94 is not a gift. 94 is a problem. Here is what the filtering can actually do about it.

**On arrival I get one new filter axis.** There are six axes in `browse.js` AXES, but only
three are marked `primary: true` — Role, Level, Time. Topic, Format and Cost sit behind a
`More filters +` toggle, collapsed by default (verified live:
`document.getElementById('filtersMore').classList.contains('hidden') === true`). Role and
Level are already filled in by the front door. So the single filter I am offered without
an extra click, on a page of 43 cards, is **Time**. On a 688px-tall window the rail only
shows the Role group — ten checkboxes for a question I answered thirty seconds ago —
before I have to scroll the rail to reach Level and Time.

**How often the filters dead-end.** Reproducing `matches()` from `browse.js:70-88`:

```
$ python - <<'EOF'   # (full script run in session; core of it below)
dev=[i for i in items if "developer" in i["roles"]]
# A) role + ONE more filter click
# B) role + level + ONE other filter
# C) role + one value on all five other axes
EOF

A) role=developer + ONE filter click: 1 of 27 combinations return 0
     ZERO: cost = paid-once
B) role=developer + level + ONE other filter: 26 of 92 return 0 (28%)
     never-used  12 zeros
     basic        7 zeros
     confident    2 zeros
     builder      5 zeros
C) role=developer + one value on ALL FIVE other axes: 3449 of 3584 return 0 (96.2%)
```

**96.2%.** On the biggest role on the site, if I use the filter UI the way it is drawn —
one thing from each group — I hit an empty page 3449 times out of 3584. And at the level
where I have the fewest options to start with, `never-used`, more than half my second
clicks (12 of 24) land on nothing.

A concrete one. I want the official written reference on Claude Code, at builder level,
free, and I have an afternoon:

```
D) developer + builder + topic=claude-code + format=docs + cost=free
     time=under-15min  -> 1
     time=under-1hr    -> 4
     time=half-day     -> 0
     time=multi-day    -> 0
```

Half a day of official Claude Code docs: zero. The empty-state copy says *"Try removing
one filter — time is usually the one to loosen."* It is right, which tells you the Time
axis is mostly decorative on this role.

**There is no filter for how well you checked it.** Six axes, none of them tier. I cannot
say "only show me things somebody actually read". That is the one axis this site sells
itself on — the whole home page section is headed *"We say how we checked"* — and it is
the one thing I cannot filter by. I can sort by it. I cannot filter by it.

**Are these really for me?** Six of my 94 cards have a `For:` line written for somebody
else:

```
$ python -c "...regex over who_for for PM|owner|founder|data analyst..."
developer cards whose 'For:' line names a NON-developer audience: 6
```

Including, and I am not making this up, **step 1 of my own path**:

> **Claude Code 101 (Anthropic Academy)**
> For: *A PM who has decided to learn Claude Code properly and wants the mechanics from
> the source rather than from a newsletter.*

The first step of "Getting good at Claude Code", the only developer path on the site, is
described as being for a product manager. Also in my 94:

> **Remote MCP Servers directory**
> For: *Owners/consultants connecting Claude to business tools beyond the built-in SMB
> connectors.*
> Skip if: *The built-in SMB connectors already cover your stack.*

I do not have an "SMB connector stack". That card is for a small-business owner and it was
filed under `developer` because it mentions MCP.

**Format mix.** From `00-facts.md`: video 38, article 16, course 14, docs 12, repo 12,
hands-on 1, podcast 1. **Exactly one hands-on resource in 94.** For the role whose entire
job is typing things and seeing what happens. 52 of my 94 cards are video or course —
sit-and-watch formats — and 1 is do-it.

**Topic gaps.** `Counter(topics)` over my 94: claude-code 57, agents 51, mcp 32, api 31,
skills 23, chat-prompting 7, safety 6, **cowork 1**. There is nothing here on the boring
things that decide whether I can use this at work: cost control at team scale, data
retention, what happens to my source code. `safety` is 6 cards out of 94.

## 4. Paths

One path: **"Getting good at Claude Code"** — 6 steps, "about 6 hours", free.

The six steps, with what the site itself files them as:

| # | step | format | time | source |
|---|---|---|---|---|
| 1 | Claude Code 101 (Anthropic Academy) | course | half-day | Anthropic Academy |
| 2 | Best practices for Claude Code | docs | under-1hr | Claude Code docs |
| 3 | The new rules of context engineering for Claude 5 generation models | article | under-15min | Anthropic |
| 4 | Maximizing the value of your Claude Code sessions | article | under-15min | Anthropic |
| 5 | Effective context engineering for AI agents | article | under-1hr | Anthropic |
| 6 | A harness for every task: dynamic workflows in Claude Code | article | under-15min | Anthropic |

**Is 6 hours honest? No — it is arithmetic on a bucket, and the bucket is wrong.**

`scripts/build-paths.py:37` maps `{"under-15min": 12, "under-1hr": 45, "half-day": 210,
"multi-day": 600}`. So 210 + 45 + 12 + 12 + 45 + 12 = 336 minutes = "about 6 hours".
Checked against the stored value: `total_minutes: 336`. The arithmetic is internally
consistent.

But **62% of that headline number is one step**, and that step is one of two duplicate
rows for the same course. `academy.claude.com/courses/claude-code-101` is filed
`under-1hr`; `anthropic.skilljar.com/claude-code-101` is filed `half-day`. Same course,
same publisher, same `free-account`. The path happens to point at the skilljar row. Had it
pointed at the other one:

```
if the path used the OTHER duplicate row of Claude Code 101 (under-1hr): 171 min = 2.9 hours
```

**The advertised length of the only developer path on this site is "about 6 hours" or
"about 3 hours" depending on which of two identical rows the build script grabbed.** That
is not an estimate, it is a coin flip printed as a fact.

**The path is a reading list, not a path.** Six of six steps are published by Anthropic
(Academy, the docs, or the Anthropic blog). Four of six are Anthropic blog posts. Zero
hands-on. Zero video — out of the 38 videos this site holds for me, the curated route uses
none. Nothing in it asks me to type anything. "Getting good at Claude Code" contains no
Claude Code.

**The path is shredded by the level filter.** Its steps are filed across three different
levels:

```
never-used   0 of 6 steps visible
basic        1 of 6 steps visible
confident    2 of 6 steps visible
builder      3 of 6 steps visible
```

So whichever level I answered on the front door, Browse can show me at most **half** of my
own path. There is no level at which the six steps appear together.

**And the path badges are honest about themselves in a way that hurts.** Step 1 is
`previewed` — "We read the outline or a free sample. We have not seen the whole thing."
The stored `weakest_tier` on the path is `previewed`. So the first 210 of my 336 minutes
are being spent on something nobody here has done.

## 5. The card and the resource page

I opened three. All live, all on `mojtaba-alehosseini.github.io`.

**(a) `resource.html?id=r-c1f2ae6b68` — Model Context Protocol: Advanced Topics.** Tier
`listed` — "Found only". Nobody has opened this one. Read from the live DOM:

```
badge:      "Found only"
badgeTip:   "We found it and sorted it. Nobody has looked at the content yet."
teaches:    "What it teaches — handle transport and authentication for MCP servers
                              — scale Model Context Protocol implementations"
howChecked: "Found only. We found it and sorted it. Nobody has looked at the content yet."
```

Read those two out loud. On one screen the page says nobody has looked at the content, and
then tells me what the content teaches, who it is for, what I must know first, and gives
me two sentences of "Skip it if". This is not one bad record:

```
catalogue: listed items = 43
  ... with a non-empty 'teaches' list: 43
  ... with a non-empty 'skip_if':      43
  ... with a non-empty 'summary':      43
```

**43 of 43.** Every single "Nobody has looked at this" card on the site ships a full set of
judgements about the thing nobody looked at.

The publisher line on this page also reads **"Anthropic Academy · Anthropic (Claude
Academy)"** — the same organisation printed twice. `ui.js` has a whole `authorLine`
function whose comment says *"'Anthropic Academy · Anthropic' says the same thing twice"*,
and it fails here because neither string is a substring of the other. 24 of 353 cards
print a source and author that share a word.

**(b) `resource.html?id=r-3b409df1d4` — How to Build an MCP Server with Python, Docker,
and Claude Code.** This one is broken on the live site. From the DOM:

```
whereFits: "Where this fits  This is step 1 of 6 in first-week.
            The order matters — the path says why."
link:      "paths.html?id=first-week"
```

Two failures in one sentence. It prints the raw internal slug **`first-week`** where the
title should be. And the claim is false: I followed the link, and `paths.html?id=first-week`
is "Your first week with Claude", whose six steps are *"Claude is not one tool. It's six."*,
*"Get started with Claude"*, *"Claude 101"*, *"What are Projects?"*, *"Why do AI models
hallucinate?"*, *"Get started with Claude Cowork (Help Center)"*. This builder-level MCP
article is not among them.

**(c) `browse.html?role=developer&level=basic` — the duplicate, side by side.** Read
straight off the live page:

```
[{ title: "Claude Code 101",
   badge: "Skimmed", chips: "course/one hour/free, sign-up needed",
   path:  "Step 1 of 6 in claude-code-start" },
 { title: "Claude Code 101 (Anthropic Academy)",
   badge: "Skimmed", chips: "course/a half day/free, sign-up needed",
   path:  "Step 1 of 6 in Getting good at Claude Code" }]
```

Two cards. Same course. Both claim to be **step 1 of the same 6-step path**. One says it
takes an hour, the other says half a day. One prints the internal slug
`claude-code-start` where a human-readable title belongs. This is on the page a developer
who has "used it a little" lands on straight from the front door.

**What the cards do well:** the `Skip if:` line is the best thing on the site and I read
every one of them. *"Skip if you already use worktrees. Most of the twenty minutes explains
the git feature, not the Claude Code part."* That saved me twenty minutes. Nobody else on
the internet writes that sentence.

## 6. Search, in my words

Reproduced with `scripts/test-search.py`, which runs the same IDF, the same admit gate and
the same floor as `assets/js/search.js`.

```
$ python scripts/test-search.py "how do i wire this into my CI" \
    "does it work with my existing test suite" "rate limits and pricing for the API"

"how do i wire this into my CI"   4 result(s)
     22.4  [developer] Claude Code Headless Automation & Agent Workflows
     13.4  [developer] anthropics/claude-code-action
     13.4  [developer] I Built an Agentic Software Factory with Codex and Claude Code

"does it work with my existing test suite"   80 result(s)
     18.6  [pm,designer] Claude Code for Product Managers with Sachin Rekhi
     16.1  [developer  ] Skill authoring best practices
     16.1  [developer  ] Demystifying evals for AI agents

"rate limits and pricing for the API"   5 result(s)
     58.5  [designer        ] Guide to the Figma MCP server
     28.4  [business-founder] Plans & Pricing
     23.9  [business-founder] Claude Team pricing for a small business
```

Query 1 is good. Genuinely good — three right answers, no padding.

Query 2 is a mess. **80 results out of 353** — 23% of the entire catalogue for a specific
question. The top hit is a product-manager video. The one card that is actually about
tests, *"Red Green Refactor is OP With Claude Code"*, ranks **6th**, below "Skill authoring
best practices" and "MCP: Build Rich-Context AI Apps".

Query 3 is a failure. Top hit for a developer asking about **Claude API rate limits and
pricing** is a **Figma** guide for designers. Then two small-business pricing pages. Zero
of the 5 hits are tagged `developer`.

```
first developer-tagged hit at position: NONE
Claude Platform documentation home     -> NOT IN RESULTS
Building with the Claude API           -> NOT IN RESULTS
```

The Claude Platform docs home — the page that documents rate limits — is not in the result
set at all. And the reason is upstream of the ranker:

```
--- does ANY resource mention rate limits? ---
   [ai-reviewed] Guide to the Figma MCP server | roles=['designer']
   [ai-reviewed] Agent SDK overview            | roles=['developer']
   count: 2
```

**Two records in 353 mention rate limits, and one of them is a Figma guide.**

Now the part that actually ends my visit. On Browse, `matches()` applies the axis filters
*and* the ranked set. I arrived from the front door with `?role=developer&level=builder`.
Simulating that:

```
"how do i wire this into my CI"             never-used=1  basic=0  confident=0  builder=3
"does it work with my existing test suite"  never-used=1  basic=7  confident=10 builder=14
"rate limits and pricing for the API"       never-used=0  basic=0  confident=0  builder=0
"can i self host this"                      never-used=0  basic=0  confident=1  builder=1
"what are the rate limits"                  never-used=1  basic=0  confident=1  builder=0
```

Typing the most ordinary API question a developer has, on the page the site sent me to,
returns **zero at every level**. The message I get is *"No match for 'rate limits and
pricing for the API'. Try fewer words, or browse by role instead."* I am already browsing
by role. That is the advice it gives me and it is the thing I am doing.

## 7. On a phone

Checked from the `@media (max-width: 768px)` block in `assets/css/site.css:590-635`, and
by applying that block's own `.sheet` / `.sheet-body` rules (lines 617-628) to the live
page and measuring. I deliberately did **not** resize the shared browser window, because
four other agents were working in it.

- `.filter-rail { display: none; }` — the whole rail is gone. Everything goes through the
  bottom sheet.
- The sheet body is built from `AXES.map(groupHTML)` — **all six axes, every option, one
  column**. Measured live: **37 checkboxes**, `scrollHeight: 1969px` in a `clientHeight`
  of `554px`. **3.6 screens of thumb-scrolling.**
- Group order in the sheet is Role, Level, Time, Topic, Format, Cost. The first group is
  **Role — ten options with icons** — which I already answered on the front door and which
  is already ticked (`rolePreChecked: ["developer"]`). On a phone, screen one of the filter
  sheet is a question I have answered, and Format sits at roughly 1371px down.
- One thing I expected to be broken and is not: `renderFilters()` rewrites
  `sheetBody.innerHTML` on every tick, so I tested whether the scroll position survives a
  tap. It does — `scrollTop 1371.2` before, `1371.2` after. Credit where due.
- Good: the sheet traps Tab, Escape closes it, `body:has(.mobile-filter-bar)` pads the
  footer so the fixed bar does not eat the last line, and `.footer-col a` is forced to
  44px. Somebody has actually held this thing in a hand.

## 8. Content quality — the three worst entries I was shown, quoted

Named, as asked. All three are in my 94.

**1. "CLAUDE CODE Full Course For Beginners (DATA DOMAIN Edition)"** — Ansh Lamba, video,
`multi-day`, published 2026-03-15, tier **Skimmed**.

> Skip if: *Skip if you only have one evening. At 6:47 it needs a real schedule, and a
> shorter course will teach you the same basics faster.*

A 6-hour-47-minute YouTube video, filed under `developer`, whose `For:` line says it is
for *"Data analysts and data engineers"*. The card's own advice is that a shorter course
teaches the same thing faster — and this site holds several. So why is it here, taking a
slot in a role it is not for, at a length the card itself calls unjustified? This is the
purest example of a link that exists because it was found, not because it was chosen.

**2. "Complete Claude Code Course In 2 Hours For Developers"** — Krish Naik, video,
`half-day`, published 2026-05-25, tier **Skimmed**.

> Skip if: *Skip if you want polished production and tight editing. The delivery is live
> and repeats itself, so two hours holds about ninety minutes of content.*

"Two hours holds about ninety minutes of content" is a claim you can only make by watching
two hours. The badge on this card says *"We read the outline or a free sample. We have not
seen the whole thing."* One of those two statements is false. Also: it is called a 2-hour
course and is filed as `half-day`.

**3. "Model Context Protocol: Advanced Topics"** (`r-c1f2ae6b68`, the
`academy.claude.com` copy) — course, tier **Found only**.

> Skip if: *Skip if you have not built an MCP server at all; do the introductory course
> first. Skip if you only install other people's servers rather than writing your own.*

A duplicate of a card that already exists, with a worse write-up, a worse badge, and
*more* topic tags than the good one (`['mcp','api','agents']` versus `['mcp']`). Which
means the topic filter actively prefers the bad copy:

```
topic=mcp     builder -> [('listed', academy.claude.com), ('previewed', anthropic.skilljar.com)]
topic=api     builder -> [('listed', academy.claude.com)]
topic=agents  builder -> [('listed', academy.claude.com)]
```

Filter by `agents` or `api` and you get **only** the copy nobody read. The one with the
detailed write-up about sampling, stdio handshakes and StreamableHTTP is filtered out.

**Honourable mention for filler I would close instantly:** *"Claude Code Tutorial - Build
Apps 10x Faster with AI"* (Programming with Mosh, 2026-03-24) and *"Parallel Claude Code +
Git Worktrees: This Setup Will Change How You Ship"* (Cole Medin, 2026-04-22). "10x
Faster" and "This Setup Will Change How You Ship" are thumbnail copy, not titles. **11 of
my 38 videos were published in the nine weeks between 2026-03-01 and 2026-05-01** — the
signature of a channel-cycle pile-on, and the site indexed it wholesale.

## 9. Everything that is broken, ranked                (evidence for each)

**9.1 — Not one video or course on this entire site has been checked past the outline.**

```
--- whole catalogue: tier by format ---
video      {'previewed': 75, 'listed': 3}
course     {'previewed': 50, 'listed': 4}
article    {'ai-reviewed': 55, 'previewed': 44, 'listed': 9}
docs       {'ai-reviewed': 43, 'listed': 14, 'previewed': 10}

videos in whole catalogue: 78  ai-reviewed: 0
```

**0 of 78 videos. 0 of 54 courses.** Zero. The tier is not a measure of care, it is a
measure of whether the thing was machine-readable text. For me that is not a detail: video
is my biggest format at 38 of 94, and video plus course is **52 of 94 — 55% of everything
I am shown carries a verdict written without seeing the content.** Overall **80 of my 94
cards are `previewed` or `listed`.**

`how-we-check.html` says: *"We find material, read it, and write two things: who it helps,
and who should skip it."* For 80 of my 94 that sentence is not true.

It also gives a reason for the Skimmed tier: *"Paid courses usually stop here, because we
cannot see inside them."* That excuse does not cover a single one of my videos:

```
developer: previewed videos = 37  free: 37  on youtube: 37
```

All 37 are free, all 37 are on YouTube, all 37 are fully visible to anyone with a browser.
Nothing stopped anybody watching them.

**9.2 — The same course is in the catalogue twice, with different times, different badges,
and both claiming to be step 1 of the same path.** Live, on
`browse.html?role=developer&level=basic`:

```
"Claude Code 101"                    Skimmed  course/one hour/free, sign-up needed
                                     "Step 1 of 6 in claude-code-start"
"Claude Code 101 (Anthropic Academy)" Skimmed  course/a half day/free, sign-up needed
                                     "Step 1 of 6 in Getting good at Claude Code"
```

Two duplicate pairs exist, both landing on my role:

```
slug: claude-code-101
   r-7340ad4c33 | Claude Code 101                     | previewed | basic   | under-1hr
   r-530cb03364 | Claude Code 101 (Anthropic Academy) | previewed | basic   | half-day
slug: model-context-protocol-advanced-topics
   r-c1f2ae6b68 | listed    | builder | academy.claude.com
   r-8e9aab2f3a | previewed | builder | anthropic.skilljar.com
```

`anthropic.skilljar.com` is the platform behind `academy.claude.com`. The same course was
harvested from both hostnames and never reconciled. Three more duplicate pairs exist
outside my role (AI Fluency ×3, AI Fluency for Students ×2, 15 Claude Tips ×2, Getting
Started with Claude in Excel ×2).

**9.3 — Eight cards claim to be steps in paths they are not in, and print the internal
slug on screen.**

```
items carrying a STALE `paths` field that paths.json does not confirm: 8
  Claude Code 101                              -> claude-code-start step 1 of 6
  Steering Claude Code: when to use CLAUDE.md… -> first-week step 6 of 6
  Equipping agents for the real world…         -> first-week step 5 of 6
  MCP: Build Rich-Context AI Apps with Anthropic -> first-week step 3 of 6
  How to Build an MCP Server with Python…      -> first-week step 1 of 6
  (+3 for non-technical and pm)
```

Five of the eight are mine. `ui.js` LC.items() falls back to the item's stored `paths`
when `LC_PATHS` has no entry, and that stored object has no `pathTitle`, so
`LC.esc(p.pathTitle || p.path)` prints the slug. Live on
`browse.html?role=developer&level=builder` I read three cards saying **"Step 5 of 6 in
first-week"**, **"Step 1 of 6 in first-week"**, **"Step 3 of 6 in first-week"**. Following
one through, `resource.html?id=r-3b409df1d4` says *"This is step 1 of 6 in first-week. The
order matters — the path says why."* and links to a path whose six steps are *"Claude 101"*,
*"What are Projects?"*, *"Why do AI models hallucinate?"* and so on. My builder-level MCP
article is not in it. A raw slug, a false claim, and a link that disproves it — three
failures in one line of copy.

**9.4 — Every one of the 43 "Nobody has looked at the content yet" cards ships a full set
of judgements about content nobody looked at.**

```
catalogue: listed items = 43
  ... with a non-empty 'teaches' list: 43
  ... with a non-empty 'skip_if':      43
  ... with a non-empty 'summary':      43
```

Live proof on `resource.html?id=r-c1f2ae6b68`: badge *"Found only"*, tooltip *"Nobody has
looked at the content yet"*, and directly below it *"What it teaches — handle transport and
authentication for MCP servers"*. The honesty system and the content system contradict each
other on the same screen, and the reader has no way to know which one to believe.

Two cards even confess it inside the `Skip if:` line, in the first person, on a site that
otherwise says "we":

> *"I read a detailed third-party description of the repo, not the skill files."*
> — Ralph: PRD skill plus autonomous implementation loop
> *"I did not inspect the repo contents, only the install instructions quoted in the guide."*
> — compound-engineering-plugin (Every)

**9.5 — "Newest first" buries every official doc below a 2024 video.**

`ui.js`: `c.sortDate = x.published && x.published !== "UNVERIFIED" ? x.published : "0000"`.
Undated items sort last. **34 of my 94 have no publish date, and 11 of my 12 `docs` are
among them.** Result, from the live sort order:

```
 59. 2024-12-19 article  Building effective agents
 60. 2024-09-05 video    AI prompt engineering: A deep dive
 61. 0000       docs     Best practices for Claude Code
 62. 0000       docs     Agent SDK overview
 63. 0000       docs     Claude Managed Agents overview
 64. 0000       docs     Claude Code overview and install guide
 87. 0000       docs     Hooks reference (Claude Code)
```

Sorting a fast-moving developer catalogue by "Newest first" — the exact thing I do when a
tool ships monthly — pushes the continuously-maintained official documentation to
positions 61 through 87, underneath a prompt-engineering video from September 2024. The
one sort a developer reaches for is the one that inverts the answer.

**9.6 — The filter grid dead-ends 96% of the time on the biggest role.**

```
C) role=developer + one value on ALL FIVE other axes: 3449 of 3584 return 0 (96.2%)
B) role=developer + level + ONE other filter:           26 of 92  return 0 (28%)
     never-used 12 zeros / basic 7 / confident 2 / builder 5
```

And three of the six axes (Topic, Format, Cost) are collapsed behind `More filters +` by
default, while two of the three visible ones are already answered by the front door. On
arrival at a 43-card page I am offered exactly one new way to narrow it: Time. Which is
the axis the site's own empty-state copy tells me to loosen.

**9.7 — Search cannot answer the two most ordinary API questions a developer has, and the
role filter turns a bad answer into no answer.**

`"rate limits and pricing for the API"` → 5 results, top hit **"Guide to the Figma MCP
server"** (designer), zero tagged `developer`. Filtered to `role=developer`:
`never-used=0 basic=0 confident=0 builder=0`. `"does it work with my existing test suite"`
→ **80 results**, 23% of the catalogue, top hit a PM video, the actually-relevant card
6th. Underneath it, the catalogue itself: only 2 of 353 records mention rate limits.

**9.8 — The front door deletes the search box for answering its own questions.**

`index.html`: `.search-row.answered .input { visibility: hidden; opacity: 0; max-width: 0 }`,
toggled by `home.js` once role and level are both set. The prompt is *"Or describe what you
want to do…"* — the one route that would take my actual sentence instead of two coarse
buckets — and answering the two buckets removes it.

**9.9 — The front door never mentions the path.** `home.js` submit builds
`browse.html?role=…&level=…`. There is no branch that checks whether the answered role has
a path. The site knows I am a developer, knows a developer path exists, and sends me to 43
unordered cards instead. And the path itself cannot be reassembled from Browse at any level:
0/6 steps visible at `never-used`, 1/6 at `basic`, 2/6 at `confident`, 3/6 at `builder`.

**9.10 — The only developer path is 6/6 Anthropic and 0/6 hands-on, and its headline
duration is a coin flip.** Steps by source: Anthropic Academy, Claude Code docs, Anthropic,
Anthropic, Anthropic, Anthropic. Formats: course, docs, article, article, article, article.
`total_minutes: 336` where 210 of them come from a duplicate row; the other row of the same
course would give 171 minutes = "about 3 hours". Step 1's `For:` line is written for a PM.

**9.11 — Six of my 94 cards are written for somebody else, and there is no way to tell
before opening one.** Named in §3. Two of them (`Remote MCP Servers directory`,
`knowledge-work-plugins/small-business`) also carry one-line `Skip if:` copy — *"The
built-in SMB connectors already cover your stack."* — against the two-clause, reasoned
sentences everywhere else. The catalogue was clearly written in batches by different
hands and the seams show inside a single role's results.

**9.12 — Small ones.** `ui.js:87` comments *"176 of 353 resources publish no date"*; the
data says **171 of 353**, and `00-facts.md` agrees with the data. The code's own
documentation is stale against the file it sits next to. And 24 of 353 cards print
`Source · Author` where both name the same organisation — *"Anthropic Academy · Anthropic
(Claude Academy)"* — which is precisely the case `LC.authorLine` was written to suppress.

## 10. The one thing that would make me leave and not come back

Finding 9.1.

I came here because the home page promised judgement — *"We say when to skip"*, *"We say
how we checked"*, *"Four levels, and we do not round up."* That promise is the entire
product. A list of Claude links is worth nothing; I can get that from a search engine in
four seconds.

Then I find that **0 of 78 videos and 0 of 54 courses on this site have been checked past
the outline**, that **55% of my own results are those two formats**, and that a card can
tell me *"two hours holds about ninety minutes of content"* while wearing a badge that says
*"We have not seen the whole thing."*

The moment I work that out — and it took me one `Counter` over `items.json` — every `Skip
if:` line on the site becomes unreadable. Not wrong: unreadable. I cannot tell which ones
came from watching and which came from a YouTube description, because the badge does not
distinguish them and the badge is the only instrument on offer. And I cannot filter for the
ones I can trust, because tier is the one axis with no filter.

A directory that grades itself and then grades 226 of 353 entries "we did not really look"
has not solved my problem. It has re-labelled it and asked me to trust the label.

## 11. What is genuinely good                          (be honest, but brief)

- **`Skip if:` is the reason to build this site.** *"Skip if you already use worktrees. Most
  of the twenty minutes explains the git feature, not the Claude Code part."* Nobody else
  writes that. When it comes from a card that was actually read, it is worth the visit on
  its own.
- **The tier vocabulary is brave.** "Found only — nobody has looked at the content yet" is a
  thing almost no directory would print. The problem is that the rest of the record ignores
  it, not that it exists.
- **It is fast and it is honest about state.** No spinner, no framework, filter state in the
  URL so I can bookmark and share a filtered view, 0.14s to first byte on Browse, works
  from `file://`. The code comments explain *why* rather than *what*, which is rarer than
  it should be.
- **The mobile work is real.** 44px targets, focus trapped in the sheet, Escape closes it,
  the fixed bar does not eat the footer, and the filter sheet holds its scroll position
  through a re-render. Somebody used this on a phone.
- **`role-view.py` reproduces the on-screen order exactly.** That the project ships a tool
  to check itself is the best sign here that the problems above are fixable rather than
  structural.

If I am honest: the skeleton is better than the contents. The judgement layer is the right
idea, executed on a catalogue that is roughly twice as big as the checking effort behind
it. I would rather have the 70 you can vouch for. The site says so itself, at the top of
`how-we-check.html`, and then does not do it.

## Checklist — every line ticked or the file is not finished
- [x] I opened the live site — `curl` (index 200, browse 200, items.js 200/624KB) and a
      browser tab I created and closed, on `browse.html`, `resource.html` ×2,
      `paths.html?id=first-week`
- [x] I tried all four levels — 3 / 16 / 32 / 43, read off the live `#count` element and
      matching `role-view.py --counts`
- [x] I quoted at least 5 real titles or lines from the site — 20+ verbatim titles and 9
      verbatim `Skip if:` / `For:` lines
- [x] Every number I used is in 00-facts.md or I show the command
- [x] I looked at a phone width — via the `@media (max-width: 768px)` block and by applying
      its own `.sheet-body` rules live and measuring (37 checkboxes, 1969px, 3.6 screens);
      I did not resize the shared window because four other agents were using it
- [x] I found at least one thing nobody has mentioned before — 9.1 (no video or course
      anywhere on the site has been checked past the outline), 9.2 (duplicate courses, both
      claiming step 1 of the same path), 9.3 (8 stale path claims printing raw slugs),
      9.4 (43/43 "nobody looked" cards ship full judgements), 9.5 ("Newest first" buries
      every official doc), 9.6 (96.2% of filter combinations dead-end)
