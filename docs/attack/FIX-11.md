# Fix prompt — the path page as cards, then the Academy harvest

Paste everything below the line into Claude Code, in the project folder.

---

Two jobs. Do them in the order written, and commit between them.

**Why this order.** Job 1 is small, self-contained and verifiable in an hour. Job 2 is 289
pages of judgment and will take much longer. If the run dies halfway I want job 1 already
in git, not stuck behind a harvest.

---

# Job 1 — the path page is text, and it should be cards

Open `paths.html?id=first-week` and look at it. It is a numbered list of paragraphs.
Nobody scans that; they read it or they leave.

**The design is already done and already checked in a browser.**

- `docs/design/sample-path-card.html` — a working sample on real tokens, real fonts and
  real path data. Open it first.
- `docs/design/path-card-spec.md` — every rule in it, with the reasoning.

Build what the sample builds, in `one()` in `assets/js/paths.js`. The path index is
adequate; leave it unless the same components make it obviously better for free.

Do not redesign it. If you disagree with something in the spec, say so and stop — do not
quietly build a third thing.

## First, a bug the sample uncovered — fix this before anything else

`assets/icons/formats/*-alpha.png` are **not transparent**. All seven are 1024×1024 with a
solid `#f0eee6` ground. Measured: 0.0% of pixels have alpha 0. They are named `-alpha` and
they are not.

They only look right because `#f0eee6` is `--ivory-medium`, the page canvas. Put one on a
card (`--ivory-light`) and there is already a faint square behind it today, at 32px on
every Browse card. Put one on a tint and it is a plain white box.

`docs/design/scratch-icons/` holds transparent versions, made by keying out the flat ground
and unpremultiplying — `article` came out 93.0% transparent, `course` 78.8%. **Regenerate
them properly and replace the shipped seven.** Check the edges at 200% before committing;
a naive key leaves a halo and these are line art with soft anti-aliasing.

This blocks everything else on this job. Do it first.

## Two small things from the same screenshots

- **A line under every heading.** The single path has an `intro`. The *index* headings —
  "Other paths", "For a teacher" — have nothing under them. One line each, saying who the
  section is for.
- **Breadcrumb.** `← All paths` says how to leave but not where you are. Make it read
  `Paths / <title>`.

## The publisher marks — a real job, not a detail

The card has a badge in the tile's bottom-left corner for the publisher's own logo. There
is no fallback. **The real logo or no badge.** Initials were built and rejected: a lettered
square is not a mark, it is an apology for not having one.

So this needs a build step. `docs/design/path-card-spec.md` has the whole rule; the shape
of the work:

1. Fetch each mark **once, at build time**, into `assets/icons/publishers/`. Commit them.
   Nothing may be requested at render — a favicon service called per card would send the
   reader's browsing to a third party, and the page has to keep working from `file://`.
2. A host-to-slug table beside the icons, so the seven Anthropic hosts resolve to one file
   and an unknown host falls through to *no badge* rather than a broken image.
3. Start with the three that matter. Measured over the 354 entries: YouTube 72, GitHub 31,
   and one Anthropic mark standing for seven hosts, 87. **That is 54% of the catalogue in
   three files.** Coursera, Northeastern, DataCamp, Medium, Udemy and LinkedIn take it to
   61%. Stop there.
4. Prefer the publisher's own SVG, then `apple-touch-icon`, then `favicon.ico`. **If
   nothing above 32px exists for a publisher, drop that publisher** — a 16px favicon
   upscaled into a 28px badge looks broken, and a broken badge is worse than none.

The other 121 hosts get an empty corner. That is correct, not a compromise: the publisher
name is already in text under the title, so the badge adds recognition where recognition
exists and stays quiet where it does not.

## The time wording changes everywhere — check everywhere

`LC.TIME` gets short labels: **15 min**, **1 hour**, **half a day**, several days.

One vocabulary, not a chip variant — `ui.js` says a label must never drift between two
screens, and a second time vocabulary is that drift.

This moves the words in the Browse filter rail, on every card, and in the path summary
line. Open all three. A filter row reading "15 min" is fine, but check it against its
heading, and check "half a day" still reads as a sentence where it is used as one. Update
`docs/design/ux-copy.md` in the same commit — if the copy deck and the code disagree, the
deck stops being worth reading.

## Verify

Open it and look at it. Do not tell me it works from reading the diff.

- a path at 375px width — the tile becomes a 16:7 band, the arrow disappears
- Tab through a card: focus rings the **card**, not the four words of the title
- "Start with this" is still clickable, and still reaches our resource page
- the drawings **and the publisher marks** load from `file://`
- a step whose publisher has no mark — the corner is empty, not a broken image
- Browse still reads correctly with the short time labels
- `prefers-reduced-motion` — the fade stays, every movement goes

---

# Job 2 — harvest Claude Academy

