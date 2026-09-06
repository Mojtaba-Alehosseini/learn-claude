# Attack 3: working with data
Written as an analyst, 2026-09-06. Site version: 9deb0db.

I clean, join and check numbers for a living. Other people make decisions on my totals.
I do not write software and I do not want to. I came here to find out whether Claude can
do the boring half of my job without me having to take its word for anything.

## 1. The first 60 seconds

The home page says **"Find what's worth your time."** and then **"I'm a [role] and I've
[level]."** with the two blanks underlined in orange. Below it: **"588 resources, each
with a reason to skip it and the date we last looked."**

That is the right sentence. It is the first learning-directory front page I have seen that
leads with a subtraction promise instead of a size promise. The three panels below —
**"We say when to skip"**, **"We say how we checked"**, **"We show the date"** — read like
someone who has been burned by a link dump.

I clicked **working with data**. The sentence completed itself to *"I'm working with data
and I've [level]."*, the drawing changed to a bar chart, and a line appeared: **"72
resources match so far."** That is the correct interaction. No account, no email, no
cookie banner, no modal. Two clicks to a filtered shelf.

Watching it without touching anything: the role chips light one at a time and the drawing
crossfades through the role illustrations. The headline keeps the literal placeholders
`[role]` and `[level]` the whole time — in five screenshots taken across ten seconds it
never once demonstrated what the finished sentence looks like. The animation shows me the
menu but never the payoff. Minor, but it is the one moment the page has to teach me what
it does, and it spends it on a picture.

Verdict at 60 seconds: I stayed. That is more than most sites get.

## 2. Does the front door work for me (all four levels, with what I was shown)

I answered the two questions honestly at all four levels and followed **Show me** through
to Browse each time. Counts are the site's own, read off the page.

**"never used Claude" — 7 resources.** Picks: *Upload files to Claude (Help Center)*,
*AI capabilities and limitations*, *Claude 101 (DataCamp)*. Then "Everything else for you
(4)". The first pick's reason is the best line on the site for me: *"The step every data
guide assumes already happened, and the only candidate naming the ceilings you will hit -
500MB in chat versus 30MB in a Project, and code execution needed for XLSX."* That is a
real fact I would have found out the slow way. Seven is thin but every one of the seven is
plausibly for me.

**"used it a little" — 19 resources.** Picks: *Use Claude for Excel* (Read by AI), *Data
Analysis with Claude Code — it's not just for programmers*, *The ONLY Claude Cowork
Tutorial You'll Ever Need in 2026*. This is the best shelf on the site for my job. The
Excel pick's skip line is worth the visit on its own: *"it carries an explicit
prompt-injection warning - a downloaded template or a vendor's workbook can contain hidden
instructions that push Claude into extracting or destroying data, and testing has produced
exactly that."* Nobody told me that. I would not have thought of it.

**"used it a lot" — 34 resources.** This is where it falls apart, and I measured why.
**24 of the 34 come from one publisher, Anthropic Academy.** Seven of them are
near-identical vendor connector pages — *Using Aiera*, *Using Databricks*, *Using LSEG*,
*Using Moody's*, *Using MT Newswires*, *Using PitchBook*, *Using S&P global data* — all
"docs · 15 min", all requiring a commercial agreement I do not have. Badges across the 34:
**30 Skimmed, 4 Read by AI, 0 Read in full.**

**"built things with it" — 12 resources.** Picks: *claude-cookbooks: data_analyst_agent
notebook*, *4 Lines You Should Include in Your Claude Skill*, *MCP Tutorial for Beginners*.
Formats: **7 of 12 are `code`**, and **7 of 12 are hosted on GitHub**. The tail asks for
"Python, Jupyter and your own Anthropic API key before the first cell runs", "MCP config
you edit by hand", "live database credentials".

The front door works. The four levels give me four genuinely different shelves and the
counts match the site's own STATUS figures for my cells (7 / 19 / 33 eligible / 12). The
problem is not the door. It is what is behind the third one.

## 3. What the catalogue actually gives me (are these really for me?)

Filtering to **working with data** with no level gives **72 resources**. Of those:

- **47 of 72 are published by Anthropic** (Anthropic, Anthropic Academy, Claude Help
  Center, Claude Platform docs, Claude Privacy Center, Claude Code docs).
