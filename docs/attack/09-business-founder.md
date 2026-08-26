# Attack: running a business
Written as someone who is running a business, at 2026-08-27. Site version: 22e4532.

I have one hour before the shop opens. Four people on payroll. I pay for my own software.
I am not here to browse. I want to know three things: will this replace work I am paying
for, is my customer list safe, and what does it cost for five people. Then I want to go.

---

## 1. The first 60 seconds

The home page says **"I'm a [role] and I've [level]."** Two blanks. I press
`running a business`. The drawing changes to a shopfront. The line under the button says
**"54 resources match so far."**

That is a good first ten seconds. Better than most.

Then I look for the thing I actually came for and it is not there. There is no price on
this page, no "what will Claude cost me", no "is it safe for client data". The only free
text box says **"Or describe what you want to do…"** — so I type a real sentence into it,
because that is what it asked for. That was a mistake. See section 6.

One thing I noticed and did not like. On a 1568×745 window the count line
`54 resources match so far.` sits below the visible area until you pick a role. At
390px wide it is at y=849 in an 844px viewport — off screen. The one honest number on the
page is the one you have to scroll for.

---

## 2. Does the front door work for me (all four levels, with counts)

Live, clicking each level chip on `https://mojtaba-alehosseini.github.io/learn-claude/`
and reading `#tally`:

| I've… | it says |
|---|---|
| never used Claude | `10 resources match so far.` |
| used it a little | `35 resources match so far.` |
| used it a lot | `5 resources match so far.` |
| built things with it | `4 resources match so far.` |

Matches `00-facts.md` (10 / 35 / 5 / 4). Also matches
`python docs/attack/role-view.py business-founder --counts`.

The front door works. The room behind it does not.

**35 of my 54 sit in one bucket.** Two thirds of everything I am offered is "used it a
little". Ten cards before that. Nine cards after it, total, for the rest of my life with
this tool. So the shape of my catalogue is: a short shelf, one enormous shelf, then a
cliff.

I run a business. I will not stay a beginner. In three months I will be at "used it a
lot" and the site will have **five** things for me — and I have read them below. It is
three YouTube videos and two link directories.

Then "built things with it" gives me **four**. I checked all four on the live site
(`browse.html?role=business-founder&level=builder`, count line: `4 resources. Remove a
filter to see more.`):

1. `Agent-native Product Management (Every's guide)` — tagged `pm`
2. `awesome-mcp-enterprise` — tagged `developer`
3. `Introduction to Model Context Protocol` — tagged `developer`
4. `compound-engineering-plugin (Every)` — tagged `pm`, `developer`

Zero of four are tagged for me alone. Zero of four are about running a business. The site
has taken a product manager's reading list and a developer's reading list, stapled my
name to them, and called it my top tier. Three of the four are a GitHub repo or a course
about a wire protocol.

The `builder` chip for "running a business" is a lie of composition. There is no such
shelf. There are four borrowed items in a box with my name on it.

---

## 3. What the catalogue actually gives me (are these really for me?)

`00-facts.md`: **only 18 of my 54 are mine alone.** Lowest specialisation of any role on
the site. So 36 are hand-me-downs.

I read the `For:` line on every one. Command:

```
python -c "import json,re; items=json.load(open('data/items.json',encoding='utf-8'));
mine=[i for i in items if 'business-founder' in i['roles']];
biz=re.compile(r'business|founder|owner|SMB|company|payroll|invoice|customer|client|nonprofit|operations|back-office|team of',re.I);
print(sum(1 for i in mine if biz.search(i['who_for'])), sum(1 for i in mine if not biz.search(i['who_for'])))"
→ 25 29
```

**29 of my 54 have a `For:` line with no business word in it at all.** Not "owner", not
"customer", not "team", not "invoice". Nothing. The site's own one-sentence description
of who the thing is for does not mention anyone like me.

Named, from the list I was actually shown:

- `Claude Design: The Complete Guide` — *"For: Working designers evaluating Claude Design
  seriously, and anyone who wants a designer's opinion rather than a feature demo."*
  `Skip if: Skip if you have no design background - the critique assumes you can tell
  good layout from bad.` I have no design background. Why is this in my 35?
- `Create on-brand content (use case)` — *"For: Writers and marketers who keep rewriting
  Claude's output to sound like their own voice…"*
