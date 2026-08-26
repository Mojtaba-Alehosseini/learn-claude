# Attack: a writer
Written as someone who is a writer, at 2026-08-27. Site version: 22e4532.

I write for money. Some of it is copy, some of it is longer. I have one hour, and I am
here because a client asked whether I use AI and I did not have a clean answer. I do not
need a tour of the chat window. I need to know whether this thing can write in my voice,
whether anyone can tell, and what I am supposed to say when they ask.

---

## 1. The first 60 seconds

The home page is good-looking and it is honest about being a list. "Find what's worth
your time." Then a sentence with two holes in it: *"I'm a [role] and I've [level]."*
I like it. It is a sentence, not a form. Somebody who writes made that.

Then I look for myself in the ten chips and I am the tenth. Last. Alone on the second
row, after "running a business".

```
Live, https://mojtaba-alehosseini.github.io/learn-claude/ — the ten role chips in order
not a coder · a student · a researcher · a teacher · a developer
working with data · a product manager · a designer · running a business
a writer
```

**"a writer."** Two words. I click it and the drawing changes to a pencil lying on a
closed book, and the tally says:

```
41 resources match so far.
```

Now — I am also the person who buys the ads. The chip does not say so. The underlying
key does:

```
$ grep -n "writer-marketer" assets/js/ui.js
22:    "business-founder": "running a business", "writer-marketer": "a writer"
```

`writer-marketer`. One shelf for a novelist and a demand-gen marketer. Those are not the
same person and they do not want the same hour. The site knows it — the key has a hyphen
in it — and it decided to show me the half of the word that makes a nicer chip. Hold that
thought, because section 3 is about what it cost.

Sixty seconds in: pleasant, well-written, and I have already been mislabelled.

---

## 2. Does the front door work for me (all four levels, with counts)

I answered as myself at every level. Read live off the tally line on
`https://mojtaba-alehosseini.github.io/learn-claude/`:

```
role only            -> 41 resources match so far.
never used Claude    ->  3 resources match so far.  | "I'm a writer and I've never used Claude."
used it a little     -> 28 resources match so far.  | "I'm a writer and I've used it a little."
used it a lot        ->  7 resources match so far.  | "I'm a writer and I've used it a lot."
built things with it ->  3 resources match so far.  | "I'm a writer and I've built things with it."
```

Matches `00-facts.md` and `python docs/attack/role-view.py writer-marketer --counts`
exactly: 3 / 28 / 7 / 3.

**The curve is wrong for the people it catches.** 28 of 41 sit at "used it a little" —
68% of my whole shelf in one bucket. Three cards for someone who has never opened Claude.
Three for someone who has built something.

That middle bulge is not a curve, it is a landfill. It is where everything goes that
nobody graded properly. And it is where I am. Look at what is in it — the on-screen order
from `python docs/attack/role-view.py writer-marketer basic`, cards 13, 14 and 15, three
in a row:

```
13. FULL Claude Tutorial For Beginners in 2026! (FULL COURSE)   — Productive Dude, half-day
14. FULL Claude Tutorial for Beginners in 2026! (Become a PRO!) — AI Foundations, one hour
15. Full Claude Tutorial: Beginner to Advanced in 19 Minutes    — Futurepedia, one hour
```

Three near-identical titles, back to back, none of them about writing. If you are sorting
resources for a writer and you hand them three general YouTube tours of the product in
consecutive slots, you have not sorted anything. You have concatenated.

The front door itself works. The two questions are answered in four clicks, the number
updates before I commit, and "Show me" takes me to a filtered Browse. Mechanically fine.
It is the shelf behind the door that is wrong.

---

## 3. What the catalogue actually gives me (are these really for me?)

I read all 41 `who_for` lines. Here is who the site thinks I am.

**It thinks I am a journalist.**

```
$ python docs/attack/role-view.py writer-marketer | grep "    For:" \
    | grep -Eiw "journalist|journalists|journalism|newsroom|newsrooms|editor|editors|editorial|reporter|reporters|outlet|outlets" | wc -l
11

$ python docs/attack/role-view.py writer-marketer | grep "    For:" \
    | grep -Eiw "marketer|marketers|marketing|SEO|copywriter|copywriters|campaign|campaigns|brand|ads|advertising|growth|conversion|funnel" | wc -l
5
```

