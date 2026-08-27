# Run log — the decisions and the seven, 2026-08-27

Follows `RUN-LOG.md`. Same format: one line per unit, what changed, what was left alone
and why. The "still open" list at the bottom of the previous log is worked through here.

| # | Unit | Commit | Changed | Left alone, and why |
|---|---|---|---|---|
| 1 | Clay | `b77cbcb` | how-we-check gets **Browse the N resources**; a single path gets **Start with this** on step 1 | The path index and Browse stay at zero. Rule restated in `design-brief.md` §4a as *at most one per page, and none where there is no single action* |
| 2 | Cost | `3369d9b` | 14 entries; definition written to `docs/specs/2026-08-27-what-cost-means.md` | The two claude-cookbooks repos stay `free-account`; Medium entries stay `free` |
| 3 | Time | `e3fc171` | 2 courses rounded up to `half-day` | "Teaching AI Fluency" stays `half-day` — see below |
| 4 | Placeholder check | `5bb1de1` | `PLACEHOLDER_OPENERS` + 4 tests, 30 checks | The check was **not** widened to heuristics |
| 5 | The syllabus | `236735c` | prerequisites settled, `time` corrected, price recorded, one of my own skip_if lines corrected | Neither contradictory field deleted; `level` left at `confident` and flagged |
| 6 | Publisher names | `a169b73` | 66 cards; 49 hosts mapped, 7 platforms added, reporting fixed | `prettify()` kept as the last resort; Medium *publications* stay mapped by name |
| 7 | The swept files | `3fe6b52` | `.gitignore` records the decision | History left alone; the files stay tracked |

## Unit 1 — clay

Measured rather than assumed, at 1440px, counting only what a reader can see. browse.html
already **had** a clay button — `#sheetConfirm` in the mobile filter sheet, `display:none`
above 768px — so the count was 2 of 5 on desktop and 3 of 5 on a phone.

The count on how-we-check is written by the same script that writes the tier tally, from
`window.LC.items().length`. That page's whole claim is that its numbers come from the
data; a hardcoded 351 in the call to action would have been the one line that rots.

Verified: how-we-check 1, `?id=first-week` 1 on step 1 of 6, `?id=pm-without-engineering`
1 on step 1 of 5, paths index 0, browse 0. No console errors.

## Unit 2 — cost

Fourteen entries, every one tested with an unauthenticated request and the ambiguous ones
opened in a browser.

Eleven moved to `free`. Two were mislabelled inside the paid values. **One moved the
other way** — *Head of Claude Code: What happens after coding is solved* read `free` and
is behind a Substack paywall. The rule is a question, not a licence to relabel.

Five stayed `subscription` after checking: Sachin Rekhi, Lenny's *Everyone should be
using Claude Code more*, Department of Product, Product Compass, Every's *Claude Code for
Product Managers*. Two neighbours on those same hosts are **not** gated. Per-article,
never per-host — which is how both wrong readings got in.

**Surprise.** WebFetch reported Every's paywalled essay as "completely readable". A
browser showed the gate and 6,010 characters. Raw fetch and browser disagree, exactly as
the runner and the laptop did over education.gov.au. Every ambiguous case in this unit
was therefore re-checked in the browser, and that is written into the spec.

## Unit 3 — time

Two 90-minute courses moved up. The real figure now ships in `skip_if`, because `notes`
was taken out of the browser mirror in an earlier round and a duration recorded there is
invisible.

**One case deliberately not moved.** "Teaching AI Fluency" is `half-day` and its notes
say five to six hours. Rounding up means `multi-day`, which renders as "several days".
Six hours is not several days: that overstates by four or five times where `half-day`
understates by two. **Rounding up is the safer error only while it stays smaller than the
error it replaces.** The real figure went into `skip_if` instead.

Checked in both directions — nothing states a duration below its bucket's floor.

## Unit 4 — the placeholder that got through