- **63 Skimmed, 9 Read by AI, 0 Read in full.**
- Formats: 33 docs, 12 video, 10 article, 8 code, 5 course, 4 hands-on.
- **17 of the 72 name a terminal, Python, an API key, Jupyter, git, hand-edited MCP config
  or SQL somewhere on the card.**

**Does the role filter return analyst work or developer work?** Both, and it splits by
level cleanly. At "never used" and "used it a little" it is analyst work — spreadsheets,
uploads, retention terms, checking arithmetic. At "built things with it" it is developer
work wearing an analyst hat: seven `code` rows, seven GitHub repos, and prerequisites like
*"It expects working SQL, a DuckDB or MotherDuck instance already running, and MCP config
you edit by hand"* (MotherDuck / DuckDB MCP Server) and *"Skip unless you can point this at
a read-only, least-privilege role. It takes live database credentials"* (Postgres MCP Pro).

**Does `builder` mean anything to somebody who does not ship software?** For my role, no.
"I've built things with it" is a sentence I would say honestly — I have built a repeatable
month-end reconciliation in Claude that I rerun every cycle. The shelf that sentence opens
is a shelf of servers to install. Only two of the twelve are about building the thing an
analyst builds: *4 Lines You Should Include in Your Claude Skill* ("Assumes no coding")
and *claude-cookbooks: data_analyst_agent notebook* (which needs an API key with credits).
The other ten assume I want to be the person who wires the tool up, not the person who
uses it. The word does not translate.

To be fair to the rules: every one of those ten tells me in its skip line that it wants a
terminal. The tagging is honest. It is the *level name* that is wrong for me, not the
cards.

**Do the five collection cards (Sales, Legal, HR, Finance, Operations) help me or get in
my way?** Neither — **none of the five appears in my role's 72 rows.** I only found them
by browsing all 588 unfiltered. I opened *Use cases for Finance*: it is honest about what
it is (*"This is a menu, not a lesson"*) and its "Who it's for" says *"Someone who owns the
numbers in a small company"*, which is a founder, not me. It also names *"variance
commentary, intercompany reconciliation, contract-to-ledger extraction, scenario
forecasts"* — real FP&A work that I would want, filed where I will never see it. So the
collections do not get in my way; they are invisible to me, which for the Finance one is a
loss rather than a mercy.

**Do the stripped `listed` cards read as honest or broken?** Honest, and useless. There
are three (`browse.html?checked=listed`). Each carries a title, a publisher, chips, dates,
and one line: *"Skip if: You want something we have read. We have not opened this one
yet."* No `For:` line — the only cards on the site without one. That reads as honest. But
one of the three, *Head of Claude Code: What happens after coding is solved (Boris
Cherny)*, is chipped **subscription**. The site is showing me a paid item it has never
opened, with no price and no judgement of who it is for. Honest about the gap, careless
about the consequence.

**Can I find out what the "how well checked" badge means?** With a mouse, yes: hovering
the badge shows *"We read the outline or a free sample. We have not seen the whole
thing."* On the resource page it is written out in full under "How we checked this one".
`how-we-check.html` defines all four levels plainly and says *"Nothing is Read in full
yet, and the cards say so."* That is good. But see section 7 — on a phone the badge does
nothing at all.

**Do the date lines make the site look maintained?** Mixed, and the mix is the honest
kind. On my 34-row shelf, 32 say "No publish date given" — which STATUS.md says is
deliberate and I believe it, because the "Checked" dates are all within the last three
weeks and one card carries "Updated 2 Sep 2026", four days ago. A site that says "I do not
know when this was published" while showing me it looked last week reads as maintained.
The one that reads as abandoned is the opposite case: *"Published 5 Sep 2024 · over a year
ago, may not match Claude today"* — and see finding 1 for where the site then puts it.

**Does naming one person and Claude as "we" raise or lower my trust?** Raises it, clearly.
`how-we-check.html` says: *"One person makes this site - a researcher at the Technical
University of Denmark... The reading is done by Claude, at the level each card's label
claims and no further... A person sets the rules, decides what the labels are allowed to
say, and reads the arguments - and has not yet read a single resource end to end."* That
paragraph explains the zero in the "Read in full" column instead of hiding it. I work with
people who will not tell me how a number was produced. This one told me before I asked.