Eleven to five. Verbatim, from the live cards:

> *"An editor or small newsroom without an AI policy who needs a starting checklist of
> what to cover."*

> *"Journalists, editors, and freelancers who want current professional-body ethics
> language to cite or adapt for a newsroom policy."*

> *"A newsroom or freelance journalist comfortable installing Claude Code who wants
> journalism-specific guardrails rather than generic writing skills."*

> *"Anyone benchmarking their own disclosure policy against a major outlet that moved
> from an outright ban to a narrow, approved list of AI uses."*

I do not have a newsroom. I do not have an outlet. I have three clients and an invoice
template. The chip says "a writer" and the shelf says *staff journalist at a mid-size
publication*. Half the people that chip catches will not recognise themselves in a single
one of those lines.

**And it has nothing at all for the marketer half of its own key.**

```
$ python -c "term in json.dumps(item).lower(), over all 353 items"
seo                catalogue  2 | writer-marketer  0
search engine      catalogue  0 | writer-marketer  0
content marketing  catalogue  0 | writer-marketer  0
email marketing    catalogue  0 | writer-marketer  0
press release      catalogue  0 | writer-marketer  0
landing page       catalogue  4 | writer-marketer  1
copywriting        catalogue  3 | writer-marketer  2
```

Zero SEO. Zero content marketing. Zero email marketing. Zero press releases. Across the
whole 353, not just my 41. The role is literally named `writer-marketer` and the word
"SEO" does not appear on my shelf once.

Search agrees:

```
$ python scripts/test-search.py "seo"
"seo"   1 result(s)
     17.6  [pm,non-technical     ] How to use Claude Code for non-engineering use cases
```

One result on the entire site, and it belongs to a product manager.

**The one entry that does name my job is the one entry that costs money.**

```
23. [Skimmed] Claude AI Comprehensive Guide
    Coursera · course · half-day · subscription · checked 2026-08-18 · published UNVERIFIED
    Summary: "A six-module Coursera course with one module specifically on marketing and
              copywriting tasks (long-form content, landing pages, social media)..."
    Skip if: You don't want a Coursera Plus subscription — the course is listed as
             included with Coursera Plus rather than as a standalone free offering.
```

36 of my 41 are free (`--counts`: `free: 36`). Exactly one takes a subscription. It is
the only one in the catalogue whose description contains the words *marketing*,
*copywriting*, *landing pages* and *social media*. And the site's own skip line pushes me
off it. So the marketer's answer is: pay Coursera, or nothing.

**Half the shelf is not addressed to anyone like me.**

```
$ python -c "count who_for lines with no writing/editing/marketing/journalism word"
cards whose "For:" line never names writing, editing, marketing or journalism: 18 of 41
```

Eighteen. Including *"People who have never opened Claude and want the basics fast."*,
*"Knowledge workers who have heard Cowork mentioned…"*, *"Methodical learners who want a
single long course…"*. Those are not writers. Those are anyone.

**And here is the seam.** The shelf is two piles, and you can date them:

```
$ python -c "group my 41 by checked date"
2026-08-18  n=21  formats={docs:6, article:12, repo:2, course:1}  only-this-role=21
2026-08-20  n= 2  formats={course:2}                             only-this-role= 0
2026-08-21  n= 3  formats={article:1, course:1, hands-on:1}       only-this-role= 0
2026-08-22  n=15  formats={video:13, article:1, docs:1}           only-this-role= 0
```

All 21 of my only-this-role resources were checked on one day, 18 August. Every one of
the other 20 was borrowed from another role's shelf, and 13 of those are YouTube videos
added on 22 August. So: 21 cards someone actually chose for a writer, plus 20 cards of
generic Claude onboarding shovelled in to make the number look less thin.

41 is not 41. It is 21 and a bulking agent.

**On the thing I came for.** Disclosure. Whether a client can tell. The catalogue has
resources on exactly this — and none of them is on my shelf:

```
$ python -c "catalogue items about AI detection / disclosure"
Disclosing the Use of AI                       roles=student,researcher
Documenting Your AI Use                        roles=student
Referencing AI and Acknowledging AI Use        roles=student
Guidance on AI detection, and why we're
  disabling Turnitin's AI detector             roles=teacher
Plagiarism and Academic Integrity 101          roles=student
```

