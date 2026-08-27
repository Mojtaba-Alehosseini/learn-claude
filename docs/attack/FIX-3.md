# Fix prompt — the "Anyone" bucket, then the four missing paths

Paste everything below the line into Claude Code, in the project folder.

---

Good judgment on the last one — the seven verdicts read like decisions, not a script,
and declining to tag three of them is what made the other seven credible.

Your diagnostic answer is the next job. Two parts, in this order, because the first one
probably unblocks the second.

## Part 1 — the 16 general resources wearing one role

You found 18 resources tagged `non-technical` and nothing else, 16 of which open their
own `who_for` with "Anyone", "Someone" or "People". That is the same fault you just fixed
in the two paths, one level up: `non-technical` has been used as a bucket for "general
beginner" rather than as one of ten equal roles.

Judge each of the 16 the way you judged the eleven steps — one at a time, one line of
reasoning each, and **decline where declining is right**. Some genuinely are for the
non-coder specifically. *Claude, Claude Projects and Claude Code for Non-Coders* has it
in the title.

Two anchors so this does not become mass-tagging:

- The question is still **would this person, at this level, get real value from this
  exact resource** — not "could it conceivably apply".
- If a resource ends up on eight or nine roles, ask whether it is genuinely universal or
  whether you are just avoiding a decision. Universal resources exist; there are not
  sixteen of them.

## Part 2 — then look again at the four pathless roles

This is why Part 1 comes first. Here is what those roles have at the two beginner levels
right now:

```
data-analyst      37 total     never-used  1     basic 17
pm                56 total     never-used  3     basic 20
designer          29 total     never-used  1     basic  8
writer-marketer   41 total     never-used  3     basic 28
```

Six of the 16 in Part 1 are `never-used`. A designer with one beginner resource cannot be
given a route; a designer with four or five might be.

So after Part 1, re-measure and tell me, per role: **is there now enough to build an
honest path?** An honest path means at least three steps, every step at least
`previewed`, every step genuinely serving that person, and a real reason for each
position.

Do not build the paths yet. Tell me which of the four are now possible, which are still
too thin, and what each thin one is missing — a level, a topic, a format. That is a
research shopping list I can act on, and it is worth more to me than a path built out of
whatever happened to be lying around.

## What would make this wrong

- Tagging to hit a number. If designer still cannot support a path after Part 1, say so.
  "Still too thin" is a real answer and I would rather have it than a weak path.
- Touching `build-paths.py`. Not yet — Part 2 is a measurement, not a build.
- Rewriting any `who_for` or `skip_if`. Those 72 weak lines are still mine.

---

One commit for Part 1. Part 2 is a report, no commit needed. Short answers.
