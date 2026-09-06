# Attack 3: a writer
Written as a freelance writer, 2026-09-06. Site version: 9deb0db.

I write for money. Some marketing, some editorial. My voice is the product. If a client
reads a paragraph and hears a machine, I lose the client. So I care about three things and
almost nothing else: keeping the words mine, knowing what I must disclose, and not being
accused later of passing off machine text as my own. Everything below is judged against
that.

---

## 1. The first 60 seconds

The home page says **"Find what's worth your time."** and then **"I'm a [role] and I've
[level]."** Two blanks. Ten role chips. I am the last chip: **"a writer"**.

I clicked it. The sentence completed to **"I'm a writer and I've [level]."** and the page
said **"84 resources match so far."** That is a good interaction. It is honest, it is
fast, and it does not ask me to make an account.

Three promises sit under the fold:

- **"We say when to skip"** — "Every entry has a Skip if: line. A link with no judgment is
  just a list, and lists are what made this hard in the first place."
- **"We say how we checked"** — "Four levels, and we do not round up."
- **"We show the date"**

That is a good pitch. It is also an incomplete one, and the incomplete part is the part I
would have wanted first. Nowhere on the home page does it say who wrote those judgments.
The footer says: **"Learn Claude is an independent directory. It is not affiliated with
Anthropic. Every entry says who it is for, who should skip it, and when we last checked
it."** No name. No mention of AI.

The answer is three clicks away on `how-we-check.html`, and it is this: **"The reading is
done by Claude, at the level each card's label claims and no further: Claude opens the
pages, writes the summary, the who-it-is-for and the who-should-skip-it lines, and chooses
the three picks."**

So every judgment on this site — the exact thing the home page sells me — is written by an
AI, and the home page does not say so. I am the visitor least likely to forgive that, and
I found it by accident.

**Sixty-second verdict:** good front door, and a disclosure problem sitting behind it.

---

## 2. Does the front door work for me (all four levels, with what I was shown)

I answered "a writer" and then each of the four levels in turn. Counts are the site's own,
read off the Browse header.

| level, in the site's words | resources | what the list actually is |
|---|---|---|
| never used Claude | 20 | the generic beginner list, with three odd extras |
| used it a little | 36 | **the real writer shelf.** Journalism ethics, AI tells, newsroom policy |
| used it a lot | 24 | marketing and nonprofit fundraising recipes |
| built things with it | 4 | four good things, three of which need Claude Code |

20 + 36 + 24 + 4 = 84, which matches the "84 resources match so far" the home page showed
before I picked a level. The counting is consistent. The content is not.

### never used Claude — 20

Titles 1 to 20, in the order given:
Claude 101 · Getting started with Claude.ai · My Claude AI Review (2026): Is It Worth the
Hype? · Choose a Claude plan (Help Center) · Claude is producing links that don't work and
falsely claiming that it has sent emails or produced external documents · How do usage and
length limits work? · How up-to-date is Claude's training data? · I Took 20+ Free Claude
Courses. These Are the Best · Troubleshoot Claude error messages · Use voice mode · What
are artifacts and how do I use them? · What are some things I can use Claude for? · What
interfaces can I use to access Claude? · AI capabilities and limitations · Using the
bioRxiv and medRxiv Connector in Claude · Work through grant options in chat ·
Next-Generation AI Assistant: Claude by Anthropic · Anthropic Claude for Absolute
Beginners · Claude 101 (DataCamp) · I tested Claude Cowork — Tom's Guide

**Not one of the twenty is about writing.** Ten are Claude Help Center pages.

I then opened `browse.html?role=non-technical&level=never-used`, which is the generic "not
a coder" cell, and got **52 resources**. I compared the two lists by hand. **17 of my 20
also appear in the "not a coder" list.** Only three are mine alone, and they are:

- **"Using the bioRxiv and medRxiv Connector in Claude"** — a preprint-server connector.
- **"Work through grant options in chat"** — "For: Grant administrators or proposal writers
  deciding which funders are worth pursuing."
- **"Next-Generation AI Assistant: Claude by Anthropic"** (Coursera) — whose own skip line
  reads: **"The title made you think Anthropic built it - it is a Coursera and Starweaver
  production, one module long, rated only 4.1 from 33 reviews, and it never leaves basic
  marketing prompts."**

So at the level where most people arrive, choosing "a writer" buys me 85% of the generic
list plus a preprint server, a grant-funding chart, and a course the site itself calls
one module long and 4.1-rated. The role question did almost nothing.

### used it a little — 36

This is the one that works. **"Claude, Editor"**, **"Wikipedia:Signs of AI writing"**,
**"How to Stop Claude Writing Like an AI"**, **"How to Spot AI Writing, According to
Wikipedia"**, **"The Guardian Updates Its AI Policies Around Training, Trust and In-House
Tools"**, **"Creating a Public AI Policy for Your Newsroom"**, **"AP Sets New AI Standards
for Newsroom Use"**, **"Proposed Revisions to SPJ's Code of Ethics (2026)"**, **"How Three
Newsrooms Are Charting Different Paths for AI Use"**.

