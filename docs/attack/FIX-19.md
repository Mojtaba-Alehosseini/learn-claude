# Fix prompt — make the rot visible

Paste everything below the line into Claude Code, in the project folder.

---

Read your own round again. The twenty rows are the least of it. Every finding that
mattered was silent rot found by accident: a stale date quietly excluding a live
resource from every pool, a redirect the link check called "ok", counts rotting one
round after the rule against it, six `who_for` lines opening the same way. None of
those had an instrument. This round builds the instruments, then runs them.

Two corrections to your report first. "Official ratio held at 61%" hides that the batch
was 80% Anthropic — it held because 20 is small against 618, not because leg 2 worked.
And "AI for Science" was not wrong by ten months, it was stale by ten months: Help
Center dates are last-updated dates and drift by design. Different fault, same
exclusion. Job 2 follows from that.

# Rulings

- The "Research"-feature collision flag stays unfixed. Never edit a card to silence an
  advisory check.
- Removing the expired SBA event was right. Convention stands: an expired event is
  removed; a dead resource with a redirect gets its new URL; dead with no destination
  is removed. Write that convention into the link checker's docstring.
- Add this to `CLAUDE.md` under Working rules, word for word:
  *Shell hygiene: never put a regex or a backslash through a heredoc — write scripts
  to a file and run the file. Commit messages via `git commit -F`. Never background a
  command that backgrounds itself; confirm a job started before reporting it running.*

# Job 1 — numbers are generated, never typed

Hand-written counts have rotted twice in three rounds. Discipline is not the fix.

- `scripts/measure.py` prints every number the docs use: catalogue size, publishers,
  tier counts, format, level, cost, official ratio, UNVERIFIED count, cells with
  picks, thin and empty cells, dead links at last check.
- `build.sh` writes it to `docs/STATUS.md`, dated. Generated file, committed, never
  edited by hand — say so in its first line.
- THE-PROJECT.md part 3 and README "Where it stands" become pointers to STATUS.md,
  the way START-HERE became a pointer. Historical numbers in part 9 stay — they
  describe what a past run did.
- `how-we-check.html` already computes from data. Confirm it agrees with STATUS.md.

# Job 2 — exclusions print, and drifting dates get re-read

- The build prints every live resource the freshness rule excludes from the picks
  pre-filter: count and list. Silent exclusion is how a good resource vanished.
- Measure how many dated items are currently flagged outdated. Re-open each one and
  apply the FIX-18 method — printed date becomes the date, "updated this week" stays
  `UNVERIFIED`. If the count is over 60, stop after 60 and show me the hit rate
  before continuing.
- For pages on the Intercom template (`support.claude.com`), the weekly check parses
  the printed date and reports drift against `published`. Stale-by-design dates get
  re-read by machine from now on.

# Job 3 — a redirect is a fault, not an "ok"

- `check-links.py` gains a `moved` class: permanent redirects (301, 308) with the
  final URL recorded. Report it in the weekly run beside ok/gone/blocked.
- Run it now. For every `moved`: open the destination, update the URL and everything
  that references it — ids come from URLs, so picks and paths move with it, and the
  validators will tell you if they did not — and re-read the card against the new
  page, because the Excel one changed what the reader needed to know. Log old → new.
- The 21 blocked hosts stay blocked; note them once in STATUS.md as unverifiable by
  machine, with the last date a person checked.

# Job 4 — copy monotony is a number

The `skip_if` measurement two rounds ago (5% shared openings versus 12%) was done once
by hand. Make it permanent: the validator prints the share of `skip_if` and `who_for`
lines sharing their first three words, per build, and warns above 10%. Print only —
nobody edits copy to move a statistic.

# Job 5 — survey the advanced end, do not harvest it

Leg 2 yielded four of nine. Before spending a round on `builder` and `confident`,
measure the supply: walk the indexes of five independent publishers likely to carry
advanced non-coder material — Cowork, Skills, connectors, agents — and count what
exists, per cell it would land in. A report in `research/`, dated, no entries
written. If the supply is real, that is the next round. If it is not, part 11 says so
and we stop chasing it.

# Not yours

Still mine: the email address, nothing is `reviewed`, the subject axis, the NVDA and
High Contrast run.

# Commits

One per job, `FIX-19.md` with the round. Finish with what surprised you and what you
got wrong — and this time, whether any of it was already in CLAUDE.md.
