# Attack 3: not a coder
Written as someone who is not a coder, 2026-09-06. Site version: 9deb0db.

I work in an office. I do not write code and I will not start. I have typed a few things
into Claude. I want to be better at it for my job. I gave the site one hour.

All numbers below come from `docs/attack/00-facts.md`, `docs/STATUS.md`, or a page I
opened and can quote.

---

## 1. The first 60 seconds

I opened `https://mojtaba-alehosseini.github.io/learn-claude/`.

The page says:

> Find what's worth your time.
>
> **I'm a [role] and I've [level].**
>
> Who are you?

Then ten buttons, then "588 resources, each with a reason to skip it and the date we last
looked."

I understood it at once. Two questions, my own words, no sign-up. That is good.

Then I sat and watched it, which is what the plan asked me to do. Over about 15 seconds a
picture on the right changed four times — an easel, a bar chart, a paintbrush, a book —
and a different role button lit up each time: `a designer`, `working with data`,
`a teacher`, `a researcher`. So the page is showing me itself filling the sentence in.

**But the sentence never fills in.** In every screenshot I took, across six different
highlighted buttons, the headline still read the literal words `I'm a [role] and I've
[level].` The square brackets stay. I know what square brackets in a sentence mean,
because I see them in mail-merge letters that went out wrong: **"Dear [FIRST NAME]"**.
That is what the biggest text on the home page looks like for the first ten seconds. A
demo that lights up the buttons but leaves `[role]` sitting there tells me the page is
half-built.

It repairs itself the moment I click. `I'm not a coder and I've [level].` Then
`I'm not a coder and I've never used Claude.` That is a nice touch. It arrives too late.

---

## 2. Does the front door work for me (all four levels, with what I was shown)

I picked **not a coder** every time. The page then said **"134 resources match so far."**
Then I picked each level in turn.

| level I picked | sentence the page built | count it gave me | Browse page title |
|---|---|---|---|
| never used Claude | "I'm not a coder and I've never used Claude." | 52 resources match so far | Browse 52 Claude resources |
| used it a little | "I'm not a coder and I've used it a little." | 63 resources match so far | Browse 63 Claude resources |
| used it a lot | "I'm not a coder and I've used it a lot." | 17 resources match so far | Browse 17 Claude resources |
| built things with it | (front door, then Browse) | 2 | Browse 2 Claude resources |

The counts on the home page and on Browse agree every time. The URL is readable
(`browse.html?role=non-technical&level=never-used`). No account, no cookie banner, no
pop-up. That part is honest and quick.

Two things about the shape of it:

- **134 of the 588 are mine.** The home page shouts 588. Whichever of the ten buttons I
  press, most of the site is not for me. That is fine, but 588 is a number for the owner,
  not for me.
- **The drop is a cliff.** 52 → 63 → 17 → 2. The moment I say I am good at Claude, the
  site nearly empties. At "used it a lot" I get 17 things, and I will show in section 3
  that 12 of them need software I do not have.

**At "built things with it" the site handles the emptiness well.** It says:

> Only 2 at "built things with it" for not a coder.
> The level below, "used it a lot", has 17. **Add "used it a lot" too**
>
> Too few to pick from — these are all of them.

That is the best writing on the site. It admits the shelf is bare, tells me the real
number next door, and gives me one button. I pressed it (as a URL:
`browse.html?role=non-technical&level=builder,confident`) and got **19 resources**, which
is 2 + 17 exactly. The offer keeps its promise.

**But taking the offer costs me the site's best feature.** At 2 resources I get "Too few
to pick from". At 17 I get "Start with these three". At 19 — after I accept the site's own
suggestion — I get **neither**. I checked: the words "Start with these three", "Too few to
pick from" and "Everything else for you" are all absent from the 19-result page. So the
one-click help hands me an unsorted list of 19 and takes away the three picks. Nobody has
said this before.

---

## 3. What the catalogue actually gives me (are these really for me?)

Short answer: at level 2 yes, at level 1 mostly, at level 3 almost not at all.

### The "not a coder" filter still returns other people's jobs

I looked at all **134** cards under `role=non-technical` and read every `For:` line. Ten
name a specific job. Six of those name a job that is not mine and is not general office
work:

