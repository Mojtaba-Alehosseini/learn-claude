# Claude Design — round 2: the remaining screens

**Date:** 2026-08-21
**Round 1** (`claude-design-prompt.md`) produced the Home screen. That screen is approved.
**This round:** everything else. Home is not to be touched.

**Attach:** `docs/design/ux-copy.md`, `assets/css/tokens.css`, and the current
`data/sample-items.json`.

---

## The prompt

Copy everything below.

---

The Home screen is finished and approved. **Do not redesign it, do not restyle it, do not
"improve" it.** If a decision I make below would change Home, tell me instead of changing it.

What Home already settled, and what every screen from here inherits without discussion:

- The colour system, the type scale, the 20px serif body
- The nav bar and the footer
- The filled button — clay, `border-radius: 0 0 8px 8px`, dark text
- The focus ring, the hover behaviour, the motion timings
- No shadows. No gradients. Elevation is tone plus a 1px border.

Now design the rest of the site. **In this order**, because each one feeds the next:

1. The resource card
2. Browse
3. Resource detail
4. Paths — index, then one path
5. How we check
6. Empty and error states

All copy is in `ux-copy.md`. **Use those exact strings.** Do not write new copy. If a
string you need is missing, ask me for it rather than inventing one.

---

### 1. The resource card — do this first

Every other screen is made of these, so it has to be right before anything else.

Fixed order of information:

1. Badge — how thoroughly we checked it
2. Title, serif
3. Source and author, sans, `--bark`
4. Three chips: format · time · cost
5. `For:` — one line
6. `Skip if:` — one line, **serif, heavier than everything above it**
7. Footer: checked date, plus a flag if it looks old

**`Skip if:` is the reason the site exists.** If it reads as a footnote, the card is wrong.

Design it against real content, not comfortable content:

- Longest title is **88 characters** — *"Ethical guidelines on the use of AI and data in
  teaching and learning for educators (EU)"*
- Shortest title is **9 characters** — *"ClaudeLog"*
- Longest `Skip if:` is **300 characters**, three sentences. It must not be truncated.
- Longest `For:` is **183 characters**
- Longest source name is **"Society of Professional Journalists"**

Show me the card in all of these states:

- Each of the four badges
- In a path → `Step 2 of 6 in Your first week with Claude`
- Published over a year ago → the outdated flag
- **No published date at all** — see below
- Dead link → `This link no longer works`

#### The date problem

The footer shows `Checked 21 Aug 2026`. That date is always known, always shown, and
carries the weight — it is the date we control.

`Published` is different. **177 of 288 resources publish no date at all** — mostly
documentation, which is maintained continuously and simply does not print one. So for
**61% of the catalogue we cannot say whether it is stale.**

Three states, all three need drawing:

1. Published, under a year old → nothing special
2. Published, over a year old → `Published over a year ago — may not match Claude today`
3. **No published date → we say we do not know**

State 3 is the most common one. It must not look like broken data or a missing field. It
is a true statement about the resource. Find a way to say "no date published" that reads
as honesty, not as an error.

#### The publisher problem

Every resource has a `source` — the publisher as a reader would name it. There are **110
distinct publishers**, and **79 of them appear exactly once**.

**93 of 288 (32%) are published by Anthropic themselves.** Those are often the best answer
and a visitor genuinely wants to spot them.

The constraint: this site is **not affiliated with Anthropic** and must never look like it
is. I need a treatment that says *"this resource is from Anthropic"* and never implies
*"this site is from Anthropic"*.

- No Anthropic logo, wordmark, or artwork. Ever.
- Not clay — clay is spent on the one button per page.
- It must not outrank the how-we-checked badge. How carefully we checked matters more
  than who made it.
- It has to survive 109 other publisher names without becoming a logo wall.

**Show me two options for this one.**

---

### 2. Browse

Top bar: wordmark left, **Browse · Paths · How we check** right.

Left column — filters. Three groups visible: **Role, Level, Time**. Then a divider and
**More filters**, collapsed, holding **Topic, Format, Cost**. Nobody can pick a topic
before they know which topics exist.

Applied filters show as removable chips: `researcher ×`

Main column — **Search** field, **Sort** control, an exact live count, then the cards.

The count is always exact and never rounded: `77 resources` · `1 resource` ·
`12 resources for a researcher who has never used Claude`. When the count gets low it
offers the way out: `6 resources. Remove a filter to see more.`

Sort options: **Best checked first** · **Newest first** · **Shortest first**

Below 768px: filters move into a bottom sheet, title **Filters**, confirm button
**Show 24 resources**, dismiss **Close**.

Design against the real distribution, so the filter panel is not a fantasy:

| Filter | Reality |
|---|---|
| Format | article 108 · docs 70 · course 54 · code 32 · video 10 · podcast 7 · hands-on 7 |
| Level | basic 116 · confident 80 · builder 47 · never used 45 |
| Cost | free 214 · free, sign-up 42 · subscription 20 · pay once 12 |
| Checked | Skimmed 141 · Read by AI 99 · Found only 48 · **Read in full 0** |

