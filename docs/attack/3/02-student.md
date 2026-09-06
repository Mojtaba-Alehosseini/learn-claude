# Attack 3: a student
Written as a student, 2026-09-06. Site version: 9deb0db.

Undergraduate, mid-degree, coursework due. I want to use Claude without being accused of
cheating, and I want it to help me learn, not do the work. I will not pay for anything.

---

## 1. The first 60 seconds

I opened `https://mojtaba-alehosseini.github.io/learn-claude/`.

The big line says:

> I'm a [role] and I've [level].

It stays that way. I watched the page for 21 seconds without touching it and sampled the
sentence 30 times. It never changed. The square brackets are still there.

Under it, one role chip is painted a different colour than the other nine. It moves. I
sampled every chip's background every 700 ms for 21 seconds:

```
0s  showing = running a business
1s  showing = a writer
4s  showing = not a coder
7s  showing = a student
9s  showing = a researcher
12s showing = a teacher
15s showing = a developer
17s showing = working with data
20s showing = a product manager
```

Every one of those samples had `sentence = I'm a [role] and I've [level].`

So the page lights up a chip every ~2.5 seconds and never fills the sentence the chip is
supposed to fill. The highlight colour is not the selected colour either — a really
selected chip goes dark with white text (`aria-pressed="true"`), the loop uses a pale
panel colour. I checked `aria-pressed` on all fourteen chips while one was lit: all
`false`.

What I saw for the first ten seconds was a page where one option looks half-chosen at
random and the headline is full of placeholder brackets. That reads as a page that failed
to load, not as an invitation.

The three promise blocks below are good and I read all three. "Every entry has a `Skip if:`
line" is the reason I kept going.

**Verdict: the copy is good, the first paint is broken.**

---

## 2. Does the front door work for me (all four levels, with what I was shown)

I clicked **a student**. The page said "77 resources match so far." Then I did each level.

| level I clicked | home page said | Browse said | picks block |
|---|---|---|---|
| never used Claude | "42 resources match so far." | `browse.html?role=student&level=never-used` — 42 resources | "Start with these three" + "Everything else for you (39)" |
| used it a little | "26 resources match so far." | 26 resources | three picks + "Everything else for you (23)" |
| used it a lot | "9 resources match so far." | 9 resources | three picks + "Everything else for you (6)" |
| built things with it | "0 resources match so far." | 0 resources | none |

**Level 1 — never used Claude (42).** The three picks are the best thing on the site for
me:

- "Claude for Education Is Made for Learning" — University of Pittsburgh
- "Claude 101" — Anthropic Academy
- "Plagiarism and Academic Integrity 101 in the Age of AI" — Tulane University Libraries

The third one is the question I actually have, and the reason given says so: "The only
candidate that answers the question a student has before any tool question - where the
line is". That is the first time a directory has read my mind.

**Level 2 — used it a little (26).** Picks are "Visuals that appear as you study with
Claude", "Documenting Your AI Use" (St. Catherine University Library) and "Claude AI for
Researchers: Projects, Skills, Cowork & Consensus Explained". "Documenting Your AI Use" is
for "A student who wants to protect themselves from a false accusation by keeping a
defensible record of how they worked." That is exactly me.

**Level 3 — used it a lot (9).** This is where it falls apart. See section 3.

**Level 4 — built things with it (0).** The "Show me" button is still enabled at zero, and
the count line says "0 resources match so far." — "so far" reads like it will get better
by clicking. It will not. Browse then says:

> We have nothing for this combination yet.
> It's on the list. The level below has 9. **Add "used it a lot" too** Or see everything
> for this role, or browse everything.

I clicked "Add "used it a lot" too". It worked: it took me to
`browse.html?role=student&level=builder%2Cconfident` with 9 resources. Honest, and I would
take it.

But adding the second level **deleted the picks block**. At `level=confident` alone the
page has "Start with these three". With two levels ticked the only heading left is
"Filters" and I get a flat list of 9. The site's own `how-we-check.html` says: "It will
not tell you which of three results is best; that is what 'Start with these three' is
for". So the one-click offer for the empty cell hands me the exact list the site says it
cannot rank for me.