| card | its own `For:` line |
|---|---|
| Claude AI for Teachers: Complete Beginner's Guide to Getting Started (Projects, Prompts & More) | "Classroom teachers starting from zero who want examples from their own job **rather than generic office tasks**." |
| Claude Design Fundamentals | "A designer who has never opened Claude and wants a structured route…" |
| Claude Design: The Complete Guide | "Working designers evaluating Claude Design seriously…" |
| Claude for nonprofits partnership guide for all users | "Nonprofit staff new to Claude…" |
| Using the Blender Connector in Claude | "Blender users who want Claude to work with their live open scene." |
| Using the Function Connector in Claude | "A Function membership holder in the US wanting to ask questions about their own lab results." |

The first one is the killer. `00-facts.md` says Rule B "reads each card's own `who_for`
line and drops a tag the line denies." That card's `who_for` line **denies me by name** —
it says it is for teachers "rather than generic office tasks", and generic office tasks
are the whole of my job — and it still carries the `not a coder` tag. The rule failed on
the exact test the rule was written for.

The Function connector one is worse in a different way. It is in my **beginner** list. To
use it I need a paid US lab-testing membership, a Claude Pro or Max subscription, and a US
address. That is not a role. That is three walls.

### Level 3 is a list of things I cannot do

At "used it a lot" I get 17 cards: 3 picks and "Everything else for you (14)". I read all
14 `Skip if:` lines. **12 of the 14 name something I would have to have first**:

- Create health and exercise notes — "the Notes connector is a Mac-only desktop extension… so it doesn't work in a browser or on Windows at all"
- Turn text threads to researched notes — "effectively macOS/Apple-ecosystem only"
- Daily bookends — needs a "Daily" folder in a Cowork project "plus at least one of Google Calendar/Slack/Gmail connected"
- Slack and Teams message sweep — "Needs Slack, Microsoft 365 and Gmail all connected"
- Turn emails into an event tracker — "Needs the Gmail integration enabled"
- Plan your career path — "Needs your resume in Google Drive with the connector enabled"
- Financial analysis workflows with Claude — "Every workflow needs separately licensed data subscriptions - Daloopa, S&P Global, FactSet - already connected; **nothing here works without them**"
- Stress-test your financial plan across scenarios — "Needs your actual tax returns, investment statements, Social Security estimates and budget uploaded"
- Handle a request while away from your keyboard — "the Claude desktop app must stay running with a keep-awake toggle set… none of which is on by default"
- Using Claude Cowork for sales — "Needs the Sales plugin installed plus your own CRM, warehouse and call-recording connectors"
- Using Research — "paid plans only (Pro, Max, Team, Enterprise)"
- Let Claude use your computer in Cowork — "computer use has no sandbox, no safeguards are perfect, and they do not recommend it on apps holding healthcare, financial or other personal records"

Twelve of fourteen. And 12 of the 14 come from one publisher, Anthropic Academy. So the
reward for telling the site I am good at Claude is a menu of Anthropic recipes that need
an IT department. This is the level where a real office worker gives up.

### The five collection cards

Sales, Legal, HR, Finance, Operations. **They did not trip me up, because none of them
appears in my 134.** I only met them by browsing all 588.

When I read them they are clear enough — the `For:` line saves them — but they are five
cards with one sentence between them. All five `Skip if:` lines begin the same way:

- Finance: "This is a menu, not a lesson: these recipes assume…"
- HR: "This is a menu, not a lesson: every recipe wants…"
- Legal: "This is a menu, not a lesson: nearly every recipe waits on…"
- Operations: "This is a menu, not a lesson: every recipe wants…"
- Sales: "This is a menu, not a lesson: every recipe needs…"

Two of them then say **"none of them teaches you anything about Claude itself."** A site
called Learn Claude is carrying cards it says teach me nothing about Claude. That is
honest, and it is also an argument for removing them.

### Jargon that leaked into my lists

Read out loud, to me, in cards tagged for a person who does not code:

- "this stops at general craft and never gets into **evals** or model-specific tuning" (top pick, level 2)
- "it teaches **byte-pair encoding** for pricing intuition"
- "this assumes basics and jumps into **MCP connectors** and multi-agent setups" (top pick, level 3)
- "names **Claude Opus 5** specifically and suggests raising the **effort level**"
- "The only page **in this whole harvest**…" (top pick, level 1)

"Harvest" is the worst. That is the owner's word for his own database. It is printed in
the first `Skip if:` a brand-new visitor reads.

---

## 4. Paths

There are 7 paths (STATUS.md: 7 paths, 36 steps). I read all seven headers.

**There is exactly one for me: "Your first week with Claude."** Its own line says
"For not a coder, a student, a teacher, running a business" and its description is
"Anyone who has just opened Claude and does not know what to do next."

