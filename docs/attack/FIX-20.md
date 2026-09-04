# Fix prompt — one field doing two jobs, and the date class

Paste everything below the line into Claude Code, in the project folder.

---

Every instrument found something on its first run. That is the round working. Now
the two things you handed back, one you routed around, and one class you opened but
did not close.

# Ruling 1 — `published` gets a sibling: `updated`

You were right not to write a last-updated date into `published`. The fix is the
field, not the fudge.

- New optional field `updated`, a real `YYYY-MM-DD` or absent. Validator: when both
  are real, `updated >= published`. Never `UNVERIFIED` — absent is the honest empty.
- **Freshness uses the later of the two.** The outdated flag, the picks pre-filter and
  the exclusion print all move to that rule. One definition, one place — you know why.
- The Intercom drift parser writes `updated`, never `published`. The 15 drifts convert
  now. GOV.UK gets both dates.
- **Migrate every `support.claude.com` item:** Intercom never prints a publication date,
  so the dates FIX-18 wrote into `published` move to `updated`, and `published` goes
  back to `UNVERIFIED`. That includes the ten checkpoint entries and the sixteen
  re-dated. Same for any other item whose `notes` say the date came from a
  "last updated" line.
- The card shows what it knows: the published line as now, an updated line only when
  present. New strings in `ui.js` and `ux-copy.md` together. `measure.py` and
  STATUS.md gain the count of items carrying `updated`.

Re-run the exclusion print after. Report how many of the 14 excluded come back.

# Ruling 2 — `teacher|confident`: fix the tag, do not route around it

The third-publisher item's `who_for` names a student and nothing else, and it carries
the `teacher` tag. That is the Puckett shape, and FIX-16 gave you the test: the card
must support every role tagged. Open the page. If it does not serve a teacher, trim
the tag — the cell returns to two publishers, the cap returns to two, and three picks
are legal again. If it genuinely does serve teachers, widen `who_for` so the card says
so, and the two-pick cell stands. Either way the answer comes from the page.

# Job — the date class, closed

Five of the nineteen excluded items carried a date the page never printed. Only the
excluded ones were opened. Every other dated item is in a pool right now and printing
a date on a card, and nobody has checked whether the page agrees.

- **Count first:** dated items that are not YouTube (upload dates are true) and not
  Intercom (the parser now covers them).
- **Open each one.** The page prints the date, or its metadata carries it
  (`article:published_time`, `dateModified`, a visible byline date) — record which.
  Nothing printed anywhere → `UNVERIFIED`. A last-updated line → `updated`.
- **Checkpoint at 60.** Show me the hit rate — how many were wrong — before going on.
  If it is under 5% after 60, finish without stopping. If it is higher, stop and we
  talk about where those dates came from.
- Extend the drift parser to generic page metadata where it exists, so this sweep
  never has to be done by hand again. The weekly run reports drift on every host it
  can read, not only Intercom.
- Log every change old → new.

# Small rulings

- **Monotony threshold.** My 10% was wrong for the field's grammar; your second figure
  is the right one. Set its warning at the measured baseline, so it fires on
  regression only. Print both.
- **Part 11 states the advanced-end gap now**, as measured by the survey: five
  candidates from five walkable publishers, the two most likely indexes unwalkable by
  machine. I will walk YouTube and Udemy by hand or not at all; the doc does not wait
  for that.
- **The four-step path.** Removing step 2 changed what step 3 follows. Re-read every
  `why` in that path and confirm each still explains its position. Fix any that now
  point at a step that is gone.

# Not yours

Still mine: the email address, nothing is `reviewed`, the subject axis, the NVDA and
High Contrast run, the YouTube and Udemy walk.

# Commits

Ruling 1, Ruling 2, the date sweep, the small rulings — four. `FIX-20.md` with the
round. Finish with what surprised you and what you got wrong, and whether it was
already in CLAUDE.md.