---

## 3. What the catalogue actually gives me (are these really for me?)

At my highest level — **a student, used it a lot, 9 resources** — this is the whole shelf:

1. Reduce hallucinations — *For: **Any analyst** worried about confidently-wrong output.*
2. How To Use Claude For Academic Research (My Actual AI Stack) — *For: Academics and research students*
3. AI-Powered Flashcards with Claude Projects
4. AI feedback customized for student writers: the updated PAIRR prompts — *Skip if: ... **written primarily for instructors to deploy***
5. How to Set Up a Claude Project that Answers Questions about Your Class
6. Chart your data in conversation with Claude before you commit to a reading — *For: Someone about to present a data finding*
7. Map your lit review mid-conversation to surface the underlying debate — *For: **Graduate students or researchers***
8. Map your understanding and build lessons from the gaps
9. Turn research into presentations

Nine items. The **number one pick** is written for an analyst. Number 4 tells me in its own
skip line it is for instructors. Numbers 2 and 7 name graduate students and researchers.
Number 6 is a data-analyst page.

I am an undergraduate with an essay due. At the top level of my own role, roughly half of
what I am given is somebody else's job. The role filter does not fail at level 1 — it
fails at level 3, where there is nothing left to hide behind.

Across all 77 cards tagged `a student`: 61 are badged **Skimmed**, 16 **Read by AI**, none
**Read in full**. So 79% of my shelf is material where, in the site's own words, "We read
the outline or a free sample. We have not seen the whole thing."

---

## 4. Paths

`https://mojtaba-alehosseini.github.io/learn-claude/paths.html` — 7 paths. Two say they
are for me:

- **"Your first week with Claude"** — "For not a coder, a student, a teacher, running a
  business". 6 steps, about 4 hours, free. This is the start. Fine if I have never opened
  Claude.
- **"Using Claude for research without embarrassing yourself"** — "For a researcher, a
  student". 5 steps, about 2 hours, **"some paid steps"**.

So yes, there is one route above beginner. I followed it
(`paths.html?id=research-with-claude`) and it is not for me:

- The description is "Researchers and academics who want the speed without the retraction."
  I do not have retractions. I have a deadline.
- **Step 3** is "Claude AI and Literature Reviews: An Experiment in Utility and Ethical
  Use", Johns Hopkins University Press, `Library Trends 73(3):355-380`, chipped **"pay
  once"** with no price anywhere. That is a paywalled journal article. Step 3 of 5 is a
  wall for anybody without institutional access, and the path never says how much.
- **Step 5** is "ICMJE Recommendations — Use of AI in Publishing" — the International
  Committee of Medical Journal Editors. "Before you submit anything, read what the ICMJE
  expects you to declare." I am not submitting to a medical journal.

Between "you have just opened Claude" and "you are about to publish", there is nothing.
For an undergraduate mid-degree — the exact person the role chip names — there is no path.

No path shows a level. The cards say "For a researcher, a student" and nothing about how
much Claude you need to know first.

---

## 5. The card and the resource page

I opened three resource pages.

**`resource.html?id=r-6bdd922cd9` — "Claude for Education Is Made for Learning"**, the
number one pick for a student who has never used Claude. The page is well built: summary,
"What it teaches" as three verbs, "Who it's for", "Skip it if", "How we checked this one",
dates, "Open on University of Pittsburgh", "Copy link".

Then, halfway down:

> **Before this**
> — Access to an educational Claude account

That prerequisite is **not on the Browse card**. The card shows the badge, title, source,
`article`, `15 min`, `free`, the For: line, the Skip if: line and the dates. Nothing about
needing a Claude for Education account. And the Skip if: line does not mention it either —
it says "You already build Projects and write structured prompts. Nothing here goes past
the basics, and the Pitt login references will not apply to you."

My university may not have a Claude for Education licence. If it does not, the site's top
recommendation for me is unusable, and the only place that says so is a line I have to
click through to find. That is the opposite of "we say when to skip".

