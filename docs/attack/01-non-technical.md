# Attack: not a coder
Written as someone who is not a coder, at 2026-08-27. Site version: 22e4532.

I am not a developer. I have one hour today. I want to know what Claude is, what it
costs me, and what to do first. I will leave if the site wastes my time.

**How I checked.** I opened the live site in Chrome and clicked through it. I read the
real cards with `python docs/attack/role-view.py non-technical <level>`, which prints
the same cards in the same order as Browse. I ran the site's own search with
`python scripts/test-search.py`. I confirmed the deployed data matches the repository:

```
curl -s https://.../learn-claude/data/items.js -o live-items.js
python -c "a=open('data/items.js','rb').read().replace(b'\r\n',b'\n'); \
           b=open('live-items.js','rb').read().replace(b'\r\n',b'\n'); print(a==b)"
-> identical after newline normalisation: True 624541 624541
```

Quoting `role-view.py` is quoting the live site.

For the phone pass I did not resize the browser window. Four other agents were working
in the same Chrome window at the same time, and a resize would have moved their pages
too. I checked mobile from the `@media (max-width: 768px)` block in
`assets/css/site.css`, from `browse.html`, and by asking the live page which element
holds each control. Every mobile claim below names its evidence.

---

## 1. The first 60 seconds

The page says **"Find what's worth your time."** in small grey text. Under it, in very
large serif, is a fill-in-the-blank sentence: **"I'm a [role] and I've [level]."** Two
words are underlined in orange. Under that, ten role chips.

I understood it in about four seconds. That is good, and I will say so again in
section 11.

Three things happened in the first minute that I did not like.

**A drawing takes the right-hand third of my screen and tells me nothing.** Before I
click, it cycles through a picture every 2.6 seconds. When I pick "not a coder" it
settles on a coffee mug. At "built things with it" the mug gets steam. I am here to
learn a tool. A mug is not information. `home.js` says there are 40 of these drawings
and about a megabyte of them.

**Nothing on this screen mentions the thing that was built for me.** There is a path
called "Your first week with Claude". `data/paths.json` tags it with
`"roles": ["non-technical", ...]` and `"level": "never-used"`. That is exactly the two
answers I just gave. The home page never mentions it. See 9.2.

**Three promise columns sit below the fold.** "We say when to skip", "We say how we
checked", "We show the date". The first one reads:

> Every entry has a **Skip if:** line. A link with no judgment is just a list, and
> lists are what made this hard in the first place.

Hold on to that sentence. It comes back in 9.6.

---

## 2. Does the front door work for me (all four levels, with counts)

I clicked "not a coder", then each level in turn, and read the live tally under the
button.

| I answered | Sentence on screen | Tally on screen |
|---|---|---|
| role only | "I'm not a coder and I've [level]." | **68 resources match so far.** |
| never used Claude | "I'm not a coder and I've never used Claude." | **24 resources match so far.** |
| used it a little | "I'm not a coder and I've used it a little." | **39 resources match so far.** |
| used it a lot | "I'm not a coder and I've used it a lot." | **5 resources match so far.** |
| built things with it | "I'm not a coder and I've built things with it." | **0 resources match so far.** |

All five numbers match `00-facts.md`. The counter is honest. Credit where it is due.

**What the site does when a level gives me almost nothing: nothing.**

At "used it a lot" I get 5. On Browse the count line reads
`5 resources. Remove a filter to see more.` I have exactly two filters, and they are the
two questions the site asked me. It is telling me to un-answer its own question.

At "built things with it" I get 0. The chip looks identical to the other three. The
"Show me" button stays orange and stays clickable — I checked, `disabled` is `false`.
The site knows the answer is 0 before I click, prints "0 resources match so far.", and
still lets me walk into the wall. I clicked it. The browser tab said
**"Browse 0 Claude resources — Learn Claude"** and the page said:

> **Nothing matches all of those.**
> Try removing one filter — time is usually the one to loosen.

I never set a time filter. There is no time filter on the screen. The only two chips are
"not a coder ×" and "built things with it ×". The site gave me advice about a control I
never touched. See 9.7.

