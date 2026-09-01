# Fix prompt — three rulings, then read what shipped

Paste everything below the line into Claude Code, in the project folder.

---

The picks shipped, the departure was flagged instead of buried, and both of your own
mistakes were caught by your own checks. Good round. Now three rulings, and then the
part nobody has done: reading it.

# Ruling 1 — constraint 4 stays as you built it

Fire-and-justify is accepted. Hard rejection would have meant swapping better-fitting
picks for worse ones to please a checker — that is the one sin this project has in
writing. The measurement (30–90% single-topic dominance in every pool) earns the design.

One consequence you may have missed: the 21 justifications are copy now. They get read
in the audit below, at the same bar as everything else.

The subject-axis idea is parked. It is mine, do not start it.

# Ruling 2 — pm|builder: a constraint may never carry an item in

The Maven pick is honest and still wrong. The publisher rule exists to reject bad sets,
and in this cell it hauled a $3,000 certification into a "start with" slot the model
never wanted filled. That inverts the rule.

New principle, written into the validator's docs in one sentence:
**a constraint may reject a set of picks; it may never pull an item into one.**

Operationally: a legal set must come from the model's own ranked shortlist — the picks
and runners-up it already produces. If no legal three exist inside the shortlist, show
two. An item may be lifted by a constraint, never hauled in from below the cut.

Do now:

- Re-pick `pm|builder` under this rule. Expected result: two picks, Maven in the
  runners-up with the honest line it already carries.
- Extend `validate-picks.py`: a two-pick cell must carry a machine-readable cause
  (`publisher-thin` or `rule-carried-third-refused`), never a bare count of two.
- The heading machinery for "Start with these two" already exists — reuse it, verify it
  renders for this cell in a real browser.

# Ruling 3 — the documents

Commit `docs/attack/FIX-12.md`, `FIX-13.md`, `FIX-14.md` and `docs/THE-PROJECT.md` —
they are project history and history lives in git.

Then fix the staleness THE-PROJECT.md itself complains about:

- `docs/START-HERE.md` still says 353 resources and 3 paths. Cut it down to a short
  pointer: the session rules, then "numbers live in THE-PROJECT.md". A second copy of
  the numbers is how one stale file becomes two.
- THE-PROJECT.md part 10 lists the two picks decisions as open. They are closed —
  update it, and add the picks feature to part 3 with numbers measured from the data,
  not remembered from this prompt.
- README "Where it stands" gets one line about the picks, same rule: measured.

# The job — an audit of all 37 cells, by reading

Nobody has read what shipped. The checkpoint covered 3 cells; the other 34 — roughly a
hundred reason sentences, the runner-up lines, the 21 justifications — went live
unread. The site's product is judgment, so unread judgment is unshipped work wearing a
green build.

Read every cell. Four checks, all from the project's own bars:

1. **The reason bar.** Every reason says why this pick beat the pool. If someone who
   read the title would already know it, it is not doing work.
2. **Card-answerable.** Every sentence must be writable from the card fields alone.
   Flag anything only a person who opened the resource could say — the model was
   ranking our notes, and a reason that claims more is an invented claim.
3. **Self-contradiction.** No pick whose own `skip_if` or `who_for` argues against the
   cell's role or level. The designer checkpoint caught one of these; check all 37.
4. **Justifications are reasons, not permits.** Each of the 21 must explain why the
   topic clash serves the reader, not merely acknowledge the clash.

Also the mechanical sweep: headings count-honest in every cell, `picked by AI` label
and date present, runner-up records complete, fingerprints match the pools, and the
strings contain no "best", "top" or "recommended" anywhere.

**How to handle what you find:** fix mechanical faults directly. Rewrite weak reasons —
but log every change, old sentence and new, in the findings file. Anything structural
beyond `pm|builder` (dropping or swapping a pick) stops and asks me first.

Findings go in `docs/attack/PICKS-AUDIT.md`: per-cell verdict, every change logged,
and the count of reasons that failed which check.

# Small job — generalise Puckett into a check

You named the signature yourself: a one-persona `who_for` under 3+ role tags. Write it
into the validator as a printed **warning**, never an error and never an auto-fix —
role tags are broad by design and only a person can tell breadth from mis-tagging. Run
it once and put the list with a one-line verdict per item at the end of the audit file.

# Not yours

Still mine: the email address, nothing is `reviewed`, and the subject axis. The
accessibility pass is next round, not this one — but if the audit trips over an a11y
fault in the new block, note it in the findings rather than fixing it blind.

# Commits

Rulings 2 and 3 separately, then the audit fixes as one commit with the findings file.

Finish with what surprised you and what you got wrong.
