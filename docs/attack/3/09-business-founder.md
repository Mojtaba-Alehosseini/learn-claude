# Attack 3: running a business
Written as somebody running a small business, 2026-09-06. Site version: 9deb0db.

I run a company with under twenty people. I do the invoices, the quotes, the hiring and
the marketing, often on the same day. I have no IT department. Two questions decide
whether I touch this at all: **what does it cost me**, and **is my customer data safe**.
Everything below is judged against those two questions.

---

## 1. The first 60 seconds

I opened `https://mojtaba-alehosseini.github.io/learn-claude/`.

The page says:

> Find what's worth your time.
>
> I'm a [role] and I've [level].

Then two rows of buttons, then:

> 588 resources, each with a reason to skip it and the date we last looked.

That is a good front door. Two questions, ten roles, four levels, no sign-up, no cookie
banner, no newsletter box. "running a business" is one of the ten roles. In ten seconds I
knew this site thinks I exist. Most directories do not.

Three promises sit under the buttons:

> We say when to skip — Every entry has a `Skip if:` line. A link with no judgment is just
> a list, and lists are what made this hard in the first place.

I agree with that sentence more than the people who wrote it probably know. That is the
whole reason I would use a site like this instead of searching.

**What is missing in the first 60 seconds:** nothing on the home page mentions money or
data. The word "cost" does not appear. The word "privacy" does not appear. For me those
are the entry conditions, not a later chapter.

**I watched the page for 42 seconds and touched nothing.** The sentence stayed at
`I'm a [role] and I've [level].` the whole time. It never filled itself in, never cycled
through an example, never moved. Measured on the live page: 42 seconds watched, zero
changes to the two blanks, `prefers-reduced-motion` off, computed `animation-name: none`
on both the blank and its text. The sentence is a form with two holes in it, and it never
shows me one filled-in example of what a filled-in sentence produces. See finding 9.

---

## 2. Does the front door work for me (all four levels, with what I was shown)

I answered "running a business" and then each level in turn.

| level I picked | URL I landed on | resources |
|---|---|---|
| never used Claude | `browse.html?role=business-founder&level=never-used` | **37** |
| used it a little | `browse.html?role=business-founder&level=basic` | **62** |
| used it a lot | `browse.html?role=business-founder&level=confident` | **45** |
| built things with it | `browse.html?role=business-founder&level=builder` | **9** |

All four match STATUS.md's per-cell table for `business-founder` (37 / 61 / 45 / 9); the
one extra at "used it a little" is the freshness-excluded row, which STATUS.md says still
appears in Browse. Nothing here is invented and nothing is broken.

With no level chosen, `browse.html?role=business-founder` gives **153**. Adding the four
level cells gives 153 as well. The arithmetic holds.

**Level 1 — never used Claude (37).** The best result of the whole hour. "Start with these
three" opened with:

> **Is my data used for model training? (Privacy Center)** — Claude Privacy Center · Anthropic
>
> For: Anyone worried about data privacy — the #1 SMB hesitation.
>
> Our own card calls this the number-one small-business hesitation, and this is the only
> candidate that answers it from policy - the page to quote to a worried co-owner, read by
> AI in full.

That is exactly right. It put my second question first, and it said why. Pick two was
"How to setup Claude for Small Business" (Harry Davies) — "The shortest path in the pool
from decision to working setup, and honest that it does no convincing". Pick three was
"Claude 101". Why-safe, how-fast, what-it-is. I would follow all three.

**Level 2 — used it a little (62).** Picks were "Claude for Small Business setup (decision
tree + 15 workflows)", "Master Claude for Excel in 10 Minutes: Financial Modeling", and
"What are Projects?". The first one's reason is the best sentence on the site:

> The only candidate built to be read before installing rather than after - it names the
> three cases where the plugin adds nothing, and compares itself honestly to the
> competition, which its own card notes is rare in this genre.

A recommendation that tells me when the thing is worthless. Good.

**Level 3 — used it a lot (45).** Picks were "Teach Claude your way of working using
skills", "My Simple Claude Cowork System (for normal people)" (Jeff Su), and
"knowledge-work-plugins/small-business (source repo)". Pick three is a GitHub repo. I do
not read source. Its own card says "This is the source, not the product." Two of three
are useful; one is aimed at somebody else. Then positions 4 to 8 are the five collection
cards in a block — see section 8.

