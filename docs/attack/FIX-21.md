# Fix prompt — a date needs a source

Paste everything below the line into Claude Code, in the project folder.

---

Stopping at the checkpoint was right, and what you found is bigger than nine dates. The
catalogue has never recorded where a date came from, so a wrong one could sit there
for a year and nothing could surface it. The fix is not correcting nine. It is the same
move this site already made twice: never round up. A date without a source is
`UNVERIFIED`.

# The ruling — `date_source`

New field, required whenever `published` or `updated` is a real date:

| value | means |
|---|---|
| `printed` | a person read it on the page |
| `metadata` | the parser read it from JSON-LD, `article:published_time`, `dateModified` |
| `upload` | a video platform's upload date |
| `intercom` | the Help Center parser |

Validator: a real date with no `date_source` is an error. `UNVERIFIED` needs none.
From now on no harvest can write a date without saying how it knows.

# Job 1 — apply it to all 194

Work through the population you measured, and log every change old → new.

**49 with metadata.** Metadata wins unless the page visibly prints a different date;
`datePublished` → `published`, `dateModified` → `updated`. One-day differences are
timezone — take the metadata value and move on. The 40 that agreed get
`date_source: metadata` too.

**49 readable without metadata.** These were never opened. Open each one — this is the
part the parser cannot do. A printed date → keep, `printed`. A printed last-updated
line → `updated`. Nothing printed → `UNVERIFIED`, and the old value goes into `notes`
so a person can restore it if they ever find where it came from. No checkpoint — the
rule is mechanical, printed or not.

**7 unreadable by machine.** `UNVERIFIED`, old value in `notes`. We cannot stand behind
a date nobody can currently see. They are on my list to open by hand.

**71 YouTube.** Try the parser on the watch pages first — `uploadDate` sits in the
page's JSON-LD and may be readable without touching the consent wall. Readable →
`upload`, confirmed. Blocked → `upload` with a note that it dates from harvest, and
the count of unconfirmed ones goes into STATUS.md. Do not click the banner.

**18 Intercom.** `intercom`, already parser-driven.

Then let the machinery fire: freshness, the exclusion print, stale fingerprints,
re-picks. The Small Business item will flip to outdated and may fall out of a pool —
that is correct. UNVERIFIED will rise. Say so in STATUS.md and part 11 as a measured
number, not an apology.

# Job 2 — no typed numbers becomes a check

You built `measure.py` and four days later typed "ninety minutes" into a path intro.
The rule was too narrow and it had no check behind it.

- Validator warning: any prose field in `paths.json` (intro, every `why`) and any
  reader-facing string in `ui.js` that contains a number or number-word next to
  minutes, hours, days, steps, resources, or a percent. Warning, not error — some
  numbers are legitimate — but it prints every hit so a typed figure cannot hide.
- Change the CLAUDE.md rule to this, word for word:
  *Numbers anywhere a reader or I will read them — docs, path intros, UI strings,
  commit messages that state a count — are generated or measured, never typed.
  `scripts/measure.py` writes `docs/STATUS.md` on every build; docs point at it.*

# Small

- The first-of-month analysis: keep it in the audit log as inconclusive, exactly as
  you wrote it. Do not chase it.
- STATUS.md gains a provenance table: count per `date_source`, plus UNVERIFIED.

# Not yours

Still mine: the email address, nothing is `reviewed`, the subject axis, the NVDA and
High Contrast run, the YouTube and Udemy walk, the 7 unreadable pages.

# Commits

The field and validator, the 194 applied, the re-picks, the number check — four.
`FIX-21.md` with the round. Finish with what surprised you, what you got wrong, and
whether it was already in CLAUDE.md.
