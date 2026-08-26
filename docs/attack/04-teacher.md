# Attack: a teacher
Written as someone who is a teacher, at 2026-08-27. Site version: 22e4532.

I teach. I have one free hour between classes. I came here with three questions, and
they are the only three that matter to me:

1. Are my students using this to cheat, and what do I do about it?
2. Is it legal and safe for me to put a 14-year-old in front of it?
3. How do I grade an essay when I cannot tell who wrote it?

I am not here to learn prompting. I can learn prompting from anybody. I am here because
my head of department asked me a question I cannot answer.

---

## 1. The first 60 seconds

The home page says **"Find what's worth your time."** Then it gives me one sentence to
fill in: *"I'm [a role] and I've [level]."*

I press the first blank. Ten options. One of them is **"a teacher"**. Good. That is more
than most sites do.

I press the second blank. Four options: *never used Claude, used it a little, used it a
lot, built things with it*. I choose "used it a little" — I have typed into Claude twice.

Then the search box vanishes.

That is a real thing. `index.html` has `.search-row.answered .input { visibility:
hidden; ... }`. Once I answer both questions, the box that says *"Or describe what you
want to do…"* collapses to zero width and leaves the tab order. So the site asks me who
I am, and as a reward it takes away the only place on the page where I could have typed
**how do I stop students cheating**.

I did not want to be a role. I wanted to ask a question. The site made me choose, and
then it decided for me.

Three promises sit under the fold:

- "We say when to skip"
- "We say how we checked"
- "We show the date... You can see when we last looked, and whether the thing is old."

Hold on to the third one. I come back to it in 9.4.

## 2. Does the front door work for me (all four levels, with counts)

Command:

```
python docs/attack/role-view.py teacher --counts
```

```
teacher: 47 total
  never-used    16
  basic         24
  confident      6
  builder        1
  tiers:   {'ai-reviewed': 10, 'previewed': 22, 'listed': 15}
  formats: {'article': 14, 'docs': 11, 'video': 10, 'course': 9, 'repo': 1, 'podcast': 2}
  free:    37
  no date: 21
  only this role: 29
```

Matches `00-facts.md` exactly. 47 total. 16 / 24 / 6 / 1.

I opened all four on the live site.

**never used Claude — 16.** The first card is
*"Claude for K-12 teachers - product page with worked prompts"*. Its own Skip-if says:
"Skip if sales pages irritate you - most of this is claims, logos and testimonials.
Skip if you are outside the US, because the free plan is US-only."

The site put a sales page in position one, then told me it is a sales page. I am outside
the US. So card one of sixteen does not apply to me, and the site knows it does not.

**used it a little — 24.** This is the only shelf with anything I actually asked for. It
holds the policy material: Cornell on assignment design, the AI Assessment Scale,
Vanderbilt on AI detectors, UNESCO, the EU ethical guidelines, the Australian framework,
the US toolkit, and a district leader explaining why he blocked the product. Eight cards
that speak to my real job. Every single one is at the bottom badge. See 9.1.

**used it a lot — 6.** Confirmed live at
`browse.html?role=teacher&level=confident` → "6 resources. Remove a filter to see more."

The six, in the order the site gave them:

```
43 Claude Skills for college teachers
AI Fluency for pK-12 Train the Trainer
How to Set Up a Claude Project that Answers Questions about Your Class
Teaching AI Fluency (Anthropic Academy)
Kris Puckett - Becoming an AI-native designer (Dive Club)
AI feedback customized for student writers: the updated PAIRR prompts
```

Number five is a podcast with a Stripe design manager about building his own apps and
teaching Claude to write metal shaders. Its `who_for` field, printed on the card, reads:
**"Designers wanting a deep, honest look at an AI-native design practice."** No teacher.
No classroom. No student. It is one of six cards I get at this level, so it is 17% of my
"used it a lot" shelf. See 9.6.

**built things with it — 1.** Confirmed live at
`browse.html?role=teacher&level=builder` → "1 resource. Remove a filter to see more."

That one resource:

```
[Skimmed] Agent Skills for K-12 Teachers (open source)
GitHub · repo · under-1hr · free · checked 2026-08-21 · published UNVERIFIED
For:     Teachers outside the US who cannot get the official plan, and anyone who wants
         to read and edit the exact instructions Claude follows when it writes a lesson plan.
Skip if: Skip if you do not use a terminal - installing needs git and Claude Code. Skip
         if you already have Claude for Teachers, where the skills are installed for you.
```

