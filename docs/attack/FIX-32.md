# Fix prompt — three rulings, then Attack 3

Paste everything below the line into Claude Code, in the project folder.

---

Two rounds green on red, one shipped, and now the build can see itself fail. That was
the right round to run before this one. Three rulings first, small, then the attack.

# Rulings

1. **The index budget is a measurement, not a figure.** 166 KB against a typed 150.
   Measure what a reader feels: time from first keystroke to first result on a
   throttled phone connection, in the browser, three runs. Restate the budget in the
   spec as that time and the size that produced it. Do not cut content to satisfy a
   number nobody measured. If the time is bad, say what would be cut and stop there.
2. **The suite is the instrument, and attackers are its blind set.** Self-retrieval
   stays as a warning — it catches a row that cannot describe itself — but the record
   says plainly it cannot see a rewrite. Attack agents never see `test-search.py`;
   every query they type is a hold-out, and every one joins the suite afterwards with
   its verdict. Write that into the attack method file.
3. **`docs/` gets a gate.** The typed-number check reaches `THE-PROJECT.md`,
   `README.md`, `START-HERE.md` and `docs/specs/`. A count on a line that carries a
   month or a year is history and passes; a count on a line without one is a live claim
   and fails. Fix what it finds by pointing at STATUS.md. The round records under
   `docs/attack/` are dated by construction and stay out of it.

# Attack 3

**Reuse the method.** Read `docs/attack/PLAN.md`, `RUN.md`, both `RUN-LOG` files and
`docs/attack/2/SUMMARY.md` before writing anything. Refresh `00-facts.md` from
STATUS.md. Ten agents, one per role, four levels each, the live site, their own words,
no knowledge of the data model, the rules, the suite, or this brief.

**A finding is a claim.** URL, what was done, what was seen, what was expected, whom it
harms. Nothing unreproducible is filed. Severity by reader harm.

**What changed since Attack 2 — every agent spends real time here:**

- **Tags and levels.** "Built things with it" now means building. Does the level
  filter return people like them? Does "not a coder" still return other people's
  jobs?
- **The five collection cards.** Sales, legal, HR, finance, operations. Does a founder
  understand what one is before clicking? Does anyone else trip over them?
- **Search, in their words.** Five queries per agent, typed cold, top three judged.
  Then the same question asked two different ways — does the site agree with itself?
- **The stripped cards.** Three `listed` rows now carry a title, a link and one fixed
  skip line. Do they read as honest or as broken?
- **"How well checked" as a filter**, and the tier definition reachable from a card.
- **The thin-level offer.** `teacher` + `builder`: does the one-click line make sense,
  and does the reader take it?
- **Date lines.** Published, Updated, month-only, "over a year ago" beside the date.
  Does the site look maintained?
- **Price chips** on the four paid rows, and the cost chip beside them.
- **"Who we is."** Does naming one person and Claude raise trust or lower it?
- **The picks block after re-picks**, and its two-pick and empty-cell sentences.

**The four deferred from Attack 2, now in scope:** the social preview title, the home
attract loop, the sort semantics, and paths above beginner level. Each agent tries
what a real visitor would: share a link, watch the home page, change the sort, look
for a path at their level.

**One closing question per agent, answered in their own words:** would you come back
to this site, and what one thing would make you? Verbatim into the findings.

# Regression sweep

Attack 2's summary lists 30 findings and 15 decisions. Re-test every one rated high and
every decision that was built: finding, fixed in, still fixed today. Add Attack 1's
five policy findings that Attack 2 said were undecided — they are decided now; confirm
the site agrees.

# Output

- `docs/attack/3/01-…10-….md`, `SUMMARY.md` with findings deduplicated and ranked,
  then two lists — mechanical and decisions; `REGRESSION.md`; the closing answers
  gathered in `SUMMARY.md` under their own heading.
- Every agent query joins the suite with its verdict. Report the suite number before
  and after the additions — it will drop, and that drop is the honest new baseline.
- Fix the mechanical list directly, one commit, every change logged. Do not touch the
  decisions.

# Not yours

