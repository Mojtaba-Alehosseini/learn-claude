# Attack: a student
Written as someone who is a student, at 2026-08-27. Site version: 22e4532.

I have an essay due. I have one hour. I want to know three things: am I allowed to use
Claude, how do I cite it, and does it cost me money. That is the whole job.

Where a number is not in `00-facts.md`, the command that produced it is printed next to
it. Everything I quote is copied from the live site or from
`python docs/attack/role-view.py`, which prints the same cards in the same order.

---

## 1. The first 60 seconds

I land on a big sentence: **"I'm a [role] and I've [level]."** Both blanks are
underlined in orange. A drawing of a coffee mug cycles on the right. Under the sentence
there is a row of ten chips. I press **"a student"**. The counter says
**"41 resources match so far."**

That is a good sixty seconds. It is the only good sixty seconds in this report.

Under the sentence there is also a field: **"Or describe what you want to do…"**. That
is the box I actually want, because my question is a sentence, not a category. I will
come back to it in section 6. It does not work.

---

## 2. Does the front door work for me (all four levels, with counts)

I clicked all four level chips on the live site and read `#tally` after each one.

| I've… | tally on screen | 00-facts |
|---|---|---|
| never used Claude | "20 resources match so far." | 20 |
| used it a little | "15 resources match so far." | 15 |
| used it a lot | "6 resources match so far." | 6 |
| built things with it | **"0 resources match so far."** | 0 |

The counts are honest. Three problems.

**a) The chooser closes itself and does not tell you it has.** The moment I picked my
level, both chip rows vanished. I clicked where "used it a lot" had been and hit empty
page. Nothing happened, and nothing told me nothing had happened. To change my level I
have to work out that the words *in the sentence* are buttons. I only found that because
I went looking. On a normal visit I would have used the browser Back button.

**b) The search field disappears at the same moment.** `index.html` collapses
`.search-row .input` to `max-width: 0; visibility: hidden` once both blanks are filled.
I confirmed it live: with role set and no level, `getComputedStyle(q).visibility` is
`visible`; after picking a level the field is gone. So the site takes away the "describe
what you want" box precisely when I have told it who I am. The one moment it knows most
about me is the moment it offers me least.

**c) 0 results is presented exactly like 41 results.** At `builder` the tally reads "0
resources match so far.", the "Show me" button stays orange and enabled, and the drawing
is a warm stack of books with a seedling growing out of it. I pressed it. I got:

> **Nothing matches all of those.**
> Try removing one filter — time is usually the one to loosen.

I never set a time filter. There is no time filter to loosen. The site told me to undo
something I never did. The correct sentence is "we have nothing for a student who builds
things" and the code can already produce it — `browse.js:194` has a
"We have not covered this role yet." branch, but it is gated on `!anyOtherThanRole()`,
and `level` counts as an "other", so a role+level dead end can never reach it.

---

## 3. What the catalogue actually gives me (are these really for me?)

41 resources. Format mix from `00-facts.md`: docs 15, video 13, article 9, course 2,
podcast 2, repo 0, hands-on 0.

**Docs is my biggest format at 15 of 41, and that is the wrong shape for a student.**
Zero hands-on. Zero repos. Two courses. A student with a deadline needs to *do* a thing;
this hands me library web pages to read.

And most of those docs are somebody else's university. From my own count:

```
python -c "... re.search(r'not at |-only|specific|Pitt login|no Claude for Education licence|behind institutional login|internal wikis', i['skip_if'])"
-> STUDENT items whose Skip if names one institution: 9 of 41
```

Real examples, verbatim from Browse:

> **Claude Enterprise at Syracuse University** — Skip if: You are not at Syracuse. Half
> the links go to internal wikis and sign-up forms you cannot open.

> **AI for Students** (Monash) — Skip if: You are not at Monash. The module and the unit
> are both behind institutional login, so all you get is the shape of the curriculum.

I am not at Syracuse. I am not at Monash. Nine of my forty-one cards are somebody else's
intranet.

**Does the catalogue speak to academic honesty? Yes — and it hides it.** I checked the
`topics` field:

```
python -c "collections.Counter(t for i in student_items for t in i['topics'])"
-> [('chat-prompting', 27), ('safety', 17), ('cowork', 3), ('skills', 3),
    ('claude-code', 2), ('mcp', 1), ('agents', 1)]
```

