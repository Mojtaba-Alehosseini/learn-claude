# Landscape map, part 1: who publishes Claude learning content

**Researched:** 2026-08-16. Every URL below was fetched or seen in live search results on that date.
**Method:** web search + direct page fetch + GitHub API (stars, last push) + YouTube RSS feeds (upload cadence).

---

## 1. Official Anthropic

### Hubs, docs, blogs

| Name | URL | Type | Free/Paid | Notes |
|---|---|---|---|---|
| Anthropic Academy (hub) | https://www.anthropic.com/learn | Course hub | Free | Landing page; links to Skilljar catalog |
| Anthropic Courses (Skilljar) | https://anthropic.skilljar.com/ | LMS, 20 courses + 1 path | Free, certificates | Needs a Skilljar account, not an Anthropic one |
| Course browser (with metadata) | https://claude.com/resources/courses | Filterable catalog | Free | **Best machine-readable source** — exposes lecture count + video length per course |
| Tutorials | https://claude.com/resources/tutorials | Video + written | Free | |
| Claude Platform docs | https://platform.claude.com/docs/en/home | Docs | Free | API/SDK |
| Claude Code docs (separate site) | https://code.claude.com/docs/en/overview | Docs | Free | Incl. `/en/best-practices` |
| Help Center | https://support.claude.com/en/ | Docs | Free | End-user, non-developer |
| Engineering blog | https://www.anthropic.com/engineering | Blog | Free | Source of the widely-cited "effective context engineering" and "writing effective tools" posts |
| Claude blog | https://claude.com/blog | Blog | Free | |
| Newsroom | https://www.anthropic.com/news | Blog | Free | |
| AI Fluency newsletter | Signup on https://www.anthropic.com/learn | Newsletter | Free | Quarterly |

### Anthropic Academy course list

All free. Verified from https://claude.com/resources/courses. Prefix URLs with `https://anthropic.skilljar.com`.

| Course | Path | Lectures | Video length |
|---|---|---|---|
| Claude 101 | /claude-101 | 12 | 1 hr |
| Claude Code 101 | /claude-code-101 | 12 | 1 hr |
| Claude Code in Action | /claude-code-in-action | 15 | 1 hr |
| Claude Platform 101 | /claude-platform-101 | 12 | 1 hr |
| Building with the Claude API | /claude-with-the-anthropic-api | 84 | 8.1 hr |
| Introduction to Claude Cowork | /introduction-to-claude-cowork | n/a | metadata blank |
| Introduction to agent skills | /introduction-to-agent-skills | 6 | 30 min |
| Introduction to subagents | /introduction-to-subagents | 4 | 20 min |
| Introduction to Model Context Protocol | /introduction-to-model-context-protocol | 16 | 1 hr |
| MCP: Advanced Topics | /model-context-protocol-advanced-topics | 15 | 1.1 hr |
| Claude with Amazon Bedrock | /claude-in-amazon-bedrock | 85 | 8 hr |
| Claude on Google Cloud (Vertex AI) | /claude-with-google-vertex | 85 | 8 hr |
| AI Fluency: Framework & Foundations | /ai-fluency-framework-foundations | 14 | 1.1 hr |
| AI Fluency for educators | /ai-fluency-for-educators | 4 | 24 min |
| AI Fluency for students | /ai-fluency-for-students | 5 | 30 min |
| Teaching AI Fluency | /teaching-ai-fluency | 7 | 36 min |
| AI Fluency for nonprofits | /ai-fluency-for-nonprofits | 9 | 54 min |
| AI Fluency for Small Businesses | /ai-fluency-for-small-businesses | 9 | ~0.9 hr |
| AI Fluency for Builders | /ai-fluency-for-builders | 10 | 1 hr |
| AI Fluency for pK-12 Educators (path, 2 courses) | /path/ai-fluency-for-pk-12-educators | 8 | 1 hr |
| AI capabilities and limitations | /ai-capabilities-and-limitations | 13 | 15 min |

### Certification — real, but partner-gated

Source: https://www.pearsonvue.com/us/en/anthropic.html (page last updated 2026-07-08)

