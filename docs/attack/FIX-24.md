# Fix prompt — Attack 2 rulings, part 1: trust

Paste everything below the line into Claude Code, in the project folder.

---

Push the eight commits first. The attack is not real until it is on `master`.

Then read this whole file before touching anything. Fifteen decisions came back from
Attack 2. Every one is ruled on below, with the reason. Seven are done this round —
the ones about whether the site tells the truth. Eight are recorded now and built next
round — the ones about whether the site works well. Do not start the second list.

# Rulings done this round

**D1 — An unread item may not carry a verdict. Verify, re-tier, or strip.**
The 36 `listed` items carry prose that could only come from reading. So for each one the
tier is the lie, not the prose — unless the prose is invented, which is worse. Open every
one of the 36. If the page supports what the card says, the honest tier is `previewed`
and it moves there, with `notes` recording that it was verified today. If the page
cannot be opened, or the prose claims something the page does not support, strip it: the
card keeps title, link, publisher, format, and one fixed `skip_if` — *"Skip if you want
something we have read. We have not opened this one yet."* — and stays `listed`.
Then the validator makes it permanent: a `listed` item may carry no `summary`, `teaches`,
`who_for`, or `questions`, and its `skip_if` must be that fixed line. Rule 2 stands —
`skip_if` is never empty — and this line is a true reason to skip.
*(Veto point: if you would rather strip all 36 without verifying, say so; it is faster
and loses nothing the label was entitled to claim.)*

**D2 — No sentence on the site may claim a checking level the data shows as zero.**
Three lines lie today. Rewrite each to what is true, in the copy deck:
- First screen: *"635 resources. Every one opened, dated, and given a reason to skip
  it."* — the number generated, not typed.
- The 70-versus-700 line goes. It describes a site that does not exist yet. If you keep
  the thought, it is an aim, stated as one: *"We would rather read fewer resources in
  full than list more we have only skimmed. Today the count read in full is zero, and
  the label on every card says how far we got."*
- "We find material, read it, and write two things" → "read as far as the label says".
- "We do not list something we cannot open" → "whose page we cannot open. A paid course
  is opened at its sales page; the label says so."
Then add the four sentences to the regression sweep so Attack 3 re-reads them.

**D6 — The staleness warning sits beside the date, never in place of it.**
"Published 16 Aug 2023 · over a year ago, may not match Claude today." The home page
promises the date; show it.

**D7 — A cell with two picks or none says why.**
From `two_pick_cause`: *"Only two here — everything else at this level comes from the
same publisher."* From a pool of three or fewer: *"Too few to pick from — these are all
of them."* The empty state already speaks; the thin states must too.

**D8 — Picks survive a search.**
The block stays whenever role and level are set. Picks that fail the extra filter or the
query are omitted; the count-honest heading you already built adapts; all three gone →
one line, *"None of the three picks match your other filters."* The site's best editorial
work must not vanish on the first question.

**D11 — The tier badge's meaning is reachable without a mouse.**
The badge is a link to its definition on `how-we-check.html#tier`, with the one-line
meaning in `aria-describedby`. The tooltip may stay for mouse users; it is no longer
the only path.

**D15 — A publisher name is a gate, not a lookup.**
Validator: every host in the catalogue must resolve to a publisher name from the
mapping, or the entry fails. Fix "Und", "Master" and `qwe.edu.pl` now, and every other
slug the rule finds. The August fix was right and did not run on new rows; this makes
it run on every row forever.

# Also this round — three mechanical things the attack surfaced

- **Two picks contradict the card beneath them** (2.9c): the researcher's retention page
  and the PM's onboarding page. The FIX-15 audit said zero self-contradictions; it was
  wrong on these two. Re-run check 3 over all cells with the attackers' method — read
  the pick's own `who_for` and `skip_if` against the cell — fix what it finds, and add
  "contradicted its own card" as a recorded runner-up cause.
- **Time chips that contradict the card's text** (D14): extend the typed-number check
  to items — a card whose prose says "fifteen minutes" under a "half a day" chip is a
  fault. Print the list, fix from the page, log old → new. Checkpoint at 40 if the list
  is longer than that.
- **"Claude code" lowercase in 164 bullets**: the capitalisation map is single-word;
  teach it the phrase. Mechanical.

# Rulings recorded now, built next round

Read these so nothing you do today works against them. Do not build them.

**D3 — Search is rebuilt.** Stemming, synonyms, British spellings, a deterministic
tie-break, and `skip_if`/`who_for` in the index. Spec first, in `docs/specs/`, then
build; the 57-query suite is the measure and the before/after per role is the report.

**D4 — A thin level says so and offers the level below.** The front door keeps all four
levels — hiding one lies about who the visitor is. When a cell returns fewer than five,
the page says so and offers one click to include the level below. Exact match stays
the default.

**D5 — A role tag must be true of the card.** Extend the Puckett check: a `who_for`
that names a persona not among the tagged roles is a warning. Sweep the list with the
FIX-16 test — open the page, trim or widen. Checkpointed.

**D9 — Price is a field.** Optional, for the 26 paid items: amount, currency, and it
inherits the checked date. Shown only when known, as "from $995". Hand-verified.

**D10 — "How well checked" is a filter.** It is the differentiator and you cannot
filter on it. Four values, same machinery as the other five axes.

**D13 — The site names its "we".** One person, not affiliated, and Claude did the
reading at the tiers the labels say; a person has read nothing in full yet. On
`how-we-check.html`. *(Veto point: whether to use your name is yours; the sentence
works with "one researcher at DTU" if not.)*

**D12 — The recipe gallery is a spec, not a ruling.** 148 rows from one prompt-recipe
gallery, 78 of them filed at "built things with it". A prompt recipe is not building.
This round only measures: how many of the 148 are picks or path steps, and what every
`builder` cell looks like without them. The decision follows the measurement.

Deferred without a ruling, on purpose: the og:title build step, the attract loop, the
sort semantics, paths above beginner level. They wait for the human test.

# Not yours

STATUS.md "Needs a person" and part 10. The human test.

# Commits

One per ruling done, one for each of the three mechanical items, one for the D12
measurement — eleven at most, each one job. `FIX-24.md` with the round. Finish with
what surprised you, what you got wrong, whether it was in CLAUDE.md — and how many of
the 36 survived verification.
