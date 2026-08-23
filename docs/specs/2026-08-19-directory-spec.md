# Spec: Claude learning directory

**Last updated:** 2026-08-19
**Status:** agreed. Page layout still deferred.
**Replaces:** `2026-08-16-directory-design.md` and `2026-08-19-content-model-and-search.md`.
This is the only spec. Change it here, nowhere else.
**Research behind it:** `research/2026-08-16-who-publishes-claude-content.md`,
`research/2026-08-16-competitors-and-learner-demand.md`

---

## 1. The problem

There is a lot of Claude learning content and no way to tell what is worth your time.
Verified from real threads on r/ClaudeAI:

- People cannot find a starting point. "Where should I start?" is asked repeatedly.
- People do not know the order. "Beginner roadmap for Anthropic's free courses: what's the best order?" — nobody answers it.
- People distrust what they find. "New to Claude — tired of YouTube grifters."
- Content goes stale fast. Every six months everything changes and you start again.
- Existing directories do not solve it. Class Central lists 659 Claude courses with no judgment. The big awesome-lists are developer-only and drowning in unprocessed submissions.

The benchmark to beat is not another directory. It is the most common answer in those
threads: **"just ask Claude."** To beat that we must be judged, sequenced, and current.

## 2. Who it is for

Everyone, from someone who has never opened Claude to a researcher or a builder. Not
narrowed by field.

The largest underserved group is people who call themselves **"non-coder"** or
**"non-technical."** Every existing Claude directory is developer-only. This is the wedge.

## 3. What makes it different

No existing site has all four. The combination is the product.

1. Claude-specific **and** open to non-developers
2. Filters by role and level
3. A written judgment on every item — who it is for, and when to skip it
4. A visible **date checked** on every item

Supporting differentiators found in research:

- **Sequencing.** Ordered paths through the free Anthropic courses. Asked for repeatedly, answered nowhere.
- **Grifter filtering.** An explicit note when a video buries its content under ten minutes of hype.
- **A certification warning.** Claude certification is real but gated to the Claude Partner Network. An SEO industry sells prep for exams most readers cannot sit. Saying this plainly is a genuine service.

## 4. Scope

**Version 1 covers:** Claude only — the Claude app, Claude Code, Cowork, Skills, MCP,
agents, the API.

**Not in version 1:** other AI tools, live AI on the site, user accounts, comments,
public submissions, short-form video (TikTok / Reels / X).

**Deferred:** page layout, first-visit flow, card design.

## 5. Taxonomy — six filter axes

| Axis | Values | Required |
|---|---|---|
| **Role** | non-technical · student · researcher · teacher · developer · data-analyst · pm · designer · business-founder · writer-marketer | Yes, at least one |
| **Level** | never-used · basic · confident · builder | Yes, exactly one |
| **Topic** | chat-prompting · claude-code · cowork · skills · mcp · agents · api · safety | Yes, at least one |
| **Format** | video · course · docs · article · hands-on · podcast · repo | Yes, exactly one |
| **Time** | under-15min · under-1hr · half-day · multi-day | Yes, exactly one |
| **Cost** | free · free-account · paid-once · subscription | Yes, exactly one |

**Field is an optional extra tag, not a filter.** Role predicts what someone should watch;
field usually does not. A PM in fintech and a PM in a hospital need the same course. A
doctor and a medical researcher do not. Field is applied only to genuinely domain-specific
content ("Claude for legal document review"). Most items carry no field tag.

## 6. Categories — three separate layers

One word, three different jobs. Keeping them separate is what stops the interface from
drowning.

**Layer 1 — filter axes.** Six, closed, visible. Section 5. These narrow a list. They must
stay small and fixed. A filter list that grows becomes useless.

**Layer 2 — hidden keywords.** Unlimited, invisible. Section 9. These feed search only.
They never appear as a filter or on a card. Because they are invisible they can be
unlimited at no cost to the interface. This is what makes the site feel intelligent
without a screen full of switches.

**Layer 3 — entry questions. Two, asked once, on the first screen.**

| Order | Question | Axis | Why |
|---|---|---|---|
| 1 | Who are you? | Role | Research shows people describe themselves this way — "I am a non-coder", not "I am intermediate". Easy to answer, easy to tag. |
| 2 | How much Claude do you already know? | Level | Sets the starting point in a sequence. |