STATUS.md "Needs a person" and part 10. The human test — and if ten agents' closing
answers say the same thing, that is the first task for the three real people.

# Commits

The three rulings, the facts refresh, the attack files, the suite additions, the
regression sweep, the mechanical fixes — one job each. `FIX-32.md` with the round.
Push. Finish with what surprised you, what you got wrong, whether it was in CLAUDE.md —
and which single finding you would fix first if you were me.

---

# The round as run

## The suite number, before and after the additions

| role | before Attack 3's queries | after |
|---|---|---|
| business-founder | 4 of 6 | 7 of 11 |
| data-analyst | 5 of 5 | 8 of 10 |
| designer | 7 of 7 | 11 of 12 |
| developer | 5 of 7 | 10 of 12 |
| non-technical | 5 of 5 | 8 of 10 |
| pm | 7 of 7 | 9 of 12 |
| researcher | 4 of 5 | 9 of 10 |
| student | 5 of 5 | 9 of 10 |
| teacher | 4 of 6 | 7 of 11 |
| writer-marketer | 4 of 4 | 6 of 9 |
| **total** | **50 of 57 — 88%** | **84 of 107 — 79%** |

**Nothing broke.** The build is green, no `ok` query regressed, and the fifty new rows all
entered with the verdict their author gave them. The proportion fell because the instrument
stopped being graded only on questions it had been tuned against, which is what a hold-out
set is for. **79% is the honest baseline.** Four roles that read 100% before read 90% or
less now, and the two that fell furthest — writer at 67%, business owner at 64% — are the
two whose vocabulary is furthest from the catalogue's.

---

## The three rulings

### 1. The index budget is a measurement now

Measured in the browser on the live site rather than typed into a spec. Amendment 8.

| | |
|---|---|
| bytes the server sends for the index | 176,934 (`encodedBodySize`, compressed) |
| typing pause before anything runs | 150 ms, from `browse.js` |
| parsing the index | 26 ms cold, 4 ms warm |
| keystroke to results, index loaded | 159, 164, 164, 166, 159 ms over five queries |
| ranking and redrawing 588 rows | 9–16 ms |
| first keystroke of a session, modelled slow 4G | **≈1.2 s to a ranked answer** |

**The budget is: under 1.5 s to a ranked answer on the first search of a session, and under
200 ms on every keystroke after it.** Both met. The size is recorded as what produced the
time. Nothing was cut, and the file names the phrase map as the lever if the time ever goes
bad — so that nobody reaches for the catalogue's content instead.

**Measuring it found something the size never would have.** Until the index lands the page
falls back to substring matching. Over twelve suite queries the fallback's top result
**differs from the ranked one eight times and shows an empty page five times** — "grading",
"write emails for me", "make a lesson plan", "how much does claude cost" and "can claude
read my csv" all render *0 resources* for about a second before the answer arrives. Recorded
in the spec, not fixed: choosing between a spinner, a held render and a tiny always-loaded
first-pass index needs evidence about what readers do.

### 2. The suite is the instrument; attackers are its blind set

Written into `PLAN.md` as its own section. An agent never sees `test-search.py`, never opens
`scripts/` or `data/`, and every query it types is a hold-out that joins the suite afterwards
with its author's verdict. All ten confirmed the restriction in their checklists.

`check-self-retrieval.py` now says in its own header what it cannot see, with the
measurement behind it: run against the exact catalogue FIX-30 pushed with eight suite
queries broken, it reported nothing.

### 3. `docs/` has a gate

`check-typed-numbers.py` reaches THE-PROJECT.md, README.md, START-HERE.md and `docs/specs/`,
on the rule as given: a count on a line carrying a month or a year is history and passes; a
count on a line without one is a live claim and fails. Round records stay out — dated by
construction.

It found **60 lines**. The live documents now point at STATUS.md; the specs say when their
figures were true. It also caught THE-PROJECT warning that START-HERE is stale about numbers
START-HERE no longer carries. `test-gates.py` plants a live count in a document and watches
the build go red.

