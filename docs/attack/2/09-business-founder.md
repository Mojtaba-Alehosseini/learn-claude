# Attack 2: running a business
Written as a small-business owner, 2026-09-05. Live site only:
`https://mojtaba-alehosseini.github.io/learn-claude/`.

**Method note.** Pixel clicking in my browser pane was unreliable (clicks landed on wrong
elements, tabs re-navigated between calls). Everything below was verified either through the
site's rendered DOM, the site's own shipped data/JS, or both. **I dropped two observations I
could not attribute to the site.** Where I state a number I computed it from the site's own
`data/items.js`, `picks.js` and `search-keywords.js`.

---

## 1. First 60 seconds

Landing page: a mug drawing and "I'm a [role] and I've [level]." with the brackets showing. Then
"Who are you?" and ten chips.

Two seconds in, the headline said **"I'm a teacher and I've [level]."** I had clicked nothing. It
cycles by itself every 2.6s (`startAttract()` in `home.js`) and marks a chip while it does. My
first reaction was "did I mis-click?" — no, the site is filling in an answer I never gave. It
stops when you choose, and it respects reduced-motion. Still: the first thing the site did was
put words in my mouth.

Otherwise it is fast, quiet, no cookie banner, no popup, no signup. That bought it another five
minutes.

---

## 2. The front door, all four levels

I picked **running a business**. Headline became "I'm running a business and I've [level]." with a
shopfront drawing. "235 resources match so far." Then four level chips.

| I've... | Resources | Picks block |
|---|---|---|
| never used Claude | 42 | 3 |
| used it a little | 66 | 3 |
| used it a lot | 48 | 3 |
| built things with it | 79 | 3 |

Every count is real — I checked all five against the data file and they match exactly. That is
more than most sites manage.

But the front door hides the funnel. It says "235 resources match so far" and then, once you
answer question two, you get 42. Nothing tells you 193 just vanished. And **"Show me" is
redundant** — the level chip already sets everything; the button just navigates.

Cross-checking other roles: **teacher + "built things with it" = 2 resources and no picks block at
all.** The count line says "2 resources. Remove a filter to see more." So the site's two questions
can land you on two links and no recommendation. Three of the forty role+level combinations have
no picks (`student|builder`, `teacher|builder`, `writer-marketer|builder`) — the headline feature
just is not there, with no explanation.

---

## 3. What the catalogue gives me

The cards are the best thing here. Real specifics, not blurb:

> **"Skip if:** The free tier stops at five Projects, and the larger knowledge base that makes one
> useful for a whole topic only arrives on a paid plan"

> **"Skip if:** Two ceilings here are different and easy to trip over: a chat takes 500MB per file,
> a Project takes 30MB, and twenty files is the limit either way."

> **"Skip if:** Skills need a paid plan (Pro, Max, Team or Enterprise) AND a separate setting, Code
> execution and file creation, switched on first"

> **"Skip if:** A vendor's blog that still names who should not buy: regulated firms, anyone with a
> no-AI-on-customer-data policy, and Microsoft-only shops. Check its pricing against
> claude.com/pricing before repeating any of it."

That last one is a directory telling me to distrust its own entry. Good.

The problem is what the 235 business entries are *about*. They are overwhelmingly Anthropic's own
product pages. Of the 79 in the "built things with it" pool, **76 are Anthropic Academy** — the
site's own pick reason admits it: *"Seventy-six of these 78 are Anthropic's own single-workflow
pages"*. I verified that count; it is exactly right. Which means the honesty is real and the
catalogue is still mostly one vendor's marketing, re-shelved.

---

## 4. Paths

Seven paths. Exactly one includes "running a business": **"Your first week with Claude"**, shared
with "not a coder, a student, a teacher". There is no path about invoices, customers, staff,
quotes, or books.

Meanwhile **a designer (47 items in the catalogue) gets a dedicated path. Running a business (235
items — the largest role by a wide margin) gets none.** The biggest audience gets the generic
beginner track.

I followed the one path I am allowed. Every step reason does justify its position — this is
genuinely well done:

> Step 1: "Start here because most confusion is not about prompting — it is not knowing that Claude
> is several different products."
> Step 2: "Now open the thing itself and do one real task. Reading about it any longer is
> procrastination."
> Step 3: "By now you have had a generic, disappointing answer."
> Step 4: "Once you repeat a task twice, you need somewhere to keep the context... Learning this
> earlier would have been abstract."
> Step 6: "Last, because working on your own files only makes sense once you trust the answers."

