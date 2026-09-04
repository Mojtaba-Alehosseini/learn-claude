# Fix prompt — the who_for faults, then the accessibility pass

Paste everything below the line into Claude Code, in the project folder.

---

The audit round did what it should: one systematic cause found and closed, every change
logged, and your own miscounts caught by your own checks. Three rulings to record, one
small job, then the last big item on the list.

# Rulings, recorded

1. **No re-pick over `card_view`.** The 37 cells were chosen on a smaller card than the
   reader sees, but the audit just read all of them against the full cards: zero
   self-contradictions, eight reason faults, all fixed. Re-picking now would be churn.
   Add one line to `PICKS-AUDIT.md` saying the shipped picks predate the `summary` fix
   and the next natural re-pick (a stale cell) uses the full view.
2. **`notes` stays out of `card_view` and out of the mirror.** Your reasoning was
   right: a reason must be checkable by the reader, and the reader cannot see `notes`.
3. Commit `FIX-16.md` (this file) with this round, same as you did for FIX-15.

# Job 1 — who_for must support every role tagged

The test is the one you already named: the card must support each role it is tagged
for. A business owner reading **"For: Researchers"** is the site lying in its own
voice.

- Fix `What are Projects?` and `Generate an AI policy`: either widen `who_for` so it
  honestly covers the tagged roles, or trim the roles. Decide per item from the card
  and the resource's own page — open the URL, do not guess.
- Apply the same test to the 3 items your Puckett check marked "worth a look". Trim or
  rewrite where the answer is clear; if any is genuinely ambiguous, list it in the log
  and leave it.
- `who_for` rewrites are held to the skip_if bar. Log every change old-and-new.
- Any roles trim refreshes the affected cell fingerprints — you know this from Puckett.

Commit this on its own.

# Job 2 — the accessibility pass, for real this time

This is the last standing item that is not personally mine. It has never been run.

**Start from the spec:** `docs/specs/2026-08-23-accessibility-audit.md`. Follow it —
do not invent a second method beside it. `scripts/a11y-audit.js` exists; use it, but
remember what this project has proved four times: a headless pass is not a page that
works. The keyboard walk happens in a real browser.

What must be covered, spec plus what was built since the spec was written:

1. **Contrast, computed in the browser** — not from the token file. `--bark` on both
   ivories, `--clay-text` at every size it ships, the picks label and reason lines,
   badge text, the footer.
2. **Keyboard, all five pages.** Full walk: logical focus order, a visible focus state
   on every interactive element, no unreachable control, no trap except the one that
   is meant to be there.
3. **The mobile filter sheet.** The trap holds while open, Esc closes, and focus
   returns to the element that opened it.
4. **Announcements.** The result count on Browse announces when filters change. The
   picks block is new since the spec: its heading structure, the "picked by AI" label,
   and the two-pick and empty-cell states must all make sense read aloud.
5. **Images and icons.** The 47 drawings, the publisher marks, the format tiles:
   decorative ones hidden from the reader, meaningful ones named. A screen reader
   hearing forty filenames is the failure mode.
6. **Cards.** The whole card is one click — check what that click is to a keyboard and
   a reader: one link with a proper name, not a clickable div.

**Fixing rules:**

- Every colour fix happens at the token, on its own hue, the way `--bark` was made.
  No new hardcoded values anywhere — rule 4 stands in an audit exactly as it does in
  a feature.
- Measure before changing any design value. If a fix would visibly change the design
  (a colour shift a sighted reader would notice, a focus ring that changes the look),
  make the change, log it, and flag it for my review — do not silently trade the
  design away, and do not silently keep the failure either.
- Anything you cannot fix without a design decision goes in the findings as a question
  for me, with the measurement attached.

**Findings** go in `docs/attack/A11Y-AUDIT.md`: what was checked, what passed, every
change old-and-new, and the open questions. Then verify the fixes in a real browser —
keyboard and screen-reader semantics, desktop and mobile — and re-run the picks and
catalogue validators to prove nothing else moved.

Commit the a11y work separately from Job 1.

# Not yours

Still mine: the email address, nothing is `reviewed`, the subject axis, and whether to
harvest the thin cells (`designer`, `never-used`). Do not start any of them.

Finish with what surprised you and what you got wrong.
