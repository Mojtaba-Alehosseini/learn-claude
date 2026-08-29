# Path step card — the spec

The working sample is `docs/design/sample-path-card.html`. Open it. It loads the real
tokens and the real fonts, so what renders is what the site would render. Every rule below
is implemented there and was checked in a browser, not reasoned about.

Three ideas hold the whole thing together.

**1. The tint goes on the tile, never behind text.** `--bark` is 4.60:1 on the page canvas
and has no headroom left. Put it on a tint and it fails AA. Anthropic's own cards do the
same thing — colour on the image area, words on white. That is not a style choice, it is
the only version that passes.

**2. One click.** The whole card is pressable, and it points at *our* resource page, not
at the resource. Our page carries the `Skip if` line and the report link; sending someone
past those is the thing this site exists to prevent.

**3. Badge the exception, not the rule.** About 90% of the catalogue is free, so a "Free"
badge on nine cards in ten is decoration. A "Sign-up needed" badge on the tenth is
information.

## Layout

A two-column card: a 4:3 tile on the left at 200px, the text on the right.

```
┌─────────────────────────────────────────────────────────────┐
│  ┌───────────────────┐   Step 3 · Course              (→)   │
│  │            [time] │   Claude 101                          │
│  │      ✎  drawing   │   Anthropic Academy                   │
│  │                   │   ─────────────────────────────────   │
│  │ [AA]      [cost]  │   why this step sits here             │
│  └───────────────────┘   [Skimmed]  Checked 20 August 2026   │
└─────────────────────────────────────────────────────────────┘
```

**The tile has four fixed corners.** Every card puts the same thing in the same place, so
a reader scans a column instead of reading it:

| corner | holds | when |
|---|---|---|
| top right | time, `LC.TIME[item.time]` | always |
| bottom left | the publisher's own logo | only when we hold that logo |
| bottom right | cost, `LC.COST[item.cost]`, in `--clay-text` | only when not plain `free` |
| centre | the format drawing | always |

One chip language for all three: ivory ground, hairline, 12px, square. They are
self-contained, so whatever tint sits underneath cannot touch their contrast — which is
the reason the tint is allowed to exist at all.

Cost goes bottom right, not top left: at 200px the tile cannot hold "Sign-up needed" and
"one hour" on the same row. Verified — it collided.

**The list is capped at 880px.** At the full 1280px page width the card is 1250px wide,
the prose still stops at `--measure`, and the arrow ends up marooned 400px from the
nearest thing it relates to. 880 = 200 tile + 24 gap + ~600 text, and 600px is what 50ch
of 20px Tiempos measures. The card ends where the sentence ends.

**A hairline runs between cards**, centred on the tile. A path is an *order* and that is
the entire product; cards on their own read as a set. The Academy does not need this line
because its cards are not ordered. Ours are.

**`step.why` keeps its current weight.** Serif, full size, hairline above it — the same
treatment `Skip if` gets on a browse card. If it ends up reading as a caption, the card is
wrong and the page got worse.

## The publisher mark — the real logo or no badge

Initials were built and rejected. A lettered square is not a mark, it is an apology for
not having one, and it makes 129 publishers look like they share a house style they do not
share.

**Real means a file we hold.** Fetched once at build time into
`assets/icons/publishers/<slug>.png|svg`, committed, never requested at render. A favicon
service called per card would send the reader's browsing to a third party, and this site
promises not to do that. Local files also keep the page working from `file://`.

**Where the coverage is.** Measured over the 354 entries, 2026-08-28:

| mark | hosts it stands for | entries | running |
|---|---|---|---|
| YouTube | `youtube.com` | 72 | 20% |
| GitHub | `github.com` | 31 | 29% |
| Anthropic | `claude.com`, `support.claude.com`, `anthropic.com`, `anthropic.skilljar.com`, `code.claude.com`, `platform.claude.com`, `academy.claude.com` | 87 | **54%** |
| Coursera | `coursera.org` | 6 | 56% |
| Northeastern | `learning.northeastern.edu` | 6 | 57% |
| DataCamp, Medium, Udemy, LinkedIn | — | 15 | 61% |

Three files carry more than half the catalogue. Eight carry 61%. The remaining 121 hosts
get **no badge**, and the corner stays empty.

