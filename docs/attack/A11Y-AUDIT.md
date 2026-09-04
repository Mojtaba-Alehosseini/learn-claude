# Accessibility pass — 1 September 2026

The first accessibility pass actually run. `docs/specs/2026-08-23-accessibility-audit.md`
set the method and found three problems; **all three were fixed before this pass began**,
and this run confirms them fixed and then covers what the spec did not: the picks block,
which did not exist when the spec was written, and the four areas below it.

Run on the local server at desktop (1280×900, 900×1500) and at 375 px, with
`scripts/a11y-audit.js` for the machine-checkable half and a real keyboard for the rest.
Every Tab in this document is a real key press, not a synthetic event — synthetic key
events do not move focus, so a "keyboard test" built on them proves nothing.

---

## The three problems from the spec: all fixed, all confirmed

| Spec problem | State today |
|---|---|
| `index.html` has no `h1` | **Fixed.** "Find what's worth your time." is an `h1.meta`. The solution differs from the spec's suggestion, for a stated reason in the markup: the big `.display` line contains two buttons, so making *it* the heading would have made a screen reader read the whole control as the page title. |
| `--flag-outdated` fails AA | **Fixed** with `#ac5233`. Measured today where it actually ships — a card — at **4.97:1** on `#faf9f5`, 12 px. Passes. |
| The mobile sheet does not hold the keyboard | **Fixed.** Re-tested below with 40 real Tab presses. |

---

## 1. Contrast, computed in the browser

Every text/background pair that renders, measured from `getComputedStyle` on the live
page rather than read off the token file. **Nothing fails.**

| What | Size | Pair | Ratio | Needs |
|---|---|---|---|---|
| `--bark` on the canvas | 12–16 px | `#6c6b66` on `#f0eee6` | **4.60** | 4.5 |
| `--bark` on a card | 12–16 px | `#6c6b66` on `#faf9f5` | **5.07** | 4.5 |
| `.picks-meta` — "picked by AI · date" | 12 px | `#6c6b66` on `#f0eee6` | **4.60** | 4.5 |
| `.pick-reason` — the pick's sentence | 16 px | `#6c6b66` on `#f0eee6` | **4.60** | 4.5 |
| Badge text | 12 px | `#6c6b66` on `#faf9f5` | **5.07** | 4.5 |
| `--flag-outdated` where it ships | 12 px | `#ac5233` on `#faf9f5` | **4.97** | 4.5 |
| Footer link | 18 px | `#faf9f5` on `#141413` | **17.50** | 4.5 |
| Footer note | 12 px | `#b0aea5` on `#141413` | **8.29** | 4.5 |
| Chip on the panel tone | 16 px | `#141413` on `#e3dacc` | **13.31** | 4.5 |
| Focus ring, footer | — | `#faf9f5` on `#141413` | **17.50** | 3 |

Thirty-five distinct text/background pairs were swept on Browse alone; zero failed.

**The thinnest margin on the site is the picks block**: `.picks-meta` and `.pick-reason`
both sit at **4.60 against a 4.5 requirement**. They use `--bark`, which was built to
clear exactly that bar on this canvas. It passes, and it has no room to spare — a future
lightening of `--bark`, or moving those two lines onto the panel tone, breaks them.

**One latent risk, not shipping today.** On `--surface-panel` (`#e3dacc`):

| Ink | Ratio on panel | Verdict |
|---|---|---|
| `--bark` `#6c6b66` | 3.86 | would fail at normal size |
| `--clay-text` `#ac5233` | 3.78 | would fail at normal size |

Neither ships there. `--surface-panel` carries exactly two things — the path step tile,
which holds an image and no text, and the home page chip while its drawing shows, which
uses near-black ink at 13.31. So there is nothing to fix. It is recorded because putting
secondary or clay text on a panel later would fail silently, and the spec already flagged
this when it preferred `#9a492e` over `#ac5233` for precisely this reason.

---

## 2. Keyboard, all five pages