The caveat it forces is real and the site does not duck it: **not one of the 72 cards in
my role was read by a human.** An AI wrote the skip lines and an AI chose the three picks
("picked by AI · 6 Sep 2026" is printed above them). I would use this shelf to shortlist.
I would not quote it.

## 4. Paths

There **is** a path for me: **"Analysing your own data without getting the numbers
wrong"** — *"Analysts with a spreadsheet, a deadline, and somebody who will ask where the
number came from."* Five steps, about two hours, free. That description is the best single
sentence on the site. It is my job written by someone who has done it.

I followed it. The arc is stated up front and it is a good arc: *"get it in front of the
model, know what happens to it, then learn the difference between Claude reading your
numbers and Claude actually running them. Only the last step needs a terminal, and you can
stop before it."*

1. Upload files to Claude (Help Center) — 15 min
2. How long do you store my data? — 15 min
3. Introducing the analysis tool in Claude.ai — 15 min
4. How to Use Claude for CSV Data Analysis (The Honest Guide) — 1 hour
5. Claude Code for Data Analysis: Excel-Free Answers From CSVs — 1 hour

Step 2 being second is argued for, not asserted: *"An analyst decides at upload, before
anything: once somebody else's data is pasted, reading the retention terms afterwards
changes nothing."* I agree with it. Step 5 tells me I may stop before it. That is a path
written by someone who respects that I have a day job.

**Is there one at my level rather than at the start?** No. There is exactly one path for
my role and it starts at "how to attach a file". The paths page labels every path by role
only — *"For working with data"* — with no level anywhere. If I have used Claude for a
year, nothing on the paths page tells me the first two steps are beneath me until I open
it and read the step notes. And there is no path at all for the builder shelf: the twelve
rows there are twelve unconnected repos.

Two things wrong inside the path, both in section 10.

## 5. The card and the resource page

I opened three.

**Use Claude for Excel** (`resource.html?id=r-1e88a43d53`). I would click through, without
hesitating. It gives me "What it teaches" as four bullets, "Who it's for", "Skip it if",
and **"Before this — Paid Claude plan / Working knowledge of Microsoft Excel"**. The
summary is specific enough to be useful on its own: *"ask about an open workbook and get
answers with cell-level citations, flex an assumption while formula relationships keep
recomputing, trace a #REF! to its cause"*. The skip line told me two things the vendor's
own page buries. This page is worth the whole site.

And it is chipped **`free`** while its own "Before this" block says **"Paid Claude plan"**.
Same screen. See finding 2.

**Introducing the analysis tool in Claude.ai** (`resource.html?id=r-7f2c2387f7`). Would I
click through? No — and the site agrees with me, which is the odd part. Its browse card
says *"this is history rather than instruction - useful for understanding why Claude runs
code at all, useless as a guide to doing it today. Go to the code execution documentation
for the current feature."* It is step 3 of 5 in my path.

**Head of Claude Code (Boris Cherny)** (`resource.html?id=r-9f57e8bf80`). No. `Found only`,
`subscription`, no summary, no "For" line, no price. There is nothing here to decide on.

All three pages have an **"Open on <publisher>"** button and a **"Copy link"** button, and
a footer line *"Something wrong with this one? Tell us — opens a GitHub issue with the
details already filled in."* I do not have a GitHub account. Nobody I work with does.

## 6. Search, in my words

Typed into the Browse search box at `browse.html`, no role or level filter, so the ranking
is not doing me any favours.

