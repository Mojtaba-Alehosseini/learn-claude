# Attack 2: not a coder
Written as an office worker who is not a coder, 2026-09-05. Live site only:
`https://mojtaba-alehosseini.github.io/learn-claude/`. All URLs are re-checkable.

I want to use Claude for my job. I know the URL and nothing else.

---

## 1. First 60 seconds

I get a big sentence with two blanks — **"I'm a [role] and I've [level]."** — and under it
one question, **"Who are you?"**, with ten chips. The second question is not there. It only
appears after I click a role. So the headline promises two blanks and the page gives me one.
Not fatal, but the sentence lied to me for four seconds.

The line I actually read: **"635 resources, checked by hand."** That is the sales pitch, and
I believed it. Section 11 is where it falls apart.

The three promises underneath are good writing:

> "We say when to skip — Every entry has a `Skip if:` line. A link with no judgment is just a
> list, and lists are what made this hard in the first place."
> "We say how we checked — Four levels, and we do not round up. If nobody has opened it, the
> card says so."
> "We show the date — Claude changes every few months. You can see when we last looked, and
> whether the thing is old."

I spent the rest of the hour checking those three sentences. All three are broken in ways I
can point at.

A drawing on the right cycles by itself and faintly tints whichever role chip it is drawing.
Twice I thought a role was already selected for me.

---

## 2. The front door, all four levels

I picked **"not a coder"** and each level in turn.

| I said | Resources | Picks block |
|---|---|---|
| never used Claude | **68** | "Start with these three" |
| used it a little | **73** | "Start with these three" |
| used it a lot | **14** | "Start with these three" |
| built things with it | **8** | **"Start with these two"** |

Two things a normal person notices immediately.

**(a) "Never used Claude" returns fewer results than "used it a little" (68 vs 73).** The
absolute beginner — the person this site's front page is written for — is the second-worst
served level for their own role.

**(b) The cliff.** 73 -> 14 is a fall off a table. And the last cell, "not a coder / built
things with it", is eight cards. All eight are from **Anthropic Academy**. All eight say **"No
publish date given"**. All eight say **"Checked 29 Aug 2026"**. All eight are badged
**"Skimmed"**. Two of them are *"How to use the Prior Auth Review sample skill with Claude"*
(health-insurance claim review) and *"Using the Blackbaud connector in Claude"* (nonprofit
donor CRM). That is the ceiling of this site for someone like me.

I also checked the other roles the front page invites in. The floor is worse than mine:

- **a student + built things with it = 0 resources**
- **a teacher + built things with it = 2 resources**
- **a writer + built things with it = 3 resources**

Meanwhile *a developer / built things with it* = 64 and *running a business / built things
with it* = 79. The site is built for developers, PMs and founders and dressed up as a site for
everyone else.

---

## 3. What the catalogue gives me

`browse.html?role=non-technical&level=never-used` — 68 cards.

**21 of those 68 cards (31%) are for somebody else's job.** Not my inference — their own
"For:" lines say so. In my beginner list I was handed:

- *"Using the ICD-10 Connector in Claude"* — "For: Medical coders and billing specialists
  validating diagnosis and procedure codes."
- *"Using the CMS Coverage Connector in Claude"* — "Covers Medicare Part B only."
- *"Using the HealthEx Connector in Claude"* — "Claude Max only, US-based, plus government-ID
  biometric verification through CLEAR."
- *"Using the NPI Registry Connector in Claude"*, *"Using the Function Connector in Claude"*
- *"Using the Blender Connector in Claude"* — "For: Blender users who want Claude to work with
  their live open scene."
- *"See what your campaign goal actually requires"* — "Built specifically around
  capital-campaign gift-pyramid math (3-to-1 and 4-to-1 prospect ratios)."
- plus *"Work through grant options in chat"*, *"Using the Benevity connector"*, *"Using the
  Candid connector"*, *"See why donor retention beats acquisition"*, *"See budget futures side
  by side"*, *"Claude for nonprofits partnership guide"*
