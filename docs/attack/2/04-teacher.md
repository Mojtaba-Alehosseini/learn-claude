# Attack 2: a teacher
Written as a school teacher, 2026-09-05. Live site only:
`https://mojtaba-alehosseini.github.io/learn-claude/`.

I teach. I have built a marking helper and a scheme-of-work generator. My head of
department has asked me for the policy pile — what the frameworks say, what we are allowed
to do about detection, what to tell parents.

**Method note.** This browser was shared with other agents, which repeatedly hijacked the
tab (filters flipping, self-navigation, junk history). I spent about fifteen minutes
chasing a phantom "the home page navigates itself" bug before reading `assets/js/home.js`
and confirming the site has **no** auto-navigation code. **Discarded — not reported.**
Every finding below is reproduced either from a direct URL or from an in-page test that does
not depend on the input harness. Outbound links are unreachable from this sandbox (all 75
teacher URLs return curl `000`), so **I make no claim about link rot.**

---

## 1. First 60 seconds

A cup drawn in marker, and one sentence: *"I'm a [role] and I've [level]."* Underneath,
*"635 resources, checked by hand."* No signup, no cookie banner, no newsletter. That buys
goodwill fast.

But the second question is not there. I get "Who are you?" and ten chips; the level chips
only appear after I pick. So it is a two-screen quiz sold as one sentence. Fine, minor.

The thing that made me sit up: three promises under the fold — *"We say when to skip"*,
*"We say how we checked"*, *"We show the date."* That is the right three. The rest of this
report is about whether they hold.

---

## 2. The front door, all four levels

Picked **a teacher** -> *"75 resources match so far."* Then each level, measured live from
the front door:

| I've... | matches |
|---|---|
| never used Claude | **32** |
| used it a little | **32** |
| used it a lot | **9** |
| built things with it | **2** |

I am the fourth one. The site asked me two questions, I answered both honestly, and it
handed me **2 things out of 635**.

`browse.html?role=teacher&level=builder` -> *"2 resources. Remove a filter to see more."*

1. **"Build interactive diagram tools"** (Anthropic Academy) — whose own Skip if reads:
   *"Filed under 'Personal' despite being a medical-education reference app - and its own
   tip says to spot-check the anatomy content against a real textbook before studying from
   it, since it isn't a verified medical source."* That is not a teaching resource. That is
   an anatomy app demo.
2. **"Agent Skills for K-12 Teachers (open source)"** (GitHub) — genuinely relevant.

So the honest answer for an experienced teacher is *one* usable link. Both cards say
"Skimmed". Both say "No publish date given". And there is no "Start with these three" block
at this level — the page just stops.

Ten roles by four levels = 40 cells. Three have no picks block at all; **student by "built
things with it" has literally zero resources.**

---

## 3. What the catalogue gives me

The cards are the best-written thing here. Real examples I read:

- *"Skip if you only need text output like lesson plans and worksheets - Artifacts is
  overkill for that."*
- *"Needs verified US K-12 educator status, and the featured scheduled-briefing workflow
  additionally depends on a TeachFX classroom-recording account, a separate paid
  third-party product."*
- *"Needs the model picker set to Opus 5 specifically (the page even has a typo calling it
  the model 'picket')"*
- *"Skip if sales pages irritate you - most of this is claims, logos and testimonials. Skip
  if you are outside the US, because the free plan is US-only."*

That last one is a card telling me the thing it is linking to is a sales page. I have never
seen a directory do that. Credit.

**Two structural problems.**

**(a) The topic filter has nothing to do with my job.** "More filters" gives eight topics:
*chat and prompting, Claude Code, Cowork, Skills, connectors, agents, API, limits and
safety.* Six of eight are Anthropic product surfaces. There is no assessment, no academic
integrity, no policy, no classroom. Meanwhile the catalogue contains the **UNESCO AI
competency framework for teachers**, the **Australian Framework for Generative AI in
Schools**, the **EU ethical guidelines**, the US Dept of Education toolkit, and **The AI
Assessment Scale (AIAS)** — and no filter on this site can reach them as a group. My head of
department asked me for exactly that pile, and the taxonomy is built around a product line
instead of around me.