| Exam | Registration URL |
|---|---|
| Claude Certified Associate – Foundations (CCAO-F) | https://anthropic-partners.skilljar.com/claude-certified-associate-foundations-certification |
| Claude Certified Architect – Foundations (CCAR-F) | https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification |
| Claude Certified Architect – Professional (CCAR-P) | https://anthropic-partners.skilljar.com/claude-certified-architect-professional-certification |
| Claude Certified Developer – Foundations (CCDV-F) | https://anthropic-partners.skilljar.com/claude-certified-developer-foundations-certification |

- Delivered by Pearson VUE (test center or OnVUE online). Badges via Credly.
- **Caveat:** Pearson's page states certification is open to organizations in the Claude Partner Network, and prep training is for Partner Network members. **Not verified as open to the general public.**
- Retake policy: 14/30/90-day waits; max 4 attempts per rolling 12 months.
- **UNVERIFIED:** prices ($99–$175), "120 min / 720 pass score / 12-month validity" appear only in third-party SEO blogs, not on Pearson or Anthropic pages.
- Partner Academy: https://anthropic-partners.skilljar.com/

### Official YouTube — two channels, different jobs

| Channel | URL | Channel ID | Cadence (latest upload) | Content |
|---|---|---|---|---|
| Anthropic | https://www.youtube.com/@anthropic-ai | UCrDwWp7EBBv4NwvScIpBDOA | ~1/month (2026-08-10) | Research, model launches, interpretability. **Not tutorials.** |
| Claude | https://www.youtube.com/@claude | UCV03SRZXJEz-hchIAogeJOg | Several/week (2026-08-14) | Product + feature how-tos. **The official teaching channel.** |

### Official GitHub

Stars and last-push via GitHub API, 2026-08-16.

| Repo | Stars | Last push | Status |
|---|---|---|---|
| anthropics/skills | 169,582 | 2026-08-13 | Active |
| anthropics/claude-code | 141,582 | 2026-08-14 | Active |
| anthropics/claude-cookbooks | 51,555 | 2026-08-14 | Active (renamed from `anthropic-cookbook`, old URL 301s) |
| anthropics/prompt-eng-interactive-tutorial | 37,678 | 2026-03-01 | Mildly stale (~5.5 mo) |
| **anthropics/courses** | 22,631 | **2025-11-13** | **STALE (~9 mo)** — superseded by Anthropic Academy |
| anthropics/claude-quickstarts | 17,444 | 2026-08-06 | Active (renamed from `anthropic-quickstarts`) |
| anthropics/claude-agent-sdk-python | 7,898 | 2026-08-14 | Active |
| modelcontextprotocol/servers | 89,601 | 2026-08-10 | Active |
| modelcontextprotocol/modelcontextprotocol | 8,971 | 2026-08-14 | Active (spec) |

### Official community

- Discord: https://discord.com/invite/6PPFFzqPDZ
- Reddit: https://www.reddit.com/r/ClaudeAI/ (~1M members per ClaudeLog)
- Events: https://luma.com/claudecommunity
- Ambassadors: https://claude.com/community/ambassadors
- Campus: https://claude.com/programs/campus
- Community hub: https://claude.com/community (33 countries, 67 cities)

---

## 2. Major platform courses