Somebody thought about writers here. Whoever it was, this cell is why I did not close the
tab.

It is also visibly journalism-shaped. I am a freelancer, not a newsroom. Eight of the good
entries are about what a *publication* should do. None is about what a lone freelancer
puts in an invoice or a contract.

### used it a lot — 24 (this is my real level)

**14 of the 24 are Anthropic Academy.** Thirteen of those fourteen are single-recipe pages:

Adapt content across platforms · Analyze campaign performance · Analyze fundraising
performance · Audit a folder of visual assets against your guidelines · Build a campaign
brief · Create a company newsletter · Create brand assets · Develop a program toolkit ·
Grant proposal assembly line · Recap your ad performance · Repurpose content across
channels · Size a market using your research · Using the Blackbaud connector in Claude

That is marketing operations and nonprofit development work. Blackbaud is donor-management
software. "Analyze fundraising performance" is direct mail and corporate sponsorship. This
is not writing. It is the job of the person who books the writer.

The three cards actually about words at this level are **"Claude for Localization"**,
**"How to Use Claude Code for UX Writing"** and **"ux-writing-skill (open source)"**.

**This answers the brief's question directly: at my own level the role filter returns
marketing-ops work, not writing work.**

### built things with it — 4

Four, and the site says so plainly: **"Only 4 at 'built things with it' for a writer. The
level below, 'used it a lot', has 24. Add 'used it a lot' too"**.

The four are good: **"avoid-ai-writing (Claude Code / agent skill)"**, **"How I Use Claude
Cowork to Write With AI in My Voice"**, **"Package your brand guidelines in a skill"**,
**"Claude Skills for Journalism, Media & Academia"**. Three of the four need Claude Code
or a folder-and-markdown setup. Their own skip lines say so — "You don't use Claude Code
or a similar agent tool — this doesn't work as a plain chat prompt."

Also worth saying out loud: this cell shows **"Start with these three"** and then
**"Everything else for you (1)"**. Three picks out of four items. The heading is doing no
work.

---

## 3. What the catalogue actually gives me (are these really for me?)

**45 of my 84 are Anthropic's own** — 21 Anthropic Academy, 12 Claude Help Center, 9
Anthropic, 3 more Help Center. That is 54%, close to the 58% the site admits to on
`how-we-check.html` for the whole catalogue. I do not mind official material. I mind that
the official material for "a writer" is mostly a filing cabinet of marketing recipes.

### The card the site holds and hides from me

Search for **"write in my voice"** with no filter and the third result is a resource
literally called **"Write in my voice"** (Anthropic Academy). Its summary: "Analyzes your
own sent mail and messages to extract tone and style rules, saved as a reusable /my-voice
skill that improves as you correct its drafts over time."

That is the single most on-the-nose resource on this entire site for a writer.

Now run the same search with the writer filter on:
`browse.html?role=writer-marketer&q=write%20in%20my%20voice` → **20 results, and "Write in
my voice" is not one of them.** It is not in any of my four levels. It is not tagged for
"a writer".

Its who-for line is **"Anyone who writes a lot of internal communication and is tired of
editing Claude's generic drafting voice."** I can see the logic — "internal
communication" is not freelance journalism, so the rule dropped the tag. The result is
that the rule made the tags honest and made the shelf useless. A freelance writer who
filters by role never sees the site's best answer to their own core question.

### The three collection cards that were not made

The site has five collection cards: **Use cases for Sales · Use cases for Legal · Use
cases for HR · Use cases for Finance · Use cases for Operations**. I checked; those are
all five.

**There is no "Use cases for Marketing".** So the thirteen loose Anthropic Academy
marketing recipes never got bundled — and the role they were left sitting in is mine. The
tidy-up was applied to five families and skipped the sixth, and the sixth is the one that
lands on the writer's page. Nobody has mentioned this.

### Prices

STATUS.md: 10 paid-once and 16 subscription. That is 26 rows that cost money. I checked
every one on the live site. **Four carry a price chip**: "from $995", "from $2,999", "from
$3,000", "from $49". The other 22 show only a word — "pay once" or "subscription".

For me it is worse than that. `browse.html?role=writer-marketer&cost=paid-once,subscription`
returns **5 resources, and all 5 show no price**:

- Claude AI Comprehensive Guide (Coursera) — subscription
- Claude Cowork 7-Day Challenge (LinkedIn Learning) — subscription
- Everyday Productivity with Claude Cowork (LinkedIn Learning) — subscription
- Anthropic Claude for Absolute Beginners (Udemy) — pay once
- Claude, Claude Code, Claude Cowork, and Claude in MS Office (Udemy) — pay once

**Every paid thing a writer is shown has no price on it.** The four rows that do have
prices belong to other roles. So the answer to "is it clear what you would pay before you
click" is, for me, no — not once, not on any card.

### Dates

I counted the date lines on all 84 of my cards on the live page:

- **57 say "No publish date given"** (68%)
- 27 carry a Published date
- 28 carry an Updated date
- **2** carry the "over a year ago, may not match Claude today" note

