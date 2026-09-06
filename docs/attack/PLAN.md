# Attack plan — 10 roles, 10 files, 1 summary

A long job. This file exists so that nothing is invented, nothing is confused, and
nothing is skipped. Read it before each batch and again before the synthesis.

## The rule that matters most

**No number may be invented.** Every figure comes from one of three places:

1. `docs/attack/00-facts.md` — already measured, authoritative
2. a command run in this session, with the command shown
3. the live site, opened in a browser

If a claim has none of those behind it, it does not go in the file. "Probably",
"likely", "seems" are banned in findings. They are allowed in the *opinion* section, and
only there.

## The 10 roles — fixed, in this order

| # | role key | shown to a visitor as | resources |
|---|---|---|---|
| 1 | `non-technical` | not a coder | 68 |
| 2 | `student` | a student | 41 |
| 3 | `researcher` | a researcher | 41 |
| 4 | `teacher` | a teacher | 47 |
| 5 | `developer` | a developer | 94 |
| 6 | `data-analyst` | working with data | 37 |
| 7 | `pm` | a product manager | 56 |
| 8 | `designer` | a designer | 29 |
| 9 | `business-founder` | running a business | 54 |
| 10 | `writer-marketer` | a writer | 41 |

Ten. Not nine, not eleven. Tick each one off in the tracker below as its file lands.

## What each agent does

One agent per role. It is **that person**, not a reviewer being polite. It wants to
learn Claude today, it has an hour, and it is unimpressed. It must be hostile — a
finding that flatters the site is worthless here.

It does all of this:

1. Opens `https://mojtaba-alehosseini.github.io/learn-claude/` and answers the two
   questions honestly as that role, at **every one of the four levels**.
2. Follows through to Browse. Reads the actual cards it is given — titles, `Skip if:`,
   dates, badges.
3. Opens Paths. Is there a route for this person? Follows one if there is.
4. Opens two or three resource pages and judges whether it would click through.
5. Searches the way this person would phrase it — three real sentences in their own
   vocabulary, not keywords.
6. Looks at the whole thing on a phone-width viewport.

## What each agent writes

Fixed path: `docs/attack/NN-<role>.md`, e.g. `docs/attack/08-designer.md`.

Fixed sections, all of them, in this order. An empty section is written as "nothing
found" — it is never deleted, because a missing section reads as a skipped step:

```
# Attack: <role shown to a visitor>
Written as someone who is <role>, at <date>. Site version: <git short sha>.

## 1. The first 60 seconds
## 2. Does the front door work for me       (all four levels, with counts)
## 3. What the catalogue actually gives me  (are these really for me?)
## 4. Paths
## 5. The card and the resource page
## 6. Search, in my words
## 7. On a phone
## 8. Content quality — the three worst entries I was shown, quoted
## 9. Everything that is broken, ranked                (evidence for each)
## 10. The one thing that would make me leave and not come back
## 11. What is genuinely good                          (be honest, but brief)

## Checklist — every line ticked or the file is not finished
- [ ] I opened the live site
- [ ] I tried all four levels
- [ ] I quoted at least 5 real titles or lines from the site
- [ ] Every number I used is in 00-facts.md or I show the command
- [ ] I looked at a phone width
- [ ] I found at least one thing nobody has mentioned before
```

**Agents find. Agents do not fix.** No edits to any file outside `docs/attack/`.

## The suite, and why an agent may not see it

`scripts/test-search.py` holds every search query this project has ever been judged on,
with the verdict each one got. **An attacking agent is never shown it, never told it
exists, and never reads a file under `scripts/` or `data/`.** It types what its role would
type, at the live site, and reports what it got.

That is not politeness. It is the only reason the number means anything.

The suite is the instrument the search work is steered by. Every query already in it has
been read, argued over and in some cases had a card rewritten around it. A query written
by somebody who has seen the suite is a query written to pass. FIX-29 found exactly that
in the catalogue's own `questions[]` field - it had been written by somebody who had read
the test - and the honest rewrite made the number fall before it rose.

**So every query an attacker types is a hold-out**, in the strict sense: written without
sight of the instrument, judged on what the live site returned, and only afterwards added
to the suite with the verdict its author gave it. The suite grows by exactly the queries
it could not have anticipated.

**The number will drop when they are added, and that drop is the honest new baseline.**
A suite that only ever grows by queries the site already answers is a suite measuring its
own reflection. Report the number before and after the additions, and never quietly hold
a failing query out.

Two rules follow from this and both are load-bearing:

- **The agent's verdict is the verdict.** Not re-graded later to make a number better. If
  a round disagrees with an agent, it argues in the suite row's reason and keeps the
  agent's original answer beside its own - see the accepted-answers note in
  `scripts/test-search.py`.
- **No check inside the build can replace this.** `scripts/check-self-retrieval.py` asks
  every row its own questions, and it passes on a catalogue whose questions have just been
  damaged - measured against the state FIX-30 pushed with eight suite queries broken, it
  reported nothing. A row is very good at finding itself with its own words. Only a
  stranger's words find out whether the words are right.

## Running order

Two batches of five, so nothing overloads and I can check the first five before
committing to the rest.

- Batch A: non-technical, student, researcher, teacher, developer
- Batch B: data-analyst, pm, designer, business-founder, writer-marketer

After each batch: confirm all five files exist, have all 11 sections, and have a
completed checklist. **A file that fails this is re-run, not patched by hand.**

## Then the summary

Read all ten files. Write `docs/attack/SUMMARY.md`:

- What every role hit — a problem 8 of 10 people have is structural, not a detail
- What only one role hit, where it is severe enough to matter anyway
- The findings ranked by how much they cost a real visitor, not by how easy they are
- Anything the ten files disagree about, named as a disagreement rather than averaged
- What is genuinely good, so it does not get refactored away later
- The decisions that are Morteza's and not mine

Then verify: every claim in the summary traces to a numbered finding in one of the ten
files. A summary point with no parent is deleted.

## Tracker

| # | role | file written | 11 sections | checklist done |
|---|---|---|---|---|
| 1 | non-technical | 01-non-technical.md | 11/11 | yes |
| 2 | student | 02-student.md | 11/11 | yes |
| 3 | researcher | 03-researcher.md | 11/11 | yes |
| 4 | teacher | 04-teacher.md | 11/11 | yes |
| 5 | developer | 05-developer.md | 11/11 | yes |
| 6 | data-analyst | 06-data-analyst.md | 11/11 | yes |
| 7 | pm | 07-pm.md | 11/11 | yes |
| 8 | designer | 08-designer.md | 11/11 | yes |
| 9 | business-founder | 09-business-founder.md | 11/11 | yes |
| 10 | writer-marketer | 10-writer-marketer.md | 11/11 | yes |
| — | SUMMARY.md | SUMMARY.md | n/a | 161 citations, 0 broken |

## Already known — do not present these as new

**This list is refreshed every round, and the refresh is part of the round.** It was not,
once. Attack 3 ran with the Attack 1 version still here - "4 roles have no path", "0 of 353
are reviewed", "171 of 353 have no publish date" - and a designer checked, found seven
paths, and reported the briefing as stale. An attacker correcting its own instructions is
the method working and the plan failing. **Refresh this list and `00-facts.md` together, or
neither.**

The current list lives in [`00-facts.md`](00-facts.md) under "Already known", where it sits
beside the figures that date it, rather than here where it aged for two rounds. An agent
may confirm or sharpen anything on it; the value is in what is *not* on it.