- and cards whose own For: line says **"A student, in any subject..."**, **"Classroom teachers
  starting from zero..."**, **"A designer who has never opened Claude..."**

I answered the question honestly and a third of the answer is Medicare coding, 3D modelling
and capital-campaign fundraising. **Who it harms:** exactly the reader this site claims to
rescue from "drowning in options" — the one who cannot yet tell which links are not for them.

The good news: when a card *is* for me, the writing is genuinely better than anything else in
this space. *"Upload files to Claude"* — "For: Anyone with a spreadsheet on their laptop and
no idea how to get Claude to look at it. The step every data guide assumes you have already
done." That is a real sentence written by someone paying attention.

---

## 4. Paths

`paths.html` — seven paths. Exactly one is for me: **"Your first week with Claude"** (also for
students, teachers, business owners). Everyone else's route is role-specific; the four biggest
non-developer audiences share one.

I followed it. **The step reasons are the best thing on this site.** They actually explain the
position:

> Step 4 — What are Projects? — "Once you repeat a task twice, you need somewhere to keep the
> context. Projects is that place. **Learning this earlier would have been abstract.**"
> Step 6 — "Last, because working on your own files only makes sense once you trust the
> answers."
> Header — "Steps 1, 2, 4, 5 and 6 take fifteen minutes each; step 3 is Anthropic's own
> 2.5-hour Claude 101, and stopping there still leaves you better off than most people."

That is real editing. Now the problems.

**(a) The path drops the `Skip if:` line.** The home page's first promise is "Every entry has
a `Skip if:` line." On `paths.html?id=first-week` there is no Skip if on any of the six steps.
Step 1 is *"Claude is not one tool. It's six."* by Ruben Hassid. Its Skip if — visible on
Browse, hidden here — reads: **"The author writes in a promotional, personal-brand newsletter
style with frequent subscribe prompts."** The one page that tells me to *do these six things
in order* is the one page that withholds the warnings. **Harms:** the most trusting reader,
the one who follows an ordered list.

**(b) Step 1 of the beginner path is not in the beginner list.** *"Claude is not one tool.
It's six."* is filed at level "used it a little". So a reader who answers "never used Claude"
on the home page gets 68 cards that **do not include step 1 of the only path written for
them.** Reproduce: `browse.html?role=non-technical&level=never-used`, search the page for that
title — absent; it appears only at `&level=basic`.

**(c) All six steps say "No publish date given."** The flagship path, on a site whose third
pillar is "We show the date", shows zero publication dates.

**(d) On the index, step titles are cut off:** "The new rules of context engineering for
Cla...", "Claude for Product Managers: Synthesizing Us...". And one path is costed **"about 81
minutes"** while the others say "about 4 hours" / "about 2 hours". Nobody says 81 minutes.

---

## 5. The card and the resource page

I opened three: `resource.html?id=r-434e205e76`, `?id=r-bcd03ac245`, `?id=r-4d17281029`.

**Would I click through to the real thing?** Yes — the pages are clean, the "Open on Anthropic
Academy" button is unmissable, and I sampled 45 outbound links across the whole catalogue: **45
of 45 returned HTTP 200.** No link rot found. Credit where due.

But three things on those pages are wrong.

**(a) The "What it teaches" bullets are visibly broken.** On `resource.html?id=r-4d17281029`
(*Claude Code overview and install guide*), four bullets in a row:

> — Install **Claude code** across **macos linux and windows** environments
> — Configure **Claude code** in **vs code** and JetBrains editors
> — Run initial **Claude code** commands for tests bug fixes and git workflows
> — Navigate to **Claude code** docs for **ci** scheduling and integrations

Three sentences above, the same page writes it correctly: "terminal on macOS, Linux, Windows
PowerShell and CMD... VS Code, JetBrains". The page proves it knows the right spelling and
prints the wrong one four times. There are no commas in any bullet on any resource page.
**Harms:** every reader's confidence — this is the first block on the page, and it reads like a
machine nobody proofread.