17 of my 41 carry the `safety` topic, and when I listed them they are almost all the
integrity material — Plagiarism and Academic Integrity 101, Acknowledging AI tools and
technologies, Referencing AI and Acknowledging AI Use, Documenting Your AI Use,
Disclosing the Use of AI, Generative AI and Academic Integrity. Good content. It exists.

But `ui.js:41` labels that topic **"limits and safety"** in the filter list. I am
worried about getting reported to an academic integrity panel. I am not going to click
"limits and safety" — that reads like AI guardrails and model refusals. The best answer
to my actual question is behind a label written for a different reader.

**Cost. The thing I care about most, and the catalogue is silent.** All 41 are `free`
(35) or `free-account` (6) — the six are Coursera AI Fluency, AI Fluency for students,
Use Claude for Education at your university, and three Northeastern guides. Nothing is
`paid-once` or `subscription`. That sounds great until you notice what it means: the
site is telling me the *page* is free. It is not telling me whether *Claude* is free.

```
python -c "re.search(r'pricing|price|subscription|pro plan|costs?|pay', title+summary) for student items"
-> (no output)
```

Zero of my 41 mention price, pricing, cost, subscription or paying, in title or summary.
The catalogue does have the page that answers it — **Plans & Pricing**, claude.com/pricing
— and its own `who_for` says *"Anyone comparing plans before buying."* It is tagged
`roles: ['business-founder']`. Only. A student cannot see it.

Anyone. Except me.

**Two cards in my list are not for me at all**, and their own text says so:

> **What is Claude Code?** (rank 11 of my 20 never-used cards)
> For: Developers about to install Claude Code who want the mental model before the
> first command.

> **Kris Puckett - Becoming an AI-native designer (Dive Club)** (rank 5 of my 6
> "used it a lot" cards)
> For: Designers wanting a deep, honest look at an AI-native design practice.

One in six of my top-level cards is a design podcast that tells me on its own page that
I need "intermediate design experience".

**And a course with my job title in the name is hidden from me.** There are two entries
called "AI Fluency for Student(s)":

```
python -c "print title, roles for titles starting 'ai fluency for student'"
AI Fluency for Students | roles ['researcher'] | Coursera
AI Fluency for students | roles ['student','teacher'] | Anthropic Academy
```

A Coursera course literally titled **"AI Fluency for Students"** is tagged for
researchers and not for students. It is not in my 41.

---

## 4. Paths

Two of the three paths name me. Neither works.

**First: the Paths page never says which one is mine.** I chose "a student" on the front
door. I click Paths in the nav. My answer is thrown away. Three paths, three
descriptions, no role labels, no filter, no highlight. The middle one is for developers.
I have to read all three and guess. The site knows the answer — `data/paths.json` has a
`roles` array on every path — and it does not print it.

**Second, and this is the finding that ends the section.** I checked every step in both
of my paths against the role tags in `data/items.json`:

```
python -c "for each path naming student, count steps where 'student' in item['roles']"

PATH: Your first week with Claude | cost label: free
  step 1 [not student] Claude is not one tool. It's six.      roles=non-technical
  step 2 [not student] Get started with Claude                roles=non-technical
  step 3 [not student] Claude 101                             roles=business-founder,data-analyst,non-technical,researcher,writer-marketer
  step 4 [not student] What are Projects?                     roles=researcher
  step 5 [not student] Why do AI models hallucinate?          roles=non-technical
  step 6 [not student] Get started with Claude Cowork         roles=business-founder,non-technical
  -> 0 of 6 steps are tagged for student

PATH: Using Claude for research without embarrassing yourself | cost label: some paid steps
  step 1 [not student] Reduce hallucinations                  roles=data-analyst
  step 2 [not student] What are Projects?                     roles=researcher
  step 3 [not student] Claude AI and Literature Reviews...    roles=researcher
  step 4 [not student] Connect ... Zotero library with Cowork roles=researcher
  step 5 [not student] ICMJE Recommendations — Use of AI...   roles=researcher
  -> 0 of 5 steps are tagged for student
```

**Zero out of eleven.** Every single step in both of my paths is a resource the site's
own catalogue says is for somebody else. If I browse as a student I will never see one
of them. The paths and the catalogue are two different products wearing the same name.

For contrast, same command, other roles:

```
Your first week with Claude:   non-technical 5/6 · business-founder 2/6 · teacher 0/6 · student 0/6
Getting good at Claude Code:   developer 6/6
Using Claude for research:     researcher 4/5 · student 0/5
```

Developers get 6/6. Researchers get 4/5. I am the only role on the site that gets 0/N on
**both** of its paths.

**Third: the paid steps.** The research path header says "5 steps · about 2 hours ·
some paid steps". It does not say which. I had to open the path and read all five.

- **Step 3 — "Claude AI and Literature Reviews: An Experiment in Utility and Ethical
  Use"**, publisher shown as **"Jhu"**, chips: `article · one hour · pay once`. It is a
  Project MUSE journal article. The site does not say the price. It also carries
  "Published over a year ago — may not match Claude today". So the one thing I am asked
  to pay for is also the one thing flagged as out of date. As a student, that is an
  instant no. I will find it through my library or not at all — and the site, which is
  written for people at universities, never mentions that a library exists.

- **Step 2 — "What are Projects?"** is `free, sign-up needed`.

- **Step 4 — "Connect and integrate your local Zotero library with Claude Cowork"** is
  tagged **free**. Cowork needs a paid Claude plan. The site knows this: another card in
  *my own list* says so in its Skip if — *"if you are still deciding whether to pay for
  Claude - Cowork requires a paid plan."* So step 4 is not free either, and the path does
  not say so.

Then, printed by `paths.js` at the bottom of that same page, directly under a step
labelled "pay once":

> **We do not track your progress. Nothing here needs an account.**

Step 2 needs an account. Step 3 needs a credit card. Step 4 needs a subscription.

**Fourth: the research path is not written for me.** Its own subtitle is "Researchers and
academics who want the speed without the retraction." Step 5 is the ICMJE recommendations
— rules for submitting to medical journals. I have an essay due on Thursday. I am not
submitting to a journal. Nothing in this path is about coursework, and nothing in it is
about my department's rules, which is the only rulebook that can actually get me in
trouble.

---

## 5. The card and the resource page

The card layout is genuinely good: badge, title, publisher, three chips, **For:**,
**Skip if:**, checked date, published date. It is more honest than any other directory
I have used. Two things ruin it.

**The publisher line is a chopped-up domain name.** Screenshot from Browse, my
never-used list:

> **Acknowledging AI tools and technologies**
> Au · Academic Skills, University of Melbourne

> **AI Student Research Guide: Prompt Engineering**
> Libguides · Westmoreland County Community College Library

"Au". "Libguides". Counted:

```
python -c "count student items whose source is a domain fragment or a hosting platform"
-> 11 of 41
   Ac   -> Claude for Education at Northumbria        (www.northumbria.ac.uk)
   Syr  -> Claude Enterprise at Syracuse University   (its.syr.edu)
   Au   -> Acknowledging AI tools and technologies    (students.unimelb.edu.au)
   Au   -> Using AI in university                     (www.unsw.edu.au)
   Libguides -> Referencing AI and Acknowledging AI Use   (warwick.libguides.com)
   Libguides -> AI Student Research Guide             (westmoreland.libguides.com)
   Stkate -> Documenting Your AI Use                  (libguides.stkate.edu)
   Csun -> Generative AI and Academic Integrity       (libguides.csun.edu)
   Studentguidetoai -> 2026 Student Guide to AI       (studentguidetoai.org)
   Substack -> AI feedback customized for student writers
   Buzzsprout -> Peer and AI Review of Student Writing
```

Two different Australian universities both show as "Au". Two unrelated institutions both
show as "Libguides". The comment above the function that renders this
(`ui.js:125-127`) says: *"Named because it is the publisher, not the platform"* — and
then ships "Substack" and "Buzzsprout", which are platforms.

I am about to cite an academic-integrity page in an argument with my tutor. "Who says
this" is the entire question. The site answers "Au".

**The resource page makes it worse, because it puts the fragment on the button.** I
opened `resource.html?id=r-57225bbae4` (Documenting Your AI Use). The single orange
call-to-action reads:

> **Open on Stkate**

And the footer line reads "Found through Stkate". That is St. Catherine University. The
real name is sitting right there in the `author` field. It is used everywhere except the
button.

The rest of that page is fine and I would click through. "What it teaches" is two
bullets — *"format ai citation references for apa mla and chicago styles"*, *"save prompt
logs to create a defensible audit trail"* — which is exactly my question, written in
lower case with APA and MLA uncapitalised, like a database row that escaped.