**(b) The site has already done the classification I need, then throws it away.** Twelve of
my 75 cards end their "For:" sentence with a bare fragment: *"Own work."*, *"Policy, not
classroom practice."*, *"Policy and classroom judgement."*, *"Own work and school policy,
school level."* That is the single most useful axis a teacher could have — is this about my
planning, my classroom, or my school's policy? It is applied to 12 of 75, it is **not a
filter**, and the words "own work" appear nowhere on the site outside the card data. "How we
check" contains no mention of disclosure, conflict, or self-promotion. So *"Own work."* reads
like a copy-paste accident.

**Where I am, geographically:** 9 of 75 teacher items are explicitly US-gated (FERPA,
"US-only", "verified US K-12 educator status"), and they are the four most important ones —
the product, its terms, its announcement, its demo. The cards flag it every single time,
which is genuinely good. There is still no country filter.

---

## 4. Paths

Seven paths. Exactly one lists me: **"Your first week with Claude"**, shared with *"not a
coder, a student, a teacher, running a business."*

Developers get "Getting good at Claude Code". Writers get "Using Claude on work you put your
name to". PMs, researchers, analysts and designers each get a route built for their job.
Teachers get the generic beginner track. **There is no teacher path.** Not for marking, not
for assessment design, not for the policy conversation — even though the catalogue holds the
material for all three.

I followed `paths.html?id=first-week` and read every step reason. They are good — each one
justifies its *position*, not just its content:

- Step 1: *"Start here because most confusion is not about prompting — it is not knowing
  that Claude is several different products."*
- Step 3: *"By now you have had a generic, disappointing answer."*
- Step 4: *"Once you repeat a task twice, you need somewhere to keep the context... Learning
  this earlier would have been abstract."*
- Step 6: *"Last, because working on your own files only makes sense once you trust the
  answers."*

That is real editorial work and the best thing on the site. Two problems with it anyway:
**all six steps say "No publish date given"** — six for six — and **five of six are published
by Anthropic** (Claude Help Center x3, Anthropic Academy x2). Not one of the six steps
mentions a classroom, a student, marking, or a policy. It is a product onboarding, labelled
for teachers.

The Paths page also has no filter, so I read seven blurbs to learn six were not for me. And
it says *"4 steps · about 81 minutes"* on one path next to *"about 4 hours"* on another.
"About 81 minutes" is not about anything.

---

## 5. The card and the resource page

Three pages opened. Yes, I would click through — the resource pages are better than the
cards. **"Guidance on AI detection, and why we're disabling Turnitin's AI detector"**
(Vanderbilt) carries this:

> *"never treat any detector score as proof against a student - false accusations fall
> hardest on non-native English writers."*

That is the most useful sentence on this website and nobody paid them to write it.

**Then the badge underneath it destroys it.** Same page:

> *"Found only. We found it and sorted it. Nobody has looked at the content yet."*

And directly above, on the same page, the site states as fact: *"at its own submission volume
the false-positive rate would have wrongly flagged thousands of papers a year, and Turnitin
would not explain how the score is produced"*, plus a "What it teaches" list: *"argue against
using turnitin ai detection in your department"*, *"explain false-positive risks to school
administrators"*, *"protect non-native English writers from false AI accusations."*

You cannot write any of that without reading the page. Same contradiction on **"Anthropic
launched Claude for Teachers. We blocked it for our district."** — badge says nobody looked,
page states a specific legal argument: *"FERPA lets a vendor act as a 'school official' only
where the district designates it and keeps direct control, and an individual teacher cannot
make that designation on the district's behalf."*

**I checked all 36 "Found only" items. 36 of 36 have a written summary (median 214
characters), a written "Skip if" (median 160 characters), and a three-item "What it teaches"
list.** Not one is a bare link. The tier label is false on every single one of them.

---

## 6. The picks block

`browse.html?role=teacher&level=confident` — *"Start with these three · picked by AI · 5 Sep
2026"*.

**Is it the first three rows? No — I checked.** I reimplemented the default sort (tier, then
checked-date, then title) against the data. Overlap with the picks: **1 of 3** for
never-used, **1 of 3** for basic, **2 of 3** for confident. Something is genuinely choosing,
not slicing.

**Do the reasons add anything the title did not?** Yes, and they are comparative, which is
the hard kind:

- *"Two courses in this pool carry almost this name; this is the one that is actual training
  rather than a delivery kit, and the only candidate built around the constraints schools
  actually have - limited budget, many people to answer to."*
- *"The only candidate that pairs getting started with the harder question - which thinking
  students must still do without help - which is the question a teacher is asked in week
  one."*
- *"The classroom craft task with the widest reach in the pool - every teacher
  differentiates, where the alternatives serve one subject's typesetting or one syllabus
  shape."*

That last one is doing real work: it tells me the alternatives are a LaTeX maths thing and an
economics syllabus thing, so I do not have to open them. Good.

**Is the "used it a lot" cell narrow? Badly.** Nine resources, **three publishers**, and
**seven of the nine are Anthropic Academy** (78%). The picks themselves come from **two**
publishers: Doan Winkel, then Anthropic Academy twice.

And the block admits it. The first pick reason reads: *"...and the only non-Anthropic voice
in the pool."* The site is telling me, in its own recommendation copy, that its
confident-teacher shelf is one company plus one blogger. Once I noticed that, the "Everything
else for you (6)" list confirmed it: *"Create custom course materials"* is university maths
and the tcolorbox LaTeX package; *"Plan your syllabus"* is checked against Mankiw and
Blanchard economics textbooks; *"Turn research into presentations"* says *"For: Students or
academic researchers."* Three of the six are not for a school teacher at all.

**Trust up or down from "picked by AI"?** Up, slightly, and only because it is honest. I
would trust "picked by AI" over an unlabelled editor's list, because I know what I am
getting. What I will not do is act on it without opening the thing — and the site agrees with
me, which is the point. The label is the right call.

---

## 7. Dates and tier badges

**The dates are the honest part, and then two bugs undo them.**

489 of 635 cards (77%) say *"No publish date given"* — in my slice, 54 of 75 (72%). That is
worse than "three in four". 44 items site-wide (14 of my 75) show an *"Updated"* date with no
published date. Three show a month with no day (*"Updated May 2026"*, *"Updated Feb 2026"*).

That is not abandonment. Every one of the 635 was checked between **18 August and 5 September
2026** — an 18-day window — and **211 were checked today**. This catalogue is three weeks old
and maintained daily. The missing dates are the publishers' fault, not the site's, and
`ui.js` even documents why: Intercom-templated pages print a revision date and never a
publication date, and writing that into `published` *"would make the card state a publication
date that is false."* Correct decision, well reasoned.

**Bug 1 — the recency evidence disappears on the page you would actually forward.** Browse
card for *"Claude for Teachers: your data and our terms"*: `Checked 5 Sep 2026 / No publish
date given / **Updated 28 Aug 2026**`. Click it. `resource.html?id=r-5aa9ca06c5` says:
`Checked 5 Sep 2026 · No publish date given · Found through Claude Help Center`. **The
"Updated 28 Aug 2026" is gone.** Cause: `resource.js` prints `item.published` directly and
never reads `fresh.updatedNote`. This is the page a head of department gets emailed, and it
is strictly less informative than the card that linked to it. Affects all 96 items that carry
an updated date.

**Bug 2 — the staleness warning disappears too.** Browse card for the Turnitin piece:
**"Published over a year ago — may not match Claude today"**. Its resource page: **"Published
16 Aug 2023"**, no warning. Same cause — `resource.js` ignores `fresh.note`. So the one card
the site correctly flags as three years old loses the flag on the page you would cite in a
department meeting.

**Tier badges — what they say about the work behind this site.** "Read by AI" (98), "Skimmed"
(501), "Found only" (36). Four in five cards are outline-only. That is a person harvesting
fast, then writing carefully. I respect the ladder existing at all. But as shown in section 5,
the bottom rung is a lie in all 36 cases — and once one badge is provably false, I stop
trusting the other two.

---

## 8. Search, in my words

