# Design debug — four parallel audits, 2026-08-24

Four agents ran at once, ~15 minutes: token conformance (static), JS/CSS timing sync
(static), edge cases (browser, localhost:8000), visual review (browser, live site,
desktop + mobile). Findings only — nothing was changed. Every claim below carries its
source and, where it exists, the file:line.

One measurement caveat: the visual agent's pane composites emulated viewports scaled,
so its *numbers* come from JS inside a correctly emulated 1280px/375px viewport and are
accurate; its 1:1 eyeballing was done at 390px.

## What is clean, verified

- **Colours: fully token-clean.** No hex, rgb(), or named colour outside `tokens.css`
  in any shipped css/html/js. No box-shadow, no gradient, anywhere.
- **Injection-safe.** `resource.html?id=<script>…`, `browse.html?q=<img onerror=…>`:
  rendered escaped, no element created, zero console errors. Unknown ids and unknown
  filter values produce honest empty states with working escape routes.
- **Icons: 47/47 live.** All 40 role/level PNGs and all 7 format icons return 200 with
  real payloads. (Format icons are named `<format>-alpha.png` — `ui.js:167`.)
- **Font sizes token-true everywhere.** 20px desktop / 18px mobile on every page, both
  from the tokens. Focus ring is the authored `2px solid` slate on `:focus-visible`.
- **The one timing pair the rule was written for is correct.** `FADE_MS` 220 ==
  `--dur-base` 220ms. No horizontal overflow on any page in normal states. The
  role-then-level fast-click race was traced end to end: settles correctly, no stuck
  opacity, no double fade.

## Bugs — mechanical fixes, no design judgment needed

1. **Browse mobile: the footer's last line can never be read.** `.mobile-filter-bar`
   is fixed, 69px tall, and nothing pads the page bottom, so at max scroll the fixed
   bar covers the final 21px of `.footer-note` — the disclaimer is sliced
   mid-sentence, permanently. Fix: bottom padding equal to the bar height inside the
   mobile media block. *(visual audit)*

2. **A long unbroken search term gives the whole page a horizontal scrollbar.**
   `"x"×300` in the browse search → the no-match message paints 4,673px wide
   (viewport 1,536). `.empty .prose`/`<strong>` has no `overflow-wrap`. Realistic
   trigger: pasting a URL into search. Fix: `overflow-wrap: anywhere` on `.empty`.
   *(edge-case audit)*

3. **"Copy link" timer is never cleared.** `resource.js:100-104`: click Copy twice
   ~1.5s apart and the first timer snaps the second "Copied" back early. And the
   clipboard-refused branch sets "Press Ctrl+C" with no timer — permanent for the
   life of the page. *(timing audit)*

4. **Reduced motion still pays the full 220ms.** CSS durations go to ~0 under
   `prefers-reduced-motion`, but `FADE_MS` stays 220, so the drawing (and the chip
   mark) trail input by up to 220ms as hard cuts — for exactly the users who asked
   for instant. Nothing breaks; it is safe, not correct. Fix: set `FADE_MS` to 0 when
   the media query matches. *(timing audit)*

5. **The chip highlight does not actually fade on the click path.** `render()`
   replaces both chip rows via `innerHTML` in the same tick as the mark, so the first
   style resolution already sees the final background — the 220ms fade the CSS
   comment promises only runs on hover, where `render()` is not called. Mostly
   invisible today (a clicked chip goes pressed-black, which wins), but the promise
   in `site.css:306-313` is false as written. *(timing audit)*

6. **Mobile footer links are 140×25px.** The site's own rule (`site.css:46`) is 44px
   minimum for every control. *(visual audit, noticed outside brief)*

## Latent — cheap to close, nothing exploits them today

- **`LC.esc` does not escape apostrophes** (`ui.js`), and `ui.js:167` interpolates a
  value inside a single-quoted `url('…')` in a style attribute. All data is curated,
  so nothing hits it; the escaper is still the wrong one for that context.
- **Browse re-renders everything on every keystroke**: ~350 items re-filtered, both
  filter panels rebuilt, every card rebuilt, `history.replaceState` per keystroke
  (Safari throttles at ~100/30s), and the `aria-live` count rewritten at typing
  speed. With the mobile sheet open, the rebuild drops focus to `<body>` until the
  next Tab. A ~150ms debounce fixes all four at once.
- **The art swap has no load gate** (`home.js:49-51`): on a cold cache the incoming
  `<img>` is raised to opacity 1 before the PNG has arrived. ~1MB across 40 drawings,
  only the fonts are preloaded.
- **`--dur-slow` (550ms) is declared, zeroed under reduced motion, and used nowhere.**
- The Persian no-match quote renders inside an LTR run — cosmetic; `dir="auto"` on
  the `<strong>` would fix it.

## Design decisions — yours, not mine

- **Three pages have zero clay.** The rule says clay appears once per page on one
  filled button. Browse (desktop) has none — its only `btn-primary` lives inside the
  closed mobile sheet. Paths and how-we-check have none at all, not even hidden. The
  "never twice" half of the rule holds everywhere; the "exactly once" half fails on
  3 of 5 pages. Each needs you to pick the one action that deserves it.
- **The desktop measure breaches your own ceiling on three pages.** The 816px column
  at 20px pushes the longest lines to 90.0 (paths), 90.5 (how-we-check), 92.7
  (browse card) cpl. Home and resource sit at 42–58. You measured 72 last time and
  kept it; these three are past 90.
- **Mobile measure is 30–42 cpl everywhere** — under the 45 floor on all five pages,
  worst on paths (30 cpl at a 287px measure; the step rail eats 88px). Largely
  inherent to 375px at 18px serif; narrowing the step rail is the one real lever.
- **Off-scale literals in site.css.** The spacing scale says "4px base, nothing
  outside this scale", but `.badge`/`.chip`/`.card-path` pad with 3px and 10px, one
  `11px` font-size exists (`site.css:424`) below the smallest type token, and ~15
  layout widths (264px grid rail, 56px step column, 27px rule offset…) are
  untokenised. Fixing is mechanical and visually identical only if we tokenise the
  current values as they are — deciding whether 3px/10px/11px *should exist* is a
  design call.

## Not bugs, so nothing to do

- Hero art "blank frames" in screenshots: pane compositing lag during the crossfade —
  21 sampled frames all had one image at opacity 1.
- The `.flag-outdated` colour repeating per outdated card: documented token choice.
- 353 cards render with no pagination (130k–180k px document): works, scrolls, and
  filtering is the intended navigation. Noted, not flagged.