The **Checked** dates are the good news: 49 say 5 Sep 2026, 18 say 29 Aug 2026, 12 say 18
Aug 2026, and the rest are 20–22 Aug 2026. Every card was looked at within the last three
weeks. That reads maintained.

The **Published** side reads unknowable. Two thirds of the shelf has no age at all, which
means the site's own freshness warning can almost never fire — and, as section 5 shows,
it fails to fire on exactly the document where it matters most to me.

---

## 4. Paths

There **is** a path for me, and it is the best single thing on this site:

**"Using Claude on work you put your name to"** — "Writers and marketers whose byline goes
on it, and who would rather not explain themselves later." For a writer. 4 steps, about an
hour and a quarter, free.

1. **Claude, Editor** — Restructured
2. **Wikipedia:Signs of AI writing** — Wikipedia
3. **How to Stop Claude Writing Like an AI** — Will Francis
4. **The Ethics of Using AI** — SPJ Ethics Central

The ordering argument on the path page is genuinely well made: *"The order runs from what
job Claude has, through the tells everyone else is trained to spot, to what you owe the
reader. The last step is the one people skip and it is the one with consequences."* And
step 4's note: *"Last, and last on purpose: everything above makes the work harder to
detect, which is exactly why disclosure has to be the step you finish on."*

I would follow that. I did follow it. Two things are wrong with it.

**a) The whole path sits at one level, and it is not mine.** I checked all 84 writer cards
for a path breadcrumb. Seven carry one, and all four writing-path steps appear only in the
"used it a little" cell. At "used it a lot" and "built things with it" — where I actually
am — **no card carries a path breadcrumb at all.** There is no route at my level. The
answer to the deferred question "paths above beginner level" is: for a writer, no.

**b) The last step is three and a half years old and the site hides that.** See section 5.

---

## 5. The card and the resource page

I opened four resource pages: *Claude, Editor*, *How to Stop Claude Writing Like an AI*,
*Write in my voice*, *The Ethics of Using AI*.

**Would I click through? Yes, on three of them.** The resource pages are the strongest
part of the build. They give a real summary, a "What it teaches" list, "Who it's for",
"Skip it if", "Before this" prerequisites where they exist, a plain "How we checked this
one" paragraph, and the checked date. *How to Stop Claude Writing Like an AI* is described
as "A practical, copy-pasteable set of Custom Instructions and a banned-words list, built
from Wikipedia's AI-writing-tells research plus the author's own year of producing content
with Claude." That is enough for me to spend fifteen minutes. I clicked.

### The one that broke my trust

`resource.html?id=r-3edab99ecf` — **The Ethics of Using AI**, SPJ Ethics Central, step 4 of
4 in my path.

- The resource page summary says: **"SPJ's early position statement on AI in journalism,
  prompted by the 2023 CNET AI-byline controversy…"**
- The skip line says: **"You need current, specific rules — this predates SPJ's 2026 Code
  of Ethics revision (see next entry)."**
- The date line says: **"Checked 5 Sep 2026 · No publish date given"**

So the site knows this is a 2023 document — it says "2023" in its own summary — and the
date line says **"No publish date given"**, which means it does not get the "over a year
ago, may not match Claude today" note that two other cards in my role do get. The freshness
warning is switched off on the oldest thing I was sent to read.

STATUS.md confirms the mechanism: this row is the single entry under **"Back in the pools
because we lost the evidence"** — "date we had 2023-02-01, age it implied 1313 days". The
date was dropped because ethicscentral.org blocks the automated check, and that host's
"last confirmed by a person" is **never**.

It gets worse in two more places:

1. **"(see next entry)" points at nothing.** On the resource page there is no next entry —
   the page ends. On the Browse card at writer/used-it-a-little, "The Ethics of Using AI"
   is row 10 and row 11 is "The Guardian Updates Its AI Policies", not the SPJ 2026
   revision. The document it means, **"Proposed Revisions to SPJ's Code of Ethics
   (2026)"**, is row 35 of the same list. The phrase assumes an ordering that no view of
   this site produces.
2. **On the path page the skip line is not shown at all.** Step 4 shows the narrative, the
   "Read by AI" badge, "Checked 5 Sep 2026" and "No publish date given". A reader who
   follows the path — the site's own recommended route — is never told the document
   predates the current code. They finish the path believing they have read the current
   professional standard. They have read the 2023 one.

That is the finding that matters most to me personally. The site built a path whose whole
argument is *"this is what you owe the reader"*, and the last step is a stale document
presented with its age erased and the current version unlinked.

### Badges, and whether I can find out what they mean

On a Browse card the badge is a plain `<span>` with a `title` attribute. Hovering with a
mouse shows "AI read all of it. No person has checked the notes yet." There is a
screen-reader description too, in a `visually-hidden` block. **There is nothing for a
sighted person who is not hovering, and there is nothing at all on a phone,** because a
`title` tooltip has no touch equivalent. The "How well checked" filter lists the four
words — Read in full, Read by AI, Skimmed, Found only — with no definitions attached.

