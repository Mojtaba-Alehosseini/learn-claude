# Fix prompt — three rulings, the a11y leftovers, then the harvest

Paste everything below the line into Claude Code, in the project folder.

---

Good round. The 80-word link names are the finding of the month: every machine check
called it a pass, and the page was unusable anyway. Keep asking what the name actually
says. Three rulings, one small job, then the decision I have been sitting on.

# Rulings

1. **Keep the path-card ring fix.** One focused element, one ring. The CTA ringing the
   whole card was noise wearing a focus state. Do not revert.
2. **Pin the `--bark` margin where a future editor will meet it.** A comment in
   `tokens.css` at the token: the measured pairs, the 4.60 and 5.07, and that the picks
   block passes by 0.10 — so nobody lightens it for taste and fails silently. No value
   changes.
3. **`Generate an AI policy` — re-judge it as a pick.** The card was right and the
   audit was wrong; now the open question is whether a nonprofit-specific walkthrough
   still beats its pool for the general reader of its cell. Judge it by the standing
   bars against the corrected card. If the reason no longer beats the runners-up, swap
   with a recorded runner-up and log it. If it still wins, say why in the log and leave
   it.

Commit these together, small.

# Small job — the two a11y leftovers a browser can test

Both are DevTools-emulable, no new method needed:

- **400% zoom.** All five pages: content reflows, no horizontal scroll, nothing
  clipped or overlapped, the filter sheet still usable.
- **Forced colors.** Emulate `forced-colors: active`: focus rings survive, chips and
  badges remain distinguishable, nothing disappears into the background.

Fix what fails under the same rules as last round — tokens only, log old-and-new,
design-visible changes flagged. Append findings to `docs/attack/A11Y-AUDIT.md`.

The real screen-reader run stays mine — NVDA, by hand. Do not simulate one and call
it done.

# The job — harvest the thin end

Decision made: we fill the thin spots. The main audience is people who have never used
Claude, and that is the thinnest level in the catalogue. Priorities, in order:

1. **`never-used`, all roles** — the number that has bothered me longest.
2. **`designer`** — the thinnest role.
3. **Non-Anthropic material at `confident` and `builder`** — every builder cell runs on
   1–3 publishers and almost all of it is Anthropic's own. If good independent material
   exists, we want it. If it genuinely does not, measure that and say so — do not
   force weak entries in to move a number.

**Step 0 — measure first.** Current counts per cell from `data/items.json`, not from
this prompt. Numbers in prompts rot; you know this.

**Step 1 — build the source list by walking indexes.** The Academy gap happened
because the harvest was search-driven and never walked the publisher's own index. So:
start from the publishers we already hold and the two research files from August, find
each one's index or archive, and walk it. Search fills gaps; it is not the method.
The source list goes in `research/` as markdown with URLs and dates checked.

**Step 2 — checkpoint.** The first 10 entries, full schema, before the rest. If the
`skip_if` lines are weak at 10 they will be weak at a hundred, and I would rather stop
at 10.

**Step 3 — the rest.** The rules do not bend for volume:

- Every URL opened. Every claim sourced and dated. Nothing invented — no course, no
  price, no date. `published` is a real date or `UNVERIFIED`.
- `skip_if` at the bar, every entry. The Academy run proved fast batches can grade
  better than slow ones — the bar is still the bar.
- Tier honesty: `previewed` means we read the outline, `listed` means we only sorted
  it. Nothing gets `ai-reviewed` unless the whole thing was actually read this round.
- Anything older than 12 months gets the outdated flag.
- Duplicate rules 10 and 11 do their work; escape hatches only with a written reason.

**Step 4 — let the machinery fire.** Build. The changed pools make cell fingerprints
stale — that is the system working. Re-pick every stale cell with the full card view,
under all four constraints and the shortlist principle. Report which publisher-thin
cells the harvest un-thinned, if any.

**Step 5 — verify and ship.** Validators, link check, a real browser on the changed
cells, then deploy. Report the per-cell deltas: before, after, and what is still thin.

# Not yours

Still mine: the email address, nothing is `reviewed`, the subject axis, the NVDA run.

# Commits

Rulings, a11y leftovers, harvest, and re-picks — four separate commits. Commit
`FIX-17.md` with the round.

Finish with what surprised you and what you got wrong.