- `How Anthropic's Growth Marketing team cut ad creation from 30 minutes to 30 seconds` —
  *"For: Marketers and writers who suspect Claude Code is not for them because they do
  not code."* This is card **number 1** at my "used it a little" level. The first thing
  the site shows me is a marketing-team case study.
- `Getting started with research in Claude.ai` — *"For: Anyone who does market scans,
  competitor checks, or background reading by hand…"* Closest to fair of the borrowed
  ones, and still not written for me.
- `Introduction to Model Context Protocol` — *"For: Technical owners, consultants, or
  in-house devs…"* `Skip if: You're non-technical — use the one-click built-in connectors
  instead.` This is one of my four `builder` cards. It tells me to skip it.
- `awesome-mcp-enterprise` — *"For: Teams that need governed, security-reviewed
  integrations."* I have four staff and a shared Google Drive.

Then the format mix (`00-facts.md`): video 19, article 12, course 10, docs 8, repo 4,
**hands-on 1**, podcast 0. Nineteen videos. One hands-on thing. I do not have time to
watch nineteen YouTube videos with names like `FULL Claude Tutorial For Beginners in
2026! (FULL COURSE)` and `The ONLY Claude Cowork Tutorial You'll Ever Need in 2026`. The
site's own note on that second one: `Skip if: The title oversells - this is a solid
overview, not the only thing you will ever need.` If you know the title oversells, why is
the title the biggest text on the card?

Four filter options are dead for me. Command and output:

```
# per-axis counts over the 54 items tagged business-founder in data/items.json
time  multi-day   0   <-- DEAD
topic api         0   <-- DEAD
format podcast    0   <-- DEAD
cost  paid-once   0   <-- DEAD
→ dead filter options for business-founder: 4 of 27
```

Small, but it is four boxes I can tick that give me an empty screen and the message
`Nothing matches all of those. Try removing one filter — time is usually the one to
loosen.`

**Safety is 6 of 54.** The site's own card says data privacy is *"the #1 SMB hesitation"*
— and it gives me six things on the topic `limits and safety`, four of which are the same
"AI Fluency" course in different wrappers.

---

## 4. Paths

I have a path. `Your first week with Claude` — 6 steps, about 2 hours, free, and it names
`business-founder` in its roles list. It is shared with three other audiences:
non-technical, student, teacher.

Live: `curl -s "https://mojtaba-alehosseini.github.io/learn-claude/paths.html?id=first-week"`
returns **HTTP 200, 1987 bytes**, and the body contains no path content at all — no title,
no steps. Everything is drawn by JavaScript after load. Nothing to share, nothing to
forward to my staff as a link preview.

Now the steps. I checked which of them the site itself tags for me:

| Step | Title | roles it is tagged with |
|---|---|---|
| 1 | Claude is not one tool. It's six. | `non-technical` |
| 2 | Get started with Claude | `non-technical` |
| 3 | Claude 101 | `business-founder`, +4 |
| 4 | What are Projects? | `researcher` |
| 5 | Why do AI models hallucinate? | `non-technical` |
| 6 | Get started with Claude Cowork (Help Center) | `business-founder`, `non-technical` |

**Four of the six steps in the path that names me are resources the site does not
consider mine.** Step 4 is tagged for researchers only. Not one of the six `why` lines
mentions a business, a customer, a cost, or a member of staff. Read them:

- Step 1: *"Start here because most confusion is not about prompting — it is not knowing
  that Claude is several different products."*
- Step 2: *"Now open the thing itself and do one real task. Reading about it any longer is
  procrastination."*
- Step 3: *"By now you have had a generic, disappointing answer."*

That is a path for a curious individual. It is fine. It is not for someone with payroll.
Nowhere in two hours does it say: decide what not to give it, tell your staff the rules,
check where your customer data goes, work out the bill.

**Step 1 is the worst part.** Live, on the path page:

> Step 1 · **Claude is not one tool. It's six.** · Substack · Read by AI · article ·
> 15 minutes · free · Checked 18 Aug 2026 · **No publish date given**

Author: Ruben Hassid. `official: false`. The site's own hidden note on this item:

> "This is the kind of creator-newsletter content the research brief specifically warned
> about — genuinely useful structure and steps, wrapped in heavy personal-brand framing"

and its `skip_if`:

> "The author writes in a promotional, personal-brand newsletter style with frequent
> subscribe prompts — if that tone bothers you, get the same information from Anthropic's
> own Cowork docs instead."

The site knows this is a newsletter with subscribe prompts. The site wrote down that its
own brief warned against exactly this. And it made it **step 1** of the only path it
offers me. The publisher printed on the card is "Substack", which is not a publisher, it
is a website where anyone can type.

---

## 5. The card and the resource page

I opened three.

**`resource.html?id=r-f21dc84635` — "Getting started with Claude Cowork (Airtree course)"**

What the live page shows:

- Byline: **`Vc · Marnix Denys, Airtree`**
- Chips: `course` · `one hour` · **`free`**
- Button: **`Open on Vc`**
- Provenance line: `Checked 21 Aug 2026 · No publish date given · **Found through Vc**`
- And, three sections down: `Before this — appropriate claude subscription`

"Vc" is not a publisher. It is the tail of `airtree.vc`. A directory whose entire value is
telling me who stands behind a thing has printed the letters "Vc" on a button and asked me
to press it. The same defect prints **`To`** on Every's guide — I saw it live on my
`builder` list: `Agent-native Product Management (Every's guide) | To · Marcus Moretti, GM
of Spiral at Every`.

This is not a data typo, it is a rule the code states and the data breaks. `assets/js/ui.js`,
`LC.publisher`:

> "Named because it is the publisher, not the platform: a video on Anthropic's channel is
> from Anthropic, not 'from YouTube'."

Count of cards that break that stated rule:

```
python -c "import json;from collections import Counter;items=json.load(open('data/items.json',encoding='utf-8'));
plat={'Substack','GitHub','YouTube','Coursera','Medium','Reddit','Udemy','Notion','Vc','To'};
b=[i for i in items if i.get('source') in plat];print(len(b),Counter(i['source'] for i in b))"
→ 61 Counter({'GitHub': 31, 'Substack': 11, 'Coursera': 8, 'Medium': 4, 'Udemy': 4, 'To': 2, 'Vc': 1})
```

**61 of 353.** Six of mine.

**`resource.html?id=r-e36c212931` — "Everyone should be using Claude Code more"** (the paid one)

- Byline: `Lenny's Newsletter · Lenny Rachitsky`
- Chips: `article` · `one hour` · **`subscription`**
- Button: `Open on Lenny's Newsletter`
- `Published 14 Oct 2025`

This is card 6 of the 10 the site gives someone who has **never used Claude**. It costs
money and the site will not say how much. "subscription" is not a price. I am the person
who pays; "subscription" tells me nothing I can put in a spreadsheet.

Its own `skip_if`, quoted whole:

> "Skip it if you want method rather than inspiration - it is a list of what other people
> do, most of it sits behind a paid subscription, and it dates from October 2025 so it
> predates Cowork."

Out of date, behind a paywall, and inspirational rather than useful — by the site's own
words — and it is in my top ten for day one.

How widespread the missing price is:

```
python -c "import json,re;items=json.load(open('data/items.json',encoding='utf-8'));
paid=[i for i in items if i['cost'] in ('subscription','paid-once')];
wp=[i for i in paid if re.search(r'[\$£€]\s?\d',' '.join(str(i.get(k) or '') for k in ('summary','notes','skip_if')))];
print(len(paid),len(wp))"
→ 32 3
```

**32 paid items on the site. 3 state a price.** In my 54, exactly one card contains a
currency figure — and that card is chipped **free**. See 5b.

**5b. The `free` chip is not true, and I am the one it lies to**

This is my angle and it is the worst thing I found. I filter by Cost = free because I have
not decided to pay yet. 48 of my 54 come back. Then:

```
python -c "import json,re;items=json.load(open('data/items.json',encoding='utf-8'));
mine=[i for i in items if 'business-founder' in i['roles']];
pat=re.compile(r'paid|pro\b|max\b|team\b|enterprise|subscription',re.I);
hit=[i for i in mine if i['cost']=='free' and any(pat.search(p) for p in i.get('prerequisites',[]) or [])];
print(len(hit)); [print(' -',i['title'],'|',i['prerequisites']) for i in hit]"
→ 7
 - How to install and use the Claude for Small Business plugin | ['claude desktop app installed', 'claude pro max or team subscription']
 - Claude Team pricing for a small business | ['basic familiarity with claude subscription tiers']
 - awesome-mcp-enterprise | ['familiarity with mcp architecture', 'enterprise tech stack knowledge']
 - Getting started with Claude Cowork (Airtree course) | ['appropriate claude subscription']
 - Getting started with Claude in Excel | ['paid claude plan pro max team or enterprise']
 - Learn 80% of Claude Cowork in Under 20 Minutes | ['paid claude plan']
 - Master Claude for Excel in 10 Minutes: Financial Modeling | ['a paid Claude plan and Microsoft Excel']
```

Five of those seven need me to buy a Claude plan before the content is of any use, and all
five are chipped **free**. The `skip_if` lines say it out loud, verbatim from the cards I
was shown:

- `Skip if: You are not on the desktop app with a Pro/Max/Team plan.`
- `Skip if: Skip if you are on the free plan, because Claude in Excel is a research preview
  for Pro, Max, Team and Enterprise only.`
- `Skip if: Skip if you do not use Excel or have no paid Claude plan, since the add-in
  requires one.`
- `Skip if: Skip if your plan does not include Cowork, because you cannot follow along with
  any of it.`
- `Skip if: … Also skip if you do not have a paid Claude plan, since Cowork needs one.`

And one more, also chipped `free`, `AI for Small Business: Explore Tools and Build Systems`:

> `Skip if: You only want Claude context — stop after the free Part 1; Part 2 (the 'AI
> Business Manifesto') is a $99 upgrade.`

A $99 upsell behind a chip that says "free". That is the only currency figure in my whole
catalogue and it is on the wrong card.

Yes, the chip means "the resource is free", not "the product is free". I understand the
distinction. **I do not care.** I am filtering on cost because cost is my constraint, and
the filter puts things in front of me that I cannot use without opening my wallet. A cost
filter that ignores the cost is not a cost filter.

**5c. The site contradicts itself on the very same title**

```
python -c "import json;from collections import defaultdict;items=json.load(open('data/items.json',encoding='utf-8'));
g=defaultdict(list); [g[i['title']].append(i) for i in items];
[print(t,len(v),sorted({x['cost'] for x in v}),sorted({x['level'] for x in v})) for t,v in g.items() if len(v)>1]"
→ AI Fluency: Framework & Foundations   3 ['free','free-account'] ['basic','never-used']
→ 15 Claude Tips for Everyday Data Analysis 2 ['subscription'] ['basic']
→ Model Context Protocol: Advanced Topics 2 ['free-account'] ['builder']
→ Getting started with Claude in Excel  2 ['free','subscription'] ['basic']
```

Two entries, same title, same author (Anthropic), same product — **"Getting started with
Claude in Excel"**. One is chipped `subscription` and says the add-in "needs a paid Claude
plan plus Microsoft 365". The other is chipped `free`. I am shown the `free` one. The site
has both answers on file and hands me the wrong one.

And **"AI Fluency: Framework & Foundations" exists three times**. Two of those three are in
my 54 — one at `never used Claude` (Coursera, `free, sign-up needed`, no publish date), one
at `used it a little` (Anthropic Academy, `free`, published 1 Jun 2025). Same 4D framework,
same two professors. One summary calls it ten modules and three hours; the other calls it a
half day. I am sold the same course twice, at two different levels, with two different cost
chips and two different lengths. Add `AI Fluency for Small Businesses` and `AI Fluency for
Nonprofits` and **4 of my 10 courses are the same framework in different packaging.**

---

## 6. Search, in my words

The three sentences I would actually type. Reproduced with
`python scripts/test-search.py "<sentence>"`.

**"will this save me hiring someone"** → 8 results.

```
  20.4  [developer]        The CLAUDE.md file
  15.5  [business-founder] Small Business plugin (skill inventory)
  12.2  [developer]        Hooks reference (Claude Code)
```

I ask whether an AI can do the job of a person I would otherwise hire. The top answer is a
developer reference page about a configuration file. Third is `Hooks reference (Claude
Code)`. Two of my top three are engineering documentation.

**"is my customer data safe"** → 11 results. Top three are right:
`AI Fluency for Small Businesses` (46.0), `Is my data used for model training? (Privacy
Center)` (26.4), `Use Claude Cowork safely` (26.4). Then it goes to
`Claude for Teachers: your data and our terms` and a UK schools toolkit. Good start, then
somebody else's classroom.

**"how much does it cost for 5 staff"** → 12 results. Top two are correct and useful:
`Plans & Pricing` and `Claude Team pricing for a small business`. Then `Using AI in
university` and `The CLAUDE.md file` at rank 3 and 4.

So the ranking is decent on money and privacy, poor on the labour question, and it never
respects who I said I was.

**Now the part that made me want to close the tab.**

The home page invites me to type a sentence: `Or describe what you want to do…`. I typed
one, pressed **Show me**, and landed on:

`browse.html?role=business-founder&level=basic&q=will+this+save+me+hiring+someone`

Live, in a browser, with JavaScript state read straight from the page:

```
{ count: "0 resources",
  empty: "No match for “will this save me hiring someone”.\nTry fewer words, or browse by role instead.",
  indexReady: false,
  title: "Browse 0 Claude resources — Learn Claude" }
```

**Zero.** Then I clicked in the search box and typed a single space — one character, which
changes nothing about the question:

```
{ q: "will this save me hiring someone ",
  count: "1 resource. Remove a filter to see more.",
  indexReady: true,
  titles: ["Small Business plugin (skill inventory)"] }
```

The same query. 0 → 1. `indexReady` flipped `false` → `true`.

The cause is in the code. `assets/js/search.js` loads the 255 KB keyword index **only on
the first keystroke** in the Browse box. `assets/js/browse.js` reads `?q=` from the URL on
load and renders immediately, and its fallback is plain substring matching — every word in
my sentence has to appear literally in a title, summary, `who_for` or source. I checked all
three of my sentences against that fallback:

```
substring fallback, exactly as browse.js matches() does when the index is absent:
  "will this save me hiring someone"   → 0
  "is my customer data safe"           → 0
  "how much does it cost for 5 staff"  → 0
```

**Every sentence typed on the home page returns "No match".** The home page asks you to
describe what you want, then tells you it has nothing. The site owns the answers. It just
has not loaded them yet, and nothing on that page ever will.

I would have left here. I only did not because I had already read the data file.

---

## 7. On a phone

I measured a real 390×844 viewport by loading the live pages in a same-size frame and
reading the layout back.

Browse, `?role=business-founder&level=basic`:

```
{ vw: 387, scrollW: 372, clientW: 372, overflowX: false,
  railHidden: "none", barVisible: "block",
  count: "35 resources", cards: 35, tooSmallTapTargets: 1 }
```

This is fine. No sideways scroll. The filter column is hidden and replaced by a bar pinned
to the bottom where my thumb is. All 35 cards render. Exactly one control is under the
44px minimum the stylesheet sets for itself — the `Learn Claude` wordmark in the header, at
40px high.

Home at the same width: no sideways scroll either, single 340px column, and the drawing
still loads at 280×280 — at `artTop: 905`, so it is below the fold and costs me a picture I
never see. The count line sits at y=849 on an 844px viewport. Off screen.

The path page at 390px: no overflow, steps stack cleanly.

Phone is the best-built part of this site. I have no complaint here. Which makes the rest
harder to forgive — somebody clearly cared, just not about me.

---

## 8. Content quality — the three worst entries I was shown, quoted

**1. `AI Fluency for Nonprofits`** — Anthropic Academy, course, `used it a little`.
Its `Skip if:` line, verbatim:

> "You run a for-profit business — use the small-business version."

I run a for-profit business. That is the role I selected. The site put a card in my list
whose one-line summary of who should skip it is *a description of me*. Nobody checked. It
is not a judgement call, it is a two-second check that was never run.

**2. `AI for Small Business: Getting Started with Claude (SBA event)`** — card 10 of 10 at
`never used Claude`, format `course`, badge **`Found only`** (which the site itself defines
as *"We found it and sorted it. Nobody has looked at the content yet."*).

> `published 2026-08-05`
> `Skip if: The listed date has passed — check sba.gov for the next scheduled session.`

I checked the URL: `curl -s -L -o /dev/null -w "%{http_code}" https://www.sba.gov/event/85201`
→ **200**, and the page says **"Date and time … day, August 5, 2026"**. That event happened
22 days ago. The site lists a webinar that is over, as a course I can take, in the list it
gives to a person on their first day, and its own note admits the date may have passed.

The link is not dead, so the site counts it as healthy. `00-facts.md` says **0 dead links**.
That number is measured on HTTP status, not on whether the thing still exists. A 200 on a
finished event is a worse failure than a 404, because a 404 at least tells me.

**3. `Everyone should be using Claude Code more`** — Lenny's Newsletter, `subscription`,
`never used Claude`, published 14 Oct 2025.

> "…it is a list of what other people do, most of it sits behind a paid subscription, and
> it dates from October 2025 so it predates Cowork."

Paid, superseded, and inspirational rather than instructive. The site wrote all three of
those things down and put it in the ten-card list for someone who has never opened Claude.
There is no price on the card.

Dishonourable mention: `Claude Design: The Complete Guide`, in my `used it a little` list,
`Skip if: Skip if you have no design background - the critique assumes you can tell good
layout from bad.`

---

## 9. Everything that is broken, ranked

**9.1 — A sentence typed on the home page always returns nothing.**
`browse.html?q=…` renders before the search index loads, and nothing on that path ever
triggers the load — `assets/js/search.js` `load()` is called only from the `input` handler
in `assets/js/browse.js`. Live evidence: `?q=will+this+save+me+hiring+someone` →
`count: "0 resources"`, `indexReady: false`. Typing one space → `count: "1 resource"`,
`indexReady: true`. All three of my sentences return 0 through the substring fallback and
8, 11 and 12 through the real index. The home page's own invitation — *"Or describe what
you want to do…"* — leads to a dead end 100% of the time.

**9.2 — The `free` chip is not a claim about money I can rely on.**
5 of my 48 `free`-chipped cards need a paid Claude plan before the content is usable
(`prerequisites` name it; `skip_if` says it in plain words). One more hides a `$99`
upgrade behind the word "free". Command and full list in 5b. Site-wide the same pattern
hits 9 of 353.

**9.3 — Two cards for the same thing give opposite cost answers.**
"Getting started with Claude in Excel" exists twice: one `subscription`, one `free`. I am
shown the `free` one. "AI Fluency: Framework & Foundations" exists three times, two of them
in my 54, at two different levels with two different cost chips and two different stated
lengths. Command in 5c.

**9.4 — The `builder` level for "running a business" contains nothing about running a
business.** All four items are tagged `pm` or `developer`; two of the four tell me in their
own `Skip if:` to go away (`"You're non-technical — use the one-click built-in connectors
instead."`, `"You want simple consumer one-click tools."`). Verified live at
`browse.html?role=business-founder&level=builder`. `confident` is barely better: 1 of 5 is
business-specific, the other four are three YouTube videos and a link directory.

**9.5 — The path that names me is mostly not for me.**
4 of the 6 steps in `Your first week with Claude` are tagged for other roles only
(`non-technical` ×3, `researcher` ×1). Not one of the six `why` lines mentions cost, staff,
customers or risk. Step 1 is a personal-brand Substack newsletter with no publish date,
which the site's own note flags as *"the kind of creator-newsletter content the research
brief specifically warned about"*.

**9.6 — A finished event is still on sale as a course.**
`AI for Small Business: Getting Started with Claude (SBA event)`, published 2026-08-05, is
card 10 of 10 at my entry level. The event date has passed (sba.gov confirms 5 August 2026);
the URL returns 200, so the site's dead-link count of 0 does not catch it. Nothing in the
data model can express "this was a one-off and it is over" — `status` only has `live` and
`dead`.

**9.7 — The publisher line prints a domain fragment.**
`Open on Vc`, `Found through Vc`, `To · Marcus Moretti, GM of Spiral at Every`. Both seen
live. `assets/js/ui.js` states the rule this breaks — *"it is the publisher, not the
platform"* — and 61 of 353 cards break it (`GitHub` 31, `Substack` 11, `Coursera` 8,
`Medium` 4, `Udemy` 4, `To` 2, `Vc` 1). On a directory whose product is trust, "Vc" on a
button is self-harm.

