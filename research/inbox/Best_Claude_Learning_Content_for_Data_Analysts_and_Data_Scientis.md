# Best Claude Learning Content for Data Analysts & Data Scientists (checked 2026-08-19)

**TL;DR**
- The single best starting stack is official and free: Anthropic's **Claude 101** and **Introduction to Claude Cowork** (Anthropic Academy), the Help Center article on the **analysis tool**, and the **Use Claude for Excel** docs — all current as of August 19, 2026 and honest about verification limits.
- For "doing, not watching," go to **anthropics/claude-cookbooks** (the `managed_agents/data_analyst_agent.ipynb` and `skills/` notebooks with real financial CSVs) and analyst write-ups like **Vincent Codes Finance** and the "significant"-threshold Towards Data Science skill guide, which explicitly teach checking AI output against the data.
- The dangerous gap everywhere is verification: most tutorials show a query that runs and stop there. Uprank Anthropic's **Reduce hallucinations** docs and the honest CSV/Excel guides; treat any "AI analytics tool" demo (Coupler.io, Windsor.ai, ClickUp, Julius) as marketing, not training.

## Key Findings
1. Anthropic's own catalog is the most trustworthy and the most current, but it is **not** data-analyst-specific — Claude 101 and Cowork teach general workflows you adapt to data work. The genuinely data-focused official assets are the **analysis tool** Help Center article, the **Claude for Excel** docs, and the **claude-cookbooks** notebooks.
2. The best hands-on, honest third-party material comes from working analysts and data educators (DataCamp code-alongs, LinkedIn Learning's Emma Chieppor course, Vincent Codes Finance, Towards Data Science). Downrank SEO round-ups ("13 free courses…") and vendor pages.
3. The MCP layer is where analysts get real leverage (databases, warehouses, BI). The **official Anthropic Postgres reference server is archived and has a documented SQL-injection flaw** — do not use it. Use **crystaldba/postgres-mcp**, **motherduckdb/mcp-server-motherduck**, or **tableau/tableau-mcp** instead.
4. Correctness is the recurring blind spot. Only a minority of resources teach that Claude has two CSV modes (text-reasoning vs. the code-executing analysis tool) and that the text mode can silently hallucinate sums.

## Details

### Reviewed / previewed / listed items

| Title | URL | Author/Source | Format | Level | Time | Cost | Tier | Tools covered | Why it's good | Skip if |
|---|---|---|---|---|---|---|---|---|---|---|
| Claude 101 | https://anthropic.skilljar.com/claude-101 | Anthropic Academy | course | basic | under-1hr | free-account | previewed | Claude.ai, Excel, connectors | Official, current, covers file upload/analysis and when to pick connectors vs. search; honest framing | You already use Claude daily |
| Introduction to Claude Cowork | https://anthropic.skilljar.com/introduction-to-claude-cowork | Anthropic Academy | hands-on | basic | under-1hr | free-account | previewed | Cowork desktop, files, plugins, skills | Teaches the task loop on real files and "steering multi-step work responsibly" [Anthropic Courses](https://anthropic.skilljar.com/) | You only use the web chat |
| Enabling and using the analysis tool | https://support.anthropic.com/en/articles/10008684-enabling-and-using-the-analysis-tool | Anthropic Help Center | docs | basic | under-15min | free | reviewed | Analysis tool, CSV | The canonical how-to for the code sandbox that gives verifiable numbers; explains the context-window limit [anthropic](https://support.anthropic.com/en/articles/10008684-enabling-and-using-the-analysis-tool) | You need depth beyond setup |
| Use Claude for Excel | https://support.claude.com/en/articles/12650343-use-claude-for-excel | Anthropic Help Center | docs | basic | under-15min | subscription | reviewed | Excel add-in, cell citations | Current GA docs; unusually honest — lists "audit-critical calculations without verification" as a non-use [Claude](https://support.claude.com/en/articles/12650343-use-claude-for-excel) | You don't use Excel |
| Reduce hallucinations | https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations | Anthropic Platform Docs | docs | confident | under-15min | free | reviewed | Prompting, grounding, citations | The verification playbook: allow "I don't know," quote-grounding, best-of-N, chain-of-thought checks [Claude Platform Docs](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) | You want data-specific recipes |
| claude-cookbooks: data_analyst_agent | https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/data_analyst_agent.ipynb | Anthropic | repo | builder | half-day | free-account | previewed | Python, pandas, plotly, API | Working notebook: hand a CSV, get a narrative HTML report; reproducible steps [GitHub](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/data_analyst_agent.ipynb) | You don't code in Python |
| claude-cookbooks: skills notebooks | https://github.com/anthropics/claude-cookbooks/tree/main/skills | Anthropic | repo | builder | half-day | free-account | previewed | Python, Excel/PPTX/PDF, financial CSVs | Real sample financial datasets; teaches building reusable analysis Skills [GitHub](https://github.com/anthropics/claude-cookbooks/blob/main/skills/README.md) | Not building Skills |
| Prompt Engineering Interactive Tutorial | https://github.com/anthropics/prompt-eng-interactive-tutorial | Anthropic | repo | basic | half-day | free | previewed | API, prompting, SQL prompting | Best structured prompting course; 9 chapters w/ exercises [GitHub](https://github.com/anthropics/prompt-eng-interactive-tutorial) incl. data separation | You want current-model specifics |
| Introduction to the analysis tool (blog) | https://anthropic.com/news/analysis-tool | Anthropic | article | basic | under-15min | free | reviewed | Analysis tool, CSV, viz | Explains why code execution yields "mathematically precise and reproducible" [techradar](https://www.techradar.com/pro/anthropic-updates-claude-ai-to-write-and-run-javascript-code) answers [anthropic](https://anthropic.com/news/analysis-tool) | Published Oct 2024 — dated framing |
| Introduction to Claude Analysis | https://www.codecademy.com/learn/ext-courses/introduction-to-claude-analysis | Codecademy | course | basic | under-1hr | free-account | previewed | CSV, stats, React Artifacts | Structured beginner path: upload, repair data issues, basic stats, visualize [Codecademy](https://www.codecademy.com/learn/ext-courses/introduction-to-claude-analysis) | You're notebook-native already |
| 15 Claude Tips for Everyday Data Analysis | https://www.linkedin.com/learning/15-claude-tips-for-everyday-data-analysis | Emma Chieppor (LinkedIn Learning) | video | basic | under-1hr | subscription | previewed | Spreadsheets, formulas, troubleshooting | Bite-size, Excel-primary, covers pitfalls and auditing data with Claude [Johns Hopkins University](https://imagine.jhu.edu/classes/15-claude-tips-for-everyday-data-analysis/) | No LinkedIn Learning access |
| Create Claude Skills for Data Tasks | https://www.datacamp.com/code-along/create-claude-skills-for-data-tasks | Tom Farnschläder (DataCamp) | hands-on | confident | under-1hr | free-account | previewed | Python, EDA, feature engineering | Builds EDA/feature-engineering Skills on a real soccer dataset [DataCamp](https://www.datacamp.com/code-along/create-claude-skills-for-data-tasks) | You don't want DataCamp's env |
| Introduction to Claude (code-along) | https://www.datacamp.com/code-along/introduction-to-claude | Aimée Gott (DataCamp) | hands-on | basic | under-1hr | free-account | previewed | Python, SQL, prompting | Shows a data-analysis workflow generating Python and SQL [DataCamp](https://www.datacamp.com/code-along/introduction-to-claude) [DataCamp](https://www.datacamp.com/blog/best-resources-learn-claude) | Too introductory for you |
| Sales Analysis with Claude | https://www.coursera.org/projects/sales-analysis-with-claude-data-driven-sales-analytics | Hussein ElGhoul (Coursera) | hands-on | basic | under-1hr | subscription | listed | Claude.ai Pro, viz | Guided project: trends, pattern recognition, exec recommendations [coursera](https://www.coursera.org/projects/sales-analysis-with-claude-data-driven-sales-analytics) | Requires Claude Pro; shallow |
| Claude Code for Data Analysis | https://vincent.codes.finance/posts/claude-code-data-analysis/ | Vincent Grégoire (Vincent Codes Finance) | article | confident | under-1hr | free | reviewed | Claude Code, Python, MCP, context7 | Analyst-grade workflow: infer schema to a Markdown file, use MCP for live docs, reproducibility [Codes](https://vincent.codes.finance/posts/claude-code-data-analysis/) | You never touch a terminal |
| Claude Code is secretly an excellent data analysis tool | https://yang3kc.substack.com/p/claude-code-is-secretly-an-excellent | Kai-Cheng Yang | article | confident | under-1hr | free | reviewed | Claude Code, Python, Jupyter, git | Researcher's honest account (98% of code generated); [Substack](https://yang3kc.substack.com/p/claude-code-is-secretly-an-excellent) real setups and caveats | You want beginner material |
| 3 Claude Skills Every Data Scientist Needs in 2026 | https://towardsdatascience.com/3-claude-skills-every-data-scientist-needs-in-2026/ | Towards Data Science | article | confident | under-1hr | free | previewed | Skills, EDA, dashboards | Practical Skills for EDA/dashboards with real insights from an energy dataset [Towards Data Science](https://towardsdatascience.com/3-claude-skills-every-data-scientist-needs-in-2026/) | Not using Skills |
| 4 Lines You Should Include in Your Claude Skill | https://towardsdatascience.com/4-lines-you-must-include-in-your-claude-skill/ | Towards Data Science | article | confident | under-15min | free | reviewed | Skills, prompting, verification | Best verification advice found: force Claude to define "significant" with real thresholds [Towards Data Science](https://towardsdatascience.com/4-lines-you-must-include-in-your-claude-skill/) | You don't write Skills |
| Data Analysis with Claude Code (not just for programmers) | https://medium.com/data-science-collective/data-analysis-with-claude-code-its-not-just-for-programmers-08adb529a70d | Alan Jones | article | basic | under-1hr | free | previewed | Claude Code, charts, reports | Non-coder walkthrough analyzing 78 years of weather data end to end [Medium](https://medium.com/data-science-collective/data-analysis-with-claude-code-its-not-just-for-programmers-08adb529a70d) | You want deep technical detail |
| Claude Code for Data Analysis: Excel-Free Answers From CSVs | https://ccforeveryone.com/guides/claude-code-for-data-analysts | CC for Everyone | article | confident | under-1hr | free | reviewed | Claude Code, CSV, verification | Strong on verification: "smell test," spot-check rows, scripts over cell edits (cites Panko's spreadsheet-error research) | You want official docs |
| How to Use Claude for CSV Data Analysis (Honest Guide) | https://www.qwe.edu.pl/tutorial/claude-csv-data-analysis/ | QWE AI Academy | article | confident | under-1hr | free | previewed | Analysis tool, CSV | Explains the two CSV modes and silent-sum hallucination; [QWE AI Academy](https://www.qwe.edu.pl/tutorial/claude-csv-data-analysis/) lesser-known source but technically sound | You want a named, established author |
| crystaldba/postgres-mcp (Postgres MCP Pro) | https://github.com/crystaldba/postgres-mcp | Crystal DBA | repo | builder | under-1hr | free | listed | Postgres, SQL, EXPLAIN, index tuning | Recommended Postgres connector; read-only mode, health checks [Awesome Claude](https://awesomeclaude.ai/how-to/connect-postgresql-with-claude) | You don't use Postgres |
| motherduckdb/mcp-server-motherduck | https://github.com/motherduckdb/mcp-server-motherduck | MotherDuck | repo | builder | under-1hr | free | listed | DuckDB, MotherDuck, SQL | Query local DuckDB or cloud warehouse in natural language; read-only by default [GitHub](https://github.com/motherduckdb/mcp-server-motherduck) | No DuckDB/warehouse |
| tableau/tableau-mcp | https://github.com/tableau/tableau-mcp | Tableau (Salesforce) | repo | builder | under-1hr | free | listed | Tableau Cloud/Server, Pulse | Official, well-maintained BI connector; OAuth, per-user permissions [Carly AI Blog](https://www.usecarly.com/blog/claude-tableau-integration/) | You don't use Tableau |
| IMNMV/ClaudeR | https://github.com/IMNMV/ClaudeR | IMNMV | repo | builder | half-day | free | listed | R, RStudio, MCP, stats | Connects RStudio to Claude; built-in reproducible stats protocol + "Reviewer Zero" auditing [GitHub](https://github.com/IMNMV/ClaudeR) | You don't use R |

### Dead or moved links
- **anthropic-cookbook → claude-cookbooks.** The old `github.com/anthropics/anthropic-cookbook` now redirects to `github.com/anthropics/claude-cookbooks` (renamed). Use the new URL.
- **support.anthropic.com → support.claude.com.** Anthropic's Help Center migrated domains; older `support.anthropic.com` article links (e.g. the analysis-tool article) still resolve but the canonical home is now `support.claude.com`.
- **@modelcontextprotocol/server-postgres and server-sqlite** reference servers were moved out of `modelcontextprotocol/servers` into `modelcontextprotocol/servers-archived` (repo archived read-only on May 29, 2025, per Datadog Security Labs).

### Looks outdated
- **anthropic.com/news/analysis-tool** (Oct 24, 2024) — still accurate on concept but references Claude 3.5 Sonnet and predates Excel/Cowork; treat as background.
- **anthropics/prompt-eng-interactive-tutorial** — excellent structure but examples use Claude 3 Haiku; [GitHub](https://github.com/anthropics/prompt-eng-interactive-tutorial/blob/master/README.md) model-specific behavior is historical. The prompting principles remain valid.
- **MattStockton/courses** and other forks of the old Anthropic "courses" repo favor Claude 3 Haiku and predate Skills/Cowork/MCP maturity — prefer the current Skilljar catalog.
- Any generic "13/20 free Claude courses" round-ups (Medium/Termdock/Spectrum AI Labs) are SEO aggregations; go to the primary Skilljar catalog instead.

### Avoid (SEO spam / vendor demos dressed as training)
- **Coupler.io** ("How to Use Claude.ai for Data Analytics") and **Windsor.ai / Supermetrics / Catchr** "Connect X to Claude" pages — product funnels for paid MCP/connector services; transferable content is thin.
- **ClickUp** "How to Use Claude for Spreadsheet Analysis" and **Julius AI** placements inside course round-ups — product marketing.
- **datastudios.org**, **claudereadiness.com**, **theanalyticsdoctor.com**, **claudeinexcel.com**, **ai.cc** — SEO content farms restating features; not hands-on and often unattributed. `claudeinexcel.com` even discloses it is not affiliated with Anthropic. [Claude in Excel](https://claudeinexcel.com/official-claude-for-microsoft-365-add-in)
- **DataCamp's "Best Resources for Learning Claude"** blog is useful but self-referential — every link points back to DataCamp; treat as a DataCamp catalog, not a neutral guide.

### MCP servers worth knowing (databases & data tools)
| Server | Repo | What it does | Maintenance (checked 2026-08-19) |
|---|---|---|---|
| Postgres MCP Pro | https://github.com/crystaldba/postgres-mcp | Read/write-configurable Postgres access, EXPLAIN analysis, index tuning, health checks [GitHub](https://github.com/crystaldba/postgres-mcp) | Active, not archived; ~3.2k stars; 80 commits on main; no releases listed |
| MotherDuck / DuckDB | https://github.com/motherduckdb/mcp-server-motherduck | SQL analytics over local DuckDB or MotherDuck cloud; read-only by default | Active; ~488 stars; latest release v1.0.7 (Jun 9, 2026) |
| Tableau (official) | https://github.com/tableau/tableau-mcp | Query datasources, search workbooks, pull Pulse metrics; OAuth, per-user perms | Active, Tableau-supported; ~302 stars; latest release v2.21.1 (Jul 2, 2026); hosted endpoint at mcp.tableau.com [Carly AI Blog](https://www.usecarly.com/blog/claude-tableau-integration/) |
| Multi-DB (executeautomation) | https://github.com/executeautomation/mcp-database-server | One server for SQLite, SQL Server, PostgreSQL, MySQL | Active but low activity; ~379 stars; 35 commits |
| ClaudeR (R + RStudio) | https://github.com/IMNMV/ClaudeR | Connects RStudio to Claude/Codex/Gemini via MCP; reproducible stats + manuscript auditing | Active; ~255 stars; latest release v0.3.1 (Mar 24, 2026) |
| MCP reference servers | https://github.com/modelcontextprotocol/servers | Current reference set: filesystem, fetch, git, memory, time, sequential-thinking, everything | Active; ~86.7k stars; latest release 2026.1.26 (Jan 27, 2026) |

**Do not use:** `@modelcontextprotocol/server-postgres`. Datadog Security Labs documented a read-only-bypass SQL-injection vulnerability in this reference server ("We found a SQL injection vulnerability in Anthropic's reference Postgres MCP server that allowed us to bypass the read-only restriction and execute arbitrary SQL statements"), with a payload as destructive as `COMMIT; DROP SCHEMA public CASCADE`. Anthropic fixed it in git on May 29, 2025 and archived the server the same day, then formally deprecated it July 10, 2025 — but v0.6.2 on npm/Docker was never patched and still draws roughly 312,000 installs a month (Datadog cited ~21,000 weekly npm downloads). If you must use that lineage, the patched fork is Zed Industries' `@zeddotdev/postgres-context-server` v0.1.4; otherwise prefer Postgres MCP Pro.

**Vet community Skills and MCP servers before production.** Snyk's ToxicSkills audit (published Feb 5, 2026) scanned 3,984 skills from ClawHub and skills.sh and found prompt injection in 36% (1,467 skills), critical-level security issues in 13.4% (534 of 3,984), and 76 confirmed malicious payloads (8 still live at publication). Always connect databases through a dedicated read-only, least-privilege role rather than relying on a server's own "read-only" claim.

### Gaps (what analysts need but nobody has made well)
- A single, current, **vendor-neutral course on verifying Claude's analytical output** — the two-CSV-modes trap, reconciling totals, spot-checking rows, and a repeatable QA checklist. Bits exist across blogs; no authoritative course.
- **R-first** learning material — nearly everything is Python/Excel; ClaudeR and a few community Skills are the exception.
- An honest, updated **"Claude chat vs. the analysis tool vs. Claude Code vs. Claude for Excel — which surface for which task"** decision guide from a neutral source.
- **Reproducible reporting/automation** (scheduled recurring reports with saved, rerunnable scripts) taught end-to-end for non-engineers.
- **Stakeholder communication** — turning verified analysis into honest, non-overconfident narratives; the "define significant" TDS post is the closest thing.

## Recommendations
1. **Everyone starts here (½ day, free):** Claude 101 → the analysis-tool Help Center article → Reduce hallucinations docs. This gives you the tool, the workflow, and the verification mindset before you touch real data.
2. **Excel-primary users:** add the Use Claude for Excel docs + Emma Chieppor's LinkedIn Learning course. Benchmark to advance: you can get a workbook analysis *and* independently verify two of its numbers against source cells.
3. **Notebook-native users:** go straight to claude-cookbooks (`data_analyst_agent.ipynb` + `skills/`) and Vincent Codes Finance. Benchmark: you have Claude write its schema understanding to a Markdown file and save reusable, rerunnable scripts.
4. **When you need databases/BI:** add exactly one MCP server for your stack (Postgres MCP Pro, MotherDuck, or Tableau), always via a read-only role. Threshold to expand: only add a second connector once the first is stable and audited.
5. **Change your plan if:** Anthropic ships a dedicated data-analyst course or renames the analysis tool/Excel features (these change every few months) — re-verify the Help Center and Skilljar catalog before relying on any third-party tutorial older than ~6 months.

## Caveats
- "checked" = 2026-08-19 for every item. Course pages that gate content behind login were **previewed** (syllabus/description) not fully completed; blogs I read in full are **reviewed**; repos and login-walled videos are **listed**.
- Anthropic does not publish completion times or fixed prices on Skilljar course pages; time/cost fields are best estimates from descriptions and marked accordingly.
- GitHub landing pages render last-commit dates via JavaScript, so exact last-push dates were not directly readable; I report latest-release dates and commit counts as recency proxies (all six recommended repos are active and non-archived).
- File-handling features (analysis tool, Excel add-in, Cowork, Skills) are changing rapidly; any resource older than ~12 months may describe a stale UI even if the concepts hold.
- The Panko figure referenced in the CC-for-Everyone guide traces to Raymond Panko's field-audit literature review ("94% of spreadsheets have errors, with an average cell error rate of 5.2%"), a useful anchor for why human verification of AI output still matters.

---

## JSON array (one object per item)

```json
[
  {
    "title": "Claude 101",
    "url": "https://anthropic.skilljar.com/claude-101",
    "author": "Anthropic Academy",
    "roles": ["data-analyst", "data-scientist"],
    "level": "basic",
    "topics": ["chat-prompting", "cowork", "mcp"],
    "format": "course",
    "time": "under-1hr",
    "cost": "free-account",
    "language": "en",
    "tier": "previewed",
    "summary": "Official beginner course covering Claude's core features, file upload and analysis, and when to use connectors versus search or research for a task.",
    "who_for": "Anyone new to Claude who does data work in spreadsheets or docs. Assumes no coding.",
    "skip_if": "You already use Claude daily and know the analysis tool and Excel add-in.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Not data-analyst-specific; general workflows you adapt. Anthropic does not publish course length or price. Tools assumed: Claude.ai, optionally Excel and connectors."
  },
  {
    "title": "Introduction to Claude Cowork",
    "url": "https://anthropic.skilljar.com/introduction-to-claude-cowork",
    "author": "Anthropic Academy",
    "roles": ["data-analyst", "data-scientist"],
    "level": "basic",
    "topics": ["cowork", "skills", "agents"],
    "format": "hands-on",
    "time": "under-1hr",
    "cost": "free-account",
    "language": "en",
    "tier": "previewed",
    "summary": "Hands-on course on Claude Cowork's task loop, plugins, skills, and file/research workflows, with emphasis on steering multi-step work responsibly.",
    "who_for": "Analysts who want Claude to act on real local files. Assumes no coding.",
    "skip_if": "You only use the web chat and don't want the desktop Cowork app.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Cowork is the desktop file-automation app. Tools assumed: Cowork desktop, plugins, skills."
  },
  {
    "title": "Enabling and using the analysis tool",
    "url": "https://support.anthropic.com/en/articles/10008684-enabling-and-using-the-analysis-tool",
    "author": "Anthropic Help Center",
    "roles": ["data-analyst", "data-scientist"],
    "level": "basic",
    "topics": ["chat-prompting"],
    "format": "docs",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Canonical how-to for enabling and using the analysis tool, the JavaScript code sandbox in Claude.ai that runs code on CSV files for verifiable computation and visualization.",
    "who_for": "Every analyst using Claude.ai for CSV work. Assumes no coding, but explains the code sandbox.",
    "skip_if": "You need depth beyond enabling/using it.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Now canonically hosted at support.claude.com. Explains the context-window limit for uploaded CSVs. Tools assumed: Claude.ai, CSV."
  },
  {
    "title": "Use Claude for Excel",
    "url": "https://support.claude.com/en/articles/12650343-use-claude-for-excel",
    "author": "Anthropic Help Center",
    "roles": ["data-analyst"],
    "level": "basic",
    "topics": ["chat-prompting", "skills"],
    "format": "docs",
    "time": "under-15min",
    "cost": "subscription",
    "language": "en",
    "tier": "reviewed",
    "summary": "Current docs for the Claude for Excel add-in: cell-level citations, adjusting assumptions while preserving formulas, debugging errors, and building models inside Excel.",
    "who_for": "Excel-primary analysts on paid Claude plans. Assumes Excel familiarity, no coding.",
    "skip_if": "You don't use Excel.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Add-in is GA for Pro/Max/Team/Enterprise. Notably lists 'audit-critical calculations without verification' as a non-use. Tools assumed: Microsoft Excel."
  },
  {
    "title": "Reduce hallucinations",
    "url": "https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations",
    "author": "Anthropic Platform Docs",
    "roles": ["data-analyst", "data-scientist"],
    "level": "confident",
    "topics": ["chat-prompting", "safety", "api"],
    "format": "docs",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Anthropic's verification playbook: allow Claude to say 'I don't know', ground answers in direct quotes, use best-of-N and chain-of-thought verification, and restrict to provided data.",
    "who_for": "Any analyst worried about confidently-wrong output. Assumes no coding.",
    "skip_if": "You want data-specific step-by-step recipes rather than general guardrails.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "The most important item for the 'silently incorrect analysis' failure mode. Mirror exists at docs.claude.com."
  },
  {
    "title": "claude-cookbooks: data_analyst_agent notebook",
    "url": "https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/data_analyst_agent.ipynb",
    "author": "Anthropic",
    "roles": ["data-scientist", "data-analyst"],
    "level": "builder",
    "topics": ["api", "agents"],
    "format": "repo",
    "time": "half-day",
    "cost": "free-account",
    "language": "en",
    "tier": "previewed",
    "summary": "Working Jupyter notebook that sets up a reusable data-analysis agent: hand it a dataset, watch it run, and download a narrative HTML report plus generated files.",
    "who_for": "Notebook-native analysts/data scientists comfortable with Python and an API key.",
    "skip_if": "You don't code in Python or don't want to use the API.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Repo renamed from anthropic-cookbook. ~51.9k stars, actively maintained. Tools assumed: Python 3.11+, pandas, plotly, Anthropic API key."
  },
  {
    "title": "claude-cookbooks: Skills notebooks",
    "url": "https://github.com/anthropics/claude-cookbooks/tree/main/skills",
    "author": "Anthropic",
    "roles": ["data-scientist", "data-analyst"],
    "level": "builder",
    "topics": ["skills", "api"],
    "format": "repo",
    "time": "half-day",
    "cost": "free-account",
    "language": "en",
    "tier": "previewed",
    "summary": "Three notebooks teaching Claude Skills for document/data workflows (Excel, PowerPoint, PDF) using realistic sample financial datasets, plus building custom Skills from scratch.",
    "who_for": "Analysts building reusable, repeatable analysis workflows. Assumes Python.",
    "skip_if": "You are not building Skills.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Includes financial_statements.csv, portfolio_holdings.json, budget_template.csv. Tools assumed: Python, Jupyter, Anthropic API key."
  },
  {
    "title": "Anthropic's Prompt Engineering Interactive Tutorial",
    "url": "https://github.com/anthropics/prompt-eng-interactive-tutorial",
    "author": "Anthropic",
    "roles": ["data-analyst", "data-scientist"],
    "level": "basic",
    "topics": ["chat-prompting", "api"],
    "format": "repo",
    "time": "half-day",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "Nine-chapter interactive prompting course with exercises, including separating data from instructions and prompting Claude to write SQL.",
    "who_for": "Anyone who wants disciplined prompting fundamentals. Light coding (Jupyter) helps but a Google Sheets version exists.",
    "skip_if": "You need current-model behavior specifics.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Examples use Claude 3 Haiku (historical); principles still valid. Also available via anthropics/courses repo and a Google Sheets version."
  },
  {
    "title": "Introducing the analysis tool in Claude.ai",
    "url": "https://anthropic.com/news/analysis-tool",
    "author": "Anthropic",
    "roles": ["data-analyst", "data-scientist"],
    "level": "basic",
    "topics": ["chat-prompting"],
    "format": "article",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Launch blog explaining the analysis tool as a built-in code sandbox that produces mathematically precise and reproducible answers from CSV data.",
    "who_for": "Analysts who want to understand why code execution beats text-only reasoning for numbers.",
    "skip_if": "You want current UI steps rather than background.",
    "published": "2024-10-24",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "References Claude 3.5 Sonnet and predates Excel/Cowork; dated framing but conceptually sound."
  },
  {
    "title": "Introduction to Claude Analysis",
    "url": "https://www.codecademy.com/learn/ext-courses/introduction-to-claude-analysis",
    "author": "Codecademy",
    "roles": ["data-analyst"],
    "level": "basic",
    "topics": ["chat-prompting"],
    "format": "course",
    "time": "under-1hr",
    "cost": "free-account",
    "language": "en",
    "tier": "previewed",
    "summary": "Beginner course on Claude's analysis tool: natural-language queries, preparing/uploading CSVs, repairing common data issues, basic statistics, and React Artifact visualizations.",
    "who_for": "Excel-to-analysis beginners. Assumes no coding.",
    "skip_if": "You're already notebook-native.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Third-party but structured and hands-on. Tools assumed: Claude.ai, CSV."
  },
  {
    "title": "15 Claude Tips for Everyday Data Analysis",
    "url": "https://www.linkedin.com/learning/15-claude-tips-for-everyday-data-analysis",
    "author": "Emma Chieppor (LinkedIn Learning)",
    "roles": ["data-analyst"],
    "level": "basic",
    "topics": ["chat-prompting"],
    "format": "video",
    "time": "under-1hr",
    "cost": "subscription",
    "language": "en",
    "tier": "previewed",
    "summary": "Bite-size video course pairing Claude with a spreadsheet: high-impact prompts, generating formulas, formatting data, troubleshooting errors, and auditing data.",
    "who_for": "Excel-primary analysts who prefer short video lessons. Assumes no coding.",
    "skip_if": "You have no LinkedIn Learning access.",
    "published": "2026-04-14",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "21 minutes, ~11.7k viewers (popularity is a tiebreaker only). Covers pitfalls and data auditing. Tools assumed: spreadsheets."
  },
  {
    "title": "Create Claude Skills for Data Tasks",
    "url": "https://www.datacamp.com/code-along/create-claude-skills-for-data-tasks",
    "author": "Tom Farnschläder (DataCamp)",
    "roles": ["data-scientist", "data-analyst"],
    "level": "confident",
    "topics": ["skills"],
    "format": "hands-on",
    "time": "under-1hr",
    "cost": "free-account",
    "language": "en",
    "tier": "previewed",
    "summary": "Code-along building Claude Skills for exploratory data analysis and feature engineering, applied to a real soccer dataset to generate insights and analysis-ready features.",
    "who_for": "Analysts and data scientists wanting reusable AI workflows. Assumes basic Python.",
    "skip_if": "You don't want to work inside DataCamp's built-in environment.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "DataCamp content is quality but promotes its own platform. Tools assumed: Python, pandas."
  },
  {
    "title": "Introduction to Claude (code-along)",
    "url": "https://www.datacamp.com/code-along/introduction-to-claude",
    "author": "Aimée Gott (DataCamp)",
    "roles": ["data-analyst", "data-scientist"],
    "level": "basic",
    "topics": ["chat-prompting", "api"],
    "format": "hands-on",
    "time": "under-1hr",
    "cost": "free-account",
    "language": "en",
    "tier": "previewed",
    "summary": "Code-along walking through a data-analysis workflow with Claude, including prompt-engineering tips and generating Python and SQL code.",
    "who_for": "Beginners wanting a guided data-analysis and code-generation demo. Light coding.",
    "skip_if": "You're past introductory material.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Uses DataLab/DataCamp environment. Tools assumed: Python, SQL."
  },
  {
    "title": "Sales Analysis with Claude: Data Driven Sales Analytics",
    "url": "https://www.coursera.org/projects/sales-analysis-with-claude-data-driven-sales-analytics",
    "author": "Hussein ElGhoul (Coursera)",
    "roles": ["data-analyst"],
    "level": "basic",
    "topics": ["chat-prompting"],
    "format": "hands-on",
    "time": "under-1hr",
    "cost": "subscription",
    "language": "en",
    "tier": "listed",
    "summary": "Guided 1.5-hour project analyzing sales data with Claude: trend identification, pattern recognition, visualizations, and strategic recommendations.",
    "who_for": "Business analysts comfortable with spreadsheets and business metrics. No coding.",
    "skip_if": "You want depth; it's shallow and requires a Claude Pro subscription.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Requires Claude.ai Pro. Included with Coursera Plus. Does not visibly emphasize verification."
  },
  {
    "title": "Claude Code for Data Analysis",
    "url": "https://vincent.codes.finance/posts/claude-code-data-analysis/",
    "author": "Vincent Grégoire (Vincent Codes Finance)",
    "roles": ["data-scientist", "data-analyst"],
    "level": "confident",
    "topics": ["claude-code", "mcp", "api"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Working analyst's guide to Claude Code for data analysis: setup, having Claude infer and write the data schema to a Markdown file, MCP connectors like context7, and reproducibility.",
    "who_for": "Analysts/researchers comfortable in a terminal who want reproducible pipelines. Assumes Python.",
    "skip_if": "You never touch a terminal.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Finance-focused academic author; strong on reproducibility and grounding. Tools assumed: Claude Code, Python, MCP."
  },
  {
    "title": "Claude Code is secretly an excellent data analysis tool",
    "url": "https://yang3kc.substack.com/p/claude-code-is-secretly-an-excellent",
    "author": "Kai-Cheng Yang",
    "roles": ["data-scientist"],
    "level": "confident",
    "topics": ["claude-code"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "A researcher's candid account of using Claude Code for the data analysis behind a paper (an estimated 98% of code generated), with concrete setups and honest limitations.",
    "who_for": "Data scientists/researchers who write Python and want a real-world workflow. Assumes coding.",
    "skip_if": "You want beginner or Excel-first material.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Mentions the tools used (Claude Code, Lazygit, Cursor, Jupyter). Honest about caveats. Tools assumed: Claude Code, Python, git."
  },
  {
    "title": "3 Claude Skills Every Data Scientist Needs in 2026",
    "url": "https://towardsdatascience.com/3-claude-skills-every-data-scientist-needs-in-2026/",
    "author": "Towards Data Science",
    "roles": ["data-scientist", "data-analyst"],
    "level": "confident",
    "topics": ["skills", "claude-code"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "Practical walkthrough of three Claude Skills for data scientists, including dashboard/EDA generation with real insights drawn from an energy-consumption dataset.",
    "who_for": "Data scientists exploring Skills for EDA and dashboards. Assumes Python familiarity.",
    "skip_if": "You are not using Skills.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "TDS is a reputable practitioner outlet. Tools assumed: Claude Code/Skills, Python."
  },
  {
    "title": "4 Lines You Should Include in Your Claude Skill",
    "url": "https://towardsdatascience.com/4-lines-you-must-include-in-your-claude-skill/",
    "author": "Towards Data Science",
    "roles": ["data-analyst", "data-scientist"],
    "level": "confident",
    "topics": ["skills", "safety"],
    "format": "article",
    "time": "under-15min",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Argues for anchoring Claude's language to real thresholds (e.g. defining what counts as a 'significant' change) so polished output doesn't mask overconfident, unverified claims.",
    "who_for": "Anyone writing Skills or reports for stakeholders. Assumes no coding.",
    "skip_if": "You don't write Skills or reports.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Best explicit take found on preventing confidently-wrong narrative output."
  },
  {
    "title": "Data Analysis with Claude Code — it's not just for programmers",
    "url": "https://medium.com/data-science-collective/data-analysis-with-claude-code-its-not-just-for-programmers-08adb529a70d",
    "author": "Alan Jones",
    "roles": ["data-analyst"],
    "level": "basic",
    "topics": ["claude-code"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "Non-coder's end-to-end walkthrough using Claude Code to analyze 78 years of London weather data, producing charts and a written report without writing code.",
    "who_for": "Analysts curious about Claude Code but wary of the terminal. No coding required.",
    "skip_if": "You want deep technical detail or verification depth.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Medium member-only for some; approachable framing. Tools assumed: Claude Code."
  },
  {
    "title": "Claude Code for Data Analysis: Excel-Free Answers From CSVs",
    "url": "https://ccforeveryone.com/guides/claude-code-for-data-analysts",
    "author": "CC for Everyone",
    "roles": ["data-analyst"],
    "level": "confident",
    "topics": ["claude-code", "safety"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "reviewed",
    "summary": "Guide to using Claude Code for CSV chores (dedupe, join, pivot, A/B significance) with strong verification advice: run a smell test, spot-check rows, and prefer rerunnable scripts over silent cell edits.",
    "who_for": "Analysts who want plain-English data workflows plus a verification discipline.",
    "skip_if": "You prefer official documentation only.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Cites Raymond Panko's spreadsheet-error research ('94% of spreadsheets have errors') to justify human checking. Notes Claude for Excel GA on May 7, 2026. Tools assumed: Claude Code, CSV."
  },
  {
    "title": "How to Use Claude for CSV Data Analysis (The Honest Guide)",
    "url": "https://www.qwe.edu.pl/tutorial/claude-csv-data-analysis/",
    "author": "QWE AI Academy",
    "roles": ["data-analyst"],
    "level": "confident",
    "topics": ["chat-prompting"],
    "format": "article",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "previewed",
    "summary": "Explains that Claude has two ways of handling a CSV — text-reasoning (which can hallucinate sums) versus the code-executing analysis tool — and how to force the reliable one, plus the 30MB/context limits.",
    "who_for": "Analysts who need to understand why the same prompt can return two different totals.",
    "skip_if": "You want a named, established author or institution.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Lesser-known source but technically accurate on the two-modes trap — the core correctness risk. Tools assumed: Claude.ai, CSV."
  },
  {
    "title": "Postgres MCP Pro (crystaldba/postgres-mcp)",
    "url": "https://github.com/crystaldba/postgres-mcp",
    "author": "Crystal DBA",
    "roles": ["data-analyst", "data-scientist"],
    "level": "builder",
    "topics": ["mcp"],
    "format": "repo",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "listed",
    "summary": "The recommended PostgreSQL MCP server: configurable read/write access, EXPLAIN-plan analysis, index tuning, and health checks, letting Claude query a database in natural language.",
    "who_for": "Analysts connecting Claude to Postgres. Assumes DB credentials and comfort editing MCP config.",
    "skip_if": "You don't use PostgreSQL.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Active, ~3.2k stars, 80 commits, no releases listed. Use read-only/least-privilege role. Replaces the archived, vulnerable @modelcontextprotocol/server-postgres."
  },
  {
    "title": "MotherDuck / DuckDB MCP Server",
    "url": "https://github.com/motherduckdb/mcp-server-motherduck",
    "author": "MotherDuck",
    "roles": ["data-analyst", "data-scientist"],
    "level": "builder",
    "topics": ["mcp"],
    "format": "repo",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "listed",
    "summary": "MCP server for local DuckDB and MotherDuck cloud, letting Claude explore schemas and run analytical SQL in natural language; read-only by default in current versions.",
    "who_for": "Analysts/data scientists using DuckDB or a MotherDuck warehouse. Assumes SQL and MCP setup.",
    "skip_if": "You don't use DuckDB or a warehouse.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Active, ~488 stars, latest release v1.0.7 (Jun 9, 2026). A fully-managed remote endpoint (api.motherduck.com/mcp) also exists. Tools assumed: DuckDB/MotherDuck, SQL."
  },
  {
    "title": "Tableau MCP (official)",
    "url": "https://github.com/tableau/tableau-mcp",
    "author": "Tableau (Salesforce)",
    "roles": ["data-analyst"],
    "level": "builder",
    "topics": ["mcp"],
    "format": "repo",
    "time": "under-1hr",
    "cost": "free",
    "language": "en",
    "tier": "listed",
    "summary": "Tableau's official MCP server: query datasources, search workbooks, and pull Pulse metrics from Claude in plain English, with OAuth and per-user permissions.",
    "who_for": "BI analysts on Tableau Cloud/Server. Assumes a Tableau account and PAT/OAuth setup.",
    "skip_if": "You don't use Tableau.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Active, Tableau-supported, ~302 stars, latest release v2.21.1 (Jul 2, 2026). Hosted endpoint at mcp.tableau.com for Cloud. Added as a custom connector, not one-click. Tools assumed: Tableau."
  },
  {
    "title": "ClaudeR (R + RStudio MCP)",
    "url": "https://github.com/IMNMV/ClaudeR",
    "author": "IMNMV",
    "roles": ["data-scientist", "data-analyst"],
    "level": "builder",
    "topics": ["mcp", "claude-code"],
    "format": "repo",
    "time": "half-day",
    "cost": "free",
    "language": "en",
    "tier": "listed",
    "summary": "Connects RStudio to Claude (and other agents) via MCP, with a built-in reproducible statistical-analysis protocol and a 'Reviewer Zero' mode that audits statistical claims against your R code.",
    "who_for": "R users and quantitative researchers wanting reproducible, auditable analysis. Assumes R/RStudio.",
    "skip_if": "You don't use R.",
    "published": "UNVERIFIED",
    "checked": "2026-08-19",
    "status": "live",
    "notes": "Active, ~255 stars, latest release v0.3.1 (Mar 24, 2026); PyPI package clauder-mcp. Rare R-first, verification-focused resource. Tools assumed: R, RStudio, MCP."
  }
]
```

---

### Three things that were surprising during the research
1. **Anthropic's own reference Postgres MCP server is both archived and dangerously insecure — yet still one of the most-installed.** Datadog found a read-only-bypass SQL injection; Anthropic archived it May 29, 2025 and deprecated it July 10, 2025, but the unpatched v0.6.2 still pulls roughly 312,000 npm installs a month. The "official" option is the wrong option here, which is genuinely counterintuitive.
2. **There is still no authoritative, vendor-neutral course specifically on verifying Claude's analytical output**, even though "confidently wrong analysis" is the field's single biggest risk. The best guidance is scattered across a Towards Data Science post about the word "significant," a small blog's "honest guide" to the two CSV modes, and Anthropic's general hallucination docs — not a dedicated data-analyst curriculum.
3. **The Claude data ecosystem changed faster than the tutorials.** Between Oct 2024 and Aug 2026 the analysis tool, Claude for Excel (GA May 7, 2026; Pro access Jan 24, 2026), Cowork, Skills, Claude Science, and the whole MCP layer all arrived — so a large share of "Claude for data analysis" content is already describing a stale interface, and Snyk's ToxicSkills audit found prompt injection in 36% of community Skills, meaning the fastest-growing resource type (Skills/MCP) is also the least safe to trust blindly.