---

## 3. What the catalogue actually gives me (are these really for me?)

Command: `python docs/attack/role-view.py non-technical never-used`

**The first card I am shown is addressed to a student.**

> **AI Student Research Guide: Prompt Engineering**
> Libguides · Westmoreland County Community College Library
> *For:* A student who has never thought about how they phrase a request and wants the
> smallest possible thing that will improve every prompt they write.

I am not a student. The second card is "Claude for Education Is Made for Learning", and
its For: line starts "A student, in any subject...". Card 6 is "Claude AI for Teachers".
Card 7 is "Claude Design Tutorial for Designers". Card 9 is "How to setup Claude for
Small Business".

```
python -c "... pattern match on who_for over the 24 never-used cards ..."
-> never-used cards whose For: line names a different job: 8 of 24
```

One third of my first screen is addressed to somebody else with my label stapled on.
Across all four levels, 47 of my 68 are shared with another role (68 total minus 21
only-this-role, both from `00-facts.md`). The biggest overlap is `business-founder` (25),
then `pm` (17), then `writer-marketer` (16).

**There is nothing to do, only things to watch.** At never-used my 24 cards are
9 video, 8 course, 5 article, 2 docs. Zero hands-on. Zero exercises. The whole role has
exactly 1 hands-on item (`00-facts.md`), and it is at the next level up. For the person
who has never opened Claude, the site offers 24 things to sit through.

**Nobody has read most of it.** `role-view.py --counts` gives my tier mix:
`{'ai-reviewed': 9, 'previewed': 56, 'listed': 3}`. 56 of 68 are "Skimmed", which the
site itself defines as *"We read the outline or a free sample. We have not seen the
whole thing."* At never-used it is worse: 20 of 24 Skimmed, 1 Found only.

Meanwhile `how-we-check.html` opens with:

> We would rather have 70 resources we can vouch for than 700 we cannot.

There are 353. Zero are vouched for by a person.

**The dates.** At never-used, 9 of 24 cards print "No publish date given" and 2 print
"Published over a year ago — may not match Claude today". That is 11 of 24 cards where
I cannot tell whether the thing still matches the product.

---

## 4. Paths

I clicked "Paths" in the nav, because nothing else pointed me there.

The index shows all three paths to everyone, with no marker for which one is mine. I had
to read three "for" lines and rule out "Developers who have installed Claude Code" and
"Researchers and academics who want the speed without the retraction". `paths.json`
carries a `roles` array on every path. `assets/js/paths.js` never reads it.

I opened **Your first week with Claude**. Header: `6 steps · about 2 hours · free`.
Intro:

> Six short steps. Nothing here takes more than an hour, and you can stop after step 3
> and still be better off than most people.

That intro is good. Then the page argues with itself.

**The last line of the page says "Nothing here needs an account."** Step 3 is chipped
`free, sign-up needed`. Step 4 is chipped `free, sign-up needed`. Two of the six steps
need an account, and the sentence denying it sits directly below them. The header chip
says `free` for the whole path.

**Step 1 is a promotional newsletter, and the warning is hidden.** Step 1 is
"Claude is not one tool. It's six." from Substack. The path shows the badge, the chips,
and the reason for the order. It does not show the `Skip if:` line, which on the
resource page reads:

> The author writes in a promotional, personal-brand newsletter style with frequent
> subscribe prompts — if that tone bothers you, get the same information from
> Anthropic's own Cowork docs instead.

The home page promised me that line on every entry. The path drops it. See 9.6.

**Step 4 does not exist for me.** Step 4 is "What are Projects?". In `items.json` its
roles are `['researcher']`. It is not one of my 68. If I browse as "not a coder" I can
never find it, and the path calls it essential.

**Four of six steps have no publish date.** Steps 1, 2, 4 and 5 all print
"No publish date given".

**Step 6 teaches a product I may not be able to buy.** Step 6 is
"Get started with Claude Cowork (Help Center)", chipped `free`. Cowork needs a paid
Claude plan. The site knows: another Cowork card says *"Skip if your plan does not
include Cowork, because you cannot follow along with any of it."* See 9.1.