**9.8 — There is no price anywhere, for anything.**
32 items site-wide are chipped `subscription` or `pay once`; 3 of them state a number. In
my 54 exactly one card contains a currency figure, and that card is chipped `free`. For the
one role on this site defined by spending its own money, "subscription" is not information.

**9.9 — 29 of my 54 `For:` lines do not mention anyone who runs anything.**
Command in section 3. Combined with only-this-role 18 of 54 (`00-facts.md`, lowest of any
role), two thirds of my catalogue is somebody else's shelf with my label added.

**9.10 — Four filter options return zero for me** (`multi-day`, `api`, `podcast`,
`pay once`), 4 of 27. The empty state that follows suggests loosening *time*, which is
wrong advice for three of the four.

**9.11 — The attack tool does not reproduce the site's card order exactly.**
`docs/attack/role-view.py:47` ties-breaks on Python's `i.get("title","")`, which sorts
uppercase before lowercase; `assets/js/browse.js:113` uses `title.localeCompare(title)`,
which does not. At `builder` the live site shows `awesome-mcp-enterprise` second;
role-view.py shows it third. Small, but anyone quoting "the order Browse shows them" from
that script is quoting it slightly wrong on ties.

**9.12 — A number in the code has drifted from the data.**
`assets/js/ui.js`, `LC.freshness` comment: *"176 of 353 resources publish no date at all"*.
The file says 171 (`00-facts.md` agrees; verified by counting `published == "UNVERIFIED"`).
Invisible to a visitor, but it is the same class of mistake as 9.6: a number written once
and never re-derived.

