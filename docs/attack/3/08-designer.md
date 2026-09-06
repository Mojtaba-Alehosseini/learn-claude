# Attack 3: a designer
Written as a designer, 2026-09-06. Site version: 9deb0db.

I own a design system. I write the interface copy. I am here because I want to know what
Claude is worth in my week, and I have been burned by demos.

## 1. The first 60 seconds

The home page loads to one sentence at 68px: **"I'm a [role] and I've [level]."** — with
the square brackets rendered as literal characters. I watched it for 16 seconds without
touching anything (polled `.blank` innerText 40 times at 400 ms). It never changed. There
is no attract loop, no cycling example, nothing that shows me the sentence finished. The
first thing the site says to me is placeholder syntax.

The biggest, most inviting thing on the page — `a [role]`, 199 x 75 px, `cursor: pointer`,
underlined in clay — is a disclosure button that ships **already expanded**
(`aria-expanded="true"`). So my first click on it does the one thing I did not want: it
collapses `#chooser` from 184 px to 0 and both questions disappear. "Show me" stays on
screen and stays live. I am left looking at a sentence with two empty brackets and an
active primary button. Clicking the blank again brings the questions back, but nothing on
screen tells me that.

Its accessible name is `a [role]`. There is no `aria-label`. A screen reader announces a
button called "a role, expanded".

Craft note I could not unsee: the `<h1>` on this page is
`<h1 class="meta">Find what's worth your time.</h1>` at **16px**. The 68px sentence is a
`<p class="display">`. The document outline and the visual hierarchy are inverted, and the
class names admit it — "Who are you?" is `<h2 class="h3">`, also 16px, the same size as
body copy. Two different `h2`s render at 16px and 24px on one page.

Below the fold the three promises are good and plainly written: "We say when to skip",
"We say how we checked", "We show the date". I believed them enough to keep going.

## 2. Does the front door work for me (all four levels, with what I was shown)

I answered "a designer" and then each level in turn, on the live home page, and followed
"Show me" each time.

| level I picked | home said | Browse gave me | first pick |
|---|---|---|---|
| never used Claude | "8 resources match so far." | 8 | Good from Afar, But Far from Good: AI Prototyping in Real Design Contexts (NN/g) |
| used it a little | "11 resources match so far." | 11 | Claude for Designers in 2026: Where AI Actually Helps |
| used it a lot | "22 resources match so far." | 22 | Claude Code for Designers (Builder.io) |
| built things with it | "7 resources match so far." | 7 | knowledge-work-plugins/design/skills (source) |

8 / 11 / 22 / 7 = 48. That matches the `designer` row in STATUS.md exactly. The counter is
honest and it updates before I commit. Good.

All four cells gave me a filled "Start with these three". I never saw the two-pick heading
or the empty cell, so I cannot judge those.

**The front door has one hole.** "Show me" is not gated on the two questions. I clicked it
with nothing selected and landed on `browse.html` with no query string, title
"Browse 588 Claude resources". The button that exists to collect two answers behaves
identically whether I give them or not. What it lands on is measured in section 10.

The copy "8 resources match so far" is wrong in one word: nothing changes after. There is
no "so far".

## 3. What the catalogue actually gives me (are these really for me?)

Mostly yes, and better than I expected. At "used it a lot" I was given
**"Design system drift review"**, **"Pattern consistency audit"**,
**"Competitive teardown and heuristic audit"**, **"Claude Code and Figma: Set up the MCP
server"**, **"How to Use Claude Code for UX Writing"** and **"ux-writing-skill (open
source)"**. That is my job, not a developer's job with a design word in it. At "built
things with it" all seven were on target — Figma MCP, brand-as-a-skill, Design Systems
Collective's SKILL.md piece.

**Three false positives across 48 cards.** All three are the word "design" doing work it
should not:

- `never used Claude` — **"See your theory of change in chat with Claude"**.
  For: *"Nonprofit program designers who know what their program does but have never
  mapped out why it works."*
- `used it a little` — **"Design a local foraging guide"**.
  For: *"A hobbyist wanting a personal example of the map-as-navigation-UI artifact
  pattern."*
- `used it a lot` — **"Develop a program toolkit"**.
  For: *"Nonprofit program designers or grant writers building a new initiative's design
  framework."*