That last row is not a placeholder. **No resource has been read in full.** Nobody has
finished a course end to end yet. Draw the badge, because it will exist — but do not draw
a screen that implies we have any. If Browse looks wrong or dishonest with that badge
absent everywhere, say so. That tells me something important about the promise the site
is making, and I would rather hear it now.

---

### 3. Resource detail

Back link: **← Back to browse**
Primary button: **Open on [source name]** — this is the page's one clay element
Secondary: **Copy link**

Sections, in order:

- **What it teaches**
- **Who it's for**
- **Skip it if**
- **Before this** — prerequisites, omitted entirely when empty
- **After this** — next step in a path, omitted entirely when empty
- **How we checked this one**

Provenance line at the bottom, quiet but present:

> Checked 21 Aug 2026 · Published 4 Mar 2026 · Found through the Anthropic Academy catalogue

Design the version where `Published` is unknown and both optional sections are absent —
that is the common case, and the page must not look empty.

---

### 4. Paths — new, does not exist yet

A path is an ordered route through resources. Search gives you one thing. A path tells you
what order to do things in, and that is the part nobody else answers.

Heading: **Paths**
Intro: *A short list, in order. Start at the top.*
Note: *We do not track your progress. Nothing here needs an account.*

There are three paths, 5–6 steps each.

**Index screen.** Three paths. Not a card grid — these are routes, and they should read as
routes. Each shows title, who it is for, and a stats line: `6 steps · about 3 hours · free`.

**One path screen.** The ordered steps. The order must be unmistakable — someone landing
halfway down should know instantly they are at step 4 of 6. Step marker copy: `Step 3`.

Each step carries two different kinds of information, and the difference has to be legible:

- **The resource** — title, format, time, cost, badge. Not ours.
- **The `why`** — one or two sentences on why it sits at *that* position and not another.
  Up to 180 characters. **This is ours, and it is the reason paths exist.**

Give the `why` the same weight `Skip if:` gets on a card. It is not a caption.

A real example, so you can see the shape:

> **Getting good at Claude Code** — for developers who have installed it and are getting
> mediocre results. 6 steps · about 3 hours · free.
>
> **Step 2.** Best practices for Claude Code · Anthropic · docs · under 1 hr · free · Read by AI
> *The densest thing written about Claude Code, and everything after this assumes you have
> read it.*

Also design the state where a path is not ready:
**This path isn't ready.** We only publish a path once every step in it has been checked.

---

### 5. How we check

The About page, and the page that has to earn trust. Heading: **How we check**.

Opening line, set large — it is the argument the whole site rests on:

> We would rather have 70 resources we can vouch for than 700 we cannot.

Sections: **What we do** · **How thorough we were** · **What we will not do** ·
**About Claude certification** · **Found something wrong?**

The four levels are explained here in full. This is the only page where the badges are
defined rather than used, so the explanation should look like a definition list, not like
four more badges floating in prose.

Full copy is in `ux-copy.md`. This page is mostly text — it is the one place where the
20px serif has to carry several hundred words comfortably. Set the measure properly.

---

### 6. Empty and error states

All copy in `ux-copy.md`. Design these four:

- **Nothing matches all of those.** Try removing one filter — time is usually the one to loosen.
- **No match for "[query]".** Try fewer words, or browse by role instead.
- **We have not covered this role yet.** It's on the list. Browse everything instead.
- **The directory didn't load.** Reload the page. If it keeps happening, the site is broken and we want to know.

Search is instant and client-side. **There is no spinner in normal use.** Do not design a
loading state for search — speed is the feature, and a spinner would advertise the opposite.

---

### Accessibility, in the design and not after it

- Visible focus ring on everything: 2px `#141413`, 2px offset
- Touch targets 44px minimum
- The result count is `aria-live="polite"`, so filtering is announced
- Never signal a badge, a freshness state, or a publisher with colour alone
- Inline links keep a visible underline at rest, not on hover

---

### Deliverable

Static HTML, CSS, vanilla JavaScript. No framework, no build step. Mobile first, single
column below 768px.

**Export the markup and CSS cleanly.** I am wiring this to real data outside this tool, so
I need structure and styles — not a self-contained prototype with content baked in. Where
text comes from data, leave an obvious hook rather than hard-coded strings.

Not affiliated with Anthropic. Take the design approach, never their assets.

---

## If the output drifts

The same three, verbatim:

1. *"Remove every box-shadow. Elevation is tone plus a 1px border."*
2. *"Body copy must be serif at 20px, not sans."*
3. *"Filled buttons are `border-radius: 0 0 8px 8px` — bottom corners only."*

New for this round:

4. *"The `why` on a path step is not a caption. It carries the weight `Skip if:` carries on a card."*
5. *"Home is approved. Revert any change you made to it."*