That asymmetry is correct, not a compromise. The publisher name is already set in text
under the title, so nothing is lost. The badge adds recognition where recognition exists
and stays quiet where it does not.

**Sourcing.** Prefer, in order: the publisher's own SVG mark, `apple-touch-icon` (usually
180px), then `favicon.ico`. A 16px favicon upscaled into a 28px badge looks broken — if
nothing above 32px exists for a publisher, drop that publisher from the list rather than
ship a blurred one.

Using a publisher's own icon to identify a link to that publisher is nominative use and
standard practice. Do not restyle, recolour or crop a mark.

**The mapping lives in one place** — a host-to-slug table beside the icons, so the seven
Anthropic hosts resolve to one file and a new host fails to a missing badge rather than to
a broken image.

## Motion

Emil Kowalski's rules, and the reasoning is in the sample's comments.

| what | value | why |
|---|---|---|
| easing | `--ease-card: cubic-bezier(0.23, 1, 0.32, 1)` | the built-ins are too weak. Scoped to this component — the project's global `--ease-out` also drives the filter rail, the icons and the mobile sheet, and moving those is a separate decision |
| hover | `translateY(-2px)` + `border-color`, 200ms | named properties, never `all` |
| press | `scale(0.995)`, 120ms | 0.97 on a 880px card reads as a glitch; the same figure on a 120px button reads as a press |
| tile drawing | `scale(1.04)` on hover, 260ms | the card is seen once, so decoration earns its place |
| arrow | `translateX(2px)` on hover | enough to register, not enough to notice |
| entry | stagger 40ms, `translateY(8px)` + fade, 320ms | six at 80ms takes half a second to finish, which is longer than the page takes to be useful |

Every hover is behind `@media (hover: hover) and (pointer: fine)` — touch devices fire
`:hover` on tap and the lift would stick after the press.

`prefers-reduced-motion` keeps the fade, because it aids comprehension, and drops every
movement. Reduced motion is fewer and gentler, not none.

## One click, done accessibly

The stretched-link pattern. The `<a>` stays on the title, so a screen reader announces one
link named by the title rather than a link named "card". An `::after` with `inset: 0`
spreads that link over the whole card.

Two things that pattern breaks and the sample fixes:

- **Focus** would ring the four words of the title, not the card.
  `.sp-card:has(a:focus-visible) { outline: var(--focus-ring) }`, with the inner ring
  suppressed.
- **The "Start with this" button** would sit under the overlay and stop working.
  `position: relative; z-index: 1`.

## On a phone

One column. The tile goes full width, so 4:3 would be a 256px slab on a 390px screen — it
becomes a 16:7 band, the drawing drops to 60px, and the hover arrow is removed because
nothing hovers on a phone.

## The tint — settled

**Three warm tints rotating by position**, in the sample. Decorative, and honest about it:
they break the wall, they do not encode anything.

Keyed to format was built and rejected. The palette is warm-only by rule (`tokens.css`
line 74) so seven distinct tints inside it do not exist — `docs` and `repo` landed three
hex points apart. Even at three, the last one had to be pushed yellower before steps 3 and
4 stopped looking identical, and that push is the evidence that three is the ceiling.

No sage, no lavender, no blue. Breaking our own palette rule to look like Anthropic is a
bad trade for a site whose footer says it is not affiliated with Anthropic.

The three values are hex written in one place, not tokens. Three colours used once do not
earn a name, and naming them invites their use somewhere the contrast has not been checked.

## The time wording — settled

Short. `LC.TIME` becomes:

| key | was | is |
|---|---|---|
| `under-15min` | 15 minutes | **15 min** |
| `under-1hr` | one hour | **1 hour** |
| `half-day` | a half day | **half a day** |
| `multi-day` | several days | **several days** |

One vocabulary, not a chip variant. `ui.js` says a label must never drift between two
screens, and a second time vocabulary is exactly that drift.

This changes the words in the Browse filter rail, on every card and in the path summary
line. **Look at all three** — a filter row reading "15 min" is fine, but check it against
its heading, and check that "half a day" still reads as a sentence where it is used as
one. Update `docs/design/ux-copy.md` in the same commit; if the copy deck and the code
disagree, the deck stops being worth reading.
