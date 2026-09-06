# Attack 3 — the mechanical fixes, one at a time

Every change in the round's single mechanical commit, what it was, and what was verified
afterwards. Nothing here contains a judgement call; the things that do are in
[SUMMARY.md §9b](SUMMARY.md).

---

## M1 — `browse.html?role=X&checked=reviewed` denied the site serves the role

**Found by:** the business owner and the PM independently; reproduced on `developer`.

**What a reader saw**, live, on `?role=business-founder&checked=reviewed`:

> 0 resources for running a business
> **We have not covered this role yet.** It's on the list. Browse everything instead.

The business owner has 153 resources. The PM has 112.

**Cause.** `browse.js`'s `anyOtherThanRole()` tested levels, times, topics, formats, costs
and officials — not `tiers`. D10 added the tier axis and nothing told the function that
reasons about axes, so a role plus the tier filter looked like a role on its own. Nothing
anywhere is `reviewed`, so that filter empties every role, and the message blamed the
filter that was **set** rather than the one that **emptied the result**.

**Change.** `sel.tiers.length` added to the test, with a comment naming the next person's
obligation: an axis added is an axis added here.

**Verified.** The same URL now falls through to "Nothing matches all of those", which is
what an unfiltered-by-role empty result already said.

---

## M2 — "Newest first" was not newest first

**Found by:** six of ten agents, independently, in five different roles.

**What a reader saw.** On `role=researcher&level=never-used`, the two cards the site itself
flags *"over a year ago, may not match Claude today"* ranked first and second, and a card
marked `Updated 1 Sep 2026` ranked last of sixteen. On `role=teacher`, the most recently
updated card in the catalogue landed at 62 of 67.

**Cause.** `ui.js` built `sortDate` from `published` alone. A card can show two dates and
the sort read one of them, so an `Updated` line counted for nothing.

**Change.** `sortDate` is now the later of `published` and `updated`, each ignored when
`UNVERIFIED`. Undated rows still sort last, which is unchanged behaviour and not a
judgement this commit makes.

**Not a blanket sort bug.** Three agents noted independently that "Shortest first" is
correct. The machinery worked; one label lied.

---

## M3 — path steps threw away the `Updated` date

**Found by:** the analyst.

**What a reader saw.** A path step reading "Published 24 Oct 2024" for a row that reads
"Published 24 Oct 2024 · Updated 21 Jun 2026" on Browse and on its own page.

**Cause.** `paths.js` computes `LC.freshness(it)` and renders `fresh.checked` and
`fresh.note`, never `fresh.updatedNote`. **This is Attack 2's M1 on a third surface.** That
round found the resource page dropping the Updated date and fixed it there; the same bug sat
untouched on paths for two more rounds.

**Change.** `fresh.updatedNote` rendered, in the same position as the other two surfaces.

**Why it mattered most here.** A path is the one surface built for a reader who cannot yet
judge a resource themselves, so it was the worst place to hide the freshest date the site
holds.

---

## M4 — a pick reason quoted a sentence its card does not contain

**Found by:** the PM.

**What a reader saw**, on `pm|builder`, recommending a $3,000 course:

> …and its own card is straight that thirteen reviews is thin evidence…

The words "thirteen", "13" and "review" appear nowhere on that card. Its actual objection is
*"a sales page built on testimonials, hiring screenshots and countdown urgency"*.

**Change.** The clause now says what the card says. Nothing was added to compensate.

**The class, not the instance.** Attack 2's M13 removed three reasons that called Anthropic
material non-Anthropic and added a validator for that claim. This is the same family — a
reason asserting something its own card does not say — and the validator does not cover it.
Recorded in [REGRESSION.md §3.2](REGRESSION.md); a check for the general case is not in this
commit because it is not obvious what it would test.

---

## M5 — pick reasons printed the build's own vocabulary

**Found by:** the student, who quoted one back.

**What a reader saw**, on the first pick at `student|confident`:

> Held back on 2026-09-04 only because it is step 1 of the research path and would have
> displaced something no path carries. **Rule B removed that something from this pool on
> 2026-09-06, so the objection lapsed and the verification slot was empty** — and this is
> the only candidate here anybody has read in full.

A second reason, at `non-technical|confident`, carried a dated build note added by FIX-31.

**Cause.** Pick reasons are written during rounds and `browse.js:392` renders
`picks[].reason` verbatim on the card. Runners-up are never rendered, so the leak is exactly
these two.

**Change.** Both rewritten to say the same thing in a reader's language. No argument was
dropped; the machinery was.

---

## M6 — `pupil` returned nothing, and the fix exposed a second fault

**Found by:** the teacher.

**What a reader saw.** *"is it safe to put pupil names into Claude"* returned two
small-business courses and a GitHub Action, with the correct card — *Claude for Teachers:
your data and our terms* — at **15 of 20**. Swapping one word, `student` for `pupil`, put it
**3rd**. `pupil` alone returned **0 of 588**.

**Change 1, the data.** A synonym row: student / students / pupil / pupils / learner /
learners, with the teacher's measurement as its reason. British schools say pupil.

**Change 2, the mechanism, and this is the part worth reading.** The row did nothing. The
index builder's synonym flattener dropped any term the index had never seen — including as a
*key*. `pupil` appears nowhere in the catalogue, **which is the entire reason to have the
row**, so the flattener refused it a key and the new row expanded nothing.

The rule was right about targets and wrong about keys: expanding *to* a word with no
postings is wasted work; expanding *from* one is the whole point. `load_synonyms` now keeps
every term as a key and filters only the targets. `validate-synonyms.py` still refuses a row
unless two of its terms are in the index, so every key reaches something.

**Verified, and honestly.** `pupil` alone goes from **0 results to 42**, with the right
teacher card second. Inside the teacher's original sentence the correct card moves from
**15th to 12th** — better, and not fixed. A synonym scores at half weight and cannot beat
rows holding the reader's other words literally. That ceiling is **spec amendment 7**,
written down last round before this round found a second instance of it, and it is not
tuned here: moving a weight to rescue one query is how a search stops being measurable.

---

## Two things the agents reported that this commit deliberately did not change

**The attract loop.** Eight agents saw the role chips cycle while the headline stayed
`I'm a [role] and I've [level].` and read it as a bug. `home.js` says what it is for:
*"Before anyone has chosen, the drawing cycles slowly. It is the only hint that the
underlined words are buttons."* It cycles the **drawing**, and it does that correctly.
Whether the sentence should preview a role too is a design decision, not a defect.

**The heading order.** The designer reported the `<h1>` as a 16px caption beside a 68px
`<p>`. Both elements exist, the `<h1>` is first in the document, and which one carries the
visual weight is a typographic decision. Moved to [SUMMARY.md §9b](SUMMARY.md).

Reading the source before editing it is what kept both of these out of this commit.
