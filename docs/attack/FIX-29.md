# Fix prompt — finish the sweep, then the two causes that dominate search

Paste everything below the line into Claude Code, in the project folder.

---

+3, not +12, and you found it yourself against your own earlier report. That is the
method. The failure table says the remaining 23 are mostly two things — the reader's
words, and holes in the catalogue — and neither is a scoring mechanism. This round
works on those two, after the sweep is finished and one habit gets a guard.

# Rulings

1. **The 12 removals — approved, with one door.** Open each page once more. A page that
   teaches a generic Claude skill — prompting, files, projects, checking output —
   through an off-roster job's example is for "not a coder": keep it, tag
   `non-technical`, rewrite the card to say what it teaches rather than whom it was
   written for. A page that is that job's own workflow is out of scope for the ten
   readers: remove it, and log title, URL, publisher, tier, and `skip_if` in
   `research/out-of-scope.md` so it can return if the roster ever changes. Expect most
   to be removed.
2. **A situation is not an occupation.** Fix Rule B before finishing it: "complete
   beginners", "someone who has just been cut off", "anyone about to trust Claude" are
   situations and must not fire. Then finish the sweep under the same checkpoint rule.
3. **Commit messages carry no counts.** Three rounds, same failure, and the rule names
   commit messages by name. Add a `commit-msg` hook: a number beside a count word —
   rows, queries, items, cells, "of N" — rejects the commit. Ids, dates and hashes
   pass. The numbers live in the round record and STATUS.md, both generated. Add one
   line to CLAUDE.md under Working rules: *Commit messages describe the job. Counts
   live in the round record.*

# Cause 1 — the reader's words

Nine failures are rows whose indexed fields do not use the words a person typed.
`questions[]` is the field built for exactly this, at weight 5, and it was written in
our words.

- **Rewrite `questions[]` across the catalogue** in a reader's words: three to five
  per row, phrased as someone would type them into a box — *is claude free*, *make
  claude remember my stuff* — no product names the person would not know yet, no
  jargon the card itself had to define. The writer works from the card and the page
  only.
- **The writer is blind to the suite.** Do not open `test-search.py` while writing.
  Then the validator enforces it: no suite query may appear verbatim in any
  `questions[]` field. A pass earned by copying the test is not a pass.
- **Checkpoint at ten rows.** Show me the ten before running the rest — if the
  questions read like our copy in a different font, stop.
- Add the synonym rows the table named — feedback, email, customer, and whatever else
  it lists — each with its reason.
- Measure: top three, same accepted answers, before and after. Report per role.

# Cause 2 — the holes

Ten queries fail because the catalogue holds nothing. That list is in STATUS.md, and
it is the first harvest with an acceptance test.

- For each of the ten: walk the indexes of the publishers most likely to hold an
  answer — the August research files, the Help Center map, the YouTube metadata path
  that works — and bring back one to three resources that answer it. Every harvest rule
  stands: URL opened, `date_source`, tier honest, `skip_if` at the bar, page's own
  title, publisher gate, no invention. A question with no honest answer after a real
  walk stays a content gap, and the record says which publishers were walked.
- Each new row's `notes` names the question it was harvested to answer.
- Measure again, same footing. A harvested row that does not surface for its own
  question in the top three is a finding, not a failure to hide — record it.

*(Veto point: the content-gap list was mine to decide on. This decides it. Delete
this section to hold it.)*

# Order and measurement

Sweep → guard → questions rewrite → synonyms → measure → harvest → measure. The suite
number appears three times in the round record: after the sweep, after cause 1, after
cause 2. Gate per commit, as the spec says. Pools move twice; the stale machinery
fires twice; re-pick what it names each time.

# Not yours

STATUS.md "Needs a person" and part 10. The human test.

# Commits

The 12, the situation fix, the rest of the sweep, the hook and the CLAUDE.md line, the
questions rewrite, the synonyms, the harvest, the re-picks — one job each. `FIX-29.md`
with the round. Push. Finish with what surprised you, what you got wrong, whether it
was in CLAUDE.md — and the three suite numbers.

---

# The round, as run

## The three suite numbers

| point | suite |
|---|---|
| where the round started | 35 of 57 |
| after the sweep | 35 of 57 |
| after cause 1, the reader's words | 36 of 57 |
| after cause 2, the holes | **38 of 57** |

