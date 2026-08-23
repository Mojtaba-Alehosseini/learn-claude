# Best Claude Learning Content for Researchers & Academics — Curated Guide

**Bottom line:** The single most reliable, still-accurate place for a researcher to learn Claude is **Anthropic's own free material** (Anthropic Academy / claude.com, the Help Center, and platform docs) supplemented by a small number of working-academic guides (Effortless Academic, Laszlo Szabo) and the community Zotero-MCP tooling — but *no* resource should be used for literature review without an explicit citation-verification step, because fabricated references are the #1 documented harm for this audience and even the best guides vary in how honestly they address it. Checked **2026-08-18**.

Below are the two deliverable files (Markdown report + JSON array), followed by the "most surprising" note.

---

## FILE 1 — `claude-research-researcher-2026-08-18.md`

```markdown
# Best Claude Learning Content for Researchers & Academics
_Checked: 2026-08-18_

## TL;DR
- **Start with Anthropic's own free content** — Claude 101 and AI Fluency for the interface and judgment; the Help Center + platform docs for authoritative, current feature behavior (Projects, Research mode, the analysis/code-execution tool). Anthropic updates these when the product changes, so they age slowest.
- **For research-specific workflows**, the strongest non-official guides are from working academics: Effortless Academic (Ilya Shabanov) for Claude Code/CoWork + Zotero, and Laszlo Szabo for a citation-verification-first literature workflow. Connect Claude to your library with a community Zotero MCP server (there is no official one).
- **Never run a literature review without verifying every citation.** Publishers (Nature/Springer, Elsevier, IEEE, ICMJE) require disclosure of AI use and hold you accountable; Springer Nature explicitly treats hallucinated references as an integrity breach that can trigger rejection or retraction.

## Key Findings
1. **Official Anthropic content is the safest bet on accuracy.** Claude's interface changes every few months (the "analysis tool" was already renamed/superseded by "code execution / upgraded file creation" between Oct 2024 and Sep 2025), so third-party guides date fast. Anthropic's Skilljar courses, Help Center, and platform docs are versioned against the live product.
2. **The best research-specific teaching is done by individual academics, not institutions or big course platforms.** University library guides are trustworthy but often thin/outdated (some still describe Claude 2 / the Claude 3 family). The richest hands-on academic workflows come from Effortless Academic, Laszlo Szabo, Andy Stapleton, and Mushtaq Bilal.
3. **Citation fabrication is real, measured — but the famous numbers are NOT Claude's.** The widely-shared JMIR percentages come from studies that tested GPT/Bard, not Claude. The only peer-reviewed study that actually used Claude for a literature review (Sparkman & Witt, Library Trends 2025) reports incomplete/fabricated citations qualitatively, not as a rate. Treat any specific "Claude fabricates X%" claim with suspicion.
4. **Free API credits exist for researchers.** Anthropic's AI for Science program gives up to $20,000 in API credits over six months; a July 2026 rare-disease track offers up to $50,000.
5. **Builder-level content (Claude Code, MCP, Skills) is powerful but honestly a step up.** It suits researchers who already write R/Python; it is not terminal-free, though GUI installers now lower the Zotero-MCP barrier.

## Main table

| Title | URL | Author/Source | Format | Level | Time | Cost | Tier | Why it's good | Skip if |
|---|---|---|---|---|---|---|---|---|---|
| Anthropic Academy — Courses hub | https://claude.com/resources/courses | Anthropic | course | never-used→builder | multi-day | free-account | previewed | Official catalog, kept current with the product; single entry point to all tracks | You want research-specific workflows, not general Claude training |
| Claude 101 | https://anthropic.skilljar.com/claude-101 | Anthropic | course | never-used | under-1hr | free-account | previewed | Covers Projects, artifacts, skills, connectors, enterprise search, research mode — the features that turn Claude into a workflow | Already confident with the Claude interface |
| AI Fluency: Framework & Foundations | https://www.anthropic.com/ai-fluency | Anthropic (Profs. Feller, UCC & Dakan, Ringling) | course | never-used | half-day | free | reviewed | 12 lessons / 3–4 hrs; [anthropic](https://www.anthropic.com/ai-fluency) the 4D framework (Delegation, Description, Discernment, Diligence) [anthropic](https://www.anthropic.com/ai-fluency/conclusion) explicitly teaches when NOT to trust AI — exactly the judgment this audience needs | You want button-clicks, not a thinking framework |
| AI Fluency for Students | https://www.coursera.org/learn/ai-fluency-for-students | Anthropic | course | never-used | under-1hr | free-account | previewed | 5 lectures/~30 min; [Claude](https://claude.com/resources/courses) frames the learn-vs-outsource distinction well for PhD students | Faculty wanting advanced research workflows |
| Plan your literature review (use-case) | https://claude.com/resources/use-cases/plan-your-literature-review | Anthropic | article | basic | under-15min | free | reviewed | Official worked example using the PubMed connector to build a structured reading guide | You need the (missing) citation-verification warning — add it yourself |
| Use research on Claude | https://support.claude.com/en/articles/11088861-use-research-on-claude | Anthropic | docs | basic | under-15min | subscription | reviewed | Authoritative on the agentic Research feature (multi-step search with citations); explains Workspace integration | You're on the free plan (Research is Pro/Max/Team/Enterprise) |
| Enabling and using the analysis tool | https://support.anthropic.com/en/articles/10008684-enabling-and-using-the-analysis-tool | Anthropic | docs | basic | under-15min | free-account | reviewed | Canonical setup for in-chat data analysis/visualization of CSVs [anthropic](https://support.anthropic.com/en/articles/10008684-enabling-and-using-the-analysis-tool) | You want the newer server-side code execution (this JavaScript tool is being superseded) |
| What are Projects? | https://support.claude.com/en/articles/9517075-what-are-projects | Anthropic | docs | basic | under-15min | free-account | reviewed | Explains persistent knowledge bases + custom instructions — the backbone of a reusable research setup (free tier = 5 projects) | You already use Projects |
| Prompt Engineering Interactive Tutorial | https://github.com/anthropics/prompt-eng-interactive-tutorial | Anthropic | hands-on | confident | half-day | free | previewed | Official, hands-on, 9 chapters including a dedicated chapter on avoiding hallucinations; [Beginners in AI](https://beginnersinai.org/anthropic-prompt-engineering-course/) runnable notebooks + Google Sheets version | Examples still use the old Claude 3 Haiku model [GitHub](https://github.com/anthropics/prompt-eng-interactive-tutorial) — treat model-specific behavior as historical |
| AI for Science Program | https://support.claude.com/en/articles/11199177-anthropic-s-ai-for-science-program | Anthropic | docs | confident | under-15min | free | reviewed | Up to $20,000 in API credits [Aicreditmart](https://aicreditmart.com/ai-credit-providers/anthropic/) over a 6-month period for researchers at academic/nonprofit institutions (biology/life-sciences focus); [Claude](https://support.claude.com/en/articles/11199177-anthropic-s-ai-for-science-program) a July 2026 rare-disease track offers up to $50,000 | Your work isn't API-based or high-impact scientific research |
| How scientists are using Claude | https://www.anthropic.com/news/accelerating-scientific-research | Anthropic | article | basic | under-15min | free | reviewed | Real lab case studies (e.g. Stanford's Biomni agent) [Anthropic](https://www.anthropic.com/news/accelerating-scientific-research) that calibrate what Claude can/can't do in science | You want a hands-on how-to, not context |
| Claude Code & CoWork for Academics (Part 1) | https://effortlessacademic.com/claude-code-and-cowork-for-academics-beginner-guide-part-1/ | Effortless Academic (Ilya Shabanov) | article | confident | under-1hr | free | reviewed | Clear analogy-driven install/first-use for non-coders; unusually honest about hype ("don't outsource your cognitive sovereignty") | Terminal-averse readers may still find Claude Code a stretch |
| Claude Skills for Academics (Part 2) | https://effortlessacademic.com/claude-skills-for-academics-beginner-tutorial-part-2/ | Effortless Academic (Ilya Shabanov) | article | builder | under-1hr | free | previewed | Real skill-building (e.g. atomic-sentence writing) tied to reference-grounded drafting | You've never used Claude before — do Part 1 first |
| Connect Zotero to Claude Cowork | https://effortlessacademic.com/connect-and-integrate-your-local-zotero-library-with-claude-cowork/ | Effortless Academic (Ilya Shabanov) | article | confident | under-1hr | free | reviewed | No-terminal walkthrough of connecting a local Zotero library via MCP [Effortless Academic](https://effortlessacademic.com/connect-and-integrate-your-local-zotero-library-with-claude-cowork/) | You don't use Zotero |
| zotero-mcp (54yyyu) | https://github.com/54yyyu/zotero-mcp | Community (54yyyu) | repo | builder | under-1hr | free | previewed | Most widely-used Zotero MCP; semantic search, PDF full-text, retraction alerts; local + web API [GitHub](https://github.com/54yyyu/zotero-mcp) | You're not comfortable running any install |
| zotero-mcp-setup (GUI installer) | https://github.com/ehawkin/zotero-mcp-setup | Community (ehawkin) | repo | confident | under-15min | free | previewed | One-click Mac (DMG)/Windows installers so non-terminal users can still connect Zotero | You prefer to configure MCP manually |
| Claude AI and Literature Reviews (study) | https://muse.jhu.edu/article/961199 | Sparkman & Witt, _Library Trends_ 73(3):355–380 (2025) | article | confident | under-1hr | paid-once | reviewed | The only peer-reviewed study that actually tested Claude on a literature review; documents its real limits (synthesis, incomplete + hallucinated citations) [Project MUSE](https://muse.jhu.edu/pub/1/article/961199/summary) [jhu](https://muse.jhu.edu/article/961199) | You want a how-to, not a study (open-access copy at knightscholar.geneseo.edu/library-research/22/) |
| Claude for medical literature search: avoid hallucinations | https://lszabo.me/posts/ai-literature-search/ | Laszlo Szabo | article | confident | under-1hr | free | reviewed | The best honest, verification-first workflow: "ask for the PMID; if it doesn't resolve, it's fabricated"; [Laszlo Szabo](https://lszabo.me/posts/ai-literature-search/) PubMed connector setup | You want an official Anthropic source |
| Claude Researcher (workflows) | https://www.clauderesearcher.com/ | Independent (unaffiliated with Anthropic) | article | confident | under-1hr | free | previewed | Source-first lit-review protocol; explicit citation-discipline and role-separation; links primary sources | You want an official/named-institution source |
| Academic Research with Claude (live seminar) | https://aihorizons.io/Seminars/claude-academic-research/ | AI Horizons | course | confident | half-day | paid-once | previewed | Structured, reproducible AI research workflow across the whole lifecycle; assumes only basic prompting + some R/Python | Budget-constrained; prefer free material |
| Introduction to Claude Analysis | https://www.codecademy.com/learn/ext-courses/introduction-to-claude-analysis | Codecademy | course | basic | under-1hr | free-account | previewed | Focused ~1-hr intro to CSV cleaning, basic stats, and visualization via Claude's analysis tool [Codecademy](https://www.codecademy.com/learn/ext-courses/introduction-to-claude-analysis) | Note the tool is being replaced by server-side code execution |
| 15 Claude Tips for Everyday Data Analysis | https://www.linkedin.com/learning/topics/claude | LinkedIn Learning | video | basic | under-1hr | subscription | listed | Practical everyday data-analysis tips (21 min, released Apr 2026) | No LinkedIn Learning access |
| Andy Stapleton — AI for academia (YouTube) | https://www.youtube.com/@DrAndyStapleton | Andy Stapleton, PhD (chemistry) | video | basic | under-1hr | free | listed | Working ex-academic (288k+ subs) who tests 100+ tools; [Academia Insider](https://academiainsider.com/work-with-dr-andy/) honest, research-focused | You prefer text to video; some videos are tool-promotional |
| Mushtaq Bilal — Claude for Academic Writing/Research | https://mushtaqbilalphd.kit.com/ | Mushtaq Bilal, PhD | podcast | confident | under-1hr | paid-once | listed | Aimed squarely at non-technical academics; webinars + threads on Claude Code for research | See "Avoid": he has also promoted AI-"humanizer" detection-evasion tricks |

### Dead or moved links
- No fully dead links found during research. Note: `support.anthropic.com/...` article URLs now redirect/mirror to `support.claude.com/...` — both resolve, but prefer the `support.claude.com` form.
- The old standalone "$50 Student Builder API credits" offer no longer exists as its own page; it now redirects into the Claude Campus program (https://claude.com/programs/campus).

### Looks outdated
- **mygreatlearning "Introduction to Claude"** (https://www.mygreatlearning.com/academy/learn-for-free/courses/introduction-to-claude) — still teaches the "Claude 2 API" and legacy models; skip.
- **Syracuse University Libraries "Claude AI" guide** (https://researchguides.library.syr.edu/c.php?g=1341750&p=10258238) — copyright 2024, describes the Claude 3 family/legacy models and says Claude "cannot access external data" — no longer true (connectors, Research, MCP). Useful only as a basic definition.
- **Anthropic prompt-eng interactive tutorial** — excellent but its examples still run on Claude 3 Haiku; techniques transfer, model behavior doesn't.
- **Any "analysis tool" tutorial** (Codecademy, LinkedIn, third-party blogs) — the JavaScript-in-browser analysis tool was superseded by server-side code execution ("upgraded file creation and analysis") in Sep 2025; screenshots and toggles may not match.

### Avoid
- **AI-"humanizer" / "make AI text 100% human" tricks** (promoted in some social threads, incl. by Mushtaq Bilal, and tools like the "humanizer" skill) — these exist to defeat AI-detection and enable *undisclosed* AI use, which conflicts with Nature/Springer, Elsevier, IEEE, and ICMJE disclosure requirements. Dangerous for this audience.
- **Fully-automated "complete research paper" pipelines** (e.g. the academic-research-skills Claude Code suite's 10-stage "one instruction → finished paper" pipeline, https://tosea.ai/blog/academic-research-skills-claude-code-suite-guide-2026) — high risk of undisclosed AI authorship and citation fabrication at scale. Use component skills, not the end-to-end auto-paper.
- **Gumroad reseller "21-part Claude AI course" (£135)** (https://thekitmarket.gumroad.com/l/jkats) — resell-license SEO product, not a trustworthy learning resource.
- **Generic "beginnersinai.org", "perplexityaimagazine.com", "claudelab.net", "aionx.co" SEO explainers** — some are decent and *do* warn about fabricated citations (credit where due), but they are aggregated/SEO content; prefer the primary sources they summarize.

### Publisher policies
- **ICMJE** — https://www.icmje.org/recommendations/browse/artificial-intelligence/ — Disclose AI use in the cover letter AND the manuscript; [ICMJE](https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html) AI cannot be an author or be cited as an author; [ICMJE](https://www.icmje.org/recommendations/browse/artificial-intelligence/) "Referencing AI-generated material as the primary source is not acceptable." [RSNA](https://pubs.rsna.org/doi/full/10.1148/radiol.239024) (current recommendations, updated Jan 2026 per ICMJE.)
- **Nature Portfolio (Springer Nature)** — https://www.nature.com/nature-portfolio/editorial-policies/ai — A risk-assessment framework built on four core expectations: "human accountability cannot be transferred to AI systems; AI may support but not replace scholarly judgement; transparency about AI use builds trust and confidence; and confidentiality and data protection must be maintained when using AI tools." [Nature](https://www.nature.com/nature-portfolio/editorial-policies/ai) AI cannot be an author; disclose LLM use in Methods; AI-generated images generally prohibited; reviewers "may use AI to support peer review but must not upload manuscript content to unsecured or public AI tools." [Nature](https://www.nature.com/nature-portfolio/editorial-policies/ai) "AI assisted copy editing" is exempt from disclosure.
- **Springer Nature (integrity policy)** — https://www.springernature.com/gp/policies/editorial-policies — Explicit hallucinated-citation rule: unreliable/non-existent references generated by an AI tool constitute a breach of its integrity policy and "may result in the manuscript being rejected for publication or retracted post-publication."
- **Elsevier** — https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals — Disclose AI use; authors must independently verify factual statements and that cited sources are accurate and correctly represented; AI-generated/altered images prohibited.
- **Taylor & Francis** — https://taylorandfrancis.com/our-policies/ai-policy/ — Disclose tool name + version + how/why used; [Taylor & Francis](https://taylorandfrancis.com/our-policies/ai-policy/) AI not an author; no generative AI in creating/manipulating research outputs or images.
- **IEEE** — https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/ — AI-generated content (text, figures, images, code) must be disclosed in the Acknowledgments, naming the system and the sections it touched; [ieee](https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/) grammar/editing use is recommended-but-not-required to disclose (exclude the reference list from AI editing). [Enago](https://www.enago.com/responsible-ai-movement/publisher-ai-guidelines/ieee-ai-guidelines/)
- **AAAS/Science** (context) — strictest: bans AI-generated text/figures as content and treats undisclosed use as misconduct.

### Gaps (what researchers need but nobody has made well yet)
- **No official Anthropic tutorial dedicated to verifying citations / avoiding fabricated references** for researchers — the highest-value missing resource for this exact audience.
- **No official Zotero (or Mendeley/EndNote) connector** — all reference-manager integrations are community-built MCP servers of varying maintenance quality.
- **Little discipline-specific worked content** outside biomedicine — humanities, economics, and qualitative-methods researchers are underserved.
- **No authoritative, regularly-updated crosswalk** mapping "which Claude feature is safe for which manuscript stage under which publisher's policy."
- **Reproducibility guidance** (logging prompts, model + version, and feature used for disclosure) is scattered across blogs, not consolidated.

### Note on citation-fabrication evidence (important, and widely mis-cited)
- The most-shared numbers are **not about Claude**:
  - **Chelli et al.**, _J Med Internet Res_ 2024;26:e53164 (PMID 38776130): hallucination rates of 39.6% (GPT-3.5), 28.6% (GPT-4), and 91.4% (Bard); [JMIR](https://www.jmir.org/2024/1/e53164) reference precision only 9.4%/13.4%/0% [PubMed](https://pubmed.ncbi.nlm.nih.gov/38776130/) across 471 references from rotator-cuff systematic reviews [doaj](https://doaj.org/article/ec1a9d0c24384d3d914d5c02f6fc50fa) — **no Claude tested**.
  - **Linardon et al.** (Deakin University), _JMIR Mental Health_, 12 Nov 2025, Vol 12 e80371 (DOI 10.2196/80371, PMID 41223407): GPT-4o produced six mental-health literature reviews in which 19.9% of citations were completely fabricated [MedicalXpress](https://medicalxpress.com/news/2025-11-reveals-high-fabricated-inaccurate-citations.html) and only ~43.8% were both real and accurate — **GPT-4o, not Claude**.
- The only peer-reviewed study that actually used Claude for a literature review — **Sparkman & Witt, _Library Trends_ 73(3):355–380 (2025), DOI 10.1353/lib.2025.a961199** — found Claude "struggling with synthesis, providing incomplete citations, and hallucinating false information," [Project MUSE](https://muse.jhu.edu/pub/1/article/961199/summary) [jhu](https://muse.jhu.edu/article/961199) but reports this **qualitatively, without a percentage**.
- A 2026 preprint (Rao et al., arXiv:2604.03173) reports 3–13% hallucinated citation URLs across models including Anthropic's, [arxiv](https://arxiv.org/html/2604.03173v1) but is **not peer-reviewed** and does not isolate a clean Claude figure.
- **Practical takeaway:** there is no trustworthy peer-reviewed "Claude fabricates X%" number. Assume non-zero fabrication and verify every reference (resolve the DOI/PMID against the actual database).
```