Four resources on how to disclose AI use and one on whether detection works. All tagged
student, researcher or teacher. **Zero tagged `writer-marketer`.** A student who fails to
disclose gets a bad grade. A freelancer who fails to disclose loses a client and possibly
gets sued over a contract clause. The site gave the disclosure material to the people with
the lower stakes.

What I get instead is my entire `safety` allocation:

```
$ python -c "writer-marketer items tagged safety"
[basic] The Ethics of Using AI
[basic] Proposed Revisions to SPJ's Code of Ethics (2026)
[basic] Creating a Public AI Policy for Your Newsroom
[basic] The Guardian Updates Its AI Policies Around Training, Trust and In-House Tools
[basic] How Three Newsrooms Are Charting Different Paths for AI Use
[basic] AP Sets New AI Standards for Newsroom Use
```

Six documents. Six of them about what an *institution* should publish. Not one about what
a person with an invoice should tell a client. I asked "will they know?" and the site
handed me the Society of Professional Journalists' code of conduct.

**What is genuinely on-target**, and I want to be fair, is the AI-tells cluster — four
cards that go straight at "does this read like a machine":

```
 6. How to Stop Claude Writing Like an AI          (basic, article, 15 min, free)
10. Wikipedia:Signs of AI writing                  (basic, docs, one hour, free)
 5. How to Spot AI Writing, According to Wikipedia (basic, article, 15 min, free)
40. avoid-ai-writing (Claude Code / agent skill)   (builder, repo, one hour, free)
```

That is real curation and I would use it. But note the shape: the practical automated
tool is at **builder** and needs Claude Code, and the most thorough reference is 15,000
words written for encyclopedia editors. The writer at `basic` — 28 of 41, me — gets the
condensed blog summary and a homework assignment.

---

## 4. Paths

I have none. That is already known, one line, done.

What is *not* one line is what the Paths page does with that fact: nothing. Live text
from `paths.html`:

```
Paths
A short list, in order. Start at the top.

Your first week with Claude   — 6 steps · about 2 hours · free
Getting good at Claude Code   — 6 steps · about 6 hours · free
Using Claude for research without embarrassing yourself — 5 steps · about 2 hours · some paid steps
```

Three routes. "Start at the top." Nothing says which of them is for me, and nothing says
none of them is. So I do the reasonable thing and start the one that sounds general.

```
$ python -c "path steps vs writer-marketer tag"
Your first week with Claude — 6 steps | steps tagged writer-marketer: 1
   [  ] Claude is not one tool. It's six.        (roles: non-technical)
   [  ] Get started with Claude                  (roles: non-technical)
   [WM] Claude 101                               (roles: business-founder,data-analyst,non-technical,researcher,writer-marketer)
   [  ] What are Projects?                       (roles: researcher)
   [  ] Why do AI models hallucinate?            (roles: non-technical)
   [  ] Get started with Claude Cowork           (roles: business-founder,non-technical)
total steps across all paths: 17
```

**Five of the six steps in the only path I would plausibly pick are resources this same
site decided are not for a writer.** Across all three paths, 1 of 17 steps carries my
tag, and it is Claude 101 — the never-used entry point.

The path data even has a `roles` field. `paths.json` says
`roles: ['non-technical','student','teacher','business-founder']` for that first path.
The page never reads it. So the site knows I am excluded and shows me the door anyway.

`paths.html?role=writer-marketer` does the same thing as `paths.html`. The parameter is
dropped.

---

## 5. The card and the resource page

The card layout is the best thing here. Badge, title, publisher, three chips, **For:**,
**Skip if:**, checked date. That order is right and the `Skip if:` line is a real idea.

Then I read one out loud. Live, first card on `browse.html?role=writer-marketer&level=basic`:

> **Skip if:** Skip if you already build your own tooling — the lesson here is that a
> non-coder can, which you know. Skip too if you want prompt craft rather than workflow
> automation.

Three "skip"s in one line, one of them printed by the template. Measured live in the page:

```js
// browse.html?role=writer-marketer&level=basic
Array.from(document.querySelectorAll('#results .card-skip'))
     .filter(e => /^Skip if:\s*Skip/.test(e.innerText)).length
→ 13     // of 28 cards on screen
```

