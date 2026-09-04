# Does advanced non-coder material exist? A supply survey

**Surveyed:** 4 September 2026. Every index below was walked on that date.
**Scope:** count what exists before spending a round harvesting it. **No entries were
written.** This is a measurement, not a harvest.

## Why

`builder` and `confident` are where this catalogue is weakest, and the weakness is
specific rather than general. From `docs/STATUS.md` on the same date:

| pool | items | publishers | non-Anthropic |
|---|---|---|---|
| `non-technical\|builder` | 8 | **1** | **0** |
| `writer-marketer\|builder` | 3 | 2 | 3 |
| `teacher\|builder` | 2 | 2 | 1 |
| `data-analyst\|builder` | 33 | 2 | 3 |
| `pm\|builder` | 55 | 3 | 2 |
| `business-founder\|builder` | 78 | 3 | 2 |
| `teacher\|confident` | 9 | 3 | 1 |
| `writer-marketer\|confident` | 7 | 7 | 4 |
| `student\|builder` | 0 | — | — |

`developer|builder` is not on that list: 57 items, 17 publishers, 16 of them independent.
The advanced end is not thin in general. It is thin **for people who do not write code**.

The last harvest yielded four entries from nine candidates, so the question worth
answering first is whether the supply exists at all.

---

## What was walked

| publisher | index | walkable? |
|---|---|---|
| Coursera | `/search?query=claude cowork` | yes |
| Maven | `/search?q=claude` | yes |
| DataCamp | `/search?q=claude` | yes |
| Pluralsight | `/paths/claude-code` walked; `/search` | path yes, **search no** — the search page is rendered client-side and returns an empty template to a fetch |
| DeepLearning.AI | `/courses` filtered on Claude | yes |
| YouTube | `@simonscrapes/videos` and any channel | **no** — every channel URL 302s to `consent.youtube.com`. Getting past it means accepting a cookie banner, which is not something I will click without being asked |
| Udemy | `/courses/search/?q=claude cowork` | **no** — HTTP 403 to any automated request |

**Two of the seven cannot be walked by machine at all, and they are the two most likely
to hold independent non-coder material.** That is the single most important line in this
report. YouTube is where the independent Claude teaching happens, and its index is behind
a consent wall; Udemy refuses automation outright. Any real assessment of supply at the
advanced end needs a person to walk those two, or an authenticated session.

---

## What exists, and where it would land

Candidates found, none written to the catalogue, none opened beyond its index entry — so
every line below is **unverified beyond the listing** and would need the full open-and-read
treatment before it could ship.

### Genuinely aimed at non-coders

| candidate | publisher | shape | likely cell |
|---|---|---|---|
| **Claude Skills for Leaders** | DataCamp | code-along | `business-founder\|confident`, `pm\|confident` |
| **Create Claude Skills for Marketing** | DataCamp | code-along | `writer-marketer\|confident`, and possibly `writer-marketer\|builder` — the 3-item cell |
| **Claude Cowork for Automating Processes** | Coursera / SkillsBooster Academy | course, beginner, 1–3 months, 4.8★ from **8** reviews | `non-technical\|confident`, `business-founder\|confident` |
| **Claude Code for Customer Insights** | Maven | 2-week cohort | `pm\|confident`, `data-analyst\|confident` |
| **Introduction to Agent Skills** | DataCamp | course | `non-technical\|builder` — the zero cell — if it is genuinely non-coder |

### Advanced but developer-shaped (does not help the thin cells)

| candidate | publisher | note |
|---|---|---|
| AI Agents with Model Context Protocol & TypeScript | Coursera / Vanderbilt | 4.8★, ~9,000 reviews. Serious material, and TypeScript in the title settles which cell it serves |
| Claude Code: Software Engineering with Generative AI Agents | Coursera / Vanderbilt | 4.7★, 172 reviews |
| The Complete Claude Code & Claude Cowork Masterclass | Coursera / Dr. Ryan Ahmed | specialization, 3–6 months |
| Claude Code in Practice | Maven | 5-week cohort |
| Software Development with Claude Code | DataCamp | course |
| The six Pluralsight Claude Code courses | Pluralsight | walked last round; all developer, and their course URLs are still not derivable from the path page |

---

## The measurement

**Five plausible non-coder candidates across three walkable publishers**, against nine
thin or zero cells. Every one of the five is paid or sign-up-gated: DataCamp code-alongs
need an account, the Coursera course is free to enrol with a paid certificate, Maven is a
paid cohort.

Set against the last harvest's yield of four from nine after opening, five listings would
plausibly become **two or three shippable entries**. That is not nothing — two entries
would give `non-technical|builder` its first independent voice and `writer-marketer|builder`
a fourth item, which takes it over `MIN_POOL` and into having picks at all. But it is not
a round's worth of harvesting either.

**So the honest answer is: thin, but not zero, and measured with two hands tied.** The
two publishers most likely to hold this material could not be walked. A round spent on
the advanced end would be a round spent mostly on YouTube and Udemy, by hand.

## What this survey cannot tell you

- Whether any of the five is any good. None was opened past its index listing. The
  Coursera Cowork course carries 4.8 stars from **eight** reviews, which is a number to
  distrust rather than a recommendation.
- Whether "Introduction to Agent Skills" is genuinely non-coder. Its title suggests it
  could serve `non-technical|builder`; its publisher's catalogue is mostly for people who
  write Python. That is exactly the kind of thing the `who_for` test settles, and it
  needs the page open.
- What exists on YouTube and Udemy, which is most of it.

## Recommendation

Not a full harvest round. Two smaller things instead:

1. **Open the five.** An afternoon, not a round. If three survive, ship them — they land
   in the cells that need them most, including the only pool in the catalogue with zero
   independent material.
2. **Decide about YouTube and Udemy.** They cannot be walked from here. Either a person
   walks them, or the catalogue accepts that its independent advanced material will stay
   under-represented and part 11 says so plainly. That is a decision about the site's
   promise, not a task.