---

## FILE 2 — `claude-research-researcher-2026-08-18.json`

```json
[
  {
    "title": "Anthropic Academy — Courses hub",
    "url": "https://claude.com/resources/courses",
    "author": "Anthropic",
    "roles": ["researcher"],
    "level": "never-used",
    "topics": ["chat-prompting", "claude-code", "cowork", "skills", "mcp", "api"],
    "format": "course",
    "time": "multi-day",
    "cost": "free-account",
    "language": "en",
    "tier": "previewed",
    "summary": "Official catalog of Anthropic's free self-paced courses (Claude 101, AI Fluency tracks, Claude Code, API, MCP, Skills, Cowork), the single entry point kept current with the product.",
    "who_for": "Any researcher who wants structured, trustworthy Claude training from the vendor.",
    "skip_if": "You need research-specific workflows rather than general Claude training.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Hosted on Skilljar (anthropic.skilljar.com); catalog size changes often (was 13, then 17, then 20+ courses through 2026)."
  },
  {
    "title": "Claude 101",
    "url": "https://anthropic.skilljar.com/claude-101",
    "author": "Anthropic",
    "roles": ["researcher"],
    "level": "never-used",
    "topics": ["chat-prompting", "skills"],
    "format": "course",
    "time": "under-1hr",
    "cost": "free-account",
    "language": "en",
    "tier": "previewed",
    "summary": "Beginner course covering everyday Claude use plus Projects, artifacts, skills, connectors, enterprise search and research mode.",
    "who_for": "Researchers new to Claude who want to move past chatbot-only use.",
    "skip_if": "You're already confident with the Claude interface.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Certificate on completion; free email signup, no Claude subscription required."
  },
  {
    "title": "AI Fluency: Framework & Foundations",
    "url": "https://www.anthropic.com/ai-fluency",
    "author": "Anthropic (Prof. Joseph Feller, UCC; Prof. Rick Dakan, Ringling)",
    "roles": ["researcher"],
    "level": "never-used",
    "topics": ["chat-prompting", "safety"],
    "format": "course",
    "time": "half-day",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "12-lesson (3-4 hr) course teaching the 4D framework (Delegation, Description, Discernment, Diligence) for effective, ethical, safe AI collaboration — including when NOT to trust AI.",
    "who_for": "Researchers who want a durable mental model and judgment, not just feature tips.",
    "skip_if": "You want concrete button-clicks rather than a thinking framework.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Co-developed with academic partners; also on Coursera. Strongest official content on AI limits."
  },
  {
    "title": "AI Fluency for Students",
    "url": "https://www.coursera.org/learn/ai-fluency-for-students",
    "author": "Anthropic",
    "roles": ["researcher"],
    "level": "never-used",
    "topics": ["chat-prompting", "safety"],
    "format": "course",
    "time": "under-1hr",
    "cost": "free-account",
    "language": "en",
    "tier": "previewed",
    "summary": "Short course (5 lectures, ~30 min) applying the 4D framework to student work, emphasizing learning-with-AI vs outsourcing.",
    "who_for": "PhD/grad students wanting responsible AI habits.",
    "skip_if": "You're faculty seeking advanced research workflows.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Also on anthropic.skilljar.com/ai-fluency-for-students; enroll-free on Coursera."
  },
  {
    "title": "Plan your literature review (use-case)",
    "url": "https://claude.com/resources/use-cases/plan-your-literature-review",
    "author": "Anthropic",
    "roles": ["researcher"],
    "level": "basic",
    "topics": ["chat-prompting", "mcp"],
    "format": "article",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Official worked example using the PubMed connector and Google Drive integration to build a structured, prioritized reading guide from a research question.",
    "who_for": "Researchers wanting a vendor-blessed lit-review starting workflow.",
    "skip_if": "You need explicit citation-verification guidance — the page does not warn about fabricated references, so add that step yourself.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "CITATION RISK: teaches lit-review discovery without a fabricated-citation warning."
  },
  {
    "title": "Use research on Claude",
    "url": "https://support.claude.com/en/articles/11088861-use-research-on-claude",
    "author": "Anthropic",
    "roles": ["researcher"],
    "level": "basic",
    "topics": ["chat-prompting", "agents"],
    "format": "docs",
    "time": "under-15min",
    "cost": "subscription",
    "language": "en",
    "tier": "reviewed",
    "summary": "Authoritative Help Center article on the agentic Research feature: multi-step searches across web and connected internal sources, delivered with checkable citations.",
    "who_for": "Paid-plan researchers doing deep, multi-source syntheses.",
    "skip_if": "You're on the free plan (Research needs Pro/Max/Team/Enterprise).",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Requires web search on; consumes usage limits faster."
  },
  {
    "title": "Enabling and using the analysis tool",
    "url": "https://support.anthropic.com/en/articles/10008684-enabling-and-using-the-analysis-tool",
    "author": "Anthropic",
    "roles": ["researcher"],
    "level": "basic",
    "topics": ["chat-prompting"],
    "format": "docs",
    "time": "under-15min",
    "cost": "free-account",
    "language": "en",
    "tier": "reviewed",
    "summary": "Canonical setup/use guide for Claude's in-chat analysis tool: run code, do computation, and analyze/visualize CSV data.",
    "who_for": "Researchers doing quick data cleaning, stats and charts inside chat.",
    "skip_if": "You want the newer server-side code execution.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "OUTDATED-RISK: the original JavaScript analysis tool was superseded by server-side code execution (Sep 2025)."
  },
  {
    "title": "What are Projects?",
    "url": "https://support.claude.com/en/articles/9517075-what-are-projects",
    "author": "Anthropic",
    "roles": ["researcher"],
    "level": "basic",
    "topics": ["chat-prompting", "skills"],
    "format": "docs",
    "time": "under-15min",
    "cost": "free-account",
    "language": "en",
    "tier": "reviewed",
    "summary": "Explains Projects: self-contained workspaces with a knowledge base and custom instructions that persist across chats.",
    "who_for": "Researchers wanting a reusable, context-rich setup per paper/topic.",
    "skip_if": "You already use Projects.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Free tier = 5 projects; RAG on paid plans expands knowledge-base capacity."
  },
  {
    "title": "Prompt Engineering Interactive Tutorial",
    "url": "https://github.com/anthropics/prompt-eng-interactive-tutorial",
    "author": "Anthropic",
    "roles": ["researcher"],
    "level": "confident",
    "topics": ["chat-prompting", "api"],
    "format": "hands-on",
    "time": "half-day",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "Official 9-chapter hands-on prompting course with exercises, including a dedicated chapter on avoiding hallucinations; runnable notebooks plus a Google Sheets version.",
    "who_for": "Researchers comfortable running notebooks who want disciplined prompting skills.",
    "skip_if": "You want a no-setup, non-technical intro.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "OUTDATED-RISK: examples use Claude 3 Haiku; techniques transfer, model-specific behavior may not. Needs an Anthropic API key for interactive exercises."
  },
  {
    "title": "Anthropic's AI for Science Program",
    "url": "https://support.claude.com/en/articles/11199177-anthropic-s-ai-for-science-program",
    "author": "Anthropic",
    "roles": ["researcher"],
    "level": "confident",
    "topics": ["api"],
    "format": "docs",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Program giving up to $20,000 in Anthropic API credits over a 6-month period to researchers at academic/nonprofit institutions (biology/life-sciences focus).",
    "who_for": "Researchers who can use the API for high-impact scientific work.",
    "skip_if": "Your work isn't API-based or high-impact science.",
    "published": "2025-05-05",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Applications reviewed monthly; credits are API-only (not claude.ai). A July 2026 rare-disease track offers up to $50,000."
  },
  {
    "title": "How scientists are using Claude to accelerate research",
    "url": "https://www.anthropic.com/news/accelerating-scientific-research",
    "author": "Anthropic",
    "roles": ["researcher"],
    "level": "basic",
    "topics": ["agents", "api"],
    "format": "article",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Overview of real lab use of Claude (e.g. Stanford's Biomni agentic platform) that helps calibrate realistic expectations.",
    "who_for": "Researchers wanting grounded examples of what Claude does in science.",
    "skip_if": "You want a hands-on how-to.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Vendor blog — motivational context, not a tutorial."
  },
  {
    "title": "Claude Code & CoWork for Academics (Beginner Guide, Part 1)",
    "url": "https://effortlessacademic.com/claude-code-and-cowork-for-academics-beginner-guide-part-1/",
    "author": "Effortless Academic (Ilya Shabanov)",
    "roles": ["researcher"],
    "level": "confident",
    "topics": ["claude-code", "cowork"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Non-coder-friendly intro to installing and using Claude Code/CoWork for academic tasks (synthesizing PDFs, restructuring data), with honest caveats about hype.",
    "who_for": "Researchers ready to move from chat to file/agent workflows.",
    "skip_if": "You're strongly terminal-averse — Claude Code may still feel like a stretch.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Part 1 of a series; unusually candid ('don't outsource your cognitive sovereignty')."
  },
  {
    "title": "Claude Skills for Academics (Beginner Tutorial, Part 2)",
    "url": "https://effortlessacademic.com/claude-skills-for-academics-beginner-tutorial-part-2/",
    "author": "Effortless Academic (Ilya Shabanov)",
    "roles": ["researcher"],
    "level": "builder",
    "topics": ["skills", "cowork"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "How to create and use Claude Skills for academic work, e.g. an atomic-sentence writing method that keeps references attached to claims.",
    "who_for": "Researchers who've done Part 1 and want reusable writing automations.",
    "skip_if": "You've never used Claude — start with Part 1.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Uses third-party Obsidian skills; reference-grounded approach reduces (but doesn't eliminate) fabrication risk."
  },
  {
    "title": "Connect and integrate your local Zotero library with Claude Cowork",
    "url": "https://effortlessacademic.com/connect-and-integrate-your-local-zotero-library-with-claude-cowork/",
    "author": "Effortless Academic (Ilya Shabanov)",
    "roles": ["researcher"],
    "level": "confident",
    "topics": ["mcp", "cowork"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "No-terminal walkthrough of connecting a local Zotero library to Claude via an MCP connector to search, annotate and reason over your own papers.",
    "who_for": "Zotero users who want Claude to work from their real library, not its training memory.",
    "skip_if": "You don't use Zotero.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Grounding Claude in your library reduces fabrication risk but doesn't remove it."
  },
  {
    "title": "zotero-mcp (54yyyu)",
    "url": "https://github.com/54yyyu/zotero-mcp",
    "author": "Community (54yyyu)",
    "roles": ["researcher"],
    "level": "builder",
    "topics": ["mcp"],
    "format": "repo",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "Widely-used Zotero MCP server connecting your library to Claude: search, metadata, PDF full-text, semantic search, retraction alerts; local and web API modes.",
    "who_for": "Technically comfortable researchers wanting deep Claude+Zotero integration.",
    "skip_if": "You aren't comfortable running installs.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Community-built; there is NO official Zotero connector. Pair with ehawkin/zotero-mcp-setup for easier install."
  },
  {
    "title": "zotero-mcp-setup (GUI installer)",
    "url": "https://github.com/ehawkin/zotero-mcp-setup",
    "author": "Community (ehawkin)",
    "roles": ["researcher"],
    "level": "confident",
    "topics": ["mcp"],
    "format": "repo",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "One-click Mac (DMG)/Windows installer scripts and step-by-step guide to connect Zotero to Claude without terminal experience.",
    "who_for": "Non-terminal researchers who still want the Zotero-MCP capability.",
    "skip_if": "You prefer manual MCP configuration.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Wraps the community zotero-mcp; verify scripts before running."
  },
  {
    "title": "Claude AI and Literature Reviews: An Experiment in Utility and Ethical Use",
    "url": "https://muse.jhu.edu/article/961199",
    "author": "Max Sparkman & Alan Witt, Library Trends 73(3):355-380",
    "roles": ["researcher"],
    "level": "confident",
    "topics": ["safety", "chat-prompting"],
    "format": "article",
    "time": "under-1hr",
    "cost": "paid-once",
    "language": "en",
    "tier": "reviewed",
    "summary": "Peer-reviewed study comparing a Claude-produced literature review to a human one; documents Claude's strengths (summarizing agreement) and limits (weak synthesis, incomplete + hallucinated citations).", [ResearchGate](https://www.researchgate.net/publication/392174837_Claude_AI_and_Literature_Reviews_An_Experiment_in_Utility_and_Ethical_Use)
    "who_for": "Researchers wanting evidence, not hype, on Claude's real lit-review limits.",
    "skip_if": "You want a step-by-step how-to.",
    "published": "2025-02-01",
    "checked": "2026-08-18",
    "status": "live",
    "field": "library and information science",
    "notes": "DOI 10.1353/lib.2025.a961199. The ONLY peer-reviewed study that actually tested Claude on a lit review; reports fabrication qualitatively, not as a rate. Open-access copy: knightscholar.geneseo.edu/library-research/22/."
  },
  {
    "title": "Claude for medical literature search: Avoid hallucinations",
    "url": "https://lszabo.me/posts/ai-literature-search/",
    "author": "Laszlo Szabo",
    "roles": ["researcher"],
    "level": "confident",
    "topics": ["safety", "mcp", "chat-prompting"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Verification-first workflow for AI-assisted literature search: PubMed connector setup plus habits like 'ask for the PMID; if it doesn't resolve, the citation is fabricated.'",
    "who_for": "Clinicians/researchers who want to use Claude on literature safely.",
    "skip_if": "You want an official Anthropic source.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "field": "medicine",
    "notes": "Individual clinician-researcher; strongest honest treatment of the fabrication problem found."
  },
  {
    "title": "Claude Researcher — source-first literature review workflows",
    "url": "https://www.clauderesearcher.com/",
    "author": "Independent (unaffiliated with Anthropic)",
    "roles": ["researcher"],
    "level": "confident",
    "topics": ["safety", "chat-prompting", "mcp"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "Independent guide to source-first lit review with Claude: citation-checking protocol, role separation, PRISMA discipline, and links to primary sources.",
    "who_for": "Researchers wanting a citation-discipline-focused workflow.",
    "skip_if": "You require an official or named-institution source.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Explicitly states it is not affiliated with Anthropic; strong on citation verification."
  },
  {
    "title": "Academic Research with Claude (live seminar)",
    "url": "https://aihorizons.io/Seminars/claude-academic-research/",
    "author": "AI Horizons",
    "roles": ["researcher"],
    "level": "confident",
    "topics": ["chat-prompting", "cowork", "claude-code"],
    "format": "course",
    "time": "half-day",
    "cost": "paid-once",
    "language": "en",
    "tier": "previewed",
    "summary": "Live online seminar teaching Claude (claude.ai, Projects, CoWork, Claude Code) as an integrated, reproducible research infrastructure across the research lifecycle.",
    "who_for": "Faculty/postdocs/advanced grad students with basic prompting + some R/Python.",
    "skip_if": "You prefer free, self-paced material.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Part of a paid 4-course certification; no prior Claude/coding experience required per syllabus."
  },
  {
    "title": "Introduction to Claude Analysis",
    "url": "https://www.codecademy.com/learn/ext-courses/introduction-to-claude-analysis",
    "author": "Codecademy",
    "roles": ["researcher"],
    "level": "basic",
    "topics": ["chat-prompting"],
    "format": "course",
    "time": "under-1hr",
    "cost": "free-account",
    "language": "en",
    "tier": "previewed",
    "summary": "Short course on Claude's analysis tool: uploading/cleaning CSVs, basic statistics, and visualization via React artifacts.",
    "who_for": "Researchers wanting a gentle intro to in-chat data analysis.",
    "skip_if": "You need the newer server-side code execution or advanced stats.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "OUTDATED-RISK: the analysis tool is being replaced by code execution; screens may differ."
  },
  {
    "title": "15 Claude Tips for Everyday Data Analysis",
    "url": "https://www.linkedin.com/learning/topics/claude",
    "author": "LinkedIn Learning",
    "roles": ["researcher"],
    "level": "basic",
    "topics": ["chat-prompting"],
    "format": "video",
    "time": "under-1hr",
    "cost": "subscription",
    "language": "en",
    "tier": "listed",
    "summary": "Short (21 min) practical course of everyday data-analysis tips with Claude.",
    "who_for": "Researchers with LinkedIn Learning access wanting quick data tips.",
    "skip_if": "You have no LinkedIn Learning subscription.",
    "published": "2026-04-14",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Metadata only (course behind subscription); release date from LinkedIn Learning listing."
  },
  {
    "title": "Andy Stapleton — AI for academia (YouTube)",
    "url": "https://www.youtube.com/@DrAndyStapleton",
    "author": "Andy Stapleton, PhD",
    "roles": ["researcher"],
    "level": "basic",
    "topics": ["chat-prompting", "cowork", "skills"],
    "format": "video",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "listed",
    "summary": "Channel by an ex-academic chemist (288k+ subscribers) covering AI tools for research, including Claude Projects/Skills/CoWork, with honest tool testing.",
    "who_for": "Researchers who learn by watching and want a working-academic perspective.",
    "skip_if": "You prefer text; note some videos are tool-promotional.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Individual creator; quality varies by video. Has publicly criticized undisclosed AI text in peer review."
  },
  {
    "title": "Mushtaq Bilal — Claude for Academic Writing & Research",
    "url": "https://mushtaqbilalphd.kit.com/",
    "author": "Mushtaq Bilal, PhD",
    "roles": ["researcher"],
    "level": "confident",
    "topics": ["claude-code", "chat-prompting"],
    "format": "podcast",
    "time": "under-1hr",
    "cost": "paid-once",
    "language": "en",
    "tier": "listed",
    "summary": "Webinars, threads and a newsletter aimed at non-technical academics learning Claude/Claude Code for writing and research (e.g. automating systematic-review screening).",
    "who_for": "Non-technical academics wanting approachable, research-focused guidance.",
    "skip_if": "You want to avoid disclosure-evasion tactics — he has promoted AI-'humanizer' tricks to defeat AI detection.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "CAUTION: some content promotes making AI text 'pass' as human, which conflicts with publisher disclosure rules. Webinars are paid; many threads free."
  },
  {
    "title": "ICMJE Recommendations — Use of AI in Publishing",
    "url": "https://www.icmje.org/recommendations/browse/artificial-intelligence/",
    "author": "International Committee of Medical Journal Editors",
    "roles": ["researcher"],
    "level": "basic",
    "topics": ["safety"],
    "format": "docs",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Authoritative policy: disclose AI use in cover letter and manuscript; AI cannot be an author or be cited as author; AI-generated material is not an acceptable primary source.",
    "who_for": "Any author submitting to medical/biomedical journals.",
    "skip_if": "Your field follows a different body (still align with your target journal).",
    "published": "2026-01-01",
    "checked": "2026-08-18",
    "status": "live",
    "field": "medicine",
    "notes": "Current recommendations updated Jan 2026 per ICMJE."
  },
  {
    "title": "Nature Portfolio — Artificial Intelligence (AI) editorial policy",
    "url": "https://www.nature.com/nature-portfolio/editorial-policies/ai",
    "author": "Springer Nature (Nature Portfolio)",
    "roles": ["researcher"],
    "level": "basic",
    "topics": ["safety"],
    "format": "docs",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Risk-assessment framework: human accountability can't be transferred to AI; AI may support but not replace judgement; transparency and confidentiality required. AI can't be author; disclose LLM use in Methods; reviewers must not upload manuscripts to unsecured/public AI tools.",
    "who_for": "Authors and reviewers for Nature Portfolio journals.",
    "skip_if": "You publish only outside Springer Nature (still check your publisher).",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "'AI assisted copy editing' is exempt from disclosure; AI-generated images generally prohibited."
  },
  {
    "title": "Elsevier — Generative AI policies for journals",
    "url": "https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals",
    "author": "Elsevier",
    "roles": ["researcher"],
    "level": "basic",
    "topics": ["safety"],
    "format": "docs",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Disclose generative-AI use; authors must independently verify factual statements and that cited sources are accurate and correctly represented; AI-generated/altered images prohibited; AI not an author.",
    "who_for": "Authors submitting to Elsevier journals.",
    "skip_if": "You publish only outside Elsevier.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Policy applies to the writing process; code written with AI must be declared in Methods."
  },
  {
    "title": "IEEE — Author Guidelines for AI-Generated Text",
    "url": "https://open.ieee.org/author-guidelines-for-artificial-intelligence-ai-generated-text/",
    "author": "IEEE",
    "roles": ["researcher"],
    "level": "basic",
    "topics": ["safety"],
    "format": "docs",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "AI-generated content (text, figures, images, code) must be disclosed in the Acknowledgments, naming the system and the affected sections; grammar/editing use is recommended-but-not-required to disclose.",
    "who_for": "Authors submitting to IEEE conferences/journals.",
    "skip_if": "You publish only outside IEEE.",
    "published": "UNVERIFIED",
    "checked": "2026-08-18",
    "status": "live",
    "notes": "Reviewers must not process manuscripts through public AI tools (confidentiality). Exclude the reference list from AI editing."
  }
]
```

---

## Most surprising during the research (2–3 sentences)
The most striking finding is that the citation-fabrication statistics researchers cite most often — the JMIR "19.9% fabricated" (Linardon et al.) and "28.6%/91.4%" (Chelli et al.) figures — are **not about Claude at all** (they tested GPT-4o and Bard); [JMIR](https://www.jmir.org/2024/1/e53164) the only peer-reviewed study that actually put Claude through a literature review reports its fabrication problem qualitatively, with no percentage, so there is effectively no trustworthy "Claude fabricates X%" number in the literature. It was also surprising how quickly official material dates: Anthropic renamed and replaced its data "analysis tool" within a year, and even Anthropic's own flagship prompt-engineering tutorial still teaches on the retired Claude 3 Haiku. Finally, the best research-specific teaching came overwhelmingly from individual working academics (Shabanov, Szabo, Stapleton, Bilal) rather than universities or big MOOC platforms — and one of those popular educators openly promotes AI-"humanizer" detection-evasion tricks that directly conflict with the disclosure rules every major publisher now enforces.