# Landscape map, part 2: competitors, learner demand, failure patterns

**Researched:** 2026-08-16. Every URL below was fetched or seen in live search results on that date.
**Method:** web search + direct page fetch + GitHub API + Reddit via browser (Reddit blocks automated fetchers).

---

## A. Who already built something like this

| Site | Covers | Organised by | Reviews or just links? | Maintained? | Business model |
|---|---|---|---|---|---|
| [awesomeclaude.ai](https://awesomeclaude.ai/) + [webfuse-com/awesome-claude](https://github.com/webfuse-com/awesome-claude) | Claude-specific: SDKs, MCP, Claude Code, cheatsheet, an "Educational Resources" section (12 Anthropic Academy courses, video tutorials, ~4 community guides) | Flat topic sections. **No level/role/field filter, no search** | One-line descriptions. No judgment, no "who it's for" | Yes — 1,639 stars, last push 2026-08-10; **196 open PRs** backlog | Free list, funded as marketing for Webfuse (embedded "Start free demo" CTA above the fold) |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Claude Code only: slash commands, CLAUDE.md files, CLI tools, workflows | Sections by artifact type | Links + short blurbs | Very active — 52,392 stars, pushed 2026-08-16, but **860 open issues** (submission queue) | None visible |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Claude Skills | Categories | Links | 72,571 stars, pushed 2026-08-10, **1,122 open PRs** — curation is drowning | Marketing for Composio |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | Claude Skills | Categories | Links | Slipping — 14,668 stars, last push **2026-04-28** (~4 mo), 681 open PRs | Free |
| [claudeskill.net/learn](https://www.claudeskill.net/learn) | "Claude Skill Hub" — prompts, tools, learning | Tags: Beginner/Intermediate/Advanced + a "Use case:" line | Level tags + use-case line — **closest thing to judgment found** | **Stale.** Only 6 learn entries, mostly generic. Links `docs.anthropic.com` and `anthropics/anthropic-cookbook`, **both now 301 redirects**. Latest Wayback snapshot 2026-06-06 | None visible |
| [claudeainews.com/courses](https://www.claudeainews.com/courses) | Claims a curated Claude course catalogue across 6 tracks | 6 named tracks | Promises reviews | **Empty.** Page says the first reviewed batch lands "within the next few weeks". Zero courses. Not in Wayback at all | States explicitly: no paid placements |
| [intuitionlabs.ai](https://intuitionlabs.ai/articles/claude-cowork-training-courses-directory) | Claude Cowork training only | Long-form article: official docs, community guides, video/courses, workshops, case studies | Prose commentary | One-off article, not a maintained directory | Lead-gen |
| [classcentral.com/subject/claude](https://www.classcentral.com/subject/claude) | **659 Claude courses**, dedicated taxonomy node under AI Models > Anthropic Claude | Filters: free / certificate / universities / **level** / **duration** / language / provider / sort by rating. 434 followers | Provider-supplied descriptions + aggregated star ratings + its own 250K user reviews. **No editorial "why this / who for"**, no date-checked, **no role or field axis** | Yes, very. 250K courses, 100M unique users | [Stated](https://www.classcentral.com/about): advertising + affiliate links; sponsored results marked |
| [coursesity.com](https://coursesity.com/search?query=claude) | Course aggregator | — | — | **Zero Claude coverage** — search returns "No courses found!" | Affiliate |
| [roadmap.sh](https://roadmap.sh/roadmaps) | 94 roadmaps incl. [Claude Code](https://roadmap.sh/claude-code), [Vibe Coding](https://roadmap.sh/vibe-coding), [Prompt Engineering](https://roadmap.sh/prompt-engineering), [AI Agents](https://roadmap.sh/ai-agents), [AI Product Builders](https://roadmap.sh/ai-product-builder) | Node graph + **"Role based" vs "Skill based" split**; AI Tutor chat per roadmap | Node-level resource links, no reviews | Very active — 364K GitHub stars, 2.8M users | Free + paid accounts, sponsorship |
| [datacamp.com/blog/best-resources-learn-claude](https://www.datacamp.com/blog/best-resources-learn-claude) | 12 Claude resources, 2026-05-12 | TL;DR table with **Type / Level / Best for**, a 3-stage learning path, then a **role-based decision framework** (non-coder in Excel, PM/designer, data scientist, production engineer) | **Genuinely opinionated** — each entry says what it is good for and where it fits | Fresh | Content marketing — **every entry links to DataCamp's own content** |
| [anthropic.skilljar.com](https://anthropic.skilljar.com/) | 20 official free courses | Course list | Official, no third-party comparison | Current | Free, first-party |

### The gap, stated plainly

Nobody combines all four of:

1. Claude-specific **and** non-developer scope
2. Filters by level / field / role
3. An editorial judgment per item
4. A visible "date checked"

Class Central has the filters but no judgment and no role axis. DataCamp has the judgment but only sells its own catalogue. The awesome-lists have breadth, zero judgment, and are developer-only.

---

## B. How learners actually search and ask

All Reddit threads below verified in-browser 2026-08-16.

### Absolute-beginner entry point

- **"I am a completely newbie and frankly not a young bird anymore. There is a feeling that I have already missed out on AI. If I have to start somewhere with Claude learning, where should I start?"** — 53 pts, 63 comments, 2026-07-25 — https://www.reddit.com/r/ClaudeAI/comments/1v61kb7/
  Body: YouTube is more overwhelming than the Claude console itself; poster has logic but no coding; not much money for experiments.
- "For a complete N00b, what's the best way to dive in and learn Claude?" — 37 comments, 2026-07-13 — https://www.reddit.com/r/ClaudeAI/comments/1uvez0g/ — top answer (29 pts) is just "ask Claude."
- "How to start learning Claude as an absolute beginner to become an expert?" — 39 pts, 47 comments, 2026-02-25 — https://www.reddit.com/r/ClaudeAI/comments/1re5a8g/
- "Best way to go from beginner to advanced when learning about Ai?" — 83 pts, 88 comments, 2026-03-28 — https://www.reddit.com/r/ClaudeAI/comments/1s5z5oq/

### Asking for curated resources by name

- "Building Expertise in Claude - Seeking Quality Learning Resources" — 21 comments, 2026-05-17 — https://www.reddit.com/r/ClaudeAI/comments/1tfiagm/
- "Best resources to actually understand Claude beyond basic prompting — agents, connectors, automations?" — 2026-03-31 — https://www.reddit.com/r/ClaudeAI/comments/1s8n1r8/
- "What's the best free course to learn Claude Code?" — 2026-07-30 — https://www.reddit.com/r/ClaudeAI/comments/1vaxfxj/ — poster explicitly wants practical/hands-on over theory.
- "Best Claude course for intermediate users" — https://www.reddit.com/r/ClaudeAI/comments/1uaqwhs/
- **"Beginner roadmap for Anthropic's free courses: What's the best order and cost?"** — https://www.reddit.com/r/ClaudeAI/comments/1sc6wbw/ — the question is **sequencing**, plus whether free courses can be finished without paying for API credits.
- "Any good/up-to-date tutorials on how to use advanced CC features?" — 2026-04-17 — https://www.reddit.com/r/ClaudeAI/comments/1so30ar/

### Complaints about existing tutorials

- **"New to Claude – what's the best way to actually get started? (tired of YouTube grifters)"** — 27 comments, 2026-07-15 — https://www.reddit.com/r/ClaudeAI/comments/1ux75g1/ — body complains every video spends ten minutes on an "AI agency making $40k/month" story before saying anything useful.
- **"Is anyone else overwhelmed by how many GenAI courses exist right now?"** — r/learnmachinelearning, 2026-04-08 — https://www.reddit.com/r/learnmachinelearning/comments/1sfz5zy/ — every course either goes too deep into math or stays too surface level; top reply agrees there is no middle ground. (One reply is an affiliate pitch with a discount code — the "curation" people find is often paid.)
- "What's with all the claude-fluencers" — 30 pts, 28 comments, 2026-04-12 — https://www.reddit.com/r/ClaudeAI/comments/1sjnq12/ — a data scientist asks why the optimal Claude workflow is reinvented every week; replies blame the YouTube algorithm.
- In the newbie thread above, a 25-pt reply calls YouTube a swamp — the more you watch the more you get buried, most videos are shallow, and **every ~6 months everything changes and you feel like you're starting over**.
- "Escaping Tutorial Hell: Can I use Claude as a 'Strict Mentor' instead of a code generator?" — https://www.reddit.com/r/ClaudeAI/comments/1tssdny/
- "Complete Beginner in AI – Looking for the Best Resources and Advice" — 24 pts, 29 comments, 2026-07-16 — https://www.reddit.com/r/learnmachinelearning/comments/1uy4dv9/

### How people describe themselves — occupation, not skill level

**"Non-coder" / "non-technical" is by far the biggest cluster:**

- "Non-coder doctor here — rebuilt my department's website…" — 854 pts — https://www.reddit.com/r/ClaudeAI/comments/1ugcnkd/
- "Non coders: What's something really helpful you made with Claude?" — 237 pts, 295 comments — https://www.reddit.com/r/ClaudeAI/comments/1tely7p/
- "Any tip from technical people to us non-technicals on how to make the most out of claude?" — https://www.reddit.com/r/ClaudeAI/comments/1ufchrt/
- "Feeling left behind in the AI race as a non-technical person - genuine advice needed" — https://www.reddit.com/r/ClaudeAI/comments/1tfxe5n/
- "The gap between what technical and non-technical people get from AI is huge now" — 581 pts — https://www.reddit.com/r/ClaudeAI/comments/1spnb80/

**Other named roles:**

- PM — https://www.reddit.com/r/ClaudeAI/comments/1sk4gz3/ · https://www.reddit.com/r/ClaudeAI/comments/1txt5p9/
- Teacher — https://www.reddit.com/r/ClaudeAI/comments/1s7iwex/ · https://www.reddit.com/r/ClaudeAI/comments/1oj60c3/
- Designer — https://www.reddit.com/r/ClaudeAI/comments/1rc44mp/
- Engineer (non-software, civil) — https://www.reddit.com/r/ClaudeAI/comments/1s2b34m/
- 3D artist — https://www.reddit.com/r/ClaudeAI/comments/1vck1bu/
- Entrepreneur / career-switcher — https://www.reddit.com/r/ArtificialInteligence/comments/1tjhfso/ · https://www.reddit.com/r/learnmachinelearning/comments/1uo3iq0/

### The benchmark to beat

The single most common **answer** in these threads is "just ask Claude" or "just start a small project." Any directory has to beat that — which means being **faster than asking Claude**: judged, sequenced, and current.

---

## C. Failure patterns — how these directories die

- **Submission flood beats curation capacity.** ComposioHQ/awesome-claude-skills: **1,122 open PRs**. travisvn/awesome-claude-skills: **681**. jqueryscript/awesome-claude-code: **458**. webfuse-com/awesome-claude: **196**. hesreallyhim/awesome-claude-code: **860 open issues**. (GitHub API, 2026-08-16.) All "alive" but functionally unable to accept contributions.
- **Once the maintainer stops, the list rots but stays visible in search.** Real cases, none marked archived, none warning the visitor:
  - [luspr/awesome-ml-courses](https://github.com/luspr/awesome-ml-courses) — 3,103 stars, last push **2024-12-12**
  - [Niraj-Lunavat/Artificial-Intelligence](https://github.com/Niraj-Lunavat/Artificial-Intelligence) — 1,857 stars, last push **2023-04-20**
  - [openbestof/awesome-ai](https://github.com/openbestof/awesome-ai) — 581 stars, last push **2024-05-04**
- **Copy-paste clones with no upkeep.** [ai-for-developers/awesome-claude](https://github.com/ai-for-developers/awesome-claude) — 80 stars, pushed 2026-02-24, and its GitHub description still reads "A curated list of awesome cloud computing resources." The template was never edited.
- **Link rot is unusually fast in this niche.** claudeskill.net links `docs.anthropic.com` (now 301 → platform.claude.com/docs) and `anthropics/anthropic-cookbook` (now 301 → anthropics/claude-cookbooks). Anthropic renamed both inside that site's lifetime.
- **Announcing a curated catalogue is easy; shipping one is not.** claudeainews.com/courses has six well-defined tracks, a no-paid-placement policy, and **zero courses**.
- **Generic aggregators do not cover the tool.** Coursesity returns no results for "claude." Class Central covers it (659 courses) but with no editorial layer — the "which of these 659 is worth my Saturday" problem is untouched.
- **A meta-list codified the decay rate.** [zhimin-z/awesome-awesome-artificial-intelligence](https://github.com/zhimin-z/awesome-awesome-artificial-intelligence) excludes any list "not actively maintained (> 12 months)" or under 1k stars — an explicit admission that 12 months of silence kills a list.

**Unverified:** a competitor blog claims Futurepedia has stale listings and out-of-date categories. Could not verify independently, and the source sells a rival directory.

---

## What this changes about our design

1. **Role beats level as the primary axis.** People say "I'm a non-coder doctor", not "I'm intermediate". Our filters should lead with occupation.
2. **"Non-technical" is the biggest underserved segment** and every existing Claude directory is developer-only.
3. **Sequencing is an explicit, repeated request** — "what order should I do the free Anthropic courses in?" Nobody answers it.
4. **"Date checked" is a real differentiator**, not a nice-to-have. Every competitor lacks it, and link rot here is fast enough to be visible within months.
5. **Grifter-filtering is a feature.** People ask for it by name. A "skip this, it's 10 minutes of hype" note has real value.
6. **Do not accept public submissions early.** The submission flood is what killed curation on every large list.
7. **We must beat "just ask Claude."** Judgment + sequencing + freshness is the only way.
