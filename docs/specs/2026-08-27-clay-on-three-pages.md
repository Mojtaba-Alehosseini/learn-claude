# The three pages with no clay

**Status: SUPERSEDED — the proposal was accepted and built on 2026-08-27, commit
`b77cbcb`. The live rule is section 4a of `docs/design/design-brief.md`; this file stays
as the record of what was proposed and why.**

Two things below are wrong and are left uncorrected, because a proposal edited after the
fact stops being a record. The single-path URL is `paths.html?id=…`, not `?p=…`. And the
catalogue held 347 resources the day this was written; the call to action that shipped
reads the count from the data and never hardcodes it.

---

**Originally: a proposal. Nothing was changed.** The design brief says one clay element per
page, and three of five pages have none, so the rule fails on the "exactly" half. This is
a design decision and it belongs to Morteza. Written 2026-08-27.

## Which three, measured rather than assumed

Checked in Chrome at 1440px, counting elements that are actually visible:

| Page | Visible clay | Where the clay is |
|---|---|---|
| index.html | 1 | the **Show me** submit, plus the clay underline on the two blanks |
| resource.html | 1 | the outward link to the resource itself |
| browse.html | **0** | `#sheetConfirm` is clay but lives in the mobile filter sheet, `display:none` above 768px |
| paths.html | **0** | — |
| how-we-check.html | **0** | — |

browse.html is the interesting one: it has a clay button in the markup and a reader on a
desktop never sees it. So the count is 2 of 5 on desktop and 3 of 5 on a phone.

## What the natural single action is on each

**browse.html — none, and that is the honest answer.** Browse is a filtering surface.
Every control on it is a filter, and a filter is not an action, it is a continuous
adjustment. The one thing a reader does after filtering is open a card, and the cards are
already the whole page — painting one of 347 cards clay would be a lie about which one
matters. The nearest real candidate is **Clear all filters**, which appears when filters
are on. That is a destructive action, and clay on this site means *go*, not *undo*.

**paths.html — "Start this path", on a path card.** This is the strongest of the three.
A path is a sequence with a first step, so there genuinely is one thing to press, and
right now the page offers five equal-weight cards and no verb. But there are five paths,
so a single clay button on the index would have to sit somewhere other than the cards —
the rule is one per page, not one per card. On the single-path view (`paths.html?p=…`)
the case is cleaner still: one path, one first step, one button.

**how-we-check.html — "Browse the 347", at the end.** The page argues for the method and
then stops. A reader who accepts the argument has nowhere to go. This is the classic
place for a single call to action and there is exactly one sensible destination.

## What I would do

**Add clay to two of the three, not all three, and not the same way.**

1. **how-we-check.html — yes.** One clay link at the foot: *Browse the 347*. It is the
   only page on the site that ends in a full stop and asks nothing. Lowest risk, clearest
   gain, and it does not compete with anything else on the page.

2. **paths.html?p=… — yes, on the single-path view only.** One clay button on step 1:
   *Start with this*. On the path **index** the honest answer is no clay, because the
   page's job is to help you choose between five, and colouring one of them is an
   argument the page is not making.

3. **browse.html — no.** Leave it. Two changes are worth making here instead, and neither
   is clay: the desktop reader should not be the only one who never sees the site's accent
   colour, and `#sheetConfirm` being clay-but-invisible above 768px means the rule as
   written is already being satisfied on paper and failed in practice.

If the rule is to survive, it probably needs restating as **at most one per page, and
zero where there is no single action** — which is what the site already does, honestly,
on browse.html. "Exactly one" forces a button onto a page that does not want one, and a
manufactured call to action is a worse fault than a missing accent colour.

## What this would cost

Small. Two elements, both `.btn-primary`, both already styled. No new tokens, no new
rules. The wording is the only thing that needs deciding, and the two suggestions above
are placeholders, not proposals.