| # | what I typed | top 3 I was shown | verdict | why |
|---|---|---|---|---|
| 1 | why does Claude give me a different total every time I ask | 1. Answer the ad-hoc data question (Anthropic Academy) 2. How does Claude handle mathematical equations and calculations? (Claude Help Center) 3. Source insights from your tools to build a deck (Anthropic Academy) | ok | 81 results. #2 is genuinely on my question — Claude predicts rather than computes — so this scrapes a pass. But the card written for exactly this, *How to Use Claude for CSV Data Analysis (The Honest Guide)*, whose own reason says "the single explanation behind every total that ever came back wrong", is **4th**, below a slide-deck recipe. |
| 2 | clean up a messy spreadsheet with duplicate customer names | 1. Introduction to Claude Analysis (Codecademy) 2. 15 Claude Tips for Everyday Data Analysis (LinkedIn Learning) 3. Complete Guide to Claude Cowork (with 12 free interactive lessons) | bad | 36 results and not one of the top three mentions cleaning, deduplication or messy data. #1 and #2 are generic beginner data courses (#2 is subscription-only with no price); #3 is a Cowork tour. Deduplication is the single most common thing on my desk and the search treated it as "data, beginner". |
| 3 | is it safe to upload our company sales data to Claude | 1. AI Fluency for Small Businesses (Anthropic Academy + PayPal) 2. Introduction to Claude Analysis (Codecademy) 3. Using Daloopa for financial analysis (Anthropic Academy) | bad | 44 results. The catalogue holds *How long do you store my data?* — "For: Anyone about to paste work data into Claude and wanting the retention figures from the company itself" — and it is **4th**. #3 is an invitation-only paid financial data connector; it has nothing to do with safety. This is the question that decides whether I use the tool at all, and the site answered it with a PayPal course. |
| 4 | get Claude to write SQL against our data warehouse | 1. MotherDuck / DuckDB MCP Server (GitHub · MotherDuck) 2. Using Databricks for Data Analysis (Anthropic Academy) 3. Introduction to Claude (code-along) (DataCamp) | ok | 12 results, tightly scoped, and the top two are exactly right. Marks off for #3 being a beginner code-along and for *Postgres MCP Pro* — the obvious answer for anyone whose warehouse is Postgres — being nowhere in the top eight, while *How to use the FHIR Developer agent skill with Claude Code* is 7th. |
| 5 | join two csv files and check the join did not drop rows | 1. Claude Code for Data Analysis: Excel-Free Answers From CSVs (CC for Everyone) 2. How I Use Claude Code as a Data Analyst (10 Real Use Cases) 3. Upload files to Claude (Help Center) | ok | Only 4 results out of 588, which is honest narrowing rather than padding. #1 is the closest thing the catalogue holds — it is the row that "argues for checking the output at all, leaning on Panko's finding that 94% of spreadsheets contain errors". Nothing here is about joins specifically, but nothing here is noise either. |

**The same question, asked two ways.** I asked query 1 again as **"how do I stop Claude
getting my numbers wrong"** — the same question in plain words. **The site did not agree
with itself, and the second wording is far worse.** It returned 77 results whose top five
were *Working smarter with Claude in PowerPoint*, *Map your understanding and build lessons
from the gaps*, *How I use Claude Code for real engineering*, *How do usage and length
limits work?* and *How to Use Claude Code as a Product Manager* — **not one of which is
about numbers being wrong.** In that same result list, *How does Claude handle
mathematical equations and calculations?* is 8th, *Reduce hallucinations* — whose own card
says "For: Any analyst worried about confidently-wrong output" — is **11th**, and *How to
Use Claude for CSV Data Analysis (The Honest Guide)* is **30th**. Under the first wording
the maths page was 2nd. Same question, two wordings, and the words "numbers wrong" pushed
every relevant card off the screen while "different total" pulled one back.

The same disagreement shows on query 3: reworded as **"what happens to my data after I
paste it into Claude"**, *How long do you store my data?* jumps from 4th to **1st** and
*Is my data used for model training?* arrives at 3rd. The wording an anxious person
actually types — "is it safe" — is the one that fails.

## 7. On a phone

375×812. Genuinely good, with one hole.

The home page stacks cleanly, the ten role chips wrap into five rows with real touch
targets, the illustration is dropped rather than squashed, and there is no horizontal
scroll anywhere I looked. Browse puts a sticky **Filters** button across the bottom of the
screen, which is the right pattern. The resource page is the best of the three: large
serif body text, a full-width orange **"Open on Anthropic"** button, **"Copy link"** under
it. I could use this on a train.

The hole: **I tapped the "Read by AI" badge on a card and nothing happened.** It is a plain
`<span>`, not inside a link, `cursor: auto`, and the URL does not change. The definition
exists in two places a phone cannot reach — a `title` attribute (mouse hover only) and a
`visually-hidden` element (screen reader only). So on the one surface where the site is
best, the badge that carries its central promise — "we do not round up" — is a word I
cannot look up in place. I have to leave the card and find "How we check" in the nav.

## 8. What changed since Attack 2 — my verdict on each