Six steps, six real reasons. No filler. But **all six steps say "No publish date given."** Every
one.

Small tell: the paths list says "6 steps · about 4 hours", "5 steps · about 2 hours", and then "4
steps · **about 81 minutes**". Nobody writes 81 minutes. That is a machine talking.

---

## 5. The card and the resource page

Three resource pages.

**"Mastering Claude Cowork & AI Agents in 5 hours"** (Udemy). Badges: `course`, `half a day`,
**`pay once`**. Button: "Open on Udemy". Then:

> "**Skimmed.** We read the outline or a free sample. We have not seen the whole thing."
> "Checked 5 Sep 2026 · No publish date given · Found through Udemy"

So: a paid course, nobody watched it, **no price anywhere on the page**, and no date. "Pay once"
could be a tenner or ninety. I am not clicking that.

**"Everyone should be using Claude Code more"** (Lenny's Newsletter). Badge `subscription`, no
price. Its Skip if is honest — *"most of it sits behind a paid subscription, and it dates from
October 2025 so it predates Cowork"* — but the card next to it says "Updated 29 Jul 2026", which
reads as recent. Two opposite signals on one card.

Outbound links are done properly: `target="_blank" rel="noopener noreferrer"`, and the button names
the destination rather than saying "Read more". Credit.

---

## 6. The picks block

Verdict: **real judgment, not the first three rows.** I tested this rather than assumed it. I
reimplemented the site's sort and compared:

- `business-founder|builder`: pick #2 sits at **position 78 of 79** in the default order.
- `business-founder|confident`: pick #1 sits at **position 40 of 48**.
- `business-founder|basic`: pick #2 sits at **position 34 of 66**.
- Only one of four cells shares even two entries with the default top three.

The reasons add things the title cannot:

> "The only candidate built to be read before installing rather than after - it names the three
> cases where the plugin adds nothing"
> "The only candidate that helps you choose an integration rather than use or build one, sorted on
> governance and security rather than popularity"
> "the two picks above are the why-safe and the how-fast, this is the what."

That last one is a set with an argument, not three links. That is the best writing on the site.

**Does "picked by AI" make me trust it more?** No — and mostly because it is meaningless. **All 37
pick cells are `picked_by: "ai"`.** There is no human-picked cell anywhere. The label reads like a
distinction ("this batch was AI, that batch was us") when the truth is "everything here is AI". If
you are going to label it, do not imply a contrast you do not have.

What I *do* trust: the pick dates are 31 Aug to 5 Sep 2026, so nothing is older than five days.
That is the honest part.

**Break:** the picks vanish the moment you add a third filter or type anything. I have 15 minutes,
so I click "15 min" — and the site's best judgment disappears with no message. The code's reasoning
is defensible (a pick might get filtered out) but the reader just sees the good bit evaporate.

**And a typed number that drifted:** the builder pick says *"The only candidate of 78 we have read
in full"* and *"Seventy-six of these 78..."* while the page header says **79 resources**. The 76 is
still right; the 78 is stale. A hand-typed count in copy that a generated count sits three inches
above.

---

## 7. Dates and tier badges

**489 of 635 entries (77%) say "No publish date given."** Three in four.

Worse, **44 entries show both lines at once**:

> "Checked 5 Sep 2026 / No publish date given / Updated 1 Jul 2026"
> "Checked 5 Sep 2026 / No publish date given / Updated 16 Mar 2026"
> "Checked 5 Sep 2026 / No publish date given / Updated 2 Jun 2026"

To a normal person that is a contradiction: you do not know when it was written but you know when
it was changed? The code has a careful reason for it. The card does not give me the reason. It
gives me two lines that fight.

Three entries show a month with no day — "Updated Jun 2026" on **"Real-World AI for Everyone
(Specialization)"**, a Coursera subscription course.

**Tier badges.** Across 635 entries:

- **Skimmed — 501 (79%)**: *"We read the outline or a free sample. We have not seen the whole
  thing."*
- **Read by AI — 98 (15%)**: *"AI read all of it. No person has checked the notes yet."*
- **Found only — 36 (6%)**: *"We found it and sorted it. Nobody has looked at the content yet."*
- **Read in full — 0.**

For my role specifically: 235 business entries, **217 of them Skimmed**, 1 never opened, none read
in full by a person.

**Would I act on a "Skimmed" recommendation?** For a free help-centre page, yes — the cost of being
wrong is five minutes. For the paid Udemy course, no. The site is asking me to spend money on a
five-hour course whose outline it glanced at. That is the same confidence level I would get from
the Udemy listing itself, which at least shows the price.

**Would I spend money on a tool recommended by a site that looks like this?** Not on the strength
of this site. Three cards in four with no date, plus a badge on almost everything saying nobody read
it, plus no prices — that is a site I would use to *find* candidates and then verify somewhere else.
Which is most of the value gone.

---

## 8. Search, in my words

I typed these as I would type them. I verified each by running the site's own ranking function
against its own shipped index; two I also confirmed live in the browser and the results matched
exactly.

**1. "how much does claude cost" — BROKEN on first use, then good**

First time I typed it: **"0 resources for 'how much does claude cost'"**. Nothing. On a site whose
front page brags about 635 resources, and which contains a card literally titled "Plans & Pricing".

Cause, from the site's own code: the 373 KB search index loads on the first keystroke. Until it
lands, `browse.js` falls back to plain substring matching that requires *every* word — "how",
"much", "does", "claude", "cost" — to appear in the title, summary, who-for or source. For a real
question that is never true. The code comment says *"fall back to plain substring so typing is never
dead."* It is not dead. It is worse — it confidently says zero.

Once loaded: **18 resources**. Top three: *Plans & Pricing* (Anthropic), *Claude Team pricing for a
small business*, *Getting Started with Claude for Financial Services*. First two are exactly right.
Third is a swerve. **Verdict: right answer, delivered after a wrong one.**

**2. "claude for invoices" — 2 results**

*Organize your business finances* (Anthropic Academy, Skimmed) — For: "Solo or freelance business
owners wanting clarity on their own invoicing data." Correct. *Small Business plugin (skill
inventory)* — reasonable.
**Verdict: both relevant, and only two out of 235 business entries. Invoices are the single most
common small-business task. Thin.**