Across all four of my levels it is 18 of 41. This has been noticed before for another
role, so: confirmed, one line, moving on. **What has not been noticed is why it happens
on some cards and not others.**

```
$ python -c "my 41, grouped by checked date"
checked      n   median len   starts "Skip if"   em dash (—)   spaced hyphen ( - )
2026-08-18  21      104            0                18              0
2026-08-20   2      115            0                 2              0
2026-08-21   3      169            3                 0              3
2026-08-22  15      150           15                 2              6
```

Two writers. Two style sheets. **The 18 August batch never says "Skip if" twice and
always uses an em dash. The 22 August batch always says "Skip if" twice and reaches for a
spaced hyphen.** You can date any card on this site by looking at its punctuation.

Site-wide it is a coin flip:

```
$ python -c "whole catalogue 353"
starts "Skip if...": 161 | starts "You...": 180 | other: 12
em dash: 77 | spaced hyphen: 84
```

I am being sold judgment about writing by a site that cannot hold a house style across
353 entries. That is not pedantry. If you cannot keep one dash consistent, I do not
believe your claim that a person weighed each of these.

**The resource page.** I opened three. `r-da0e8aedbc`, "How to Stop Claude Writing Like
an AI" — good page, I would click through. What it teaches is three concrete bullets, the
skip line is honest, the date is there. But the byline reads:

```
Willfrancis · Will Francis
Open on Willfrancis
Checked 18 Aug 2026 · Published 13 Mar 2026 · Found through Willfrancis
```

The publisher is a domain with a capital letter glued on, printed three times, once
beside the human name it was scraped from. `ui.js` has a function whose entire job is to
suppress that — its comment says *"Anthropic Academy · Anthropic" says the same thing
twice* — and it fails here because the two strings differ by one space. Two of my cards
do this: "Willfrancis · Will Francis" and "Theopennotebook · The Open Notebook".

Nine of my 41 print a machine-cased domain as a publisher. The worst is not even a
domain:

```
"Open on Cloud"    <- ranthebuilder.cloud
```

**The site took a top-level domain and used it as a publisher name.** "Open on Cloud."
Also on my shelf: "Open on Journalism" (journalism.co.uk), "Open on Substack"
(restructurednews.substack.com — the actual publication name thrown away), "Open on
Beutlerink", "Open on Ethicscentral", "Open on Localizelikeapro", "Open on
Ccforeveryone", "Open on Niemanlab".

Second page, `r-6a6a4daf55`, "AP Sets New AI Standards for Newsroom Use". Live:

```
Found only
...
What it teaches
— track changes in major press agency ai standards
— define appropriate boundaries for ai-generated headlines and summaries
— keep human reporting central in newsrooms using ai
...
How we checked this one
Found only. We found it and sorted it. Nobody has looked at the content yet.
Checked 18 Aug 2026 · No publish date given · Found through Media Copilot
```

"Nobody has looked at the content yet" and then three confident statements about what it
teaches, on the same screen. Pick one.

The bullets are also raw database rows: 116 of 116 "What it teaches" lines across my 41
start with a lowercase letter, 27 of them write **claude** in lowercase and 24 write
**ai** in lowercase. Site-wide that is 974 of 974 and 260 lowercase "claude". Another role
already reported this; I confirm it, and I note that a directory about writing quality is
failing to capitalise a proper noun 260 times.

---

## 6. Search, in my words

Three sentences I would actually type. First, the way the site sends me there — from the
home page's own **"Or describe what you want to do…"** field, then Show me. Done live:

```
home → typed "will clients know I used AI" → Show me
lands on  browse.html?q=will+clients+know+I+used+AI
page says: 0 resources
           No match for “will clients know I used AI”.
           Try fewer words, or browse by role instead.
```

Screenshot-confirmed. Second sentence, same result:

```
browse.html?q=make%20my%20copy%20not%20sound%20like%20AI
document.title                    → "Browse 0 Claude resources — Learn Claude"
window.LC_SEARCH_INDEX            → undefined
window.LCSearch.ready()           → false
```

Zero. Then I clicked into the box and pressed the **space bar**. One keystroke, same
query:

```
document.title                    → "Browse 4 Claude resources — Learn Claude"
window.LCSearch.ready()           → true
first three results               → "How to Stop Claude Writing Like an AI"
                                    "Create on-brand content (use case)"
                                    "Claude Code for Data Analysis"
```