I also opened `resource.html?id=r-16c564ede1` — **Claude for higher education**. It says:

> **Found only.** We found it and sorted it. Nobody has looked at the content yet.

and four lines above that:

> **Skip it if:** You already have access, or you want to be taught something. This is a
> sales page and it teaches nothing about using Claude well.

Somebody clearly looked at it — enough to call it a sales page. Both sentences cannot be
true. And a directory whose stated job is judgment should not be carrying an entry whose
own judgment is "it teaches nothing".

That is not one bad entry. Every `listed` item does this:

```
python -c "listed-tier items and how many carry a written Skip if"
-> site-wide listed: 43, with a Skip if: 43
-> student listed: 11, with a Skip if: 11
```

43 of 43 cards tell me nobody has looked at the content, then tell me what they think of
the content.

There is no "next", no "related", and no "back to my path" on a resource page. It is a
dead end. On a phone, going back means the browser Back button and a lost scroll
position.

---

## 6. Search, in my words

I typed three real sentences. This is the worst thing on the site.

**Test 1, on the live site.** `browse.html?role=student&q=how do I cite Claude`

```
on load:              "0 resources for a student"   indexReady=false   indexScriptTags=0
after one keystroke:  "3 resources for a student"   indexReady=true
                      Referencing AI and Acknowledging AI Use
                      Documenting Your AI Use
                      Acknowledging AI tools and technologies
```

Zero on arrival. Three after I touch a key. The three correct answers to my question
exist in the catalogue and the site showed me none of them.

**Test 2.** `browse.html?q=can I use this for my essay without cheating`

```
on load:              "0 resources"                 indexReady=false   indexScriptTags=0
after one keystroke:  "7 resources"
                      Using AI for Writing Feedback
                      Generative AI and Academic Integrity
                      Claude for Education Is Made for Learning
                      Acknowledging AI tools and technologies
```

Same seven, in the same order, that `python scripts/test-search.py "can I use this for
my essay without cheating"` predicts.

**The cause, in the source.** `search.js:41` — *"Loaded on the first keystroke rather
than with the page."* `browse.js:335-337` boots with `readURL(); render();` and never
calls `LCSearch.load()`. So a query that arrives in the URL never loads the index.
`rank()` returns `null`, and `browse.js:87-88` falls back to plain substring AND-matching
across title + summary + who_for + source. "cite" is in none of them. Zero results.

The only way to get to Browse with a `?q=` in the URL **is the front page search box**.
So the site's headline feature — the box that says "Or describe what you want to do…" —
is dead on arrival, one hundred per cent of the time, for every visitor who uses it.

**What it says to me when it fails:**

> **No match for "is claude free for students".**
> Try fewer words, or browse by role instead.

It blames my words. My words were fine. The index was not loaded.

**And the count line lies about why.** With a role and a query it printed **"0 resources
for a student"** — the wording reserved for a role-only filter, because `anyFilters()`
in `browse.js:66` only looks at the six chip axes and not at `q`. So the screen tells me
the *role* found nothing, when a search is what found nothing. Same bug on the way back
up: "3 resources for a student. Remove a filter to see more." The thing to remove is the
search box, and it is not a filter.

**Test 3, ranking, once the index is loaded.** I ran `scripts/test-search.py` and printed
all hits instead of the top 3:

```
"free tools for students" -> 33 results
     28.5 AI Fluency for students
     28.2 Day of AI - free K-12 AI literacy curriculum (MIT RAISE)
     21.2 A Comprehensive Guide to AI Training for Small Businesses
     ...
     13.4 Plans & Pricing          <- rank 20 of 33

"is claude free for students" -> 32 results
     29.1 AI Fluency for students
     28.5 Day of AI - free K-12 AI literacy curriculum (MIT RAISE)
     19.3 Practical ways to get started using Claude for educators
     ...
     14.0 Plans & Pricing          <- rank 21 of 32
```

I asked, in English, whether Claude is free for students. The second result is a K-12
teacher curriculum. The third is small-business training. The page called **Plans &
Pricing** is twenty-first. Search is not filtered by my role either, so my answer is
buried under material for teachers and founders.

---

## 7. On a phone

