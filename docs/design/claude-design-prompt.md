# Prompt for Claude Design

**Date:** 2026-08-19
**Attach these four files to the session:**

- `docs/design/design-brief.md`
- `docs/design/ux-copy.md`
- `assets/css/tokens.css`
- `data/sample-items.json`

Also attach the icons if the tool accepts images: `assets/icons/roles/*.png`,
`assets/icons/level/moon-frame.png`, `assets/icons/time/hourglass-frame.png`.

---

## The prompt

Copy everything below.

---

I'm building a static directory site called **Learn Claude**. Tagline: *Find what's worth
your time.*

It lists the best places to learn Anthropic's Claude. What makes it different from every
other link list: **every resource has a "Skip if:" line telling you when not to bother**,
a visible date we last checked it, and an honest label for how thoroughly we checked. The
design has to make those three things feel like the point, not like small print.

I've attached four files. Please follow them exactly:

- `design-brief.md` — the visual system and the rules
- `ux-copy.md` — every string. Use these words. Do not write new copy.
- `tokens.css` — every colour, size, radius and font. Do not introduce values outside it.
- `sample-items.json` — 13 real resources, chosen to cover every card state

**Design the Browse screen first.** It's the heart of the site and it exercises every
component. Then the Home screen, then the resource detail.

### The feel

A scientific field journal printed on warm parchment. Ivory surfaces, never white, never
cool gray. Editorial serif carries the body text at 20px — that single decision is what
makes it read as a publication instead of a product. Sans-serif is chrome only: nav,
buttons, badges, metadata. Flat throughout: elevation comes from tone plus a 1px hairline,
never a shadow. Quiet, generous whitespace, low density.

### Non-negotiable

- **No box-shadow anywhere.** Layering is `#f0eee6` page → `#faf9f5` card → `#f5e3c7`
  feature, plus 1px `#cccbc8` borders.
- **No gradient, blur, glow, or glass.**
- **Palette is ivory, oat, clay only.** No blue, no green, no cool gray. Never pure white.
- **Clay `#d97757` appears once per page**, on one filled button. Not on icons, not on
  links, not on hover states. Its text is `#141413`, not white — white on clay fails
  contrast at 3.12:1.
- **Body copy is serif at 20px.** If body text ends up sans, the design has failed.
- **Filled buttons use `border-radius: 0 0 8px 8px`** — bottom corners only, top corners
  sharp. This is the signature detail. Not a pill, not evenly rounded.
- **Cards are 24px radius.** Nav, badges and links have no radius.
- **Inline links keep a visible underline** always, not on hover. Print convention.
- **No thumbnails on cards.** They import each source's branding and make the grid noisy.
- **Secondary text uses `--bark #6c6b66`**, never the lighter neutrals — they fail
  contrast and the dates have to be readable.
- No tabs, no carousels, no dropdown navigation, no stock photos, no emoji, no icon fonts.

### Browse screen — what's on it

Top bar: wordmark left; **Browse · Paths · How we check** right. Flat, no shadow, no blur.

Left column, filters. Only three groups visible: **Role, Level, Time**. Topic, Format and
Cost sit behind a collapsed **More filters** control — a person can't pick a topic before
they know which topics exist. Below 768px filters move into a bottom sheet with a
**Show 24 resources** confirm button.

Main column: a **Search** field, a **Sort** control, an exact live result count
(`77 resources`), then the cards.

### The card — this is the important component

Information in this exact order:

1. Badge — how thoroughly we checked it
2. Title, serif
3. Source and author, sans, `--bark`
4. Three small chips: format · time · cost
5. `For:` — one line, who it's for
6. `Skip if:` — one line, **serif, visually heavier than everything above it**
7. Footer row: `Checked 19 Aug 2026`, plus an outdated flag when the resource is over a
   year old

`Skip if:` is the whole product. Give it real weight. If it looks like a footnote, the
card is wrong.

### The four badges

Colour must never carry this alone — the words are always visible.

| Reads | Treatment |
|---|---|
| Read in full | Filled `#141413`, text `#faf9f5` |
| Read by AI | Filled `#e3dacc`, text `#141413` |
| Skimmed | Outline `#87867f`, text `#6c6b66`, transparent fill |
| Found only | Outline `#cccbc8`, text `#6c6b66`, transparent fill |

They always sort in that order.

### Home screen — the first thing anyone sees

Two columns. Left: a sentence the visitor fills in.

> I'm a **[role]** and I've **[level]**.

Two blanks only. Each is underlined 2px in clay and opens a set of choices below the
sentence. This underline is the one decorative use of clay allowed, because it marks the
thing you act on. Time is deliberately not asked here — it is a filter on the Browse
screen instead.

Right: a square illustration that **changes when the role changes**. Ten roles, ten
drawings, attached. Level does not change it.

Below the sentence: a search field with the placeholder *"Or describe what you want to
do…"*, and one filled clay **Show me** button. That button is the page's only clay element.

No hero image. No carousel.

### Icons

All in one hand: thick uneven hand-drawn black outline, one flat `#e3dacc` accent shape,
`#faf9f5` fill elsewhere. Use the attached files. Do not draw new ones in another style.

Level and time each use **one** drawing whose fill level changes — a moon that fills left
to right, an hourglass that fills bottom to top. Two axes, two motions, so they never
read as the same thing.

### Motion

Almost none. Motion confirms a choice, it never decorates.

- Role chosen → illustration cross-fades, 220ms
- Level or time chosen → icon fill grows, 550ms, ease-out
- Filter applied → results change instantly, no animation. Speed is the feature.
- Hover → colour change only. Nothing moves, nothing lifts.

Honour `prefers-reduced-motion`.

### Accessibility, not as a later pass

- Visible focus ring on everything: 2px `#141413`, 2px offset.
- Touch targets 44px minimum.
- Result count is `aria-live="polite"` so filtering is announced.
- Role icons are decorative with empty `alt`; level and time icons carry real `alt` text.
- Never signal a badge or a freshness state with colour alone.

### Deliverable

Static HTML, CSS and vanilla JavaScript. No framework, no build step. Search and filtering
run client-side against a JSON file and must feel instant. Mobile first — single column
below 768px.

Use the 13 real resources in `sample-items.json`. Don't invent placeholder content — they
were picked specifically to show every state you need to draw, including the longest title
and the states with no `reviewed` example.

One last thing: this site is **not affiliated with Anthropic** and must never look like an
official Anthropic property. Take the design approach, never their assets — no Anthropic
logo, wordmark, or artwork anywhere.

---

## If the output drifts

It always drifts in the same three places. Say these back verbatim:

1. *"Remove every box-shadow. Elevation is tone plus a 1px border."*
2. *"Body copy must be serif at 20px, not sans."*
3. *"Filled buttons are `border-radius: 0 0 8px 8px` — bottom corners only."*

And if it gets colourful: *"The palette is ivory, oat and clay. Clay appears once per
page. Remove everything else."*