Nought to four, and the correct answer first, because I hit the spacebar. The index is
only requested inside the `input` handler (`assets/js/browse.js:263-266`); the boot
sequence at the end of that file is `readURL(); render();` and never asks for it. The
only thing on the entire site that produces a `?q=` URL is the home page search field.
So the site's own alternative front door is wired to a dead end. Other roles have hit
this too — it is not mine alone — but it is the difference between me leaving in minute
four and staying.

With the index loaded, ranked results for my three sentences:

```
$ python scripts/test-search.py "make my copy not sound like AI"
     59.4  [writer-marketer      ] How to Stop Claude Writing Like an AI
     35.2  [writer-marketer,business-founder] Create on-brand content (use case)
     23.6  [data-analyst         ] Claude Code for Data Analysis

$ python scripts/test-search.py "will clients know I used AI"
     17.9  [student              ] Documenting Your AI Use
     17.9  [writer-marketer      ] Wikipedia:Signs of AI writing
     16.3  [non-technical,teacher] AI Fluency: Framework & Foundations

$ python scripts/test-search.py "write blog posts that rank"
     23.1  [writer-marketer      ] How I Use Claude Cowork to Write With AI in My Voice
      8.6  [developer            ] Claude Code: Software Engineering with Generative AI Age
      8.6  [student              ] AI for Students
```

Query one is good. Genuinely good — that is the right answer.

Query two proves section 3's point in one line: the best answer the site has to *"will
clients know I used AI"* is a resource tagged for **students**, and the second is a
15,000-word Wikipedia page for encyclopedia editors.

Query three is where a marketer finds out this site is not for them. "Write blog posts
that rank" returns a **builder**-level Cowork config walkthrough whose own skip line says
*"You're not comfortable with folder structures and markdown config files"* — followed by
a software-engineering course and a resource called "AI for Students". Nothing about
ranking. Nothing about search. Because there is nothing.

---

## 7. On a phone

Rendered `browse.html?role=writer-marketer&level=basic` in a 375px frame on the live
site, so the `@media (max-width: 768px)` block in `assets/css/site.css:590` is really
applied. Measured, not guessed:

```
innerWidth                    372
mediaMatches768               true
.filter-rail display          none
.mobile-filter-bar display    block, 69px, button 44px
horizontal overflow           false      (scrollWidth 357 ≤ 372)
footer link heights           44, 44, 44
count / cards                 "28 resources" / 28
first card top                538px   → 67% of the first screen before any result
first card visible on screen  202px of 646px
first card height             646px
page height                   15,972px = 19.7 phone screens
filter options visible        0
```

The bones are right. No sideways scroll, 44px touch targets, the filter bar sits under a
thumb. Somebody did that work.

But: **two-thirds of my first phone screen is chrome.** Wordmark, nav, "Browse", a search
box, a Sort dropdown, two filter chips, a count — and then 202 pixels of one card. And 28
cards at 646px each is **nearly twenty screens of thumb-scrolling** for one level of one
role. I am not reading twenty screens. I am reading two and closing the tab.

The card is that tall because it carries a full `For:` paragraph and a full `Skip if:`
paragraph. On desktop that density is the product. On a phone it is a wall, and there is
no compact mode, no collapse, no sort-by-shortest by default.

---

## 8. Content quality — the three worst entries I was shown, quoted

**Worst 1 — "Next-Generation AI Assistant: Claude by Anthropic".** Card 2 of the only
three I get at never-used. Live text:

> Coursera · course · half-day · free-account · checked 2026-08-21 · published UNVERIFIED
> **For:** A marketer or small-business owner who has used ChatGPT casually and wants a
> single guided exercise that ends with real campaign copy.
> **Skip if:** Skip it if the title made you think Anthropic built it - it is a Coursera
> and Starweaver production, one module long, rated only 4.1 from 33 reviews, and it
> never leaves basic marketing prompts.

Read those two lines together. The **For:** line is the only card in my whole 41 that
promises a marketer real campaign copy. The **Skip if:** line then says it is
mislabelled, one module long, rated 4.1 from 33 reviews, and never gets past basics. The
site is warning me off the one thing it offered me. It is one third of everything a
beginner writer is shown. Why is it on the shelf at all? Keeping it is not honesty, it is
padding with a disclaimer attached.