---

## 10. The one thing that would make me leave and not come back

The home page tells me to describe what I want. I describe it. It says **"No match for
'will this save me hiring someone'."**

It has eight answers to that question sitting in a file it already shipped to my browser.
It just did not load the index, and on that route it never will. So the site's own front
door hands me its emptiest possible screen, on my first real question, in my own words.

I would not tick a box or read a taxonomy after that. I would assume the directory is thin
and go back to YouTube. **9.1.** Nothing else on this list matters if people leave in the
first minute, and this is engineered to make them leave in the first minute.

Runner-up, and the reason I would not come back even if 9.1 were fixed: I filtered by
**free** because money is my constraint, and got back five things I cannot use without
buying a Claude plan first. If the one chip aimed at me is not true, I have no reason to
believe the other chips either.

---

## 11. What is genuinely good (be honest, but brief)

- **`Skip if:` is the best idea on this site.** No other directory tells me who should not
  bother. It is also, ironically, the evidence for half of section 9 — the lines are honest
  enough to convict the cards they sit on.
- **The two-question front door is fast and the count is exact.** "54 resources match so
  far" before I click, and no rounding. I knew where I stood in ten seconds.
- **The phone build is genuinely careful.** No sideways scroll on any page I checked, the
  filter rail becomes a thumb-height bar, one control under 44px on the whole page. Someone
  measured this instead of guessing.
