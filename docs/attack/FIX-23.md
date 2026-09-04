# Fix prompt — Attack 2

Paste everything below the line into Claude Code, in the project folder.

---

The instrument arc is finished. Nine rounds, every check fired on its first run, and
the last one measured that undated material is holding the top half of the site up.
Good. Now the thing no fix round can do.

Since the ten-role attack in August the site has changed more than it did before it:
a picks block on forty cells, two-pick and empty cells, an `Updated` line, month-only
dates, rebuilt card links, repaired paths — and **77% of cards now say "No publish date
given."** That is honest. It may also read as a broken site. Nobody has looked at the
whole thing as a hostile stranger since it held 353 resources and no picks. Fix rounds
verify what they changed. They do not find what changed around them.

This round is Attack 2. Two small guards first, because you keep breaking the same rule
one commit after writing it, and the concrete damage is always the same byte.

# Preliminaries — two guards, one commit each

1. **`measure.py` checks its own output.** Every value it emits is typed and every
   partition sums: tiers to the total, levels to the total, formats, costs,
   `date_source` plus UNVERIFIED to the dated population. A test runs it and fails
   on a shadowed name, a string where a count belongs, or a partition that does not
   add up. It is the file everything else quotes; it gets a test before anything else.
2. **A pre-commit hook rejects control characters** in any tracked text file — the
   backspace byte a heredoc leaves behind — and runs the catalogue validator. Local
   mirror of CI, so the failure lands before the commit, not after the push.

# Attack 2 — the method

**Reuse August.** Read `docs/attack/PLAN.md`, `RUN.md`, `RUN-LOG.md`, `role-view.py` and
the ten findings files before writing anything. The method exists; do not invent a
second one beside it. Where the old run was slow or blind, say so in the new log and
improve it there.

**Refresh `00-facts.md` from STATUS.md.** It was hand-written in August. Every number
in it is now generated — point at STATUS.md and keep only what a visitor cannot see
from the site.

**Ten agents, one per role, in parallel.** Each visits the live site as a hostile
stranger at all four levels: never used, used a little, used a lot, built things. Their
own words for their own job. They do not know the data model, the constraints, or
this brief. They know the URL.

**A finding is a claim.** Every one carries the URL, what was done, what was seen, what
a reasonable person expected instead, and who it harms. No invented findings — an
attacker who cannot reproduce it does not report it. Severity by reader harm, not by
how interesting it is.

# What is in scope that August could not see

Tell every agent to spend real time on these, at every level:

- **The picks block.** Do the three feel like judgment or like the first three rows?
  Does each reason say something the title did not? Does "picked by AI" read as
  honesty or as a warning label? What does a two-pick cell feel like? The empty cell?
- **The date lines.** Three cards in four say "No publish date given." Does the site
  look unmaintained? Does "Checked 4 Sep 2026" carry the trust it is meant to? Does an
  `Updated` line without a published date make sense? Does "May 2026" with no day?
- **The tier labels.** "Skimmed" on 78% of the catalogue — what does a stranger think
  that means about the site?
- **Search, in the visitor's words.** Each agent writes five queries a real person in
  that role would type — *is claude free*, *make claude remember my stuff* — and
  judges the top three. Every query and its verdict is recorded.
- **Paths after repair.** Read every `why` as a stranger. Does each step's reason still
  explain its position?
- **Keyboard and phone.** One full walk each, per agent, at one level. Card links,
  the filter sheet, the picks block heading order.
- **The method page.** Does `how-we-check.html` make a stranger trust the site more or
  less? Is the 61%-official statement read as candour or as a shopfront confession?

# Regression sweep

Attack 1's summary lists what it found. Re-test every finding it rated high: the `?q=`
deep link, publishers recorded as platforms, 96-character lines, useless `Skip if`
lines, the unsourced accusation. Nine rounds of change since; confirm none came back.
One table: finding, fixed in, still fixed today.

# Output

- `docs/attack/2/01-non-technical.md` … `10-writer-marketer.md`, same shape as August.
- `docs/attack/2/SUMMARY.md`: findings deduplicated across roles, ranked by harm, with
  the count of roles that hit each. Then two lists — **mechanical**, fixable without a
  judgment call, and **decisions**, which are mine.
- `docs/attack/2/REGRESSION.md` — the sweep table.
- **The search queries become a test.** Every query the agents wrote goes into
  `scripts/test-search.py` with its expected top result where the agent was satisfied,
  and marked `xfail` with the reason where it was not. Fifty queries in a visitor's
  words, kept forever, run on every build. That is the instrument this round leaves
  behind.

**Fix the mechanical list directly** — typos, contradictions, dead controls, wrong
labels — one commit, every change logged in SUMMARY.md. **Do not touch the decisions
list.** If an attacker says the date line makes the site look abandoned, that goes to
me with the evidence, not into a redesign.

# Not yours

Still mine, and in a file: STATUS.md "Needs a person" and part 10. Do not start the
subject axis, the advanced-end harvest, or any design change the attack argues for.

# Commits

The two guards, the facts refresh, the attack files, the search suite, the mechanical
fixes — six. `FIX-23.md` with the round. Finish with what surprised you, what you got
wrong, whether it was in CLAUDE.md — and which single finding you would fix first if
you were me.