So the answer to "is there one at *my* level rather than at the start" is **no**. There is
one route for a non-coder and it begins at zero. If I say I have "used it a lot" — 17
resources — the site has no route for me at all. Every other path names a different job:
a developer, a writer, a product manager, a researcher, working with data, a designer.

The path page also gives me no way to filter. I have to read seven blocks and work out
which one has my label in it.

**I followed it.** `paths.html?id=first-week`. It is good. Six steps, and each one says
why it is there and why it is in that place:

> Step 3 · Course — **Claude 101** … "By now you have had a generic, disappointing answer.
> Anthropic's own beginner course is the fix"
>
> Step 6 · Docs — **Get started with Claude Cowork (Help Center)** … "Last, because working
> on your own files only makes sense once you trust the answers."

That is real teaching. It is the best thing on this site.

Three problems with it:

1. **Three different time claims on one page.** The header says "6 steps · about 4 hours".
   The intro says "step 3 is Anthropic's own **2.5-hour** Claude 101". The chip on step 3
   says **"half a day"**. If I am deciding whether this fits in an evening, "2.5 hours" and
   "half a day" are not the same answer.
2. **Every one of the six steps says "No publish date given."** Not one. So on the single
   route built for me, the site's third front-page promise — "We show the date" — delivers
   nothing at all.
3. **Step 1 is a personal newsletter.** "Claude is not one tool. It's six." by Ruben
   Hassid, and the site's own note warns me: "The author writes in a promotional,
   personal-brand newsletter style with frequent subscribe prompts". It has no date. An
   undated article listing how many products Claude has, on a product the site tells me
   "changes every few months", is the first thing I am sent to.

Small thing, but it made me distrust the page: on `paths.html` several step names are cut
off in the text itself — "The new rules of context engineering for Cla…", "Claude for
Product Managers: Synthesizing Us…". I checked; the `…` is in the HTML, not a CSS effect.
There is no hover text and no way to see the rest. None of those are in my path, so it
costs me nothing, but it is a page whose whole job is to list steps.

---

## 5. The card and the resource page

### The card

A card gives me: a badge, a title, a publisher, three chips (format / time / cost), a
`For:` line, a `Skip if:` line, and two dates. It is a good card. I can decide from it.

Two things are wrong with it.

**The badge cannot be read on a phone.** The badge on my first card says `Skimmed`. Nothing
on the Browse page says what that means. I looked at the markup: it is
`<span class="badge badge-previewed" title="We read the outline or a free sample…">`. A
`title` is a mouse-hover tooltip. A `<span>` cannot take keyboard focus. The full wording
does exist on the page but inside `<div class="visually-hidden">`, which is for screen
readers only. **So on a phone there is no way to find out what "Skimmed" means from a
card.** "We say how we checked" is the site's second promise on the home page, and on the
device most people use, the label is a word with no definition. On the resource page the
badge is a link to `how-we-check.html#tier-ai-reviewed`, which works. On Browse it is not.

**"Skip if:" does not always contain a skip.** The home page promises "Every entry has a
`Skip if:` line." Technically true. Read what it says. My number-one recommendation at
level 1, "Explore what Claude can do for you":

> **Skip if:** The only page in this whole harvest with a genuinely zero-prerequisite start
> - just describe your role - **so there's nothing to skip** unless you already know
> Claude's capabilities well enough not to need a personalized map.

And at level 2, "Use Claude Cowork safely":

> **Skip if: Nothing** — worth reading before your first real Cowork task regardless of
> experience level.

On a phone the first one runs to seven lines, in the biggest and boldest type on the card,
to tell me there is nothing to skip. The whole promise of the site is that it warns me off
things. A warning that says "no warning" is an advert wearing a warning's clothes.

### The resource pages

I opened three.

**`resource.html?id=r-fc4a37f0dd` — "Claude is not one tool. It's six."** Good page. What
it teaches (three bullets), Who it's for, Skip it if, "Where this fits — This is step 1 of
6 in Your first week with Claude", how it was checked, and "Open on Ruben Hassid" going to
`ruben.substack.com`. **Would I click through? Yes, but with my guard up** — undated, a
Substack, and the site itself warns me about the subscribe prompts.

**`resource.html?id=r-d91d3354ec` — "Mastering Claude Cowork & AI Agents in 5 hours"
(Udemy).** This is one of only **three** things the site picks for me at "used it a lot".
It costs money. The page says `pay once`. **It does not say how much.** Not on the card,
not on the resource page, nowhere. **Would I click through? No.** I am not clicking into
Udemy to discover a price the directory could have told me. Its "Skip it if" also says the
course "jumps into MCP connectors and multi-agent setups", which is language for somebody
else.