| Course | URL | Provider / Instructor | Free/Paid | Length | Level |
|---|---|---|---|---|---|
| Claude Code: A Highly Agentic Coding Assistant | https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant | DeepLearning.AI × Anthropic / Elie Schoppik | Free | 2h | Intermediate |
| MCP: Build Rich-Context AI Apps with Anthropic | https://www.deeplearning.ai/courses/mcp-build-rich-context-ai-apps-with-anthropic | DeepLearning.AI × Anthropic / Elie Schoppik | Free | 1h58m | Intermediate |
| Agent Skills with Anthropic | https://www.deeplearning.ai/courses/agent-skills-with-anthropic | DeepLearning.AI × Anthropic / Elie Schoppik | Free | 2h19m | Beginner |
| Building toward Computer Use with Anthropic | https://www.deeplearning.ai/courses/building-toward-computer-use-with-anthropic | DeepLearning.AI × Anthropic / Colt Steele | Free | 1h47m | Beginner |
| Building with the Claude API | https://www.coursera.org/learn/building-with-the-claude-api | Coursera / **Anthropic** (official) | Paid (sub) | 7 modules | Dev |
| Real-World AI for Everyone (3-course Specialization) | https://www.coursera.org/specializations/real-world-ai-for-everyone | Coursera / **Anthropic + AWIT**, Dan Mellott | Paid | 3 courses | Beginner |
| Claude Code: Software Engineering with Generative AI Agents | https://www.coursera.org/learn/claude-code | Coursera / Vanderbilt, Jules White | Paid | ~5 hr | Beginner |
| Generative AI Software Engineering (Specialization) | https://www.coursera.org/specializations/generative-ai-software-engineering | Coursera / Vanderbilt | Paid | multi-course | — |
| **Free Claude Code Course** | https://frontendmasters.com/courses/claude-code/ | Frontend Masters ("Master.dev") / **Lydia Hallie** (Claude Code team) | **Free** | 16 lessons, 1.9 hr, 4.7★ | Intermediate |
| Claude Code path (6 courses) | https://www.pluralsight.com/paths/claude-code | Pluralsight | Paid | 7 hr total | Intermediate |
| ├ Introduction to Claude Code | /courses/claude-code-introduction | Jon Friskics | Paid | 43m (2026-07-06) | |
| ├ Claude Code in Practice | /courses/claude-code-practice | Sarah Holderness | Paid | 47m (2026-01-30) | |
| ├ Advanced Claude Code | /courses/advanced-claude-code | Karoly Nyisztor | Paid | 1h27m (2026-01-21) | |
| ├ Building with Claude Agent SDK | /courses/building-claude-agent-sdk | Dan Tofan | Paid | 1h34m (2026-07-17) | |
| ├ Claude Code Testing and Debugging | /courses/claude-code-testing-debugging | Laurentiu Raducu | Paid | 1h9m (2026-08-07) | |
| └ Automating Workflows with Claude Code | /courses/automating-workflows-claude-code | Bogdan Sucaciu | Paid | 1h39m (2026-07-08) | |
| Introduction to Claude | https://www.pluralsight.com/courses/introduction-claude | Pluralsight | Paid | upd. 2026-04-10 | Beginner |
| First Look: Claude Cowork | https://www.pluralsight.com/courses/claude-cowork-first-look | Pluralsight | Paid | upd. 2026-02-19 | Beginner |
| Claude Code Full Course | https://www.freecodecamp.org/news/claude-code-full-course/ | freeCodeCamp (YouTube) | Free | ~5 hr | Beginner→adv |
| Claude Code for Beginners | https://www.freecodecamp.org/news/claude-code-for-beginners/ | freeCodeCamp (YouTube) | Free | ~4 hr | Beginner |
| AI Coder: Complete Claude Code & Coding Agents Course | https://www.udemy.com/course/ai-coder-from-vibe-coder-to-agentic-engineer/ | Udemy / Ligency + Ed Donner | Paid | 16.5 hr, 95 lectures, 4.7★ (9,858 reviews) | All levels |
| A Practical Intro to AI Agents and Agentic AI (Cowork) | https://www.udemy.com/course/practical-intro-to-ai-agents-agentic-generative-ai-with-claude-cowork/ | Udemy / Ligency + Alex Honchar | Paid | 3.5 hr, 49 lectures, 4.6★ | Beginner |
| Claude Code (cohort hub) | https://maven.com/courses/claude-code | Maven | Paid, live cohort | multi-week | Varies |
| Claude Code for Product Managers | https://maven.com/aman-khan/claude-code-for-product-managers | Maven / Aman Khan, Eric Xiao | Paid | cohort | PM |

### LinkedIn Learning — partly unverified

Topic page exists: https://www.linkedin.com/learning/topics/claude. LinkedIn blocks automated fetching, so the titles below come from **search-result snippets only** — durations and levels unverified.

- Claude Code in Action by Anthropic — /learning/claude-code-in-action-by-anthropic (Anthropic-produced, redistributed)
- Everyday Productivity with Claude Cowork — /learning/everyday-productivity-with-claude-cowork
- Claude Code 101: From Prompt to Product — /learning/claude-code-101-from-prompt-to-product
- Claude Code for Everyday Professionals — /learning/claude-code-for-everyday-professionals-build-productivity-tools-with-plain-english
- Maximize Your Claude Code Programming Productivity — /learning/maximize-your-claude-code-programming-productivity

