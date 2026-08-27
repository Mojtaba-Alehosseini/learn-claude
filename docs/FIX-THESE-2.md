# Fix prompt — round 2

Paste everything below the line into Claude Code, in the project folder.

---

Good work on the last round. I had it reviewed and all four items hold — I re-checked
the OTS finding, the `norm()` bug, the font counts and the validator myself. **You were
right about the font and the reviewer was wrong**: the PIL number measured FreeType, not
Chrome. Keep Light. Three things left. Read `CLAUDE.md` first.

## 1. The validator misses the rule the README calls most important

`scripts/validate-catalogue.py` has no mention of `reviewed`. That is the one rule the
README singles out:

> Only a person may write `tier: reviewed`. No automated stage may claim a human read
> something.

Provenance is not visible in a file, so you cannot enforce it directly — do not pretend
to. But **0 of 353 entries are `reviewed` today**, so any appearance of it is an event.

Add a check that fails when the count of `tier: reviewed` is greater than the number
recorded in a small committed file (start it at 0). Message should say which entries
claim it and that a person must confirm each one before the number is raised. That way
the first automated stage that quietly writes `reviewed` stops the build, and I raise
the number by hand when I have genuinely finished something.

Prove it: add it to `test-validate-catalogue.py` like the other 16.

## 2. Delete the 36 font files nothing references

I confirmed your counts: 48 committed, 12 referenced by CSS, 6 of those are the `.woff2`
a browser actually fetches. **36 files are referenced by nothing at all** — 2.6 MB,
including both OTS-damaged ones.

Delete those 36. Not a design decision: no CSS points at them, so nothing can change
visually. Then prove it — validate, build, and load all five pages to confirm every
`@font-face` still resolves.

Leave the 6 `.otf` fallbacks alone for now. I will decide on the remaining 12 separately.

## 3. The Mac question — measure, do not change

Every measurement so far was on Windows, where `-webkit-font-smoothing: antialiased` is
a no-op. On macOS it switches to grayscale antialiasing and genuinely lightens text.
So on a Mac the body copy may be thinner than either of us has seen, and Light is
already the lightest cut in the family.

I do not have a Mac. Work out how much of a risk this actually is without one — look at
what that declaration is doing for us on Windows (probably nothing), and tell me whether
simply deleting it is safe. If deleting it costs nothing on Windows and removes the
macOS risk, that is the answer and you should say so plainly.

Do not change the typeface.

---

One at a time, one commit each, message saying what was wrong and how you know it is
fixed. Short answers. Ask before anything large.