On the **resource page** the badge *is* a link, to `how-we-check.html#tier-ai-reviewed`,
and the anchors exist and work. So the definition is reachable — one page deep, and only
if you click the title first.

### Publishers with no domain

The source line names a brand or a person and never the host. Step 1 of my path,
**"Claude, Editor"**, is credited to **"Restructured"**. The actual link is
`restructurednews.substack.com`. Pick 2 at my own level, **"Set Your Standards Before You
Start: A Journalist's Journey Using Claude.md"**, is credited to **"Stephen Stirling"**;
STATUS.md shows it is a `medium.com/@stephenstirling` post. Both may be excellent. But a
Substack and a masthead look identical on a card, and I am the reader who needs to tell
them apart before I cite one.

---

## 6. Search, in my words

Five sentences, typed the way I would type them.

| # | what I typed | top 3 I was shown | verdict | why |
|---|---|---|---|---|
| 1 | how do I stop Claude from making my writing sound like AI | 1. Write in my voice (Anthropic Academy) · 2. How to Stop Claude Writing Like an AI (Will Francis) · 3. Create on-brand content (use case) (Anthropic Academy) | ok | Result 2 is the answer, near-verbatim. Result 1 is the site's best voice resource. This is the search working properly. Note the irony: result 1 is a card the role filter will not show me. |
| 2 | do I have to tell my client I used AI to write this | 1. Support incident postmortem (Anthropic Academy) · 2. Set Your Standards Before You Start: A Journalist's Journey Using Claude.md (Stephen Stirling) · 3. Introduction to Model Context Protocol (Anthropic Academy) | bad | A support-incident recipe and an MCP intro for a disclosure question. Result 4 was "Red Green Refactor is OP With Claude Code". The site holds five disclosure documents and only one scraped into the top three. |
| 3 | is it safe to paste a client's unpublished draft into Claude | 1. How long do you store my data? (Claude Privacy Center · Anthropic) · 2. AI Fluency for Small Businesses (Anthropic Academy + PayPal) · 3. Introduction to Model Context Protocol (Anthropic Academy) | ok | Result 1 is exactly right — retention and training are the answer. Results 2 and 3 are noise, but the first card does the job. |
| 4 | will an editor be able to tell a machine wrote this | 1. Claude, Editor (Restructured) · 2. Claude Code overview and install guide (Anthropic) · 3. Complete Claude Code Course In 2 Hours For Developers (Krish Naik) | bad | Result 1 matched the word "editor" and is about using Claude *as* an editor — the opposite sense. Results 2 and 3 are Claude Code install guides. "Wikipedia:Signs of AI writing", the one document on this site that catalogues what AI prose looks like, ranked **28th of 32**. |
| 5 | what should I put in my contract about using AI | 1. Compare and analyze competing options (Anthropic Academy) · 2. Contract redlining and negotiation (Anthropic Academy) · 3. AI Fluency for Small Businesses (Anthropic Academy + PayPal) | bad | Result 2 is about redlining somebody else's contract, not about an AI-use clause in mine. Nothing here answers it. The site returned 30 confident-looking cards and never said the shelf is empty on this subject — `how-we-check.html` promises "when we have nothing on your subject, you get nothing back and a line saying so", and that did not happen. |

**Same question, two ways.** I asked question 2 again in different words: **"when do I need
to disclose that AI helped with an article"**. Top three: **Writing an AI diligence
statement** · **Elsevier — Generative AI policies for journals** · **Disclosing the Use of
AI (Princeton University Library)**. **The site did not agree with itself — the two top-3
lists share nothing at all.** The word "disclose" unlocks a whole shelf; "tell my client I
used AI" returns a support-incident postmortem. Same question, opposite outcome. A writer
who phrases it the human way gets nothing and concludes the site has nothing.

**One more, and it is not a sentence.** I typed the exact title **"Write in my voice"**.
The resource of that exact name came back **third**, behind "How I Use Claude Cowork to
Write With AI in My Voice" and "Create on-brand content (use case)". Quoting it — typing
`"Write in my voice"` with quote marks — changed nothing; the quotes are treated as
ordinary characters. An exact complete title match should not rank third.

---

## 7. On a phone

I set the viewport to 375 × 812 and worked through the home page, Browse and a resource
page.

**What is fine.** The document does not scroll sideways — `documentElement.scrollWidth`
is 375 at a 375 viewport, so nothing overflows. Type is large and readable. The role chips
reflow to a two-column grid. The illustration is dropped, which is right. Browse puts
Search and Sort at the top, the active filter chips below them, then the count, then
"Start with these three", with a sticky **Filters** button pinned at the bottom of the
screen. That is a sensible phone layout.

**What is not.** Two things.

1. **The badge is unreadable on a phone.** "Skimmed" and "Read by AI" are `<span>`
   elements whose only visible explanation is a `title` tooltip. A touchscreen has no
   hover. So on a phone the words "Skimmed" and "Read by AI" are undefined labels, on
   every card, and the only way to learn what they mean is to open a resource page and tap
   the badge there. The site's second promise — "We say how we checked" — is the one that
   breaks on the device most people will read it on.