**`resource.html?id=r-76de44b7a7` — "Anthropic launched Claude for Teachers. We blocked it
for our district."** A `Found only` card. Covered in section 8.

---

## 6. Search, in my words

I typed each of these as a whole sentence into the Browse search box, on the full 588, with
no filters.

| # | what I typed | top 3 I was shown | verdict | why |
|---|---|---|---|---|
| 1 | how do I use claude to take notes in my meetings | 1. Prepare and plan from your calendar · 2. Prep call look-ahead · 3. Feedback synthesis to prioritized themes | bad | 31 hits and not one of them takes a note. #1 is an evening calendar routine needing Claude in Chrome plus Google Calendar and Gmail; #2 is a Monday look-ahead "for a business owner or manager" needing the Google Calendar connector; #3 is for "Product managers turning scattered feedback into a roadmap-ready brief" and wants Slack/Linear/Intercom/Zendesk. The site matched the word "meetings" and ignored "notes". |
| 2 | is it safe to upload work documents to claude | 1. Anthropic Claude for Absolute Beginners · 2. How Can I Create and Manage Projects? · 3. Getting started with Claude.ai | bad | 36 hits, and the top three are a paid beginner course, a Projects page "For: Writers and editors", and a first-time video tour. None is about safety. The right card exists and the site put it **9th**: "How long do you store my data?", whose own `For:` line reads "Anyone about to **paste work data into Claude**". "Upload files to Claude (Help Center)" was 12th. I asked in the card's own words and got the card ninth. |
| 3 | how do I stop claude from making things up | 1. Reduce hallucinations · 2. 4 Lines You Should Include in Your Claude Skill · 3. Claude Code settings and permission rules | ok | #1 is exactly right — "For: Any analyst worried about confidently-wrong output. Assumes no coding." Then it falls apart: #2 is about writing a `SKILL.md` file and #3 is Claude Code permission rules for keeping a tool "away from part of a repository". Two of my three answers are for programmers. |
| 4 | can claude write emails in my own writing style | 1. Write in my voice · 2. How I Use Claude Cowork to Write With AI in My Voice · 3. How to Stop Claude Writing Like an AI | ok | The best result of the five. #1 and #3 are right for me and I would open both. #2 is explicitly "For: **Technically comfortable** writers", so one of my three is again for someone else. |
| 5 | I have never used claude what should I do first | 1. Get started with Claude · 2. Claude 101 (DataCamp) · 3. Claude Code 101 | ok | #1 says "For: Someone who has literally never used Claude before." Perfect. #2 is a beginner course. #3 is a trap: "Claude Code 101" looks like the official 101 to a beginner, and it is "For: **Engineers** who have not used an agentic coding tool before". Putting that third, to a question that begins "I have never used claude", is how a person ends up in a terminal on day one. |

**The same question asked two ways.** I asked question 3 again in words I would use if I
did not know the word "hallucination":

- **"how do I stop claude from making things up"** → 25 hits. #1 is **Reduce hallucinations**.
- **"why does claude give me answers that are not true"** → 41 hits. Top three: **Answer the
  ad-hoc data question**, **AI Student Research Guide: Prompt Engineering**, **What are some
  things I can use Claude for?**. Positions 5 to 8 are "Building agents with the Claude
  Agent SDK", "Use Claude Cowork safely", "Claude Code for PMs: The Beginner's Guide",
  "Claude Code for Designers: The Complete Guide".

**The site does not agree with itself.** "Reduce hallucinations" fell from **1st to 34th**.
"Claude is providing incorrect or misleading responses. What's going on?" is **30th**. And
"Why do AI models hallucinate?" — which is **step 5 of the only path the site has for me** —
**is not in the 41 results at all**.

I got the same result on question 2, from the other side. I asked
**"what happens to my company files after I paste them into claude"** and got #1 "How long
do you store my data?" and #2 "Is my data used for model training? (Privacy Center)" —
both correct. The same question worded as "is it safe to upload work documents to claude"
put the first of those 9th and the second nowhere in the top three.

So the search does hold the right answers. Whether I see them depends on which synonym I
happened to reach for. That is not a search. That is a coin toss with good odds.

---

## 7. On a phone

I set the window to 375×812 and looked at the home page, Browse and a card.