**Is one card a legitimate answer to a question the site asked me?** No.

The site offered me four buttons. Three of them are real shelves. The fourth returns a
single GitHub repo whose own Skip-if line disqualifies almost every teacher alive: "Skip
if you do not use a terminal." A teacher who presses "built things with it" is a teacher
who writes Google Apps Script or maintains the school website. She presses the button,
gets one repo, is told to install git and Claude Code, and has nothing else. The site
does not say "there is almost nothing here for you at this level." It shows one card and
a nudge — "Remove a filter to see more" — which means: undo the answer you just gave me.

If a question has one answer, it is not a question. It is a shrug with a button on it.

## 3. What the catalogue actually gives me (are these really for me?)

**Which is it — teaching *with* Claude, or teaching *about* Claude?**

It is both, badly mixed, plus a third thing nobody asked for.

I sorted my 47 by what they are actually about:

- **Teaching *with* Claude** (my own planning, marking, admin): the K-12 videos, the
  Projects tutorial, the Artifacts tutorial, the practical guides. This is the largest
  group and it is the only group the site does well.
- **Teaching *about* Claude** (what I put in front of students): the AI Fluency courses,
  Day of AI, Teaching AI Fluency. Real, present, decent.
- **Institutional policy and risk** (my actual question): 8 cards, all at the lowest
  badge. See 9.1.
- **Neither** — cards written for somebody else and shown to me anyway. See 9.5 and 9.6.

The mix is wrong in one specific way. **The catalogue is heavy on "how to use the tool"
and near-empty on "what to do when a student uses the tool."** I can prove that with the
site's own vocabulary.

`assets/js/ui.js:40` holds every topic word the site owns. There are eight:

```js
LC.TOPIC = {
  "chat-prompting": "chat and prompting", "claude-code": "Claude Code",
  "cowork": "Cowork", "skills": "Skills", "mcp": "connectors",
  "agents": "agents", "api": "API", "safety": "limits and safety"
};
```

Seven of the eight are Claude product features. The eighth is "limits and safety."

There is no word for academic integrity. No word for assessment. No word for classroom
policy. No word for student data. No word for safeguarding. The vocabulary cannot say
the thing I came here to ask.

So everything gets shovelled into "safety". Command:

```
python -c "... [i for i in items if 'teacher' in i['roles']] ... Counter(topics)"
→ {'chat-prompting': 30, 'safety': 25, 'skills': 6, 'cowork': 5, 'agents': 2,
   'claude-code': 1, 'mcp': 1}
```

Confirmed live at `browse.html?role=teacher&topic=safety` → **"25 resources"**.

25 of my 47 cards carry one topic word, "limits and safety". That word has to cover:

- the model invents facts
- FERPA and my district's data agreement
- the EU ethical guidelines and GDPR
- UK safeguarding under KCSIE
- how to design an assignment a student cannot outsource
- whether to trust an AI detector

Those are six different meetings with six different people. The site calls them one
topic. Filtering by it removes 22 cards and tells me nothing.

And the first card inside that filter — live, top of the list — is *"Advancing Claude
for Education"*, whose For line reads: **"A student at a Claude for Education university
who wants to know whether their lectures and library are connectable."**

The top of my safety shelf is addressed to a student.

## 4. Paths

`00-facts.md` says I have a path: **"Your first week with Claude"** — 6 steps, about 2
hours, free, roles `non-technical, student, teacher, business-founder`.

I clicked Paths. Here is what the live page gave me:

```
curl -s https://mojtaba-alehosseini.github.io/learn-claude/paths.html?id=first-week
→ 200, 1987 bytes, <div id="content"></div>
```

Rendered, via the live page:

```
Your first week with Claude
Anyone who has just opened Claude and does not know what to do next.
6 steps · about 2 hours · free
1. Claude is not one tool. It's six.
2. Get started with Claude
3. Claude 101
4. What are Projects?
5. Why do AI models hallucinate?
6. Get started with Claude Cowork (Help Center)
```

**Does step 1 speak to a teacher?** No. Step 1 is a Substack post called *"Claude is not
one tool. It's six."* Its whole argument is that Claude is several products and people
look in the wrong place. That is a fine post. It is not about me. It is not about a
classroom, a student, a lesson, a school, or a rule.