The step order itself is sensible. Tool → do a task → course → Projects → how it fails →
Cowork. The `why` sentence on each step is the best writing on the site. Step 3's is:

> By now you have had a generic, disappointing answer. Anthropic's own beginner course
> is the fix, and it is the single highest-value hour here.

That is worth reading. It is buried two clicks away behind a nav link, and the site
never once suggests I click it.

---

## 5. The card and the resource page

I opened three.

**`resource.html?id=r-496c145f5c`** — "Full Claude Tutorial: Beginner to Advanced in
19 Minutes". Directly under that title is a chip that says **`one hour`**. The title and
the chip contradict each other by 3x, on the same screen, four lines apart. The real
runtime is in the site's own data: `notes: "852K views, 19:12, verified 2026-08-22"`.
The page never shows it.

The action button says **"Open on Futurepedia"**. The link goes to `youtube.com`.

**`resource.html?id=r-9b8a0da5f7`** — "Claude AI Step-by-Step: The Beginner's Blueprint
for Real Results", by Teacher's Tech. Chipped `one hour`. `notes` says `20:50`. Button
says "Open on Teacher's Tech" and goes to `youtube.com`. The write-up itself is good and
honest: *"Strong on the mental model of how to ask, weak on advanced features - which is
the right trade for the audience."*

**`resource.html?id=r-136c8e0f7b`** — "Claude, Claude Projects and Claude Code for
Non-Coders". This one is tagged `non-technical` and nothing else. It is card 34 in my
"used it a little" list. Its page shows **two** "Where this fits" blocks:

> **Where this fits**
> This is step 4 of 6 in **first-week**. The order matters — the path says why.
>
> **Where this fits**
> This is step 2 of 5 in **research-with-claude**. The order matters — the path says why.

Both are false. Step 4 of "Your first week with Claude" is "What are Projects?". Step 2
of the research path is also "What are Projects?". And the link text is a raw internal
id — `first-week`, `research-with-claude` — not the human title the site uses everywhere
else. See 9.3.

**What the resource page does well:** "What it teaches" as plain bullets, "Who it's for"
and "Skip it if" as full sections, "How we checked this one" naming the tier and linking
to the method. That is a good page. It is let down by the two numbers on it that I most
need — how long, and where does it really sit.

---

## 6. Search, in my words

I did not type keywords. I typed sentences. I ran the site's own ranking by importing
`scripts/test-search.py` and intersecting the result with the role filter, which is what
Browse does (`assets/js/browse.js`, `matches()` ANDs the query with every filter).

### "I don't know where to start" — 18 results site-wide

Top hit: **"Introduction to Claude (code-along)"**, score 30.4, tagged `data-analyst`,
format `hands-on`. A *code-along*. I said I am not a coder. With my role filter on I get
7 results, and the highest is "Best practices for getting started with Claude Cowork" —
which needs a paid plan.

The correct answer to that sentence is the path called "Your first week with Claude". It
cannot be returned. The search index holds 353 ids and zero paths:

```
python -c "import json; k=json.load(open('data/search-keywords.json')); print(list(k.keys()), len(k['ids']))"
-> ['version','count','ids','weights','words','phrases'] 353
```

### "is this going to cost me money" — 8 results site-wide, 0 for me

This is the single most important question I have, and the site has the answer. It has
"Plans & Pricing" and "Claude Team pricing for a small business". Both are tagged
`business-founder` and nothing else. Live, at
`browse.html?role=non-technical&q=is this going to cost me money`:

> **0 resources for not a coder**
> **No match for "is this going to cost me money".**
> Try fewer words, or browse by role instead.

I *am* browsing by role. The site's recovery advice is the thing I am already doing.

### "how do I stop it making things up" — 8 results site-wide, 3 for me

Top hit for me: **"Claude for Education Is Made for Learning"**, a university blog post
about Learning Mode. The actual answer — Anthropic's own **"Reduce hallucinations"**,
score 43.4 — is tagged `data-analyst` and level `confident`. I cannot reach it. Third
site-wide is "Hooks in Claude Code — Full Theory + Practical Use", for developers at
builder level.