2. **"a writer" is the last of ten chips**, bottom of the grid, and on a 375-wide screen
   the "Show me" button is already cut off by the fold when the chips are drawn. Small,
   but it means the role I need is the furthest one down.

I also noticed a console warning on every page load: *"The resource … Tiempos Fine
Light.woff2 was preloaded using link preload but not used within a few seconds from the
window's load event."* A font file downloaded and never used, on every page, on a phone
connection.

---

## 8. What changed since Attack 2 — my verdict on each

**Tags rebuilt on a rule.** Half works, half backfires. The `builder` cell is now four
things a person actually built, and it is the cleanest cell I have. But Rule B — drop a
role tag the card's own who-for line denies — deleted **"Write in my voice"** from the
writer role, which is the site's best writer resource. Honest tags, worse shelf. And the
rule did not fire where it obviously should: **"Analyze fundraising performance"** carries
a skip line reading *"The page's own category chip says Marketing, but the actual content
is nonprofit development work (email, events, direct mail, corporate sponsorship) - **a
mismatch worth knowing if you're browsing by role**."* The card diagnoses its own
mis-filing, in writing, and is still filed under "a writer". A rule that reads who-for
lines and misses that sentence is not finished.

**Five collection cards.** I never met one. `browse.html?role=writer-marketer` contains no
"Use cases for" card at all, and there are only five of them — Sales, Legal, HR, Finance,
Operations. No Marketing. So the thirteen loose marketing recipes were left un-bundled in
my role. The clean-up skipped exactly the family that lands on me.

**Search rebuilt.** Two of five ok, three bad, and it contradicts itself between two
wordings of the same question. Details in section 6. The stemmer and synonyms clearly do
something — question 1 is excellent — but the vocabulary they were tuned on is not mine.
"Disclose" works. "Tell my client" does not.

**Cards that were stripped.** Honest, not broken. **"Skip if: You want something we have
read. We have not opened this one yet."** with a "Found only" badge is exactly the right
sentence. One quibble: **"Head of Claude Code: What happens after coding is solved"** is
tiered `listed` *and* chipped `subscription`. Asking me to pay for something nobody has
opened is a bit much. Also, none of the three is in my role, so I only found them by
filtering for them deliberately.

**How well checked, as a filter.** Reachable with a mouse, reachable with a screen reader,
**not reachable on a phone and not reachable by keyboard alone from a card**. The filter
panel lists the four tier names with no definitions. And filtering on the top tier is a
trap: `browse.html?checked=reviewed` returns **0 resources** and says **"Nothing matches
all of those. Try removing one filter — time is usually the one to loosen."** I had set no
time filter. With a role and level also set, it says **"We have nothing for this
combination yet. It's on the list. Loosen the level…"** Loosening the level cannot help:
0 of 588 are "Read in full", by design. The empty state gives advice that cannot work and
never says the top badge is empty everywhere.

**The thin-level offer.** It works and I would take it. At writer/built-things-with-it the
line reads **"Only 4 at 'built things with it' for a writer. The level below, 'used it a
lot', has 24. Add 'used it a lot' too"**. Clicking it moved me to
`level=builder%2Cconfident` and the header changed to 28. Both numbers were correct. This
is the best-designed small thing on the site.

**Date lines.** Maintained on the "Checked" side — every one of my 84 cards was checked
within three weeks. Unknowable on the "Published" side — 57 of 84 say "No publish date
given". And the missing dates are not neutral: they suppress the age warning on the one
card where I needed it (section 5).

**Prices.** Not clear. **0 of the 5 paid rows in my role show a price.** Four rows on the
whole site show one, and none is mine.

**Who "we" is.** This raises my trust and then spends it. What it gets right: it says
outright that Claude writes every summary, every who-for line, every skip line and picks
the three picks, and that the person "has not yet read a single resource end to end". That
is braver than most sites manage and it is the reason the "0 Read in full" count is
credible rather than embarrassing.

What it gets wrong, and it is the thing my whole job is about: **the disclosure page names
an employer and withholds a name.** "One person makes this site - a researcher at the
Technical University of Denmark, working on it outside their job." That borrows a
university's credibility while staying anonymous. The name is on the site — it is in the
URL of the "Something wrong with this one? Tell us" link on every resource page,
`github.com/Mojtaba-Alehosseini/learn-claude` — so the anonymity is not even holding. Put
the name on the page.

And the second half: **none of this is on the home page.** The home page sells "We say when
to skip" and never says who "we" is. **485 of 588 cards say "Skimmed"** and the tier
definition reads "**We** read the outline or a free sample" — where "we" turns out to mean
Claude, three pages away. A reader who never opens `how-we-check.html` will finish this
site believing a person skimmed 485 things. **Is it enough? No.** One line under the
headline would fix it: *the judgments on this site are written by Claude and checked by one
person.*