**This is the best-built part of the site.** Home page: the illustration is dropped, the
ten role buttons wrap into a clean two-column stack, the tap targets are large, the type is
big and readable. Browse: Search and Sort at the top, my two filter chips with an `×` on
each, "52 resources", then the cards, with a sticky **Filters** button pinned to the bottom
of the screen. That is the right pattern and it works. No sideways scrolling anywhere I
looked.

Three complaints:

1. **The badge is dead on a phone.** As in section 5 — `Skimmed` is a hover tooltip. There
   is nothing to tap.
2. **The `Skip if:` swamps the card.** It is set in a serif face, larger than the `For:`
   line above it, and on my first card it ran to **seven lines** to say there is nothing to
   skip. The `For:` line — the part that tells me whether this is mine — is smaller and
   above it.
3. **The pick reason repeats the card.** Under the first card the reason says "The only
   candidate here with a genuinely zero-prerequisite start", and the `Skip if:` three
   inches above says "The only page in this whole harvest with a genuinely zero-prerequisite
   start". On a narrow screen I read the same phrase twice inside one thumb-scroll.

---

## 8. What changed since Attack 2 — my verdict on each

**Does the "not a coder" filter still return other people's jobs?**
**Yes.** 6 of the 134 cards have a `For:` line naming a job that is not mine. The worst is
"Claude AI for Teachers", whose own line says it is for teachers' work "rather than generic
office tasks" and which still carries my tag. Evidence in section 3.

**Do the five collection cards make sense to me or trip me up?**
Neither. **They never reach me** — none of Sales, Legal, HR, Finance or Operations appears
in my 134. When I found them by browsing all 588 they were readable but interchangeable,
and two of them say outright "none of them teaches you anything about Claude itself".

**Do the stripped `listed` cards read as honest or broken?**
**Honest, and one of them contradicts itself.** All three carry the same line:

> **Skip if:** You want something we have read. **We have not opened this one yet.**

Nobody could misread that. But the first one, "Head of Claude Code: What happens after
coding is solved (Boris Cherny)", also carries **"Published 19 Feb 2026 · Updated 13 Apr
2026"** on the same card. A card that tells me nobody has opened the page, and then tells
me the day the page was updated, is asking me to hold two things at once. The resource page
does the same in a smaller space: the badge block says "Nobody has looked at the content
yet" and four lines lower it says "**Checked** 21 Aug 2026". Checked how?

**Can you find out what the "how well checked" badge on a card means?**
**On a desktop, by hovering. On a phone, no.** Full evidence in section 5. It is explained
properly on `how-we-check.html`, but that is two clicks and a scroll away from the card I
am looking at, and nothing on the card says the page exists.

**Do the date lines make the site look maintained?**
**They make it look honestly abandoned.** Every card carries "Checked 5 Sep 2026" or
similar — yesterday, in effect — so somebody is clearly here. But 442 of 588 say "No publish
date given" (STATUS.md, 75%), including **all six steps of my path**, and the ones with real
dates carry "· over a year ago, may not match Claude today". I trust the *checking*. I have
no idea how old the *material* is. Those are not the same reassurance, and the site's third
promise ("We show the date") is the one it keeps least.

**Does naming one person and Claude as "we" raise or lower your trust?**
**It raises my trust in the site and lowers my trust in the contents, and that is the right
way round.** `how-we-check.html` says: "One person makes this site - a researcher at the
Technical University of Denmark… The reading is done by Claude… Claude opens the pages,
writes the summary, the who-it-is-for and the who-should-skip-it lines, and chooses the
three picks. A person sets the rules… and has not yet read a single resource end to end."

I have never seen a site admit that. I believe everything else on the page more because of
it. But then I go back to Browse and I remember: every `For:` and every `Skip if:` I have
been reading — the judgment that the home page says is the whole point — was written by an
AI that skimmed the outline, and no human has checked it. The picks block says "picked by
AI · 6 Sep 2026" right on it. So the honesty is real and the product is thinner than the
first screen suggests.

One thing spoils it. My level-3 top pick's reason ends:

> "Rows arrived in this pool **on 2026-09-06** that do end in a customised skill, which is
> why this sentence no longer claims to be the only one."

That is a note from the owner to himself, dated, published to me. It means nothing to a
visitor. It is the clearest sign that the "we" writing this is not always writing to me.

**Share a link.**
**Broken, and this is the one that would stop the site spreading.** Section 10, finding 3.

**Watch the home page without touching it.**
The buttons light up and the picture changes; the headline stays `[role]` / `[level]`.
Section 1.