**Tags and levels rebuilt on a rule.** Role tagging: good. Every one of the 72 rows in my
role has a `For:` line that names a person doing my job, and where a row is a stretch the
line says so (*"Data analysts and data engineers who want the full Claude Code feature set
explained with data problems, not to-do apps"*). Two rows still do not belong — section 9.
Level: `builder` does not survive contact with my role. It means "you can install a server".

**Five collection cards.** Invisible to me — none is in my role's 72. *Use cases for
Finance* names FP&A work I would want and is filed where I cannot find it.

**Search rebuilt.** Two of five bad, and the two that failed are the two questions I most
needed answered: how to stop the numbers being wrong, and whether my company's data is
safe. It does not agree with itself across wordings of the same question. The stemmer is
clearly doing something — five sentence-length queries all returned sensible result *sets*
— but the ranking inside those sets is not reliable enough for me to type a question and
trust the first thing I see.

**Stripped `listed` cards.** Honest. But one is `subscription` with no price and no
judgement, which is the one combination that should not ship.

**How well checked, as a filter.** The filter works (`checked=listed` gave me exactly the
3). The definition is reachable by hover, by screen reader and on the resource page — but
not by touch. Two of three routes is not "reachable from a card".

**The thin-level offer.** I checked `teacher|builder`. It reads: *"Only 2 at 'built things
with it' for a teacher. The level below, 'used it a lot', has 8. Add 'used it a lot' too"*,
with *"Too few to pick from — these are all of them."* replacing the picks heading. It
makes sense, it is one click, and I would take it. Best small piece of copy on the site.
It never fires for me — my thinnest cell is 7.

**Date lines.** Maintained, not abandoned — because "No publish date given" sits next to a
"Checked" date from this month. The credibility comes from the recency of the checking, not
from the publish dates. But see finding 5: the path pages throw away the freshest date the
site holds.

**Prices.** Not clear at all, for me. **8 of my role's 72 rows cost money or need an
account and not one of them shows a price.** Across all 588 rows only **4** carry a price
chip (`from $49`, `from $995`, `from $2,999`, `from $3,000`) and all four belong to other
roles. Worse than missing prices is finding 2: sixteen rows on my main shelf are chipped
`free` and are not.

**Who "we" is.** Raises my trust. See section 3.

**The picks block.** I would open all three at "used it a little" and two of three at
"never used". The reasons are comparative, which is the hard part and the part everyone
else skips — *"The only candidate about what Claude gets wrong rather than what it can do,
which for someone whose first upload is a spreadsheet is the more useful half"*. At "used
it a lot" the picks are the only three rows on that shelf I could act on today; the AI that
picked them did better than the shelf deserved.

**Social preview title.** Broken. Finding 4.

**Home attract loop.** Runs, cycles the drawings, never fills the sentence in. Section 1.

**Sort control.** Broken. Finding 1.

**Paths above beginner level.** None. One path for my role, starting at zero, with no level
label on the paths page.

## 9. Content quality — the three worst entries I was shown, quoted

All three were shown to me at `browse.html?role=data-analyst&level=confident` — my main
shelf, not something I had to dig for.

**1. Stress-test your financial plan across scenarios** (Anthropic Academy, docs, 15 min,
`free`). *"For: Someone testing their own retirement or financial plan against real
downside risk."* / *"Skip if: Needs your actual tax returns, investment statements, Social
Security estimates and budget uploaded."* This is personal retirement planning. It is
filed under the professional role "working with data", at the level for people who use
Claude a lot. My tax return is not a dataset I work with. If Rule B reads each card's own
`who_for` line and drops a tag the line denies, this line denies the tag in its first six
words and the tag survived.

**2. Using MT Newswires for real-time financial news** (Anthropic Academy, docs, 15 min,
`free`). *"Skip if: A paid premium newswire you must be invited to - contact MT Newswires
directly."* This is not a resource for learning anything; it is a vendor's connector
listing. It has six identical siblings on the same shelf, and the worst of them is **Using
LSEG for financial market data analysis**: *"Invitation-only, and LSEG's own reference
documentation for it isn't published yet ('available soon') - you're contacting LSEG for
access to something even they haven't fully documented."* The site is telling me, in its
own words, that this page documents a thing that is not documented and that I cannot get.
It is still on my shelf, chipped `free`, and seven of the thirty-four slots I have go to
this family.

**3. Analyze fundraising performance** (Anthropic Academy, docs, 15 min, `free`). *"Skip
if: The page's own category chip says Marketing, but the actual content is nonprofit
development work (email, events, direct mail, corporate sponsorship) - **a mismatch worth
knowing if you're browsing by role**."* The card diagnoses a role mis-filing, in those
words, and then the site files it under my role anyway. If you know a page is filed wrong,
the fix is not to warn the reader you sent it to.

## 10. Everything that is broken, ranked (evidence for each)

**1. "Newest first" puts the oldest card first and the freshest card last.**
URL: `browse.html?role=data-analyst&level=confident`, Sort changed from "Best checked
first" to **"Newest first"**. What I saw: the first card of the sorted list (below the
three fixed picks) is **"AI prompt engineering: A deep dive"**, whose own date line reads
**"Published 5 Sep 2024 · over a year ago, may not match Claude today"**. The last card of
the same list is **"Let Claude use your computer in Cowork"**, whose date line reads
**"Updated 2 Sep 2026"** — four days before today, and the freshest date on the page. Under
"Best checked first" that card sits 6th; asking for newest moved it to 34th.
Expected: newest at the top, and at minimum not the single row the site itself flags as
over a year old. Harm: I sort by date to triage. A sort control that inverts itself is
worse than no sort control, because I would have acted on it. I checked "Shortest first"
on the same page — 15 min → 1 hour → half a day, correct — so the machinery works and only
this label lies.