**Worst 2 — "The Ethics of Using AI".** Ethicscentral, article, basic.

> **Skip if:** You need current, specific rules — this predates SPJ's 2026 Code of Ethics
> revision (see next entry).

```
published 2023-02-01 → 1303 days old at 2026-08-27
```

Three and a half years old. Its own skip line says it is superseded by the very next card
on the shelf. So the site placed a card it knows is out of date directly above its
replacement, and told me to skip it. That is not curation, that is a filing cabinet with
commentary. Also: *"(see next entry)"* is written as if this were a printed page. On
Browse, "next entry" depends on my sort order and my filters. Sort by Newest and the
sentence points at nothing.

**Worst 3 — "AP Sets New AI Standards for Newsroom Use".** Media Copilot, article, basic,
the one **Found only** card in my 41.

> **Found only.** We found it and sorted it. Nobody has looked at the content yet.
> **For:** Anyone tracking how AP's position has shifted since its original 2023 guidelines.
> **Skip if:** You need AP's full stylebook chapter on AI rather than a news summary of
> the update.
> Checked 18 Aug 2026 · **No publish date given**

Nobody read it. No date. And it is a third-party news summary of somebody else's policy
update — a summary of a summary. Then the page asserts three things it teaches. Every
statement on that page beyond the URL is unearned.

**Dishonourable mention — the skip lines that skip nothing.** Five of my 41 say only
"you already did this":

> *"You already run a Project with knowledge and instructions configured."* (69 characters)
> *"You've already got Projects and Styles configured — this is a conceptual explainer, not new tactics."*
> *"You already run Claude through Projects with saved context and glossaries — you're doing what this post recommends."*

That is not a judgment. That is the **For:** line with a "not" in front of it. The site's
own home page says *"A link with no judgment is just a list."* Correct. Here are five.

---

## 9. Everything that is broken, ranked

**9.1 — The site's own search box returns zero for every sentence I typed.**
Live, from the home page field, Show me: `browse.html?q=will+clients+know+I+used+AI` →
`0 resources` / *"No match for "will clients know I used AI"."* Same for
`?q=make my copy not sound like AI`. On the page: `window.LC_SEARCH_INDEX → undefined`,
`window.LCSearch.ready() → false`. One space bar keystroke turned the identical query
into `Browse 4 Claude resources` with the right answer first. Cause:
`assets/js/browse.js:263-266` is the only `LCSearch.load()` call in the codebase and it
sits inside the `input` handler; boot is `readURL(); render();`. The only producer of a
`?q=` URL is the home page field. Also seen by other roles — I confirm it end to end for
mine.

**9.2 — The role is called `writer-marketer` and there is nothing for a marketer.**
Over all 353 items: `seo` 2 hits (0 mine), `content marketing` 0, `email marketing` 0,
`press release` 0, `search engine` 0. `python scripts/test-search.py "seo"` → 1 result
site-wide, tagged `pm,non-technical`. The one entry naming copywriting, landing pages and
social media — "Claude AI Comprehensive Guide" — is the single `subscription` item on a
shelf that is otherwise 36-of-41 free, and its own skip line pushes me off it.

**9.3 — The chip says "a writer" and the shelf is written for a newsroom.**
11 of 41 `who_for` lines name journalists / newsrooms / editors / outlets; 5 name
marketers or campaigns (word-boundary grep shown in section 3). All six of my `safety`
resources are institutional newsroom AI policies. There is no card addressed to a
freelancer, an agency, or a contractor. Half the people that chip catches will not find
themselves anywhere on the page.

**9.4 — Four resources on disclosing AI use exist, and none is tagged for me.**
"Disclosing the Use of AI" (`student,researcher`), "Documenting Your AI Use" (`student`),
"Referencing AI and Acknowledging AI Use" (`student`), "Guidance on AI detection, and why
we're disabling Turnitin's AI detector" (`teacher`). Zero `writer-marketer`. The one
profession where non-disclosure is a contract breach was given six newsroom codes of
conduct instead.