**Change the sort control.**
`Newest first` does not mean newest. Section 10, finding 2. `Shortest first` is correct
(15 min ×38, then 1 hour ×5, then half a day ×4, then several days ×1) except that the
picks block sits above it unsorted, so position 3 on a "Shortest first" page is a "half a
day" course.

**Look for a path at your level.**
There is none. One path, and it starts at zero. Section 4.

**Prices — is it clear what I would pay before I click?**
**No.** I filtered `cost=paid-once` (10 rows) and `cost=subscription` (16 rows). That is 26
rows that cost money. **Four of them show a price**: "from $995", "from $2,999", "from
$3,000", "from $49". The other **22 show only the words "pay once" or "subscription"** —
including "Mastering Claude Cowork & AI Agents in 5 hours", which is one of the **three**
things the site picks for me at my level, and "Anthropic Claude for Absolute Beginners",
which is in my beginner list. The four that do show a price are the ones in the thousands,
for other people's roles.

**The picks block.**
It behaved correctly for me at every level: three at 52, three at 63, three at 17, and
"Too few to pick from — these are all of them" at 2. The reasons are the strongest writing
on the site — "This pool is thick with beginner tours, and this is the only one whose own
notes rule out complete beginners". **Would I open those three?** At level 1, yes, all
three. At level 3, one of the three is a paid Udemy course with no price, so: two of three.

**The thin-level offer.**
Makes sense, and I would take it — and then I would lose the picks. Section 2.

---

## 9. Content quality — the three worst entries I was shown, quoted

**1. "Using the Function Connector in Claude" — shown to me at *never used Claude*.**

> **For:** A Function membership holder in the US wanting to ask questions about their own
> lab results.
>
> **Skip if:** Three simultaneous gates - a paid Function lab-testing membership, a Claude
> Pro or Max subscription, and a US location - and the page states plainly it's not for
> medical advice, diagnosis, or treatment recommendations.

I am a beginner in an office. This is a blood-test service. The card's own `Skip if:`
disqualifies almost every human who will ever read it. It is on the beginner shelf.

**2. "Claude AI for Teachers: Complete Beginner's Guide…" — shown to me at *never used
Claude*.**

> **For:** Classroom teachers starting from zero who want examples from their own job
> rather than generic office tasks.

The card says, in its own words, that it is not for generic office tasks. Generic office
tasks are my job. The tag survived a rule written to catch exactly this.

**3. "Explore what Claude can do for you" — my number one recommendation at *never used
Claude*.**

> **Skip if:** The only page in this whole harvest with a genuinely zero-prerequisite start
> - just describe your role - so there's nothing to skip unless you already know Claude's
> capabilities well enough not to need a personalized map.

The first `Skip if:` a brand-new visitor ever reads contains the owner's private word for
his database, and contains no reason to skip. It is the site's headline promise failing on
the site's first card.

Dishonourable mention: **"Using the Blender Connector in Claude"** — "For: Blender users who
want Claude to work with their live open scene" — also on my beginner shelf.

---

## 10. Everything that is broken, ranked (evidence for each)

Ranked by what it costs me, not by how hard it is to fix.

**1. Search gives a different answer to the same question depending on the words I pick.**
`browse.html?q=how do I stop claude from making things up` → "Reduce hallucinations" is
**1st**. `browse.html?q=why does claude give me answers that are not true` → "Reduce
hallucinations" is **34th**, "Claude is providing incorrect or misleading responses" is
**30th**, and "Why do AI models hallucinate?" is **not returned at all** among the 41 hits —
although it is step 5 of the only path the site has for me. Top of that second list:
"Answer the ad-hoc data question", "AI Student Research Guide: Prompt Engineering",
"Building agents with the Claude Agent SDK", "Claude Code for Designers". The same split
happened on my file-safety question in the other direction: "what happens to my company
files after I paste them into claude" put "How long do you store my data?" **1st**, and
"is it safe to upload work documents to claude" put the same card **9th**.
**Expected:** two plain-English wordings of one question return roughly the same shelf.
**Harms:** everybody who does not already know the technical word for their problem — which
is exactly the person this site is for. A visitor does not know they got the bad wording.
They conclude the site has nothing.

