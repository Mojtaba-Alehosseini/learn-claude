# Attack 3: a teacher
Written as a teacher, 2026-09-06. Site version: 9deb0db.

Secondary school, full timetable, no free periods. I want lesson materials, help with
marking, and a policy line I can put in front of a head of department. I will not put
pupil work anywhere I cannot account for. No budget.

## 1. The first 60 seconds

I load `https://mojtaba-alehosseini.github.io/learn-claude/`. The biggest text on the page
says, word for word:

> I'm a [role] and I've [level].

Square brackets and all. I sat and watched it for 16 seconds on a fresh load without
touching anything. It never changed. It reads like a template that failed. The drawing
beside it *does* move — I recorded the image swapping through
`roles/non-technical/never-used.png` → `student` → `researcher` → `teacher` → `developer`
→ `data-analyst` — so something on the page is alive, and the one thing a visitor reads
first is the thing that is not.

The rest of the first minute is good. "588 resources, each with a reason to skip it and
the date we last looked" is a real promise, and "We say when to skip" tells me what the
site is for in one line. I picked "a teacher". The sentence completed to "I'm a teacher
and I've [level]." and a second question appeared. That works.

## 2. Does the front door work for me (all four levels, with what I was shown)

Two clicks, then "Show me". Counts are what the home page told me, then what Browse told
me. They agree.

| my answer | home page said | Browse said | what I got |
|---|---|---|---|
| a teacher + never used Claude | "28 resources match so far." | 28 resources | "Start with these three", then "Everything else for you (25)" |
| a teacher + used it a little | "29 resources match so far." | 29 resources | "Start with these three", then "Everything else for you (26)" |
| a teacher + used it a lot | "8 resources match so far." | 8 resources | "Start with these two", then "Everything else for you (6)" |
| a teacher + built things with it | "2 resources match so far." | 2 resources | no picks, an offer to widen, "Too few to pick from — these are all of them." |

**never used Claude (28).** The best cell on the site for me. The three picks are
"AI Fluency for pK-12 Educators", "Practical ways to get started using Claude for
educators" (A.J. Juliani) and "Claude AI for Teachers: Complete Beginner's Guide to
Getting Started (Projects, Prompts & More)". All three are school teaching, not
university. The reason under the first one is the sort of sentence I would write myself:
"the only candidate built around the constraints schools actually have - limited budget,
many people to answer to." If I were new, I would start here and be pleased.

**used it a little (29).** Picks are "Claude for K-12 Teachers: context steering,
Projects and Skills", "Claude for Teachers: your data and our terms", and "How Teachers
Can Create Interactive Classroom Activities with AI". The middle one is exactly my
question, and the reason says so: "The question every teacher is asked before any tool
question - is this safe for student data". Then its own Skip line says "Skip if you are
outside the US; none of this applies to you." Which is honest, and leaves me with
nothing.

**used it a lot (8).** This is where it stops being for me. Of the 8:
- "43 Claude Skills for college teachers" — For: "University lecturers". Its Skip line
  says "Skip if you teach at school level; the framing is semesters, syllabi and
  departments." It is a **pick**, ranked first, on a page I reached by saying I am a
  teacher.
- "Create custom course materials" — For: "University math instructors".
- "Plan your syllabus" — For: "University instructors deciding whether they can reorder a
  course's syllabus."
- "Getting good at Claude: A research-backed curriculum" — For: "Someone responsible for
  helping a team build fluency".
Four of the eight are not my job. The other four are.

**built things with it (2).** Two cards. One is "Agent Skills for K-12 Teachers (open
source)", which is genuinely mine. The other is "Build interactive diagram tools",
For: "Someone building a reference app from an existing structured data/SVG source."
That is a developer. At the top level of the teacher ladder, half of what exists is not
about teaching.

So: the front door works mechanically at all four levels and the arithmetic is right at
all four. It stops being *about a teacher* somewhere between level 2 and level 3.

## 3. What the catalogue actually gives me (are these really for me?)

Unfiltered, "a teacher" is 67 resources. The good half is real and specific: "The
Ultimate Claude Guide for Teachers" (Paul Matthews) is For "School teachers, especially
heads of department, who already use ChatGPT and want to know whether Claude is worth the
move" — that is a person I could name in my staffroom. "AI Fluency for pK-12 Train the
Trainer" is For "School AI leads, instructional coaches and heads of department who must
deliver INSET" — again, a real job.