Nor is step 2, 3, 4, 5 or 6. Six steps, about two hours of my life, and the word
"teacher" does not occur once.

The path's own `for` line is **"Anyone who has just opened Claude and does not know what
to do next."** Literally *anyone*. A path shared with "not a coder", "a student" and
"running a business" is not shared. It is a generic beginner path with four role tags
stapled on so that four counters can say "has a path: yes".

**Then it gets worse.** Two things I checked and did not expect:

```
grep -n "role\|ROLE" assets/js/paths.js
→ (no output)
```

`assets/js/paths.js` never reads the `roles` field. Not once. The Paths page lists all
three paths in a row and never says which one is mine. The data knows. The page does not
tell me.

And:

```
python -c "... first-week steps tagged teacher ..."
→ step 1 teacher=False  roles=non-technical
   step 2 teacher=False  roles=non-technical
   step 3 teacher=False  roles=business-founder,data-analyst,non-technical,researcher,writer-marketer
   step 4 teacher=False  roles=researcher
   step 5 teacher=False  roles=non-technical
   step 6 teacher=False  roles=business-founder,non-technical
   first-week steps tagged teacher: 0 of 6
```

Zero of six. And across the whole site:

```
all path step items: 16
teacher-tagged items that are a step in ANY path: 0
```

**Not one of my 47 cards is in any path.** So the "Step 3 of 6 in Your first week with
Claude" line that `ui.js:167` prints on a card can never appear on a card I am shown. I
can browse all 47 of my resources and never learn a path exists.

Step 4 is *"What are Projects?"*, tagged `researcher` only. My own shelf has *"How to Use
Claude Projects (Full Tutorial)"* sitting on it. Same subject. Different card. The path
sends me to the researcher's copy, which I would never find, instead of mine, which I
already have. Nobody joined these two things up.

So: I have a path. It does not name me on screen, none of its steps is tagged for me,
none of my resources leads to it, and when I finally find it by guessing, it teaches me
nothing about my job. See 9.2.

## 5. The card and the resource page

I opened three.

**The AI Assessment Scale (AIAS)** —
`resource.html?id=r-3ef5584cd6`. Live text:

```
Found only
The AI Assessment Scale (AIAS)
Aiassessmentscale · Mike Perkins, Jasper Roe, Leon Furze and Jason MacVaugh
Who it's for: University lecturers and senior-school teachers writing an assessment
policy or a per-assignment AI rule. Teaching-students.
Skip it if: Skip if you are looking for a way to catch cheating - the scale is about
designing tasks, not policing them...
How we checked this one
Found only. We found it and sorted it. Nobody has looked at the content yet.
```

This is the single most useful card on the whole site for me. A five-level scale my
department could adopt on Monday, with the papers behind it. And the site's verdict on
it is: **nobody has looked at the content yet.**

The publisher name is rendered as **"Aiassessmentscale"**. That is a domain with the
dots removed and one capital bolted on. Same pattern on other cards: "Unesco", "Eu",
"Au", "Ed", "Gov", "Dayofai", "Aifluencyframework". I am asked to trust a directory that
cannot write "UNESCO".

**Guidance on AI detection, and why we're disabling Turnitin's AI detector** —
`resource.html?id=r-1b663b7646`. Live provenance line:

```
Checked 21 Aug 2026 · Published 16 Aug 2023 · Found through Vanderbilt
```

Three years old. Badge: "Found only. We found it and sorted it. Nobody has looked at the
content yet."

This is the card that tells me not to accuse a student on the strength of a detector
score. It is the one card here that could stop a colleague ruining a child's year. It is
from 2023 and no human has read it.

**Claude for higher education** — never-used shelf, position 15. Its Skip-if:

> "You already have access, or you want to be taught something. This is a sales page and
> it teaches nothing about using Claude well."

The site is telling me, on the card, that the card teaches nothing. Then why is it in a
directory whose home page says "Find what's worth your time"? Delete it or keep it. Do
not print an admission of worthlessness and leave the thing on my shelf.

**On the resource page as a design:** the order is good — what it teaches, who it's for,
skip it if, how we checked. That order is right. But there is no way to report anything,
no comment, no "this is out of date", nothing. And one thing goes missing between the
card and the page. See 9.4.

## 6. Search, in my words