**2. "Newest first" is not newest.**
`browse.html?role=non-technical&level=never-used`, Sort → **Newest first**. Position 4 (the
first card after the picks) is "Claude AI Step-by-Step: The Beginner's Blueprint for Real
Results — **Published 13 Jul 2026**". Position 42 is "How up-to-date is Claude's training
data? — **Updated 1 Sep 2026**". Position 46 is "What are artifacts and how do I use them? —
**Updated 3 Sep 2026**". So the two most recently touched cards on the page are 42nd and
46th of 52, under a control labelled Newest first, with their fresher dates printed on
their faces. 41 of the 49 non-pick cards (84%) carry no publish date, so the sort does
nothing at all for most of the list.
**Expected:** "Newest first" puts the thing dated three days ago near the top, or the
control says which date it sorts on.
**Harms:** anyone who reaches for the sort because the site told them Claude "changes every
few months". The control is there to answer that worry and it answers it wrongly.

**3. Every shared link looks identical.**
`resource.html?id=r-d91d3354ec` has browser title "Mastering Claude Cowork & AI Agents in 5
hours — Learn Claude" but `og:title` = **"Resource — Learn Claude"** and `og:description` =
"What this resource teaches, who it is for, who should skip it, and how thoroughly we
checked it." `browse.html?role=non-technical&level=never-used` has title "Browse 52 Claude
resources — Learn Claude" but `og:title` = **"Browse — Learn Claude"**. There is no
`og:image` and no `og:url` on any page I checked.
**Expected:** when I paste a link in Teams or WhatsApp, the preview names the thing I am
sending.
**Harms:** everybody, and the site most of all. The way a directory like this spreads in an
office is one person pasting a link. Right now every paste — a course, a filtered list, a
resource page — produces the same grey card saying "Resource — Learn Claude". There is no
reason for a colleague to click it.

**4. At my strongest level, 12 of the 14 things offered need software I do not have.**
`browse.html?role=non-technical&level=confident`, "Everything else for you (14)". Quoted in
section 3: Mac-only ×2, Google/Slack/Microsoft connectors ×4, paid data subscriptions
(Daloopa, S&P Global, FactSet) ×1, personal tax returns ×1, desktop-app setup ×1, Sales
plugin plus CRM ×1, paid plan only ×1, plus one that Anthropic itself advises against on
records. 12 of 14, and 12 of 14 from one publisher.
**Expected:** a shelf for an experienced non-coder holds things an experienced non-coder can
do today.
**Harms:** the person most likely to become a regular reader. It is the level where the site
stops being useful and starts being a catalogue of what I am locked out of.

**5. On a phone I cannot find out what the badge on a card means.**
The badge is `<span class="badge badge-previewed" title="…">Skimmed</span>`. A `title` needs
a mouse. The wording also sits in `<div class="visually-hidden">`, which is for screen
readers. Nothing on `browse.html` explains "Skimmed" in visible text and no card links to
the explanation.
**Expected:** the label the site is proudest of can be read on the device most people use.
**Harms:** every phone visitor. "We say how we checked" is promise number two on the home
page.

**6. 22 of the 26 things that cost money show no price.**
`cost=paid-once` (10) and `cost=subscription` (16). Four price chips exist: "from $995",
"from $2,999", "from $3,000", "from $49". Neither the card nor the resource page for
"Mastering Claude Cowork & AI Agents in 5 hours" gives a number, and that course is one of
only three picks shown to me at my level.
**Expected:** "we say what it costs" is a directory's minimum.
**Harms:** anyone deciding whether to click, and it makes the picks block feel like an
advert at the one moment it recommends something paid.

**7. The home page headline reads as a broken template for the first ten seconds.**
Six screenshots, six different highlighted buttons, one unchanged headline:
`I'm a [role] and I've [level].` The picture and the buttons animate; the sentence they are
supposed to be filling does not.
**Expected:** if the demo lights up "a designer", the sentence says "I'm a designer".
**Harms:** first-time visitors, at the exact second they decide whether the site is
finished.

**8. Accepting the site's own thin-level suggestion removes the picks.**
`browse.html?role=non-technical&level=builder` offers "Add "used it a lot" too". Taking it
gives 19 resources and **no** "Start with these three", **no** "Too few to pick from" and
**no** "Everything else for you".
**Expected:** the site's one-click help does not take away the site's best feature.
**Harms:** the small number of advanced non-coders, who are the ones the offer is for.

**9. A card says nobody has opened it and then gives its update date.**
"Head of Claude Code: What happens after coding is solved (Boris Cherny)" — badge **Found
only**, "We have not opened this one yet", and on the same card **"Published 19 Feb 2026 ·
Updated 13 Apr 2026"**. The resource page for another `Found only` row says "Nobody has
looked at the content yet" and, four lines down, "Checked 21 Aug 2026".
**Expected:** one story per card.
**Harms:** small — 3 of 588, and none in my lists — but it is the site's honesty label
contradicting itself, which is the one thing it cannot afford.