**2. Sixteen of the thirty-four cards on my main shelf are chipped `free` and are not
free.** URL: `browse.html?role=data-analyst&level=confident`. I counted the cards whose own
text names a paid third-party subscription, an invitation, a waitlist, an Enterprise plan
or a paid Claude plan as a prerequisite: **16 of 34, and all 16 carry the chip `free`.**
Examples in their own words: *Draft investment memos* — *"Claude for Enterprise plus your
own paid Daloopa, S&P Global and Kensho subscriptions"*; *Build financial models* —
*"Daloopa, S&P Global and Box are all separate paid connectors"*; *Getting Started with
Claude for Financial Services* — *"This is a sold enterprise engagement - contact Sales or
AWS Marketplace"*; *Using S&P global data* — *"Access needs a commercial agreement with S&P
Global you must arrange directly"*. The same contradiction sits on one screen at
`resource.html?id=r-1e88a43d53`: chip **`free`**, and four lines below, **"Before this —
Paid Claude plan"**. `how-we-check.html` never defines what the cost chips mean.
Expected: a chip called `free` means I can do this thing for nothing. Harm: `free` is the
filter I would use to build an evening's reading list. Half of what it hands me is a sales
page. This is the site's own "we do not round up" promise failing on the one axis where
rounding up costs me money.

**3. Search does not agree with itself on the same question, and fails the two questions
that matter most to me.** URLs: `browse.html?q=how+do+I+stop+Claude+getting+my+numbers+
wrong` and `browse.html?q=why+does+Claude+give+me+a+different+total+every+time+I+ask`.
Asked the first way, the top five are *Working smarter with Claude in PowerPoint*, *Map
your understanding and build lessons from the gaps*, *How I use Claude Code for real
engineering*, *How do usage and length limits work?*, *How to Use Claude Code as a Product
Manager*; *Reduce hallucinations* is 11th and *How to Use Claude for CSV Data Analysis (The
Honest Guide)* is 30th of 77. Asked the second way, *How does Claude handle mathematical
equations and calculations?* is 2nd. Same for privacy: *"is it safe to upload our company
sales data to Claude"* puts *How long do you store my data?* 4th, behind a PayPal course
and an invitation-only connector; *"what happens to my data after I paste it into Claude"*
puts it 1st. Expected: two plain wordings of one question return roughly one answer set.
Harm: the home page invites me to *"describe what you want to do"*. If the answer depends
on which synonym I reached for, I cannot rely on the box, and the box is the fastest route
to the shelf.