**Level 4 — built things with it (9).** This is where the front door stops working for me.
The three picks were:

1. "Agent-native Product Management (Every's guide)"
2. "awesome-mcp-enterprise" — GitHub · bh-rat (community)
3. "Introduction to Model Context Protocol" — Anthropic Academy

Pick 3's own Skip if line says:

> You build the servers here rather than install them, in Python, from scratch.

I run a business. If I answered "built things with it" I meant I built a workflow, a
Project, a set of skills — I did not mean I write Python servers. Two of my three picks at
my own top level are a community GitHub list and a Python course. The rest of the nine
includes "Claude Cowork Enterprise Admin Guide" (written, in its own words, "for a rollout
team on a paid Enterprise plan") and "Claude for nonprofits partnership success guide for
admins". Nine resources, and the level's answer to a twenty-person company is either
enterprise rollout documentation or Python.

**Verdict on the front door:** it works well at levels 1 and 2, thins at 3, and at level 4
it hands a business owner other people's jobs.

---

## 3. What the catalogue actually gives me (are these really for me?)

Across my whole role (`browse.html?role=business-founder`, 153 cards), measured on the
live page:

- **137 of 153** carry the badge **Skimmed**. 16 carry **Read by AI**. **0** carry
  **Read in full**.
- **124 of 153 (81%)** say **"No publish date given"**. That is worse than the site-wide
  75% in STATUS.md.
- **5 of 153** are not free. **0 of those 5** show a price. See finding 4.

So: nine out of ten cards in my role are a machine's skim of a page with no date on it.

Are they for me? Mostly yes at the low levels, and the writing is good. "Claude Team
pricing for a small business" — "Seat math for 3–15 person teams, when an API key beats a
seat, and worked examples at 5 and 12 people" — is the single most useful line on the
site for somebody in my chair, and it is not a pick anywhere.

Where it stops being for me is anything that needs somebody else. Counting only the five
collection cards at "used it a lot", the Skip if lines require, between them: Cowork with
Salesforce or HubSpot connected; "a workspace admin enabling a Claude for Legal plugin on
Team or Enterprise"; "NetSuite, Microsoft 365 or a self-hosted connector"; "a calendar,
Drive or payroll connector". I have none of those and nobody to set them up.

**The filter I need does not exist.** The Topic filter offers exactly eight topics:

> chat and prompting · Claude Code · Cowork · Skills · connectors · agents · API ·
> limits and safety

Six of those eight are product surfaces a developer cares about. There is no topic for
**cost**, **plans**, or **privacy and data**. The two questions that decide whether I use
this tool at all cannot be filtered for. "limits and safety" is the nearest, and on the
cards it turns out to mean usage limits and hallucination. The taxonomy is built around
Anthropic's product menu, not around a buyer's questions.

---

## 4. Paths

There are 7 paths (STATUS.md: 7 paths, 36 steps). Exactly one of them lists me:

> **Your first week with Claude**
>
> Anyone who has just opened Claude and does not know what to do next.
>
> For not a coder, a student, a teacher, running a business
>
> 6 steps · about 4 hours · free

That is my only route, and it is the beginner route, shared four ways. **There is no path
for running a business at any level above the first week.** Compare what every other role
gets:

- a developer → "Getting good at Claude Code"
- a writer → "Using Claude on work you put your name to"
- a product manager → "Product work without waiting for engineering"
- working with data → "Analysing your own data without getting the numbers wrong"
- a designer → "Judging AI's design output"

Every one of those has a sharp promise owned by that role. `running a business` is the
**largest role pool in the catalogue** — 153 on the live Browse, more than any other role
in STATUS.md's per-cell table — and it is one of three roles (with "not a coder" and "a
teacher") that has no path of its own.

**I followed the path anyway.** `paths.html?id=first-week`. Six steps:

1. Claude is not one tool. It's six.
2. Get started with Claude
3. Claude 101
4. What are Projects?
5. Why do AI models hallucinate?
6. Get started with Claude Cowork (Help Center)

**Not one step is about money. Not one step is about data.** The site's own top pick for a
business owner who has never used Claude is the data-privacy page, and its own card calls
that "the #1 SMB hesitation" — and the path built for that same person leaves it out.
The picks block and the path disagree about what matters most to me, on the same site, at
the same level.

Also: **all six steps say "No publish date given."** Six out of six, on a path about a
product the home page says "changes every few months."

---

## 5. The card and the resource page

I opened three resource pages.

**`resource.html?id=r-dbd5a58a87` — "Is my data used for model training? (Privacy Center)".**
Would I click through? Yes, immediately. The page gives three "What it teaches" bullets
("Assess whether Claude meets your company privacy standards"), the who-it's-for, the
skip-it-if, the tier spelled out in words with a link, and the outbound link is labelled
"Open on Claude Privacy Center" so I know where I am going before I go. This is a good
page.

**`resource.html?id=r-0927578f60` — "Claude Team pricing for a small business".**
Would I click through? Yes. It is the thing I came for. Two things I noticed that the card
does not tell me: the publisher is **SSD Nodes** and the destination is
`ssdnodes.com/learn/claude-team-plans-small-business`, and the badge is **Skimmed** —
"We read the outline or a free sample. We have not seen the whole thing." So the site's
best cost advice for me is a third-party vendor's page that nobody here has read. Its own
Skip if line half-admits it: "You prefer the official pricing page (this adds
interpretation, not authority)."