**(b) The time chip is a bucket pretending to be a duration.** On
`resource.html?id=r-bcd03ac245` the chips say **"hands-on · half a day · subscription"** while
the summary on the same screen says **"Guided 1.5-hour project"** and the Skip-if says
**"Ninety guided minutes"**. Worse, on Browse: *"AI capabilities and limitations"* carries the
chip **"half a day"** and its own Skip-if says **"at 15 minutes across 13 short lectures, this
is a primer"**. I then set the Time filter to "15 min"
(`browse.html?role=non-technical&level=never-used&time=under-15min`, 55 results) — **the
15-minute course is filtered out.** **Harms:** the reader with a lunch break, who skips the
thing that fits.

**(c) "Copy link" gives you a link nobody can read.** Every resource page ships as `<title>Resource
— Learn Claude</title>` with `og:title="Resource — Learn Claude"`. All 635 of them. Paste any of
them into Slack, Teams or LinkedIn and the preview card says "Resource — Learn Claude" with the
same generic description. The page has a **Copy link** button whose output is indistinguishable
for every entry in the catalogue. **Harms:** anyone who tries to recommend this site to a
colleague — the whole word-of-mouth loop.

---

## 6. The picks block

Header: **"Start with these three"**, label: **"picked by AI · 4 Sep 2026"**.

**Does it feel like real judgment?** Sometimes. This one is genuinely sharp:

> *Full Claude Tutorial: Beginner to Advanced in 19 Minutes* — "Five beginner tours in this
> pool, and this is the only one whose own notes rule out complete beginners — too fast to be a
> true first video — which is exactly what makes it the right speed for someone who has already
> poked at Claude."

That is an argument. But the very first pick a beginner sees is not. On
`browse.html?role=non-technical&level=never-used`, the card and the reason directly beneath it
read:

> **Skip if:** "The only page in this whole **harvest** with a genuinely zero-prerequisite start
> - just describe your role - so there's nothing to skip unless you already know Claude's
> capabilities well enough not to need a personalized map."
> **Reason:** "The only **candidate of 51** with a genuinely zero-prerequisite start - you
> describe your job and it maps the capabilities to you, where everything else orients you to
> the product in general."

Two sentences, stacked, both opening "The only ... with a genuinely zero-prerequisite start".
**The AI's reason is a paraphrase of the line printed two centimetres above it.** It tells me
nothing the card did not.

**"candidate of 51" against a page header that says "68 resources."** Two numbers on one screen,
neither explained. And **"harvest"**, **"pool"**, **"candidate"**, **"in this batch"** are the
site's private words for its own shortlist. I counted them: **66 of the 109 pick reasons use
"candidate", 45 use "pool".** I am not on the team. I do not know what the pool is.

Also note that first card's `Skip if:` **does not tell me when to skip.** It argues the
opposite. The site's headline promise, spent on praise.

**Does "picked by AI" make me trust it more or less?** Less, and specifically because of the
badges next to it. The card is badged "Skimmed" and the block says "picked by AI". So: an AI
picked three things, from notes written about material nobody read all of, and the front page
told me all 635 were "checked by hand." The label is honest, and its honesty is what damages
it.

**A cell with TWO:** `browse.html?role=non-technical&level=builder`. The header quietly becomes
**"Start with these two"**, dated **"picked by AI · 31 Aug 2026"** — five days older than the
other cells. No line saying why there are two. From eight candidates.

**A cell with NONE:** `browse.html?role=teacher&level=builder` — two resources, **and the block
simply is not there.** No heading, no sentence, no "we have no picks here yet". The page changes
shape and says nothing. Compare the 0-result state, which *does* speak. It feels like a gap in a
spreadsheet, not a decision.

---

## 7. Dates and tier badges

**Dates.** I counted the whole catalogue from the site's own data file:

- **489 of 635 (77%) have no publish date.** The card says "No publish date given."
- **445 of 635 (70%) have neither a publish date nor an updated date.** Those cards carry
  exactly one date: "Checked ...".
- Only **146 (23%)** carry a publication date — which means the site's own staleness warning can
  physically appear on less than a quarter of the catalogue.

Against the promise "**You can see when we last looked, and whether the thing is old**": I can
see when they looked. I cannot see whether it is old, on three cards in four.