Honest note on method: I could not hold the browser at 390px. The Chrome window is shared
with four other agents running at the same time, and every `resize_window` call was
undone before the screenshot — `innerWidth` stayed at 1536 and
`matchMedia('(max-width: 768px)').matches` stayed `false` on three attempts. So this pass
is: the `@media (max-width: 768px)` block in `assets/css/site.css:590-635`, the block in
`index.html`, plus one measurement I took on the live page by constraining the results
column to phone width.

**The measurement.** I set `#results` to 358px wide (390px phone minus the 16px page
padding each side that `.wrap` applies at this breakpoint) and read the card heights on
`browse.html?role=student&level=never-used`:

```js
r.style.width='358px'; cards.map(c => c.getBoundingClientRect().height)
-> {"n":20,"tallest":637,"median":540,"totalPx":10643}
```

20 cards, median 540px tall, 10,643px total. On an 844px-tall phone that is **12.6
screens** of continuous scrolling, with no grouping, no "start here", no way to collapse
a card, and no sub-headings. Every card is the same weight. (Desktop body text is 20px
and mobile is 18px, so the real figure is a little lower — the shape of the problem is
not.)

**What the CSS does at phone width.** `.filter-rail { display: none }`, and a fixed
bottom bar appears with one button. The button's whole label is **"Filters"** — no count,
no indication that two filters are already on. Arriving from the front door with
`role=student&level=never-used`, the only thing telling me I am filtered is the applied
chip row in the main column, above 12 screens of cards. Scroll past it and the bottom bar
says "Filters" as if none are set.

**One thing I could measure that is a phone cost.** The front page cross-fades a drawing
every 2.6 seconds until you choose (`home.js`, `startAttract`). That cycles all ten
never-used PNGs:

```
du -sk assets/icons/roles  ->  1020 KB
per-file: designer 23KB · researcher 21KB · pm 20KB · writer-marketer 20KB · teacher 17KB
          non-technical 16KB · business-founder 12KB · developer 12KB · data-analyst 11KB
          student 10KB
```

162KB of decoration, on mobile data, before I have answered a single question — for an
animation whose stated job in the code comment is "the only hint that the underlined
words are buttons". On a phone the chooser is already open below the sentence, so the
hint is not needed and the drawing has been pushed below it anyway.

---

## 8. Content quality — the three worst entries I was shown, quoted

**1. Kris Puckett - Becoming an AI-native designer (Dive Club)** — card 5 of the 6 I get
at "used it a lot".

> For: Designers wanting a deep, honest look at an AI-native design practice.
> Skip if: You have already read the Cat Wu article — the video covers the same ground,
> and I could not confirm its runtime or publication date.
> Before this: — intermediate design experience

Four failures in one card. It is for designers, not students. It is filed as a
**podcast** and the Skip if calls it "the video". It is chipped **one hour** while
admitting the runtime could not be confirmed. And it is written as "**I** could not
confirm" — the only card in my 41 that breaks into the first person singular when the
whole site says "we". Its hidden `questions` field is *"how are senior designers using
claude code"* and *"how to use claude code for creative coding and shaders"*. This is one
sixth of everything the site offers a confident student.

**2. Claude for higher education** (Anthropic).

> **Found only.** We found it and sorted it. Nobody has looked at the content yet.
> Skip it if: You already have access, or you want to be taught something. This is a
> sales page and it teaches nothing about using Claude well.

A curated directory carrying a vendor sales page, admitting nobody read it, and admitting
it teaches nothing. If the site's own note is "it teaches nothing", the entry is not a
resource. It is filler that makes 41 look bigger than it is.

**3. Claude Enterprise at Syracuse University.**

> **Found only** · Syr · docs · 15 minutes · free · checked 21 Aug 2026 · published UNVERIFIED
> For: A student who wants the prompting fundamentals in one screen, plus links to
> Projects guides and workshop recordings.
> Skip if: You are not at Syracuse. Half the links go to internal wikis and sign-up forms
> you cannot open.

Nobody read it, it has no date, the publisher is "Syr", and by its own admission half of
it is unopenable unless you attend one specific American university. It is one of my
twenty never-used cards.

Runner-up, because it is the funniest: **"Use Claude for Education at your university"**,
whose Skip if reads *"Skip if you want teaching advice; the 'what can I use Claude for'
list is written for students, not for people who set assignments."* That advice is
addressed to a teacher. It is printed on a card in the student list.

---

## 9. Everything that is broken, ranked