Two things are missing that I came for.

**Marking.** I searched the whole catalogue for `marking`: **4 results**, top two "Claude
AI Comprehensive Guide" and "PRD from a problem statement". I searched `grading`: **4
results**, top two "Teaching AI Fluency (Anthropic Academy)" and "Demystifying evals for
AI agents". A machine-learning evaluation document is not marking. Filtered to teacher +
"used it a little", `marking essays` returns **2 resources**, and neither is about
marking. Marking is the largest single thing on my desk and the site has close to nothing
on it.

**A policy line for a non-US school.** The one card written for the question — "Claude for
Teachers: your data and our terms" — ends "Skip if you are outside the US; none of this
applies to you." What is left is national framework documents (UK DfE, Australian
framework, EU ethical guidelines) which are about AI in general, not about this tool.

The site is also honest that it is mostly Anthropic's own material: STATUS.md says 343 of
588 (58%). In the teacher space that shows. Anthropic Academy supplies four of the eight
cards at "used it a lot".

## 4. Paths

Seven paths. I read all seven. Exactly one names me:

> **Your first week with Claude** — Anyone who has just opened Claude and does not know
> what to do next. For not a coder, a student, a teacher, running a business.
> 6 steps · about 4 hours · free

I followed it. It is a well-made path — the reason on step 5 ("Before you trust Claude
with anything that matters, understand exactly how it fails. This is the step people skip
and later regret.") is better writing than most paid courses manage. But its six steps
are "Claude is not one tool. It's six.", "Get started with Claude", "Claude 101", "What
are Projects?", "Why do AI models hallucinate?", "Get started with Claude Cowork". **Not
one step is about teaching.** It is a general product tour that four roles share.

Now compare. A developer gets "Getting good at Claude Code" — for people "getting
mediocre results", i.e. above beginner. A writer gets "Using Claude on work you put your
name to". A product manager gets "Product work without waiting for engineering". A
designer — the thinnest role on the site — gets "Judging AI's design output". Every one of
those is about that person's job.

**A teacher gets the beginner tour and nothing else.** There is no route for a teacher at
my level, and no route about teaching at any level. The page does not say what level each
path is for, and there is no way to filter it to my role, so I had to read all seven
descriptions to find that out.

## 5. The card and the resource page

I opened three.

**"Claude for Teachers: your data and our terms"** (`resource.html?id=r-5aa9ca06c5`).
The best page on the site. The summary tells me the substance before I click: "no model
training on your conversations, you are the data controller and Anthropic the processor,
encryption and deletion details, and which Team features are switched off for educators."
"What it teaches" lists "Verify safety compliance for school deployment". Tier "Read by
AI", "Checked 5 Sep 2026 · No publish date given · Updated 28 Aug 2026". **I would click
through to this one immediately** — and I did want to, until the Skip line told me it is
US-only.

**"Claude, Claude Code, Claude Cowork, and Claude in MS Office"** (Udemy,
`resource.html?id=r-cbd7194dc6`). The only paid thing a teacher is shown. Chips read
`course` / `half a day` / `pay once`. **There is no price anywhere** — not on the card, not
on the resource page. I have no budget and no idea whether "pay once" means £12 or £120,
so I will not click "Open on Udemy". Elsewhere in the catalogue prices *do* appear — I
found "from $49", "from $995" and "from $2,999" on other cards — so the site knows how to
show one. Mine has none.

**"Anthropic launched Claude for Teachers. We blocked it for our district."**
(Dr. Joe Phillips, `resource.html?id=r-76de44b7a7`). Tier "Found only". The whole page:

> Skip it if — You want something we have read. We have not opened this one yet.
> How we checked this one — Found only. We found it and sorted it. Nobody has looked at
> the content yet.

It reads honest, not broken; the sentence is plain and admits the gap. But two things bite.
First, the same page also says **"Checked 21 Aug 2026"** two lines below "Nobody has
looked at the content yet". "Checked" and "nobody has looked" cannot both be true, and
"Checked" is the word a hurried reader takes. Second, of the 588 things here, this is the
one title that argues against adopting the tool in a school — the single most useful
document to hand a sceptical head of department — and it is the one with no summary and no
verdict.

The "Something wrong with this one? Tell us" link at the foot opens a GitHub issue with
the resource, the link and the page pre-filled. That is thoughtful. It still needs a
GitHub account, and no teacher I work with has one.

## 6. Search, in my words

Typed into the Browse search box, no role or level filter, exactly as written.

| # | what I typed | top 3 I was shown | verdict | why |
|---|---|---|---|---|
| 1 | how do I mark 30 essays faster without uploading my students' work | Claude for Education Is Made for Learning (Univ. of Pittsburgh) · AI in assignment design (Cornell) · PRD from a problem statement (Anthropic Academy) | bad | Nothing about marking or feedback. #1 and #2 are university policy pages; #3 is a product-manager document. The site holds "AI feedback customized for student writers: the updated PAIRR prompts", which is the right answer, and it did not appear. |
| 2 | is it safe to put pupil names into Claude | AI Fluency for Small Businesses · Claude for Small Business (Back-Office AI, honest review) · anthropics/claude-code-action | bad | A child-data question returns two small-business marketing courses and a GitHub Action. The right card, "Claude for Teachers: your data and our terms", is ranked **15th of 20**. Searching `pupil` on its own returns **0 resources**; `student` returns 36. |
| 3 | I need to write an AI policy for my school department | Using AI in education settings: support materials (UK DfE) · The Australian Framework for Generative AI in Schools · Creating a Public AI Policy for Your Newsroom | ok | The first two are precisely it, and they are national-level documents I could actually cite. The third is a newsroom, which is noise, but two out of three is a real answer. |
| 4 | make me a lesson plan and worksheet for year 9 | How Teachers Can Create Interactive Classroom Activities with AI (RoarTech Education) · Claude AI for Teachers: Complete Beginner's Guide (Teaching With Intelligence) · Stress-test your financial plan across scenarios (Anthropic Academy) | ok | #2 is genuinely usable for making materials. #1 is adjacent and fair. #3 is a personal-finance card in answer to a question about Year 9, which tells me the ranking is loose. "Adapt a standard textbook page to every reading level" exists here and would have been the perfect hit; it did not surface. |
| 5 | how do I stop my students handing in work Claude wrote | Best practices for getting started with Claude Cowork (Anthropic) · AI in assignment design (Cornell) · Claude Code settings and permission rules | ok | #2 is the correct professional answer — design the assignment differently. #1 and #3 are a Cowork onboarding page and a developer permissions reference, neither of which has anything to do with academic honesty. One right answer out of three, in second place. |

**The same question asked two ways.** I asked query 2 again in completely different
words: *"what happens to the information I type about the children in my class"*. That
returned "What does AI know about me?" at #1 and **"Claude for Teachers: your data and our
terms" at #2** — the right card, near the top. The first wording, *"is it safe to put
pupil names into Claude"*, put the same card at **15th**, behind two small-business
courses and a GitHub Action. I checked the difference directly: *"is it safe to put
**student** names into Claude"* puts it at **3rd**; *"is it safe to put **pupil** names
into Claude"* puts it at **15th**; the word `pupil` alone returns **0 of 588**.

**No, the site does not agree with itself.** One ordinary British word for a child breaks
the most important question a teacher can ask it, and instead of returning nothing it
returns confident, wrong answers about small business.

## 7. On a phone

Set to 375×812. This is the best part of the site.

- No sideways scrolling anywhere I looked. `document.documentElement.scrollWidth` is 375
  on both the home page and Browse.
- Browse collapses the filter rail into a "Filters" button pinned at the bottom, and Sort
  becomes a proper native dropdown instead of the three-button row it is on desktop. That
  is a real mobile design decision, not a squashed desktop one.
- Cards are large and readable. "For:" and "Skip if:" stay legible at arm's length. One
  card fills about one phone screen, which is honest — it is one thing at a time.

Two costs. The teacher + "used it a little" page is **18,032 pixels tall** for 29 cards,
and the first card starts 609 pixels down, so I scroll a full screen before I see
anything. And the pinned "Filters" bar sits on top of the card underneath it.

The badge problem below (section 8) is worst here: on a phone there is no hover, so the
words "Skimmed" and "Read by AI" on every card mean nothing at all and there is no way
from the card to find out.

## 8. What changed since Attack 2 — my verdict on each

**Tags and levels rebuilt on a rule.** Half right. At "never used Claude" and "used it a
little" the 57 cards I was shown are teachers' material. At "used it a lot" and "built
things with it", 5 of 10 are university lecturers, a training lead, or a developer
building an SVG app. The rule made the role tag true of the card; it did not make the
*card* about a school teacher. "43 Claude Skills for college teachers" carries the teacher
tag, is picked first at my level, and its own Skip line says "Skip if you teach at school
level". The tag survived a rule that reads the card's own words, and the card's own words
contradict it.

**Five collection cards.** Nothing found. I filtered to teacher and read all 67 titles;
no Sales, Legal, HR, Finance or Operations card appears. I did not trip over them.

**Search rebuilt.** See section 6. It handles a policy question well and a vocabulary
question badly. The failure mode is the dangerous one: a query it cannot serve returns 20
confident results rather than nothing, so I have no signal that it did not understand me.

**Cards that were stripped.** Honest, not broken — the sentence is plain and does not
pretend. Two faults: the same page says "Checked 21 Aug 2026" beside "Nobody has looked at
the content yet", and the teacher's one stripped card is the most decision-relevant title
in the whole teacher space.

**How well checked, as a filter.** The filter works (`Read in full` / `Read by AI` /
`Skimmed` / `Found only`, and "Found only" returns exactly 3). The *definition* does not
reach me. On a card, the badge is `<span class="badge badge-previewed" title="We read the
outline or a free sample...">Skimmed</span>` — the definition lives in a `title` attribute,
which only a mouse hover reveals. The card title link carries
`aria-describedby="tierdesc-previewed"`, and that text sits in a `<div class="visually-
hidden">`. So: a mouse user learns what "Skimmed" means; a screen-reader user learns it;
a sighted person on a keyboard learns nothing, and **a person on a phone learns nothing at
all**, because a phone has no hover. 00-facts says the definition is "meant to be
reachable from a card without a mouse". For a sighted touch user it is not. The words are
on `how-we-check.html`, but nothing on the card takes me there.

**The thin-level offer.** This is the best new thing on the site. At teacher + "built
things with it" I was shown:

> Only 2 at "built things with it" for a teacher.
> The level below, "used it a lot", has 8. **Add "used it a lot" too**
>
> Too few to pick from — these are all of them.

It makes sense, it names the exact number I would gain, and the arithmetic held — I
clicked it and got 10 resources, 2 + 8. **Yes, I would take it**, and I did. Two notes.
Nothing warns me that four of the eight I am about to add are written for university
lecturers. And the "Too few to pick from — these are all of them" line under it is the
right sentence: it tells me not to expect a recommendation, which is more useful than a
fake one.

**Date lines.** They make the site look maintained. "Checked 5 Sep 2026" is yesterday.
The stale flag is exactly right: "Published 27 Aug 2025 · over a year ago, may not match
Claude today" is the sentence I want on a card about a tool that changes quarterly. But
**48 of the 67 teacher cards say "No publish date given"** (I counted them on the live
page). That is 72% of my catalogue with no idea how old it is, on a subject where age is
the whole risk. "Checked" tells me when *this site* looked; it does not tell me whether
the thing it looked at is from last month or 2024.

**Prices.** No. The one paid resource a teacher is shown carries `pay once` and no number,
on both the card and the resource page. Across the whole catalogue I found 26 paid rows
and only **4** carrying a price. So for 22 of 26, and for 1 of 1 in my role, it is not
clear what I would pay before I click.

**Who "we" is.** It raises my trust in the site and lowers my trust in the
recommendations, and both are correct. `how-we-check.html` says: "One person makes this
site - a researcher at the Technical University of Denmark, working on it outside their
job... The reading is done by Claude... A person sets the rules... and has not yet read a
single resource end to end." I have never seen a directory admit that. I believe this site
more than I believe a glossy one. But it means the second-highest badge, "Read by AI", is
the best thing on offer, and I cannot walk into a head of department's office and say the
evidence is that an AI read it. One small inconsistency: the card tooltip defines Skimmed
as "We read the outline or a free sample. We have not seen the whole thing", while
`how-we-check.html` defines the same tier as "We read the outline or a free sample. Paid
courses usually stop here, because we cannot see inside them." Two different second
sentences for one label.

**The picks block.** Strong. The reasons are comparative — they say why *this* one and not
the others, which is the only kind of reason worth reading: "The only candidate that pairs
getting started with the harder question - which thinking students must still do without
help." At "used it a lot" it says "Start with these **two**" and explains itself: "Only two
here — a third would have to repeat a publisher or a format, and the rules allow neither."
The heading matches the count. Yes, at never-used and basic I would open all three.

**The social preview title.** Broken for sharing, which is how a site like this actually
spreads in a school. I checked the meta tags on three pages:
- `resource.html?id=...` — `og:title` is **"Resource — Learn Claude"**, while the browser
  tab correctly says "Claude for Teachers: your data and our terms — Learn Claude".
- `browse.html?role=teacher&level=builder` — `og:title` is **"Browse — Learn Claude"**,
  while the tab says "Browse 2 Claude resources — Learn Claude".
- `paths.html?id=first-week` — `og:title` is **"Paths — Learn Claude"**, while the tab
  says "Your first week with Claude — Learn Claude".
There is also **no `og:image` on any page**. So when I paste the data-and-terms link into
a staff chat, my colleagues see a picture-less grey card reading "Resource — Learn Claude
/ What this resource teaches, who it is for, who should skip it". Nobody clicks that. The
correct title already exists in `document.title` on every one of these pages.

**The home attract loop.** It runs — the illustration cycles roles — but it never touches
the sentence. Sixteen seconds on a fresh load, sampled every 400ms, and the headline stayed
"I'm a [role] and I've [level]." throughout. The picture moves and the words stay broken.
The loop also only ever shows `never-used.png`, so the illustration is stuck at one level
while it cycles ten roles.

**The sort control.** "Shortest first" is correct (15 min → 1 hour → half a day → several
days). "Newest first" is not what the label says. On teacher (67 cards), sorted newest
first: the item at **position 62 of 67** is "What are artifacts and how do I use them?",
**Updated 3 Sep 2026** — the most recently updated thing on the page, three days before I
looked, sitting near the bottom. Position 20 is "Get started with Claude Cowork", Updated
2 Sep 2026. Position 1 is "Why is Claude for Teachers?", Published 21 Jul 2026, six weeks
older. The sort uses `published` only, so the 48 cards with no publish date are dumped
below rank 19 regardless of how fresh they are — and inside that block they are not
ordered by `Updated` either, since 3 Sep sits 42 places below 2 Sep. "Newest first" buries
the newest thing.

**Paths above beginner level.** There are none for me. See section 4.

## 9. Content quality — the three worst entries I was shown, quoted

1. **"Build interactive diagram tools"** (Anthropic Academy, docs, 15 min, free) — one of
   only **two** cards a teacher gets at the top level. Its own For line:
   > For: Someone building a reference app from an existing structured data/SVG source.
   No teacher. No classroom. And the Skip line is a warning about the *content of the
   linked page*, not about who should skip:
   > Skip if: Filed under 'Personal' despite being a medical-education reference app - and
   > its own tip says to spot-check the anatomy content against a real textbook before
   > studying from it, since it isn't a verified medical source.
   That is a note-to-self about a page that appears to be miscategorised at source. It has
   been carried into my level as one of two options.

2. **"43 Claude Skills for college teachers"** (Doan Winkel) — ranked **first pick** at
   teacher + "used it a lot", with a reason praising it, directly above its own line:
   > Skip if: ...Skip if you teach at school level; the framing is semesters, syllabi and
   > departments.
   The site recommends it to me and tells me to skip it, in the same card, four lines
   apart.

3. **"Anthropic launched Claude for Teachers. We blocked it for our district."**
   (Dr. Joe Phillips) — the most important title in my role, with no For line, no summary,
   and a stock Skip line:
   > Skip if: You want something we have read. We have not opened this one yet.
   And, on the same page, "Checked 21 Aug 2026". It sits inside my "used it a little" cell
   among 29 cards, indistinguishable at a glance from the ones that were actually read.

## 10. Everything that is broken, ranked (evidence for each)

**1. Search fails on the ordinary British word for a child, and fails loudly.**
URL: `browse.html`, search box, no filters. Typed *"is it safe to put pupil names into
Claude"*. Got 20 results; top three "AI Fluency for Small Businesses", "Claude for Small
Business (Back-Office AI, honest review)", "anthropics/claude-code-action". The correct
card, "Claude for Teachers: your data and our terms", was 15th. Typed *"is it safe to put
student names into Claude"*: same card, 3rd. Typed `pupil` alone: **0 of 588**. Typed
`student` alone: 36. On its own, `pupil` is handled correctly — "0 resources for "pupil".
No match for "pupil". Browse everything instead." Inside a sentence, the other words
rescue it into twenty confident wrong answers. Expected: a synonym map that pairs `pupil`
with `student`, or — far more important — **no results rather than wrong ones**, so I know
the site did not understand me. Harms: every teacher outside the United States asking the one question they
must answer before touching this tool with a class. They get a confident wrong answer, not
a blank.

**2. Sharing a link shows the wrong title, and no image.**
URLs checked: `resource.html?id=r-5aa9ca06c5`, `browse.html?role=teacher&level=builder`,
`paths.html?id=first-week`. `og:title` on those three pages is "Resource — Learn Claude",
"Browse — Learn Claude", "Paths — Learn Claude". `document.title` on the same three pages
is correct and specific. No `og:image` exists on any page. Expected: the preview to carry
the title I can already see in my browser tab. Harms: anyone who tries to spread this in a
school. Teachers share by pasting links into staff chats and emails; a grey card saying
"Resource — Learn Claude" is not opened. This is the difference between a site one person
uses and a site a department uses.

**3. "Newest first" buries the newest thing.**
URL: `browse.html?role=teacher&sort=newest`. The card at position 62 of 67 is "What are
artifacts and how do I use them?", Updated 3 Sep 2026 — the most recent date on the page.
Position 20 is Updated 2 Sep 2026. Position 1 is Published 21 Jul 2026. 48 of the 67 cards
say "No publish date given" and all of them are ranked below position 19. Expected: a
control labelled "Newest first" to put the most recently dated thing first, using
`Updated` when `Published` is absent. Harms: exactly the careful reader — the one who sorts
by newest because AI advice rots — is handed the six-week-old item first and the three-day-
old item 62nd.

**4. No path for a teacher above absolute beginner, and no path about teaching at all.**
URL: `paths.html`. Seven paths. One names a teacher: "Your first week with Claude — Anyone
who has just opened Claude and does not know what to do next." Its six steps are "Claude
is not one tool. It's six.", "Get started with Claude", "Claude 101", "What are Projects?",
"Why do AI models hallucinate?", "Get started with Claude Cowork". Meanwhile a developer,
a writer, a product manager, a data analyst and a designer each get a path about their own
job. Expected: at least one ordered route through marking, materials or classroom policy —
the site holds enough teacher material to build one. Harms: the returning visitor. A path
is the thing that brings someone back a second week, and mine ends after week one.

**5. Nothing here about marking.**
URL: `browse.html`. `marking` → 4 results of 588, led by "Claude AI Comprehensive Guide"
and "PRD from a problem statement". `grading` → 4, led by "Teaching AI Fluency" and
"Demystifying evals for AI agents". Filtered to teacher + "used it a little",
`marking essays` → 2 resources, neither about marking. Expected: the largest recurring task
in the job to be covered. Harms: every teacher who arrives on a Sunday evening with a pile
of books, which is most of us, most weeks.

**6. The "how well checked" badge cannot be understood on a phone or by keyboard.**
URL: any card on `browse.html`. The badge is `<span class="badge badge-previewed"
title="We read the outline or a free sample. We have not seen the whole thing.">Skimmed
</span>` — no `tabindex`, not focusable. The definitions also exist inside
`<div class="visually-hidden">` and are attached to the card's title link with
`aria-describedby`. So the definition reaches a mouse (hover) and a screen reader, and
reaches nobody else. Expected: the badge to be a link, a focusable control, or to carry
its own short gloss. Harms: phone readers, who are most teachers reading between lessons.
A tier ladder whose top rung is empty is a strong honesty signal only if the reader can
find out what the rungs mean.

**7. The one paid item a teacher is shown has no price.**
URLs: `browse.html?role=teacher&cost=paid-once,subscription` and
`resource.html?id=r-cbd7194dc6`. "Claude, Claude Code, Claude Cowork, and Claude in MS
Office" (Udemy) shows chips `course` / `half a day` / `pay once` and no figure, on the card
and on the resource page. Across the whole catalogue, `cost=paid-once,subscription`
returns 26 cards and only 4 carry a price ("from $49", "from $995", "from $2,999"). STATUS.md
records 10 paid-once and 16 subscription. Expected: a price, or "price not checked", on
every paid card. Harms: anyone with no budget, who must not click through to a sales page
to discover the number.

**8. The home page headline is a raw template until you touch it.**
URL: `/learn-claude/`. On a fresh load, sampled every 400ms for 16 seconds with no input,
`p.display` reads "I'm a [role] and I've [level]." throughout, while the illustration
cycles `non-technical` → `student` → `researcher` → `teacher` → `developer` →
`data-analyst`. `prefers-reduced-motion` is not set. Expected: if the picture cycles roles,
the sentence cycles with it — or the sentence starts as a readable question. Harms: every
first-time visitor, in the first two seconds, on the page that has to earn the next click.
Square brackets are what unfinished software looks like.

**9. "Checked" is printed on cards nobody has opened.**
URL: `resource.html?id=r-76de44b7a7`. The page says "Found only. We found it and sorted it.
Nobody has looked at the content yet." and, three lines below, "Checked 21 Aug 2026".
Expected: a different word — "Found 21 Aug 2026" — where nothing was checked. Harms: the
skimming reader, who takes "Checked" as a warrant.

**10. "1 resources" on a filtered page.**
URL: `browse.html?role=teacher&checked=listed`. The page reads "1 resources for a teacher.
Remove a filter to see more." The browser tab on the same page reads "Browse 1 Claude
resource — Learn Claude", correctly singular. Without a role, the same state reads
"1 resource." correctly. So the plural bug is only in the role-qualified string. Expected:
"1 resource for a teacher." Harms: small, but it is the kind of thing a head of department
notices while I am arguing that the site is careful.

## 11. The one thing that would make me leave and not come back

Asking whether it is safe to put pupil names into Claude and being shown "AI Fluency for
Small Businesses".

Not because the answer is missing — the answer is on this site, and it is good. Because the
site answered anyway. Twenty confident results, none of them mine, and no line saying "we
did not understand that". If a directory returns small-business marketing when I ask about
children's data, I have to independently verify everything else it tells me, and at that
point I am doing the work the site exists to save. I would close the tab and ask a
colleague.

## 12. What is genuinely good (honest, brief)

- **The Skip if: line.** It is the reason to use this site. "Skip if you teach at school
  level; the framing is semesters, syllabi and departments" saved me an hour, even though
  it appeared under a recommendation.
- **`how-we-check.html`.** "One person makes this site - a researcher at the Technical
  University of Denmark... and has not yet read a single resource end to end." No
  directory admits that. It is the reason I trust the labels.
- **The picks reasons.** Comparative, not promotional: "The only candidate that pairs
  getting started with the harder question - which thinking students must still do without
  help."
- **The thin-level offer.** Names the number, keeps its promise, and refuses to fake a
  recommendation: "Too few to pick from — these are all of them."
- **The phone layout.** Genuinely designed for a phone, not shrunk onto one. The Filters
  button and the native Sort dropdown are real decisions.
- **The never-used teacher cell.** Three picks, all school teaching, all free, all
  explained. If a colleague asked me where to start, I would send them
  `browse.html?role=teacher&level=never-used`.

## 13. Would I come back, and what one thing would make me?

Yes, but only for one thing, and only if I already know what I am looking for.

I would come back and send `browse.html?role=teacher&level=never-used` to the two people
in my department who keep asking me where to start. Those three cards are better than
anything I could put together myself, and the Skip lines mean I am not wasting a
colleague's evening. That is real, and it is more than most sites give me.

I would not come back for myself. I have used Claude for a while, and the moment I say so
the site starts handing me university lecturers and a page about building an SVG diagram
app. There is no path for me past week one, there is nothing about marking, and the search
box cannot handle the word "pupil". Everything I actually came for is either missing or
one wrong synonym away from invisible.

One thing. **Make the search say "I don't know" instead of guessing.** If I ask about
pupil data and you have nothing indexed under that word, tell me you found nothing. The
site already knows how — type `pupil` on its own and it says, correctly, "0 resources for
"pupil". No match for "pupil". Browse everything instead." Put the same word in a
sentence and the other words rescue it into twenty wrong answers. `how-we-check.html`
promises the honest behaviour — "when we have nothing on your subject, you get nothing back
and a line saying so" — and does not keep it for my question. Twenty wrong answers cost me more than zero answers,
because zero answers takes two seconds and twenty takes ten minutes and leaves me
distrusting the nineteen good things you have. Everything else here is honest. Make the
search honest too, and I will use this every week.

## Checklist
- [x] I opened the live site
- [x] I tried all four levels
- [x] I quoted at least 5 real titles or lines from the site
- [x] Every number I used is in 00-facts.md, STATUS.md, or quoted from the site
- [x] I looked at a phone width
- [x] I read no file under scripts/ or data/
- [x] I found at least one thing nobody has mentioned before
