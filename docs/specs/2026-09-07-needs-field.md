# `needs` — what a thing needs is not what it costs

**`cost` is what it costs to consume this resource. `needs` is what you must already have
before it is any use to you.**

That is the whole rule. The 2026-08-27 cost spec settled the first half and sent the
second half to `skip_if`, where a reader finds it only after opening the card. Attack 3, on
6 September 2026, found sixteen cards saying `free` while needing a paid data
subscription, and one saying `free` four lines above "Before this — Paid Claude plan". The chip was not lying.
It was answering a different question than the reader asked.

## The field

`needs` is an optional array on a catalogue row. Empty or absent means "nothing beyond
opening the link". Values come from a closed vocabulary:

| value | means | rendered |
|---|---|---|
| `paid-claude-plan` | Pro, Max, Team or Enterprise — any paid Claude plan | yes |
| `mac` | macOS only | yes |
| `windows` | Windows only | yes |
| `data-subscription:<name>` | a paid data service — `lseg`, `daloopa`, `databricks`… | yes |
| `connector:<name>` | a connector must be enabled — `google-drive`, `figma`, `zotero`… | no |
| `github-account` | a GitHub account to read or run it | no |
| `api-key` | an Anthropic API key | no |

`<name>` is a lowercase slug: letters, digits, hyphens. The validator rejects anything
else, and anything outside this table.

**Adding to the vocabulary** is a copy-deck change: the entry goes in
`docs/design/ux-copy.md` under *Needs labels* with the reason it exists, before it is
used. A value with no reason in the deck is rejected by the validator, because the deck is
what the validator reads.

## Where the value comes from

**The page, not the card.** A row gets `needs` by opening its URL and reading what the
page itself requires. The card's own words — `skip_if`, `prerequisites` — are the
shortlist, not the evidence. Where the page and the card disagree, the page wins and the
disagreement is logged.

**The first pass, in this order:** rows whose card already carries `prerequisites`; rows
tagged `data-analyst`; `confident` and `builder` rows mentioning Cowork, a connector or a
plan. Within each group, rows whose own words name something *rendered* — a paid plan, a
platform, a data subscription — come first, because those are the rows the chip exists
for. **Checkpoint at 40 rows**, set on 21 September 2026: the round record shows, per row,
what the page said, what the card said, and what was recorded. **The pass stops early** if page and card disagree on more than three rows (21 September
2026, with the checkpoint). That is the signal the cards cannot be trusted as
a shortlist, and the method needs re-ruling before the other rows are touched.

## The chip

Rendered beside the cost chip, never instead of it, and only when `needs` holds something
rendered (the table above). Labels, from the copy deck:

| value | chip |
|---|---|
| `paid-claude-plan` | needs a paid Claude plan |
| `mac` | Mac only |
| `windows` | Windows only |
| `data-subscription:<name>` | needs a `<Name>` subscription |

"Free · needs a paid Claude plan" is the honest card. One chip per row: where several
rendered values apply, the paid plan wins, then the data subscription, then the platform —
a card row holds one more chip, not three, and the resource page lists them all.

`connector:*`, `github-account` and `api-key` are recorded and shown on the resource page
under "Before this", not as a chip: a connector is free to enable, a GitHub account is
free, and an API key is a developer's own arrangement. They are recorded now so the data
exists when a ruling wants them shown.

## Where it is defined for a reader

`how-we-check.html`, beside the price rule, in two sentences: the cost chip is what it
costs you to open and consume the resource; the needs chip is what you must already have
for it to be any use — a paid plan, a Mac, a data subscription. Both chips point there.

## Not in this round

- `needs` is not a filter. If Attack 4 asks for one, it earns one.
- No re-derivation of `cost` from `needs`. The two fields answer two questions.
- Rows outside the first 40 wait for the checkpoint to be read.

## Verification

- `validate-catalogue.py` rejects an unknown `needs` value and a malformed slug;
  `test-validate-catalogue.py` plants both.
- The card for a row with `needs: ["paid-claude-plan"]` renders the chip after the cost
  chip; a row with only `connector:figma` renders no extra chip. Checked in the browser
  on the built site.
- The checkpoint table in `docs/attack/FIX-34.md` holds, for the pass of 21 September
  2026, 40 rows with page evidence.