I typed three real sentences. Reproduced with `python scripts/test-search.py`, which the
file itself says "mirrors assets/js/search.js exactly — same index, same IDF, same admit
gate, same floor."

### "how do I stop students cheating"

```
python scripts/test-search.py "how do I stop students cheating"
"how do I stop students cheating"   45 result(s)
     35.2  [researcher            ] AI Fluency for Students
     26.1  [researcher,student    ] 3 Mind Blowing Claude & Consensus Research Workflows | N
     20.5  [student               ] Plagiarism and Academic Integrity 101 in the Age of AI
```

Rank 3 is *"Plagiarism and Academic Integrity 101 in the Age of AI"*. Rank 4 is
*"Generative AI and Academic Integrity"*. Those are the two best answers to my question
in the entire catalogue.

```
python -c "... items where title/summary/who_for contains plagiar|cheat|academic integrity ..."
Plagiarism and Academic Integrity 101 in the Age of AI
   roles=['student'] level=never-used tier=previewed
Generative AI and Academic Integrity
   roles=['student'] level=never-used tier=listed
```

**Both are tagged `student` only. Neither is tagged `teacher`.** Of 353 resources, two
are about academic integrity, and a teacher cannot reach either one from the teacher
filter. The site handed the cheating problem to the people doing the cheating and told
the person who has to deal with it to look somewhere else.

With my role filter on, as Browse would apply it, I get 11 cards. The top one is
*"AI feedback customized for student writers: the updated PAIRR prompts"* at the "Found
only" badge, and its For line begins **"A student who wants feedback prompts…"**.

### "is this safe for 14 year olds"

```
python scripts/test-search.py "is this safe for 14 year olds"
"is this safe for 14 year olds"   14 result(s)
     16.9  [business-founder,non-technical] AI Fluency for Small Businesses
     16.9  [business-founder      ] Is my data used for model training? (Privacy Center)
     16.9  [non-technical         ] Use Claude Cowork safely
```

I asked about a child. The site's first answer is **AI Fluency for Small Businesses**.
Then a business privacy page. Then a Cowork safety page. The first teacher-tagged result
is at rank 6. The top five all score an identical 16.9, so the ranking here is not
ranking anything — it matched "safe" and gave up.

With my role filter on: 5 cards. Four are about the US product's terms. The fifth is the
UK DfE pack, whose Skip-if says "Skip if you are outside England."

Nothing in those five answers the question. So I checked whether the answer exists at
all:

```
python -c "... word-boundary search across the 47 teacher cards ..."
18-plus         1  AI Fluency for students
under 18        1  AI Fluency for students
age-appropriate 1  AI Fluency for students
coppa           0
consent         0
safeguard       1  Using AI in education settings: support materials (UK DfE)
gdpr            1  Ethical guidelines on the use of AI and data in teaching (EU)
ferpa           3
```

**One card in 47 says Claude is 18-plus.** One. And it says it inside a Skip-if line, on
a course *for students*:

> "Skip if your students are under 18 and you need age-appropriate classroom activities -
> this is written for adult learners and Claude is 18-plus."

That is the most important sentence on this entire site for a school teacher, and it is
buried in the twelfth card of the beginner shelf, in the paragraph that tells me to skip
the card. See 9.3.

### "how do I mark AI written essays"

```
python scripts/test-search.py "how do I mark AI written essays"
"how do I mark AI written essays"   7 result(s)
     21.3  [teacher               ] AI in assignment design - Cornell Center for Teaching In
     21.3  [writer-marketer       ] Wikipedia:Signs of AI writing
     18.1  [student,non-technical ] Claude for Education Is Made for Learning
```

Seven results in a 353-item catalogue. Rank 1 is right, and it is at the "Found only"
badge. Rank 2 is a Wikipedia style page for marketers. With my role filter on I get
**two** cards, and the second is *"Lesson 7: Effective prompting techniques (Deep Dive)"*
— a generic prompting video with nothing to do with marking.

Two cards. For the question every teacher in the world is asking in 2026.

## 7. On a phone

I did not resize the browser. Four other people are working in that window and I am not
going to break their session to make a point. So I read the code that decides what my
phone gets: `assets/css/site.css:590`, the `@media (max-width: 768px)` block, plus
`assets/js/browse.js`.

What happens at 768px and below:

- `.filter-rail { display: none; }` — the whole left filter column is removed.
- `.mobile-filter-bar` is shown, fixed to the bottom, full-width button. Thumb-reachable.
  Correct instinct.
- Pressing it opens `.sheet`, a full-screen panel, built by
  `el.sheetBody.innerHTML = AXES.map(groupHTML).join("")` — the same six axes as the
  desktop rail, stacked in one scrolling column.

Six axes: Role (10 options), Level (4), Time (4), Topic (8), Format (7), Cost (4). That
is **37 checkboxes in a single vertical scroll**, with no search inside the sheet and no
collapsed groups. To reach Topic on a phone I scroll past 18 controls I do not want.

The bar is good. The sheet is a desktop rail dropped into a phone.

Two mobile details the code shows are already handled, so I am not claiming them:
`body:has(.mobile-filter-bar) .site-footer .wrap` now pads for the fixed bar, and
`.footer-col a { min-height: 44px }` fixes the tap targets. Both carry comments
explaining the fix. Fine.

One thing that is not handled. `data/items.js` is loaded by every page:

```
curl -s -o /dev/null -w "%{size_download}" .../data/items.js            → 624541 bytes
curl -s --compressed -o /dev/null -w "%{size_download}" .../data/items.js → 173810 bytes
```

Every visitor downloads all 353 resources to read one shelf of 47. On school wifi, on a
phone, between lessons. And 2,100 bytes of that is text no code will ever read (9.8).

## 8. Content quality — the three worst entries I was shown, quoted

**Worst 1 — "Claude for K-12 teachers - product page with worked prompts."** Position 1
of 16 on the never-used shelf. Badge: "Read by AI" — the highest badge that exists on
this site, because `reviewed` is empty. Its own Skip-if:

> "Skip if sales pages irritate you - most of this is claims, logos and testimonials.
> Skip if you are outside the US, because the free plan is US-only."

The very first thing the site shows a teacher who has never used Claude is a vendor sales
page it describes as claims and logos, for a product most of the world cannot get.

**Worst 2 — "Kris Puckett - Becoming an AI-native designer (Dive Club)."** One of my six
"used it a lot" cards. Confirmed live in the teacher/confident list. Its For line:

> "Designers wanting a deep, honest look at an AI-native design practice."

Its Skip-if:

> "You have already read the Cat Wu article — the video covers the same ground, and I
> could not confirm its runtime or publication date."

The summary in `items.json` says it is about "building his own apps with Claude Code,
creating custom skills, teaching Claude metal shaders, and building internal tools."
There is no education content in it. The skip line names an article I have never heard of
and admits the entry could not be verified. It is on my shelf because somebody typed
`teacher` into a roles array.

**Worst 3 — "Claude for higher education."** Never-used shelf. Badge "Found only". For
line: "A student checking whether their institution is covered." Skip-if:

> "You already have access, or you want to be taught something. This is a sales page and
> it teaches nothing about using Claude well."

A sales page, for students, that the site says teaches nothing, on the beginner shelf of
a teacher.

**Dishonourable mention — "Guidance on AI detection, and why we're disabling Turnitin's
AI detector."** Not badly written. Badly handled. Published 16 Aug 2023, "Found only",
nobody has read it. Its own Skip-if contains the best sentence on this website:

> "And never treat any detector score as proof against a student - false accusations fall
> hardest on non-native English writers."

That sentence deserves to be on the front page. It is at the bottom of the worst-checked
tier of a three-year-old card.

## 9. Everything that is broken, ranked

### 9.1 Every policy and integrity resource I have is unread and undated

The eight cards that answer my real questions:

```
Anthropic launched Claude for Teachers. We blocked it   tier=listed  pub=UNVERIFIED
AI in assignment design - Cornell                       tier=listed  pub=UNVERIFIED
The AI Assessment Scale (AIAS)                          tier=listed  pub=UNVERIFIED
Guidance on AI detection / Turnitin (Vanderbilt)        tier=listed  pub=2023-08-16
The Australian Framework for Generative AI in Schools   tier=listed  pub=UNVERIFIED
UNESCO AI competency framework for teachers             tier=listed  pub=UNVERIFIED
Ethical guidelines on AI and data for educators (EU)    tier=listed  pub=UNVERIFIED
Empowering Education Leaders: a toolkit                 tier=listed  pub=2024-10-24
8 policy cards; listed: 8 ; no date: 6
```