- **The badges do not flatter.** `Skimmed` says "We read the outline or a free sample". Most
  sites would have called that "reviewed". This one did not, and *"We would rather have 70
  resources we can vouch for than 700 we cannot"* is the right instinct — even though there
  are 353 and nothing is at the top badge.
- **Search ranking, once it loads, is better than I expected.** "is my customer data safe"
  and "how much does it cost for 5 staff" both put the right card first, with no shared
  words. That is real work. It seems to me the only thing wrong with search is when it
  loads, not how it ranks.

---

## Checklist — every line ticked or the file is not finished
- [x] I opened the live site (home, browse, resource ×2, paths, all at
      `https://mojtaba-alehosseini.github.io/learn-claude/`, plus curl for HTTP evidence)
- [x] I tried all four levels (10 / 35 / 5 / 4, read live from `#tally`)
- [x] I quoted at least 5 real titles or lines from the site (well over 20: `AI Fluency for
      Nonprofits`, `AI for Small Business: Getting Started with Claude (SBA event)`,
      `Everyone should be using Claude Code more`, `Claude Design: The Complete Guide`,
      `Getting started with Claude in Excel`, `Claude is not one tool. It's six.`,
      `awesome-mcp-enterprise`, `The ONLY Claude Cowork Tutorial You'll Ever Need in 2026`,
      and their `Skip if:` lines verbatim)
- [x] Every number I used is in 00-facts.md or I show the command
- [x] I looked at a phone width (390×844, measured, not guessed)
- [x] I found at least one thing nobody has mentioned before (9.2 the false `free` chip,
      9.3 the same title with two opposite cost chips, 9.6 an event that is over still
      listed as a course while counting as a live link, 9.7 `Open on Vc`, 9.8 no price
      anywhere, 9.11 role-view.py's tie-break disagreeing with the live sort)