**Time was cut on 2026-08-19. It was measured against the real 77 items, not guessed:**

| Questions asked | Items left, median across roles |
|---|---|
| Role only | 27 |
| Role + level | **6** |
| Role + level + time | **0** |

Half of every role/level/time combination returns nothing at all. And 85% of the catalogue
is already under an hour, so time barely separates anything. A third question mostly buys
an empty results page.

Time stays as a **refine filter** and as a **"shortest first" sort**, which is what people
actually want it for.

Topic, Format, Cost and Time are all refine filters. They appear after results, never
before. A person cannot choose a topic before they know which topics exist.

**Re-measure this if the catalogue grows past roughly 300 items.** A third question earns
its place only when role + level routinely leaves more than about 15 results.

**Decided:** question 1 asks role, not goal. Goals are what people actually want ("write
my thesis faster") but goals are unlimited and cannot become a fixed list. The search bar
handles goals instead, through the hidden layer. Role for the guided path, goal for
search. Both routes reach the same items.

## 7. Review tiers

Four tiers. The tier is visible on every item. The site never claims more checking than it
did.

| Tier | Value | Meaning | Who sets it |
|---|---|---|---|
| **Reviewed** | `reviewed` | Full content consumed **and** a person confirmed the judgment | Human |
| **AI reviewed** | `ai-reviewed` | Full content consumed by AI. No person checked it. | Gemini pipeline, or a research run for short text |
| **Previewed** | `previewed` | Syllabus, outline or free sample only | Research run |
| **Listed** | `listed` | Metadata only, content not checked | Research run |

Rank order everywhere: Reviewed > AI reviewed > Previewed > Listed. Items get promoted as
we process them.

**Who may claim what:**

- A **research run** is web search. It may claim `ai-reviewed` only for `docs` and
  `article` — short text pages it can read fully in one fetch. Never for `video`,
  `course`, `podcast`, `hands-on` or `repo`.
- The **Gemini pipeline** may claim `ai-reviewed` for any format, including video.
- Only a **person** may set `reviewed`. No automated stage may ever write it.

## 8. Gemini is the analysis engine

Gemini reads the content. Claude writes the rubric, the validation, the pipeline and the
site. The two jobs stay separate.

**Where Gemini runs:** in the pipeline only. Offline. Before publishing.

**Where Gemini never runs:** the website. No API key ships to the browser. No request
leaves the visitor's machine. The site stays static, with no backend and no running cost.
Hard rule.

**What it changes:** Gemini reads YouTube video directly, so videos reach a full review
instead of `listed`. Reviewing at scale becomes possible. Re-checking an item every six
months costs an API call, not a person's afternoon.

**What it does not change:**

- **Paywalls stay closed.** Gemini cannot open Udemy, Coursera, LinkedIn Learning, O'Reilly, Skillshare, Patreon or Skool. Those still cap at `previewed`.
- **A summary is not a judgment.** "Summarise this course" returns marketing copy in different words. See the rubric, section 10.
- **Gemini invents facts.** Nothing enters `items.json` without validation.

## 9. Data model

One file is the single source of truth: **`data/items.json`**. The pipeline is the only
thing that writes to it. The site only reads it.

### Visible fields — a person reads these

| Field | Notes |
|---|---|
| `id` | Stable slug |
| `title` | |
| `url` | Canonical URL at the original source, never an aggregator link |
| `source_id` | Points into `data/sources.yaml` |
| `author` | Person or organisation |
| `roles` | Array |
| `level` | One value |
| `topics` | Array |
| `format` | One value |
| `time` | One value |
| `cost` | One value |
| `language` | ISO code |
| `field` | Optional, only when genuinely domain-specific |
| `tier` | reviewed / ai-reviewed / previewed / listed |
| `summary` | What it teaches, in plain language |
| `who_for` | Who should watch this |
| `skip_if` | When not to bother. The differentiator. **May never be empty** |
| `published` | Date the content was published |
| `checked` | Date we last verified it. **Shown on the site** |
| `status` | live / dead / outdated |
| `sequence` | Optional. Position in a named ordered path |

### Hidden fields — never shown, used only by search

Written by Gemini. Generated, therefore cheap. Generate generously.

| Field | Type | What goes in it |
|---|---|---|
| `keywords` | 10–30 strings | Tools named, tasks covered, problems solved, the words the teacher actually uses. **Include beginner words and misspellings on purpose** |
| `questions` | 3–8 strings | Real questions this item answers, phrased as a person would ask: "how do I make Claude read my PDFs?" |
| `prerequisites` | array | What you must already know. Feeds sequencing |
| `teaches` | array | Concrete abilities after finishing. Abilities, not topics |
| `embedding` | array of floats | One vector per item. Stored in a separate file, loaded only on search |

Rules:

- No hidden field may contradict a visible field. Validation checks this.
- Never copy another site's description or review. Write our own or write nothing.
- Never invent an item, a link or a rating.
- Anything published more than about 12 months ago is flagged as possibly outdated.

## 10. The judgment rubric

The hardest part and the actual product. Gemini must be forced to criticise.

Every item needs an explicit answer to all six, or it does not ship:

1. **What does it teach?** Concrete abilities, not topics.
2. **Who should watch it?** One named kind of person.
3. **Who should skip it, and why?** May not be empty.
4. **How much of the running time is real content?** Flag anything that buries the material under an introduction, a sales pitch or repeated self-promotion.
5. **Is it still accurate?** Name any part that no longer matches the current Claude interface or features.
6. **Does it show its work?** Does the teacher demonstrate on a real task, or only talk?

**Rule:** a review with an empty `skip_if`, or a summary that reads like the sales page, is
rejected on ingest and re-run. Never repaired by hand.

## 11. Search — no AI at query time

The visitor types a sentence. The browser answers. No API call, no key, no cost. This
works because Gemini did the thinking earlier, offline, and wrote the result into the data
file.

**Stage one — keyword and synonym index.** Build first. Maps typed words to items through
`keywords` and `questions`. Small, fast, easy to debug. Handles "help me write my thesis"
because an item is tagged `thesis`, `academic-writing`, `literature-review`.

**Stage two — precomputed embeddings.** Build second. One vector per item; the browser
compares vectors and ranks by similarity. Understands full sentences and words we never
listed. Roughly 100 KB for 300 items, quantised, in a separate file.

**Constraint:** the embedding file loads after the page, never before. Search must never
delay first paint.

**Deferred:** a live AI answer on the site. Would need a backend. Not in version 1.

## 12. Sources

Defined in **`data/sources.yaml`** — 60+ sources in seven groups, each with its harvest
method, re-check cadence, and the best tier it can reach.

Priority order:

1. **Official Anthropic** — Academy, three doc sites, blogs, two YouTube channels, GitHub orgs. The backbone.
2. **Course platforms** — DeepLearning.AI, freeCodeCamp, Frontend Masters free; then Coursera, Udemy, Pluralsight, LinkedIn Learning, O'Reilly, edX, Udacity, DataCamp, Skillshare, Maven, plus AWS / Google Cloud / Microsoft academies.
3. **Independent and written** — ClaudeLog, Simon Willison, Peter Steinberger, GitHub awesome-lists, Reddit, Hacker News, Dev.to, named Substacks.
4. **Creator platforms** — Patreon, Skool, Gumroad, Teachable. Mostly capped at `listed`; paywalled with no public outline.
5. **Audio and other video** — independent YouTube channels, podcasts, conference talks. Short-form excluded.
6. **Academic and public sector** — university AI-literacy courses, Anthropic Campus, EU and national programs.
7. **Non-English** — a real gap, deliberately deferred.

Standing rules:

- Aggregators (Class Central, awesomeclaude.ai, awesome-lists) are **discovery seeds only**. Always verify at the original source.
- The blocklist of abandoned and fake repositories is enforced, not advisory.
- Always verify a YouTube channel by its RSS feed before listing it. One widely recommended "best Claude channel" had its last upload in 2015.
- If a source blocks us, record that as a fact on the source. Never silently skip it.

## 13. The pipeline

Runs on a schedule. Four stages.

1. **Discover** — work through `sources.yaml` in priority order. New candidate URLs append to a queue. One source per run.
2. **Extract** — fetch page, video, curriculum outline or repository metadata, using the method declared on that source.
3. **Judge** — Gemini applies the rubric (section 10), writes visible and hidden fields, assigns all six tags, sets the tier by what was actually available.
4. **Verify** — check every existing link is alive. Re-check items older than six months. Write a change report.

Output goes to `data/staging.json` and `reports/YYYY-MM-DD.md`. **Never straight to live.**
A person says "publish" and it merges into `items.json`.

Throughput: roughly 15–30 items per run, one source at a time. Collection is automatic;
publishing has a one-word human gate.

`scripts/validate-report.py` is the gate. Run it on every file before it moves forward.
Use `--pipeline` for Gemini output, no flag for research runs.

## 13b. Merging the 10 research files — decided 2026-08-19

Ten role research files will describe the same course many times. Anthropic Academy will
appear in the student file, the teacher file and the PM file at once.

1. **Merge, never duplicate.** One item, many roles. Match on canonical URL. Five copies of
   the same course would make the site look broken.
2. **Reports live in `research/reports/`.** Not loose in the project root.
3. **A merge script does the work:** read all ten files → merge by URL → run
   `scripts/validate-report.py` → write `data/items.json`.
4. **When two files describe the same course differently, the version with the better
   `skip_if` wins.** The other wording is kept in a note, never thrown away.

## 14. The site

Static HTML, CSS and JavaScript reading `items.json`. Client-side search and filters,
instant. Free static hosting. Mobile first. No backend, no API keys, no running cost.

### Visual direction

Reference: Anthropic's own design system, captured at
`https://styles.refero.design/style/d469cba4-c448-4a43-a033-883f8bfcdc42`
(checked 2026-08-19). Warm ivory canvas, editorial serif body text at 20px, sans for
interface chrome only, one clay accent reserved for the single most important action, flat
surfaces with hairline borders and no shadows.

**Typefaces.** Anthropic Serif, Sans and Mono are proprietary — drawn by Chester Jenkins of
BSPK, identity by Geist. **They are not sold.** The licensable ancestors:

| Role | Buy | Foundry |
|---|---|---|
| Serif — body text | Tiempos Text | Klim Type Foundry |
| Sans — interface chrome | Styrene B | Commercial Type |

Free fallback for prototyping: Source Serif 4 and Inter.

**Images and icons.** Anthropic uses vintage scientific illustration — botanical and
zoological plates in 19th-century field-guide style, warm-toned to sit inside the palette.
Iconography is minimal and in the same warm neutral family as the text.

**Rule: we copy no image, no icon and no illustration.** We take the *approach* — warm,
editorial, low density, illustration at hero scale only — and draw our own. An approach is
not owned. A drawing is.

**Deferred:** page layout, first-visit flow, card design.

## 15. Risks

| Risk | Response |
|---|---|
| ~~YouTube transcripts blocked~~ **CLOSED 2026-08-19** | Gemini reads video directly. Video items reach `ai-reviewed`, not `listed`. |
| Gemini returns a summary instead of a judgment | Empty `skip_if`, or a summary that reads like the sales page, is rejected on ingest and re-run. Never repaired by hand. |
| Gemini invents facts about content it read | Every claim validated against the source before it enters `items.json`. |
| Video processing cost grows without a limit | A monthly item budget and a per-job model choice. Both still open. |
| Link rot is unusually fast here — Anthropic renamed `docs.anthropic.com` and `anthropic-cookbook` inside one competitor's lifetime | The Verify stage exists for this. Date checked is shown publicly. |
| Curation drowning in submissions killed every large competitor | No public submissions in v1. |
| Popularity fills the site with viral beginner content | Popularity is a tiebreaker only, never a ranking signal. Accuracy first. |
| The whole thing rots if the schedule stops | Freshness is the product. If the pipeline stops, the site should say so rather than quietly go stale. |

## 16. Still open

- Prices and licence terms for Tiempos Text and Styrene B.
- Which Gemini model for which job, and a monthly budget rule.
- Page layout, first-visit flow, card design.
- Which named ordered paths to build first. The Anthropic free-course sequence is obvious.
- Target languages beyond English.
- Whether the certification warning is a page, a banner or a tag.
