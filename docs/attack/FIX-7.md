# Fix prompt — finish the quality work, end to end, without stopping

Paste everything below the line into Claude Code, in the project folder.

---

Batch 1 was the best content work of this project. "You don't use Excel." became a line
that names the plan requirement *and* Anthropic's own audit-critical warning — and you
noticed both were sitting in `notes`, which stopped shipping to browsers last week. That
is the standard for everything below.

**Do not stop for approval. Run all four parts to the end**, then give me one report. I
will analyse the whole thing at once. Commit each unit separately as you go, so that a
problem in part 4 never costs me parts 1 to 3.

Keep a running log at `docs/attack/RUN-LOG.md` — one line per unit, what changed, what
you left alone and why. I will read it against your report.

## Part 1 — finish the `Skip if:` rewrite (68 remaining)

Same rule as batch 1, unchanged: **would someone who has just read the title, source and
format already know this?** If yes, rewrite. If no, leave it — you left #12 alone
correctly and I want that judgment applied throughout.

Same hard constraint: derive from `summary`, `who_for`, `teaches`, `notes`, `level`,
`cost`, `time`, `format`, or open the source and read it. **Anything you cannot ground,
leave exactly as it is and list it.** Never invent.

Two things from batch 1 to carry forward:

- Where you open a source and find our tier is wrong in our favour, say so. Do not
  silently upgrade.
- No house style. Eleven different openings in batch 1 was right.

At the end, replace your estimate with the real number: how many of the 79 survived.

## Part 2 — the four duplicate-title groups

`data/duplicate-titles.txt` records four groups and says plainly that listing is not
agreement. Decide each one now:

- **Same resource, two URLs** → merge, keeping the URL our own `notes` prefer, exactly as
  you did with the Claude Code course.
- **Genuinely two things** → keep both and write the reason into the file, so nobody
  revisits it.

You already flagged "Model Context Protocol: Advanced Topics" as probably the same host
migration. Check it properly rather than trusting that.

If a merge changes a path's step count or advertised time, say so — that happened last
time and the 6h → 3h correction was real.

## Part 3 — the design faults from the token audit

Three findings from the four-agent audit are still open. Fix the first two; **propose
only** on the third.

1. **Off-scale literals** — `3px`, `10px`, `11px` and the off-scale paddings sit outside
   the spacing and type scales in `tokens.css`. Either they earn a token or they move to
   the nearest existing one. `CLAUDE.md` says no hardcoded size anywhere; this is that
   rule, unenforced.

2. **Line length** — the audit measured 90–93 characters per line on three pages at
   desktop, and 30–42 on mobile. I measured 72 on the Browse card myself and left it
   alone. Both can be true; find where the difference is and fix the pages that are
   genuinely over. 66–75 is the target. Measure in a browser, not in PIL.

3. **Clay** — three of five pages have zero clay, so "exactly one per page" fails on the
   "exactly" half. **Do not change this.** Tell me which three, what the natural single
   action on each would be, and what you would do. It is a design decision and it is mine.

## Part 4 — the designer and data-analyst research

You wrote the shopping list two rounds ago:

- **data-analyst** — one `never-used` resource about pointing Claude at real data, and one
  on data safety or confidentiality.
- **designer** — two or three `basic` resources on design work that is not prototype
  generation (critique, research synthesis, design systems), and one honest `never-used`
  starting point.

Go and find them. Same standard as every entry in the catalogue:

- A real URL you opened. **Never invent a resource** — that rule has not moved.
- Every required field, controlled vocabulary only, `skip_if` that passes the test above.
- `tier` honest: `previewed` if you read an outline or sample, `listed` if you only found
  it. **Never `reviewed`** — the allowance file still says 0 and it stays there.
- Reject aggressively. Six good entries beat twenty weak ones, and a thin role is better
  than a padded one. If you cannot find a genuine `never-used` designer resource, say so
  — that is the same honest "no" you gave me before and I valued it.

Then re-measure and tell me whether either role can now support a path. **Do not build
one.** That is the next conversation.

## Rules for the whole run

- Every part validates before you move on: `validate-catalogue.py`, its test suite,
  `test-browse-query.js`, and a build.
- Never touch `checked` dates unless you actually re-read the resource.
- Do not touch: the home-page search box, `Skip if:` typography, the email question.
  Those are mine and they stay mine.
- If something surprises you mid-run — as `norm()` did, and the runner-versus-laptop
  difference did — **stop that unit, log it, and carry on with the next.** Do not silently
  work around a surprise.

## The report I want at the end

Short. In this order:

1. Real number: how many of the 79 `Skip if:` lines survived untouched.
2. What you could not ground, and why.
3. The four duplicate decisions, one line each.
4. Design: what you fixed, and your recommendation on clay.
5. Research: what you added, what you rejected and roughly how many, and whether
   designer or data-analyst can now support a path.
6. Anything that surprised you.
7. Anything you got wrong mid-run and corrected.

Items 6 and 7 have been the most useful part of every round. Do not leave them empty out
of politeness.