**8 of 8 are at `listed`** — "We found it and sorted it. Nobody has looked at the content
yet." **6 of 8 have no publication date.** The 2 that have one are both over a year old
and carry the outdated flag.

Now compare. Of the 10 teacher cards at the top badge, five are Anthropic's own pages:

```
support.claude.com/...  Use Claude for Education at your university
anthropic.com/news/...  Advancing Claude for Education
anthropic.com/news/...  Introducing Claude for Teachers
claude.com/solutions/teachers   Claude for K-12 teachers - product page
support.claude.com/...  Claude for Teachers: your data and our terms
```

The default sort is tier first (`browse.js:111-113`). So the effect is mechanical and
constant: **short, scrapeable vendor pages get read, badged, and put at the top. Long
government and university PDFs get found, not read, and sunk to the bottom.** The
ranking rewards how easy a page was to process, not how much it matters. For a teacher
that inverts the catalogue exactly.

### 9.2 The path that names me is unreachable from anywhere I go

- `assets/js/paths.js` contains zero references to `role` (`grep -n "role\|ROLE"` → no
  output). The Paths page cannot tell me which path is mine.
- 0 of the 6 `first-week` steps is tagged `teacher`.
- 0 of the 16 step items across all 3 paths is tagged `teacher`.
- Therefore the `Step N of M in …` line at `ui.js:167` can never render on a card a
  teacher is shown.

The `roles` array on each path is shipped to every visitor in `data/paths.js` and read by
nothing. "Has a path: yes" is true in a spreadsheet and false on the screen.

### 9.3 The one fact a school teacher must know is stated once, in a skip line

Across all 47 of my cards: `18-plus` / `under 18` / `age-appropriate` → **1 card**.
`COPPA` → **0**. `consent` → **0**. `safeguard` → **1**. `GDPR` → **1**. `FERPA` → **3**.

Claude's consumer terms are 18+. The site says so exactly once, inside the Skip-if of
*"AI Fluency for students"*, a course aimed at adult learners. A secondary teacher can
work through all 16 never-used cards and never be told that the tool cannot lawfully be
put in front of most of her class.

And of the four cards that name any law, all four geofence me out — 7 of my 47 cards
carry a "skip if you are outside the US / EU / England" clause. If I teach in Denmark,
Canada, India or Brazil, the site has no legal answer for me and does not say so.

### 9.4 The "may not match Claude today" warning is removed at the exact moment I decide

The home page promises: "You can see when we last looked, **and whether the thing is
old**."

`LC.freshness` (`ui.js:90-111`) computes a note when a resource is over 365 days old:
`"Published over a year ago — may not match Claude today"`, with the class
`flag-outdated`. The browse card prints it (`ui.js:189`).

Live, at `browse.html?role=teacher&q=turnitin`, the card foot reads:

```
Checked 21 Aug 2026 | Published over a year ago — may not match Claude today
```

Click that card. Live, at `resource.html?id=r-1b663b7646`, the provenance line reads:

```
Checked 21 Aug 2026 · Published 16 Aug 2023 · Found through Vanderbilt
```

`resource.js:55` calls `LC.freshness(item)`, uses `fresh.checked`, and **throws away
`fresh.note` and `fresh.cls`**. The warning is calculated and discarded. It shows on the
page where I am skimming and is gone on the page where I commit my hour. That is the
wrong way round. 9 of my 47 cards are affected.

There is a second edge to this. A card with `published: UNVERIFIED` gets the neutral text
"No publish date given" and **no warning class at all**. So an honest 2023 date is
punished with a red flag, and a missing date gets a shrug. 21 of my 47 have no date and 9
carry the flag: only 17 of 47 have a verified, in-date publication date. The
date-less card looks *safer* than the dated one.

### 9.5 Eight of my cards are written to a student, not to me

```
python -c "... who_for startswith 'a student' among teacher items ..."
AI Fluency for students
Use Claude for Education at your university
Anthropic Education Report: How University Students Use Claude
Advancing Claude for Education
Claude for higher education
How to Set Up a Claude Project that Answers Questions about Your Class
AI feedback customized for student writers: the updated PAIRR prompts
Peer and AI Review of Student Writing with Marit MacArthur and Anna Mills
COUNT who_for starts with a student: 8
```

8 of 47. The `who_for` text is written once per resource, but a resource can carry many
roles. So the card speaks to whichever audience the writer had in mind that day, and
everybody else reads someone else's mail.