Every figure is that commit's own suite, ranker and index, graded on the top three.

| role | after | content gaps |
|---|---|---|
| business-founder | 4 of 6 | 0 |
| data-analyst | 2 of 5 | 1 |
| designer | 5 of 7 | 2 |
| developer | 4 of 7 | 0 |
| non-technical | 4 of 5 | 0 |
| pm | 3 of 7 | 4 |
| researcher | 4 of 5 | 0 |
| student | 4 of 5 | 0 |
| teacher | 4 of 6 | 0 |
| writer-marketer | 4 of 4 | 0 |
| **total** | **38 of 57** | **7** |

## The sweep

Rule B now reports zero rows carrying a tag their card denies and zero fitting no role,
across the whole catalogue rather than the gallery alone.

The twelve held at FIX-28's checkpoint went through the door the ruling opened. Two teach a
generic Claude lesson through an off-roster job's example - a four-step Cowork setup shown
on a sales call brief, and retrieve-analyse-produce shown on an investment memo - and are
kept, tagged `non-technical`, with cards rewritten to say what they teach. The rest are the
job's own workflow and are in `research/out-of-scope.md` with their address, publisher,
tier and skip line, so a roster that ever gains a clinician or an investment analyst can
bring them back without redoing the reading. The file now holds 12 rows.

Reading the remaining rows found five patterns matching inside another word - `developer`
in "Non-developers", `coder` in "medical coders", `researcher` in "UX Researcher", `owner`
in "design-system owners" - every one of them deciding rows in the branch that REPLACES a
card's tags. Four are guarded and tested; the fifth, "a teacher used to explaining tooling",
is the author of a course rather than its reader, and no pattern can see that, so those rows
are left alone with the reason written down.

`scripts/test-role-buckets.py` holds the ruling's own three situation examples and six
occupations that must still route to Rule C. A guard loose enough to call everything a
situation would pass the first half of that test and quietly stop the sweep working.

## The guard

`scripts/commit-msg.py` rejects a commit message that states a count. It caught its own
first message - which quoted its test strings - and found its own false positive on day
one: "one" is an article far more often than a quantity, so it no longer fires the
adjacency patterns and stays in the ratio shape where it is unambiguous. CLAUDE.md gains
the line.

## Cause 1, the reader's words

The questions rewrite is at its checkpoint. The sample is written and applied, chosen by a
deterministic spread across roles and levels rather than from the failure table, because
picking the failing rows first would be the suite writing the questions by the back door.
The rest of the catalogue waits, because the ruling says show the sample first and that
judgement is not mine to make about my own writing.

I am not blind to the suite and cannot be: I have read it many times this session. The
guard is therefore mechanical - `scripts/check-questions.py` refuses any question that is a
suite query once case, punctuation and spacing are stripped - rather than a claim about my
memory.

The synonym rows the table named were added and did nothing, and the reason is a design
fault this round inherited. FIX-27 gave synonyms the same shape as stems: half weight,
ranking only, never admitting. Every vocabulary failure in the table is a row containing
none of the reader's words, and a rank-only expansion cannot surface a row that is not in
the results. A synonym now admits, and "marking essays" reaches the row that answers it.

## Cause 2, the holes

Two rows harvested from the Claude Code docs - the hooks guide the reference tells you to
read first, and the settings page that defines allow, ask and deny. Both fetched and read
in full, both `ai-reviewed`, both `UNVERIFIED` for date because neither page prints one,
and each row's notes name the question it was harvested to answer.

**"em dash" was never a content gap.** Wikipedia's Signs of AI writing, which this
catalogue has held all along, has a section headed "Overuse of em dashes". The answer was
on the shelf and the card never used the words. The previous round classified it wrong.

Two walks came back empty and say so: the Help Centre's Claude-in-Excel articles hold no
pivot tables, and the Academy's Product department holds neither roadmap nor stakeholder.

And the finding the ruling asked for rather than hid: the harvested hooks guide does not
surface for the question it was harvested to answer. It is sixth; the reference is first.

## Still open

- The questions rewrite, waiting on the checkpoint.
- `data-analyst`, unmoved all round.
- Typography and "will ai design replace me", not walked.
- The vocabulary failures the questions rewrite is for.
