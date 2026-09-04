# Attack 2: a student
Written as a university student, 2026-09-05. Live site only:
`https://mojtaba-alehosseini.github.io/learn-claude/`. Every URL and count below was
reproduced at least twice.

I have coursework due. English is not my first language. What I actually want to know is
whether using Claude will get me accused of cheating, and how to say I used it if I do.

---

## 1. First 60 seconds

Landing page is one sentence with two holes: **"I'm a [role] and I've [level]."** Under
it, ten chips headed "Who are you?", a text box ("Or describe what you want to do..."), an
orange **Show me**, and **"635 resources, checked by hand."**

I understood it immediately. That is the good news, and it is real.

Three things registered inside a minute:

- A drawing on the right cycles by itself (book, microscope, mug, stack of books), and a
  role chip tints itself in step with it, every ~2.6 seconds, before I have touched
  anything. I reloaded three times and got a different chip tinted each time. It is not a
  selection — selected chips go dark-on-light — but something on the page is moving and
  changing while I read.
- The level question does not exist until I answer the role question. So on arrival I can
  only answer half of the sentence I have been shown.
- "635 resources, checked by hand" sets an expectation. The **How we check** page then says
  *"Right now: 635 resources — 98 read by ai, 501 skimmed, 36 found only. **Nothing is read
  in full yet**"*. "Checked by hand" and "nothing read in full" are on two pages of the same
  site.

---

## 2. The front door, all four levels

I picked **a student** and then each level in turn. The home tally updates live before you
click Show me, which I liked.

| I said | Home tally | Browse result |
|---|---|---|
| never used Claude | "44 resources match so far." | 44 resources, three picks |
| used it a little | "25 resources match so far." | 25 resources, three picks |
| used it a lot | "10 resources match so far." | 10 resources, three picks |
| **built things with it** | **"0 resources match so far."** | **0 resources** |

**The fourth answer is a dead end.** The page offers me a fourth button, tells me it
returns nothing, and leaves **Show me** fully enabled and bright orange (`disabled` is
`false`, no `aria-disabled`). Push it and you land on
`browse.html?role=student&level=builder`:

> **We have nothing for this combination yet.**
> It's on the list. Loosen the level, or browse everything.

How it feels: like being asked a question the site already knew it could not answer. The
wording is honest and I respect that it is not a generic shrug. But I inspected the empty
block — **it contains zero links and zero buttons** (`#empty` innerHTML has no `<a>`, no
`<button>`). "Loosen the level, or browse everything" is dead text. The way out exists
only as small x chips further up.

There is a second problem hiding behind this. The level filter is **exact match**, not
"this level and below" (`browse.js`: `a.key === "levels" ? [it.level]`). At "used it a lot"
I get 10 items and the 44 beginner ones vanish completely. The page offers no hint, because
the "Remove a filter to see more" line only fires at 6 results or fewer.

---

## 3. What the catalogue gives me

79 items are tagged for students out of 635 (12%). Split: 44 / 25 / 10 / 0.

Tier split across the whole catalogue: 0 "Read in full", 98 "Read by AI", 501 "Skimmed",
36 "Found only".

The student cards are the strongest content on the site. Real examples I read in full:

- **"Plagiarism and Academic Integrity 101 in the Age of AI"** — *"Skip if: You need your
  own institution's rules. The Policies tab is Tulane-specific and cannot substitute for
  your syllabus."*
- **"Documenting Your AI Use"** — *"For: A student who wants to protect themselves from a
  false accusation by keeping a defensible record of how they worked."*
- **"AI-Powered Flashcards with Claude Projects"** — *"Skip if: ... Card-making is itself
  retrieval practice, and this hands that step to a machine."* That is an honest argument
  against its own entry. Nobody writes that unless they mean it.

Then the shelf falls apart at the top level. At "used it a lot", 10 items, and four of them
open by addressing somebody who is not me:

- *"For: **Academic researchers** checking the reproducibility of a paper's statistics
  before relying on it."*
