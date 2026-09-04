# Fix prompt — month precision, the undated tie-break, and the human backlog

Paste everything below the line into Claude Code, in the project folder.

---

Every date says how it knows. The videoId check was exactly the paranoia the site is
built on. Three rulings from what the round exposed, then two small jobs that point at
the one gap no instrument can close: nobody has used this site.

# Ruling 1 — a month is a fact; keep it

"Last update: June 2026" is page-supported. Forcing it to `UNVERIFIED` because the
schema wants a day is the schema being wrong. So:

- `published` and `updated` accept `YYYY-MM` as well as `YYYY-MM-DD`. Validator
  updated; `date_source` still required.
- **Display what the page says:** the card prints "June 2026", never an invented day.
- **Freshness uses the earliest date consistent with it** — the first of the month.
  Never round up applies to staleness too: a month-only date is treated as its oldest
  possible day.
- Restore the two Coursera rows with `updated: 2026-06` / `2026-05`, source `printed`,
  and any other row whose `notes` now hold a month-only value that was dropped.

# Ruling 2 — undated stays eligible, dated wins ties

Excluding `UNVERIFIED` from picks would empty the pools — measure how many of the 40
cells would fall under three candidates if it were excluded, and put that number in
the validator's docs so the decision carries its evidence.

Then the tie-break: the picker's prompt says that at equal fit a dated resource beats
an undated one, and when that rule decided a slot, the reason says so in one clause.
Applies from the next re-pick on. Do not re-run cells for this.

# Ruling 3 — two lines for CLAUDE.md

Add under Working rules, word for word. Veto is mine; the wording is yours to paste:

*A commit does one job. If a file change serves two jobs, the second waits.*
*Scratch files go in `tmp/` — gitignored — never outside the repo.*

Create `tmp/` and the `.gitignore` line with it.

# Job 1 — the human backlog is a file

My by-hand list lives in the "Not yours" paragraph of nine prompts. Wrong place.

- `measure.py` writes a **Needs a person** section into STATUS.md, from data: the
  seven unreadable rows with URL and the date last dropped, the 21 blocked hosts with
  the last date a person checked, the resources that re-entered pools on lost evidence,
  every cell with zero non-Anthropic items, and every empty cell.
- THE-PROJECT.md part 10 carries the standing items that data cannot see — NVDA, High
  Contrast, the YouTube and Udemy index walk, `reviewed`, the report-link email — and
  points at STATUS.md for the rest. One list, two halves, no third copy.

# Job 2 — write the first human test

THE-PROJECT part 11 says three real people would teach more in an hour than another
fix round. It has said so for three weeks. When I find them, the hour must not be
wasted on deciding what to ask.

Write `docs/specs/2026-09-04-first-human-test.md`:

- Three participants, one each: a teacher, a student, a writer. Twenty minutes each.
  Their own device, the live site, no introduction beyond the URL.
- Four tasks, each tied to a promise the site makes: find the one thing you would open
  first for yourself; tell me what "Skip if" is for; find something about Cowork
  without using search; tell me what "Read by AI" means on a card. Word them as the
  person would hear them, not as we would.
- What to watch, not ask: time to first click, where they hesitate, whether they read
  the `Skip if` line at all, whether the picks block is noticed, what they say the
  tier labels mean, whether they leave through our resource page or straight out.
- A note sheet, one page, that a person can fill by hand while watching.
- What we do not do: no leading, no explaining, no tracking — the site has none by
  design and the test does not add any.
- What counts as a finding and where it goes: `docs/attack/HUMAN-1.md`, same shape as
  the ten role attacks.

Keep it to two pages. It is a script, not a study.

# Not yours

Still mine, and now in a file: see STATUS.md and part 10 after this round.

# Commits

Ruling 1, Ruling 2, Ruling 3, Job 1, Job 2 — five, one job each. `FIX-22.md` with the
round. Finish with what surprised you, what you got wrong, and whether it was already
in CLAUDE.md.