Walked with real Tab presses on `index`, `browse`, `paths`, a path detail page,
`resource` and `how-we-check`.

- **Focus order follows the DOM, and the DOM follows the screen.** The one "tab moves up
  the page" warning on Browse is the two-column layout — down the filter rail, then up to
  the search field at the top of the results column. That is the reading order for two
  columns, as the spec already recorded.
- **The skip link is the first focusable element** and its target exists.
- **A visible focus state on every interactive element.** `--focus-ring` is
  `2px solid #141413` at 2 px offset, swapped to ivory in the footer. Measured on the
  focused element, not assumed.
- **No unreachable control** and **no trap** other than the sheet.
- Path step cards use `:has()` to move the ring from the title's words to the whole card.
  Confirmed working: with a step title focused, the link's own outline is `none` and the
  card's is `solid`.

---

## 3. The mobile filter sheet

At 375 px, sheet open, **40 real Tab presses**:

| Check | Result |
|---|---|
| `role="dialog"`, `aria-modal="true"`, `aria-label="Filters"` | present |
| Focus moves into the sheet on open | lands on **Close** |
| Tab stays inside | **0 escapes in 40 presses**, wrapped back to Close twice |
| Escape closes it | yes |
| Focus returns to the opener | yes — `button#openSheet` |
| Body scroll restored | yes, `overflow` back to `visible` |

---

## 4. Announcements

- **The result count announces.** `#count` is `role="status"` with `aria-live="polite"`,
  and the text is written into the same node on every render, so the live region is never
  torn down and rebuilt.
- **The picks block** needed two fixes, both below. After them: one `h2` inside the
  region, the region named by that heading, and the "everything else" heading a sibling
  that precedes the list it names.
- **The two-pick state** reads correctly: the heading itself says "Start with these two"
  over exactly two cards, so the count is in the announced text rather than only in the
  layout.
- **The empty-cell state** is a `.empty` block whose first line is a `<strong>` — "We
  have nothing for this combination yet." The count line above it announces "0 resources"
  through the live region at the same moment, so the change is announced even though the
  message itself is not a live region.

---

## 5. Images and icons

| Surface | Count | Handling |
|---|---|---|
| Home page drawings | 2 `<img>` | `alt=""` — decorative. The chip beside each carries the words ("not a coder"). |
| Path step format tiles | 11 `<img>` | `alt=""` — the format is already in the step kicker ("Step 1 · Article"). |
| Publisher marks | `<img alt="" width=16 height=16>` | decorative; the publisher name is in the text line beside it. |
| Browse card format icons | 30 CSS backgrounds | `aria-hidden="true"`, no text. |

**No image on the site has a missing `alt` attribute, and none has a non-empty one.**
That is the correct answer here rather than a gap: every drawing is paired with its own
label in text, so naming the image would make a screen reader say everything twice. The
failure mode the brief named — a reader hearing forty filenames — does not occur.

---

## 6. Cards — and the largest finding of this pass

**Every browse card was a single `<a>` wrapped around the entire card.** Its accessible
name was therefore every word on it.

Measured on a ten-card page before the fix:

| | |
|---|---|
| Link name length | **70 to 123 words**, median 80 |
| Longest | **689 characters** |
| What one link announced | tier badge, title, publisher, three chips, the whole `who_for`, the whole `skip_if`, the checked date and the publish note — as the *name of the link* |

A screen reader user tabbing the results heard all of that per card, with no way to skim.
On a 618-resource browse this is the difference between a usable list and an unusable one.

The site already had the right pattern: path step cards wrap only the title in the link
and spread it over the card with `.sp-title a::after`. Browse cards now do the same.

**After the fix: 4 to 10 words per link name.** The rest of the card is still read as
content, in place, when the reader moves through the page.

---

## Every change, old and new

### 1. `assets/js/ui.js` — `LC.card()`: the card is an article holding one link

*Was:* `<a class="card" href="…">` wrapping the badge, title, source, chips, `For:`,
`Skip if:`, path line and footer, closing `</a>`.