- *"For: **Academics** who want to see how a published researcher actually integrates
  Claude..."*
- *"For: **Any analyst** worried about confidently-wrong output."*
- *"For: **Academics** with large local document collections..."*

Across all 79 student items, 10 open their "For:" line naming a researcher, academic,
analyst, developer or professional. I filtered for "a student". The card then tells me it
is for somebody else.

**And the single item I most needed is not on my shelf at all.** The catalogue contains
*"Guidance on AI detection, and why we're disabling Turnitin's AI detector"* (Vanderbilt),
whose own note reads *"never treat any detector score as proof against a student - false
accusations fall hardest on non-native English writers."* Its `roles` field is
`["teacher"]`. So is *"AI & Academic Integrity"*. Of the 8 integrity-related items in the
catalogue, 4 are teacher-only, and they are the two that answer the question I actually
came with. English is not my first language. That item is about me and I cannot reach it
through the front door.

---

## 4. Paths

Seven paths. Two list me: **"Your first week with Claude"** (6 steps, about 4 hours) and
**"Using Claude for research without embarrassing yourself"** (5 steps, about 2 hours, some
paid steps). There is no path for a student who is neither a beginner nor doing research.

I read every step's reason on both. **Most of them genuinely justify the position, not just
the item.** Examples:

- *"Start with the failure, not the feature. Fabricated citations are the one mistake that
  ends careers..."*
- *"Once you repeat a task twice, you need somewhere to keep the context. Projects is that
  place. **Learning this earlier would have been abstract.**"*
- *"Last, because working on your own files only makes sense once you trust the answers."*

That is the best writing on the site. Now the problems.

**Every single step on both student paths says "No publish date given."** Eleven steps,
eleven blanks. A path is an ordering claim about a fast-moving tool and not one item in it
carries a publication date.

**Step 1 of the flagship beginner path is an influencer Substack post.** "Claude is not one
tool. It's six." by Ruben Hassid (`ruben.substack.com`), badged "Read by AI" — no person has
checked it — with no publish date. The site's own rule elsewhere is to prefer official
sources. The first thing a nervous beginner is told to read is an unread, undated
newsletter.

**The research path's last step is not for me.** *"5. ICMJE Recommendations — Use of AI in
Publishing"*, with the reason *"Before you submit anything, read what the ICMJE expects you
to declare. **This is not optional** and most people learn it too late."* ICMJE is the
International Committee of Medical Journal Editors. I am submitting coursework. "This is not
optional" is simply false for the student half of the audience the path names.

**Step 3 of that path costs money** — a Johns Hopkins University Press / *Library Trends*
article, chip "pay once". The header says "some paid steps" and never says how much.

On the Paths index, step titles are cut off — *"3. The new rules of context engineering for
Cla..."*, *"1. Claude for Product Managers: Synthesizing Us..."* — so you cannot read what
is in a path from the page that lists paths.

And one line that reads like a machine wrote it: **"4 steps · about 81 minutes · free"**.
Every other path says "about 4 hours", "about 3 hours", "about 2 hours". "About 81 minutes"
is precise and vague in the same breath.

---

## 5. The card and the resource page

Would I click through? On three of them, yes.

The card is well built: badge, title, publisher, three chips, **For:**, **Skip if:**, path
position, dates. One focus stop per card (the title), with the whole card as the click
target.

**Resource page 1 — "Plagiarism and Academic Integrity 101 in the Age of AI".** Clean.
"What it teaches" / "Who it's for" / "Skip it if" / "How we checked this one: Skimmed...".
I would click through. This is the site working.

**Resource page 2 — "Generative AI and Academic Integrity" (CSU Northridge).** This one
broke my trust. See section 12, finding 1.

**Resource page 3 — "Claude for Education Is Made for Learning" (Pitt).** The #1 AI pick for
a student who has never used Claude. Two problems, both visible on the page:

- The summary reads *"**The clearest short onboarding page I found**..."*. Who is "I"? The
  badge on the same screen says *"Read by AI. AI read all of it. **No person has checked
  the notes yet.**"* Two student-facing cards use this first person; the other is
  "Acknowledging AI tools and technologies" — *"The cleanest declaration template **I
  found**"*.