**`resource.html?id=r-d91d3354ec` — "Mastering Claude Cowork & AI Agents in 5 hours" (Udemy).**
Would I click through? **No.** See finding 4.

**Can I find out what the badge means?** On the resource page, yes and clearly:

> How we checked this one
> Skimmed. We read the outline or a free sample. We have not seen the whole thing. How we check.

with "How we check" as a link. On the **card**, no. The badge is a `<span>` with
`tabindex="-1"` and a `title=` attribute. `title` shows on mouse hover only. There is no
link to `how-we-check.html` anywhere inside the results area of Browse — I checked every
`<a>` in `<main>` and found none. A screen reader gets the text through
`aria-describedby` on the title link; a sighted person using a keyboard, or anyone on a
phone where hover does not exist, gets nothing from the card. The tier descriptions are
correctly hidden in a `.visually-hidden` wrapper, so this is a missing affordance, not a
layout bug.

---

## 6. Search, in my words

I typed each of these as a whole sentence into the home page box ("Or describe what you
want to do…"), which submits to `browse.html?q=…`.

| # | what I typed | top 3 I was shown | verdict | why |
|---|---|---|---|---|
| 1 | how much is this going to cost me every month | 1. How context affects Claude's performance and cost · 2. Find the cloud cost anomaly · 3. claude-cookbooks: Skills notebooks | `bad` | All three are about somebody else's cost. #1 is API token cost, #2 is cloud infrastructure anomaly detection, #3 is code notebooks. The right answer, "Claude Team pricing for a small business", is at #5, and "Plans & Pricing" and "Choose a Claude plan" are nowhere in the top 5. It matched the word "cost" and ignored "me" and "every month". |
| 2 | is my customer data safe if I paste it into Claude | 1. AI Fluency for Small Businesses · 2. How long do you store my data? · 3. Working smarter with Claude in PowerPoint | `ok` | #2 is a genuine answer — retention figures from Anthropic. But #3 is PowerPoint, and the site's own #1 pick for exactly this worry, "Is my data used for model training? (Privacy Center)", sits at **#17 of 27**. A useful answer is in the top three by luck, not by rank. |
| 3 | can it write my quotes and invoices for me | 1. Small Business plugin (skill inventory) · 2. Organize your business finances · 3. Claude Cowork for Product Managers: A Working Guide | `ok` | #1 and #2 are the right shelf — a skill inventory and a finances recipe. #3 is a product manager's guide and has nothing to do with invoicing. Two of three is a pass. |
| 4 | I have nobody in IT, can I set this up myself | 1. Claude Managed Agents overview · 2. Teach Claude your way of working using skills · 3. What does AI know about me? | `bad` | The worst result of the five. #1 is server-hosted agents — the most technical thing on the site — handed to a question that opens "I have nobody in IT". #3 is a privacy essay. At **#6** sits "I Built an Agentic Software Factory with Codex and Claude Code". The site's own recommended answer, "How to setup Claude for Small Business" ("the shortest path from signup to a working setup"), is at **#35 of 43**. |
| 5 | what should I use it for first in a small company | 1. AI Fluency for Small Businesses · 2. How to setup Claude for Small Business · 3. Claude for Small Business plugin: 31 skills that run your operations | `ok` | The best of the five. All three are on the subject, at my level, for my situation. This is what the search is capable of when the wording happens to match. |

**The same question asked two ways.** I asked my data question twice.

- Wording A: **"is my customer data safe if I paste it into Claude"** → 27 results. "Is my
  data used for model training? (Privacy Center)" ranks **#17**.
- Wording B: **"does Anthropic train on the files I upload"** → 51 results. The same page
  ranks **#1**.

**The site did not agree with itself.** Same question, same intended answer, rank 17
versus rank 1. Wording B is the one that uses the site's own vocabulary ("train",
"upload"). Wording A is the one an actual owner types, and it buries the page that the
site itself hand-picked as the number-one answer for my role.

