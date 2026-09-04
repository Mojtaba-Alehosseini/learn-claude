# Source list for the thin-cell harvest

**Built:** 4 September 2026. Every index below was fetched on that date.
**Method:** walk the publisher's own index or archive. Search fills gaps; it is not the
method. This is the direct lesson of the Academy gap — that harvest was search-driven and
never walked `academy.claude.com`'s own catalogue, so 291 resources sat invisible for
weeks while search returned the same forty pages.

---

## Step 0 — what the catalogue holds today, measured

From `data/items.json`, 618 rows, using the same eligibility rule as
`scripts/pick-candidates.py` (role, exact level, live, tier above `listed`, not stale).
Each cell reads **eligible / distinct publishers / non-Anthropic**.

| role | never-used | basic | confident | builder |
|---|---|---|---|---|
| non-technical | 51 / 19p / 16x | 69 / 27p / 25x | 13 / 5p / 4x | **8 / 1p / 0x** |
| student | 21 / 14p / 11x | 15 / 10p / 7x | 8 / 5p / 3x | **0 / 0p / 0x** |
| researcher | **12 / 4p / 0x** | 18 / 15p / 12x | 18 / 11p / 10x | 20 / 3p / 2x |
| teacher | 18 / 9p / 5x | 18 / 12p / 9x | 8 / 2p / 1x | **2 / 2p / 1x** |
| developer | **7 / 4p / 1x** | 19 / 11p / 8x | 37 / 18p / 19x | 56 / 17p / 16x |
| data-analyst | **6 / 4p / 1x** | 18 / 13p / 11x | 21 / 11p / 10x | 33 / 2p / 3x |
| pm | 10 / 7p / 5x | 40 / 15p / 15x | 52 / 22p / 25x | 55 / 3p / 2x |
| designer | **5 / 4p / 4x** | 10 / 8p / 6x | 20 / 16p / 16x | 11 / 4p / 3x |
| business-founder | 29 / 14p / 10x | 63 / 24p / 22x | 47 / 7p / 6x | 78 / 3p / 2x |
| writer-marketer | 9 / 8p / 6x | 31 / 23p / 21x | 7 / 7p / 4x | **3 / 2p / 3x** |

**What that says against the three priorities:**

1. **`never-used` is the thinnest level.** Six of ten roles hold fewer than 13 eligible
   items, and `researcher|never-used` has **zero** non-Anthropic material — twelve items
   from four publishers, all Anthropic's own. `designer|never-used` holds five.
2. **`designer` is the thinnest role**, 46 across all four levels.
3. **Publisher concentration at the top two levels is real and it is not imaginary
   scarcity in every case** — `developer|builder` has 17 publishers and 16 non-Anthropic
   items. It is specific: `non-technical|builder` (1 publisher, 0 non-Anthropic),
   `data-analyst|builder` (2), `pm|builder` (3), `business-founder|builder` (3),
   `researcher|builder` (3), `teacher|confident` (2).

---

## What we already hold, by host

| host | held |
|---|---|
| `academy.claude.com` | 290 |
| `youtube.com` | 72 |
| `claude.com` | 17 |
| `support.claude.com` (Help Center) | **16** |
| `code.claude.com` | 7 |
| `coursera.org` | 6 |
| `platform.claude.com` | 5 |
| `udemy.com` | 4 |
| `medium.com` | 4 |
| `deeplearning.ai` | 3 |
| `freecodecamp.org` | 3 |
| `nngroup.com` | 3 |
| `pluralsight.com` | **0** |
| `figma.com` | 1 |

Two of those are the story: **the Help Center is barely touched** and it is the single
largest beginner source in existence for this product; **Pluralsight is at zero** despite
three courses being named in the 16 August research file and never harvested.

---

## Index 1 — Claude Help Center · `support.claude.com`

Walked from the Help Center home, 2026-09-04. **16 collections**:

| Collection | URL | Articles |
|---|---|---|
| Claude | `/en/collections/4078531-claude` | **79** |
| Team and Enterprise plans | `/en/collections/9387370-team-and-enterprise-plans` | 67 |
| Claude API and Console | `/en/collections/5370014-claude-api-and-console` | 39 |
| Privacy and legal | `/en/collections/4078534-privacy-and-legal` | 25 |
| Claude Code | `/en/collections/14445694-claude-code` | 20 |
| Safeguards | `/en/collections/4078535-safeguards` | 17 |
| Pro and Max plans | `/en/collections/5953830-pro-and-max-plans` | 16 |
| Connectors | `/en/collections/15399129-connectors` | 16 |
| Claude Mobile apps | `/en/collections/9387080-claude-mobile-apps` | 15 |
| Identity management | `/en/collections/17270717-identity-management-sso-jit-scim` | 15 |
| Claude Cowork | `/en/collections/19667525-claude-cowork` | 13 |
| Claude Desktop | `/en/collections/16163169-claude-desktop` | 9 |
| Claude for Government | `/en/collections/19395194-claude-for-government` | 9 |
| Amazon Bedrock | `/en/collections/4078537-amazon-bedrock` | 6 |
| Claude in Chrome | `/en/collections/18031491-claude-in-chrome` | 5 |
| Claude for Education | `/en/collections/12630177-claude-for-education` | 4 |