- Under a heading **"Before this"** it says: *"— **Access to an educational Claude
  account**"*. That prerequisite exists on 447 of 635 items and **the browse card never
  shows it** (`LC.card` renders no prerequisites). So the site's top recommendation for a
  first-time student requires a university Claude for Education licence, and I only find
  that out after clicking.

One card renders its publisher as a broken word: **"AI: Artificial Intelligence Resources:
Claude / Und · Chester Fritz Library"**. `source` is literally `"Und"` — a slug off
`libguides.und.edu`. On the resource page the primary orange button reads **"Open on
Und"**.

---

## 6. The picks block

With exactly one role and one level, I get **"Start with these three"** and **"picked by AI
· 4 Sep 2026"**, then **"Everything else for you (41)"**. At `role=pm&level=builder` the
heading correctly becomes **"Start with these two"** and the tail reads "(56)". The counts
are honest — nothing is hidden, the picks are moved up, the total is unchanged.

**Are they just the first three rows? No, and I checked.** I reproduced the default sort and
located each pick in it:

| cell | pick positions in default order | pool |
|---|---|---|
| student / never used | 3rd, 9th, **23rd** | 44 |
| student / used it a little | **20th**, 2nd, 11th | 25 |
| student / used it a lot | 9th, 4th, 1st | 10 |

Reaching 23 rows down is real selection. Across all 37 cells, only one (developer / never
used) matches the top rows.

**Do the reasons add something?** Two of three, yes:

- *"The only candidate that covers prompting, Learning Mode, Projects and the hallucination
  warning in one twenty-minute read written for students in any subject - four first-day
  needs, one page, read by AI in full."* — names four things the title does not.
- *"The official course with no hidden prerequisite - **its Academy sibling for students
  assumes the 4D Fluency course first without saying so in the title** - and this one
  assumes nothing."* — this is the best sentence on the whole site. It names a specific
  rejected alternative and why.