**`resource.html?id=r-57225bbae4` — "Documenting Your AI Use"**, St. Catherine University
Library. "four ways to save your prompt log so you can prove your process, and why shared
chat links are unreliable evidence." I would click through to this immediately. This is the
page I came for.

**`resource.html?id=r-9f181deca1` — "Anthropic Claude for Absolute Beginners"**, Udemy.
Chip says **"pay once"**. There is no price on the card and no price on the resource page.
Compare "Academic Research with Claude (live seminar)", which shows two chips — "pay once"
and "from $995". Two paid-once rows in my role; one tells me the price, one does not. I
will not click a Udemy link to find out what it costs.

Would I click through? To Pitt, Tulane, St. Catherine, Warwick, Northeastern — yes,
immediately. To the two paid rows — no.

---

## 6. Search, in my words

Typed into the home box ("Or describe what you want to do…") and the Browse search.

| # | what I typed | top 3 I was shown | verdict | why |
|---|---|---|---|---|
| 1 | will my professor know i used claude for my essay | 1. Documenting Your AI Use (St. Catherine University Library) 2. Generative AI and Academic Integrity (CSU Northridge) 3. Claude for Education Is Made for Learning (Univ. of Pittsburgh) | ok | #1 is exactly the defensive record I want. 20 results. But the one page in the catalogue actually about AI detection — "Guidance on AI detection, and why we're disabling Turnitin's AI detector" — is not in the 20 at all. |
| 2 | how do i cite claude in my apa reference list | 1. Referencing AI and Acknowledging AI Use (University of Warwick Library) 2. Documenting Your AI Use (St. Catherine) 3. AI & Academic Integrity (Cornell) | ok | #1 and #2 both do citation formats. #2's own page names "APA, MLA and Chicago 18th". Best result of the five. |
| 3 | is claude free for students | 1. AI Fluency for students (Anthropic Academy) 2. Day of AI - free K-12 AI literacy curriculum (MIT RAISE) 3. Claude for Teachers: your data and our terms (Claude Help Center) | bad | 34 results, none of the top three says what Claude costs. #2 is a K-12 school curriculum, #3 is for teachers. "Choose a Claude plan (Help Center)" — the page that answers this — is **17th of 34**. The word "free" matched "free K-12" in a title. |
| 4 | i want claude to explain my lecture notes not write the essay for me | 1. AI-Powered Flashcards with Claude Projects (Northeastern) 2. Create custom course materials (Anthropic Academy) 3. Claude for Education Is Made for Learning (Pittsburgh) | ok | #1 and #3 are usable — #3's summary names "the exact click path to turn on Learning Mode". But "Using Claude Learning Mode to Study" — the single card that is about Claude teaching instead of answering — is **absent from all 28 results**, and #2 is a page for teachers building course material. |
| 5 | can claude help me revise for an exam without doing it for me | 1. How to Use AI to Help You Prepare for Quizzes and Exams (Northeastern) 2. Using Claude Cowork for your small business (Anthropic Academy) 3. Using Claude Learning Mode to Study (Northeastern) | ok | #1 and #3 are precisely right. #2 is a small-business page sitting at rank 2 of an exam-revision query in a 12-result set. |

**Same question, two ways.** I asked the thing I actually care about twice:

- "**will my professor know i used claude for my essay**" → 20 results. Top three:
  Documenting Your AI Use / Generative AI and Academic Integrity / Claude for Education Is
  Made for Learning.
- "**can my university detect ai writing in my assignment**" → 23 results. Top three: Using
  AI in university / Claude for Education at Northumbria / The AI Assessment Scale (AIAS).

**The site did not agree with itself.** Zero overlap in the top three. "Documenting Your AI
Use" is #1 in one wording and #10 in the other. The Turnitin/AI-detection page — the
literal answer — is missing entirely from the first wording and #9 in the second. The
second wording's #3, "The AI Assessment Scale (AIAS)", is a framework for staff setting
assessment policy.

---

## 7. On a phone

I set the viewport to 375 x 812.

Good:

- Home: `document.scrollWidth` 375, `clientWidth` 375. No sideways scroll.
- Browse: same, no sideways scroll. The filter rail collapses into one "Filters" button
  pinned to the bottom of the screen. The applied chips ("a student ×", "never used Claude
  ×") stay visible under the sort control.
- Every button and link is at least 44 px tall except the "Learn Claude" logo (40 px).

Bad:

- **The badge on every card is a mouse tooltip.** The badge markup is
  `<span class="badge badge-ai-reviewed" title="AI read all of it. No person has checked
  the notes yet.">Read by AI</span>`. On a phone there is no hover, so there is no way to
  find out what "Read by AI", "Skimmed" or "Found only" means from the card. The four
  definitions do exist on the page, inside `<div class="visually-hidden">` — screen
  readers get them, my eyes do not. The "How well checked" filter that carries the same
  four words is hidden behind "More filters +", collapsed by default, and lists them with
  no definitions either. The only sighted route is to leave Browse and read
  `how-we-check.html`, or to open a resource page.
- **"browse everything" on a phone is a wall.** `browse.html` with no filters renders all
  588 cards into one document. I measured `document.scrollHeight` = **321,320 px**. At
  812 px of phone screen that is **396 screens**. There is no pagination and no "load
  more". The empty-state message for my own level-4 cell ends with "or browse everything."
  — pointing me straight at it.

---

## 8. What changed since Attack 2 — my verdict on each

**Does the level filter return people like me or people much further along?**
At level 1 and 2, people like me. At level 3 (9 items), no. The #1 pick's own For: line
says "Any analyst". Two more name "Graduate students or researchers" and "Academics and
research students". One says in its skip line it is "written primarily for instructors to
deploy". Rule B reads the `who_for` line only, so a card whose `who_for` was widened to
mention a student keeps the tag while its `skip_if` still says it is for teachers. Two
examples, both live:

- "AI feedback customized for student writers: the updated PAIRR prompts" — *For:
  Instructors and students…* / *Skip if: … written primarily for instructors to deploy.*
- "Peer and AI Review of Student Writing with Marit MacArthur and Anna Mills" — *For: A
  student who wants to understand why their instructors are structuring AI use the way
  they are…* / *Skip if: … This is a conversation aimed at teachers about course design,
  and there is nothing to do afterwards.*

A card that tells me there is nothing for me to do afterwards should not be in my list.

**Do the stripped `listed` cards read as honest or broken?**
Honest in wording, broken in shape, and over-claiming on one point. All three
(`browse.html?checked=listed`) read:

> Skip if: You want something we have read. We have not opened this one yet.

No "For:" line at all, where every other card has one. But they still print a format, a
length and a cost. "Head of Claude Code: What happens after coding is solved (Boris
Cherny)" is labelled `podcast · half a day · subscription`. You cannot know it takes half a
day if you have not opened it. Say you have not read it, then do not tell me how long it
takes.

**Can I find out what the "how well checked" badge on a card means?**
Not from the card, and not with a finger. See section 7. The resource page does it
properly — "Read by AI. AI read all of it. No person has checked the notes yet. How we
check." — but that is one click away and a phone user has no reason to think the badge is
explainable at all.

**Do the date lines make the site look maintained or abandoned?**
Maintained. Of my 77 student cards, 50 say "Checked 5 Sep 2026" — yesterday. Seven carry
"over a year ago, may not match Claude today", which is the note working exactly as it
should. Fifty-five of 77 say "No publish date given"; that is a lot of blank, but the site
says up front on `how-we-check.html` why, and I would rather have a blank than a guess.
This one is a pass.

**Are the prices on the paid rows clear before I click?**
No, and inconsistently so. Same role, same list: "Academic Research with Claude (live
seminar)" shows `pay once` **and** `from $995`; "Anthropic Claude for Absolute Beginners"
(Udemy) shows `pay once` and no number, on the card and on its resource page. A site whose
whole promise is "do not waste your time" makes me leave the site to find a price.

**Does naming one person and Claude as "we" raise or lower my trust?**
Raises it, clearly. "One person makes this site - a researcher at the Technical University
of Denmark, working on it outside their job… The reading is done by Claude… A person sets
the rules… and has not yet read a single resource end to end, which is why the strongest
label has the count you can see above it." Nobody lies like that. It also tells me what I
am buying: 61 of my 77 cards are "Skimmed" and none is "Read in full". I would rather know.