Ranked by what it costs me, not by how hard it is to fix.

**9.1 — The front page search box returns zero results, always.**
`browse.html?role=student&q=how do I cite Claude` renders **"0 resources for a student"**
with `window.LCSearch.ready() === false` and zero `search-keywords` script tags in the
document. One `input` event later: **"3 resources for a student"** — Referencing AI and
Acknowledging AI Use, Documenting Your AI Use, Acknowledging AI tools and technologies.
Cause: `search.js:41` loads the index "on the first keystroke"; `browse.js:335-337` boots
`readURL(); render();` and never calls `load()`; `browse.js:87-88` silently degrades to
substring AND-matching. The **only** producer of a `?q=` URL is the front page field.
Verified live twice, on two different sentences.

**9.2 — Both paths that name me contain zero steps tagged for me.**
"Your first week with Claude": 0 of 6. "Using Claude for research without embarrassing
yourself": 0 of 5. Same command on other roles: developer 6/6, non-technical 5/6,
researcher 4/5. I am the only role scoring 0/N on both of its paths. Every one of those
11 resources is invisible in my Browse view of 41.

**9.3 — Nothing in my 41 tells me what Claude costs, and the page that does is reserved
for founders.** Zero of 41 mention price, pricing, cost, subscription or paying in title
or summary. **Plans & Pricing** (claude.com/pricing), `who_for: "Anyone comparing plans
before buying."`, is tagged `roles: ['business-founder']`. Cost is the first question a
student asks and the site has no answer for it.

**9.4 — "Free" on a card does not mean free, and nothing anywhere defines it.**
"Claude Cowork for Academics: Full Setup & Use Cases" is chipped **free** and its own
Skip if says *"if you are still deciding whether to pay for Claude - Cowork requires a
paid plan."* Step 4 of my research path is a Cowork walkthrough, also chipped free. The
`how-we-check.html` page defines all four checking tiers and says nothing at all about
what the cost chips mean.

**9.5 — The publisher name is a chopped domain on 11 of my 41 cards.** "Au" for both
unimelb.edu.au and unsw.edu.au. "Libguides" for both warwick and westmoreland. "Ac",
"Syr", "Csun", "Stkate", plus "Substack" and "Buzzsprout", which are hosting platforms —
directly against the rule stated at `ui.js:125-127`. It reaches the primary button on the
resource page as **"Open on Stkate"**. Site-wide, 36 items have a source of five
characters or fewer.

**9.6 — 16 of my 41 cards render as "Skip if: Skip if …".** The stored text repeats the
label. Screenshotted live, two cards in a row on
`browse.html?role=student&level=never-used&format=video`: *"Skip if: Skip if you want
feature coverage…"* and *"Skip if: Skip if you already use Claude weekly."* Site-wide it
is 127 of 353.

**9.7 — "Found only" says nobody looked, then prints an opinion about what they saw.**
43 of 43 `listed` items carry a written Skip if; 11 of mine do. Claude for higher
education gets called "a sales page" by a tier that says "Nobody has looked at the
content yet."

**9.8 — Role tagging is wrong in both directions.** Into my list: "What is Claude Code?"
(*"For: Developers about to install Claude Code…"*) and the Kris Puckett design podcast
(*"For: Designers…"*, *"Before this: intermediate design experience"*). Out of my list: a
Coursera course called **"AI Fluency for Students"** tagged `['researcher']`.

**9.9 — A 0-result dead end tells me to loosen a filter I never set.** role=student +
level=builder gives *"Nothing matches all of those. Try removing one filter — time is
usually the one to loosen."* No time filter is set. The better message exists in
`browse.js:194` but `anyOtherThanRole()` counts `level`, so role+level can never reach
it.

**9.10 — "Nothing here needs an account" is printed under steps that need accounts and
money.** `paths.js` emits it at the foot of every path page, including the research path
whose step 2 is `free, sign-up needed` and whose step 3 is `pay once`.

**9.11 — The chooser closes itself with no exit.** After the second answer both chip rows
are hidden and the only way back is to notice that the words in the sentence are buttons.
Three of my clicks landed on empty page and changed nothing.

**9.12 — The count text says "for a student" when a search is what failed.**
`anyFilters()` (`browse.js:66`) ignores `q`, so a role + query state renders in the
role-only wording — "0 resources for a student", "3 resources for a student. Remove a
filter to see more." The advice points at the wrong control.