| # | I typed | Results | Top three | Verdict |
|---|---|---|---|---|
| 1 | `can students cheat with claude` | 21 | 1. **"Claude Code Crash Course For Developers"** (Traversy Media) 2. "Teaching AI Fluency" 3. "AI feedback... PAIRR prompts" | **Fail.** #1 is a video for *"Experienced web developers"*. The site holds "AI & Academic Integrity", "The AI Assessment Scale (AIAS)" and the Vanderbilt detector piece — **none in the top five**. |
| 2 | `make a lesson plan` | 56 | 1. "How Teachers Can Create Interactive Classroom Activities" 2. "Claude for K-12 teachers – product page" 3. "Claude for Teachers in action" | **Fail, comically.** #1's own Skip if: *"Skip if you only need text output like lesson plans and worksheets - Artifacts is overkill for that."* #2 is the card that says it is *"claims, logos and testimonials."* #4 was **"How I use Claude Code for real engineering"** and #5 **"Ralph: PRD skill plus autonomous implementation loop"** — an autonomous coding agent, in a lesson-plan search. |
| 3 | `marking essays` | **2** | 1. "Claude for Education Is Made for Learning" — *"For: A student..."* 2. "Plagiarism and Academic Integrity 101" — *"For: Any student..."* | **Total fail.** The most common teacher task on earth returns two resources, both aimed at students. "43 Claude Skills for college teachers", whose own summary says *"rubrics, rubric-aligned feedback"*, is not returned. |
| 4 | `ai policy for school` | 49 | 1. Australian Framework for Generative AI in Schools 2. US DoE "Empowering Education Leaders" 3. UK DfE "Using AI in education settings" | **Pass — very good.** Three governments, each labelled by jurisdiction. This is the query the site was built for. (Two of three are "Found only".) |
| 5 | `is claude safe for students` | 31 | 1. "Claude for Teachers: your data and our terms" 2. "Empowering Education Leaders" 3. **"Top 7 Claude Skills for Product Managers"** (Snyk) | **Half pass.** #1 is exactly right. #3 is product-manager marketing and #4 is a LinkedIn Learning subscription course. |

**Control that proves the mechanism:** I typed `grading`. Three results. **#1 is
"Demystifying evals for AI agents" (Anthropic)** — machine-learning regression testing.
`marking essays` and `grading` return different, near-disjoint, tiny sets for the same job.
There are no synonyms: *marking* is not *grading* is not *feedback* is not *rubric*; *essays*
is not *writing*. The search is literal token matching over title/summary/who_for/source. For
a site whose search box says *"Title, topic, or what you want to do"*, "what you want to do"
is exactly what it cannot handle.

---

## 9. On a phone

375x812. Good. Chips are large and tappable, the illustration is dropped (saves a megabyte of
hand-drawn PNGs), applied filters show as removable chips, and there is a sticky **Filters**
button pinned to the bottom. I opened the sheet: it renders, it locks body scroll (`overflow:
hidden`), and **it moves focus to the Close button**. Somebody thought about that.

One complaint: on Browse I scroll a full screen past *Browse -> Search -> Sort -> chips -> "9
resources" -> "Start with these three" -> "picked by AI"* before the first card title, and
the first card's "For:" line is still below the fold. Seven rows of chrome before one word of
content.

---

## 10. Keyboard walk

41 focusable controls on Browse at 1440x900, sane DOM order, and a real focus ring — `1.6px
solid rgb(20,20,19)`, correctly gated on `:focus-visible`. Skip link is first. Filter buttons
carry `role="checkbox"` and `aria-checked` tracks state correctly (I verified true/false
toggling with fresh DOM queries against the live count: 9 -> 41 -> 9).

**One real defect: "Skip to content" does not skip.**

Activating it in-page (`sk.click()`, which is what Enter on a link does): `location.hash`
becomes `#main`, and `document.activeElement` **falls back to `<body>`** —
`focusMovedIntoMain: false`. Then the next Tab starts over at the top of the document; with a
real keypress I confirmed the next Tab landed on "Learn Claude", the second element on the
page.

Root cause, one attribute: `<a class="skip-link" href="#main">` points at `<main id="main">`,
which has **no `tabindex="-1"`**. A fragment link to a non-focusable element scrolls but does
not move focus. Reproduced identically on `index.html`, `browse.html` and `resource.html`.

Consequence: the keyboard user the skip link exists for must Tab past **24 controls** (nav x4,
Clear all, 10 role buttons, 4 level buttons, 4 time buttons, More filters, search, sort, 2
filter chips) before reaching the first result — on every single browse page.