**The picks block.** Reasons are good. At my level the three were **AI Fluency for Creative
Work** — "The only candidate with a repeatable method for the question this level actually
faces - when AI use protects a creative practice and when it erodes it" — **Set Your
Standards Before You Start** — "The only candidate about a writer's own ethical standards…
The skill-shaped candidates here encode a house style; this encodes a conscience" — and
**Claude Cowork Just Changed How You Do Marketing**. I would open the first two. The third
is a marketing video and I would skip it. Two of three is a good hit rate and the reasons
are the best-written prose on the site. At builder level, though, "Start with these three"
picks 3 of 4 items and then says "Everything else for you (1)", which is a heading doing
no work.

**The social preview title.** Broken everywhere except the home page. I checked the meta
tags on four pages:

| page I would share | `<title>` | `og:title` |
|---|---|---|
| home | Learn Claude — find what's worth your time | Learn Claude — find what's worth your time |
| my path | Using Claude on work you put your name to — Learn Claude | **Paths — Learn Claude** |
| my filtered browse | Browse 20 Claude resources — Learn Claude | **Browse — Learn Claude** |
| a resource | The Ethics of Using AI — Learn Claude | **Resource — Learn Claude** |

There is no `og:image`, no `og:url` and no canonical link on any of them. If I post the
writing path into a freelancers' Slack, the unfurl says "Paths — Learn Claude" with a
generic description. Nobody clicks that. This site has no analytics, no accounts and no
newsletter — **sharing is its only distribution** — and every deep link previews as a
category label.

**The home attract loop.** I watched the home page for about 45 seconds without touching
it. The illustration cycles — a book, a bar chart, a blackboard, a paintbrush, a node
graph — and one role chip lights up with each. In that time it highlighted **a designer**,
**working with data**, **a teacher** and **a product manager**. It never highlighted **a
writer**. And in every frame the headline still read **"I'm a [role] and I've [level]."**
The loop demonstrates the chips and never demonstrates the sentence, which is the one
thing a placeholder headline needs to teach.

**The sort control.** "Shortest first" is correct — 15 min, then 1 hour, then half a day,
in that order down 84 cards. **"Newest first" is not.** On
`browse.html?role=writer-marketer&sort=newest`:

- Row 27 is **"AI prompt engineering: A deep dive"**, "Published 5 Sep 2024 · over a year
  ago, may not match Claude today".
- Row 30 is **"How Can I Create and Manage Projects?"**, "No publish date given · **Updated
  3 Sep 2026**".

A page updated three days ago sits below a page published two years ago, and both dates
are printed on the cards where anyone can compare them. Row 2 has the same problem in
miniature: "Published 17 Jun 2026 · Updated 23 Aug 2026" sits below row 1's "Published 11
Aug 2026". "Newest" reads only the published date, ignores the updated date, and dumps all
57 undated cards at the bottom — so for a shelf that is 68% undated, "Newest first" sorts
about a third of what I am looking at and shuffles the rest. The label does not say that.

**Paths above beginner level.** For a writer: no. All four steps of the only writing path
sit at "used it a little". At my level, no card in 24 carries a path breadcrumb.

---

## 9. Content quality — the three worst entries I was shown, quoted

**1. "Analyze fundraising performance" (Anthropic Academy) — shown at writer / used it a
lot.**
> For: Marketers and analysts deciding which channels get next year's budget. The worked
> example is a nonprofit's events, email and direct mail.
> Skip if: The page's own category chip says Marketing, but the actual content is nonprofit
> development work (email, events, direct mail, corporate sponsorship) - **a mismatch worth
> knowing if you're browsing by role.**

The card tells me, in its own skip line, that its role filing is wrong — and the site files
it under my role anyway. This is the worst entry on my page because it is not a mistake the
system failed to see. It is a mistake the system wrote down and kept.

**2. "Using the Blackbaud connector in Claude" (Anthropic Academy) — writer / used it a
lot.**
> For: Fundraising and communications staff who already use Raiser's Edge NXT and want
> Claude to draft donor letters and appeals.
> Skip if: Needs a Blackbaud marketplace admin to install and approve scopes before an org
> owner or individual can even connect - not a self-serve setup for one person.

A donor-CRM connector, requiring a corporate admin, offered to a freelance writer. The skip
line says a single person cannot even set it up. Nothing about this belongs on my shelf.

**3. "The Ethics of Using AI" (SPJ Ethics Central) — step 4 of 4 of my path.**
> Skip if: You need current, specific rules — this predates SPJ's 2026 Code of Ethics
> revision (see next entry).
> Checked 5 Sep 2026 · No publish date given

Its own summary dates it to the 2023 CNET controversy. Its date line says no date is known,
so it escapes the "over a year ago" warning. Its pointer to the current version — "see next
entry" — resolves to nothing on the resource page, to the wrong card on Browse, and is not
shown at all on the path. And on the path page it is presented as the destination: "This is
what you owe the reader."

Dishonourable mentions, both at writer / never used Claude: **"Using the bioRxiv and medRxiv
Connector in Claude"** ("For: Researchers, journal editors and science journalists who need
early, not-yet-peer-reviewed findings") and **"Work through grant options in chat"** ("For:
Grant administrators or proposal writers…"). Both are offered to someone who has never
opened Claude.

