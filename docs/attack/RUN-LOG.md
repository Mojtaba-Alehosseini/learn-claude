# Run log — four-part run, 2026-08-27

One line per unit. What changed, what was left alone, and why. Written as the run
happened, not reconstructed afterwards. Read this against the report.

## Part 1 — the Skip if rewrite

| # | Unit | Changed | Left alone, and why |
|---|---|---|---|
| 0 | Batch 1 (previous commit `5a6a7d5`) | 11 of the 12 shortest | "Claude Code for Data Analysis" — *You never touch a terminal* passes the test: an analyst need not know Claude Code is a CLI |
| 1 | The rest of the under-45 band, 37 entries | 32 rewritten | 2 passed (see below); 1 held for Part 2 as half of a duplicate pair; 2 titles use em dashes and were missed on the first pass, caught and fixed in the same unit |
| 2 | The 45–70 band, 36 entries | 28 rewritten | 4 passed; 2 held for Part 2 |

Survivors, all eight, each naming something the card does not:

- `You never touch a terminal.` — Claude Code for Data Analysis
- `You want a hands-on how-to.` — How scientists are using Claude
- `You need current-model behavior specifics.` — Prompt Engineering Tutorial
- `Your work isn't API-based or high-impact science.` — AI for Science Program
- `The built-in SMB connectors already cover your stack.` — Remote MCP Servers directory
- `You need the newer server-side code execution or advanced stats.` — Introduction to Claude Analysis
- `You have no LinkedIn Learning access.` ×2 — the duplicate pair, resolved in Part 2

**Could not ground: none.** Every one of the 71 was derivable from `notes`,
`prerequisites`, `summary`, `level`, `cost`, `time` or `format`. No source needed opening
for this part, so no tier came into question and no `checked` date moved.

**Surprise, logged not worked around.** "Plans & Pricing" carried the literal skip_if
`N/A — always verify pricing here rather than in third-party posts.` That is an empty
line wearing a sentence, and `validate-catalogue.py`'s placeholder check does not catch
`N/A`. Rewritten. The check was **not** widened in this run — that is a separate change
with its own false positives, and it is still open.

**Second surprise.** "Academic Research with Claude (live seminar)" has
`prerequisites: [Basic prompting knowledge, Some familiarity with R or Python]` and
`notes` saying "no prior Claude/coding experience required per syllabus". Those two
contradict each other. Not resolved here — it needs the syllabus reopened, which is
Part 4's kind of work, not Part 1's. Still open.

## Part 2 — the duplicate groups

| # | Group | Ruling | Evidence |
|---|---|---|---|
| 3 | ai fluency framework foundations | **merged 3 → 1**, kept skilljar | `www.anthropic.com/ai-fluency` **redirects** to the skilljar course. Settled by the server, not by judgment. Coursera URL recorded in the survivor's notes |
| 4 | ai fluency for students | **merged 2 → 1**, kept skilljar | Same course, two platforms. Coursera URL in notes. Dropped the role `researcher`: the surviving row is about studying and career planning |
| 5 | model context protocol advanced topics | **merged 2 → 1**, kept academy.claude.com | Both pages opened. Identical description, prerequisites, audience line and section blurbs. One course, two Anthropic surfaces |
| 6 | getting started with claude in excel | **kept both** | YouTube page title read to confirm the video really carries that name. An article and 7:10 of video are two resources. Cost aligned: the article was `subscription`, now `free` |
| 7 | 15 claude tips (**not in the file**) | **deleted one row** | Both on linkedin.com, so the cross-host check was blind by design. One row pointed at `linkedin.com/learning/topics/claude`, opened today — LinkedIn's topic browse page, not a 21-minute course |

**Tier moved once, declared.** The academy.claude.com MCP row was `listed` because an
earlier attempt could not read a client-rendered page. It reads fine in a browser. Read
in full, so `previewed`, and `checked` moved to today — the only thing that earns a date.

**Surprise.** The migration note this catalogue repeats — *"Anthropic's courses moved
from anthropic.skilljar.com to academy.claude.com; old links redirect"* — is not true
today. skilljar URLs answered 200 with no redirect and `anthropic.com` redirects **into**
skilljar. The migration is partial. Corrected in place rather than deleted.

**Second surprise.** academy.claude.com says the MCP course is 11 lessons / 1 quiz /
1.5 hours; skilljar says 15 lectures / 2 quizzes / 1.1 hours of video. Our `time` said
`under-1hr`. It still does, because the vocabulary has no bucket between "one hour" and
"a half day"; the real figure is in `notes`. **Open:** the time scale has a gap that
silently rounds every 90-minute resource down to one hour.