**The thin-level offer / empty cell.** Makes sense, and I took it. Broken only in that it
strips the picks block (section 2).

**The picks block.** The reasons are the best writing on the site — except one, which is
the worst. See section 9.

**Share a link.** Broken. See section 10, finding 3.

**The home attract loop.** Running, and broken. See section 1.

**The sort control.** Broken. See section 10, finding 4.

**Paths above beginner level.** One exists and it is not for an undergraduate. Section 4.

---

## 9. Content quality — the three worst entries I was shown, quoted

**1. The pick reason on "Reduce hallucinations"** —
`browse.html?role=student&level=confident`, position 1 under "Start with these three".
This is the first sentence a student at my level reads:

> Held back on 2026-09-04 only because it is step 1 of the research path and would have
> displaced something no path carries. Rule B removed that something from this pool on
> 2026-09-06, so the objection lapsed and the verification slot was empty - and this is the
> only candidate here anybody has read in full.

That is a maintainer's changelog, printed to a visitor. "Rule B", "the objection lapsed",
"the verification slot" mean nothing to me. Worse, it says "anybody has read in full" while
the card's own badge says **Read by AI** and `how-we-check.html` says "Today the count read
in full is zero". The site contradicts itself in two places I can see at the same time. And
the card it is selling opens *For: Any analyst worried about confidently-wrong output.*

**2. "Turn research into presentations"** — Anthropic Academy, in my level-3 list:

> Skip if: Needs the actual research paper, data files and assignment rubric uploaded - the
> Canva connector it names is worth double-checking yourself since it's the only appearance
> of a non-Anthropic design tool **in this whole harvest**.

"This whole harvest" is the project's own back-office word. I do not know what a harvest is.
And the line is not a skip condition — it is a caveat wearing a "Skip if:" label. Same
pattern on two neighbours: "Skip if: Teaches epistemic caution, not a finished analysis…"
and "Skip if: Names Claude Opus 4.6 with Extended Thinking specifically for the diagnostic
precision it needs…". Neither tells me when to skip. The `Skip if:` line is the site's one
promise on the home page; on the Anthropic Academy rows it has quietly become a notes field.

**3. "Lesson 1: Introduction to AI Fluency | AI Fluency: Framework & Foundations Course |"**
— in `browse.html?role=student&level=never-used`. The title ends with a stray pipe
character. It is a raw page title with the site name half-stripped off. It is published as
the card's headline, and it sits next to "Published 12 Jun 2025 · over a year ago, may not
match Claude today". A card that looks copy-pasted and is flagged stale is not a card that
persuades me the notes above it were written with care.

---

## 10. Everything that is broken, ranked (evidence for each)

**1. The role filter puts other people's jobs at the top of my level.**
URL: `browse.html?role=student&level=confident`. I clicked a student, then used it a lot.
Saw: 9 results; #1 "Reduce hallucinations" reads *"For: Any analyst worried about
confidently-wrong output."*; #4 "AI feedback customized for student writers" reads *"Skip
if: … written primarily for instructors to deploy."*; #7 reads *"For: Graduate students or
researchers…"*. Expected: nine things for an undergraduate. Harms: any student who gets
past the beginner shelf, which is the whole point of picking a level. At level 3 there is
no volume to hide the misses.

**2. The top recommendation for a beginner hides its prerequisite on another page.**
URL: card in `browse.html?role=student&level=never-used`, then
`resource.html?id=r-6bdd922cd9`. I read the card, then opened the page. Saw: the card
carries no prerequisite; the resource page carries *"Before this — Access to an educational
Claude account."* Expected: the requirement on the card, or in the Skip if: line. Harms:
every student whose university has no Claude for Education licence — they are sent to the
number-one pick and hit a login.