**One judgement inside it, and it is mine to defend.** The check is scoped to the quantities
the build measures and writes into STATUS.md. The site's fixed vocabulary — "four levels",
"ten roles", "the two front-door questions" — is deliberately out, because a gate that
demanded a date beside "four levels" would teach people to ignore it. That narrowing is
argued in the file's header and it is yours to widen.

---

## Attack 3

Ten agents, two batches of five, each on its own browser tab, none allowed to read
`scripts/` or `data/`. Full findings in `docs/attack/3/`; the summary ranks, dedupes and
splits mechanical from decisions.

### The finding that is really one finding

**The site cannot be shared. Ten of ten.** Every resource page serves
`<title>Resource — Learn Claude</title>` and the same `og:title`; Browse and Paths serve one
constant each; there is no `og:image`, no `og:url`, no canonical. The per-page title is
written by JavaScript, which no crawler runs. **Every one of those pages carries a "Copy
link" button.**

Ten strangers, an hour each, no instruction to look at metadata, and all ten found it. Four
called it their worst finding. Three named fixing it as the one thing that would bring them
back. On a site with no analytics, no accounts and no newsletter, one person sending another
person a link is the entire distribution mechanism, and the preview at the end of it says
nothing.

### What most roles hit

- **Search does not agree with itself** — seven of ten. The wording that fails is always the
  plain-English one. The teacher isolated it to one word: `pupil` returns nothing, `student`
  returns thirty-six, and inside a sentence the other words rescue the query into twenty
  confident wrong results with no signal that it failed.
- **"Newest first" was not** — six of ten, five roles, and three noted independently that
  "Shortest first" is correct, so the machinery worked and one label lied.
- **The tier badge is undefined on a phone** — seven of ten.
- **Nothing paid says what it costs** — eight of ten.
- **The level ladder runs out a rung early** — seven of ten, with the shape named per role.

### What one role hit that matters anyway

The false empty state (`?role=X&checked=reviewed` → "We have not covered this role yet"), a
pick reason quoting a sentence its card does not contain, path pages throwing away the
`Updated` date, the writer's own path ending on superseded guidance with the current
document in the catalogue unlinked, and 16 of 34 cards on the analyst's shelf chipped `free`
while naming paid subscriptions.

### Where the agents were wrong

Three claims are right as observations and wrong as faults, and acting on them would make
the site worse. **The missing prices are a rule** — a price is stored only where the page
prints the same number for every reader — which eight agents hit and none could discover.
**The mouse-only badge is half true and deliberate**, trading a sighted phone reader's
tooltip for the single-focus-stop card seven Attack 2 agents praised. **And "four roles have
no path" was stale — that one is mine**, left in `PLAN.md`'s already-known list from Attack 1
while I refreshed `00-facts.md` beside it. A designer had to correct the briefing it was
given. The list now lives beside the figures that date it.

### The closing answers

Ten yeses, and **not one of them is a yes to the site.** Every answer names a bookmark, a
cell, a page or a shelf: *"a raid not a home"*, *"one page, not the site"*, *"for the path,
and only that"*. Gathered verbatim in `SUMMARY.md §8`.

---

## The regression sweep

All thirteen of Attack 2's mechanical fixes hold. Every built decision is where it was left.
Attack 1's five policy findings are settled — including the named-individual allegation,
which is gone from the catalogue.

**The value was in three findings a tick-box would have passed**, because all three
originals are genuinely fixed:

- **M1 was fixed on one surface of three.** The resource page renders the `Updated` date;
  `paths.js` never did.
- **M13's validator catches one sentence of a family.** It refuses a reason claiming
  non-Anthropic when the card says Anthropic. It does not refuse a reason that invents
  *"thirteen reviews"*, and one shipped.
- **D10 added an axis and left a guard behind.** The tier filter went in; the function that
  reasons about which filters are set was not told.

All three are the same shape — **verified where the bug was reported and nowhere else** — and
that question is now written into the next sweep's method.

---

## The mechanical fixes

One commit, each logged in `docs/attack/3/MECHANICAL-LOG.md` with what a reader saw, the
cause, the change and what was verified.