---

## 7. On a phone

Tested at 375×812.

**What works.** No horizontal overflow on the home page or on Browse —
`documentElement.scrollWidth` is 375 on both, so nothing spills sideways. Role buttons are
44px tall and the "Show me" button is 52px; both are comfortable taps. The filter rail
collapses into a single "Filters" button, also 44px. Card width 343px inside a 375px
viewport. The layout is genuinely responsive and somebody did the work.

**What does not.** There is no pagination and no "load more". At phone width:

- My filtered list (`role=business-founder&level=never-used`, 37 cards) renders a page
  **22,568px** tall — about **28 phone screens**, median card height 519px, tallest 779px.
- The unfiltered `browse.html` renders all **588** cards into a page **321,320px** tall —
  about **396 phone screens**.

"Browse" is in the top navigation of every page. Tapping it on a phone gives you a
four-hundred-screen scroll with no way to page through it. On my own role alone (153
cards) it is roughly a hundred screens. Filtering is the only defence, and the filter rail
is behind a button.

The card is also the wrong shape for a phone. Each one carries a badge, title, publisher,
three chips, a "For:" paragraph, a "Skip if:" paragraph and a date row. That is excellent
on a laptop and it is 519px of thumb on a phone — one and a bit cards per screen. There is
no compact view. Scanning thirty-seven things at a bus stop is not possible here.

---

## 8. What changed since Attack 2 — my verdict on each

**The five collection cards.** Sales, Legal, HR, Finance, Operations.

*Do I understand what one is before I click it?* **Yes, just about.** The title "Use cases
for Sales" plus the Skip if line does the job: "This is a menu, not a lesson: every recipe
needs Cowork with Salesforce or HubSpot connected, and none of them teaches you anything
about Claude itself." That is honest and it stopped me clicking, which is what a Skip if
line is for.

*What happens when I click?* The resource page is better than the card. "The Academy's
use-case gallery filtered to its Sales department: eleven recipes for account research,
call prep, pipeline review, proposal decks, sales reports, battlecards, renewal risk and
CRM logging." The destination is `academy.claude.com/use-cases?department=sales`. No
surprise, no bait. Good.

*The problem.* They arrive as a block. At "used it a lot" they occupy positions **4, 5, 6,
7 and 8** of 45 — five near-identical rows, all "Skimmed", all "No publish date given", all
"Checked 6 Sep 2026", one after another, each one a link to a filter on somebody else's
site. And for a company my size, four of the five need something I do not have: a
Salesforce or HubSpot connector, a workspace admin on Team or Enterprise, NetSuite or
Microsoft 365, a payroll connector. Two of them state outright that they teach "nothing
about Claude itself". So five of my top eight at my own level are menus I cannot order
from. As a founder I do not trip over them. I skip all five and my level got thinner by
five.

