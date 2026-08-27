# Fix prompt — build the two paths that are honestly possible

Paste everything below the line into Claude Code, in the project folder.

---

That was the right answer. Two buildable, two not, with a specific reason for each "no" —
better than four paths made of whatever was lying around. The designer and data-analyst
shopping lists are mine to act on; I will go and find those resources.

Build the two. **Do not build the other two, and do not revisit them in this prompt.**

## The standard, same as the existing three

Read `scripts/build-paths.py` first. Every rule that file already enforces applies here:

- **Every step carries a `why`** — the reason it sits at *that* position rather than
  another. That sentence is ours and it is the reason paths exist at all. It gets the
  same weight `Skip if:` gets on a card. If a step's `why` could be moved to any other
  position without changing, the order is not real and neither is the path.
- Steps referenced **by URL**, never by id.
- Every step at least `previewed`. The script enforces it; do not work around it.
- Time and cost computed from the real fields, never claimed.
- 5 or 6 steps. Long enough to be a route, short enough to finish.

## writer-marketer — you already found the spine, use it

Your own words: *learn it → stop it sounding like AI → disclose it honestly*. That is a
genuine editorial arc and it is better than anything I would have specified. The
`safety: 6` cluster as the ending is exactly right — it is the part every other path
lacks and the part a working writer actually gets fired over.

Title it for the person, not the topic. "Your first week with Claude" works because it
names a moment. Do the same here.

## pm — name its weakness in the path itself

You said its identity is muddier: 7 of 29 basic entries are Claude Code, which is what
the PM agent complained about. Do not hide that. If a step needs a terminal, its `why`
says so in the first clause, so a PM who does not want one can stop at step 3 and still
have gained something. "You can stop after step 3" is already how the first-week path
handles the same problem.

## Then verify, not just build

- The role-coverage check you added must pass for both new paths.
- The full validator and its 26 tests must stay green.
- Open both on the live site and read them as that person. A path that validates and
  reads badly is not done.
- Tell me the honest weakest step in each — the one you would replace first if I found
  you a better resource next week.

## What would make this wrong

- Padding to six steps. Five good ones beat six with a filler.
- Reusing the same generic opener for both. "Get started with Claude" may be right for
  one of them; it is not automatically right for both, and two paths that begin
  identically are one path with two names.
- Touching designer or data-analyst.

---

One commit. Short answer: the two titles, the step count, and the weakest step in each.
