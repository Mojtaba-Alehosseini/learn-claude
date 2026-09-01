# Fix prompt — "start with these three", and one small bug

Paste everything below the line into Claude Code, in the project folder.

---

Seven paths, all ten roles, 618 clean. And you found a real bug in shared code and left it
alone because it was outside the job — that is the right instinct and I want it kept. It
is job 2 below.

The thing you wrote about generalising: *"I had the pattern in hand and didn't generalize
from it into a check; I kept manually re-discovering individual instances."* That is the
sharpest self-criticism this project has produced. It is also the exact risk in job 1.

---

# Job 1 — 618 resources, and no order inside them

Answer "not a coder" and "used it a little" and Browse returns **70 cards**, in whatever
order the file happens to be in. Every card carries a good `Skip if` line, and none of
them says *open this one first*.

The site's promise is judgment. Right now the judgment is per-item and nothing is
comparative.

## The reframe, and it matters

**Do not call this "the best".** We cannot judge quality: 78% of the catalogue is
`previewed`, meaning we read an outline. Ranking those by quality would be inventing a
claim, and inventing claims is the one thing this site does not do.

What we *can* judge is **fit and order** — which three a person in this situation should
open first. That is the same judgment the seven paths already make, applied to a filter
result instead of a sequence. So the label is **"Start with these three"**, never "best",
never "top rated".

## The shape

40 cells: 10 roles × 4 levels. Measured just now — **37 need a decision**, 2 have three or
fewer candidates, and `student` + `builder` is empty.

Output goes in `data/picks.json`, keyed by `role|level`, **referencing steps by URL, never
by id.** You know why: the path id corruption came from list-position ids and cost a
rebuild.

## How the choosing works — follow this, do not improvise

**Step 1 — deterministic pre-filter. No model.**

- role in `roles`, `level` matches exactly
- `status == "live"`
- drop `tier == "listed"` — nobody has looked at it, so we cannot recommend it
- drop anything the freshness rule already flags as out of date

Cheap, auditable, and it means the model never gets to launder a resource nobody checked.

**Step 2 — Opus 5 picks 3 from the survivors.**

Give it, for each candidate, exactly what a reader sees on the card: title, publisher,
format, time, cost, tier, `who_for`, `skip_if`, `teaches`, published date, checked date.

**Tell it plainly, in its own prompt, that it is not looking at the resource.** It is
ranking our notes about the resource. A model that thinks it read the thing will write
confident sentences about content it never saw.

**Step 3 — every pick carries one sentence: why this one and not the other 67.**

Not what the resource is about — the card already says that. *Why it beat the pool.* This
sentence ships on the card, so it is held to the same bar as `skip_if`: if someone who read
the title would already know it, it is not doing work.

**Step 4 — three hard constraints on the set of three.** Check them in code after the
model answers, and reject and re-ask if they fail:

1. **No two from the same publisher.** Without this, designer gets three Claude Design
   tutorials — the exact failure you documented and rejected twice.
2. **At least one non-Anthropic**, whenever the pool contains one. 61% of the catalogue is
   official; if that becomes 100% of the picks, the site is an Anthropic shopfront with a
   directory bolted on.
3. **Different formats where the pool allows it.** A video, a doc and a course beat three
   docs.

**Step 5 — record what it rejected.** Two or three runners-up and one line each on why
they lost. Stored, not displayed. Without it, "we picked these" is unfalsifiable, and an
unfalsifiable claim on this site is worse than no claim.

**Step 6 — label the pick, because that is what this site is.**

`picked_by: "ai"`, `picked_on: <date>`, and the UI says so in the reader's words. Same
honesty ladder as the tiers. **Nothing may imply a person chose.** A human promotion path
can come later; the allowance for it starts at 0, like `reviewed`.

**Step 7 — make it go stale honestly.** Store a fingerprint of the eligible pool per cell.
When the pool changes, the picks for that cell are stale and the build says so. Otherwise
this rots silently, which is how the path ids rotted.

## What the reader sees

On Browse, only when **both** role and level are set — which is exactly where the two
front-door questions land:

```
Start with these three            [ picked by AI · 29 August 2026 ]
  <card>  <card>  <card>          each with its one-sentence reason

Everything else for you (67)
  <the rest, as now>
```

The others stay. Nothing is hidden, nothing is removed. If a cell has three or fewer
candidates, show them with no picks block — three out of three is not a judgment. If a
cell is empty, say so plainly, the way the paths page already does for a role with no path.

## The generalising point

You said you kept re-discovering instances instead of writing the check. The same trap is
here: 37 cells is enough that hand-picking a few and calling it done would pass a casual
read. Build the pipeline, run it over all 37, and let the constraints in step 4 fail loudly
rather than smoothing them over by hand.

---

# Job 2 — the `lstrip` bug you found

You were right, and it is live in the catalogue today. `lstrip("www.")` removes any
leading run of `w` and `.` characters, not the literal prefix:

```
weather.com     -> eather.com
wotai.co        -> otai.co
w3schools.com   -> 3schools.com
```

Five hosts we hold are being mis-trimmed right now: `warwick.libguides.com`,
`westmoreland.libguides.com`, `willfrancis.com`, `wotai.co`, `www.wrightmode.com`.

It is in two places, not one — `scripts/check-links.py:82` and
`scripts/validate-catalogue.py:408`. Fix both, and put the fix in one shared helper rather
than correcting the same line twice; two copies of a host-normaliser is how `norm()` ended
up with three definitions and a bug in each.

Add a test with `weather.com` in it. Nothing currently breaks because of this — the
collisions happen not to land — and "harmless by luck" is precisely the kind of thing that
stops being lucky the week you add a host beginning with W.

---

## Not yours

Still mine: the email address, and that nothing is `reviewed`. Do not start either.

## Then

Commit job 1 and job 2 separately. For job 1, show me three cells before you run all 37 —
`designer` + `basic` (10 candidates), `non-technical` + `basic` (70), and
`business-founder` + `builder` (78). If the reasons are weak at those three sizes they will
be weak everywhere, and I would rather stop at three than read 37.

Finish with what surprised you and what you got wrong.