*Not reported:* Enter/Space failed to activate any button through the automation harness,
including plain native `<button>` elements where the browser guarantees activation. That is
the harness, not the site. Mouse activation works correctly.

---

## 11. How we check

**More on intent, less on delivery.** It is the most honest page of its kind I have read.
*"We do not take money to rank a resource. We are not affiliated with Anthropic."* *"It needs
a GitHub account, which is a real barrier and we know it."* The note that Anthropic's
certification is Partner-Network-only, so exam-prep sellers are excluded — that is a genuine
service.

Then the page opens with this:

> *"We would rather have 70 resources we can vouch for than 700 we cannot."*

and 400 words later says:

> *"Right now: 635 resources — 98 read by ai, 501 skimmed, 36 found only. Nothing is read in
> full yet."*

By its own stated definition — "Read in full: We went through all of it and a person checked
the notes" — **it can vouch for zero of the 635.** The page states a principle and then
reports breaking it, in the same voice, without noticing.

Worse, two paragraphs collide:

> *"What we do: We find material, **read it**, and write two things: who it helps, and who
> should skip it."*
> *"Found only. We found it and sorted it. **Nobody has looked at the content yet.**"*

All 36 "Found only" items have both of those two things written. One of those sentences is
untrue.

---

## 12. Everything broken, ranked

| # | Finding | Evidence | Who it harms |
|---|---|---|---|
| **1** | **"Found only" badge is false on 36 of 36 items.** Badge: *"Nobody has looked at the content yet."* Same page states specific content claims and a 3-item "What it teaches" list. | `resource.html?id=r-1b663b7646` and `?id=r-76de44b7a7`; all 36 `listed`-tier items have summary + skip_if + teaches | A teacher taking the FERPA argument or the Turnitin false-positive claim to a head of department. They are repeating a claim the site says nobody checked, from a page that reads authoritative. |
| **2** | **Answer both front-door questions honestly as an experienced teacher -> 2 results.** Front door promises "635 resources, checked by hand". | `browse.html?role=teacher&level=builder` -> *"2 resources."* One is an anatomy-app demo. No picks block. `student\|builder` has 0. | Every teacher already past beginner — the ones with the most to contribute and the least patience. They conclude the site is a beginner farm and never return. |
| **3** | **Resource pages drop the "Updated" date the card showed.** Card: *"Updated 28 Aug 2026."* Page it links to: *"No publish date given."* | `resource.js` prints `item.published` and never reads `fresh.updatedNote`; affects 96 items. Verified live on `?id=r-5aa9ca06c5` | Anyone forwarding a link. The page you send is less trustworthy than the card you clicked. |
| **4** | **Resource pages drop the staleness warning.** Card: *"Published over a year ago — may not match Claude today."* Page: *"Published 16 Aug 2023."* No warning. | Turnitin item, card vs `resource.html?id=r-1b663b7646` | A teacher citing 2023 detector figures in a 2026 policy meeting, with the warning stripped off on the way. |
| **5** | **Search cannot handle teacher vocabulary.** No synonyms. | `?q=grading` -> #1 *"Demystifying evals for AI agents"*. `?q=marking+essays` -> 2 results, both *"For: A student"*. `?q=make+a+lesson+plan` -> #1 says skip it for lesson plans; #4 Claude Code; #5 an autonomous coding agent. | The teacher who trusts the search box instead of the filters — i.e. most of them. The right answers exist in the catalogue and are not returned. |
| **6** | **No path for a teacher.** 7 paths; 6 are role-specific; teachers share the generic beginner one. | `paths.html`; `first-week` lists *"not a coder, a student, a teacher, running a business"* | Teachers, uniquely among the ten roles the front door offers. Six other roles get a route; I get an onboarding. |
| **7** | **Topic filter has no teacher topics.** 8 topics, 6 are Anthropic product surfaces. | "More filters" -> *chat and prompting, Claude Code, Cowork, Skills, connectors, agents, API, limits and safety* | Anyone whose head of department asked about policy. UNESCO, the EU guidelines, the Australian framework and the AIAS are all in here and no filter reaches them. |
| **8** | **"Skip to content" does not move focus.** Sets `#main`, focus falls to `<body>`. `<main id="main">` has no `tabindex="-1"`. Site-wide. | In-page test on index/browse/resource: `focusMovedIntoMain: false`; next real Tab -> "Learn Claude" | Keyboard and screen-reader users, on every page, forced through 24 controls to reach the first result. |
| **9** | **"Own work." / "Policy, not classroom practice." is undefined and unfilterable.** The site's best teacher axis, thrown away as a sentence fragment. | 12 of 75 teacher cards; the phrase appears nowhere outside `items.js`; "How we check" has zero mentions of disclosure | Teachers, who need exactly this split — my planning vs my classroom vs my school's policy — and cannot sort by it. |
| **10** | **"70 we can vouch for" vs 635 it cannot.** Principle stated and broken on the same page; "we... read it" contradicts "nobody has looked at the content yet". | `how-we-check.html` | Anyone deciding whether this site's judgment is worth anything. It is the one page whose whole job is answering that. |
| **11** | Minor: Paths page has no role filter (7 blurbs to find 1). *"about 81 minutes"* beside *"about 4 hours"*. Mobile Browse shows 7 rows of chrome before the first card body. 9 of 75 teacher items are US-gated with no country filter (each one flagged in Skip if — credit). | `paths.html`, 375x812 | Time, mostly. Non-US teachers, mildly. |