**Prices on the paid rows.** **No.** This is finding 4 and it is bad. Across the whole
catalogue, 26 rows are not free and only **4** carry a price chip ("from $49", "from
$995", "from $2,999", "from $3,000"). All four belong to other roles. In **my** role, all
**5** non-free rows show a cost word and no number:

> Claude Cowork 7-Day Challenge · course · 1 hour · **subscription**
> Everyday Productivity with Claude Cowork · course · 1 hour · **subscription**
> Mastering Claude Cowork & AI Agents in 5 hours · course · half a day · **pay once**
> Anthropic Claude for Absolute Beginners · course · 1 hour · **pay once**
> Claude, Claude Code, Claude Cowork, and Claude in MS Office · course · half a day · **pay once**

The role whose entire question is "what will this cost me" is the one role that gets no
prices. Zero of five.

**The stripped `listed` cards.** They read as **honest but incomplete**. All three carry
the same line — "Skip if: You want something we have read. We have not opened this one
yet." — and the badge "Found only". I respect that. Two things spoil it. First, they have
**no "For:" line at all**, only a "Skip if:", while every other card has both — so the card
is missing the half that tells me who it is for, and it looks like a rendering failure
rather than a deliberate stub. Second, one of the three is
"Head of Claude Code: What happens after coding is solved (Boris Cherny)" — chips
`podcast · half a day · subscription`. That is half a day of my time behind a paid
subscription with no price, that nobody here has opened. Listing it is defensible.
Listing it with no price and no verdict is not.

**"How well checked" as a filter.** The definition is reachable from the **resource page**
(spelled out in words with a link to "How we check"), and from the card by mouse hover
only. Not reachable from a card by keyboard, and not reachable on a phone. Half a pass.
And using the filter produces the worst bug on the site — see finding 1.

**The thin-level offer.** Not offered to me. My thinnest cell is "built things with it"
at 9, which is above the threshold, so I never saw the one-click line. I cannot judge it.

**Date lines.** They make the site look **carefully honest and badly maintained at the same
time**, which I think is the truth. The good part: the freshness note works and it is
blunt — "Published 29 Jul 2025 · over a year ago, may not match Claude today". I trust a
site that says that. The bad part: 124 of my 153 cards (81%) say "No publish date given",
and every step of the only path I am offered says it. STATUS.md explains that this went up
on purpose because unverifiable dates were cleared, and I believe it — but a visitor does
not read STATUS.md. A visitor sees four cards in five with no date and concludes nobody is
minding the shop.

**Who "we" is.** It **raises my trust and lowers my confidence**, and I mean both.
`how-we-check.html` says:

> One person makes this site - a researcher at the Technical University of Denmark,
> working on it outside their job. ... The reading is done by Claude ... A person sets the
> rules ... and has not yet read a single resource end to end.

Nobody writes that unless they mean it. I trust the author. But what the disclosure
discloses is that the thing I came for does not exist yet. The home page sells "We say
when to skip — a link with no judgment is just a list", and the judgment is an AI's. On
the front of a card, "we" reads as a person. You have to reach the third page to learn
otherwise. That is not dishonest, but it is a slow reveal of the most important fact about
the product.

**The picks block.** Read the reasons — yes, and they are the best writing on the site. At
never-used, the three picks and their three reasons made a coherent argument (why-safe,
how-fast, what-it-is) and I would open all three. At builder they picked a Python course
for somebody who runs a shop.

**Social preview title.** Broken. Finding 3.

**Home attract loop.** Does not exist. Finding 9.

**Sort control.** Half broken. Finding 5.

**Paths above beginner level.** None for me. Section 4.

---

## 9. Content quality — the three worst entries I was shown, quoted

**1. "Where can I access Claude? (country availability)"** — shown to me at
`browse.html?role=business-founder&level=never-used`. The card's own note says:

> Skip if: **The title is wrong for what this is.** It promises somewhere to access Claude
> and delivers geography - if you want to know whether to use the web app, the desktop app
> or the mobile app, this is the wrong page and 'What interfaces can I use to access
> Claude?' is the right one. Skip entirely if you are in North America or Western Europe;
> you are on the list.

The site knows the title is wrong, knows the page is the wrong page, knows most readers
should skip it entirely — and still puts it in the list of 37 things it thinks a business
owner who has never used Claude should look at. A directory whose job is filtering should
have filtered this.

**2. "Mastering Claude Cowork & AI Agents in 5 hours"** — Udemy, shown at "used it a lot".
Chips on the card: `course · half a day · pay once`. Chips on the resource page: identical.
No price on either. I checked the full resource page text for any currency symbol and
found none. Its badge is **Skimmed**:

> We read the outline or a free sample. We have not seen the whole thing.

So I am being offered half a day of my time, for an unstated amount of money, on something
nobody here has read. Three unknowns stacked on one card.

**3. "What are some things I can use Claude for? (Help Center)"** — shown at never-used.
Its own note:

> Skip if: Two hundred and fifty words and no depth on any of the seven - if you already
> know what you want to ask, it has nothing for you. **It is also older than the product:
> written before Cowork, Skills and connectors, so it describes a chat box and not the
> thing Claude is now.**

"Older than the product" and "describes a chat box and not the thing Claude is now" is a
retirement notice, not a review. It carries "No publish date given", so the freshness flag
that would have warned me cannot fire. The note is excellent. The decision to keep the
card is not.

---

## 10. Everything that is broken, ranked (evidence for each)

**Finding 1 — The empty state tells me the site has nothing for my job, and that is false.**
*Severity: worst. It is the one message that ends a visit, and it is untrue.*

- **URL:** `https://mojtaba-alehosseini.github.io/learn-claude/browse.html?role=business-founder&checked=reviewed`
- **What I did:** on Browse with "running a business" selected, opened "More filters +"
  and clicked **"Read in full"** — the top rung of the ladder, and the obvious thing to
  click if you want the best-checked material.
- **What I saw, quoted in full:**
  > 0 resources for running a business
  > **We have not covered this role yet. It's on the list.** Browse everything instead.
- **What I expected:** "Nothing has been read in full yet" — which is what
  `how-we-check.html` says on its own page: "Today the count read in full is zero".
- **Reproduces on other roles.** `?role=developer&checked=reviewed` returns
  "0 resources for a developer — **We have not covered this role yet. It's on the list.**"
  STATUS.md's per-cell table gives `developer` 118 eligible resources. The message is chosen by
  *which filters are set*, not by *which filter emptied the result*, so the role always
  takes the blame.
- **It also misfires without a role.** `?checked=reviewed` alone returns "Nothing matches
  all of those. Try removing one filter — **time is usually the one to loosen**." No time
  filter was set.
- **Who it harms:** every visitor who tries the top badge. The site told me it holds 153
  resources for me one screen earlier. Now it says it has not covered my job. One of those
  two statements is a lie, and the reader has no way to tell which. I nearly closed the
  tab here, and I would have left believing this site is not for business owners.

**Finding 2 — Search does not agree with itself about the most important question I have.**
*Severity: very high.*

- **URLs:** `browse.html?q=is+my+customer+data+safe+if+I+paste+it+into+Claude` and
  `browse.html?q=does+Anthropic+train+on+the+files+I+upload`
- **What I saw:** the page "Is my data used for model training? (Privacy Center)" ranks
  **#17 of 27** for the first wording and **#1 of 51** for the second.
- **What I expected:** the same page near the top for both, because they are the same
  question.
- **Who it harms:** me, most. That page is the site's own number-one pick for a business
  owner at never-used level, and its own card calls it "the #1 SMB hesitation". The
  wording that fails is the plain-English one; the wording that works is the one using the
  site's vocabulary. Search rewards people who already know the site's words.

**Finding 3 — Every shared link previews as "Resource — Learn Claude".**
*Severity: high.*

- **URL:** any resource page, e.g.
  `resource.html?id=r-dbd5a58a87` (Is my data used for model training?) and
  `resource.html?id=r-0927578f60` (Claude Team pricing for a small business).
- **What I saw:** `document.title` is correct — "Is my data used for model training?
  (Privacy Center) — Learn Claude". But `og:title` on **both** pages is the static string
  **"Resource — Learn Claude"** and `og:description` is the static
  "What this resource teaches, who it is for, who should skip it, and how thoroughly we
  checked it." Browse is the same: `og:title` is "Browse — Learn Claude" whatever the
  filter, even though the tab correctly reads "Browse 37 Claude resources — Learn Claude".
- **What I expected:** the resource's own name in the preview.
- **Who it harms:** me and my business partner. Every resource page carries a **"Copy
  link"** button, so the site actively invites me to share. When I paste that link to my
  co-owner or my accountant, they see "Resource" and a generic sentence, and all 588
  resources look identical. The one thing I would genuinely do with this site — send a
  colleague the privacy page before we decide — is the thing that does not work.

**Finding 4 — Not one paid row in my role shows a price, on the card or on its own page.**
*Severity: high.*

- **URL:** `browse.html?role=business-founder`
- **What I saw:** 5 of 153 rows are not free. All five show only a cost word — three "pay
  once", two "subscription" — and no number. Across the whole 588, 26 rows are not free
  and only 4 carry a price chip; all four belong to other roles. On
  `resource.html?id=r-d91d3354ec` the paid Udemy course shows no currency symbol anywhere
  in the page text.
- **What I expected:** a price, or "price not checked", on any row that asks for money —
  especially since `how-we-check.html` already explains that "A paid course is opened at
  its sales page".
- **Who it harms:** the buyer. Four rows on this site prove the price chip exists and
  works. A business owner is the reader most likely to need it and the one who never sees
  it.

**Finding 5 — "Newest first" leaves two thirds of my list out of the sort, and puts a
year-old card above three updated last month.**
*Severity: medium-high.*

- **URL:** `browse.html?role=business-founder&level=basic&sort=newest`
- **What I saw:** of 62 cards, **22 carry a `Published` date and 40 do not**. The 22 sort
  correctly, newest first. The other 40 are dumped below in an order the label does not
  describe. Concretely, in the rendered order:
  - **row 23** — "Claude for Small Business (Back-Office AI, honest review)" —
    `Published 29 Jul 2025 · over a year ago, may not match Claude today`
  - **row 27** — "Get started with Claude Cowork (Help Center)" — `Updated 2 Sep 2026`
  - **row 28** — "What is the Team plan? (Help Center)" — `Updated 18 Aug 2026`
  - **row 30** — "Use Claude Cowork safely" — `Updated 26 Aug 2026`
- **What I expected:** under "Newest first", the thing updated four days ago beats the
  thing the site itself flags as over a year stale.
- **Also:** the "Start with these three" block does not re-sort. Under `sort=newest` the
  visible top of the page still shows a card published 24 Mar 2026 above one published
  30 Jul 2026.
- **Who it harms:** anyone using sort to escape stale material, which for Claude is
  everyone. The control does the opposite of its label for the freshest items on the page.

**Finding 6 — There is no path for running a business, and the one path I am offered
contains nothing about cost or data.**
*Severity: medium-high.*

- **URLs:** `paths.html` and `paths.html?id=first-week`
- **What I saw:** 7 paths. Exactly one lists "running a business", and it is
  "Your first week with Claude", shared with "not a coder, a student, a teacher". Its six
  steps are listed in section 4; none is about money or data safety. Every other role with
  a path gets a role-specific one.
- **What I expected:** something for the owner who is past week one — I have 45 resources
  at "used it a lot" and 9 at "built things with it" and no route through either.
- **Who it harms:** the largest role pool on the site (153 on live Browse, the largest in
  STATUS.md's per-cell table) gets the generic beginner route and nothing else.

**Finding 7 — I cannot filter for the two things I need.**
*Severity: medium.*

- **URL:** `browse.html?role=business-founder`, "More filters +"
- **What I saw:** the Topic filter offers exactly eight values: "chat and prompting,
  Claude Code, Cowork, Skills, connectors, agents, API, limits and safety". No cost. No
  plans. No privacy or data.
- **Who it harms:** every non-technical buyer. Six of the eight topics are a developer's
  map of the product.

**Finding 8 — Nothing in my role has been read by a person.**
*Severity: medium. Known site-wide, but the concentration in my role is worth stating.*

- **URL:** `browse.html?role=business-founder`
- **What I saw:** 137 of 153 cards badged "Skimmed", 16 "Read by AI", 0 "Read in full".
- **Who it harms:** anyone weighing the "Skip if" line as if a person wrote it after
  reading the thing. On my shelf, nine cards in ten are an AI's skim.

**Finding 9 — The home page never shows me what a filled-in sentence looks like.**
*Severity: low-medium.*

- **URL:** `https://mojtaba-alehosseini.github.io/learn-claude/`
- **What I did:** loaded the page and watched it for **42 seconds**, touching nothing.
- **What I saw:** the sentence stayed `I'm a [role] and I've [level].` for all 42 seconds.
  Zero changes to either blank. `prefers-reduced-motion` was off and the computed
  `animation-name` on both the blank button and its text span was `none`.
- **What I expected:** the page's whole idea is a sentence with two holes. Showing one
  filled-in example — "I'm running a business and I've never used Claude" — would explain
  the machine in two seconds without a word of instruction.
- **Who it harms:** the visitor who arrives, sees two rows of unexplained buttons and a
  sentence with square brackets in it, and does not realise the brackets are the
  interface.

**Finding 10 — A card will not tell a keyboard or phone user what its badge means.**
*Severity: low-medium.*

- **URL:** `browse.html?role=business-founder&level=never-used`
- **What I saw:** the badge is `<span class="badge badge-ai-reviewed" title="AI read all
  of it...">` with `tabIndex` **-1**. `title` needs a mouse. No link to
  `how-we-check.html` exists anywhere in `<main>` on Browse — I enumerated every `<a>` and
  found zero.
- **Who it harms:** phone users, who are most of my kind, and who have no hover at all.
  The word "Skimmed" on a card is doing a lot of work and cannot explain itself.

**Finding 11 — Browse on a phone is a four-hundred-screen scroll.**
*Severity: low-medium.*

- **URL:** `browse.html` at 375×812.
- **What I saw:** all 588 cards rendered into a **321,320px** page — about **396 phone
  screens** — with no pagination and no "load more". My own role's never-used list is
  22,568px, about 28 screens, for 37 cards.
- **Who it harms:** anyone who taps "Browse" in the navigation on a phone instead of
  answering the two questions first.

---

## 11. The one thing that would make me leave and not come back

Clicking **"Read in full"** and being told **"We have not covered this role yet."**

I would not read that as a filter result. I would read it as the site telling me, in plain
words, that it has nothing for people who run businesses. I would not try a second filter.
I would close the tab and I would not come back, and I would be wrong — there are 153
things here for me and some of them are very good. That is what makes it the worst thing
on the site. Every other problem costs me time. This one costs me the site.

Finding 3 is a close second for a different reason: it is the failure that stops the site
spreading. I cannot recommend a page to my business partner if the link arrives looking
like every other link.

---

## 12. What is genuinely good (honest, brief)

- **The `Skip if:` lines are the real thing.** They argue against the resource, by name,
  with specifics: "It names the token numbers and then sends you to another page for the
  per-model breakdown, so you will click again." Nobody else does this. It is the reason
  to use this site.
- **The never-used picks got my priorities right.** Privacy first, and the reason said
  why. That is a judgment, not a list.
- **"Claude Team pricing for a small business"** — seat math at 5 and 12 people, when an
  API key beats a seat. Exactly the calculation I have to do.
- **The freshness flag is blunt and honest:** "over a year ago, may not match Claude
  today".
- **`how-we-check.html` is more honest than it needed to be.** Naming one person, naming
  the university, and saying "has not yet read a single resource end to end" is the
  opposite of what most sites do.
- **Cards connect to paths** — "Step 3 of 6 in Your first week with Claude" on a card is a
  nice piece of joinery.
- **No account, no tracking, no cookie banner, and it says so:** "We do not track your
  progress. Nothing here needs an account."
- **The counts are honest.** All four of my level counts matched STATUS.md exactly. Whoever
  built the measuring is not rounding up.
- **It is fast**, and at phone width nothing overflows sideways.

---

## 13. Would I come back, and what one thing would make me?

Yes — but not today, and not because the site earned it. I would come back because the
`Skip if:` lines are worth putting up with the rest, and because I have not found anywhere
else that tells me when a course is a waste of my afternoon.

Here is my honest position. I came with two questions. Is my customer data safe, and what
does this cost me. The site answered the first one well the moment I said who I was — the
privacy page, first pick, with a reason. Then it spent the rest of the hour making the
second one impossible. Five paid things in my role, not one price. No topic for cost. My
plain-English cost question returned cloud anomaly detection. And when I finally clicked
the badge that means "somebody actually read this", it told me my job is not covered yet.

**One thing.** Put the price on the card. That is it. Four rows on this site already do
it — "from $49", "from $2,999" — so the machinery exists and works. Every row that asks
for money should show what it costs, or say "we have not checked the price", which is a
sentence this site is clearly comfortable writing. A directory that tells me exactly when
to skip a free thing, and then goes quiet the moment money is involved, has stopped doing
its job at the point I needed it most. Fix the prices and I will forgive the rest,
including the empty state that nearly sent me away.

And while you are in there: when the "Read in full" filter returns nothing, say "nothing
has been read in full yet." Do not tell a business owner you have not covered them. You
have. You covered them better than most.

---

## Checklist
- [x] I opened the live site
- [x] I tried all four levels
- [x] I quoted at least 5 real titles or lines from the site
- [x] Every number I used is in 00-facts.md, STATUS.md, or quoted from the site
- [x] I looked at a phone width
- [x] I read no file under scripts/ or data/
- [x] I found at least one thing nobody has mentioned before