**And when the warning does fire, it hides the date.** *"Lesson 1: Introduction to AI Fluency"*
prints **"Published over a year ago — may not match Claude today"** — no date. The data file has
the exact date (12 Jun 2025). Thirteen months and three years look identical to me. On the one
card where the date matters most, the site that promises to show the date shows a phrase
instead.

**"Updated May 2026"** and **"Updated Jun 2026"** with no day (3 cards). And 44 cards say "No
publish date given" *and* "Updated 31 Aug 2026" — updated but never published, which reads like
a page that was born already revised.

**Does it look maintained or abandoned?** Maintained, but in bursts, and the bursts are visible:
**276 resources all carry "Checked 29 Aug 2026" and 211 all carry "Checked 5 Sep 2026."** Two
hundred and seventy-six in one day. That is a machine's afternoon, not a hand's.

**Does "Checked 4 Sep 2026" reassure me?** Only until I read the badge next to it. "Checked"
turns out to mean "the link still opens and an AI skimmed the outline". It is the most prominent
date on every card and the least informative.

**Tier badges.** "Skimmed" (501 cards, 79%), "Read by AI" (98, 15%), "Found only" (36, 6%).

What do they tell me about the work? That **537 of 635 entries — 85% — were never read
through.** And the meanings are locked in a `title="..."` attribute on a plain `<span>`
(`tabIndex -1`). On a phone there is no hover. With a keyboard there is no focus. On
`browse.html?role=non-technical&level=never-used` there are **68 badges on the page and not one
of them can be opened** by a touch or keyboard user. The site's second pillar — "We say how we
checked" — is delivered by a mouse-only tooltip. **Harms:** every phone reader, which given
"Must work on mobile" is most of them.

---

## 8. Search, in my words

### Query 1 — `is claude free` -> 23 results
1. *Choose a Claude plan (Help Center)* — **right.**
2. *Claude, Claude Code, Claude Cowork, and Claude in MS Office* — Udemy, **"half a day · pay
   once."** A paid course as the second answer to "is it free".
3. *Practical ways to get started using Claude for educators* — A.J. Juliani, school teachers.
   Nothing about price.

**Verdict: 1 of 3.** *Plans & Pricing* from Anthropic — the obvious answer — sits at **position
5**, under a paid Udemy course and a teachers' article.

### Query 2 — `make claude remember my stuff` -> 33 results
1. *How Can I Create and Manage Projects?* — **right.**
2. *What does AI know about me?* — a privacy video about what happens to what I type. That is
   the *opposite* question, and for a worried office worker it is a scary wrong turn.
3. *Organize your legal workflows using Projects* — "Contract review teams doing high volume."

**Verdict: 1 of 3.** Worse: **"What are Projects?" is not in the 33 results at all.** I checked
the whole rendered list. That is the card whose own For: line reads *"Anyone who keeps
re-pasting the same background into new chats... and wants that context to stay put"*; it is
**Step 4 of the site's only beginner path**; and it is one of the site's **own AI picks** for
"not a coder / used it a little". **The site cannot find its own top pick when I describe it in
plain English.**

### Query 3 — `how do i stop claude making things up` -> 10 results
1. *Claude for Education Is Made for Learning* — University of Pittsburgh, whose Skip-if says
   "the Pitt login references will not apply to you."
2. *Reduce hallucinations* — **right**, at #2.
3. *Hooks in Claude Code — Full Theory + Practical Use | CampusX* — a **developer** video about
   programming hooks, matched on "stop an agent from doing certain things."

**Verdict: 1 of 3**, and #3 is unusable for me. This is the single most important safety question
a new user asks, and two of three answers are wrong.

### Query 4 — `write emails for me` -> 10 results
1. *Real-World AI for Everyone (Specialization)* — Coursera, **"several days · subscription."** A
   multi-week paid course, first, for "write emails".
2. *Claude AI for Teachers: Complete Beginner's Guide...* — teachers.
3. *Clean up promotional emails* — about **deleting** promotional mail, not writing anything.