One of them contradicts itself in four lines. *"Peer and AI Review of Student Writing"*:

- For: "A student who wants to understand why their instructors are structuring AI use
  the way they are…"
- Skip if: "You want study techniques. **This is a conversation aimed at teachers about
  course design**…"

The skip line knows it is for teachers. The For line does not.

### 9.6 A designer's podcast is on my "used it a lot" shelf

*"Kris Puckett - Becoming an AI-native designer (Dive Club)"*, `roles: [designer,
non-technical, pm, student, teacher]`, `topics: [chat-prompting, claude-code, cowork,
skills]`, `who_for: "Designers wanting a deep, honest look at an AI-native design
practice."`

Confirmed live in the six-card teacher/confident list. Nothing in the title, summary,
who_for, topics or teaches fields mentions education. It is 1 of 6 cards at that level,
so it costs me 17% of the shelf.

`00-facts.md` says 29 of my 47 are only-this-role — the highest specialisation of any
role except developer. This card is one of the 18 that are shared, and it shows what
sharing costs when nobody re-reads the blurb afterwards.

### 9.7 The topic vocabulary cannot express my job

Eight topics (`ui.js:40`). Seven are Claude product features. The eighth, "limits and
safety", carries 25 of my 47 cards — confirmed live: `role=teacher&topic=safety` → "25
resources". A filter that removes 22 of 47 and mixes hallucination with FERPA with
assignment design is not a filter. It is a shelf labelled *miscellaneous*.

There is no topic word for integrity, assessment, policy, student data or safeguarding.
Until there is, no amount of new content will be findable, because the site has no word
for the thing I am looking for.

### 9.8 Dead data shipped to every visitor

```
python -c "... items with alt_skip_if ..."
items with unused alt_skip_if: 13 of 353 | stray lines: 23 | bytes: 2100
grep -rn "alt_skip_if" assets/ scripts/ *.html   → no matches
```

13 resources carry an `alt_skip_if` array. No JavaScript, no HTML and no script in the
repository reads it. It is downloaded by every visitor and rendered nowhere.

Worse, its contents are contaminated. The Kris Puckett podcast — a Stripe designer on
shaders — carries these among its five stray lines:

```
"You are already comfortable with Projects, or you need student-specific coursework
 examples. The framing is aimed at LSE educators."
"You are on a personal Claude account. Sharing across an organisation is the whole
 point of the video and you do not have it."
```

Those describe other resources. Skip lines from different items have pooled into one
record. Nobody can see it, because nothing renders the field — which is precisely why it
went unnoticed.

### 9.9 The page title says "Browse 1 Claude resources"

`browse.js:215`:

```js
document.title = "Browse " + out.length + " Claude resources — Learn Claude";
```

No singular case. Live at `browse.html?role=teacher&level=builder` the browser tab reads
**"Browse 1 Claude resources — Learn Claude"**. The visible count on the same page says
"1 resource" correctly, because `LC.countText` handles it. Two counters, one careful, one
not. If I bookmark my builder shelf, that is the text that sits in my bookmarks bar.

### 9.10 Publisher names are mangled domains

Rendered on live cards and resource pages: **"Aiassessmentscale"**, **"Unesco"**,
**"Eu"**, **"Au"**, **"Ed"**, **"Gov"**, **"Dayofai"**, **"Aifluencyframework"**,
**"Substack"**.

"Eu" is the European Commission. "Gov" is the UK Department for Education. "Ed" is the US
Department of Education. Four of my cards are credited to "Substack", which is a hosting
platform, not an author. On a directory whose whole pitch is judgment and provenance, the
provenance line is a lowercased domain with a capital letter on the front.

### 9.11 Answering both questions removes the search box

`index.html`, `.search-row.answered .input { visibility: hidden; max-width: 0; ... }`.
Once role and level are both set, the "Or describe what you want to do…" field collapses
and leaves the tab order. The design comment says the field "has nothing left to offer."
It had one thing left to offer: my actual question. Browse still has a search box, but
nothing on the home page tells me that, and by then I have already been sent to Browse
with a filter I did not want instead of the sentence I wanted to type.

## 10. The one thing that would make me leave and not come back

I type **"how do I stop students cheating"**, and the two resources in this entire
catalogue that answer it — *"Plagiarism and Academic Integrity 101 in the Age of AI"* and
*"Generative AI and Academic Integrity"* — are tagged `roles: ['student']` and are
invisible to a teacher.