**10. Internal notes are printed as recommendations.**
Top pick at `level=confident`: "Rows arrived in this pool on 2026-09-06 that do end in a
customised skill, which is why this sentence no longer claims to be the only one." Also
"the only page in this whole **harvest**".
**Expected:** the reason a thing is recommended is written to the reader.
**Harms:** trust, quietly. It tells me I am reading somebody's working notes.

**11. Path step names are cut off with no way to see them.**
`paths.html`: "The new rules of context engineering for Cla…", "Maximizing the value of your
Claude Code ses…", "Claude for Product Managers: Synthesizing Us…". The `…` is in the text
itself, with no `title` attribute.
**Expected:** a page that lists steps lists the whole step name.
**Harms:** other roles more than me — none of my six steps is truncated.

**12. Three ways to say how long step 3 takes, on one page.**
`paths.html?id=first-week`: header "about 4 hours", prose "2.5-hour Claude 101", chip "half
a day".
**Expected:** one number.
**Harms:** anyone budgeting an evening.

---

## 11. The one thing that would make me leave and not come back

The search giving me a different answer depending on which everyday word I happened to use.

I did not come here to browse. I came with a question. I typed
**"why does claude give me answers that are not true"** — which is how a person who does not
know the word "hallucination" says it — and the site handed me "Answer the ad-hoc data
question", a student prompt-engineering guide, and "Building agents with the Claude Agent
SDK". The right page was 34th. The video that the site itself put at step 5 of the only
path it has for me was not in the results at all.

I would have closed the tab there. I would not have known that the same site, asked with
the word "making things up", puts the right answer first. I would have concluded it does
not have what I need, and that conclusion would have been wrong — which is worse than a site
that really has nothing, because there was no way for me to find out.

---

## 12. What is genuinely good (honest, brief)

- **The two questions.** Ten plain job names, four plain levels, a sentence that builds
  itself, a live count before I commit. No sign-up, no cookie wall, no email box.
- **The `For:` line.** One sentence that tells me whether a thing is mine. It is the reason
  to use this instead of a search engine, and it is right far more often than it is wrong.
- **The best `Skip if:` lines are worth money.** "Every workflow needs separately licensed
  data subscriptions - Daloopa, S&P Global, FactSet - already connected; nothing here works
  without them." That saved me an hour. Nobody else writes this down.
- **The path reasons.** "Last, because working on your own files only makes sense once you
  trust the answers." That is teaching, not listing.
- **The thin-cell honesty.** "Only 2 at 'built things with it' for not a coder… Add 'used it
  a lot' too" and "Too few to pick from — these are all of them". Most sites would have
  padded it.
- **`how-we-check.html`.** "has not yet read a single resource end to end", "0 Read in full",
  "It needs a GitHub account, which is a real barrier and we know it". I do not trust the
  contents more after reading it, but I trust the person more, and that is rarer.
- **The phone layout.** Genuinely well built. The sticky Filters button is the right answer.
- **The one-click report link** on each resource page, with the resource, the link and the
  page pre-filled. The GitHub wall is still a wall, but the effort is visible.

---

## 13. Would I come back, and what one thing would make me?

Yes — but not for the search, and not on my phone. I would come back for one thing: the
path. Six steps, in order, each one telling me why it is there. That is the only place on
the internet I have found somebody willing to say "read this one third, and here is why".
I would bookmark `paths.html?id=first-week`, work through it over a fortnight, and I would
probably send it to two people on my team.

Then I would run out of site. There is one path for me, and it stops where a beginner
stops. When I come back in a month knowing more, the site has nothing at my level except
seventeen Anthropic recipes that want my Gmail, my Slack, my tax returns and a Mac.

So: one thing.

**Write me a second path.** Call it "Your second month". Six steps, same voice, for someone
who has used Claude for a while and still only has a browser, a work laptop and no
permission to install anything. No connectors, no desktop app, no plugin, no paid plan.
Just the next six things worth doing.

That is what would bring me back, and it is a bigger job than fixing the sort control, and
it is worth more. The site already knows how to do it. It has done it once, for people who
have never opened Claude, and it did it well. It has simply never written the version for
the person who came back.

---

## Checklist
- [x] I opened the live site
- [x] I tried all four levels
- [x] I quoted at least 5 real titles or lines from the site
- [x] Every number I used is in 00-facts.md, STATUS.md, or quoted from the site
- [x] I looked at a phone width
- [x] I read no file under scripts/ or data/
- [x] I found at least one thing nobody has mentioned before
