# Fix prompt — the decisions, and the seven you logged

Paste everything below the line into Claude Code, in the project folder.

---

That run was the best work on this project. Three things in particular: you replaced your
own estimate with a real number and named the direction it was wrong in; you found that
`ch` is the width of the digit zero and not a character, which had been silently costing
40% of the measure since the tokens were written; and you rejected a resource because one
sentence on it was wrong, on the one page where being wrong matters most.

I have made the decisions you asked for. Here they are, then the rest.

## 1. Clay — take your recommendation

Add it to two pages, not three:

- **how-we-check.html** — "Browse the 347 resources" at the foot. That page currently
  ends and asks nothing.
- **A single path view** — "Start with this" on step 1 only.

**Not** browse.html and **not** the paths index. Your reasoning is the reason: both pages
exist so the reader can choose, and colouring one option is an argument they should not be
making.

Restate the rule in `docs/design/design-brief.md` as **at most one per page, and none
where there is no single action** — and write the reasoning in, so nobody "fixes" it back
to exactly-one later.

Use the real count, read from the data, not a number typed into the HTML. That page
already computes its tally that way and this must not be the line that rots.

## 2. Cost — cost means reading the page

A Help Center doc is free even when the feature it describes is paid. Change those three
to `free`. The paid requirement belongs in `skip_if`, where you have already put it.

Then check the rest of the catalogue against that definition and fix any others you find.
Write the definition into `docs/specs/` in one sentence so the next person filling this
field does not have to guess: **`cost` is what it costs to consume this resource, not what
it costs to use what it teaches.**

## 3. Time — round up, do not add a bucket

Leave the four buckets. File the 90-minute resources as `half-day` rather than
`under-1hr`. Overstating how long something takes is the safer error; understating it
wastes someone's afternoon.

Fix MCP Advanced Topics and any others you find in the same position. Where a resource has
a real duration worth knowing, put it in `skip_if` or leave it in `notes` — do not invent
a fifth bucket.

## 4. The seven you logged and did not fix

Work through the list at the bottom of `RUN-LOG.md`. Two I want handled specifically:

- **The self-contradicting entry.** "Academic Research with Claude" says
  `prerequisites: [familiarity with R or Python]` and `notes: "no prior coding experience
  required per syllabus"`. Open the syllabus and settle it. If the syllabus is gone or
  unclear, say so and leave both fields with a note recording the conflict — do not pick
  the one that reads better.
- **`N/A` passing the placeholder check.** You found it and deliberately did not widen the
  check. I agree with that. Instead, add `n/a` and `n\a` to the named `PLACEHOLDERS` list,
  which is the narrow fix, and add a test.

For the rest, use your judgment. Anything you decide not to fix, say why in one line.

## 5. The commit that swept up my files

`87a7c24` contains nine files that are mine — `docs/FIX-THESE*.md`,
`docs/attack/FIX-*.md`, `.claude/launch.json` — under a commit message about your run.
Leave the history alone; it is pushed and rewriting it costs more than it is worth. Just
add them to `.gitignore` going forward if they should not be tracked, or leave them
tracked if they should — your call, but stop using `git add -A`.

## Not now

- **Designer.** Your spec names the three things that would change the answer and I would
  rather find them than pad the role. Leave it.
- **The email address.** Still parked.
- **A data-analyst path.** You said it can support one; that is the next conversation, not
  this prompt.

---

Same rules as last time: run to the end, commit each unit separately, log as you go, and
finish with what surprised you and what you got wrong. Those two sections have been worth
more than the fixes.