`https://academy.claude.com/all` says **289 resources**. We have **5**. Zero tutorials.

Morteza has decided: **take all 289.** Do not re-litigate the number, but do read the
"what this costs us" section below, because it changes what else you must build.

## Why we missed them

Our harvest was search-driven. We asked Google, Gemini and YouTube for "Claude courses"
and took what came back. We never walked the Academy's own index. The list sits behind a
"Load more" button so search engines see little of it.

The pages themselves are prerendered — plain `WebFetch` returns the full text. This was a
method error, not a technical block. Same class as searching for the tool instead of the
work, which is what produced "Substack" as a publisher name.

## Getting the list

The prerendered `/all` HTML shows only the first ~24 items. Find the real list:

1. Open `/all` in a browser and watch the network panel for a JSON feed. A prerendered
   SPA is loading that list from somewhere. Try that first — it is one request against
   289 fetches.
2. Failing that, walk the filter combinations. `/all?kind=tutorial&product=chat`,
   `kind=course`, `kind=use-case`, and each `product` value linked from `/tutorials`.
3. Failing that, click "Load more" until it stops.

**Whichever route: reconcile against 289 and tell me the number you got.** If you got 271
or 305, say so and say why — a silent mismatch here means we ship an incomplete claim.

## Three traps, named

**1. The Skilljar duplicates.** We hold 13 entries on `anthropic.skilljar.com`. That is
the *old* Academy. Both hosts are live and serve the same courses:

```
ours    https://anthropic.skilljar.com/ai-fluency-for-small-businesses
theirs  https://academy.claude.com/courses/ai-fluency-for-small-businesses
```

`norm()` will not catch this — different hosts. **Dedupe those 13 by title, not URL.**
Keep the existing entry with its hand-written `skip_if`; swap the URL to the
academy.claude.com one and re-check `cost` (Skilljar requires registration —
`free-account`, not `free`). Do not create a second entry.

**2. Video tutorials.** Some `/tutorials/` pages are a video with a stub of text. You
cannot watch a video. That is `previewed`, never `ai-reviewed`. Check each page for
whether the text is the lesson or a description of the lesson.

**3. Courses are gated.** Lessons sit behind registration. A course is `previewed` at
best, no matter how good the outline reads. `reviewed` stays 0 — that allowance is not
yours to spend.

## The `skip_if` problem, which is the actual work

289 honest "Skip if" lines is the job. Everything else is data entry.

The failure mode is obvious and you should expect to catch yourself doing it: 289
variations of *"Skip if you already know X."* That passes the letter of the test and
fails the point of it.

An Anthropic-published resource has a real, repeatable weakness worth naming — it will
not tell you whether the product is worth using, only how to use it. That is exactly what
an independent directory is for. But if 289 entries say that sentence, the site has 289
copies of one judgment and no judgment at all.

So: the existing bar (*would someone who read the title already know this?*) plus one
more for this batch — **no two skip lines may be interchangeable.** Spot-check yourself:
pull 20 at random, swap them between entries, and see whether anything breaks. If nothing
breaks, they are not doing any work.

## What this costs us, and what you must build because of it

354 + ~284 = ~638 resources, of which roughly **57% would be Anthropic's own**. Right now
it is 22%. A reader who wants to know what people *outside* Anthropic think would have no
way to ask.

`data/items.json` already has an `official` boolean. **Add it as a Browse filter.**
Without it this harvest turns a curated directory into an Academy mirror with extras, and
that is a worse site than the one we have.

Say in one line on `how-we-check.html` how much of the catalogue is official and why we
carry all of it. The number comes from the data, never typed.

## Fields, roles, and one warning

Every entry needs every field `scripts/validate-catalogue.py` checks. Run it. Run
`build.sh`. Both must pass before you commit.

`published`: the Academy pages may carry no date. **Do not invent one.** 171 of 354
already have none and that is honest.

On roles — the use cases are grouped by job on their site (Sales, Marketing, Product) and
that maps onto ours. This may finally close **designer**, which is the last uncovered
role. But `using-claude-design-for-presentations-and-slide-decks` is a Claude Design
tutorial, and FIX-10 named that exact trap: *does this teach design work, or a Claude
product designers happen to open?* Do not let 289 new items paper over the gap. If
designer still cannot support an honest path after this, say so plainly, as you did
before.

## Rules, unchanged

- Never invent a resource. Real URL, opened, every field grounded.
- Reject nothing from this list — Morteza chose all 289 — but grade honestly. A weak
  resource marked `listed` with a truthful skip line is fine. A weak resource dressed up
  is not.
- `reviewed` allowance stays 0.

---

Commit job 1 on its own. Then job 2, in batches, committing as you go — do not hold 289
entries in one commit.

Finish with what surprised you and what you got wrong. Every round has produced something
real in those two sections, including a false `skip_if` you had written yourself.
