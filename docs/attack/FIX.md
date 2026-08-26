# Fix prompt — after the ten-role attack

Paste everything below the line into Claude Code, in the project folder.

---

Read `docs/attack/SUMMARY.md` first. It cites every point back to a numbered finding in
the ten role files — follow a citation whenever you need the detail.

Fix in this order. It is ordered by what it costs a real visitor, not by effort. Stop
after each numbered item, commit it alone, and say in one line what you verified.

## 1. The named-person allegation — today, before anything else

The catalogue contains an unsourced integrity allegation against a named, real academic.
The entry is tiered `listed`, meaning nobody opened the source. It is live and it ranks
first for "systematic literature review".

Find it. Open the source and read it. Then one of three:

- the source supports the claim → keep it, re-tier honestly, cite where it comes from
- the source does not support it → remove the claim from our text
- you cannot verify it either way → **remove the entry**

There is no fourth option where it stays as it is. Tell me which you did and why.
Do not soften our wording and call that a fix — either the claim is sourced or it goes.

## 2. Arriving at Browse with `?q=` returns nothing

Mine. `browse.js` loads the ranked index only inside the `input` handler, so a visitor
who arrives from the home page with `?q=<sentence>` never gets it and falls through to
the substring AND-match at `browse.js:86-88`. No English sentence survives that.

I confirmed it independently:

```
"how do I cite Claude"            role=student        -> 0
"I don't know where to start"     role=none           -> 0
"how do I stop students cheating" role=teacher        -> 0
"clean up a messy spreadsheet"    role=data-analyst   -> 0
```

Load the index on page load when `?q=` is present, before the first render.

Then the second half, which is a separate fault: with a query active,
`browse.js:172` builds the count and empty-state text without looking at `q`, so it
prints a confident "0 resources for a product manager" while holding 56, and advises
browsing by role — which is what they were already doing. The message has to know
whether the zero came from the filters or from the search.

**Verify with the site's own benchmark.** `scripts/test-search.py` has nine sentences
and seven of them return 0 through this path. All nine must return results through a
`?q=` URL. Then add that to the regression tests so it cannot come back.

## 3. Paths ignore the roles they declare

`paths.js` never reads the `roles` field, so a path that names a teacher is unreachable
for a teacher. Two path steps are tagged with the wrong role entirely — step 1 of the
research path is `roles: ["data-analyst"]`.

Fix the reading, then fix the two mistagged steps. A path that says who it is for and
then hides from that person is worse than having no paths.

## 4. Eight cards claim a step in a path they are not in

They print the raw slug on screen. `validate-catalogue.py` checks path → item but never
item → path, so it passes this. Fix the data, then add the reverse check to the
validator and to its test suite.

## 5. The duplicate course, and what it does to a path

The same course exists twice under `academy.claude.com` and `anthropic.skilljar.com`,
both claiming to be step 1 of the same path. The path's advertised "about 6 hours"
depends on which one the build happened to pick. URL-based dedupe cannot see this.

Merge them. Then decide whether the validator should catch near-duplicate titles across
different domains, and say why if you decide it should not.

## 6. Three things shipping that nobody meant to ship

- **`notes`** — 42.3 KB sent to every browser, never rendered, containing security
  warnings a reader would want. Either render it or stop shipping it. Say which and why.
- **Publisher fragments** — "Open on Pl", "Unesco", "Eu". `prettify()` in
  `add-source.py` is mangling hosts it has no mapping for.
- **`What it teaches`** — raw lowercase model output on every resource page:
  `— start and organize conversations in claude`. It has been live for days.

## 7. Two numbers that are wrong

- `ui.js` says "176 of 353 resources publish no date". The data says **171**.
- `Skip if:` exists in two generations, split on the `checked` date. Items checked
  19 Aug average 38 characters and include tautologies like "You don't use R.". Items
  checked 20–22 Aug average 115–169 with real reasons. Two agents found this by
  different methods. Report how many entries are in the weak generation — do not rewrite
  them yet, that is a content decision and it is mine.

---

Do not touch these — they are mine to decide, and the summary says so:

- whether the free-text box returns to the home page
- whether `Skip if:` should dominate the card typographically
- the three pages with zero clay
- rewriting the weak `Skip if:` lines

One commit each. Short answers. Ask before anything large.
