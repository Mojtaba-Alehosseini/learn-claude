# Fix prompt — a check whose failure cannot be seen is not a check

Paste everything below the line into Claude Code, in the project folder.

---

47 of 57 is the target met. It is not the round's finding. The finding is that
`build.sh` printed `Done.` over failing gates for an unknown number of rounds, and
that you saw eight queries fall, pushed, and wrote a paragraph. Both get a rule, and
the first gets an audit, a bite test, and a history.

# Two lines for CLAUDE.md

Under Working rules, word for word:

*A check whose failure cannot be seen is not a check. Every gate has a bite test:
plant its failure, run the build, watch it go red.*

*A failing gate is fixed or reverted before push. It is never explained.*

# The audit — every place a check is run

List every invocation of every gate: `build.sh`, `deploy.yml`, `check-links.yml`, the
pre-commit and commit-msg hooks, `install-hooks.py`, and any script that calls
another script. For each: the command, what it is piped through, whether its exit
status reaches the caller, and whether the caller stops on it. Every `| tail`,
`| head`, `2>/dev/null`, `|| true`, backgrounded run, or subshell whose status is
dropped is a hole. Fix each so failure is exit status, not text. The table goes in the
round record.

Then the bite test for the pipeline itself: `scripts/test-gates.py` runs each gate
against a temporary copy of the data with its failure planted — a dead pick, a
`listed` row with a summary, a typed count, a suite query forced to fail — and asserts
the build exits non-zero every time. CI runs it. The validators already prove they
bite one by one; this proves the thing that runs them can see them.

# The history — how long was it lying

For every round-end commit since `build.sh` first piped a check through `tail`, check
it out into a temporary worktree and run the gates with `pipefail` on. One table:
commit, round, which gates failed, and whether that commit was deployed. Then say
plainly in the record which rounds reported green on a red build, and confirm that at
HEAD every gate passes with failure visible. If anything shipped live in a failing
state and is still wrong, fix it in its own commit.

# Self-retrieval — the check the rewrite needed

The suite is 57 queries over 598 rows. Near-synonym replacement dropped eight the
suite could see. Two checks:

- **Permanent:** every row's own `questions[]` must retrieve that row in the top three.
  A row that cannot be found by its own questions has questions that do not describe
  it. Printed list, warning, run on every build.
- **Once:** take every row's `questions[]` as they were at `6021258`, run them against
  today's index, and list every row its old questions no longer find in the top
  three. For each, the page's own nouns went missing in the rewrite; put them back
  from the page, keep the reader's phrasing beside them, log old → new.

Re-measure the suite after. It may not move; the catalogue will.

# Close the search work

- The final failure table: the ten that remain, each with cause and where its answer
  sits. If any is a general ranking fault with two others of the same shape, it is a
  spec amendment for later, written down, not built now.
- The spec's section 5 gets the measured final numbers, per role, and section 4 the
  final index size. Section 6 stays.
- THE-PROJECT part 11: one paragraph on where search stands, pointing at STATUS.md.

# Not yours

STATUS.md "Needs a person" and part 10. The human test.

# Next round, so nothing today works against it

Attack 3. Search, tags, levels, collections, `questions[]`, the date lines and the
picks block have all changed since Attack 2. Same method, same ten roles, plus a
regression sweep over Attack 2's summary. Do not start it; know it is coming.

# Commits

The CLAUDE.md lines, the audit fixes, `test-gates.py`, the history, self-retrieval,
the once-check repairs, the search close-out — one job each. `FIX-31.md` with the
round. Push. Finish with what surprised you, what you got wrong, whether it was in
CLAUDE.md — and how many rounds reported green on red.

---

# The round as run

## The answer first

**Two rounds' builds reported green while a gate was failing. One of them shipped.**

`build.sh` could not fail on any gate between `9c3d100` (5 September 2026, the commit that
put the search suite behind `| tail -2`) and `5414d29` (6 September). Twelve gates
accumulated inside that window. Five round-end commits in it were genuinely green when
their gates are run with the status visible. Two were not:

- **FIX-29** shipped live with `check-typed-numbers.py` failing. No runner anywhere could
  see it: `build.sh` was piping it, and CI has never run that gate at all.
- **FIX-30** had `test-search.py` and `check-typed-numbers.py` failing. CI runs
  `test-search.py` directly, so the deploy went red and the round did not ship until it
  was fixed. That is the failure that started this round.

The typed-number faults were repaired at the end of FIX-30. At HEAD every gate passes, and
`scripts/test-gates.py` proves each one can be seen to fail.

## The audit — every place a check is run

Method and evidence in [GATE-AUDIT.md](2/GATE-AUDIT.md), including the shell behaviour
reproduced directly rather than argued from memory.

### `build.sh` — before and after

| command | was piped through | status reached the caller | stops the build |
|---|---|---|---|
| `validate-catalogue.py` | *not run here at all* | — | now yes |
| `test-validate-catalogue.py` | *not run here at all* | — | now yes |
| `stable-ids.py` | nothing | yes | yes |
| `add-source.py` | `head -3` | **no** — and `head` would break it under pipefail | yes |
| `build-paths.py` | `tail -3` | **no** | yes |
| `build-search-index.py` | nothing | yes | yes |
| `test-search.py` | `tail -2` | **no** | yes |
| `test-search.py --emit` | `> /dev/null` | yes | yes |
| `test-search-runtimes.js` | `tail -1` | **no** | yes |
| `validate-synonyms.py` | nothing | yes | yes |
| `test-stem.py` | `tail -1` | **no** | yes |
| `test-role-buckets.py` | `tail -1` | **no** | yes |
| `check-questions.py` | `tail -1` | **no** | yes |
| `check-self-retrieval.py` | *new this round* | — | yes |
| `test-gap-claims.py` | `tail -1` | **no** | yes |
| `build-sitemap.py` | nothing | yes | yes |
| `build-data-js.py` | nothing | yes | yes |
| `test-browse-query.js` | *not run here at all* | — | now yes |
| `measure.py --status` | nothing | yes | yes |
| `test-measure.py` | `> /dev/null` | yes | yes |
| `validate-picks.py` | *not run here at all* | — | now yes |
| `test-validate-picks.py` | *not run here at all* | — | now yes |
| `test-copy-claims.py` | nothing | yes | yes |
| `check-typed-numbers.py` | `tail -1` | **no** | yes |
| `audit-pick-contradictions.py` | `tail -1` | **no** | yes |
| `audit-time-chips.py` | `tail -1` | **no** | yes |

Ten gates could not fail the build. Two of the piped commands are generators rather than
gates and have been piped since the file's first commit, which is why the window opens at
the search suite rather than at the beginning.

**The fix is not `pipefail` alone.** `cmd | head -3` kills the producer with SIGPIPE, and
pipefail reports that as failure — a gate going red for a reason unconnected to what it
guards is how people learn to ignore a red build. So nothing is piped now: a `gate` helper
captures the output, prints the tail on success and every line on failure, and returns the
command's own status.

**Four gates CI ran and `build.sh` never did are now here too**, so a fault in
`items.json` is found on the machine that wrote it rather than on the server.

### The other runners

| where | command | piped | status reaches | stops |
|---|---|---|---|---|
| `deploy.yml` | the catalogue validator and its bite test, `test-measure.py`, the picks validator and its bite test, `./build.sh`, the data-file check, `test-browse-query.js`, `test-search.py`, `test-copy-claims.py` | nothing | yes | yes |
| `deploy.yml` | `test-gates.py` — **new this round** | nothing | yes | yes |
| `check-links.yml` | `check-links.py`, `report-dead-links.py` | nothing | yes | yes |
| `.git/hooks/pre-commit` | execs `scripts/pre-commit.py` | nothing | the script's status **is** the hook's | yes |
| `pre-commit.py` | `validate-catalogue.py` via `subprocess.run` | nothing | `returncode` checked explicitly | yes |
| `.git/hooks/commit-msg` | execs `scripts/commit-msg.py` | nothing | same | yes |