**3. "is my data safe" — 13 results**

Top: *Is my data used for model training? (Privacy Center)* — Read by AI, exactly the right page.
Then *AI Fluency for Small Businesses* and *Use Claude Cowork safely*.
**Verdict: best result of the five. This one works.**

**4. "write customer emails" — 40 results, bad top three**

#1 is **Real-World AI for Everyone (Specialization)** — Coursera, **subscription**, Skimmed, no
publish date, "Updated Jun 2026" with no day. #2 is **"Claude AI for Teachers: Complete Beginner's
Guide"** — a teachers' guide, for a business email query. #3 is *AI Fluency for Small Businesses*.
**Verdict: the top hit costs money and nobody watched it; the second is for the wrong job. Worst
top-three of the five.**

**5. "claude for bookkeeping" — 2 results**

#1 **"Anthropic Just Dropped Claude for Small Businesses (31 Skills)"** — YouTube-grade headline,
Skimmed. #2 *Reconcile transactions across your accounts* — actually the right answer, ranked second.
**Verdict: correct answer present, hype title above it, and again only two results.**

**Cross-cutting search fault:** ranking is relevance-first, tier second. So a "Found only" entry —
*nobody has looked at the content* — can be the #1 result. I hit one: **"keep my own voice"** returns
26, and #1 is **"Using AI for Writing Feedback"** (Northeastern), tier **Found only**, published 1
Aug 2025, which the card itself flags as **"Published over a year ago — may not match Claude
today."** Top result: unopened, and stale by the site's own rule.

---

## 9. On a phone

375x812. Measured, not guessed:

**Good.** No horizontal overflow (`scrollWidth` 375 = viewport). **Zero tap targets under 24px** — I
checked every link, button, select and input on the page. Chips wrap. Filters collapse into a sticky
"Filters" button pinned to the bottom. Type is large and the serif headings hold up.

**Bad.** The first card starts **609px down** — three quarters of a phone screen is chrome before one
recommendation: logo, nav, a giant "Browse" H1 that tells me nothing I do not know, Search, Sort,
two filter chips, count, "Start with these three", "picked by AI · 4 Sep 2026". On a phone between
two jobs I want the first card at the top.