**Verdict.** Search understands my words. The role tags then throw the best answers
away. The two pricing pages and the one hallucination page are locked to roles I did not
pick, and the site tells me nothing exists.

---

## 7. On a phone

Evidence: `assets/css/site.css` lines 590–635, `browse.html` lines 36–92, and live DOM
queries against the deployed page.

**`Clear all` is invisible on a phone.** At `max-width: 768px` the rule is
`.filter-rail { display: none; }`. The `Clear all` button lives inside that rail
(`browse.html`, inside `<aside class="filter-rail">`). I confirmed it on the live page:

```
clearAllInsideRail: true    clearAllHidden: false    sheetHasClearAll: false
sheetControls: ["Close", "✓not a coder", "a student", "a researcher"]
mobileBarText: "Filters"
```

So on a phone: I arrive from the home page with two filters, I get 0 results, the button
that would rescue me exists and is not hidden by its own class — it is hidden because
its parent is. The replacement bottom sheet has Close and Show resources and no clear
control at all. My only escape is to tap the small `×` on each chip one at a time.

**The bottom bar just says "Filters".** No count. It does not tell me two filters are
already applied.

**The empty-state advice is the same wrong advice.** "time is usually the one to loosen",
on a screen with no time filter and no visible filter rail to loosen it in.

**What is fine on a phone.** The hero stacks to one column and the drawing is capped at
280px and sits *below* the text, so the mug does not eat my first screen. Chips measure
44px tall, which is the site's own minimum, and `--text-body-sm` does not shrink at
768px, so they stay 44px there too. Footer links are given `min-height: 44px` in the
mobile block. Somebody did this work.

---

## 8. Content quality — the three worst entries I was shown, quoted

**1. "Everyone should be using Claude Code more"** — Lenny's Newsletter, card 13 of my
24 at *never used Claude*, cost `subscription`.

> *Skip if:* Skip it if you want method rather than inspiration - it is a list of what
> other people do, most of it sits behind a paid subscription, and it dates from October
> 2025 so it predates Cowork.

The site is telling someone who has never opened Claude to install a command-line tool,
via a paywalled newsletter, that the site itself says is out of date. Three
disqualifications written in the entry's own Skip-if line, and it is still on my first
screen.

**2. "Next-Generation AI Assistant: Claude by Anthropic"** — Coursera, card 15 at
*never used Claude*.

> *Skip if:* Skip it if the title made you think Anthropic built it - it is a Coursera
> and Starweaver production, one module long, rated only 4.1 from 33 reviews, and it
> never leaves basic marketing prompts.

The site knows the title is misleading. It knows the rating is 4.1 from 33 reviews. It
lists it anyway, with the warning below the fold of the card. The whole point of this
site was to not show me things like this.

**3. "Claude Code for product managers: research, writing, context libraries, custom
to-do system, more"** — card **1** of 5 at *used it a lot*.

> *Skip if:* Skip if the terminal intimidates you - the tool is command-line even though
> the work is not technical. Skip too if you want a quick tips list rather than 43
> minutes of one person's system.

Its stored prerequisite is `["basic comfort with using a command-line terminal"]`. Its
For: line says "Product managers". It is chipped `one hour` for a 43-minute video. It is
the top card the site gives to a non-coder who has used Claude a lot. Of the 5 cards at
that level, one is this, one is a designer podcast, and one is a paid Udemy course.

Dishonourable mention: **"Kris Puckett - Becoming an AI-native designer (Dive Club)"**,
also in my top 5 at that level.

> *Skip if:* You have already read the Cat Wu article — the video covers the same
> ground, and I could not confirm its runtime or publication date.

"I could not confirm its runtime". So the site does not know how long it is, tells me so,
and still chips it `one hour`.

---

## 9. Everything that is broken, ranked

Ranked by what it costs me, not by how hard it is to fix.

### 9.1 The word "free" is not true for Cowork, and Cowork is most of my catalogue

Cowork needs a paid Claude plan. The site knows — four entries record it as a
prerequisite, for example *"a claude plan that includes cowork"* and *"paid claude
plan"*. The other twenty do not.