### Negative findings

- **Scrimba: no Claude-specific course.** Only SEO articles and a generic AI Engineer Path that covers MCP but isn't Claude-specific.
- **O'Reilly, Educative, Codecademy, egghead:** nothing Claude-specific found. Unverified either way.

---

## 3. YouTube channels

Activity verified by pulling each channel's RSS feed on 2026-08-16.

| Channel | URL | Claude focus | Cadence (latest upload) | Level |
|---|---|---|---|---|
| Claude (official) | https://www.youtube.com/@claude | 100% | Several/week (2026-08-14) | Beginner–int |
| Anthropic (official) | https://www.youtube.com/@anthropic-ai | High, but research not teaching | ~monthly (2026-08-10) | All |
| IndyDevDan | https://www.youtube.com/@indydevdan | **Very high** — agentic engineering, Claude Code, skills, subagents | Weekly, Mondays (2026-08-10) | Intermediate–advanced |
| Cole Medin | https://www.youtube.com/@ColeMedin | High — Claude Code skills | 2–3/week (2026-08-14) | Intermediate |
| Nick Saraev | https://www.youtube.com/@nicksaraev | High — long-form Claude Code courses (6 hr, 2026-08-08) | ~weekly | Beginner–int, business angle |
| AI Jason | https://www.youtube.com/@AIJasonZ | High — context engineering, agent loops | ~weekly, **gap since 2026-07-20** | Advanced |
| Simon Scrapes | https://www.youtube.com/@simonscrapes | High — Cowork/memory for business users | ~2/month (2026-08-13) | Beginner, non-dev |
| Nate Herk \| AI Automation | https://www.youtube.com/@NateHerk | Medium — comparisons | ~daily (2026-08-14) | Beginner–int |
| Riley Brown | https://www.youtube.com/@RileyBrownAI | Medium — Claude vs competitors | Several/week (2026-08-15) | Beginner |
| AICodeKing | https://www.youtube.com/@AICodeKing | Medium — benchmarks | Daily (2026-08-15) | Beginner, hype-y |
| Matthew Berman | https://www.youtube.com/@matthew_berman | Medium — general AI news | Frequent | Beginner |
| Greg Isenberg | https://www.youtube.com/@GregIsenberg | Medium — founder angle | Several/week (2026-08-12) | Business |
| Wes Roth / David Ondrej / Tech With Tim / Sabrina Ramonov | verified live, all active Aug 2026 | Low–medium | Frequent | Beginner |

### Do not use — unverified or fabricated

- **"Jack Roberts"** — recommended by a listicle, but https://www.youtube.com/@jackroberts is dead (last upload 2015). Wrong handle or invented.
- **"Chase Hannegan"** — handle did not resolve.
- **Sean Kochel** — channel resolves (UCwmf8kPLoppCmp0V5MHmr_w) but returned no RSS entries; activity unverified.
- Subscriber/view counts from listicles could not be verified — YouTube blocks scraping those numbers.

---

## 4. Newsletters, blogs, independent educators

| Name | URL | Type | Free/Paid | Claude focus | Notes |
|---|---|---|---|---|---|
| **ClaudeLog** | https://claudelog.com/ | Community docs/tutorials | Free (sponsored) | **100% Claude Code** | **Best independent resource found.** By "InventorBlack" (Wilfred Kasekende), Claude Ambassador + r/ClaudeAI mod. Mechanics, CLAUDE.md vault, MCP, changelog. Last updated 2026-08-12. Explicitly not Anthropic-affiliated. |
| Simon Willison's Weblog | https://simonwillison.net/ | Blog | Free | Medium–high | Broad LLM coverage; live-blogged Code w/ Claude 2026. High trust, not Claude-only |
| Peter Steinberger | https://steipete.me/ | Blog | Free | High | Advanced Claude Code workflows |
| Latent.Space | https://www.latent.space/ | Newsletter/podcast | Freemium | Medium | AI eng. broadly, frequent Anthropic guests |
| Chain of Thought (Every) | https://every.to/chain-of-thought | Newsletter | Paid | Medium | Dan Shipper; agent workflows |
| Elevate (Addy Osmani) | https://addyo.substack.com/ | Newsletter | Freemium | Medium | AI-assisted engineering |
| Nate's Newsletter | https://natesnewsletter.substack.com/ | Newsletter | Freemium | Medium | |
| Awesome Claude (site) | https://awesomeclaude.ai/ | Directory | Free | High | Aggregator: tools, cheatsheet, skills, MCP servers |