Two of the three are nonprofit *program* design. So: Rule B holds on 45 of 48. The rule is
working; "program designer" is the hole it has not closed. Nothing developer-shaped leaked
in, which was the thing I was most ready to be angry about.

**The bigger problem is not relevance, it is sameness.** In my "used it a lot" cell I
grouped the 22 cards by their full visual signature — badge, source, all three chips, and
the whole footer line. **Eight of 22 are byte-identical on every visual token**:

    Skimmed | Anthropic Academy | docs/15 min/free | Checked 29 Aug 2026 · No publish date given

Those eight are: Audit a folder of visual assets against your guidelines · Clickable
prototype from real components · Competitive teardown and heuristic audit · Design spec
from scattered threads · Design system drift review · Develop a program toolkit · Pattern
consistency audit · Synthesize user interviews into findings.

Eight cards in a column where the only thing that differs is the title and two sentences.
Nothing on the card helps me tell them apart or rank them. My eye slides off the block.

And the site already knows how to fix this: it collapsed the equivalent material for five
other functions into single cards — **"Use cases for Sales"**, **"Use cases for Legal"**,
**"Use cases for HR"**, **"Use cases for Finance"**, **"Use cases for Operations"**, each
with the good line *"This is a menu, not a lesson"*. There is no "Use cases for Design".
The same source is one card for five business functions and eight cards for mine.

## 4. Paths

There is a designer path: **"Judging AI's design output"** — 5 steps, about 2 hours, free.
STATUS.md says 7 paths, 36 steps; I count 7 on the page.

The framing sentence is the best copy on the site: *"This covers about a fifth of a
designer's job — deciding whether to trust what Claude just produced — and says nothing
about the other four fifths."* I trust a page that says that.

**But it is not at my level, and the Paths index does not tell me that.** Every path card
says "For a designer" and none says which level it starts at. This one starts at
`never-used` — step 1 and step 2 are both cards I was shown at "never used Claude" — and
tops out at `confident`. I have built things. There is no route for me. The seven paths
cover role, not level, and I only find that out by opening one.

**The path drops the site's own core promise.** I checked the rendered text: `Skip if`
appears **zero** times on `paths.html?id=judging-ai-design-work`. Every Browse card carries
a Skip line; the path — the place where I am most committed and least able to browse away —
carries none. Step 3's own card in Browse says *"read that one first or you are running a
test without knowing what the last people found"*. On the path, step 3 comes after step 1,
so the warning is satisfied — but I had no way to know that from the path page.

**Publisher concentration.** 3 of the 5 steps are Nielsen Norman Group. The picks block on
Browse enforces a no-two-from-one-publisher rule (STATUS.md names the pools where it has to
relax). Paths do not. Same site, two standards for the same kind of shortlist.

Structural: `.sp-title a::after { position:absolute; inset:0 }` makes the whole step card
one click target, and there is a visible "Start with this" primary button inside it going
to the same href. Two nested targets, one destination. The consequence is in section 10.

## 5. The card and the resource page

I opened four resource pages. Three of them I would click through on.