The **Claude** collection was walked in full and splits into seven sub-sections: Release
notes, Get started (9), Account management (16), Conversation management (6), Features and
capabilities (33), Personalization and settings (5), Troubleshooting (4), Usage and limits
(5).

**Most of it is not learning material** and must not be harvested: billing addresses,
Japanese consumption tax, coupon troubleshooting, session security, SSO. The learning
material sits in three places — *Get started*, *Troubleshooting*, and *Usage and limits* —
and those are almost exactly the `never-used` gap. That is the find of this walk.

---

## Index 2 — Pluralsight · `pluralsight.com`

Walked `/paths/claude-code`, 2026-09-04. Six courses, all subscription-gated, all
non-Anthropic authors — directly relevant to priority 3.

| Course | Author | Length | Published |
|---|---|---|---|
| Introduction to Claude Code | Jon Friskics | 43 min | 2026-07-06 |
| Claude Code in Practice | Sarah Holderness | 47 min | 2026-01-30 |
| Advanced Claude Code | Karoly Nyisztor | 1 h 27 m | 2026-01-21 |
| Building with Claude Agent SDK | Dan Tofan | 1 h 34 m | 2026-07-17 |
| Claude Code Testing and Debugging | Laurentiu Raducu | 1 h 9 m | 2026-08-07 |
| Automating Workflows with Claude Code | Bogdan Sucaciu | 1 h 39 m | 2026-07-08 |

**Not yet harvestable.** The obvious course URL built from the path listing
(`/courses/claude-code-in-practice`) returns **HTTP 404**. Pluralsight's course slugs are
not derivable from the path page, and nothing gets written from a guessed URL. Each course
page must be reached from the path page's own links before any of these ship. Recorded
here so the next session starts from the fact rather than rediscovering the 404.

---

## Index 3 — DeepLearning.AI · `deeplearning.ai`

Walked the course catalogue filtered on Claude, 2026-09-04.

| Course | URL | Partner | Length | Level |
|---|---|---|---|---|
| Claude Code: A Highly Agentic Coding Assistant | `learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant` | Anthropic | 2 h | Intermediate |
| AI Coding Workflows: From Cloud to Local | `learn.deeplearning.ai/courses/ai-coding-workflows-from-cloud-to-local` | JetBrains | 1 h 32 m | Intermediate |

Two notes. The catalogue now serves courses from **`learn.deeplearning.ai`**, not
`www.deeplearning.ai/courses/...` as recorded on 16 August — the three rows we already
hold should be re-checked for redirects before anything new is added beside them, or
duplicate rule 11 will fire on the shared trailing slug across the two hosts. And the
second course is a genuine find for priority 3: a non-Anthropic partner, at builder level,
comparing Claude Code against other agents rather than teaching it.

---

## Indexes still to walk

Named here so the next pass starts from a list rather than from search:

- **Help Center**: *Claude Code* (20), *Claude Cowork* (13), *Claude for Education* (4),
  *Connectors* (16). Education is small and directly serves `teacher` and `student`.
- **Pluralsight**: the six course pages, reached from the path page's own links.
- **NN/g** (`nngroup.com/articles/`): the search endpoint returns only chrome to a fetch;
  the article archive must be walked instead. Priority 2, designer.
- **Independent YouTube channels** verified active in the 16 August file and still
  unharvested at depth: IndyDevDan, Cole Medin, Nick Saraev, Simon Scrapes. These are the
  realistic answer to priority 3 at `confident` and `builder`, and each has an RSS feed,
  which is a walkable index rather than a search.
- **University library guides**: we already hold Tulane, Pittsburgh, Northeastern,
  St. Catherine and Melbourne. Library guides are written for people who have never used
  the tool, which is exactly priority 1, and each university's guide list is an index.

---

## Sources checked and deliberately **not** harvested

- **Help Center account, billing and identity articles** (~40 across collections). Real
  pages, correctly published, and not learning material. A directory that lists "Notice
  regarding consumption tax (JCT) for Japanese customers" as a way to learn Claude has
  stopped meaning anything.
- **"Where can I access Claude?"** (`8461763`) was opened and rejected as a *never-used*
  entry on its merits, then kept for a different reason — see the checkpoint entries. Its
  title promises interfaces and its body is a 2,600-word list of 180 countries.