**4. Every one of the 588 resource links previews as "Resource — Learn Claude".** URL:
any `resource.html?id=…`. I fetched `resource.html` raw and it ships
`<title>Resource — Learn Claude</title>` and
`<meta property="og:title" content="Resource — Learn Claude">`; JavaScript rewrites the
title after load, which no link unfurler runs. `og:description` is the generic *"What this
resource teaches, who it is for, who should skip it, and how thoroughly we checked it."*
Expected: pasting a link in Slack shows the resource's name. Harm: the resource page has a
**"Copy link"** button on it — the site is explicitly asking me to share — and everything
I share arrives at my team looking like the same blank card. This is how a directory like
this grows, and it is switched off.

**5. Path pages throw away the `Updated` date, on every path.** URL:
`paths.html?id=numbers-you-can-defend`, step 3. The path shows **"Read by AI / Checked 5
Sep 2026 / Published 24 Oct 2024"**. The same row's Browse card and its own resource page
both show **"Checked 5 Sep 2026 · Published 24 Oct 2024 · Updated 21 Jun 2026"**. I checked
a second path — `paths.html?id=pm-without-engineering` — and it contains **zero** "Updated"
lines, though two of its five steps carry one on Browse (*Use Claude Cowork safely*,
Updated 26 Aug 2026; *Claude Code for PMs*, Updated 9 Aug 2026). Expected: the same row
shows the same dates everywhere, or at least does not look staler in the place I am told
to start. Harm: paths are for people who do not yet know how to judge. It is the one
surface where a bare "Published 24 Oct 2024" will stop someone, and it is the one surface
where the site withholds the answer it already has.

**6. My one path routes me at step 3 through a superseded feature and never links the
replacement.** URL: `paths.html?id=numbers-you-can-defend`. Step 3 is *Introducing the
analysis tool in Claude.ai*. Its Browse card says: *"the analysis tool this post introduces
is being replaced by code execution... this is history rather than instruction... useless
as a guide to doing it today. Go to the code execution documentation for the current
feature."* The path page argues for keeping it — *"Here for the concept and not the
click-path"* — and tells me the toggle now lives under Settings then Capabilities. But
**the current code-execution documentation is not a step, and is not linked**. Expected: if
the path names a replacement, the path links it. Harm: step 3 is the pivot of the whole
arc — "the idea the rest of the path rests on", in the path's own words — and it hands me
a two-year-old announcement plus a menu location, and sends me to Google for the actual
instructions. Also, the site says "replaced" in one place and "renamed" in the other.

**7. Not one paid row in my role shows a price.** URL: `browse.html?role=data-analyst`.
**8 of the 72** rows are `subscription` or `sign-up needed`: *15 Claude Tips for Everyday
Data Analysis* (LinkedIn Learning, subscription), *Sales Analysis with Claude* (Coursera,
subscription), *Claude 101 (DataCamp)*, *Introduction to Claude Analysis* (Codecademy),
*Introduction to Claude (code-along)*, *Create Claude Skills for Data Tasks*, and two
cookbook notebooks. **None carries a figure.** Across all 588 rows only 4 do, and all 4
belong to other roles. Expected: "is it clear what you would pay before you click" — for me
the answer is no, at every level. Harm: smaller than finding 2, because "subscription" at
least warns me. But two of those eight are the only structured courses on my never-used
shelf.

**8. On a phone the "how well checked" badge is inert.** URL: any Browse page at 375px. The
badge is a `<span>` with `cursor: auto`, not inside a link; clicking it changes nothing.
Its definition lives in a `title` attribute and a `visually-hidden` element. Expected: the
label the site is proudest of should be tappable where most people read. Harm: moderate —
the resource page spells it out, so it is one extra tap, but the badge is what I scan.

**9. The `builder` level for my role is a developer shelf.** URL:
`browse.html?role=data-analyst&level=builder`. **7 of 12 are `code`; 7 of 12 are GitHub
repos.** Prerequisites in their own words: *"It wants Python, Jupyter and your own
Anthropic API key before the first cell runs"*; *"MCP config you edit by hand"*; *"It takes
live database credentials"*. Expected: "I've built things with it" should reach an analyst
who has built a repeatable analysis. Harm: this is the level I would honestly pick, and it
tells me my honest answer was wrong.

