# Claude Learning Content for Designers & Creatives — Research Report

**Checked:** 2026-08-20 · **Suggested filenames:** `claude-research-designer-2026-08-20.md` and `claude-research-designer-2026-08-20.json`
**Audience:** UX/UI designers, graphic designers, illustrators, 3D artists, creative directors learning Anthropic's Claude
**Scope note:** Claude is a text/code assistant, **not** an image generator. Midjourney/Stable-Diffusion content is excluded unless a genuine Claude workflow is central.

## TL;DR
- The best starting point is Anthropic's own free material: the official **Design plugin** (7 open-source skills — accessibility-review, design-critique, design-handoff, design-system, research-synthesis, user-research, ux-copy), the free tutorial **"Using Claude Design for prototypes and UX,"** and the free **Introduction to Claude Cowork** Academy course. These are the most accurate and least likely to go stale because Anthropic updates them as the products change.
- The strongest *craft-respecting, do-not-just-watch* content comes from practising designers documenting real ships: **Kris Puckett** (Stripe) building the Epilogue iOS app in Claude Code, and **Meaghan Choi** (Anthropic's Claude Code design lead) demoing her actual daily setup. As Puckett puts it in his Epilogue essay, *"I realized the bottleneck was never coding ability. It was articulation. The ability to describe what I wanted clearly enough that something else could build it."*
- Beware two large traps: (1) "AI for designers" content that is really Midjourney/image-gen, and (2) Claude Design walkthroughs that show a beautiful prototype and skip accessibility, responsive behaviour, and real data. Prefer content that treats Claude as a capable junior inside a real design process.

## Key Findings
- Claude's design ecosystem has three surfaces designers care about: **Claude Design** (Anthropic Labs prototyping tool, launched April 17, 2026, powered by Claude Opus 4.7 — "Anthropic's most capable generally available vision model" per launch-day coverage; Figma stock reportedly fell ~7% on launch day), **Claude Code** (terminal/agent tool used for prototyping and shipping), and **Cowork** (desktop agent for files, research and handoff). Content older than ~12 months predates all three and is likely outdated.
- The **Figma MCP server** is the officially supported bridge. Figma's Help Center article "Claude Code and Figma: Set up the MCP server" documents both the remote and desktop server options for the Claude Code plugin + Agent Skills (install via `claude plugin install figma@claude-plugins-official` [GitHub](https://github.com/mcp/com.figma.mcp/mcp)  [Substack](https://designexplained.substack.com/p/how-to-send-your-app-code-to-figma) ). A cheaper community route uses Chrome DevTools instead of the full MCP.
- The **official Design plugin** (repo `anthropics/knowledge-work-plugins`, 23.2k GitHub stars / 2.8k forks as of Aug 2026, Apache-2.0) bundles the 7 skills above. The accessibility-review skill runs a "WCAG 2.1 AA audit — contrast, keyboard navigation, touch targets, screen readers," per the design README.
- Highest-trust free resources are official; highest-persuasion resources are individual practitioners. Course marketplaces (Coursera/Udemy) are mostly "listed" quality, and several are SEO/marketing-heavy.

## Details
The annotated table below scores 24 live items on accuracy, whether they teach *doing*, source trust, and craft respect. Most items are marked **previewed** (syllabus/free sample read) or **reviewed** (fully read); that split is expected and honest. Real case studies, outdated items, avoid-list, and gaps follow.

## Recommendations
1. **Start free and official (week 1).** Install the Design plugin, read the "Using Claude Design for prototypes and UX" tutorial, and take the free *Introduction to Claude Cowork* course. Benchmark to change course: if you already ship with Claude Code daily, skip Cowork 101 and go straight to the practitioner material.
2. **If your goal is shipping without an engineer**, study Kris Puckett's Epilogue essay and Meaghan Choi's ~12-min demo *before* paying for any course. Only buy a paid course (e.g., a Gumroad/ADPList vibe-coding course) if you've hit a concrete wall those free resources didn't cover.
3. **For Figma handoff**, use the official Figma MCP docs first; add the Chrome-DevTools community route only once you're comfortable and want to save tokens.
4. **Treat every generated prototype as a first draft.** Run the accessibility-review skill (WCAG 2.1 AA) and check responsive behaviour + real data before calling anything "done." If a resource skips this, downrank it.
5. **Re-check quarterly.** These tools shift every few months; anything you bookmark today should be re-verified against official docs before you rely on it.

## Caveats
- Claude Design is a research preview/beta; usage limits, plan availability and the Design↔Code handoff change frequently. Several sources note it is web-only (claude.ai/design), Opus-4.7-powered and token-hungry, and that the handoff is strong one-way (Design→Code) but weak in reverse.
- Many Medium/Substack items are single-author opinion — verify against official docs. YouTube "full tutorials" were previewed from titles/descriptions and community references, not watched end-to-end.
- One minor unverified detail: the *Introduction to Claude Cowork* course page frames itself as introductory/hands-on but does not print the literal word "Beginner"; level recorded as `basic` on that basis.

---

## Main Table

| Title | URL | Author/Source | Format | Level | Time | Cost | Tier | Design discipline | Why it's good | Skip if |
|---|---|---|---|---|---|---|---|---|---|---|
| Design plugin (official) | https://claude.com/plugins/design | Anthropic | repo | confident | under-1hr | free | reviewed | UX/UI, content design | Official, Apache-2.0; 7 skills (accessibility-review, design-critique, design-handoff, design-system, research-synthesis, user-research, ux-copy). Works in Cowork and Claude Code. | You don't use Cowork/Claude Code. |
| knowledge-work-plugins/design/skills (source) | https://github.com/anthropics/knowledge-work-plugins/tree/main/design/skills | Anthropic | repo | builder | under-1hr | free | reviewed | UX/UI, design systems | The actual SKILL.md files (23.2k-star repo); editable/forkable to encode your own process. | You want a guided course, not raw files. |
| Using Claude Design for prototypes and UX | https://claude.com/resources/tutorials/using-claude-design-for-prototypes-and-ux | Anthropic | docs | basic | under-15min | free | reviewed | Product/UX design | Official 5-min tutorial: rapid prototyping, connecting your codebase, handoff to Claude Code. [claude](https://claude.com/resources/tutorials/using-claude-design-for-prototypes-and-ux) [Claude](https://claude.com/resources/tutorials/using-claude-design-for-prototypes-and-ux) Honest about scope. | You want deep hands-on practice. |
| Introduction to Claude Cowork | https://anthropic.skilljar.com/introduction-to-claude-cowork | Anthropic Academy | course | basic | under-1hr | free-account | reviewed | All (research, docs, handoff) | Free official hands-on course: Cowork task loop, skills, plugins, file/research workflows; certificate on completion. | You only use browser chat. |
| Get started with Claude Design (Help Center) | https://support.claude.com/en/articles/14604416-get-started-with-claude-design | Anthropic | docs | basic | under-15min | free | reviewed | UX/UI | Canonical setup/first-project reference; states plans and beta status. | You've already set it up. |
| Set up your design system in Claude Design | https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design | Anthropic | docs | confident | under-15min | free | reviewed | Design systems | Official guide to feeding Claude your brand (codebase, Figma exports, assets) so output stays on-brand. | You have no design system yet. |
| Claude Code and Figma: set up the MCP server | https://help.figma.com/hc/en-us/articles/39888612464151-Claude-Code-and-Figma-Set-up-the-MCP-server | Figma | docs | confident | under-15min | free-account | reviewed | UX/UI, design systems | Official Figma setup for the Claude Code plugin + Agent Skills; remote vs desktop server explained. [Figma Help Center](https://help.figma.com/hc/en-us/articles/39888612464151-Claude-Code-and-Figma-Set-up-the-MCP-server) | You don't use Figma. |
| Guide to the Figma MCP server | https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server | Figma | docs | confident | under-15min | free-account | reviewed | UX/UI | Explains what the server reads (components, variables, tokens) + write-to-canvas; notes rate limits and seat requirements. | Not using MCP. |
| From Claude Code to Figma (Figma blog) | https://www.figma.com/blog/introducing-claude-code-to-figma/ | Figma (Gui, Design Director for AI) | article | confident | under-15min | free | reviewed | UX/UI | Primary source on the code→Figma direction: turn production code into editable Figma layers. | You only need setup steps. |
| A Designer's Guide to Claude Code | https://medium.com/design-bootcamp/a-designers-guide-to-organizing-ai-skills-and-tools-in-claude-code-f87477c35b82 | Katherine Yeh | article | confident | under-1hr | free | previewed | UX/UI, design systems | Week-by-week onboarding: build a design-principles skill, then component/token specs; treats AI as judgment tool. | You want video. |
| Claude Code for Designers (Builder.io) | https://www.builder.io/blog/claude-code-for-designers | Builder.io | article | confident | under-1hr | free | reviewed | UX/UI | Honest about where "the agentic illusion breaks down" [Builder.io](https://www.builder.io/blog/claude-code-for-designers) — git, PRs, handoff reality. Vendor blog but candid. | You want a vendor-neutral source. |
| Claude Code for Designers: The Complete Guide | https://www.intodesignsystems.com/claude-code-for-designers | Into Design Systems | article | confident | under-1hr | free | previewed | Design systems | Covers the frontend design skill, Figma workflows, and how teams at WhatsApp/Miro ship with Claude Code. | You want official docs only. |
| A better (and cheaper) Figma MCP | https://cianfrani.dev/posts/a-better-figma-mcp/ | Louis Cianfrani | article | builder | under-15min | free | previewed | UX/UI | Chrome-DevTools route to control Figma without full MCP, fewer tokens; includes a clear security warning. | You're on an enterprise-locked setup. |
| Claude Design for UX/UI (real project test) | https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/ | Elizabeth Alli (DesignerUp) | article | basic | under-1hr | free | previewed | UX/UI | Tests Claude Design on a real project across design system, wireframes, hi-fi, Code handoff; notes where it breaks. | You want a shorter overview. |
| Building AI-driven workflows with Claude Code + Codex CLI | https://uxdesign.cc/designing-with-claude-code-and-codex-cli-building-ai-driven-workflows-powered-by-code-connect-ui-f10c136ec11f | Iasonas Georgiadis (UX Collective) | article | builder | under-1hr | free-account | previewed | Design systems | Advanced: Figma MCP + Code Connect UI for codebase-accurate prototypes, not generic mockups. | You're a beginner. |
| Claude for Designers in 2026: Where AI Actually Helps | https://artofstyleframe.com/blog/claude-for-designers-2026/ | Art of Styleframe | article | basic | under-15min | free | previewed | UX/UI | Balanced "fast junior, not a senior" framing; [Art of Styleframe](https://artofstyleframe.com/blog/claude-for-designers-2026/) names failure modes (hallucinated pixel values, 3:1 contrast). | You want hands-on steps. |
| Claude Code for UX Writing | https://uxwritinghub.com/claude-code-ux-writing/ | UX Writing Hub | article | confident | under-1hr | free | previewed | Content/UX writing | Explains CLAUDE.md for enforcing voice/tone at scale. Has a paid-course upsell. | You don't write product copy. |
| ux-writing-skill (open source) | https://github.com/content-designer/ux-writing-skill | content-designer | repo | confident | under-15min | free | previewed | Content/UX writing | Installable Agent Skill enforcing UX-writing standards (CTAs, errors, empty states) across Claude/Codex/Cursor. | You prefer manual copy work. |
| Kris Puckett — building Epilogue (essay) | https://permissionless.krispuckett.com/ | Kris Puckett (Stripe) | article | confident | under-15min | free | reviewed | Product/UI design | Case study: "Fourteen thousand lines of Swift, written through conversation with Claude." Honest about what broke. | You want a step-by-step tutorial. |
| Kris Puckett — Becoming an AI-native designer (Dive Club) | https://www.youtube.com/watch?v=nPyxVMd1LIA | Dive Club / Ridd | podcast | confident | under-1hr | free | previewed | Product/UI design | Long-form: custom Claude Code skills, metal shaders, internal tools at Stripe. | You prefer text. |
| How Claude Code's lead designer builds with AI | https://www.youtube.com/watch?v=hKeDfupbA4U | Dive Club / Meaghan Choi | video | confident | under-15min | free | previewed | Product/UI design | ~12-min demo from Anthropic's Claude Code design lead: [YouTube](https://www.youtube.com/watch?v=hKeDfupbA4U) worktrees, auto mode, custom /prototype skill, "review the PR not the terminal." | You have no interest in Claude Code. |
| Full Tutorial: From Design to Code (Meaghan Choi) | https://creatoreconomy.so/p/full-tutorial-from-design-to-code-with-claude-code-meaghan-choi | Peter Yang / Meaghan Choi | video | confident | under-1hr | free | previewed | Product/UI design | 40-min Figma-to-code walkthrough, CLAUDE.md for designers, shipping to prod. | You want a quick skim. |
| A designer's first attempt at building with Claude Code | https://medium.com/design-bootcamp/a-designers-first-attempt-at-building-with-claude-code-571686dfa17f | Zhiyang | article | basic | under-1hr | free | previewed | Product/UX design | Beginner ship story: PRD via interview, Next.js PWA, Figma MCP setup, live URL. | You're already shipping. |
| Design Systems in 2026: Turn Your System into a Claude Skill | https://www.designsystemscollective.com/design-systems-in-2026-turn-your-system-into-a-claude-skill-3dd4d8bf5feb | Garima Agarwal | article | confident | under-1hr | free-account | previewed | Design systems | Concrete SKILL.md template mapping tokens, naming, component specs, accessibility rules. [Medium](https://www.designsystemscollective.com/design-systems-in-2026-turn-your-system-into-a-claude-skill-3dd4d8bf5feb?gi=a7186eb3e8bb) | Not maintaining a design system. |
| Meaghan Choi — Designing Claude Code (Dive Club) | https://podcasts.apple.com/us/podcast/meaghan-choi-designing-claude-code-and-whats-coming-next/id1686414242 | Dive Club / Ridd | podcast | confident | under-1hr | free | previewed | Product/UI design | Deep dive into how design operates at Anthropic + the Artifacts workflow. | You want practical steps only. |

## Dead or Moved Links
- None confirmed dead during this research. Note that Anthropic Academy is also mirrored at `anthropic-partners.skilljar.com` and some courses appear on Coursera/Class Central; always prefer the primary `anthropic.skilljar.com` URL. Skill directories such as mcpmarket.com / awesomeskill.ai are aggregators — prefer the original GitHub repo (`anthropics/knowledge-work-plugins`) over them.

## Real Case Studies (designers who publicly shipped something with Claude)
- **Kris Puckett (Stripe)** — Epilogue, "Fourteen thousand lines of Swift, written through conversation with Claude" (per his own essay), shipped to the App Store. Essay: https://permissionless.krispuckett.com/ · App Store: https://apps.apple.com/us/app/epilogue-ambient-reading/id6751764862 · CLAUDE.md iOS rules thread: https://x.com/krispuckett/status/1988012974024651071
- **Meaghan Choi (Anthropic, Claude Code design lead)** — demos her real daily setup shipping frontend polish to production: https://www.youtube.com/watch?v=hKeDfupbA4U
- **Zhiyang** — designer shipped a live Next.js PWA (plant-watering app) his partner uses: https://medium.com/design-bootcamp/a-designers-first-attempt-at-building-with-claude-code-571686dfa17f
- **Kay** — product designer built and deployed a wedding website via Claude Design → Claude Code → GitHub Pages: https://medium.com/design-bootcamp/can-claude-design-close-the-gap-between-design-and-engineering-b12a6d17116f
- **John Rodrigues** — designer shipped an iOS app and a Figma plugin (Ollie AI) without being a developer: https://johnrodrigues.substack.com/p/claude-code-for-designers-176

## Looks Outdated (possibly >12 months old, or predating current tools)
- **Collaborate with Claude on Projects** (Anthropic, June 2024) — https://anthropic.com/news/projects — still conceptually useful but references Claude 3.5 Sonnet; predates Cowork, Claude Design, and Skills.
- **Claude For Code** (Nick Babich, UX Planet) — https://uxplanet.org/claude-for-code-how-to-use-claude-to-streamline-product-design-process-97d4e4c43ca4 — the screenshot→HTML approach still works but predates Claude Design and the Figma MCP; likely >12 months old.
- **Intro to Projects** (Anthropic support video) — https://support.anthropic.com/en/articles/9945648-intro-to-projects — foundational but pre-Cowork framing of Projects.

## Avoid (SEO spam, image-gen mislabelled as Claude, or unverifiable claims)
- **How I Use "Claude Code" to Land 2x More Freelance Gigs** — https://medium.com/@dollyborade07/how-i-use-claude-code-and-other-ai-tools-to-land-2x-more-freelance-gigs-as-a-ui-ux-designer-214325d14b03 — mixes Claude with Midjourney; [Medium](https://medium.com/@dollyborade07/how-i-use-claude-code-and-other-ai-tools-to-land-2x-more-freelance-gigs-as-a-ui-ux-designer-214325d14b03) unverifiable income claims; engagement bait.
- **I Tried "Claude Code" for UI/UX ... Insane Results!!** — https://medium.com/@dollyborade07/i-tried-claude-code-for-ui-ux-designing-project-insane-results-dd4e1bb1bfec — cherry-picked "4x faster" stats with weak sourcing.
- **Claude Design Fundamentals (Coursera / SkillsBooster Academy)** — https://www.coursera.org/learn/claude-design-fundamentals — marketing language ("elite design co-pilot," "master the future of digital creativity"); [Coursera](https://www.coursera.org/learn/claude-design-fundamentals) third-party, neither practitioner nor Anthropic.
- **Geeky Gadgets / StarAgile Claude Design guides** — https://www.geeky-gadgets.com/claude-design-workflow-2026/ and https://staragile.com/blog/claude-design-guide — SEO content, "disrupting the industry" framing, skip accessibility/real-data caveats.
- **General warning:** a large share of "AI for designers" content on YouTube/Medium is really Midjourney/Stable Diffusion (image generation), which is out of scope for Claude. Also treat "The ONLY … Tutorial You'll Ever Need" titles skeptically — several bundle affiliate links (Lovable, Higgsfield) rather than Claude craft.

## Gaps (what designers clearly need but nobody has made well)
- A rigorous, current **accessibility-first** Claude workflow guide that treats WCAG as a required pass, not an afterthought — most Claude Design walkthroughs skip it entirely (the accessibility-review skill exists, but no strong end-to-end tutorial wraps it into a designer's process).
- A **responsive + real-data** prototyping guide showing how to move past the "beautiful but fake" AI prototype (empty/loading/error states, breakpoints, real content).
- A neutral, **non-vendor comparison** of Figma MCP vs Chrome-DevTools route vs Claude Design handoff, written for designers specifically.
- Discipline-specific content for **illustrators, 3D artists, and creative directors** — nearly all current material is UX/UI or product design; Claude's genuine (text/code/planning) role for these creatives is underexplored.
- A maintained, **dated changelog** ("what changed this quarter for designers"), since the tools shift every few months and most guides silently rot.

## What surprised me
Three things. First, how fast Anthropic itself became the best source for designers — the open-source Design plugin and the free Cowork course are more honest and current than most paid courses. Second, how consistently the credible practitioners (Puckett, Choi, Yeh) converge on the same craft framing: Claude is an unopinionated junior, and your design system and taste are the differentiators — captured in Puckett's line that "the bottleneck was never coding ability… it was articulation." Third, how much of the "AI for designers" long tail is either image-generation content mislabelled as Claude, or SEO pieces recycling the same launch-day Claude Design facts without ever touching accessibility or real data.

---

## JSON Array (`claude-research-designer-2026-08-20.json`)

```json
[
  {
    "title": "Design plugin (official)",
    "url": "https://claude.com/plugins/design",
    "author": "Anthropic",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["skills", "cowork", "claude-code"],
    "format": "repo",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Anthropic's official design productivity plugin bundling 7 skills for design critique, UX writing, accessibility audits, research synthesis, and developer handoff. Runs in Cowork and Claude Code.",
    "who_for": "UX/UI and content designers who want an official, ready-made set of Claude design workflows.",
    "skip_if": "You don't use Cowork or Claude Code and only chat in the browser.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Apache-2.0; source repo anthropics/knowledge-work-plugins (23.2k stars). Supercharged when connected to Figma/Slack/Jira MCP."
  },
  {
    "title": "knowledge-work-plugins/design/skills (source)",
    "url": "https://github.com/anthropics/knowledge-work-plugins/tree/main/design/skills",
    "author": "Anthropic",
    "roles": ["designer"],
    "level": "builder",
    "topics": ["skills", "mcp"],
    "format": "repo",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "The raw SKILL.md files behind the Design plugin: accessibility-review, design-critique, design-handoff, design-system, research-synthesis, user-research, ux-copy. Forkable to encode your own process.",
    "who_for": "Designers comfortable editing markdown who want to customize Claude's design skills.",
    "skip_if": "You want a guided course rather than raw files.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "accessibility-review runs a WCAG 2.1 AA audit (contrast, keyboard, touch targets, screen readers)."
  },
  {
    "title": "Using Claude Design for prototypes and UX",
    "url": "https://claude.com/resources/tutorials/using-claude-design-for-prototypes-and-ux",
    "author": "Anthropic",
    "roles": ["designer"],
    "level": "basic",
    "topics": ["chat-prompting", "claude-code"],
    "format": "docs",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Official ~5-minute tutorial covering rapid prototyping in Claude Design, connecting your codebase for production-aware designs, and handing off to Claude Code.",
    "who_for": "Product and UX designers wanting the official, honest overview of Claude Design's real workflow.",
    "skip_if": "You want deep hands-on practice rather than an overview.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Claude Design is Anthropic Labs; web-only at claude.ai/design; Opus 4.7."
  },
  {
    "title": "Introduction to Claude Cowork",
    "url": "https://anthropic.skilljar.com/introduction-to-claude-cowork",
    "author": "Anthropic Academy",
    "roles": ["designer"],
    "level": "basic",
    "topics": ["cowork", "skills"],
    "format": "course",
    "time": "under-1hr",
    "cost": "free-account",
    "language": "en",
    "tier": "reviewed",
    "summary": "Free official hands-on course on the Cowork task loop, plugins and skills, file/research workflows, and steering multi-step work; certificate on completion.",
    "who_for": "Designers who want Claude to work on real files (research synthesis, handoff docs) beyond chat.",
    "skip_if": "You only use Claude in the browser chat and never touch files.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Hosted on Skilljar; email/Skilljar account required. Page frames it as introductory but doesn't print the literal 'Beginner' label."
  },
  {
    "title": "Get started with Claude Design (Help Center)",
    "url": "https://support.claude.com/en/articles/14604416-get-started-with-claude-design",
    "author": "Anthropic",
    "roles": ["designer"],
    "level": "basic",
    "topics": ["chat-prompting"],
    "format": "docs",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Canonical setup and first-project reference for Claude Design, including which plans have access and that it's in beta.",
    "who_for": "Any designer setting up Claude Design for the first time.",
    "skip_if": "You've already set it up.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Available on Pro, Max, Team, Enterprise; default off for Enterprise."
  },
  {
    "title": "Set up your design system in Claude Design",
    "url": "https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design",
    "author": "Anthropic",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["chat-prompting"],
    "format": "docs",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Official guide to feeding Claude your brand (codebase, Figma exports, brand PDFs, assets) so every project stays on-brand.",
    "who_for": "Designers and design leads establishing a reusable design system in Claude Design.",
    "skip_if": "You have no design system or brand assets to import yet.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Publish toggle applies the system org-wide; Enterprise can restrict who publishes."
  },
  {
    "title": "Claude Code and Figma: Set up the MCP server",
    "url": "https://help.figma.com/hc/en-us/articles/39888612464151-Claude-Code-and-Figma-Set-up-the-MCP-server",
    "author": "Figma",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["mcp", "claude-code"],
    "format": "docs",
    "time": "under-15min",
    "cost": "free-account",
    "language": "en",
    "tier": "reviewed",
    "summary": "Official Figma instructions for installing the Figma plugin/MCP server in Claude Code, including Agent Skills and the remote-vs-desktop server choice.",
    "who_for": "UX/UI and design-system designers who want Claude Code to read and write Figma files.",
    "skip_if": "You don't use Figma.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Install via `claude plugin install figma@claude-plugins-official`. Requires a paid Figma seat for Dev Mode features."
  },
  {
    "title": "Guide to the Figma MCP server",
    "url": "https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server",
    "author": "Figma",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["mcp"],
    "format": "docs",
    "time": "under-15min",
    "cost": "free-account",
    "language": "en",
    "tier": "reviewed",
    "summary": "Explains what the Figma MCP server exposes (components, variables, tokens, layout), the write-to-canvas capability, and rate limits/seat requirements.",
    "who_for": "Designers wanting to understand MCP capabilities before wiring it into Claude.",
    "skip_if": "You're not using MCP.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Beta usage-based feature; read tools are rate-limited, write tools mostly exempt."
  },
  {
    "title": "From Claude Code to Figma: Turning Production Code into Editable Figma Designs",
    "url": "https://www.figma.com/blog/introducing-claude-code-to-figma/",
    "author": "Figma (Gui, Design Director for AI)",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["mcp", "claude-code"],
    "format": "article",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Primary-source announcement of the code-to-Figma direction: send live web interfaces from Claude Code into Figma as editable layers.",
    "who_for": "Designers who prototype in code and want to bring work back onto the canvas for team review.",
    "skip_if": "You only need setup steps, not the concept.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Assumes Claude Code + Figma MCP already set up."
  },
  {
    "title": "A Designer's Guide to Claude Code",
    "url": "https://medium.com/design-bootcamp/a-designers-guide-to-organizing-ai-skills-and-tools-in-claude-code-f87477c35b82",
    "author": "Katherine Yeh",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["claude-code", "skills", "mcp"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "A practical week-by-week plan for designers: build a design-principles skill, then component/token spec skills, connect Figma MCP, and get feedback that understands your system.",
    "who_for": "UX/UI and design-system designers moving from chat to structured Claude Code skills.",
    "skip_if": "You prefer video over long reads.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Assumes Claude Code + Figma. Single-author opinion; verify commands against official docs."
  },
  {
    "title": "Claude Code for Designers (Builder.io)",
    "url": "https://www.builder.io/blog/claude-code-for-designers",
    "author": "Builder.io",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["claude-code", "mcp"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Getting-started guide plus an unusually honest section on where the workflow gets hard for designers: git, pull requests, and syncing with the dev team.",
    "who_for": "Designers who want a realistic picture of Claude Code + Figma MCP, including the messy parts.",
    "skip_if": "You want a vendor-neutral source (this is a Builder.io blog).",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Vendor blog; nudges toward Builder's own tooling at the end."
  },
  {
    "title": "Claude Code for Designers: The Complete Guide",
    "url": "https://www.intodesignsystems.com/claude-code-for-designers",
    "author": "Into Design Systems",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["claude-code", "skills", "mcp"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "Overview of designing with Claude Code: the frontend design skill, Figma workflows, giving Claude your design system as context, and examples from WhatsApp/Miro teams.",
    "who_for": "Design-system practitioners wanting production-quality UI from Claude Code.",
    "skip_if": "You only trust first-party documentation.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Links out to related Figma-CLI and Miro case-study articles."
  },
  {
    "title": "A Better (and Cheaper) Figma MCP or How To Let Claude Design",
    "url": "https://cianfrani.dev/posts/a-better-figma-mcp/",
    "author": "Louis Cianfrani",
    "roles": ["designer"],
    "level": "builder",
    "topics": ["mcp", "claude-code"],
    "format": "article",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "A community workaround: control Figma via the Chrome DevTools MCP (a single browser MCP) instead of the full Figma MCP, using fewer tokens; works with a free Figma account.",
    "who_for": "Technically comfortable designers who want a lighter/cheaper Figma-Claude connection.",
    "skip_if": "You're on an enterprise-locked setup or uneasy giving an LLM browser access.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Includes an explicit security warning about giving Claude browser control."
  },
  {
    "title": "How to Use Claude Design for UX/UI",
    "url": "https://designerup.co/blog/how-to-use-claude-design-for-ux-ui/",
    "author": "Elizabeth Alli (DesignerUp)",
    "roles": ["designer"],
    "level": "basic",
    "topics": ["chat-prompting", "claude-code"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "A practising designer tests Claude Design on a real UX/UI project: generating a design system, wireframe flows, hi-fi prototype with animations, and handoff to Claude Code — noting where it breaks.",
    "who_for": "UX/UI designers evaluating Claude Design for real product work.",
    "skip_if": "You want a shorter overview.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Written near Claude Design's April 2026 launch; some usage-limit details may have changed."
  },
  {
    "title": "Building AI-driven workflows powered by Claude Code and other tools",
    "url": "https://uxdesign.cc/designing-with-claude-code-and-codex-cli-building-ai-driven-workflows-powered-by-code-connect-ui-f10c136ec11f",
    "author": "Iasonas Georgiadis (UX Collective)",
    "roles": ["designer"],
    "level": "builder",
    "topics": ["claude-code", "mcp"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free-account",
    "language": "en",
    "tier": "previewed",
    "summary": "Advanced workflow using Figma MCP + Code Connect UI with Claude Code (and Codex CLI) to turn rough ideas into production-ready code that reflects a real design system, not generic mockups.",
    "who_for": "Senior designers building codebase-accurate prototypes with an existing design system.",
    "skip_if": "You're a beginner or don't have a mature design system.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Medium/UX Collective; may hit a metered paywall."
  },
  {
    "title": "Claude for Designers in 2026: Where AI Actually Helps",
    "url": "https://artofstyleframe.com/blog/claude-for-designers-2026/",
    "author": "Art of Styleframe",
    "roles": ["designer"],
    "level": "basic",
    "topics": ["chat-prompting", "claude-code"],
    "format": "article",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "A balanced map of where Claude genuinely helps the UI workflow (UX copy, first-draft component code, token scaffolding, screenshot critique) and where it quietly hurts, with named failure modes.",
    "who_for": "Designers wanting an honest, craft-first orientation before diving in.",
    "skip_if": "You want hands-on setup steps.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Flags hallucinated pixel values and AI shipping 3:1 contrast as 'fine'."
  },
  {
    "title": "How to Use Claude Code for UX Writing",
    "url": "https://uxwritinghub.com/claude-code-ux-writing/",
    "author": "UX Writing Hub",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["claude-code", "chat-prompting"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "Explains using CLAUDE.md to enforce brand voice/tone and run large-scale copy audits (e.g., replacing 'Click here' across hundreds of articles) as a content systems workflow.",
    "who_for": "Content designers and UX writers wanting consistent copy at scale.",
    "skip_if": "You don't write or own product copy.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Contains an upsell to the site's paid Claude Code course."
  },
  {
    "title": "ux-writing-skill (open source)",
    "url": "https://github.com/content-designer/ux-writing-skill",
    "author": "content-designer",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["skills", "claude-code"],
    "format": "repo",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "An installable Agent Skill that makes Claude write/edit interface copy (CTAs, error messages, empty states, onboarding) to consistent standards, activating automatically when relevant.",
    "who_for": "Content designers and product teams wanting UX-writing standards enforced across Claude/Codex/Cursor.",
    "skip_if": "You prefer to write all copy manually.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Community skill (not Anthropic's official ux-copy skill); works via skills CLI."
  },
  {
    "title": "Field Notes from the In-Between (Building Epilogue with Claude Code)",
    "url": "https://permissionless.krispuckett.com/",
    "author": "Kris Puckett (Stripe)",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["claude-code"],
    "format": "article",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "A design manager's honest case study of building Epilogue — 'fourteen thousand lines of Swift, written through conversation with Claude' — shipped to the App Store, including what broke and what he learned about precise articulation.",
    "who_for": "Designers who want proof and mindset for shipping real software without a traditional engineer.",
    "skip_if": "You want a step-by-step tutorial rather than a reflective essay.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Companion: App Store id6751764862 and his CLAUDE.md iOS rules thread on X."
  },
  {
    "title": "Kris Puckett - Becoming an AI-native designer (Dive Club)",
    "url": "https://www.youtube.com/watch?v=nPyxVMd1LIA",
    "author": "Dive Club / Ridd",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["claude-code", "skills"],
    "format": "podcast",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "Long-form interview with a Stripe design manager on building his own apps with Claude Code, creating custom skills, teaching Claude metal shaders, and building internal tools.",
    "who_for": "Designers wanting a deep, honest look at an AI-native design practice.",
    "skip_if": "You prefer text to a ~1-hour podcast.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Also on Apple/Spotify. Previewed via description and secondary write-ups, not watched end-to-end."
  },
  {
    "title": "How Claude Code's lead designer builds with AI",
    "url": "https://www.youtube.com/watch?v=hKeDfupbA4U",
    "author": "Dive Club / Meaghan Choi",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["claude-code", "skills"],
    "format": "video",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "~12-minute demo from Anthropic's Claude Code design lead showing her real setup: git worktrees, auto mode, a custom /prototype skill that generates five HTML variants, and reviewing the PR instead of the terminal.",
    "who_for": "Product/UI designers who want to see an expert's actual daily Claude Code workflow.",
    "skip_if": "You have no interest in Claude Code.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Recorded at Dive Club Live NYC; previewed via description/secondary sources."
  },
  {
    "title": "Full Tutorial: From Design to Code with Claude Code (Meaghan Choi)",
    "url": "https://creatoreconomy.so/p/full-tutorial-from-design-to-code-with-claude-code-meaghan-choi",
    "author": "Peter Yang / Meaghan Choi",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["claude-code", "mcp"],
    "format": "video",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "~40-minute walkthrough of a designer's Figma-to-working-code workflow with Claude Code, custom CLAUDE.md files for designers, and how designers can get permission to ship to production.",
    "who_for": "Designers and PMs who dream of shipping frontend polish to prod.",
    "skip_if": "You want a quick skim rather than a full session.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Includes chapter timestamps and a live Figma-to-code demo."
  },
  {
    "title": "A designer's first attempt at building with Claude Code",
    "url": "https://medium.com/design-bootcamp/a-designers-first-attempt-at-building-with-claude-code-571686dfa17f",
    "author": "Zhiyang",
    "roles": ["designer"],
    "level": "basic",
    "topics": ["claude-code", "mcp"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "A beginner-friendly ship story: using Claude to interview him into a PRD, building a Next.js PWA, setting up Figma MCP, and pushing a live URL his partner actually uses.",
    "who_for": "Designers curious about building with AI who haven't taken the first step.",
    "skip_if": "You're already shipping apps.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Honest that it's not one-shot magic; still a full design process."
  },
  {
    "title": "Design Systems in 2026: Turn Your System into a Claude Skill",
    "url": "https://www.designsystemscollective.com/design-systems-in-2026-turn-your-system-into-a-claude-skill-3dd4d8bf5feb",
    "author": "Garima Agarwal",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["skills", "claude-code"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free-account",
    "language": "en",
    "tier": "previewed",
    "summary": "A concrete SKILL.md template that encodes design tokens, naming conventions, component specs, and accessibility rules so Claude applies your system to UI and Figma/React work.",
    "who_for": "Design-system owners who want Claude to respect their system consistently.",
    "skip_if": "You don't maintain a design system.",
    "published": "UNVERIFIED",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Medium/Design Systems Collective; may hit a metered paywall."
  },
  {
    "title": "Meaghan Choi - Designing Claude Code (and what's coming next)",
    "url": "https://podcasts.apple.com/us/podcast/meaghan-choi-designing-claude-code-and-whats-coming-next/id1686414242",
    "author": "Dive Club / Ridd",
    "roles": ["designer"],
    "level": "confident",
    "topics": ["claude-code", "chat-prompting"],
    "format": "podcast",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "Deep-dive interview with Anthropic's Claude Code design lead on how design operates at Anthropic, the Artifacts workflow, and where AI-native design is heading.",
    "who_for": "Designers wanting a strategic, insider view of AI-native design.",
    "skip_if": "You want practical steps only.",
    "published": "2026-07-08",
    "checked": "2026-08-20",
    "status": "live",
    "notes": "Also on YouTube and Spotify. Previewed via episode notes."
  }
]
```