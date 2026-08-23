# Research task: the best Claude learning content for data analysts and data scientists

You have been given this file as your task. Read it, do the research, save the results as files, and show them to me.

## Setup

- Check today's date first. Use it as the `checked` date on every item.
- Use web search heavily. **Never answer from memory** — content about AI tools goes stale within months, so anything you "remember" is probably wrong or outdated.
- This is a long job. Work through it properly rather than quickly. If you can run several searches in parallel, do it.
- Make a task list so I can follow your progress.

## Who this is for

**Data analysts and data scientists** who want to learn **Claude** (Anthropic's AI assistant) for data work.

Focus on: exploring and cleaning datasets, writing and debugging SQL, working with spreadsheets and CSV files, building charts and visualisations, statistical analysis, writing Python or R with Claude, connecting Claude to databases and BI tools via MCP, automating recurring reports, and explaining results to non-technical stakeholders.

This audience ranges widely — from someone whose main tool is Excel to someone who lives in a notebook. Mark the level of each item honestly so both ends are served.

## Where to look

Search these specifically. Do not stop at the first page of results.

- Anthropic's free courses at claude.com/resources/courses and anthropic.skilljar.com
- Anthropic Help Center at support.claude.com — file and spreadsheet handling
- Claude Platform docs at platform.claude.com/docs
- Anthropic's cookbook repositories at github.com/anthropics
- MCP servers for databases and data tools — github.com/modelcontextprotocol and community MCP lists
- DataCamp, Coursera, edX, Udemy, Pluralsight, LinkedIn Learning — but note that DataCamp's own "best resources" content only links to DataCamp
- YouTube channels covering AI for data analysis
- Analyst and data-science blogs
- Reddit r/dataanalysis, r/datascience, r/ClaudeAI

## What counts as "best" — in this priority order

1. **Is it still accurate?** Claude's interface and file-handling features change every few months. This is the single most important test.
2. **Does it teach doing, not just watching?** Prefer content with real datasets, working queries, and reproducible steps.
3. **Is the source trustworthy?** Official Anthropic material, working analysts, established data educators. Downrank SEO spam and vendor marketing.
4. **Is it honest about correctness?** Uprank anything that teaches how to verify AI output against the data. Downrank anything that treats AI-generated analysis as automatically correct.

Popularity — views, ratings, subscriber counts — is a **tiebreaker only**, never a ranking signal.

## A specific warning

The dangerous failure mode here is confidently wrong analysis: a query that runs, returns numbers, and is silently incorrect. Any resource that teaches AI-assisted analysis **without** covering verification is risky. Note this in `skip_if` or `notes`.

Also watch for content that is really a product demo for a BI or "AI analytics" tool. List it only if it teaches something transferable, and say so in `notes`.

## Hard rules

- Every item needs a URL you actually opened or saw in search results. **Never invent an item, a link, a rating, or a length.**
- If you cannot verify a detail, write `UNVERIFIED` for that field. Do not guess.
- If you cannot find a live link at all, leave the item out entirely.
- Do not copy the description from the source page. Write your own honest sentence, including what is weak about it.
- Prefer the original source URL, never an aggregator's link.
- Flag anything published more than about 12 months ago as possibly outdated.
- Aim for 15–30 items. Quality over quantity.

## What to save

Save two files in the working folder. Replace `YYYY-MM-DD` with today's date.

### 1. `claude-research-data-analyst-YYYY-MM-DD.md`

A readable report containing:

- A table with columns: Title | URL | Author/Source | Format | Level | Time | Cost | Tier | Tools covered | Why it's good | Skip if
- **Dead or moved links** you found while searching
- **Looks outdated** — items that appear stale, and why
- **Avoid** — SEO spam and vendor demos dressed as training, with URLs
- **MCP servers worth knowing** — database and data-tool connectors, with repo URLs and last-push dates
- **Gaps** — what analysts clearly need but nobody has made

### 2. `claude-research-data-analyst-YYYY-MM-DD.json`

A JSON array, one object per item, using **exactly** these field names:

```json
{
  "title": "",
  "url": "",
  "author": "",
  "roles": ["data-analyst"],
  "level": "",
  "topics": [],
  "format": "",
  "time": "",
  "cost": "",
  "language": "en",
  "tier": "",
  "summary": "What it teaches, in plain language. One or two sentences.",
  "who_for": "Who specifically should use this. Say whether it assumes coding.",
  "skip_if": "When someone should NOT bother with this. Be honest.",
  "published": "YYYY-MM-DD or UNVERIFIED",
  "checked": "today's date",
  "status": "live",
  "notes": "Tools assumed (Excel, SQL, Python, R, specific BI tools), plus anything odd."
}
```

## Allowed values — use these exactly, nothing else

| Field | Allowed values |
|---|---|
| `level` | `never-used`, `basic`, `confident`, `builder` |
| `topics` | `chat-prompting`, `claude-code`, `cowork`, `skills`, `mcp`, `agents`, `api`, `safety` |
| `format` | `video`, `course`, `docs`, `article`, `hands-on`, `podcast`, `repo` |
| `time` | `under-15min`, `under-1hr`, `half-day`, `multi-day` |
| `cost` | `free`, `free-account`, `paid-once`, `subscription` |
| `tier` | `ai-reviewed`, `previewed`, `listed` |

**Tier means:**

- `ai-reviewed` — you read the whole thing yourself. **Allowed only for `docs` and
  `article`** — short text pages you can fetch and read in full. Never for `video`,
  `course`, `podcast`, `hands-on` or `repo`.
- `previewed` — you read the syllabus, curriculum outline, or free sample only
- `listed` — you found metadata only and could not check the content

**Never use `reviewed`.** That tier means a person confirmed the judgment. You are not a
person. It is rejected on ingest.

## Finally

Show me both files when you are done, and tell me in two or three sentences what surprised you.