Reported last run as "`N/A` passes the placeholder check". Right about the symptom, wrong
about the cause, and the difference decided the fix: **`n/a` was already in
`PLACEHOLDERS`.** The match was on the whole string, so a placeholder with an excuse
after it was no longer equal to it. Adding more words to that set would never have caught
it.

So: a second, smaller set of forms that cannot begin a real sentence — `n/a`, `n\a`,
`n.a.`, `na`, `nil`, `tbd`, `todo`, `not applicable` — and a line that *opens* with one
fails whatever follows.

`none`, `everyone`, `anyone`, `unknown`, `unclear`, `nobody` are deliberately excluded.
*"None of the examples are in Python"* is a good skip_if. Two of the four new tests exist
to hold that line: they assert those must **pass**.

## Unit 5 — the syllabus

The contradiction is the seminar's own and both of our fields were copied faithfully. Its
page carries two sections that disagree:

- *Who Should Register?* — "you don't need any prior experience with AI tools or programming"
- *Computing* — "You should be comfortable with basic LLM prompting … and have a working knowledge of at least one statistical computing language (e.g., Python or R)"

`prerequisites` follows *Computing*: it is the operative section and the stricter one.
Neither is deleted, because deleting one hides that the seller has not decided.

Reading the page also found four unrecorded things and **one error of my own**:

| | |
|---|---|
| `time` | `half-day` → `multi-day`. Four days on Zoom, ~14 hours |
| price | $995 USD, never recorded |
| second cost | needs Claude Pro or Team on top; free tier "not recommended" |
| recordings | within 24 hours, kept four weeks |

That last one contradicts the `skip_if` I wrote for this entry last week — *"it happens
when it happens, not when you have a free evening."* Wrong. It is scheduled, but missing
it is not fatal, and calling a course unusable when it is merely inconvenient is the same
class of error this whole exercise has been removing.

## Unit 6 — publisher names

Logged as "60 hosts have no mapping". The count understated it: **66 cards** were naming a
domain fragment, and four were naming the wrong organisation — `Libguides` on two
different university libraries, `Codes` for vincent.codes.finance, `Apple` for a Dive Club
episode. `Substack` was the publisher on 11 cards and `Medium` on 4.

Every one of those entries already recorded a real `author`. The truth was in the data.

Fixed with mechanisms already in the file: 49 hosts mapped by name, 7 hosts added to
`PLATFORMS` (the branch YouTube has always used). A Medium *publication* is not on that
list — UX Collective and Design Systems Collective have their own editors. The test is
whether the host chooses what appears on it.

Two reporting faults fixed, both of which hid the problem:

- the unmapped count included hosts the platform branch handles correctly, and printed a
  name no reader would ever see;
- when the script overwrote a hand-written source with a guess it said nothing but a
  total. **That is how "Product Impact" became "Productimpactpod".** It now names the
  host, both names and the title, every run.

0 hosts now fall through to `prettify()`.

## Not built, and why

**A check for a row whose URL is a listing or search page.** Measured first: a
URL-shape heuristic (`/topics/`, `/tag/`, `/search`, `/browse`, `/collections/`, `?q=`)
flags 2 of 351, and both were opened and are legitimate — ICMJE's recommendations use
`/browse/` in their path structure, and GOV.UK's DfE *collection* is a real curated
resource with its own publication and update dates.

More to the point, it tests the wrong thing. The LinkedIn row's fault was not its URL
shape — it was that the card described a specific 21-minute course and the destination
was a search page. A prettier URL would have slipped past this check, and a check that
fires only false positives gets switched off, taking the real catch with it. Same
argument as excluding "none" from the placeholder openers.

## Still open

1. **`level` on "Academic Research with Claude"** is `confident`; the page's stated entry
   bar is basic prompting. Recorded in its notes rather than changed on a hunch.
2. **Designer cannot support a path.** Left as instructed — the three things that would
   change it are named in `docs/specs/2026-08-27-designer-and-data-analyst.md`.
3. **The email address on the report route.** Still parked.
4. **A data-analyst path.** It can support one now. Next conversation.