**Verdict: 0 of 3.** And **"Write in my voice" is not among the 10** — the catalogue entry for
drafting internal communication in your own voice, which the site's own AI ranked **#1 for "not a
coder / built things with it"**.

### Query 5 — `use claude on my excel file` -> 53 results
1. *Upload files to Claude (Help Center)* — **right.**
2. *Claude 101 (DataCamp)* — a generic half-day beginner course. Its For: and Skip-if never
   mention Excel or files.
3. *Master Claude for Excel in 10 Minutes: Financial Modeling* — relevant, but "Skip if you do
   not use Excel or have no paid Claude plan."

**Verdict: 2 of 3.** Anthropic's own *"Use Claude for Excel"* is at **#4**, behind the DataCamp
course.

### The pattern
Across five queries the same broad beginner courses float up regardless of what I asked —
*Claude 101 (DataCamp)*, *Real-World AI for Everyone*, the teachers' guides. Search is matching
topic-shaped nouns and ignoring intent. **Who it harms:** the person who types instead of
clicking chips — i.e. anyone in a hurry, which is the state the front page says it is rescuing me
from.

---

## 9. On a phone

Emulated 375 x 812.

**Good:** no horizontal scroll anywhere I looked (home, browse, paths, path detail, resource).
`document.scrollWidth` = 375 on every page. Tap targets are comfortable. Type is big enough. The
layout genuinely works.

**Bad:** there is no pagination and nothing loads lazily.

- `browse.html?role=non-technical&level=never-used` on a phone: **39,745 px tall — 49 phone
  screens**, 68 cards, all in the DOM at once.
- `browse.html` with no filters: **346,237 px — 426 phone screens**, all 635 cards.

There is no "load more", no page 2, and no back-to-top. Combine that with section 12 finding 4
and you get the worst moment of the visit: tap a card, tap "Back to browse", and you are at the
top of a 426-screen page with your role and level gone.

Also on mobile the **"Skimmed" / "Read by AI" badge is a dead word** — no hover, no explanation,
on every card.

The fixed bottom "Filters" bar covers the bottom 69 px of content permanently.

---

## 10. Keyboard walk

I could not drive real Tab keystrokes through my harness, so I am reporting only what I could
verify directly in the live DOM and stylesheet.

**What is right — and this is better than most sites:**
- A real skip link: `<a class="skip-link" href="#main">Skip to content</a>`, revealed on focus.
- Every filter is a proper `<button type="button" role="checkbox" aria-checked="true|false">` —
  operable by keyboard, and announced correctly.
- A global `:focus-visible` outline, plus a card-level ring (`.card:has(.card-title
  a:focus-visible)`) so the whole card lights up rather than just the link, plus a
  `forced-colors` block that pins the ring to `CanvasText` and selection to `Highlight`.
- The result count is `aria-live="polite" role="status"`.
- The mobile filter sheet computes to `display: none` at desktop, so its **duplicate copy of
  every filter is correctly out of the tab order.** I checked for that trap and it is not there.
- The collapsed "More filters" group is also `display: none` — correctly untabbable.

**What is wrong:**
1. **The skip link does not skip anything useful.** `browse.html` is `<main id="main">` ->
   `<aside class="filter-rail">` -> `<section aria-label="Results">`. "Skip to content" lands you
   *before* the filters. From there it is roughly 25 more Tab presses before the first resource
   link. There is no "skip to results" link. Verified by DOM order: on
   `browse.html?role=non-technical&level=never-used` the first `resource.html` link is the 50th
   focusable node in the document.
2. **The tier badge is unreachable.** `<span class="badge badge-previewed" title="We read the
   outline or a free sample. We have not seen the whole thing.">Skimmed</span>` — `tabIndex` is
   -1 and `title` tooltips do not open on keyboard focus in any browser. The site's second pillar
   is keyboard-invisible.
3. **The empty state has no focusable escape** — see section 12 finding 11.

---

## 11. How we check

Read it twice. It made me trust the site **more in the small and much less in the large**, and
the large wins.

**More.** This is unusually honest for a directory:

> "Right now: 635 resources — 98 read by ai, 501 skimmed, 36 found only. **Nothing is read in
> full yet, and the cards say so.**"
> "It needs a GitHub account, which is a real barrier and we know it."
> "We do not take money to rank a resource. We are not affiliated with Anthropic."

I independently counted the data file: 98 / 501 / 36, and 390 official. **Every number on that
page is correct.** That is rarer than it should be.

**Less — and this is the finding.** Put the home page next to this page:

- Home: **"635 resources, checked by hand."**
- Here: **"Nothing is read in full yet"**, where "Read in full" is defined as **"We went through
  all of it and a person checked the notes."**
- Here: 36 items are **"Found only. We found it and sorted it. Nobody has looked at the content
  yet."**

Those cannot both be true. **Zero resources have had a person check the notes**, and the sentence
on the front page — the one on the first screen, where most people stop — says all 635 were
checked by hand. The correction is on a page nobody opens.

And the page opens by arguing against itself: **"We would rather have 70 resources we can vouch
for than 700 we cannot."** It then reports 635, of which it can vouch for none by its own
top-tier definition. It also says "We find material, **read it**, and write two things" — while
537 of 635 were not read through.

**Does 61% Anthropic read as candour or confession?** Candour, and it is the best paragraph on
the site:

> "390 of those 635 (61%) are Anthropic's own — official just means who published it, not how
> good it is, so the rest are here because they passed the same check, not a lower one."

That is exactly the right way to say it. It does not read as a confession, because the site also
gives me a **"Source: Official Anthropic only"** filter so I can see the split myself. But it
undercuts itself in practice: "not a coder / built things with it" is **8 of 8 Anthropic
Academy**, and "not a coder / never used Claude" is thick with Anthropic connector pages for jobs
I do not have. The essay says official is not a shortcut; the shelves say otherwise.

Small thing that tells you nobody proofread: the badge everywhere on the site is **"Read by
AI"**; on this page it is **"98 read by ai"**.

And nowhere — not here, not on any card — does the site say **which** AI read, skimmed or picked.
"Read by AI" and "picked by AI" ask me to trust an unnamed thing.

---

## 12. Everything broken, ranked

**1. "Found only" pages state that nobody looked, and then describe what is inside.**
`resource.html?id=r-bcd03ac245`. The page says: **"Found only. We found it and sorted it. Nobody
has looked at the content yet."** The same page says: **"Skip it if — Nothing in it visibly tells
you to check Claude's arithmetic, which for a project built on sales numbers is the omission that
matters. Ninety guided minutes, and you need Claude Pro on top of the Coursera side."** Plus "What
it teaches" bullets and "Before this" prerequisites.
You cannot know a page omits an arithmetic warning, or runs ninety minutes, without looking at it.
**All 36 "Found only" items have a written Skip-if, a Who-it's-for and What-it-teaches bullets.**
Another: *Hooks reference (Claude Code)* — "This is a lookup reference, not a tutorial, **and it
is enormous.**"
*Expected:* a tier that says nobody looked should carry no content judgment.
**Harms:** every reader, at the exact point they are deciding whether to trust this site's
verdicts. Either the badge is wrong or the verdict is invented, and I cannot tell which.

**2. The front page claims "checked by hand" for a catalogue with zero hand-checked entries.**
`index.html` prints **"635 resources, checked by hand."** `how-we-check.html` prints **"Nothing is
read in full yet"** and "Read in full — We went through all of it and a person checked the notes."
Badges say "Read by AI"; picks say "picked by AI".
**Harms:** everyone. It is the sentence that decides whether I stay, and it is the one sentence
the site cannot support.

**3. Search cannot find the site's own best answers when I use my own words.**
`browse.html?q=make%20claude%20remember%20my%20stuff` -> 33 results, and **"What are Projects?" is
not one of them** — the site's own AI pick for that exact need and step 4 of its only beginner
path.
`browse.html?q=write%20emails%20for%20me` -> 10 results, and **"Write in my voice" is not one of
them** — the site's own #1 AI pick for my role at the top level. Top result instead: a several-day
Coursera subscription.
**Harms:** the reader in a hurry, who types rather than clicks. They get three wrong answers and
conclude the catalogue is thin.