**10. One publisher owns my main shelf.** URL:
`browse.html?role=data-analyst&level=confident`. **24 of 34 cards are Anthropic Academy**;
47 of my role's 72 rows are Anthropic-published overall. Seven of the 24 are the
near-identical `Using <vendor>` connector pages. STATUS.md is open about the catalogue-wide
ratio (343 of 588, 58%) and `how-we-check.html` states it. Harm: at 71% for one publisher
on one shelf, the shelf stops being a comparison and becomes a table of contents for
somebody's marketing site. The site's whole value is that it compares.

## 11. The one thing that would make me leave and not come back

The sort control saying "Newest first" and handing me the oldest thing on the page.

Not because sorting is important. Because it is the one claim on this site I can check in
ten seconds without leaving the page, and it is false. Everything else this site sells me
is a claim I cannot check: that somebody read this, that this is who it is for, that this
is when it was last looked at. I am being asked to trust 588 assertions I have no way to
audit, and the one assertion I *can* audit — put the newest at the top — comes back wrong,
with the row the site itself flagged as "over a year ago, may not match Claude today"
sitting in first place.

That is exactly the failure mode I spend my working life guarding against: a number that
is confidently presented, plausibly formatted, and backwards. When I find one of those in
a report, I do not fix that cell. I stop trusting the report.

Second place, and only just: a `free` chip on sixteen rows that need a commercial
agreement with S&P Global.

## 12. What is genuinely good (honest, brief)

- **The skip lines are the product and they are excellent.** *"it carries an explicit
  prompt-injection warning - a downloaded template or a vendor's workbook can contain
  hidden instructions that push Claude into extracting or destroying data, and testing has
  produced exactly that."* I have never seen a directory tell me that about anything.
- **The path description for my role.** *"Analysts with a spreadsheet, a deadline, and
  somebody who will ask where the number came from."* Somebody has done this job.
- **The pick reasons are comparative, not descriptive.** *"The only candidate about what
  Claude gets wrong rather than what it can do"* — that is a judgement, which is the whole
  point and the part everyone else omits.
- **`how-we-check.html` names the person, names the AI, and puts a zero in the top row of
  its own quality ladder.** *"has not yet read a single resource end to end, which is why
  the strongest label has the count you can see above it."*
- **The thin-cell offer.** *"Only 2 at 'built things with it' for a teacher. The level
  below, 'used it a lot', has 8. Add 'used it a lot' too"* — the right offer, one click,
  no apology.
- **Two clicks from cold to a filtered shelf, no account, no tracking, no banner.** On a
  phone as well as a laptop.

## 13. Would I come back, and what one thing would make me?

Yes, once. Not as a place I trust — as a place I raid.

I would come back for the skip lines and nothing else. That *"Skip if:"* on Use Claude for
Excel saved me an afternoon and possibly a spreadsheet. I have bookmarked the path, and I
will do steps 1, 2 and 4 this week. But I will not use the search box again, because it
gave me a PowerPoint tutorial when I asked how to stop Claude getting my numbers wrong. And
I will not use the sort, and I will not believe the `free` chip, and I will not send a link
to a colleague because it arrives looking like nothing.

So: a raid, not a home. One visit, take the four things worth taking, close the tab.

The one thing that would bring me back properly is not more resources. It is the site
holding itself to the standard it holds everything else to. It tells 588 pages exactly who
should skip them and when they were last checked, and then it ships a sort that inverts,
a chip that says free about a thing that costs $3,000 of S&P Global, and a share link with
no name on it. Fix those three and I would come back monthly, because then the metadata
would be as good as the writing — and the writing is already better than anything else I
have found on this subject.

If I could only have one: **make `free` mean free.** Put the real gate on the chip — `needs
Pro`, `needs a paid connector`, `enterprise only` — and I will read this site every week,
because then a filtered shelf is a list of things I can actually do tonight instead of a
list of things somebody could do if they worked at a hedge fund.

## Checklist
- [x] I opened the live site
- [x] I tried all four levels
- [x] I quoted at least 5 real titles or lines from the site
- [x] Every number I used is in 00-facts.md, STATUS.md, or quoted from the site
- [x] I looked at a phone width
- [x] I read no file under scripts/ or data/
- [x] I found at least one thing nobody has mentioned before — two: the `free` chip is
      affirmatively wrong on 16 of the 34 cards on my main shelf (earlier files count the
      cost chips and note missing prices; none says the chip contradicts the card), and
      `paths.html` drops the `Updated` date on every step of every path while Browse and
      the resource page both show it.