*Now:* `<article class="card">` with `<div class="card-title"><a href="…">Title</a></div>`
as the only link, closing `</article>`.

*Why:* the link's accessible name was the whole card — 70–123 words. **Pixel-identical**;
verified by screenshot against the same page before the change.

### 2. `assets/css/site.css` — the overlay and the card's focus ring

*Added:* `position: relative` on `.card`; `.card-title a { color: inherit;
text-decoration: none }`; `.card-title a::after { content:""; position:absolute; inset:0 }`;
and `.card-title a:focus-visible { outline: none }` with
`.card:has(.card-title a:focus-visible) { outline: var(--focus-ring) }`.

*Why:* keeps the whole card clickable and rings the card rather than four words of title.
Verified: probing the middle and lower third of a card resolves to the title link, on
desktop and at 375 px; keyboard focus puts `solid` on the card and `none` on the link.
**No new hardcoded values — the ring is the existing `--focus-ring` token.**

### 3. `assets/css/site.css` — the path card's ring, scoped

*Was:* `.sp-card:has(a:focus-visible)`
*Now:* `.sp-card:has(.sp-title a:focus-visible)`

*Why:* the old selector also matched the "Start with this" button inside the card, so
focusing that CTA drew **two rings at once** — one round the button, one round the whole
card — and a keyboard user could not tell which was focused. Found in the keyboard walk.

**This one is a visible change and is flagged for review** (see the questions below):
focusing the CTA no longer draws a ring around the whole card. Focusing the step title
looks exactly as it did.

### 4. `assets/js/browse.js` — the picks region names itself once

*Was:* `<section class="picks" aria-label="Start with these three">` containing an `h2`
of the same words.
*Now:* `<section class="picks" aria-labelledby="picksHeading">` with
`<h2 id="picksHeading">`.

*Why:* the label repeated the heading verbatim, so the region was announced as "Start with
these three" and then the heading as "Start with these three" again.

### 5. `assets/js/browse.js` — "Everything else for you (N)" leaves the picks section

*Was:* the `h2.picks-rest` sat **inside** `<section class="picks">`.
*Now:* the section closes first; the heading is its next sibling.

*Why:* that heading labels the results list, and the results list is not inside the picks
section. Inside it, the structure told a screen reader that everything else was part of
the picks. Confirmed after the change: `restStillInsidePicks: false`,
`restIsSiblingOfSection: true`, and the picks region now contains exactly one heading.

---

## Questions for Morteza

1. **The path-card double ring (change 3).** Fixed as described, and it is a visible
   change: the CTA inside a step card no longer rings the whole card when focused. I
   judged two simultaneous rings to be worse than none on the card, because the point of
   a focus ring is to say *which one thing* is focused. If you would rather keep the old
   behaviour, revert that one selector.

2. **`--bark` at 4.60 in the picks block.** It passes, with 0.10 of margin. Worth knowing
   before any future change to `--bark` or to what surface the picks block sits on. No
   action proposed.

---

## What this pass did **not** cover

- **No screen reader was run.** NVDA, JAWS and VoiceOver each behave differently, and
  nothing here is a claim about what one of them actually says. What was verified is the
  structure that determines it — roles, names, heading order, region labelling, live
  regions. That is not the same thing, and a real screen-reader session is still owed.
- **Zoom to 400 %** — not tested. Still open from the spec.
- **Windows High Contrast Mode** — not tested. Still open from the spec.
- **Colour vision deficiency** — not tested. Nothing on the site uses colour alone to
  carry meaning, so the risk stays low, but it is untested rather than cleared.

---

## After the changes

`scripts/a11y-audit.js` on all five pages: **0 failures**, 18 passes each. The remaining
warnings are the ones the spec already ruled correct — no live region on the four pages
that have no changing count, and the two-column tab order on Browse.

Catalogue and picks validators re-run afterwards, and the browse query suite: nothing
else moved.