**4. "Back to browse" throws away my role and level.**
On every resource page the link is `href="browse.html"` — no query string. Filters live only in
the URL (`history.replaceState`; there is no `localStorage` or `sessionStorage` anywhere in the
site's JavaScript). So: filter to 68 -> open a card -> click Back -> land on **635 resources**,
unfiltered, at the top of a page that is 426 phone screens long.
**Harms:** everyone who uses the site the way it is designed. It breaks the core loop, and on a
phone it is punishing.

**5. Nearly a third of my beginner results are for someone else's job.**
`browse.html?role=non-technical&level=never-used` — **21 of 68 cards** name a different reader in
their own "For:" line: 8 nonprofit fundraising/grants, 5 US healthcare coding (ICD-10, Medicare
Part B, NPI registry, CLEAR biometric ID), 3 designers, 3 teachers, 2 students, 1 Blender.
**Harms:** the reader who cannot yet tell which links are not for them — the exact reason this
site says it exists.

**6. Time chips are buckets shown as durations, and they break the Time filter.**
*"AI capabilities and limitations"* — chip **"half a day"**, its own Skip-if on the same card:
**"at 15 minutes across 13 short lectures, this is a primer."** Set Time to "15 min"
(`&time=under-15min`, 55 results) and **the 15-minute course disappears.** Also: chip "half a day"
on a **"Guided 1.5-hour project"**; chip "15 min" on *"A discussion guide for the AI Fluency
Index"*, which its Skip-if says **"needs 45-60 minutes of group time."**
**Harms:** anyone budgeting time — the single thing this site's tagline ("Find what's worth your
time") promises to protect.

**7. 77% of the catalogue has no publish date, so the staleness warning cannot fire.**
489 of 635 have no publish date; 445 have neither publish nor updated. The flag can only reach the
23% that have a date — and when it fires it **replaces** the date.
**Harms:** anyone learning a tool the site itself says "changes every few months".

**8. The AI pick reason repeats the Skip-if and cites numbers the reader cannot see.**
First pick at `?role=non-technical&level=never-used`: Skip-if opens "The only page in this whole
**harvest** with a genuinely zero-prerequisite start"; the reason under it opens "The only
**candidate of 51** with a genuinely zero-prerequisite start". Page header says "68 resources".
**66 of 109 pick reasons say "candidate", 45 say "pool"**, and 2 cards use "harvest" in
reader-facing copy.
**Harms:** the reader deciding whether "picked by AI" means anything. Here it visibly does not.

**9. The picks block silently drops to two, or vanishes.**
`?role=non-technical&level=builder` -> **"Start with these two"**, dated 31 Aug while neighbouring
cells say 4-5 Sep. `?role=teacher&level=builder` -> 2 cards, **no picks block at all**, no
sentence explaining its absence.
**Harms:** trust. A block that appears and disappears without comment reads as a gap in a
spreadsheet.

**10. The badge that carries the site's honesty is a mouse-only tooltip.**
`<span class="badge" title="...">Skimmed</span>`, `tabIndex -1`. 68 unopenable badges on one
browse page.
**Harms:** every mobile and keyboard reader — on a site whose own rules say it must work on
mobile.

**11. The 0-results dead end has no clickable way out.**
`browse.html?role=student&level=builder` -> **"We have nothing for this combination yet. It's on
the list. Loosen the level, or browse everything."** Neither "Loosen the level" nor "browse
everything" is a link or a button; the container holds no `<a>` and no `<button>`. Meanwhile
`resource.html?id=<nonsense>` renders **"It may have been removed. Browse everything instead."**
with "Browse everything" as a working link. The site knows how to write the escape; it just did
not put one where the dead end actually is.
**Harms:** every student who has built things with Claude — a whole cell of the grid, sent to a
wall.

**12. All 635 resource pages share one title and one social preview.**
Served HTML for every `resource.html?id=...`: `<title>Resource — Learn Claude</title>`,
`og:title="Resource — Learn Claude"`. Content is injected into an empty `<div id="content">`.
**Harms:** anyone recommending the site; and anyone with 30 tabs open, who now has 30 tabs called
"Resource".

**13. The Paths pages drop the `Skip if:` line.** See section 4(a).

**14. Step 1 of the only beginner path is missing from the beginner list.** See section 4(b).

**15. One card answers the site's headline promise with a non-answer.**
*Use Claude Cowork safely* — **"Skip if: Nothing — worth reading before your first real Cowork
task regardless of experience level."**

**16. Broken capitalisation and missing punctuation in "What it teaches".** See section 5(a).
Across the catalogue: "macos linux and windows", "vs code", "quickbooks paypal and hubspot",
"tableau cloud or tableau server", "docx pdf pptx and xlsx".

**17. The sitemap covers 353 of 635 resource pages, and every entry claims `lastmod
2026-08-23`** — while 211 resources were checked on 5 Sep 2026. 282 resource pages are not listed
at all.

**18. No pagination anywhere.** 39,745 px for a filtered phone page; 346,237 px unfiltered.

---

## 13. The one thing that would make me leave

**"Found only. Nobody has looked at the content yet"** printed on the same page as **"Nothing in
it visibly tells you to check Claude's arithmetic... Ninety guided minutes."**

Everything else on this list is a bug I would forgive. This is not a bug. It is the site telling
me, in the same breath, that it has not looked and that it knows what is inside. The whole product
is one thing — somebody's judgment, honestly labelled. The labels are the product. If the label
and the judgment contradict each other on one page, I have no way to know which of the other 634
pages have the same problem, and no reason to spend my afternoon finding out.

The second-worst is quieter and would lose me sooner in practice: I would type "write emails for
me", get a several-day paid Coursera specialization, a teachers' guide, and a page about deleting
junk mail — and close the tab believing there was nothing here. There was. The site had already
picked it. It just could not find it.

---

## 14. What is genuinely good

- **The `Skip if:` idea is the best thing in this category, and when it lands it is excellent.**
  "Two ceilings here are different and easy to trip over: a chat takes 500MB per file, a Project
  takes 30MB." — "It states the limit and offers no way round it: web search, which is the actual
  answer, is never mentioned." — "The title is wrong for what this is. It promises somewhere to
  access Claude and delivers geography." Nobody else writes this.
- **The path step reasons explain position, not just content.** "Learning this earlier would have
  been abstract" is a sentence a good teacher writes.
- **`how-we-check.html` is more honest than it needed to be**, and every number on it checks out
  against the data.
- **Link hygiene.** 45 of 45 sampled outbound links returned 200; all 16 links a beginner meets
  first (the four picks cells plus the six path steps) resolve.
- **Accessibility fundamentals are above average**: skip link, `role="checkbox"` + `aria-checked`
  on filters, `aria-live` count, `:focus-visible` rings including a whole-card ring, a
  `forced-colors` block, and the mobile filter sheet correctly kept out of the desktop tab order.
- **No horizontal overflow at 375 px on any page I opened.**
- **The "Official Anthropic only" filter** — building the escape hatch for your own biggest bias
  is the right instinct.
- **No tracking, no account, no email wall.** "We do not track your progress. Nothing here needs
  an account." I noticed, and it is why I stayed the hour.

---

## Checklist
- [x] I opened the live site at all four levels of my role — 68 / 73 / 14 / 8
- [x] I quoted at least 5 real titles or lines from the site — 35+
- [x] Every number I used is computed from the shipped data or measured in the live DOM
- [x] I looked at a phone width — 375x812, page heights measured
- [x] I did one keyboard walk — DOM-order verified; harness could not drive real Tab, and I said so
- [x] Five search queries in my own words, each with its verdict
- [x] I read the picks block and judged it — the first pick's reason paraphrases the Skip-if above it
- [x] I found at least one thing nobody has mentioned before — all 635 resource pages share one
      `<title>` and one social preview, next to a "Copy link" button; and the 0-result dead end has
      no clickable escape while the 404 page does