**One card is 504px tall — 62% of the screen.** Three picks is roughly two full screens. 42 results
is a very long thumb, and there is no pagination or "load more" anywhere in `browse.js`; all 42
render at once. At the unfiltered 635 that is a wall.

---

## 10. Keyboard walk

Verified from the DOM and the shipped CSS/JS rather than physical tabbing (my pane's key handling was
unreliable). What is actually there:

- **Skip link on all five pages** — `<a class="skip-link" href="#main">Skip to content</a>`, hidden
  until focused. Correct.
- **Global `:focus-visible { outline: var(--focus-ring); }`.** Present.
- **The card focus ring moves to the whole card**, not the title text, via `.card:has(.card-title
  a:focus-visible)`. Nice touch.
- **Filter options are `<button role="checkbox">` with `tabindex 0`** — operable by Space and Enter.
- **The mobile filter sheet is done properly**: `role="dialog"`, `aria-modal="true"`,
  `aria-label="Filters"`, Escape closes it, focus moves to the close button on open and returns to
  the trigger on close, and there is a hand-written Tab trap. That is more care than most commercial
  sites take.
- **Forced-colors support**: `:focus-visible { outline-color: CanvasText; }`.

**One real defect.** `.card-title a:focus-visible { outline: none; }` removes the ring, and the
replacement depends entirely on `:has()`. There is **no `@supports` guard anywhere in `site.css`** —
I grepped. In any browser without `:has()`, the outline is removed and nothing replaces it: keyboard
focus becomes invisible on every card title on the site. In 2026 that is a small population (old
Firefox ESR, older Android WebViews), so this is low severity — but it fails to the worst possible
state rather than the safe one.

---

## 11. How we check

Trust **less**. This page is where the site's copy and the site's data stop agreeing.

The page says:

> "We would rather have 70 resources we can vouch for than 700 we cannot."
> "We find material, read it, and write two things"
> "We do not list something we cannot open."

The home page says:

> "**635 resources, checked by hand.**"

The data says: 501 Skimmed, 36 that nobody has opened, 98 read by a machine with no human check, and
**zero** read in full by a person. 635 is much closer to 700 than to 70. And "we do not list
something we cannot open" sits four lines above the site's own admission that *"Paid courses usually
stop here, because we cannot see inside them"* — which is 501 entries.

The tier badges are the honest part. The prose around them is not. If the badges are right, "checked
by hand" is not a fair description of 635 entries, and the 70-vs-700 line is exactly backwards.

Genuinely good on that page: it names its own weakness — *"It needs a GitHub account, which is a real
barrier and we know it"* — and it explains why Claude certification prep is not listed. And "We do
not take money to rank a resource. We are not affiliated with Anthropic." is the right thing to say
plainly.

---

## 12. Everything broken, ranked

**1. Search says "0 resources" for a real question before its index loads.**
`browse.html` -> type "how much does claude cost". Saw: **"0 resources for 'how much does claude
cost'"**. Expected: the *Plans & Pricing* card that is demonstrably in the catalogue (18 results once
the index lands). Cause: 373 KB index loads on first keystroke; the substring fallback requires every
word to appear literally. **Harms every first-time visitor**, who is invited to type a sentence by
the placeholder "Title, topic, or what you want to do" and gets told the site has nothing. On a phone
connection the window is seconds long.

**2. The resource page drops the "over a year old" warning.**
Browse card for *"Claude for Small Business (Back-Office AI, honest review)"* shows **"Published over
a year ago — may not match Claude today."** Its own page at `resource.html?id=r-941099b02f` shows
**"Checked 5 Sep 2026 · Published 29 Jul 2025 · Found through Eigent AI"** — no warning. `resource.js`
never uses `fresh.note` or `fresh.cls`. **17 entries affected.** Harms anyone who opens a card to
decide — the detail page is the last screen before the outbound click, and it is the one that hides
the warning.

**3. Trust copy contradicts the site's own badges.**
"635 resources, checked by hand" and "We find material, read it" and "70 we can vouch for rather than
700 we cannot" against 79% Skimmed / 6% never opened / 0% read in full by a person. Harms anyone
deciding whether these judgments are worth acting on, especially before spending money.

**4. The resource page drops the "Updated" date entirely.**
96 entries carry an updated date; `resource.js` renders it for none. For 44 of them it is the *only*
date evidence, so the detail page shows "No publish date given" and nothing else. Confirmed on
*Real-World AI for Everyone*: page reads "Checked 5 Sep 2026 · No publish date given · Found through
Coursera" while the data holds "2026-06". Harms anyone judging freshness on the page they landed on.