**3. Every shared link previews as a generic label.**
URLs: `browse.html?role=student&level=never-used`, `resource.html?id=r-57225bbae4`,
`paths.html?id=research-with-claude`. I read the meta tags on each. Saw: browser tab titles
are correct and specific ("Browse 42 Claude resources — Learn Claude", "Documenting Your AI
Use — Learn Claude"), but `og:title` is the same static string for the whole page type —
`"Browse — Learn Claude"`, `"Resource — Learn Claude"`, `"Paths — Learn Claude"` — and
`og:description` is a fixed sentence about filtering. Expected: the preview to say what I
sent. Harms: this site spreads by one student sending a link to a course group chat. What
lands in the chat is "Resource — Learn Claude" and a sentence about filters. Nobody clicks
that. Only the home page has a real `og:title`.

**4. "Newest first" is not newest first, and it ignores every `Updated` date.**
URL: `browse.html?role=student&level=never-used&sort=newest`. I changed Sort from "Best
checked first" to "Newest first" and read the order. Saw: the three pinned picks stay on
top, so card 1 is "Claude for Education Is Made for Learning" (Published 10 Dec 2025) and
cards 2 and 3 say "No publish date given", while card 4 is Published 13 Jul 2026. Inside
the sorted list, "Lesson 1: Introduction to AI Fluency" (Published 12 Jun 2025 · over a
year ago) is ranked **above** "Get started with Claude" (Updated 2 Jun 2026) and above "AI
Student Research Guide: Prompt Engineering" (Updated 31 Aug 2026). Expected: newest means
newest. Harms: I picked that sort because Claude changes fast and I want current material;
it hands me a year-old flagged-stale video above something updated last week. With 442 of
588 rows carrying no publish date (STATUS.md), most of the catalogue falls into an
unordered tail under a label that promises an order.

**5. The badge on a card cannot be read on a phone.**
URL: any card on `browse.html`. I set the viewport to 375 x 812 and looked for a definition
of "Skimmed". Saw: the definition exists only as `title="…"` (mouse hover) and inside
`<div class="visually-hidden">` (screen readers). The "How well checked" filter is
collapsed behind "More filters +" and lists the four labels with no definitions. Expected:
a tap or a visible line. Harms: 61 of the 77 cards in my role say "Skimmed", and on a phone
I cannot find out that "Skimmed" means "We read the outline or a free sample. We have not
seen the whole thing." A quality label nobody can read is not a quality label.

**6. Search does not agree with itself about the same question.**
URLs: `browse.html?q=will+my+professor+know+i+used+claude+for+my+essay` (20 results) and
`browse.html?q=can+my+university+detect+ai+writing+in+my+assignment` (23 results). I typed
the same worry two ways. Saw: no overlap in the top three; "Documenting Your AI Use" is #1
in one and #10 in the other; the Turnitin/AI-detection page is absent from the first and #9
in the second. Expected: the same worry, the same answers. Harms: the single most common
question a student brings to this site is answered by which words they happened to use.

**7. Maintainer jargon and internal vocabulary are printed on public cards.**
URLs: `browse.html?role=student&level=confident`. Saw: "Rule B removed that something from
this pool on 2026-09-06, so the objection lapsed and the verification slot was empty";
"…the only appearance of a non-Anthropic design tool in this whole harvest". Expected:
reasons written to me. Harms: the picks block is the site's flagship, and its first pick at
my level opens with a build log.

**8. A price chip on one paid row and not the other.**
URLs: `browse.html?role=student`, `resource.html?id=r-9f181deca1`. Saw: "Academic Research
with Claude (live seminar)" carries `pay once` + `from $995`; "Anthropic Claude for
Absolute Beginners" (Udemy) carries `pay once` with no number anywhere on the card or the
resource page. Expected: a number, or "price not checked". Harms: a student who will not
pay has to open Udemy to learn that they will not pay.

**9. The home page's attract loop lights a chip and never fills the sentence.**
URL: home. I watched for 21 seconds without touching anything and sampled every 700 ms.
Saw: `data-showing` moves through all ten role chips (running a business → a writer → not a
coder → a student → a researcher → a teacher → a developer → working with data → a product
manager) while the headline stays "I'm a [role] and I've [level]." on every sample.
Expected: the sentence to fill in, since that is the only thing the loop could be for.
Harms: first-time visitors, in the first ten seconds. It looks like a rendering fault.

**10. `listed` cards state a length and a cost for something nobody opened.**
URL: `browse.html?checked=listed`. Saw: "Head of Claude Code: What happens after coding is
solved (Boris Cherny)" — `podcast · half a day · subscription` — beside "Skip if: You want
something we have read. We have not opened this one yet." Expected: no duration claim.
Harms: small — three rows — but it undercuts the one thing these cards were stripped to
protect, which is not claiming knowledge you do not have.

**11. The empty-cell offer removes the ranking the site says I need.**
URL: `browse.html?role=student&level=builder`, then the "Add "used it a lot" too" button →
`browse.html?role=student&level=builder%2Cconfident`. Saw: the destination has no "Start
with these three" heading; `browse.html?role=student&level=confident` does. Expected: the
picks to survive. Harms: the offer is made to the one cell that has nothing, and it hands
back an unranked list.

**12. "0 resources match so far." with an enabled "Show me".**
URL: home, a student + built things with it. Saw: the count line, and a live submit button.
Expected: the sentence not to say "so far", and the button to say where it is sending me.
Harms: minor. The Browse page recovers it well.

---

## 11. The one thing that would make me leave and not come back

The search disagreeing with itself about whether my professor can tell.

That is the question I came with. I asked it twice, in two ordinary English wordings, and
got two different sets of top results with nothing in common — and the one page in the
catalogue actually about AI detectors did not appear at all in the first wording. If a site
whose whole pitch is "find what's worth your time" cannot give me the same answer to the
same question twice, then everything else it says it has checked is a coin flip too. I would
go back to asking a friend.

---

## 12. What is genuinely good (honest, brief)

- **The `Skip if:` line, where it is written properly.** "You have no course files to
  upload, or you revise better by making cards yourself. Card-making is itself retrieval
  practice, and this hands that step to a machine." No other directory tells me the cost of
  taking its own advice.
- **The picks for a beginner student.** Pitt, Claude 101 and the Tulane integrity guide,
  with the reason "The only candidate that answers the question a student has before any
  tool question - where the line is". Correct, and correctly ordered.
- **"Who 'we' is" on `how-we-check.html`.** Naming one person, naming Claude as the reader,
  and saying "has not yet read a single resource end to end" raises my trust more than any
  badge could. Do not soften this.
- **The empty cell tells the truth.** "We have nothing for this combination yet. It's on the
  list. The level below has 9." Most sites would show me nine wrong things instead.
- **No accounts, no tracking, no progress bar.** "We do not track your progress. Nothing
  here needs an account." Good.
- **It is fast, and it works on a phone** — no sideways scroll, 44 px targets, filters that
  collapse sensibly.

---

## 13. Would I come back, and what one thing would make me?

Yes, once — for the integrity stuff. "Documenting Your AI Use" and the Tulane page are
genuinely the best things I have found on how to not get accused, and I would come back to
re-read them and to send them to two people on my course. That is real.

But I would not come back to *learn Claude* here, because the level ladder runs out. At
"used it a lot" I get nine things and half of them are for analysts, instructors and PhD
students, and the only path above beginner ends at medical-journal publishing rules. The
site knows how to talk to me on day one and has nothing to say to me in week three.

The one thing that would make me come back: **make the shelf at "used it a lot" actually be
for a student.** Nine items, and I would keep coming back if all nine were written for
somebody with an essay due instead of somebody with a paper to publish. If the honest
answer is that the material does not exist, say that on the page the way the empty cell
does — "we have three for you at this level and here is why" — because I would trust that
more than nine items where four are somebody else's.

And fix the link preview. I was going to send this to my group chat and the preview said
"Resource — Learn Claude". I did not send it.

---

## Checklist
- [x] I opened the live site
- [x] I tried all four levels
- [x] I quoted at least 5 real titles or lines from the site
- [x] Every number I used is in 00-facts.md, STATUS.md, or quoted from the site
- [x] I looked at a phone width
- [x] I read no file under scripts/ or data/
- [x] I found at least one thing nobody has mentioned before