No holes outside `build.sh`. The asymmetry that mattered was different: **CI never ran
seven of the gates**, including the one that was failing at FIX-29.

## The history

`tmp/gate_history.py` checks each round-end commit into a worktree and runs **that
commit's own** build steps in order, each with its pipe stripped, continuing past failures
so every failing gate is found rather than only the first. Deployment is read from the
Actions history, not inferred.

| commit | round | gates that were failing | deployed |
|---|---|---|---|
| `45fafac` | FIX-24 | none | yes |
| `fdae55e` | FIX-25 | none | yes |
| `ea7b7ea` | FIX-26 | none | yes |
| `013e36c` | FIX-27 | none | yes |
| `7ceff3e` | FIX-28 | none | yes |
| `6021258` | FIX-29 | `check-typed-numbers.py` | **yes** |
| `d80bedd` | FIX-30 | `test-search.py`, `check-typed-numbers.py` | **no — CI stopped it** |

## The bite test

`scripts/test-gates.py` copies the working tree, plants a fault in the copy, runs the real
`build.sh` in it, and asserts the build goes red **saying the words the gate meant to catch
it prints**. The control comes first: an untouched copy must build green, or nothing below
it means anything.

What it plants: a `listed` row carrying a verdict, a question written as a suite query, a
suite query forced to miss, a content gap with no evidence, a synonym with no reason, a
dead pick, and a typed count in a pick's reason. Every one turns the build red at the right
step.

It named the wrong expectation once, and said so on the first run: a content gap with no
evidence is refused by `test-search.py`, which is where the rule is enforced, while
`test-gap-claims.py` is that rule's own bite test. The expectation is a phrase now, not a
filename.

It takes about three minutes because it runs the real build once per fault. That is the
price of testing what actually runs. CI runs it; `build.sh` does not, because a build that
ran it would call itself.

## Self-retrieval

**The permanent check** — `scripts/check-self-retrieval.py`, in the build — asks each row
its own questions and looks for that row in the top three. Every row that carries questions
passes today, and **it would not have caught FIX-30**: run against the exact state that was
pushed with eight suite queries broken, every row was still findable by its own questions.
That is measured, not assumed, and it is the honest limit of this check. A row is very good
at retrieving itself with its own words; the check catches a row whose questions describe
something else, which is a different fault.

**The once-check** is what found the damage. Asking each row's pre-rewrite questions of
today's index returns 266 rows, most of it noise. Narrowed to the brief's own terms — a
word the page prints, selective enough to admit a result, gone from the questions with no
inflection covering it, on a question that no longer finds the row — it is **118 rows**.

**74 repaired, 44 left alone.** Every repair keeps the reader's phrasing and puts the
page's word back; the ones left alone dropped a verb or an adjective, not a noun the page
owns. Old to new for all of them: [NOUNS-RESTORED.md](2/NOUNS-RESTORED.md).

Three things went wrong in that pass and all three are in the log. One repair over-claimed
and pushed another row out of the top three — the gate caught it in the same build and it
is reverted. One restored a word by dropping another, caught on the re-run. One word cannot
be repaired a row at a time: the catalogue indexes `claudemd` as a single token and a reader
types "claude.md", which is a spelling-map job.

## The suite

Both columns are the same fifty-seven queries and the same rule.

| role | FIX-31 start | FIX-31 close |
|---|---|---|
| business-founder | 4 of 6 | 4 of 6 |
| data-analyst | 4 of 5 | **5 of 5** |
| designer | 5 of 7 | 7 of 7 |
| developer | 5 of 7 | 5 of 7 |
| non-technical | 4 of 5 | **5 of 5** |
| pm | 6 of 7 | 7 of 7 |
| researcher | 4 of 5 | 4 of 5 |
| student | 5 of 5 | 5 of 5 |
| teacher | 4 of 6 | 4 of 6 |
| writer-marketer | 4 of 4 | 4 of 4 |
| **total** | **45 of 57** | **50 of 57** |

