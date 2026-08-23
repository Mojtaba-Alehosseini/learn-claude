# Accessibility audit — 2026-08-23

First accessibility pass on the site. Done on the live pages at
https://mojtaba-alehosseini.github.io/learn-claude/, in Chrome, at desktop width and
at 375 px.

Tool: `scripts/a11y-audit.js`. Paste it into the DevTools console and call `LC_A11Y()`.
It reports; it does not change the page. It measures contrast, names, roles, heading
order, tab order, target size, duplicate ids and live regions.

The script cannot see three things. It cannot see if a focus ring is visible against the
pixel behind it. It cannot see if the reading order agrees with the visual order. It
cannot hear a screen reader. A person must check those.

## Result

| Page | Fail | Warn |
|---|---|---|
| `index.html` | 1 | 1 |
| `browse.html` | 1 | 1 |
| `paths.html` | 0 | 1 |
| `resource.html` | 0 | 2 |
| `how-we-check.html` | 0 | 1 |

Three problems are real. The other warnings are correct behaviour, and the last section
says why.

## Problem 1 — the home page has no `h1`

`index.html` has no `h1` element. "Find what's worth your time." is styled with
`.display`, which is a class, not a heading.

A person who uses a screen reader usually presses `H` or `1` to go to the first heading.
On this page nothing happens. The page has a title in the tab and no heading in the
content. Every other page has exactly one `h1`.

Fix: make that line an `h1` and keep the `.display` class on it. The class carries the
type; the tag carries the meaning. Nothing moves on screen.

## Problem 2 — the "possibly outdated" flag fails AA

`--flag-outdated` is `--clay-deep`, `#c6613f`. It is 12 px text.

| Surface | Ratio | AA needs |
|---|---|---|
| card `#faf9f5` | 3.85 | 4.5 |
| canvas `#f0eee6` | 3.49 | 4.5 |

This is the only contrast failure on the whole site. Everything else passes, on all five
pages. It is unlucky that the one failure is a warning label, because a warning that is
hard to read does the opposite of its job.

Two candidate values. Both keep the hue and the saturation of the clay and only lower
the lightness, which is the same method the `--bark` note in `tokens.css` describes.

| Value | card | canvas | panel | feature |
|---|---|---|---|---|
| `#ac5233` | 4.97 | 4.51 | 3.78 | 4.16 |
| `#9a492e` | 5.92 | 5.37 | 4.51 | 4.96 |

`#ac5233` passes on the two surfaces the flag renders on today. `#9a492e` passes on all
four, so it stays correct if the flag is ever put on a panel or on the feature card.

`--clay` itself does not change. The filled button keeps its colour.

## Problem 3 — the mobile filter sheet does not hold the keyboard

The sheet is good in most ways. It has `role="dialog"`, `aria-modal="true"` and
`aria-label="Filters"`. Focus moves to Close when it opens. Focus goes back to the
Filters button when it closes. Escape closes it. The body stops scrolling.

One thing is missing. Nothing stops the Tab key from leaving the sheet.

Measured at 375 px with the sheet open: 403 focusable elements sit outside the sheet and
all of them still take focus. A person who presses Tab past "Show resources" lands on the
site header, then on the 353 cards behind the panel. The panel is `position: fixed` and
covers the screen, so the focus ring is under it and cannot be seen.

`aria-modal="true"` does not do this. It tells a screen reader to keep its virtual cursor
inside the dialog. It has no effect on the Tab key.

Fix: keep Tab inside the sheet while it is open. About twelve lines in
`assets/js/browse.js`, next to the Escape handler that is already there.

## What is already correct

These were tested and passed. They are listed because they are easy to break later.

- Contrast: every other text and background pair on all five pages meets AA.
- The result count announces. `aria-live="polite"` says "132 resources" when the search
  changes the number. This is the part that is most often missing, and it is here.
- One `main`, one `header`, one `nav`, one `footer` on every page.
- The skip link is the first focusable element and its target exists.
- Heading order never skips a level.
- Every link, button and form control has an accessible name.
- No positive `tabindex`. Tab order follows the DOM, and the DOM follows the screen.
- No duplicate ids, on any page, including the 353 generated cards.
- Every control is at least 44 px tall, so target size passes with room to spare.
- `prefers-reduced-motion` is honoured.
- The focus ring is `2px solid #141413` at 2 px offset, and the footer swaps it to ivory
  on the dark background. Both are far above the 3:1 that AA asks for.

## Warnings that are not problems

- **"No live region" on `index`, `paths`, `resource`, `how-we-check`.** Correct. Nothing
  on those pages changes a count. Only `browse` needs one, and it has one.
- **"Tab moves up the page" on `browse`.** This is the "More filters +" button moving to
  the search field. The two sit in different columns, so the tab order goes down the
  filter rail and then up to the top of the results column. This is the normal reading
  order for two columns. It is not a fault.
- **"Target under 24×24" on `resource`.** This is a link inside a sentence. WCAG 2.2
  excludes inline links from the target size rule, because the line height sets it.

## Not covered

- No screen reader was used. NVDA, JAWS and VoiceOver each behave differently, and only a
  person can say if the result sounds right.
- Colour was measured, not judged. Nothing was checked for people with colour vision
  deficiency, and nothing on the site uses colour alone to carry meaning, so the risk is
  low.
- Zoom to 400 % was not tested.
- Windows High Contrast Mode was not tested.
