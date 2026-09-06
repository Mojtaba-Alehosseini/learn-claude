# Regression sweep — does the earlier work still hold?

FIX-32: *"Re-test every one rated high and every decision that was built: finding, fixed
in, still fixed today. Add Attack 1's five policy findings that Attack 2 said were
undecided — they are decided now; confirm the site agrees."*

Method: source and data checks are shown as the file and line that carries the fix; the two
that can only be seen in a browser were reproduced on the live site and are marked **live**.
Nothing here is inferred from a commit message.

---

## 1. Attack 2's mechanical list — all thirteen

| # | What it was | Fixed in | Still fixed |
|---|---|---|---|
| M1 | The detail page dropped the `Updated` date and the staleness note | `resource.js` | **yes** — `updatedNote` rendered |
| M2 | `status: "outdated"` set and never rendered | `resource.js` | **yes** |
| M3 | "about 81 minutes" | `build-paths.py` | **yes** — sub-90-minute rounding present |
| M4 | "98 read by ai" — a tier label lowercased in the trust sentence | `how-we-check.html` | **yes** — no `toLowerCase` remains |
| M5 | The skip link scrolled but moved no focus | all five pages | **yes** — `tabindex="-1"` on `<main>` in all five |
| M6 | "Back to browse" threw the reader's filters away | `resource.js` | **yes** — reads the referrer |
| M7 | The 0-result dead end had no clickable way out | `browse.js` | **yes** |
| M8 | "Try fewer words" advised to someone who typed one | `browse.js` | **yes** — gated on word count |
| M9 | "Browse 1 Claude resources" | `browse.js` | **yes** |
| M10 | The path pill was a `<span>` on the card, a link on the page | `ui.js` | **yes** |
| M11 | `Skip if:` repeated its own label on 157 cards | `data/items.json` | **yes** — **zero** rows still do |
| M12 | `sitemap.xml` listed a third of the catalogue and 35 dead ids | `build-sitemap.py` | **yes** — generated every build |
| M13 | Pick reasons called Anthropic material non-Anthropic | `picks.json` + `validate-picks.py` | **yes for that claim — see §3.2** |

**Thirteen of thirteen hold.** One of them, M1, turns out to have been fixed on one surface
of three — see §3.1.

---

## 2. Attack 2's top ten, and the decisions that were built

| Attack 2 finding | Decision | Built in | Where it stands after Attack 3 |
|---|---|---|---|
| 1. Unread tiers carry full verdicts | D1 | FIX-24 | **Holds.** Exactly three rows are `listed`, each stripped to a title, a link and the fixed line *"You want something we have read. We have not opened this one."* `validate-catalogue.py` refuses a `listed` row that carries a summary, `who_for`, `teaches` or `questions`, and `test-gates.py` plants that fault and watches the build go red. |
| 2. Three trust claims the data refutes | D2 | FIX-24 | **Holds.** `test-copy-claims.py` bans each killed sentence by substring across every reader-facing file and runs in the build. |
| 3. Search fails plain-English questions | D3 | FIX-27 → FIX-31 | **Improved, not fixed, and Attack 3 says so in ten voices.** The measured suite rose across four rounds; seven of ten agents still got two different shelves for one intent. See SUMMARY §2.1. |
| 4. Answering the top level honestly returns nothing | D4 | FIX-25 | **Holds, with a new fault.** The thin-cell offer exists and works. Accepting it **removes the picks block**, because a second level is a second filter and the block only shows at exactly one role and one level. (non-technical §10.11) |
| 5. The detail page drops the Updated date | M1 | FIX-24 | **Holds on the resource page; never applied to paths.** §3.1 |
| 6. The role filter returns other people's jobs | Rule B | FIX-25/26/28/29 | **Much improved.** The designer measured 45 of 48 cards correct and called the rule sound. The non-coder found 6 of 134 wrong; the PM found tags surviving on cards whose own text denies them; the writer found the site's best writer card **not tagged for a writer**. The rule works; its edges are still sharp. |
| 7. The staleness warning replaced the date | D6 | FIX-24 | **Holds.** `LC.freshness` returns the date and the note as separate fields and both render. |
| 8. Pick reasons call Anthropic material non-Anthropic | M13 | FIX-24 | **Holds for that claim, and a sibling shipped.** §3.2 |
| 9. 24–30 tabs to the first result; the skip link moved no focus | M5 | FIX-24 | **Holds.** |
| 10. Picks vanish on any search or third filter, silently | decision 8 | **not built** | **Still true, and sharper**: the site's own thin-level offer now triggers it. |
| — | D9, price is a field | FIX-28 | **Built, and invisible.** Four rows carry a price because the rule stores one only where the page prints the same number for every reader. Eight of ten agents hit the symptom; none could discover the rule. |
| — | D10, "how well checked" as a filter | FIX-24 | **Built, and it broke something.** §3.3 |
| — | D11, the badge's meaning without a mouse | FIX-24 | **Built with a documented trade, and Attack 3 measured the cost.** The card keeps one focus stop and carries the meaning in `aria-describedby`; the resource page has a real link. A sighted phone reader still gets nothing, and seven agents said so. |
| — | D13, the site names its "we" | FIX-28 | **Built, and the agents split on it.** SUMMARY §6. |
| — | D15, a publisher name is a gate | FIX-26 | **Holds.** `validate-catalogue.py` imports `add-source.py`'s own mapping rather than copying it, so the gate cannot drift from the fixer. |
| — | Rules A, B, C | FIX-25/26 | **Hold.** `builder` means building — the developer confirmed the level is genuinely advanced. The collection cards exist; no agent tripped over one, and the writer found the gap they leave: there is no Marketing card, which is why loose marketing recipes sit on the writer's shelf. |