**5. Paid recommendations with no price, tier "Skimmed".**
*"Mastering Claude Cowork & AI Agents in 5 hours"* — `pay once`, "We read the outline or a free
sample. We have not seen the whole thing", no price, no date. Harms an owner about to spend money on
the strength of a glance.

**6. No path for the largest role.** 235 business entries, zero business paths; designer has 47 and
gets one. Harms the site's biggest audience.

**7. Picks disappear on any third filter or search, silently.** Filter by "15 min" — the most natural
move for a busy owner — and "Start with these three" vanishes with no message.

**8. Three of forty role+level combinations have no picks.** `teacher|builder` returns **2
resources** and no picks block. Harms users who answered both front-door questions in good faith.

**9. Relevance outranks tier, so unread entries can top search.** "keep my own voice" -> #1 is *"Using
AI for Writing Feedback"*, tier **Found only**, and over a year old.

**10. Neither screen gives you the date and the verdict.** The card says "Published over a year ago"
and hides the date; the page says "Published 29 Jul 2025" and hides the verdict.

**11. A typed count drifted.** Pick reason says "of 78"; the page header says "79 resources".

**12. Coverage is thin on actual business work.** "claude for invoices" -> 2. "claude for
bookkeeping" -> 2. Out of 235 business entries, most of which are Anthropic's own workflow pages.

**13. The headline answers question one for you.** Attract loop puts "I'm a teacher" in the h1 after
2.6s with no input.

**14. Focus ring has no `:has()` fallback.** `outline: none` with no `@supports` guard — invisible
keyboard focus on card titles in browsers without `:has()`. Low severity in 2026, wrong failure
direction.

**15. "about 81 minutes."** On the paths list, next to "about 4 hours" and "about 2 hours".

---

## 13. The one thing that would make me leave

**Typing my actual question and being told there are zero results.**

I have twenty minutes. I type "how much does claude cost" — the first question anyone with a budget
asks — and the site says **"0 resources for 'how much does claude cost'"**. I do not know about index
loading. I know the site that promised to find what is worth my time could not find its own pricing
page. I close the tab and go to Google, and I never learn that the answer was eighteen results and
the right one was first.

Everything else on this list I would forgive. That one ends the visit before the site gets to show me
anything good.

---

## 14. What is genuinely good

- **The "Skip if:" lines are the real product.** Specific, checkable, occasionally against the site's
  own interest: *"Check its pricing against claude.com/pricing before repeating any of it."*
- **The picks are real selection.** One pick sits at position 78 of 79 in the default order. The
  reasons argue, compare and cross-reference each other.
- **Path step reasons all justify position**, not just content. Six of six.
- **Every count on the page is real.** 235, 42, 66, 48, 79, 18, 2 — I checked all of them against the
  data and every one matched.
- **The tier badges themselves are honest**, including the uncomfortable ones. "Nobody has looked at
  the content yet" is a hard thing to ship.
- **Accessibility is above average**: skip links everywhere, focus-visible rings, a properly built
  modal sheet with Escape and focus return, forced-colors support, no tap target under 24px, no
  horizontal overflow at 375px.
- **Outbound links name their destination** and carry `rel="noopener noreferrer"`.
- No ads, no tracking, no signup, no cookie wall, and it says so.

The judgment layer is better than the plumbing around it. Fix the search fallback and stop the
resource page throwing away its own dates and warnings, and this becomes a site I would send another
owner to.

---

## Checklist
- [x] I opened the live site at all four levels of my role — 42 / 66 / 48 / 79
- [x] I quoted at least 5 real titles or lines from the site — 20+
- [x] Every number I used is computed from the shipped data
- [x] I looked at a phone width — 375x812, card heights and first-card offset measured
- [x] I did one keyboard walk — DOM and CSS verified; physical tabbing was unreliable and I said so
- [x] Five search queries in my own words, each with its verdict, plus a control
- [x] I read the picks block and tested whether it is the top three rows — one pick is at position 78
      of 79
- [x] I found at least one thing nobody has mentioned before — the search fallback confidently
      reports "0 resources" for a real question while the index is still loading; and the focus ring
      on card titles has no `@supports` guard behind its `:has()` replacement
- [x] I discarded two observations I could not attribute to the site, and said so
