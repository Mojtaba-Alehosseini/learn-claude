# Design brief

**Date:** 2026-08-19
**Status:** current. Replaces `2026-08-16-visual-direction.md` and the earlier `design-brief.md`, both deleted.
**Read with:** `docs/specs/2026-08-19-directory-spec.md` (what the site does) and
`docs/design/ux-copy.md` (every string). This file is only how it looks.

**Files this brief depends on**

| File | What it is |
|---|---|
| `assets/css/tokens.css` | Every colour, size, radius and font. Nothing may be hardcoded. |
| `docs/design/anthropic-style-reference.md` | The captured Anthropic system, for reference |
| `data/sample-items.json` | 13 real resources chosen to cover every card state |
| `assets/icons/roles/*.png` | 10 role illustrations |
| `assets/icons/level`, `assets/icons/time` | The two fillable icons |
| `docs/design/fillable-icons.html` | Working demo of the fillable icons |

---

## 1. The feeling

A scientific field journal on warm parchment.

Ivory surfaces instead of the usual cool gray. An editorial serif carrying the body text
at 20px, which almost no tech site does — that alone is what makes the page read as a
publication rather than a product. Sans-serif handles only the chrome. One clay accent,
which appears only where you must act. Flat surfaces: elevation comes from tone and a
1px hairline, never a shadow.

Reference: `https://styles.refero.design/style/d469cba4-c448-4a43-a033-883f8bfcdc42`,
checked 2026-08-19.

**We take the approach, never the assets.** No Anthropic illustration, logo, wordmark, or
image is copied, downloaded, or hotlinked. Two reasons, both real: they are licensed brand
assets, and a directory *about* Claude that wears Anthropic's artwork looks official when
it is not. A visual approach is not owned. A drawing is.

The footer says plainly: *not affiliated with Anthropic*.

---

## 2. Colour

All eleven values are in `tokens.css`. The ones that carry meaning:

| Token | Hex | Where |
|---|---|---|
| `--ivory-medium` | `#f0eee6` | The page. Everything sits on this. |
| `--ivory-light` | `#faf9f5` | Cards. One tonal step up — this replaces a shadow. |
| `--manilla` | `#f5e3c7` | The featured hero card only. Nothing else. |
| `--oat-warm` | `#e3dacc` | Grouped panels, and the accent inside every icon. |
| `--slate-dark` | `#141413` | All primary text, all hairlines, and the footer background. |
| `--bark` | `#6c6b66` | Dates, source, all secondary text. **Ours, not Anthropic's — see below.** |
| `--cloud-medium` | `#b0aea5` | Decorative only: placeholders, inactive nav, dividers. Never readable text. |
| `--stone` | `#cccbc8` | Hairline borders. |
| `--clay` | `#d97757` | **One filled button per page. Nothing else, ever.** Text on it is `--slate-dark`, not white. |

**One deliberate departure from Anthropic.** Measured against the `#f0eee6` page:
`--cloud-medium` is 1.91:1 and `--cloud-dark` is 3.15:1. Both fail WCAG AA at the sizes we
need. Anthropic uses them for small metadata anyway. We cannot — a directory whose entire
product is a date and a one-line judgement has to make those legible. `--bark` is
`--cloud-dark` darkened along its own hue until it clears 4.60:1. It stays warm and it
passes at any size. Use it for every piece of secondary text.

White on clay is 3.12:1 and also fails. Clay buttons take `--slate-dark` text (5.90:1).

**Hard rules**

- No cool gray, no blue, no green. The palette is ivory, oat, clay. That is all.
- No `box-shadow` anywhere. Elevation is `#f0eee6` → `#faf9f5` → `#f5e3c7` plus a 1px border.
- No gradient, glow, blur, or glass.
- Never pure white `#ffffff`. It reads clinical and breaks the paper.
- Clay is not for icons, decoration, hover states, or links. Filled primary buttons only.

No dark mode in v1.

---

## 3. Type

| Role | Family | Where |
|---|---|---|
| Serif — the voice | Tiempos | Body copy at 20px, display headings, card titles, `Skip if:` |
| Sans — the chrome | Styrene B | Nav, buttons, badges, filter labels, metadata, footer |

**Body text is serif at 20px.** This is the single most important typographic decision and
the easiest to lose. If body copy ends up in sans, the page becomes an ordinary product
site.

Scale is in `tokens.css`. Line length caps at `--measure` (68 characters).

The dual display system: sans at 61px weight 700 for declarative statements, serif at 68px
weight 400 for editorial ones. Pick one per page, do not use both in the same block.

**Known limitation:** the licensed Tiempos cut in this project is *Fine*, drawn for large
display sizes. At 20px it will look lighter than Anthropic's, which uses Tiempos Text. If
Text is acquired later, drop the files into `assets/fonts/tiempos/` and update the three
`@font-face` rules. Nothing else changes.

---

## 4. Shape and space

- **Cards:** 24px radius. Padding 24–32px.
- **Filled buttons:** `border-radius: 0 0 8px 8px` — bottom corners only, top corners
  sharp. This is the signature detail. It reads as a tab pulled from a stack. Do not
  round it evenly, and do not make it a pill.
- **Outlined buttons:** 12px radius, 1px `--cloud-dark` border, transparent fill.
- **Nav, links, badges:** no radius.
- **Inline links:** underline always visible. Print convention, not reveal-on-hover.
- **Spacing:** 4px base — 4, 8, 12, 16, 24, 32, 48, 76, 100. Nothing outside the scale.
- **Section rhythm:** heading → one sentence → content → 100px gap. Repeat.
- **Page max width:** 1280px.

---

## 5. Screens

Five. Build in this order.