| # | What |
|---|---|
| M1 | `anyOtherThanRole()` now counts the tier axis, so a role plus that filter stops denying the role exists |
| M2 | `sortDate` is the later of `published` and `updated` |
| M3 | Path steps render `updatedNote`, like the other two surfaces |
| M4 | The `pm|builder` reason says what its card says |
| M5 | Two pick reasons stop printing the build's own vocabulary |
| M6 | A student/pupil/learner synonym row — and the flattener bug it exposed |

**M6 is the one worth reading.** The row did nothing at first: the index builder dropped any
term the catalogue had never seen, *including as a key*, and `pupil` appears nowhere — which
is the entire reason to have the row. The rule was right about targets and wrong about keys.
Fixed, `pupil` alone goes from **0 results to 42** with the right card second; inside the
teacher's original sentence the correct card moves from **15th to 12th** — better, and not
fixed. A synonym scores at half weight and cannot outrank the reader's other literal words.
That is spec amendment 7, written down last round, and it is not tuned here.

**Two reported faults were deliberately not changed.** The attract loop does exactly what
its own source comment says — it cycles the drawing, which is the only hint the underlined
words are buttons — and whether the sentence should preview a role too is a design decision.
The `<h1>` exists and comes first; which element carries the visual weight is typography.
Reading the source before editing it kept both out of the commit.

---

## What surprised me

**That ten independent readers converged on metadata.** I would have bet on search or on the
thin levels. Instead every one of them, unprompted, found the same four hard-coded strings —
and the designer closed it by noticing the Copy link button sitting on every page it breaks.
A directory's product is judgement; its distribution is a pasted link; and the thing that
carries the judgement into the link was never built.

**That the synonym row did nothing when I added it.** I shipped the data, tested the query,
and the number had not moved. The flattener was discarding the reader's word precisely
because the catalogue lacks it. If I had trusted the mechanism instead of testing the
outcome, the round record would have claimed a fix that did not exist.

**That reading the source disqualified two findings.** Eight agents called the attract loop
broken and its own comment says what it does. That is the value of the "where the agents were
wrong" section, and this round it saved two changes that would have been wrong.

## What I got wrong

**I refreshed `00-facts.md` and left `PLAN.md`'s already-known list at Attack 1.** Ten agents
were briefed with "4 roles have no path" when there are seven. A designer checked and told
me. An attacker correcting its own instructions is the method working and my preparation
failing.

**I put a regex through a heredoc again, and it silently corrupted the file.** `\b` inside a
non-raw Python string in a heredoc is a backspace character, not a word boundary, and the
docs gate reported zero offences for a run because its pattern ended in a control character.
CLAUDE.md has a rule for exactly this — write the script to a file and run the file — and
this is the third round I have broken it. The pre-commit control-character check would have
caught it at the commit; the measurement was wrong for several minutes before that.

**I nearly shipped M6 as done.** See above.

## Whether it was in CLAUDE.md

**The heredoc fault is in CLAUDE.md, word for word**, and I broke it again: *"never put a
regex or a backslash through a heredoc — write scripts to a file and run the file."*

**The M6 near-miss is covered too**: *"Verify before claiming done: run it, open it, check
the links."* Adding the row and not re-running the query would have been exactly that.

**The stale briefing is not in CLAUDE.md and something like it should be.** The rule the
round earned is in `PLAN.md` rather than the project file, because it is specific to the
attack method: *refresh the already-known list and the facts file together, or neither.*

---

## Which single finding I would fix first, if I were you

**The share chain.** Not because ten of ten found it — because of what the closing answers
say when you read them together. Every reader said yes, and every one of them named a
bookmark rather than the site. That is a directory being used as a folder. The one mechanism
that turns a folder back into a place people arrive at is somebody pasting a link where
other people can see it, and right now that link says nothing.

It is the largest thing in the summary and the only one that needs a build step — one served
HTML file per row, or a pre-render, with the `For:` line as the description. Everything else
in the ranked list makes an existing visit better. This is the only one that makes a visit
happen.