---

## 10. Everything that is broken, ranked (evidence for each)

Ranked by what it costs a reader, not by effort to fix.

**1. The writing path ends on a 2023 document with its age erased, and the current version
is not linked.**
`paths.html?id=writing-you-sign`, step 4 → `resource.html?id=r-3edab99ecf`. Card and
resource page both say "No publish date given", so no age warning fires. The resource
summary says "prompted by the 2023 CNET AI-byline controversy". The skip line says
"predates SPJ's 2026 Code of Ethics revision (see next entry)" — and there is no next
entry on the resource page, the next Browse row is "The Guardian Updates Its AI Policies",
and the path page does not show the skip line at all. **Harm:** a writer follows the site's
own recommended route on the one subject with legal and reputational consequences, and
finishes on superseded guidance believing it is current. The correct document, "Proposed
Revisions to SPJ's Code of Ethics (2026)", is row 35 of the same list, unlinked.

**2. Searching the way a person talks fails on the question this role most needs
answered.**
`browse.html?q=do I have to tell my client I used AI to write this` → "Support incident
postmortem", "Set Your Standards Before You Start", "Introduction to Model Context
Protocol". Reworded as "when do I need to disclose that AI helped with an article" → three
correct disclosure documents. **Harm:** the site holds the answer and hands it over only if
you already know the professional word for it. The reader who does not gets an MCP intro
and concludes the site is empty on disclosure. The two answers share no results, so the
site disagrees with itself.

**3. The home page never says the reviews are written by AI.**
`index.html` full body text contains no mention of AI. `how-we-check.html` says "The
reading is done by Claude… Claude opens the pages, writes the summary, the
who-it-is-for and the who-should-skip-it lines, and chooses the three picks." 485 of 588
cards say "Skimmed", whose definition is "**We** read the outline or a free sample".
**Harm:** the entire value proposition is human-sounding judgment, and the reader learns it
is machine-written only if they click a nav item named "How we check". For a site whose
audience includes people worried about undisclosed AI text, that is the wrong way round.

**4. The role filter returns marketing operations, not writing, at the level most writers
are at.**
`browse.html?role=writer-marketer&level=confident` → 24 resources, 14 from Anthropic
Academy, 13 of them single-recipe marketing and nonprofit-fundraising pages including
"Analyze fundraising performance", "Using the Blackbaud connector in Claude" and "Size a
market using your research". **Harm:** the reader who answers both questions honestly gets
somebody else's job. The role is called "a writer" on the front door and delivers a
marketing-ops filing cabinet.

**5. The site's best writer resource is invisible to writers.**
`browse.html?q=write in my voice` → "Write in my voice" (Anthropic Academy) at position 3.
`browse.html?role=writer-marketer&q=write in my voice` → 20 results, not including it. It
appears in none of the four writer levels. **Harm:** the role filter, which is the site's
whole navigation idea, actively hides the card that answers the role's defining question.

**6. Every shared deep link previews as a generic word.**
`og:title` is "Paths — Learn Claude" on a specific path, "Browse — Learn Claude" on a
filtered browse, "Resource — Learn Claude" on a resource page. No `og:image`, no `og:url`,
no canonical. **Harm:** the site has no other distribution channel. Every recommendation a
reader makes on its behalf arrives looking like nothing.

**7. "Newest first" ranks a two-year-old page above one updated three days ago.**
`browse.html?role=writer-marketer&sort=newest`: row 27 = "AI prompt engineering: A deep
dive", "Published 5 Sep 2024 · over a year ago"; row 30 = "How Can I Create and Manage
Projects?", "Updated 3 Sep 2026". Both dates printed on the cards. 57 of 84 undated cards
are dumped below everything dated. **Harm:** the one control a reader uses to avoid stale
material puts stale material on top.

**8. Nothing on a writer's shelf shows a price.**
`browse.html?role=writer-marketer&cost=paid-once,subscription` → 5 resources, 0 price
chips. Four rows in the whole catalogue carry a price and none is in this role. **Harm:**
"pay once" on a Udemy course could be nine dollars or ninety. The reader clicks out to
find out, which is the thing the site exists to prevent.

**9. Filtering on the best badge returns nothing and blames the wrong filter.**
`browse.html?checked=reviewed` → "0 resources. Nothing matches all of those. Try removing
one filter — time is usually the one to loosen." No time filter was set. With role and
level set the message becomes "We have nothing for this combination yet… Loosen the
level", which cannot help: 0 of 588 are "Read in full". **Harm:** the reader who most
wants human-verified material is told, twice, to change something irrelevant, and never
told the tier is empty by design.

**10. On a phone, the tier badge has no explanation at all.**
The Browse card badge is `<span class="badge" title="…">`. A `title` tooltip needs hover.
No hover exists on touch. **Harm:** "We say how we checked" is the site's second promise,
and on the majority device the words carrying it are undefined.