---

## 3. What the sweep found that a tick-box would have missed

### 3.1 M1 was fixed on one surface of three

`resource.js` renders `fresh.updatedNote`. `paths.js` computes `LC.freshness(it)` on every
step and renders `fresh.checked` and `fresh.note` — **never `fresh.updatedNote`**. The same
bug, the same shape, on the surface built for readers who cannot yet judge a resource.

A fix verified on the page where the bug was reported is not a fix verified everywhere the
bug can live. That is the lesson, and it is why this file exists.

### 3.2 M13's validator catches one sentence and not its sibling

M13 removed three pick reasons that called Anthropic material non-Anthropic, and added a
check so a fourth could not ship. Attack 3 found a fifth of the same family:
`pm|builder` recommends a course partly because *"its own card is straight that thirteen
reviews is thin evidence"*, and the card says nothing of the kind — its actual objection is
*"a sales page built on testimonials, hiring screenshots and countdown urgency"*.

The class is *a pick reason asserting something its own card does not say*.
`validate-picks.py` guards one member of it.

### 3.3 D10 built the tier filter and left a guard behind

`browse.js`'s `anyOtherThanRole()` tests levels, times, topics, formats, costs and
officials. It does not test **tiers**. So a role plus the tier filter falls through to
*"We have not covered this role yet"*, which is false for all ten roles.

**live**, `?role=business-founder&checked=reviewed`:

> 0 resources for running a business
> **We have not covered this role yet.** It's on the list. Browse everything instead.

The axis was added and the guard that reasons about axes was not told. Every regression
sweep should ask, of every new filter: what else reasons about the set of filters?

---

## 4. Attack 1's five policy findings — decided now, and the site checked against them

Attack 2 recorded these as open. Each is now settled; this confirms the site agrees.

| # | Attack 1 finding | Where it stands |
|---|---|---|
| 1 | **The search box collapse.** Two agents called it a defect; it was a deliberate call. | **Kept, and re-hit.** The designer found the same behaviour from the other end: clicking the large underlined `a [role]` collapses the chooser and hides the page. Same mechanism, same call, fresh evidence. Still Morteza's. |
| 2 | **Whether `Skip if:` should dominate the card.** | **Kept, and vindicated.** `Skip if:` is now the single most-praised thing on the site: every role that answered the closing question named it, and the business owner would return for it "and nothing else". The stylesheet's intent was right. |
| 3 | **The named-individual allegation.** | **Gone.** No card in the catalogue now carries an allegation about a named individual. Checked by reading every `summary`, `who_for` and `skip_if` for accusation language; the only matches are subject matter — a university explaining why it disabled Turnitin, a journalist's rules against fabricated quotes. |
| 4 | **Whether ten roles is too many.** | **Kept at ten, and the cost is now visible.** Attack 1 predicted thin roles would be filled by relabelling other roles' content. Attack 3 measured it: 13 of 24 cards at the writer's own level are marketing and fundraising recipes; 7 of 12 at the analyst's top level are GitHub repos. The roles were kept; the borrowing is real. |
| 5 | **Whether "a writer" should be split from "a marketer".** | **Kept as one, and Attack 3 is the strongest case yet for splitting.** The writer's shelf at their own level is mostly the marketer's work, and the missing sixth collection card is Marketing. Still Morteza's. |

---

## 5. What this sweep says about sweeps

Three of the four things it found are the same shape: **a fix that was verified where the
bug was reported and nowhere else.** M1 on one surface of three, M13 on one sentence of a
family, D10's new axis and the guard that reasons about axes.

None of those would have been caught by re-testing the original finding, because the
original finding is genuinely fixed in all three cases. They were caught by asking *where
else does this live*, which is a different question and belongs in the next sweep's method.