**9.5 — 20 of my 41 are borrowed filler, and the check date proves it.**
Grouped by `checked`: 2026-08-18 → 21 cards, **all 21** of my only-this-role resources,
articles/docs/repos. 2026-08-22 → 15 cards, **13 of them YouTube video**, **zero**
only-this-role. Two more days add 5. So 21 cards were chosen for a writer and 20 were
swept in from other shelves to make 41 look like a number. 18 of 41 `who_for` lines never
name writing, editing, marketing or journalism at all.

**9.6 — Two people wrote the `Skip if:` lines and you can tell them apart by the dash.**
My 41, by check date: the 18 Aug batch (21 cards) — 0 start with "Skip if", 18 use an em
dash, 0 use a spaced hyphen. The 22 Aug batch (15 cards) — 15 start with "Skip if", 2 use
an em dash, 6 use a spaced hyphen. Site-wide: 161 start "Skip if…", 180 start "You…",
12 other; 77 em dash, 84 spaced hyphen. A directory that sells judgment about prose
cannot hold one punctuation rule across 353 entries.

**9.7 — 18 of 41 cards print "Skip if: Skip if …".**
`ui.js:185` renders a literal `<span class="label">Skip if:</span>` and then the stored
sentence restarts the phrase. Measured live on my basic shelf: 13 of 28 cards. The worst
reads *"Skip if: Skip if you already build your own tooling — … Skip too if you want
prompt craft…"* — three "skip"s in one sentence. Reported before for another role;
confirmed here, and 9.6 explains which half of the catalogue does it.

**9.8 — 1 of 17 path steps carries my tag, and Paths never says so.**
`paths.html` lists all three routes under *"A short list, in order. Start at the top."*
with no role filter. In "Your first week with Claude", 5 of 6 steps are resources this
same catalogue tagged for other roles. `paths.json` carries a `roles` field for every
path; `assets/js/paths.js` never reads it. `paths.html?role=writer-marketer` silently
drops the parameter.

**9.9 — Nine of my publishers are machine-cased domain slugs, and one is a TLD.**
`"Open on Cloud"` for `ranthebuilder.cloud` — the site printed a top-level domain as a
publisher name. Also "Open on Journalism" (journalism.co.uk), "Open on Willfrancis",
"Open on Theopennotebook", "Open on Beutlerink", "Open on Ethicscentral", "Open on
Niemanlab", "Open on Localizelikeapro", "Open on Ccforeveryone". "Open on Substack"
discards the publication name entirely.

**9.10 — `LC.authorLine` fails on exactly the case it was written for.**
It suppresses a repeated name with `al.indexOf(sl) !== -1 || sl.indexOf(al) !== -1`, which
a single space defeats. Live on `resource.html?id=r-da0e8aedbc`:
`Willfrancis · Will Francis`, and the same page prints "Willfrancis" twice more in "Open
on" and "Found through". Second instance: `Theopennotebook · The Open Notebook`.

**9.11 — 28 of my 41 have a verdict written from an outline; 1 from nothing; 0 from a
human read.** Tiers for my role: `ai-reviewed 12, previewed 28, listed 1`, reviewed 0.
"Skimmed" means *"We read the outline or a free sample. We have not seen the whole
thing."* The `how-we-check` page opens with *"We would rather have 70 resources we can
vouch for than 700 we cannot."* There are 353 and nobody has vouched for one of them.
The zero-reviewed fact is known; what it means for me is that the site's entire pitch —
a person judged this prose — has never once been true on my shelf.

**9.12 — On a phone, 67% of the first screen is chrome and my level is 19.7 screens
long.** Measured at 372px on the live site: first card top 538px of an 809px viewport,
202px of a 646px card visible, page height 15,972px for 28 cards, 0 filter options
visible until you tap. No compact card, no default short-first sort.

**9.13 — "(see next entry)" is written for a printed page.**
"The Ethics of Using AI" says *"this predates SPJ's 2026 Code of Ethics revision (see next
entry)"*. Browse re-sorts on three orders and six filter axes. Change the sort and the
sentence points at whatever happens to land below it.

**9.14 — 13 of my 41 have no publish date and 3 are over a year old.**
`role-view.py writer-marketer --counts` → `no date: 13`. Over a year: "The Ethics of Using
AI" (2023-02-01, 1303 days), "AI prompt engineering: A deep dive" (2024-09-05, 721 days),
"Lesson 7: Effective prompting techniques" (2025-06-12, 441 days). The card shows the
warning; `resource.js` computes `fresh.note` and then never prints it, so the warning
disappears on the page where I decide. Known for another role; confirmed for mine.