1. **Home** — the two questions, then what the site is.
2. **Browse** — the catalogue with search and filters. The heart of the site.
3. **Resource detail** — one resource in full.
4. **Path** — an ordered sequence.
5. **How we check** — the criteria, and the certification warning.

### 5.1 Home, first screen

Two columns. Left: the sentence the visitor completes. Right: the role illustration.

> I'm a **[role]** and I've **[level]**.

Each underlined blank opens its choice set below the sentence. Underline is 2px clay —
this is the one decorative exception, and it is allowed because the underline marks the
thing you must act on.

**The illustration reacts to the role only.** Ten roles, ten drawings, in
`assets/icons/roles/`. Level does not change it.

Below the sentence: the search field, and one filled clay **Show me** button. That is the
page's single clay element.

No hero image. No carousel. No dropdown nav.

### 5.2 Browse

Filters in a left column on desktop, in a bottom sheet below 768px.

Six filter axes is more than a person can hold at once, so only three are visible: **role,
level, time**. Topic, format and cost sit behind **More filters**, collapsed. Reason: you
cannot choose a topic before you know which topics exist.

Note the asymmetry: time is a good *filter* but was a bad *question*. Measured on the real
77 items, adding time to the opener dropped the median result count to zero and emptied
half of all possible answers. It earns its place here, after results exist.

Result count is exact and live: `77 resources`.

### 5.3 The card

In this order, top to bottom:

1. Badge — how we checked it
2. Title (serif)
3. Source and author (sans, muted)
4. Three chips: format · time · cost
5. `For:` — one line
6. `Skip if:` — one line, serif, heavier than the rest
7. Footer: `Checked 19 Aug 2026`, plus an outdated flag if applicable

**No thumbnails.** They import each source's branding and turn a calm grid into noise.

`Skip if:` gets deliberate visual weight. It is the only thing on the card no competitor
has.

### 5.4 Badges — how we checked it

Four states. Copy is in `ux-copy.md`. **Colour never carries this alone** — the word is
always present.

| Value | Reads | Treatment |
|---|---|---|
| `reviewed` | Read in full | Filled `--slate-dark`, text `--ivory-light` |
| `ai-reviewed` | Read by AI | Filled `--oat-warm`, text `--slate-dark` |
| `previewed` | Skimmed | Outline `--cloud-dark`, text `--cloud-dark` |
| `listed` | Found only | Outline `--stone`, text `--cloud-medium` |

Sort order everywhere: Read in full → Read by AI → Skimmed → Found only.

Note: `data/items.json` currently contains no `reviewed` items, because no person has
confirmed one yet. The state still has to be designed.

---

## 6. Icons

Three sets, all in the same hand: thick uneven black outline, one flat `--oat-warm` accent
shape, `--ivory-light` for everything else, on `--ivory-medium`.

**Role — 10 drawings.** `assets/icons/roles/`. Shown large on the home screen, small
beside a filter label. Each has exactly one accent shape; accent covers 3–24% of the
frame. Prompts and rules: `prompts/images/role-icons.md`.

**Level and time — 2 drawings, not 8.** One moon, one hourglass. The amount of beige is
set by CSS, so four states cannot drift apart, and the change animates. Level fills left
to right like a phase; time fills bottom to top like sand. Two axes, two motions. Working
demo: `docs/design/fillable-icons.html`.

Any new icon goes through `scripts/normalise-icon.py`, which snaps it to the four brand
colours and reframes it to 93% of the square. Generated images never ship raw.

---

## 7. Motion

Restrained. Motion confirms a choice; it never decorates.

| Where | What |
|---|---|
| Role chosen | Illustration cross-fades, `--dur-base` |
| Level or time chosen | Icon fill grows, `--dur-slow`, `--ease-out` |
| Filter applied | Results update instantly. No animation — speed is the feature. |
| Hover | Colour only. Nothing moves, nothing lifts. |

`prefers-reduced-motion` is honoured in `tokens.css` — all durations drop to zero.

---

## 8. Accessibility floor

Not optional, and not a later pass.

- Every text colour in `tokens.css` was measured on 2026-08-19, not assumed. Results:

  | Pair | Ratio | |
  |---|---|---|
  | `--slate-dark` on page | 15.87 | pass |
  | `--slate-dark` on card | 17.50 | pass |
  | `--bark` on page | 4.60 | pass |
  | `--slate-dark` on clay button | 5.90 | pass |
  | `--cloud-dark` on page | 3.15 | **large text only** |
  | white on clay button | 3.12 | **fails — do not use** |
  | `--cloud-medium` on page | 1.91 | **fails — decorative only** |

  Re-measure whenever a colour pairing changes.
- Never signal how-we-checked or freshness by colour alone. Always pair with the word.
- Focus ring visible on everything: 2px `--slate-dark`, 2px offset. Never removed.
- Touch targets 44px minimum.
- The result count is `aria-live="polite"` so filtering is announced.
- Role icons are decorative — empty `alt`. Level and time icons carry a real `alt`.
- Works with JavaScript slow or failing: the resource list renders before search does.

---

## 9. Do not

- Drop shadows, gradients, glass, blur, glow
- Cool grays, blue, green, or any colour outside ivory / oat / clay
- Pure white surfaces
- Clay on anything except one filled button per page
- Evenly rounded filled buttons — the bottom-only radius is the signature
- Body copy in sans-serif
- Thumbnails on cards
- Stock photography, emoji, icon fonts
- Tabs, carousels, dropdown navigation
- Anthropic's logo, wordmark, colours, or artwork
- Any layout that makes this look like an official Anthropic property

---

## 10. Build

Static HTML, CSS, and vanilla JavaScript. No framework, no build step. One file per page
is fine. Search and filtering are instant and client-side, reading `data/items.json`.

Start with **Browse**. It is the heart of the site, it exercises every card state, and
everything else is easier once it exists.