- *"The only candidate that answers the question a student has before any tool question -
  where the line is - and it does it with scenarios rather than a policy PDF, at any
  university."* — this one is a paraphrase of the card's own "For:" line directly above it
  (*"...who is genuinely unsure where the line is and wants scenarios rather than a policy
  PDF"*). Same words, twice, six lines apart.

At "used it a lot" the reasons start over-claiming against a tiny pool: *"**The rarest skill
in the pool**"* — the pool is 10 items.

**Does "picked by AI" increase or decrease my trust?** It increases it, and it is the one
label on the site I would not change. It stops me imagining a curator who is not there. But
it also makes me read the reason harder — and pick #1 for a total beginner turns out to
need a university licence that the reason never mentions.

---

## 7. Dates and tier badges

**Dates.** Of 635 items, **445 carry no date at all** and 44 more have only an "Updated", so
**489 cards (77%) print "No publish date given."** I counted these from the shipped data and
matched them against what the cards show.

The home page promises *"**We show the date.** Claude changes every few months. You can see
when we last looked, and whether the thing is old."*

For the oldest material the site does the opposite. 17 items are older than a year, and for
every one of them the real date is **replaced** by **"Published over a year ago — may not
match Claude today."** The date is in the data — `2025-07-09`, `2025-04-08`, `2023-08-16` —
and the card refuses to print it. Six of those 17 are on my shelf. I cannot tell whether
"over a year ago" means thirteen months or three years, and for a tool that "changes every
few months" that is the whole question.

One card manages to do both at once. "Using AI for Writing Feedback": **"Published over a
year ago — may not match Claude today"** immediately followed by **"Updated 1 Aug 2025"**.
The published date it is hiding *is* 1 Aug 2025. It hides the date and prints it two words
later.

Does this look maintained or abandoned? Maintained — every card carries a "Checked" date,
mostly 5 Sep 2026, i.e. today, and all 79 of my links resolve. But it looks like a catalogue
that measured *itself* recently and its *contents* never.

**Tier badges.** "Skimmed" (501), "Read by AI" (98), "Found only" (36), "Read in full" (0).
The ladder tells me a lot about how much work went in: mostly a machine reading, a lot of
skimming, and a bottom rung of 36 items nobody opened.

The badges are unexplained where they matter. On Browse, `LC.badge` renders `<span
class="badge" title="...">` — **`tabIndex` -1, not focusable, explanation only in a mouse
tooltip.** There is no legend anywhere on Browse and no link from a badge to "How we check".
On a phone, and with a keyboard, "Found only" is a two-word label with no meaning attached
to it.

---

## 8. Search, in my words

| # | What I typed | Results |
|---|---|---|
| 1 | `will my university know i used ai` | 38 |
| 2 | `help me revise for exams` | 38 |
| 3 | `is it cheating to use claude for my essay` | 7 |
| 4 | `how do i cite claude in my references` | 13 |
| 5 | `summarise my lecture pdf and make notes` | 8 |

**Q1 — "will my university know i used ai" (38 results)**
1. *Generative AI and Academic Integrity* (CSUN) — badged **"Found only"**, i.e. nobody
   opened it, and its own Skip if says *"This adds little beyond a summary and local policy
   links."* **Verdict: bad.** The top answer to my most frightening question is an
   admittedly thin page nobody read.
2. *How long do you store my data?* (Claude Privacy Center) — data retention, not detection.
   **Verdict: wrong question.**
3. *Documenting Your AI Use* (St. Catherine) — *"protect themselves from a false
   accusation."* **Verdict: good, and it should be #1.**

The Turnitin/AI-detection item — the literal answer — is teacher-only and never appears. 38
results, none of which say "no, and here is why detectors are unreliable."

**Q2 — "help me revise for exams" (38 results)**
1. *How to Use AI to Help You Prepare for Quizzes and Exams* (Northeastern) — *"active
   retrieval practice and pressure rehearsal instead of re-reading notes."* **Verdict:
   excellent. Exactly right.**
2. *15 Claude Tips for Everyday Data Analysis* (LinkedIn Learning, subscription) — *"For:
   Excel-primary analysts."* **Verdict: garbage.**
3. *Working smarter with Claude in PowerPoint* — needs Pro/Max and Microsoft 365.
   **Verdict: garbage.**

One hit, then it falls off a cliff, and it still claims 38 results for a question with about
two real answers.

**Q3 — "is it cheating to use claude for my essay" (7 results)**
1. *Generative AI and Academic Integrity* — **"Found only."**
2. *Using AI for Writing Feedback* — **"Found only"** *and* **"Published over a year ago."**
3. *Claude for Education Is Made for Learning* — "Read by AI". **Verdict: relevant.**

**The two highest-ranked answers to the highest-stakes question I have are both items nobody
has read.** #4 (Melbourne) and #5 (Tulane) are the ones I actually needed.

**Q4 — "how do i cite claude in my references" (13 results)**
1. *Documenting Your AI Use* — documenting, not citing. **Verdict: near miss.**
2. *Connect and integrate your local Zotero library with Claude Cowork* — Zotero automation.
   **Verdict: wrong.**
3. *Claude Skills for Academics (Beginner Tutorial, Part 2)* — *"asks you to build Skills on
   top of third-party Obsidian ones."* **Verdict: absurd.**

The two items that literally answer it — *"Acknowledging AI tools and technologies"*
(Melbourne: *"a wording they can copy tonight"*) and *"Referencing AI and Acknowledging AI
Use"* (Warwick) — are at #5 and below, buried under a Zotero-plus-Obsidian workflow.

**Q5 — "summarise my lecture pdf and make notes" (8 results)**
1. *AI-Powered Flashcards with Claude Projects* — *"slides and notes as PDFs."* **Verdict:
   good.**
2. *Create custom course materials* — *"For: University math **instructors**... the
   tcolorbox LaTeX package."* **Verdict: wrong person, wrong subject.**
3. *How to Set Up a Claude Project that Answers Questions about Your Class* — **Verdict:
   good.**

(#4 is *Create interactive PDF forms* — *"For: Event and administration staff producing
registration or intake forms."* It matched on the word PDF.)

**Overall:** 5 of 15 top-three slots were right. The failure is consistent and it is not
random noise — the ranking cannot tell a student from an academic, and it cannot tell
"unread" from "checked", so it will hand a frightened undergraduate a "Found only" card at
position one.

---

## 9. On a phone

Emulated 375x812. This is the part of the site I have the least to complain about.

- No horizontal overflow: `document.documentElement.scrollWidth` = 375 = viewport.
- **Zero** interactive elements under 24px in either dimension. I enumerated every `button`
  and `a` on the browse page.
- Sticky **Filters** button, 343x44, opens a proper `dialog`.
- Cards stack cleanly, type stays readable, nothing clipped.

Two things I noticed anyway. On the home page at 375px the ten role chips take five rows and
**Show me** sits below the fold — you scroll to submit. And on the phone, "Loosen the level"
(the 0-result message) points at a filter rail that is not on screen; the only visible escape
is two small x chips.

---

## 10. Keyboard walk

Browse, `?role=student&level=never-used`, Tab from the top.

What is right, and it is more than most sites manage:
- Stop 0 is **"Skip to content"**, and it becomes visible on focus.
- **No positive `tabindex` anywhere.** Order follows the DOM.
- A global `:focus-visible { outline: var(--focus-ring) }`, plus a forced-colors block that
  pins the ring to `CanvasText`.
- Each result card is **one** focus stop (the title), not five. 76 stops total for 44 cards.

What is wrong:
- **The first result is Tab stop 29.** Stops 5-24 are the entire filter rail — Clear all,
  ten roles, four levels, four times, More filters — then search (25), sort (26), two
  applied-filter chips (27-28), and only then the first card. I arrived from the front door
  with my filters *already applied*, and I still have to press Tab twenty-nine times to
  reach a single result. There is no bypass link past the rail.
- **The tier badge is unreachable and unexplained by keyboard.** It is a `<span title="...">`
  with `tabIndex` -1. "Found only" never tells a keyboard user that it means nobody read the
  thing.

---

## 11. How we check

Less. Definitely less — and the page did it to itself, which is almost admirable.

It opens: **"We would rather have 70 resources we can vouch for than 700 we cannot."**
Eleven lines later: **"Right now: 635 resources — 98 read by ai, 501 skimmed, 36 found only.
Nothing is read in full yet, and the cards say so."**

635, none vouched for at the top tier. The page states a principle and then publishes the
number that breaks it, on the same screen. I read that as a stated value the site has not
lived up to, not as candour.

Second contradiction, same page: **"What we do — We find material, read it, and write two
things: who it helps, and who should skip it."** Four paragraphs down: **"Found only. We
found it and sorted it. Nobody has looked at the content yet."** Both cannot be true, and it
is the *second* one that is true for 36 resources — which still carry "who it helps" and
"who should skip it".

The ladder itself is the right idea and I want to say so. "Read by AI. AI read all of it. No
person has checked the notes yet" is a sentence very few directories would print. The
problem is not the ladder. It is that the cards do not obey it.

(Also, small: the count line writes **"98 read by ai"** in lower case while every badge on
the site says "Read by AI".)

---

## 12. Everything broken, ranked

**1 — CRITICAL. "Found only" cards pass detailed judgment on content nobody opened.**
URL: `resource.html?id=r-0723e82a39`. I opened it and read the whole page. It says, in this
order:
- Summary: *"A short library page setting out where generative AI sits against a
  university's existing academic dishonesty definitions, **kept current through August
  2026**."*
- *"What it teaches — Understand university rules on generative AI use / Know how
  unattributed AI text is treated in assignments"*
- *"Skip it if: ... **This adds little beyond a summary and local policy links.**"*
- *"How we checked this one: **Found only. We found it and sorted it. Nobody has looked at
  the content yet.**"*

Expected: a card that says nobody read it describes nothing about what is inside it.
Systemic: **all 36** "Found only" items carry a summary, a who-for, a skip-if and a teaches
list. Others: *"Nothing in it visibly tells you to check Claude's arithmetic"*; *"it is
enormous"*. You cannot know either without opening the thing.
**Harms:** every reader, most of all a student. This card is the **#1 result** for "will my
university know i used ai" and for "is it cheating to use claude for my essay". I would act
on a verdict that has no basis, and the site's entire selling point — the honesty ladder —
is void.

**2 — HIGH. The one resource about AI-detector false accusations is invisible to students.**
`"Guidance on AI detection, and why we're disabling Turnitin's AI detector"` — `roles:
["teacher"]`. So is `"AI & Academic Integrity"`. Of 8 integrity items, 4 are teacher-only.
Expected: a site that offers "a student" as a front-door role puts the false-accusation item
on the student shelf.
**Harms:** students, hardest of all non-native English writers — a group the resource's own
note singles out.

**3 — HIGH. Student + "built things with it" = nothing, and the front door still sells it.**
`index.html` -> a student -> built things with it -> **"0 resources match so far."**, **Show
me** enabled (`disabled: false`, no `aria-disabled`). -> `browse.html?role=student&level=builder`
-> **"We have nothing for this combination yet. It's on the list. Loosen the level, or browse
everything."** — `#empty` contains **no link and no button**.
Expected: a two-question front door does not offer a combination it knows is empty, and its
dead-end message is clickable.
**Harms:** the most advanced students — the ones most able to tell others the site is not for
them.

**4 — HIGH. The dates the reader needs most are the ones deliberately withheld.**
489 of 635 cards (77%) read "No publish date given". The 17 items over a year old have their
real date **replaced** by "Published over a year ago — may not match Claude today" — 6 of
them on the student shelf, with dates of `2025-07-09`, `2025-04-08`, `2025-06-12` sitting
unused in the data. Home page promises "We show the date."
**Harms:** anyone deciding whether a guide still matches the product. A student cannot
distinguish 13 months from 3 years.

**5 — MEDIUM-HIGH. Search puts unread and wrong-audience material at the top for the
highest-stakes questions.**
Five real queries, 15 top-three slots, 5 right. Two "Found only" cards ranked 1 and 2 for "is
it cheating to use claude for my essay". "15 Claude Tips for Everyday Data Analysis" ranked 2
for "help me revise for exams".
**Harms:** anyone who types a sentence instead of using the filters — which is what the home
page invites with "Or describe what you want to do...".

**6 — MEDIUM. "For:" lines address the wrong reader on the shelf I filtered.**
10 of 79 student items, including **4 of the 10** at "used it a lot": *"For: Academic
researchers..."*, *"For: Academics..."*, *"For: Any analyst..."*.
**Harms:** students at the level with the fewest items, who then find 40% of them are not
addressed to them.

**7 — MEDIUM. The top AI pick for a beginner student hides a hard prerequisite.**
`r-6bdd922cd9`. Resource page: *"Before this — Access to an educational Claude account."* The
browse card never renders prerequisites (`LC.card`), and the pick reason does not mention it.
447 of 635 items have prerequisites; none appear on cards.
**Harms:** students whose university has no Claude for Education licence — they follow the #1
recommendation and hit a wall.

**8 — MEDIUM. Tier badges are unexplained where the choice is made.**
`<span class="badge" title="...">`, `tabIndex` -1. No legend on Browse, no link from a badge
to "How we check".
**Harms:** phone users and keyboard users, i.e. the people the site's own honesty ladder is
supposed to protect.

**9 — MEDIUM. "How we check" contradicts itself and the catalogue.**
*"We would rather have 70 resources we can vouch for than 700 we cannot"* over 635 with none
read in full; *"We find material, read it"* over *"Nobody has looked at the content yet."*
**Harms:** the reader who goes to the trust page to decide whether to trust the site.

**10 — LOW-MEDIUM. 29 Tab stops to the first result, with filters already applied.**
**Harms:** keyboard and screen-reader users.

**11 — LOW. 125 of 635 cards read "Skip if: Skip if ..." (15 of 79 student cards).**
Live examples: *"Skip if: Skip if your university has no Claude for Education licence - none
of it applies."*, *"Skip if: Skip if you want feature coverage - Projects, Cowork, and Skills
are barely touched."*
**Harms:** nobody badly. It just reads as unproofread on one card in five.

**12 — LOW. Broken publisher name shipped to the primary button.** `source: "Und"` -> card
reads *"Und · Chester Fritz Library"*, resource page button reads **"Open on Und"**. It is
the University of North Dakota.

**13 — LOW. Voice contradiction on two student cards.** *"The clearest short onboarding page
**I found**"* and *"The cleanest declaration template **I found**"*, both under a badge that
reads *"No person has checked the notes yet."*

**14 — LOW. Paths index numbers and titles.** *"4 steps · about 81 minutes · free"* against
"about 4 hours" / "about 3 hours" / "about 2 hours" elsewhere. Step titles truncated: *"3.
The new rules of context engineering for Cla..."*.

**15 — LOW. One date shown, the same date hidden.** "Using AI for Writing Feedback":
*"Published over a year ago — may not match Claude today"* directly above *"Updated 1 Aug
2025"*.

**16 — LOW. "This is not optional" is false for half the named audience.** ICMJE step in a
path labelled "For a researcher, a student".

---

## 13. The one thing that would make me leave

I asked the site the only question I really came with — *will my university know i used ai* —
and the first thing it handed me was a card whose own badge says **"Found only. We found it
and sorted it. Nobody has looked at the content yet"**, sitting directly under a summary
claiming the page is **"kept current through August 2026"** and a verdict that it **"adds
little beyond a summary."**

If nobody opened it, you do not know it is current and you do not know what it adds. The
site's whole pitch over a Google search is that somebody looked and formed a judgment. At the
exact moment I needed that most, it made the judgment up. I would close the tab and go read
my own university's page instead.

---

## 14. What is genuinely good

- **Every one of the 79 student links works.** I resolved all 79 with a real browser
  user-agent following redirects: 79 HTTP 200, zero dead, zero blocked. For a hand-built
  directory of 635 items that is unusual and it is the hardest thing here to fake.
- **The picks are real selection, not the top of the list.** For "student / never used
  Claude" the three picks sit at positions 3, 9 and 23 of 44. Only 1 of 37 cells matches the
  default top rows.
- **"Skip if:" exists on all 635 entries and frequently argues against the entry.**
  *"Card-making is itself retrieval practice, and this hands that step to a machine."* That
  is a real editor's line.
- **Mobile is properly built.** No horizontal overflow at 375px, no tap target under 24px, a
  real `dialog` for filters.
- **Focus handling is above average.** Skip link, global `:focus-visible` ring, forced-colors
  fallback, one focus stop per card instead of a 689-character link name.
- **The path "why" lines mostly justify the position, not just the item.** *"Learning this
  earlier would have been abstract."*
- **The empty-state copy names the real cause** — "We have nothing for this combination yet",
  not a generic "no results".
- **"picked by AI" and "Nothing is read in full yet, and the cards say so"** are labels almost
  nobody would ship. Keep them. Then make the cards obey them.

---

## Checklist
- [x] I opened the live site at all four levels of my role — 44 / 25 / 10 / 0
- [x] I quoted at least 5 real titles or lines from the site — 30+
- [x] Every number I used is computed from the shipped data
- [x] I looked at a phone width — 375x812
- [x] I did one full keyboard walk — browse, 29 stops to result 1
- [x] Five search queries in my own words, each with its verdict — 5 of 15 slots right
- [x] I read the picks block and tested whether it is the top three rows — positions 3, 9, 23
- [x] I found at least one thing nobody has mentioned before — the AI-detector resource that
      is about students and tagged teacher-only, and the 447 prerequisites that never appear
      on a card