That is the whole visit, in one line. The site sorted the cheating problem under the
people doing the cheating.

And when I look at what it did give me instead, the pattern holds: my eight policy cards
are all at "Nobody has looked at the content yet"; the single line telling me Claude is
18-plus is hidden in a skip note; and the top of my beginner shelf is a US-only sales
page the site itself calls claims and logos.

I did not come here to learn prompting. There are a hundred sites for that, and this one
is better than most of them at it. I came with the only question that can get me
disciplined, and this site does not have a word for it — not a topic, not a filter, not a
path step, not a role tag. Eight topics and every one of them is a product feature.

I close the tab. I ask the head of department instead. She does not have a badge that
says "Nobody has looked at the content yet."

## 11. What is genuinely good (be honest, but brief)

I will not pretend this is a bad website. It is a good website pointed slightly away from
me.

- **The Skip-if line is the best idea here.** No other directory tells me who should not
  bother. "Skip if you are outside England." "Skip if you want anything practical for
  Monday - it is a competency map, not training." That saved me real minutes. Keep it,
  and never let it become marketing.
- **The badges are honest.** "Found only. We found it and sorted it. Nobody has looked at
  the content yet" is a humiliating thing to print about your own work, and printing it
  is why I trust the rest. Most sites would have called it "curated".
- **The critical entries are present.** *"Why is Claude for Teachers? (critical hands-on
  review)"* and *"Anthropic launched Claude for Teachers. We blocked it for our
  district."* sit next to Anthropic's own announcement. A directory that links the
  counter-argument is a directory run by an adult.
- **The teaching-*with*-Claude shelf is genuinely useful.** The Artifacts tutorial, the
  Projects tutorial, the pK-12 courses, the K-12 skills repo. If my question had been
  "how do I write worksheets faster", I would have had a good hour here.
- **The AI Assessment Scale is a real find.** Whoever put that in the catalogue knew
  something. It appears to be the most directly usable thing on the site for anyone who
  sets assessments. It probably deserves to be the first card a teacher sees, not the
  last, and it seems to me that reading it properly would take one person one afternoon.
- **The front door is honest about counts.** "1 resource. Remove a filter to see more."
  It did not pad the builder shelf to make itself look bigger. That restraint is rare.

The gap is not effort. It is that this catalogue was built around *the tool* and I need
one built around *the classroom*.

## Checklist — every line ticked or the file is not finished
- [x] I opened the live site — home, Browse at all four teacher levels, Paths, three
      resource pages, plus `curl` for `index`, `paths.html?id=first-week`,
      `data/paths.js` and `data/items.js` (all HTTP 200)
- [x] I tried all four levels — never-used 16, basic 24, confident 6, builder 1;
      confident and builder confirmed live on screen
- [x] I quoted at least 5 real titles or lines — 15+ verbatim titles, plus verbatim
      `For:` and `Skip if:` lines from AIAS, Vanderbilt, Kris Puckett, Claude for higher
      education, the K-12 product page, Agent Skills for K-12 Teachers, AI Fluency for
      students, and Peer and AI Review of Student Writing
- [x] Every number I used is in 00-facts.md or I show the command — `role-view.py`,
      `test-search.py`, `grep`, `curl -w`, and the `python -c` one-liners are all printed
      above with their output
- [x] I looked at a phone width — `site.css:590` `@media (max-width: 768px)` and the
      `browse.js` sheet builder; I did not resize the shared browser window, because four
      other agents were working in it
- [x] I found at least one thing nobody has mentioned before — 9.1 (the whole policy
      shelf is unread and undated while Anthropic's own pages hold the top badge), 9.2
      (0 of 16 path steps is tagged `teacher`, and `paths.js` never reads `roles`), 9.3
      (18-plus stated once, in a skip line), 9.4 (the outdated warning is computed then
      dropped on the resource page), 9.5 (8 cards address a student), 9.6 (a designer's
      podcast on the teacher shelf), 9.7 (`safety` carries 25 of 47), 9.8 (`alt_skip_if`
      is dead, contaminated data shipped to everyone), 9.9 ("Browse 1 Claude resources"),
      9.10 (publishers rendered as mangled domains), 9.11 (the search box is removed once
      both questions are answered)