**9.15 — 116 of 116 "What it teaches" bullets on my shelf start lowercase.**
27 of them write "claude", 24 write "ai". Site-wide 974 of 974 and 260 lowercase
"claude". Known; I add the writer's note that this is a proper noun and it is wrong 260
times on a site about writing.

**9.16 — 2 of my 41 carry an unused `alt_skip_if`, one of which is the writer-specific
line the card should have shown.** Claude 101 ships four alternates, including *"You've
already completed onboarding or use Claude regularly — this is entry-level and not
writing-specific."* The card shows the generic one instead. `grep -rn alt_skip_if
assets/ scripts/ *.html` → no matches. Known as dead data; the new part is that the
better, role-aware line already exists and is discarded.

---

## 10. The one thing that would make me leave and not come back

I typed a real question into the site's own search box — *"will clients know I used AI"* —
pressed the site's own button, and got **"0 resources. No match."**

I would not have tried a second sentence. I would have concluded the catalogue is empty
and closed the tab, and I would have been wrong, because that exact query has eighteen
matches sitting in a file that the page refuses to fetch. The site is not thin. It just
told me it was, in its own voice, on its own front door.

Second place, and it is close: had I got past that, the shelf would have told me it was
built for a newsroom staffer. I am not one. There is no SEO, no campaign work, no email,
no landing pages, no press releases, and the single entry that names copywriting wants a
Coursera subscription. The chip says "a writer" and means "a journalist", and the missing
half of the word is in the role key where nobody can read it.

---

## 11. What is genuinely good (be honest, but brief)

- **The two-question front door.** Four clicks, a live count before I commit, and a
  sentence instead of a form. It is the best-written thing on the site.
- **`Skip if:` as an idea.** When it is done properly it is the only thing on the
  internet that saves me an hour. *"Skip it if the title made you think Anthropic built
  it - it is a Coursera and Starweaver production… rated only 4.1 from 33 reviews"* is
  worth the whole page.
- **The AI-tells cluster.** "How to Stop Claude Writing Like an AI", "Wikipedia:Signs of
  AI writing", "How to Spot AI Writing, According to Wikipedia" and `avoid-ai-writing`
  are four correct choices in a row, and search puts the right one first. Somebody who
  understood the anxiety picked those.
- **The tier ladder is honest.** "Found only. Nobody has looked at the content yet" is a
  humiliating thing to print about your own work, and printing it anyway is the most
  trustworthy sentence on the site.
- **Ranked search, once it loads, is good.** 59.4 for the right answer on my first
  sentence. The engine is not the problem; the trigger is.
- **The phone build.** No sideways scroll, 44px targets, a thumb-reachable filter bar.
  It seems like someone tested it on a real device.

---

## Checklist — every line ticked or the file is not finished
- [x] I opened the live site — home, browse, paths, three resource pages, plus
      `curl -s ".../browse.html?role=writer-marketer"` → HTTP 200
- [x] I tried all four levels — 3 / 28 / 7 / 3, read off the live tally line
- [x] I quoted at least 5 real titles or lines from the site — "Next-Generation AI
      Assistant: Claude by Anthropic", "The Ethics of Using AI", "AP Sets New AI Standards
      for Newsroom Use", "How to Stop Claude Writing Like an AI",
      "Claude AI Comprehensive Guide", "Claude Skills for Journalism, Media & Academia",
      plus verbatim `Skip if:` and `For:` lines throughout
- [x] Every number I used is in 00-facts.md or I show the command
- [x] I looked at a phone width — 372px, live, measured
- [x] I found at least one thing nobody has mentioned before — 9.2 (no SEO / marketing
      content anywhere in 353 for a role named `writer-marketer`), 9.3 (11 journalism
      `who_for` lines to 5 marketing), 9.4 (four disclosure resources exist and none is
      tagged for me), 9.5 (21 chosen cards + 20 borrowed, provable by check date), 9.6
      (two `Skip if:` voices separated by the em dash), 9.9 ("Open on Cloud" — a TLD
      printed as a publisher), 9.10 (`authorLine` defeated by one space), 9.13
      ("see next entry" on a re-sortable page)