**Anthropic people worth tracking as sources** (not standalone channels): Boris Cherny (Head of Claude Code), Elie Schoppik (Head of Technical Education), Colt Steele (Head of Curriculum), Maggie Vo (Head of Education), Lydia Hallie (Claude Code team).

**Low signal — flagged, do not trust without independent verification:** a large cluster of Substack "Claude Code guide hub" newsletters (buildtolaunch, karozieminski, claudecodemasterclass, elshadk, aimaker) and SEO sites (claudecertificationguide.com, anthropiccertifications.com, claudepractice.com, claudecodeguides.com, developereducators.com, thesearchsherpa.com, freeacademy.ai). These rank well but are affiliate/SEO-driven and repeat unverified figures.

---

## 5. GitHub "awesome" lists & community collections

Stars and last-push verified via GitHub API, 2026-08-16.

| Repo | URL | Stars | Last push | Verdict |
|---|---|---|---|---|
| hesreallyhim/awesome-claude-code | https://github.com/hesreallyhim/awesome-claude-code | **52,391** | 2026-08-16 | **The canonical list.** Actively maintained |
| travisvn/awesome-claude-skills | https://github.com/travisvn/awesome-claude-skills | 14,668 | 2026-04-28 | Good; ~3.5 mo since update |
| davila7/claude-code-templates | https://github.com/davila7/claude-code-templates | 30,255 | 2026-08-16 | Active; CLI tool + templates |
| zebbern/claude-code-guide | https://github.com/zebbern/claude-code-guide | 4,571 | 2026-08-15 | Active; beginner→power-user |
| rohitg00/awesome-claude-code-toolkit | https://github.com/rohitg00/awesome-claude-code-toolkit | 2,516 | 2026-05-12 | Semi-active (~3 mo) |
| langgptai/awesome-claude-prompts | https://github.com/langgptai/awesome-claude-prompts | 5,407 | 2026-02-28 | **Stale (~5.5 mo)** |
| punkpeye/awesome-mcp-servers | https://github.com/punkpeye/awesome-mcp-servers | **92,398** | 2026-08-03 | Largest MCP list, active |
| wong2/awesome-mcp-servers | https://github.com/wong2/awesome-mcp-servers | 4,264 | 2026-07-13 | Active |
| subinium/awesome-claude-code | https://github.com/subinium/awesome-claude-code | 113 | 2026-04-25 | Low signal; **name collision** with the 52k repo |
| jmanhype/awesome-claude-code | https://github.com/jmanhype/awesome-claude-code | 22 | 2026-03-25 | Low signal; **name collision** |
| win4r/Awesome-Claude-MCP-Servers | https://github.com/win4r/Awesome-Claude-MCP-Servers | 85 | **2024-12-01** | **ABANDONED (~20 months)** — do not list |

---

## Takeaways

1. **Anthropic's own catalog is the strongest, and it is all free** — 20 courses + certificates. Any directory that does not lead with `claude.com/resources/courses` is doing it wrong. That page also exposes lecture counts and lengths, so it is the best machine-readable seed for our pipeline.
2. **Three separate official doc sites now** — `platform.claude.com/docs` (API), `code.claude.com/docs` (Claude Code), `support.claude.com` (end users). Easy to conflate; our data model should not.
3. **Two official YouTube channels with different jobs** — @claude teaches, @anthropic-ai announces.
4. **Certification exists but is partner-gated.** A whole SEO industry sells prep for exams most readers cannot sit. This deserves an explicit warning page on our site — it is a real, unmet user need.
5. **Best free non-Anthropic content:** four DeepLearning.AI courses, Frontend Masters' Lydia Hallie course, freeCodeCamp's two YouTube courses. ~15 free hours from credible instructors.
6. **`anthropics/courses` (22.6k stars) is 9 months stale** and still a top GitHub hit — flag as superseded.
7. **The "best Claude YouTube channels" listicle ecosystem is unreliable.** One widely recommended channel's last upload was 2015. Verify every channel by its RSS feed before listing it.