```
python -c "... cowork topic, cost, prerequisites over the 68 ..."
-> non-technical items tagged cowork: 28
   of those with a paid-plan prerequisite recorded: 4
   cowork + cost free/free-account + NO paid-plan prerequisite: 20
   at basic level: 20 cowork items, 16 of them free/free-account
```

At *used it a little*, 20 of my 39 cards are Cowork. 16 of those are badged `free`.
`00-facts.md` says 50 of my 68 are free. That number is not what a visitor thinks it
means. The `free` cost filter is the one filter a person with no budget will use, and it
is the one that misleads them. Two of the cards say the truth in their Skip-if
(*"Skip if your plan does not include Cowork, because you cannot follow along with any
of it"*), which proves the site can express it and chose not to on the other twenty.

**Cost to me:** I pick free, I watch a tutorial, I open Claude, the feature is not there.

### 9.2 The path built for me is unreachable from the two questions I answered

`data/paths.json` gives every path a `roles` array. `first-week` lists
`non-technical, student, teacher, business-founder` and `"level": "never-used"`. That is
my exact pair of answers. `assets/js/paths.js` never reads `roles`. `home.js` submits to
`browse.html` and nothing else. `browse.js` contains no reference to paths at all
(`grep -n "paths" assets/js/browse.js` returns only comments). The only route to my path
is the nav link, and then reading three descriptions to work out which is mine.

**Cost to me:** the site's best asset — a 6-step ordered route with a reason per step —
is hidden behind a generic nav item, while I am handed 24 unordered cards instead.

### 9.3 Eight resource pages claim to be steps of paths they are not in

Root cause is one line in `assets/js/ui.js`:

```js
c.paths = byId[x.id] || x.paths || [];
```

`byId` is built from the real `LC_PATHS`. The `|| x.paths` fallback then uses a stale
`paths` field baked into `items.json`. Eleven stale claims survive on eight resources.

```
python -c "... compare items.json paths field against paths.json steps ..."
-> resource pages showing a FALSE "Where this fits" block: 8
```

Live, on `resource.html?id=r-3b409df1d4`, titled "How to Build an MCP Server with
Python, Docker, and Claude Code":

> This is step 1 of 6 in **first-week**.

A Docker and Python server tutorial is being sold as step 1 of my first week with
Claude. And one of the eight is tagged `non-technical` only — see section 5,
`r-136c8e0f7b`, which claims two false path positions at once. The link text is the raw
id, so it renders as "first-week" and "research-with-claude" in the middle of a sentence.

### 9.4 The length chip says "one hour" for videos that are twenty minutes

`LC.TIME["under-1hr"]` renders as the words **"one hour"**. The bucket is 15–60 minutes.
The exact runtime is already stored in `notes`.

```
python -c "... parse mm:ss from notes for the 68, compare with the time bucket ..."
-> labelled "one hour" on the card, with a real runtime recorded: 11
   of those, actually 30 minutes or less: 8
     16 min | Claude Design Tutorial for Designers | First Look + Full Walkthrough!
     18 min | Anthropic Just Dropped Claude for Small Businesses (31 Skills)
     19 min | Full Claude Tutorial: Beginner to Advanced in 19 Minutes
     19 min | Learn 80% of Claude Cowork in Under 20 Minutes
     21 min | Claude AI Step-by-Step: The Beginner's Blueprint for Real Results
     21 min | My Simple Claude Cowork System (for normal people)
     23 min | Claude AI for Teachers: Complete Beginner's Guide to Getting Started
     26 min | How Teachers Can Create Interactive Classroom Activities with AI
```

Two of those titles state their own length and are contradicted by the chip under them.
The home page headline is "Find what's worth your time." Time is the one number the site
gets wrong.

### 9.5 "Your first week with Claude" contradicts itself four times on one screen

- Footer line: **"We do not track your progress. Nothing here needs an account."**
  Steps 3 and 4 are chipped `free, sign-up needed`.
- Header chip: `free`. Steps 3 and 4 are `free-account` in the data.
- Steps 1, 2, 4 and 5 print **"No publish date given"**.
- Step 4, "What are Projects?", has `roles: ['researcher']`. It is not in my 68. My own
  path sends me to a resource my own Browse hides.

### 9.6 The path page drops `Skip if:` — the site's whole reason to exist

`assets/js/paths.js` `one()` renders badge, chips, the step `why`, and the freshness
line. There is no `skip_if`. I confirmed on the live path page: the word "Skip" does not
appear anywhere in it.

The home page promise, verbatim:

> Every entry has a **Skip if:** line. A link with no judgment is just a list, and lists
> are what made this hard in the first place.

The one screen where the site is actively telling me what to do is the one screen where
the judgment is removed. Step 1 is a Substack newsletter the site privately describes as
"promotional, personal-brand newsletter style with frequent subscribe prompts".

### 9.7 "built things with it" is a dead end the site plans in advance

0 resources. The chip is styled like the other three. `Show me` is not disabled
(`disabled === false`, checked live). The landing page is `browse.html?role=non-technical
&level=builder`, title "Browse 0 Claude resources", and the recovery advice is:

> Try removing one filter — **time is usually the one to loosen**.

There is no time filter. `renderEmpty()` in `browse.js` only special-cases a role with
no other filter; role-plus-level falls into the generic branch and gets advice about a
control I never used.

### 9.8 The site has pricing pages and hides them from the role that asks first

"Plans & Pricing" and "Claude Team pricing for a small business" are both
`roles: ['business-founder']`. My sentence "is this going to cost me money" returns 8
results site-wide and **0** for me, and the empty state tells me to "browse by role
instead" while I am browsing by role.

### 9.9 Anthropic's "Reduce hallucinations" is locked to `data-analyst`

`r-2350921236`, `roles: ['data-analyst']`, `level: confident`. It is step 1 of the
research path. It scores 43.4 on "how do I stop it making things up". A non-coder gets a
university blog post instead. Not trusting the output is the number one beginner problem
and the best page for it is behind a role tag I did not pick.

### 9.10 Search cannot return a path

353 ids in the index, 3 paths, 0 of them indexed. Every "where do I start" sentence
therefore returns a single resource instead of the ordered route that answers it.

### 9.11 "Best checked first" means "whichever the AI read first"

0 of 353 carry the top tier, so the default sort ranks `ai-reviewed` above everything.
The result at never-used, in the real on-screen order:

```
 1 ai-reviewed  official=False AI Student Research Guide: Prompt Engineering
 2 ai-reviewed  official=False Claude for Education Is Made for Learning
 3 ai-reviewed  official=True  Get started with Claude
...
16 previewed    official=True  Claude 101
```

A community college LibGuide and a university blog post outrank Anthropic's own pages.
"Claude 101" — which my own path calls **"the single highest-value hour here"** — is
sixteenth of twenty-four.

### 9.12 A third of my first screen is addressed to somebody else

8 of 24 never-used cards name another job in the For: line, including cards 1 and 2. The
site asked me who I am and then handed me a student guide, a teacher guide, a designer
walkthrough and a small-business setup.

### 9.13 "Open on Anthropic" goes to youtube.com

29 of my 68 link to YouTube. All 29 name the channel, not the destination.

```
Open on Anthropic          ->  www.youtube.com
Open on Futurepedia        ->  www.youtube.com
Open on Kevin Stratvert    ->  www.youtube.com
```

I expect "Open on Anthropic" to take me to anthropic.com. On a work machine that blocks
YouTube, or if I do not want to be signed in, this matters.

### 9.14 Nobody's name is anywhere, and two of the notes are written by "I"

There is no `mailto:`, no contact page, no about page, no author name in any HTML file
(`grep -rn "mailto\|contact\|about.html" *.html assets/js/*.js` returns nothing). The
known problem is that "Found something wrong? Tell us." has no way to tell anyone. The
sharper version: the site says "we" throughout, has no "we", and card 2 of my first
screen is written in the first person singular — *"The clearest short onboarding page I
found"* — as is a Skip-if at level three: *"I could not confirm its runtime or
publication date."* An anonymous "I" is asking me to trust its judgment about 353 links.

### 9.15 The home page search box is a one-shot

Once both blanks are filled, `.search-row.answered` collapses the "Or describe what you
want to do…" field. It never comes back on that page load, even when I reopen a question
— I reopened the level chooser and the field stayed collapsed. Both question blocks also
vanish once answered, with no visible "change this" control; the only way back is to know
the underlined words are buttons.

### 9.16 The same episode is in the catalogue twice, as two different things

- `r-0d2b1cdbba` — "Claude Code for product managers: research, writing, context
  libraries, custom to-do system, more", source "How I AI", published 2026-01-19,
  format `video`, roles `pm, non-technical`, topics `claude-code, chat-prompting`.
- `r-0e4ddc7e7a` — "How I AI: Claude Code for product managers, with Teresa Torres",
  source "Lenny's Newsletter", published 2026-01-19, format `podcast`, roles
  `pm, researcher`, topics `claude-code, skills`.

Same show, same date, same subject — both summaries describe a context library and a
custom markdown to-do system. The site treats them as two unrelated entries with
different roles, formats and topics. One reaches me; the other does not.

---

## 10. The one thing that would make me leave and not come back

**The money.**

I opened the site to find out what learning Claude will cost me. I typed the question in
my own words. The site said **"0 resources for not a coder"** and told me to browse by
role, which is what I was already doing. It has the two pricing pages. It gave them to
"running a business" and not to me.

Then it made it worse. It badged twenty Cowork tutorials `free` when Cowork itself needs
a paid plan, and put twenty of them into the thirty-nine cards it shows a beginner. If I
had trusted that badge, I would have spent an evening on a tutorial for a feature my
account does not have — and then found out, from the product, not from the site that
promised to save my time.

A directory whose whole pitch is judgment cannot be wrong about price and wrong about
length at the same time. That is not a missing feature. That is the two facts I came for.

---

## 11. What is genuinely good (be honest, but brief)

- **The front door.** "I'm a [role] and I've [level]." I understood it instantly and the
  count updates before I commit. No signup, no cookie banner, no modal. That is rarer
  than it should be.
- **The live count is honest.** All five numbers I saw matched the ground truth exactly,
  including the zero. Most sites would have rounded or hidden it.
- **`Skip if:` is the best idea on the site.** When it is present it is specific and
  unflattering — "rated only 4.1 from 33 reviews", "the title oversells", "most of it
  sits behind a paid subscription". Nobody else writes this. Protect it, and put it on
  the path page.
- **The path `why` sentences.** "Reading about it any longer is procrastination." That
  is worth more than the link it sits under.
- **"How we check" admits the tiers.** Saying "Skimmed. We have not seen the whole
  thing" out loud is a real choice, and the right one.
- **The mobile work that has been done is real.** 44px targets, footer padding for the
  fixed bar, a proper sheet. It only fails at the one control that matters when you are
  stuck.

---

## Checklist — every line ticked or the file is not finished
- [x] I opened the live site — Chrome, my own tab, `https://mojtaba-alehosseini.github.io/learn-claude/`, closed at the end
- [x] I tried all four levels — 24 / 39 / 5 / 0, read off the live tally, section 2
- [x] I quoted at least 5 real titles or lines from the site — 19 verbatim quotes, sections 1, 3, 4, 5, 6, 8, 9
- [x] Every number I used is in 00-facts.md or I show the command — every figure is from `00-facts.md`, from a shown `python`/`curl` command, or read off the live page
- [x] I looked at a phone width — section 7; measured from the `max-width: 768px` block, `browse.html`, and live DOM queries, not from a resize, and I say why
- [x] I found at least one thing nobody has mentioned before — 9.3 (eight resource pages claim false path positions, one of them mine), 9.1 (twenty Cowork entries badged free), 9.4 ("one hour" on a 19-minute video), 9.5 ("Nothing here needs an account" under two sign-up steps), 9.6 (the path page drops `Skip if:`), 9.14 (the anonymous "I"), 9.16 (the same episode twice)