---

## 13. The one thing that would make me leave

Section 2. I answered the site's own two questions truthfully — *a teacher, built things with
it* — and it gave me **two links, one of which is a medical-anatomy app demo**, after
promising 635 on the previous screen.

A directory earns its keep by being deeper than me on my own subject. This one is shallower
than my staff-room WhatsApp group the moment I stop being a beginner. And it has no way to
tell me that in advance: the front door shows a running count that only drops after I have
committed to both answers.

If the "used it a lot" and "built things with it" cells for teachers stay at 9 and 2, do not
offer the levels. Say "this site is for teachers new to Claude" and I will respect it.
Offering four levels and stocking two is the thing that makes me close the tab.

---

## 14. What is genuinely good

- **The "Skip if:" line is the whole product and it works.** *"never treat any detector score
  as proof against a student - false accusations fall hardest on non-native English
  writers."* *"the page even has a typo calling it the model 'picket'."* *"most of this is
  claims, logos and testimonials."* Nobody writes that about a link they want you to click.
- **The picks are real editorial work, not the first three rows.** I checked against the
  actual sort: overlap 1/3, 1/3, 2/3. The reasons compare against the pool rather than
  describing the item — *"Two courses in this pool carry almost this name; this is the one
  that is actual training rather than a delivery kit."*
- **Path step reasons justify position, not content.** *"Learning this earlier would have been
  abstract."* That sentence is why paths beat lists.
- **The date honesty is principled.** "No publish date given" rather than an invented date,
  with the reasoning written into the code: writing a revision date into `published` *"would
  make the card state a publication date that is false."* And the catalogue is genuinely
  alive — all 635 checked inside 18 days, 211 today.
- **"picked by AI" and the tier ladder existing at all.** The labels move my trust in the
  right direction, even where one of them is wrong.
- **No account, no tracking, no newsletter.** *"We do not track your progress. Nothing here
  needs an account."*
- **The mobile filter sheet moves focus to Close and locks body scroll.** Small, invisible,
  correct.

---

## Checklist
- [x] I opened the live site at all four levels of my role — 32 / 32 / 9 / 2
- [x] I quoted at least 5 real titles or lines from the site — 25+
- [x] Every number I used is computed from the shipped data or from a live DOM read
- [x] I looked at a phone width — 375x812, filter sheet opened
- [x] I did one full keyboard walk — 41 stops, skip-link focus tested directly
- [x] Five search queries in my own words, plus a control (`grading`)
- [x] I read the picks block and tested whether it is the top three rows — overlap 1/3, 1/3, 2/3
- [x] I found at least one thing nobody has mentioned before — the skip link sets the hash but
      never moves focus, because `<main>` has no `tabindex="-1"`; and the "Own work. / Policy,
      not classroom practice." axis the data already carries and no filter can reach
- [x] I discarded a finding I could not reproduce, and said so — the phantom self-navigation