**9.13 — The integrity material is filed under a label no student will click.** 17 of my
41 carry the `safety` topic; the filter shows it as **"limits and safety"**. That is the
best content on the site for my role and the label describes a different subject.

**9.14 — 16 of my 41 are stale-flagged or undated.** 9 published before 2025-08-27 (so
the card prints "Published over a year ago — may not match Claude today") and 7 with no
date at all. Among the stale nine is "Using AI for Writing Feedback", which is the
number-one search hit for *"can I use this for my essay without cheating"*.

**9.15 — The same course is listed two and three times under different roles.** Five
duplicate titles site-wide; "AI Fluency: Framework & Foundations" exists three times
(Anthropic Academy → business-founder + non-technical; Coursera → four roles including
student; anthropic.com → researcher). I see one of the three and cannot tell there are
others.

**9.16 — 12.6 phone screens of undifferentiated cards.** 20 cards, 10,643px at 358px
content width, median 540px each. No grouping, no ordering signal I can act on, nothing
collapsible, and a bottom bar labelled only "Filters" with no count.

Sharpening things already on the known list, not claiming them as new:
- 0 of 353 `reviewed`. `how-we-check.html` opens with *"We would rather have 70 resources
  we can vouch for than 700 we cannot"* and its own live tally on the same page ends
  *"Nothing is read in full yet, and the cards say so."* The page argues against itself
  in two paragraphs.
- Every `checked` date in my 41 is 20, 21 or 22 August 2026. Three days. That is not
  "we check things", that is one import run.

---

## 10. The one thing that would make me leave and not come back

The search box on the front page.

That box is the site's promise. "Or describe what you want to do…" is the reason I would
choose this over a Google search — I get to ask my actual question instead of guessing
which category a stranger filed my problem under. I typed *"how do I cite Claude"*. I got
**"0 resources for a student"** and a message telling me to use fewer words.

The answer was there. Three of them. I proved it in the same browser tab: one keystroke
later the same page said "3 resources for a student" and listed exactly the three pages I
wanted. The site had them, knew about them, and told me it had nothing.

I would not have found that out. I would have concluded the directory is empty and gone
back to Google, and I would have been right to, because from where I was sitting it *was*
empty. Nothing else on this list matters if the front door hands back zero.

---

## 11. What is genuinely good (be honest, but brief)

- **`Skip if:` is the best idea on the site.** No other directory tells me who should not
  click. *"You have not studied the material yet. These prompts test you, they do not
  teach you, and going in cold just produces a demoralising transcript."* That is real
  advice from someone who has thought about it. When the tagging is right, the card is
  better than anything I would get from a search engine.
- **The four checking tiers, and refusing to round up.** "Read by AI. AI read all of it.
  No person has checked the notes yet." Nobody admits that. It is the single most
  credible sentence on the site, and it is why I would trust the other claims.
- **The counter before the click.** "41 resources match so far." means "Show me" is never
  a surprise. It seems like a small thing and it is not.
- **The integrity content itself is good and well chosen** — Melbourne, Warwick,
  Princeton, Tulane, St. Catherine, the PAIRR prompts. Someone who understands what a
  student is actually afraid of picked those. That work is done. It is the labelling,
  the routing and the search around it that throw it away.
- **The tone.** "Using Claude for research without embarrassing yourself" made me want to
  read the path. Plain, unpompous, occasionally funny. Do not lose that.

---

## Checklist — every line ticked or the file is not finished
- [x] I opened the live site
- [x] I tried all four levels — 20 / 15 / 6 / 0, read from `#tally` on the live page
- [x] I quoted at least 5 real titles or lines from the site — 19 verbatim quotes above
- [x] Every number I used is in 00-facts.md or I show the command
- [x] I looked at a phone width — via the `@media (max-width: 768px)` block plus a live
      358px measurement; the shared browser window would not hold 390px and I say so in
      section 7
- [x] I found at least one thing nobody has mentioned before — 9.1 (front-page search
      always returns 0), 9.2 (0 of 11 path steps are tagged for me), 9.3 (Plans & Pricing
      is founder-only and nothing in my 41 mentions cost), 9.5 ("Open on Stkate"), 9.6
      ("Skip if: Skip if"), 9.7 (43 of 43 unread items carry a verdict), 9.9 (loosen a
      filter I never set)