The brief predicted the suite might not move, and the noun repairs on their own did not
move it — the wins came from rows promoted on their previous entry's own terms, and from
the repairs happening to reach two of those rows. The catalogue moved either way, which
was the point.

## Closing the search work

The final failure table is in [SEARCH-FAILURES.md](2/SEARCH-FAILURES.md): seven queries,
each traced. Two are spec amendment 6 (the phrase bonus pays a row for holding a string
shorter than what the reader typed). Two are a new **amendment 7**: an expansion — stem or
synonym — scores at half weight and never admits, which is right for a synonym and doubtful
for an inflection. Two are gap candidates that stay candidates until their pages are
opened. One is the ranking working correctly.

The spec has its measured close per role and its measured index size. **The index is over
the 150 KB budget that spec set, at 166 KB transferred**, and the cause is named rather than
hidden: almost none of the growth is machinery, it is the phrase map keeping every
`questions[]` string whole while those questions were rewritten and lengthened. Amendment 6
is where that gets settled.

THE-PROJECT part 11 has a paragraph on where search stands. Writing it exposed that the
same section carried typed counts that had rotted — resources, picks and publisher figures
from two rounds ago. They now point at STATUS.md, which is generated.

## What surprised me

**That five rounds were genuinely green.** I expected the hole to have swallowed failures
all the way back. It had not: FIX-24 through FIX-28 pass with their gates visible. The hole
was real and unlucky in exactly two places, and the honest report is smaller than the fear
was.

**That the check the brief called "the check the rewrite needed" would not have caught the
rewrite.** Self-retrieval passes on the broken state. A row's own questions almost always
find it, because they are its own words. The check that found the damage is the one that
compares against what the questions used to be — and that one cannot be permanent, because
its baseline rots. The permanent successor is noun coverage: read the page-derived fields
and name every significant word the questions never use. It is not built, and it is named
here rather than quietly skipped.

**That `pipefail` alone would have been the wrong fix.** It turns `head` into a failure.
Had I added it and stopped, the build would have gone red for a reason unconnected to any
gate, and the next person would have learned to ignore it.

## What I got wrong

**I nearly repaired a row into breaking another.** Adding "when must a student cite ai use"
to Cornell's integrity page pushed *Referencing AI and Acknowledging AI Use* out of the top
three. The new CLAUDE.md line settled it in one step — fixed or reverted, never explained —
and I reverted it. Without that line I would have written a paragraph about competing rows.

**A repair of mine dropped a word while restoring another.** "the four competencies of ai
fluency" became "the 4d framework of ai fluency", which put `4d` in and took `four` out. I
only caught it because I re-ran the detector after applying, which I nearly did not.

**My first bite test asserted the wrong thing** — that a fault would be caught by the file
that tests the rule rather than by the file that enforces it. The run told me, which is
what a bite test is for, but the expectation was written from memory rather than from the
code.

## Whether it was in CLAUDE.md

The two lines added this round are the answer, and they were not there before. Neither was
anything close: the file said *verify before claiming done: run it, open it, check the
links*, and I did run it. What was missing is that running a check proves nothing unless
the check can fail.

The typed counts in THE-PROJECT part 11 **were** covered, exactly: *numbers anywhere a
reader will read them are generated or measured, never typed*. The rule has existed since
August, `check-typed-numbers.py` enforces it for pick reasons, and `docs/` has never been
inside any check. That is the same shape as this round's headline — a rule with no gate
behind it — and it is now the obvious candidate for the next one.

Shell hygiene held for the code. It did not hold for this file: the round record went
through a heredoc, the heredoc died on an unmatched quote, and it was written with the file
tool instead. That is the CLAUDE.md rule working exactly as written, and the second round
running that I have needed it.

## Next

Attack 3 is coming and nothing in this round was written to make it easier. Search, tags,
levels, collections, `questions[]`, the date lines and the picks block have all changed
since Attack 2, and the failure table, the gap candidates and amendments 6 and 7 are all
written down where an attacker will find them.
