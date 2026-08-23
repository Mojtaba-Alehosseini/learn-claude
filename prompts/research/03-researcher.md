# Research task: the best Claude learning content for researchers and academics

You have been given this file as your task. Read it, do the research, save the results as files, and show them to me.

## Setup

- Check today's date first. Use it as the `checked` date on every item.
- Use web search heavily. **Never answer from memory** — content about AI tools goes stale within months, so anything you "remember" is probably wrong or outdated.
- This is a long job. Work through it properly rather than quickly. If you can run several searches in parallel, do it.
- Make a task list so I can follow your progress.

## Who this is for

**Researchers and academics** — PhD students, postdocs, professors, industry researchers — who want to learn **Claude** (Anthropic's AI assistant) for research work.

Focus on: literature review and reading papers at scale, summarizing and comparing studies, writing and editing manuscripts, responding to peer review, analysing data, working with reference managers like Zotero, preparing figures, grant writing, and reproducibility.

This audience is **technical but usually not software engineers**. A biologist or an economist may write R or Python but will not be comfortable with a terminal-heavy workflow. Include some builder-level content, but mark its level honestly.

Also cover research-integrity guidance and journal policies on AI use in manuscripts. Publishers have real, enforced rules here.

## Where to look

Search these specifically. Do not stop at the first page of results.

- Anthropic's free courses at claude.com/resources/courses and anthropic.skilljar.com
- Anthropic's Help Center (support.claude.com) and Claude Platform docs (platform.claude.com/docs)
- Anthropic's Campus program at claude.com/programs/campus
- University research-support and library guides on AI for research — many are excellent and nobody indexes them
- Journal and publisher policies on AI use — Nature, Elsevier, Springer, IEEE, ICMJE
- Content about connecting Claude to research tools: Zotero, arXiv, PubMed, MCP servers for academic databases
- YouTube channels covering AI for academic work
- Coursera, edX — research-methods courses that cover AI tools
- Reddit r/ClaudeAI, r/PhD, r/AskAcademia — what researchers actually ask

## What counts as "best" — in this priority order

1. **Is it still accurate?** Claude's interface and features change every few months. This is the single most important test.
2. **Does it teach doing, not just watching?** Prefer real workflows and worked examples over overviews.
3. **Is the source trustworthy?** Official Anthropic material, universities, publishers, working researchers. Downrank SEO spam.
4. **Is it honest about limits?** Uprank anything that is clear about hallucinated citations, fabricated references, and where AI should not be trusted. This audience is burned by this specific failure.

Popularity — views, ratings, subscriber counts — is a **tiebreaker only**, never a ranking signal.

## A specific warning

Fabricated citations are the number one real harm for this audience. Any resource that teaches literature review with AI **without** warning about invented references is dangerous. Note this explicitly in `skip_if` or `notes`.

Also flag anything that encourages undisclosed AI use in manuscripts — most publishers now require disclosure.

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

### 1. `claude-research-researcher-YYYY-MM-DD.md`

A readable report containing:

- A table with columns: Title | URL | Author/Source | Format | Level | Time | Cost | Tier | Why it's good | Skip if
- **Dead or moved links** you found while searching
- **Looks outdated** — items that appear stale, and why
- **Avoid** — SEO spam, scams, or anything teaching undisclosed AI use, with URLs
- **Publisher policies** — journal and publisher AI policies with URLs and dates
- **Gaps** — what researchers clearly need but nobody has made

### 2. `claude-research-researcher-YYYY-MM-DD.json`

A JSON array, one object per item, using **exactly** these field names:

```json
{
  "title": "",
  "url": "",
  "author": "",
  "roles": ["researcher"],
  "level": "",
  "topics": [],
  "format": "",
  "time": "",
  "cost": "",
  "language": "en",
  "tier": "",
  "field": "optional — only if genuinely domain-specific, e.g. medicine, law, chemistry",
  "summary": "What it teaches, in plain language. One or two sentences.",
  "who_for": "Who specifically should use this.",
  "skip_if": "When someone should NOT bother with this. Be honest.",
  "published": "YYYY-MM-DD or UNVERIFIED",
  "checked": "today's date",
  "status": "live",
  "notes": "Anything odd — outdated screens, citation risks, paywall."
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