**11. The attract loop never shows the sentence it is teaching, and never shows my role.**
45 seconds of watching `index.html`: the headline stayed "I'm a [role] and I've [level]."
through every cycle; chips lit for a designer, working with data, a teacher, a product
manager; a writer never lit. **Harm:** small. The loop's whole job is to show what the
completed sentence looks like, and it never does.

**12. A font is preloaded on every page and never used.**
Console, every page: "Tiempos Fine Light.woff2 was preloaded using link preload but not
used within a few seconds from the window's load event." **Harm:** small, and worst on a
phone connection.

**13. There is no "Use cases for Marketing" collection.**
`browse.html?q=Use cases for` returns exactly five: Sales, Legal, HR, Finance, Operations.
Meanwhile 13 loose marketing recipes sit in the writer role. **Harm:** small on its own,
but it is the cause of finding 4 — the bundling that cleaned up five families never
reached the sixth.

**14. Publisher names never show a host.**
"Restructured" is `restructurednews.substack.com`. "Stephen Stirling" is a `medium.com`
post. Both appear as bare bylines. **Harm:** a reader deciding what to cite cannot tell a
self-published post from a publication without clicking out.

---

## 11. The one thing that would make me leave and not come back

Finding 1. The path called **"Using Claude on work you put your name to"** — a path whose
own text says *"The last step is the one people skip and it is the one with
consequences"* — ends on a 2023 position statement, shown with no date, no age warning,
and a pointer to the current version that resolves to nothing.

If I had followed that path, told a client I was working to the professional standard,
and then found out the standard had been revised in 2026 and the site had a copy of the
revision it never showed me — I would not come back. Not because the site made a mistake.
Because it made the mistake in the exact place it told me to trust it most, and dressed
the mistake in a confident sentence about what I owe the reader.

Everything else on this list I would forgive. That one I would not.

---

## 12. What is genuinely good (honest, brief)

- **The "Skip if:" line is the real product.** "You want a short list — this runs to
  roughly 15,000 words and is written for Wikipedia editors first, general writers second."
  That is a sentence written by somebody who does not want to waste my afternoon. No other
  directory does this.
- **The writer path exists and its argument is right.** Job first, tells second, treatment
  third, disclosure last. That ordering is correct and I have not seen it laid out
  anywhere else.
- **"used it a little" is a genuinely good writer's shelf** — Wikipedia's AI-tells page,
  the Guardian policy update, AP's standards, the SPJ 2026 revision, the Nieman Lab
  comparison. Someone thought about my job when they built that cell.
- **The 0 next to "Read in full" is stated on the front of the how-we-check page.** "Today
  the count read in full is zero." A site that admits its best label is empty is a site I
  can calibrate.
- **The thin-level offer is exactly right.** "Only 4 at 'built things with it' for a
  writer. The level below, 'used it a lot', has 24. Add 'used it a lot' too" — correct
  numbers, one click, no lecture.
- **The picks reasons are the best prose on the site.** "The skill-shaped candidates here
  encode a house style; this encodes a conscience."
- **"No publish date given" instead of a guess.** I would rather see the gap than a number
  somebody made up — as long as the gap does not switch off the age warning, which it does.
- **No accounts, no tracking, no progress bar.** "We do not track your progress. Nothing
  here needs an account." Thank you.

---

## 13. Would I come back, and what one thing would make me?

Yes, but not for the reason the site wants.

I would come back for that one shelf — "a writer", "used it a little". Wikipedia's AI tells
page, the Guardian's policy update, the SPJ revision, the Nieman Lab piece on three
newsrooms. That is a reading list I would send to another freelancer. I bookmarked it. And
I would come back for the skip lines, because nobody else writes them, and reading "this
runs to roughly 15,000 words" saved me an hour today.

I would not come back for the thing the front door promises. It asked what I am and I said
a writer, and at my actual level it handed me thirteen recipes about campaign briefs, ad
recaps, donor letters and market sizing. That is not my job. That is the job of the person
who hires me. And when I searched for the thing I actually worry about — whether I have to
tell a client — it gave me a support-incident postmortem.

**The one thing that would bring me back properly:** put the disclosure on the front, and
put a date on everything you recommend.

Say on the home page, in one line, what the how-we-check page already says honestly: *the
judgments here are written by Claude; one person sets the rules and has not read a single
resource end to end.* I will trust you more, not less, for saying it where I cannot miss
it. Hiding a good disclosure three clicks in is the same instinct that makes a writer put
"assisted by AI" in the footer at 8pt, and I recognise it because I have done it.

And then fix step 4 of my path. If you know a document is from 2023 — you say so in your
own summary — say it on the card. If you hold the 2026 revision, link it. A path about
what I owe the reader cannot end on a page where you did not do the same.

Do those two, and I will send this site to every freelancer I know.

---

## Checklist
- [x] I opened the live site
- [x] I tried all four levels
- [x] I quoted at least 5 real titles or lines from the site
- [x] Every number I used is in 00-facts.md, STATUS.md, or quoted from the site
- [x] I looked at a phone width
- [x] I read no file under scripts/ or data/
- [x] I found at least one thing nobody has mentioned before