**`resource.html?id=r-60ea446379` — "Design system drift review".** Yes, immediately. It
tells me what it is (*"Checks shipped screens and open PR diffs against your design system,
listing every deviation from tokens, components, spacing and interaction with a severity
rating"*), what it needs (*"Before this — Claude Cowork / Your tokens.json and component
inventory / GitHub/Figma connectors (optional)"*), and then the line that made me trust the
whole site: *"Pure compliance checking against your existing tokens.json, not design
judgment at all - it deliberately omits anything that already matches, so it's a triage
list of deviations, not a design review."* That is exactly the caveat I would have written.
One nit: "What it teaches" has a single bullet rendered with a leading em dash, which reads
as a truncated list.

**`resource.html?id=r-98e29a0605` — "knowledge-work-plugins/design/skills (source)".** Yes.
The Skip line points me at one file: *"accessibility-review is a full WCAG 2.1 AA audit -
contrast, keyboard, touch targets, screen readers - and you can see exactly what it checks
before trusting it."* That is a reason to open a repo.

**`resource.html?id=r-27f9d9ec35` — "How to use Claude Code for non-engineering use
cases".** No. Chips read `article / 1 hour / subscription`. **No price appears anywhere on
the page.** The Skip line says *"Skip it unless you will pay for the newsletter"* and
"Before this" lists *"Paid Anthropic subscription"* — two paywalls, neither priced. Price
chips do exist on this site: I found `from $49`, `from $995`, `from $2,999`, `from $3,000`
in the full catalogue, on four cards. None of the four is in the designer set. So the
answer to "is it clear what you would pay before you click" is: for a designer, no. Also a
copy defect in that prerequisite list: **"— Computer with mac or Windows"** — lowercase
mac, capital Windows, and the phrasing is broken English.

**`resource.html?id=r-9f57e8bf80` — the stripped `listed` card.** See section 8.

**The badge on a Browse card is not reachable without a mouse.** On the card it is
`<span class="badge badge-previewed" title="We read the outline or a free sample...">`.
`tabIndex` is -1, there is no link, and the only route to the meaning is a `title`
attribute — which needs hover. At 375 px there is no hover. I checked every `a[href]` on a
Browse results page: the only links to `how-we-check.html` are in the top nav and the
footer. **On the resource page it is a real link** (`Found only` →
`how-we-check.html#tier-listed`), which is where it should have been on the card too.
The card link does carry `aria-describedby="tierdesc-…"`, so a screen-reader user gets the
definition — a sighted touch user gets nothing.

## 6. Search, in my words

Typed into the Browse search field (placeholder: *"Title, topic, or what you want to do"*),
no role or level filter set.

| # | what I typed | top 3 I was shown | verdict | why |
|---|---|---|---|---|
| 1 | how do I stop claude from inventing spacing values that are not in my design system | 1. Design Systems in 2026: Turn Your System into a Claude Skill · 2. Set Your Standards Before You Start: A Journalist's Journey Using Claude.md · 3. Set up your design system in Claude Design | ok | #1 and #3 are the right answers. #2 is a journalism-ethics article and has no business at rank 2 — the only bridge is the word "standards". 19 results. |
| 2 | can claude read my figma file | 1. Guide to the Figma MCP server · 2. Claude Code and Figma: Set up the MCP server · 3. Full Tutorial: From Design to Code with Claude Code (Meaghan Choi) | ok | Perfect top 3. But the page then says "72 resources for “can claude read my figma file”" and **only 4 of the 72 mention Figma**; the tail ends on "Create and edit files with Claude to eliminate hours of busy work". The ranking is right and the count line is a lie about relevance. |
| 3 | is it worth letting AI do the first round of UI mockups | 1. Using Claude Design for prototypes and UX · 2. 43 Claude Skills for college teachers · 3. Claude Design: The Complete Guide | ok | Saved by #3, which is a designer's critique of output quality. #2 is nonsense for me. The damning part: the site's **own** first pick for a designer at this question — "Good from Afar, But Far from Good: AI Prototyping in Real Design Contexts", picked because *"the only candidate built on a real comparison - AI against a human designer on the same brief"* — is **absent from all 19 results**. It ranks **1st** for the keyword "AI prototyping". |
| 4 | how do I write better error messages and empty states | 1. ux-writing-skill (open source) · 2. Troubleshoot Claude error messages · 3. Write in my voice | ok | #1 is right. #2 is a pure keyword collision — I asked about writing error messages, I was given Claude's own troubleshooting page. "How to Use Claude Code for UX Writing" does not appear in the 12 results at all. |
| 5 | what does claude get wrong about accessibility | 1. Design plugin (official) · 2. knowledge-work-plugins/design/skills (source) · 3. Design Systems in 2026: Turn Your System into a Claude Skill | bad | All three answer a different question — *how do I run an accessibility check with Claude*. I asked what Claude gets wrong. The card that answers it, "Claude for Designers in 2026: Where AI Actually Helps", whose own Skip line says *"the failure modes, including invented pixel values and Claude calling 3:1 contrast acceptable when it is not"*, is **absent from all 55 results**. |

**The same question, asked two ways.** Query 1 above, and then
**"make claude use my design tokens instead of random px numbers"**. Top 3 the second time:
1. Design Systems in 2026: Turn Your System into a Claude Skill · 2. Set up your design
system in Claude Design · 3. A Better (and Cheaper) Figma MCP or How To Let Claude Design.
**The site agreed with itself** — identical #1, and the second wording actually cleaned up
by dropping the journalism article. That is a pass.

The pattern under all five: this search rewards keywords and punishes sentences. "AI
prototyping" finds the right card at rank 1; a sentence about the same subject does not
find it at all, in 19 or in 55 results. `how-we-check.html` states the opposite in its own
words: *"so a sentence in your own words usually lands."* On 2 of my 5 sentences the one
card the curator wrote for that question did not land anywhere.

## 7. On a phone

I emulated 375 x 812 and re-measured. The responsive work is the best-built part of this
site and I want to say so before I complain.

- **No horizontal overflow anywhere.** `document.documentElement.scrollWidth` = 375 =
  `innerWidth` on the home page and on Browse.
- The 68px display sentence drops cleanly to 40px/44px.
- Every role and level chip is **44 px tall**. Nav links are 44 px tall. The Filters bar is
  343 x 44 fixed to the bottom.
- The filter sheet is real work: 84 filter options, 0 visible until you tap Filters, then
  42 visible, focus moved into the sheet, `body { overflow: hidden }` while it is open, a
  Close button. All four tier options are in it.
- Media queries present: `(prefers-reduced-motion: reduce)` — 3 blocks —
  `(hover: hover) and (pointer: fine)`, and `(forced-colors: active)`. Gating hover states
  to fine pointers and supporting Windows High Contrast is craft most sites skip.
- Focus is handled properly: `:focus-visible { outline: var(--focus-ring) }`, the footer
  overrides the ring colour for its dark ground, and the card title's ring is moved onto
  the whole card with `.card:has(.card-title a:focus-visible)`.

What is wrong at phone width:

- **The badge is unreachable.** As in section 5: a `title` attribute is the only route to
  what "Skimmed" means, and touch devices do not show `title`. On a phone, the site's
  central honesty mechanism is a word with no definition.
- **Sort sits directly above a block it does not sort.** On the 375 px layout the vertical
  order is: Search → Sort → filter pills → "7 resources" → "Start with these three ·
  picked by AI". A reader will read that as cause and effect. It is not; see finding 4.
- **Single-line card titles are 24 px tall targets.** I measured every visible control on
  Browse at 375: only two are under 44 px — the wordmark (122 x 40) and the card title
  "Encode the brand as a skill" at **242 x 24**. Titles that wrap to two lines get 76 px.
  So a card's primary action is 24 px tall or 76 px tall depending on how long its title
  is. That is the tap target scraping the WCAG 2.2 minimum by accident, not by design.
- **No dark mode at all.** I enumerated the stylesheets: `prefers-color-scheme` blocks =
  **0**, `color-scheme` computes to `normal`, no `<meta name="color-scheme">`. The one
  breakpoint is `(max-width: 768px)`. A long ivory list at #F0EEE6 at night is a choice,
  and it is not the one I would make for a site people read in bed on a phone.

## 8. What changed since Attack 2 — my verdict on each

**Does the role filter return design work or developer work with a design word in it?**
Design work. 45 of 48 are mine. The three misses are named in section 3 and two of them are
"nonprofit program designer", not developer. This is fixed.

**Do the stripped `listed` cards read as honest or broken *as a piece of interface*?**
Broken, and for a reason nobody can fix with copy. I filtered to `checked=listed` and read
all three. Take the first:

    Found only
    Head of Claude Code: What happens after coding is solved (Boris Cherny)
    Lenny's Newsletter · Lenny Rachitsky with Boris Cherny (Anthropic)
    [podcast] [half a day] [subscription]
    Skip if: You want something we have read. We have not opened this one yet.
    Checked 5 Sep 2026   Published 19 Feb 2026   Updated 13 Apr 2026

The badge's own tooltip says *"We found it and sorted it. Nobody has looked at the content
yet."* On the same card, in the same 200 px, the site asserts a format, a **duration**, a
**price model**, a publish date and an update date. Nobody has looked at the content, but
we know it takes half a day. That is not honest-looking; it is a card arguing with itself.

Second problem: the `For:` paragraph is not present in the DOM at all on these three. Every
other card is `For:` then `Skip if:`. Here the positive half vanishes and the only prose
left is a negative sentence, repeated identically on all three cards. Three cards in a row
carrying the same sentence is the visual signature of a template failure, not of candour.
And the site's own footer, on every page, says *"Every entry says who it is for, who should
skip it, and when we last checked it."* For these three it does not.

The resource page for the same item is much better: the badge is a real link, and the
missing sections are simply absent rather than half-rendered.

**Is the "how well checked" badge's meaning reachable without a mouse — at phone width?**
No. Measured, section 5 and 7. It is reachable from the resource page. It is not reachable
from the card, which is where the badge is doing its persuading.

**Do the date lines make the site look maintained?** Half-and-half, and my half is the
worse one. Every card carries a `Checked` date and they are recent — 20 Aug, 21 Aug, 27
Aug, 29 Aug, 5 Sep 2026. That reads maintained. But of the **48** cards in the designer
set, **39 say "No publish date given"** — 81%, above the site-wide 442 of 588 (75%) in
STATUS.md. All **7** of my "built things with it" cards say it. The staleness flag works —
I found `<span class="flag-outdated">Published 5 Sep 2024 · over a year ago, may not match
Claude today</span>` on "AI prompt engineering: A deep dive" — but by construction it can
only ever fire on a card that has a publish date, so it protects me on 9 of my 48 and is
structurally silent on the other 39. I know when *you* last looked. On four cards in five I
do not know how old the thing is.

**Does naming one person and Claude as "we" raise or lower your trust?** It raises it, more
than anything else on the site. `how-we-check.html` says: *"One person makes this site - a
researcher at the Technical University of Denmark... The reading is done by Claude, at the
level each card's label claims and no further... and has not yet read a single resource end
to end."* I did not expect that and I believe the site more for it.

**And it detonates the badge copy.** The tooltip on 485 cards says *"**We** read the
outline or a free sample."* The truth is Claude skimmed it. The word "we" on a card, next
to a hand-written-sounding judgment, reads as a person. The correction lives on a separate
page that the card does not link to. The disclosure is excellent and it is in the wrong
place — it needs to be where the claim is made, not two clicks away in the nav.

**The thin-level offer.** I do not hit one — my thinnest cell is 7. I went and looked at
`teacher|builder` to judge it: *"Only 2 at “built things with it” for a teacher. The level
below, “used it a lot”, has 8. Add “used it a lot” too"*. The control is a real
`<button class="btn btn-secondary" data-axis="levels" data-value="confident">`, 246 x 44.
One click took 2 to 10 and the URL to `level=builder,confident`. It names the count, names
the level, names its count, and the arithmetic is right. **Yes, I would take it.** It is
the best-designed control on the site.

**The picks block.** All four of my cells shipped three picks under "Start with these three
· picked by AI · 6 Sep 2026". The reasons are comparative, not promotional — *"The only
candidate built on a real comparison"*, *"Chosen over the two longer written walkthroughs
of the same product"*, *"The only candidate about limits rather than possibilities"*. I
would open those three. I never saw the two-pick heading or the empty cell.

**Prices.** Section 5. Clear where a price chip exists; invisible in my whole set.

**Share a link.** Section 10, finding 1. It fails.

**Watch the home page.** Section 1. Nothing happens, and the brackets stay.

**The sort control.** Section 10, finding 4.

**Paths above beginner level.** Section 4. There is a designer path and it is below me.

## 9. Content quality — the three worst entries I was shown, quoted

**1. "Head of Claude Code: What happens after coding is solved (Boris Cherny)"**
(`resource.html?id=r-9f57e8bf80`, badge "Found only", chips `podcast / half a day /
subscription`). The card says *"Skip if: You want something we have read. We have not
opened this one yet."* and in the same breath tells me it costs a subscription and will
take half a day. If nobody opened it, those two chips are guesses printed in the same type
as the facts. I would not spend half a day on a paid podcast on that basis.

**2. "See your theory of change in chat with Claude"** (Anthropic Academy, shown to me at
"never used Claude"). *"For: Nonprofit program designers who know what their program does
but have never mapped out why it works."* I am four resources into the eight this site has
for a designer who has never used Claude, and one of them is nonprofit program design. In a
pool of eight, one wasted slot is 12.5% of everything I was offered.

**3. "How to use Claude Code for non-engineering use cases"** (Rich Holmes, `subscription`).
*"Skip if: Skip it unless you will pay for the newsletter - the free part ends exactly where
the templates begin"* — and no price, on the card or on the resource page. Its prerequisite
list reads *"— Computer with mac or Windows"* and *"— Paid Anthropic subscription"*. Two
paywalls, no numbers, and a typo in the prerequisites. It also opens its Skip line with the
word "Skip", so the rendered line reads "Skip if: Skip it unless…".

Honourable mention, not in the three because it is only annoying: **"Claude Design
Fundamentals"** (Coursera) — *"it is a beginner course that spends its last hour on
portfolio and interview preparation, so a working designer is paying an hour for career
advice they did not come for."* The Skip line is doing its job perfectly. The card is fine;
the resource is the problem, and the site told me so. That is the site working.

## 10. Everything that is broken, ranked (evidence for each)

**1. Every one of the 588 resource pages shares one social title, and there is a Copy link
button encouraging you to spread it.**
URL: any `resource.html?id=…`. I fetched the served HTML for
`resource.html?id=r-98e29a0605` and read the head before any script runs:
`<title>Resource — Learn Claude</title>`, `og:title` = **"Resource — Learn Claude"**,
`og:description` = "What this resource teaches, who it is for, who should skip it, and how
thoroughly we checked it.", **no `og:image`**, `twitter:card` = `summary`. The visible tab
title is set later by JS, which crawlers do not run. Then I pressed **Copy link** on
`resource.html?id=r-60ea446379` (I intercepted `navigator.clipboard.writeText`): it copies
`https://mojtaba-alehosseini.github.io/learn-claude/resource.html?id=r-60ea446379` and the
button changes to "Copied". Expected: the card's own title and its "For:" line. Actual: if
I drop five of these into my team's Slack, I get five identical grey cards reading
"Resource — Learn Claude", with no image, and nobody clicks any of them. Harms: everyone
who recommends this site to anyone. This is the whole growth mechanism, and the site built
the button and not the preview.

**2. The site's own best answer to a question is invisible to the site's own search.**
URL: `browse.html`. Typed *"is it worth letting AI do the first round of UI mockups"* → 19
results, and "Good from Afar, But Far from Good: AI Prototyping in Real Design Contexts" is
not one of them (index of the title across all rendered cards: −1). That card is pick #1 in
"Start with these three" for `designer|never-used` and step 1 of the designer path, chosen
because it is *"the only candidate built on a real comparison - AI against a human designer
on the same brief"*. Same again for *"what does claude get wrong about accessibility"* → 55
results, and the card that names Claude's accessibility failures is not among them. Control:
the keyword *"AI prototyping"* returns 9 results with that card at **rank 1**. Expected: a
site that promises *"a sentence in your own words usually lands"* to find, for a plain
sentence, the card its own editor wrote for that sentence. Harms: everybody who uses the
search box the way the placeholder invites — *"Title, topic, or what you want to do"*.

**3. The "how well checked" badge cannot be understood on a phone.**
URL: `browse.html?role=designer&level=builder` at 375 px. The badge is
`<span class="badge badge-previewed" title="…">Skimmed</span>`; `tabIndex` = −1, not inside
any link, and the only `a[href*="how-we-check"]` on the page are in the nav and the footer.
`title` tooltips do not appear on touch. Expected: the badge to be the link it already is
on the resource page (`how-we-check.html#tier-listed` etc. — the anchors exist:
`tier-reviewed`, `tier-ai-reviewed`, `tier-previewed`, `tier-listed`). Harms: every mobile
visitor, on the one signal the site is built around.

**4. The sort control does not govern the block sitting under it.**
URL: `browse.html?role=designer&level=confident`. I set `#sort` to each value and captured
the rendered order. Positions 1–3 are identical under "Best checked first", "Newest first"
and "Shortest first": Claude Code for Designers (Builder.io) → Set up your design system in
Claude Design → AI Fluency for Creative Work. Those are the picks. Only "Everything else
for you (19)" reorders. Expected: a control labelled "Sort", placed above everything, to
reorder everything, or to say what it sorts. Harms: anyone who changes the sort and watches
the top of the page not move, and concludes the control is broken. Related: "Newest first"
moves exactly 2 of the 19 sortable cards in this cell, because 17 of them say "No publish
date given". "Shortest first" is correct — all `15 min` then all `1 hour`.

**5. The empty state gives advice that cannot work, and one of its three actions is not a
link.**
URL: `browse.html?role=designer&level=builder&checked=reviewed` (reached by tapping
"Read in full" in the mobile filter sheet). Rendered HTML:
`<div class="empty prose"><strong>We have nothing for this combination yet.</strong>It's on
the list. Loosen the level, or <a href="browse.html?role=designer">see everything for this
role</a>, or <a href="browse.html">browse everything</a>.</div>`
Three problems. **"Loosen the level" is plain text** between two links in a parallel list of
three actions. **It is the wrong advice**: the filter that emptied the page is "Read in
full", and STATUS.md says `reviewed` is 0 of 588, so no level change can help — I removed
the level entirely (`browse.html?role=designer&checked=reviewed`) and still got
"Browse 0 Claude resources". **And the filter UI offers "Read in full" as an ordinary
checkbox** with no count and no disabled state, so the interface invites a click that is
guaranteed to empty the page. Harms: anyone who tries the top of the quality ladder — which
is the natural first thing to try.

**6. The primary CTA works with no answers and lands on 396 screens.**
URL: `/` → click "Show me" with neither question answered → `browse.html`, title "Browse 588
Claude resources". At 375 x 812, `document.documentElement.scrollHeight` on that page is
**321,320 px** — 396 viewport heights, all 588 cards, no pagination and no "load more".
Expected: the button that exists to collect two answers either asks for them or explains
that it is showing everything. Harms: every visitor who misreads the collapsible blanks
(see finding 8) and just presses the orange button.

**7. The judgment sentences cannot be copied.**
URL: `browse.html?role=designer`. `.card-title a::after` is `position: absolute` with
`inset: 0`, so `document.elementsFromPoint` over the `Skip if:` paragraph returns the
anchor on top: `["A.", "P.card-skip", "ARTICLE.card"]`. Same pattern on path steps
(`.sp-title a::after`) covering the "why this step" prose. Expected: to be able to drag-
select a Skip line and paste it into Slack when I recommend something. Actual: the drag
becomes a link drag. Harms: the site's own advocates. The `For:` and `Skip if:` lines are
the entire product and they are locked inside a click target.

**8. The most prominent control on the home page hides the page.**
URL: `/`. `#roleBlank` ships `aria-expanded="true"`. One click sets it to `false` and
`#chooser` goes from 184 px to 0; both questions disappear while "Show me" stays visible and
live. Its accessible name is the literal placeholder `a [role]`. Expected: a 68px underlined
control to reveal something, not to remove the only thing on the page. Harms: first-time
visitors, once each.

**9. The document heading order is inverted.**
URL: `/`. `<h1 class="meta">` renders at 16px; the 68px sentence is `<p class="display">`;
`<h2 class="h3">Who are you?</h2>` renders at 16px while `<h2 class="h2">We say when to
skip</h2>` renders at 24px. Expected: the thing that looks like the page title to be the
page title. Harms: screen-reader users navigating by heading, and search engines. Also a
design-system smell — class names pinned to visual sizes are the sign the type scale and
the semantics were never reconciled.

**10. No price on the paid things I was actually shown.**
URLs: `resource.html?id=r-27f9d9ec35` (`subscription`), and "Claude Design Fundamentals"
(`sign-up needed`, *"free to enrol, and the certificate costs"*). The chip vocabulary
across all 48 designer cards is `free`, `sign-up needed`, `subscription` — no amount.
Price chips exist elsewhere in the catalogue (`from $49`, `from $995`, `from $2,999`,
`from $3,000`, on four cards). Expected: to know what I would pay before I click. Harms:
anyone whose result set does not happen to contain one of those four rows.

**11. Eight cards in one cell are visually identical.**
URL: `browse.html?role=designer&level=confident`. Grouped all 22 cards by
badge + source + all chips + footer line: one signature covers 8 of them —
`Skimmed | Anthropic Academy | docs/15 min/free | Checked 29 Aug 2026 · No publish date
given`. Expected: either the visual differentiation the eight deserve, or the treatment the
site already gives the same material for five other functions ("Use cases for Sales",
"…for Legal", "…for HR", "…for Finance", "…for Operations"). Harms: anyone at "used it a
lot", the busiest designer cell.

**12. The path drops the Skip line.**
URL: `paths.html?id=judging-ai-design-work`. The string "Skip if" appears zero times in the
rendered text. Every Browse card has one; the footer promises one on every entry. Harms:
the reader who commits two hours on a curated route with none of the warnings the same
resources carry in the list.

**13. A single-line card title is a 24 px tap target on a phone.**
URL: `browse.html?role=designer&level=builder` at 375 px. Every visible control measured;
only two are under 44 px, one of which is the card title "Encode the brand as a skill" at
242 x 24. Two-line titles get 76 px. Harms: thumbs, mildly. Ranked last because it scrapes
the WCAG 2.2 minimum and the whole card is not the target.

## 11. The one thing that would make me leave and not come back

Nothing on this site made me want to leave. The thing that would stop me coming *back* is
finding 1, and not for the reason it looks like.

I do not return to directories. Nobody does. I return to links other people send me. This
site has a **Copy link** button on every resource page, so it knows that. And the link that
button hands me previews, everywhere, as a grey box reading **"Resource — Learn Claude"**
with no image and a description identical to the other 587. So the good work never travels.
The Skip line on "Design system drift review" is the best sentence I have read about an AI
tool this year, and if I paste it into my team's channel it arrives looking like spam. The
site's only route back to me is the one part of it that was not designed.

## 12. What is genuinely good (honest, brief)

- **The Skip line is the whole product and it earns it.** *"Pure compliance checking against
  your existing tokens.json, not design judgment at all."* *"It is a beginner course that
  spends its last hour on portfolio and interview preparation, so a working designer is
  paying an hour for career advice they did not come for."* No other directory tells me
  what not to open.
- **The "who we is" disclosure.** One person, a DTU researcher, Claude does the reading, and
  *"has not yet read a single resource end to end."* Publishing that raises my trust more
  than any badge could.
- **The counter before I commit.** "8 resources match so far" told me the truth about a thin
  cell before I spent a click.
- **The thin-level offer.** Named counts, one button, correct arithmetic, 44 px tall.
- **The picks reasons are comparative, not promotional.** *"Chosen over the two longer
  written walkthroughs of the same product."* That is a curator, not a marketer.
- **The responsive and accessibility engineering.** Zero horizontal overflow, 44 px chips, a
  proper focus-visible ring moved onto the card with `:has()`, `prefers-reduced-motion`,
  `(hover: hover) and (pointer: fine)`, and `forced-colors: active`. Somebody who cares did
  that.
- **The path's honesty about its own scope.** *"This covers about a fifth of a designer's
  job… and says nothing about the other four fifths."*
- **The `designer` catalogue itself.** 45 of 48 cards are my job. "Design system drift
  review", "Pattern consistency audit", "Design Systems in 2026: Turn Your System into a
  Claude Skill" — I had not seen three of these and I want to read all three.

## 13. Would I come back, and what one thing would make me?

Yes, but not on my own. I would come back the way I come back to anything: because somebody
pasted a link into a channel and the preview made me click. Right now that cannot happen —
every link from here arrives looking like "Resource — Learn Claude", which is what a broken
page looks like.

So: give each resource page its own `<title>` and `og:title` in the served HTML, the card's
own title, and put the `For:` line in the `og:description`. That is the one thing. The
Copy link button is already sitting there waiting for it.

And if I get a second thing — make the badge on the card a link, the way it already is on
the resource page. On my phone, "Skimmed" is a word with no definition, and "Skimmed" is
the only reason I am here rather than on Google.

## Checklist
- [x] I opened the live site
- [x] I tried all four levels
- [x] I quoted at least 5 real titles or lines from the site
- [x] Every number I used is in 00-facts.md, STATUS.md, or quoted from the site
- [x] I looked at a phone width
- [x] I read no file under scripts/ or data/
- [x] I found at least one thing nobody has mentioned before