**Third surprise, not fixed.** The `cost` field is applied inconsistently across the
catalogue for free-to-read pages about paid features. "Get started with Claude Design"
is `free`; "Use Claude for Excel" is `subscription`; both are Help Center docs about a
paid feature. Only the Excel pair was aligned, because that pair was the open complaint.
Three entries still carry `subscription` for pages that cost nothing to read. **Open —
Morteza's call**, because it changes what a cost filter returns.

**No path moved.** All five removed rows were checked against `paths.json` first and none
was a step. Step counts and advertised durations are unchanged. Unlike last time.

## Part 3 — the design faults

| # | Unit | Changed | Left alone, and why |
|---|---|---|---|
| 8 | Off-scale literals | 28 replacements; 12 new tokens | `768px` — a media query is evaluated before custom properties resolve, so it cannot be a token in any browser. `1px` in `.visually-hidden` — the clip-box idiom, a technique rather than a size. Both annotated in place |
| 9 | Line length | `--measure` 68ch → 50ch | index.html left at 44 characters: it is a three-column section, and 66–75 is a rule for running prose. Mobile left at 37–38: 66 characters at 18px needs 422px and the phone is 375px |
| 10 | Clay | **nothing** | Proposal only, as instructed: `docs/specs/2026-08-27-clay-on-three-pages.md` |

The real find in unit 8 was not the odd numbers, it was that five components that look
identical to a reader each chose their own padding: `3px 10px`, `3px 10px`, `2px 10px`,
`2px 8px`, `4px 6px 4px 10px`. None on the 4px grid. One pair now.

The real find in unit 9: **`ch` is not a character.** It is the advance width of the
digit 0. Measured in Chrome today — Tiempos 20px: `0` = 12.00px against an average prose
character of 8.52px, ratio 1.41; Styrene 16px: 11.07 against 7.97, ratio 1.39. So `68ch`
was buying 96 characters. That is why one measurement said 93 and another said 72: where
`--measure` bound it ran at 96, and where the container was narrower it never bound at
all. After: how-we-check 69, paths 70, resource 70, browse 70 and 69, nothing over 75.

**Clay, measured rather than assumed.** browse.html *has* a clay button — `#sheetConfirm`
in the mobile filter sheet, `display:none` above 768px. So the count is 2 of 5 on desktop
and 3 of 5 on a phone. The three with none at desktop are browse, paths, how-we-check.

**Could not verify visually.** No screenshot: the Browser pane is not displayed in this
session, so the page does not composite frames. Verified numerically instead — zero
clipped elements, every control still ≥44px, no horizontal overflow (1425 against a 1440
viewport), the checkbox glyph fits its 16px box at the caption size, no console errors.

## Part 4 — the research

| # | Unit | Added | Rejected, and why |
|---|---|---|---|
| 11 | data-analyst, 2 slots | Upload files to Claude; How long do you store my data? | Craig Hewitt's Claude Playbook security page — free, ungated, specific, and **wrong** that Pro excludes training by default. Anthropic's 2025-08-28 consumer terms make it a required choice for Free/Pro/Max. On a page about what is safe to paste, that is the sentence that must not be wrong |
| 12 | designer, 3–4 slots | Analyze patterns in user feedback (basic); The UX Researcher's Guide (confident) | Anthropic's own Design plugin page — names critique, UX writing, accessibility audits and research synthesis, teaches none; a marketing page. An arXiv paper on AI heuristic evaluation — never tested Claude. Six skill-directory aggregators — same skills, generated blurbs |
| 13 | Re-measure | — | `docs/specs/2026-08-27-designer-and-data-analyst.md` |

Roughly twenty candidates looked at, four survived.

**Tier.** All four are `previewed`, not `ai-reviewed`. Each page was read end to end by a
model and I read the summary; I opened none of them myself. `ai-reviewed` here means a
full read and reading a faithful summary is not that. The allowance file still says zero
`reviewed`.

**Mistake caught in-run.** `scripts/add-source.py` silently overwrote the
`source: "Product Impact"` I had written with `"Productimpactpod"`, its host-derived
fallback — the same publisher-name mangling fixed in an earlier round, still live for any
unmapped host. Host added to the map. **Open:** 60 hosts still use the fallback, so this
will happen again to the next entry on a new host.

## Still open after this run

1. `validate-catalogue.py` does not catch `N/A` as a skip_if placeholder.
2. No check catches a row whose URL is a listing or search page rather than a resource —
   that is what hid the LinkedIn topic-hub row.
3. The `time` vocabulary has no bucket between "one hour" and "a half day".
4. `cost` is inconsistent for free-to-read pages about paid features; three entries still
   read `subscription`. Morteza's call.
5. "Academic Research with Claude" contradicts itself between `prerequisites` and `notes`.
6. 60 hosts have no publisher-name mapping and get a mangled fallback.
7. designer cannot support a path, and the three things it needs are named in the spec.
