# Research task: the best Claude learning content for product managers

You have been given this file as your task. Read it, do the research, save the results as files, and show them to me.

## Setup

- Check today's date first. Use it as the `checked` date on every item.
- Use web search heavily. **Never answer from memory** — content about AI tools goes stale within months, so anything you "remember" is probably wrong or outdated.
- This is a long job. Work through it properly rather than quickly. If you can run several searches in parallel, do it.
- Make a task list so I can follow your progress.

## Who this is for

**Product managers** — including product owners and programme managers — who want to learn **Claude** (Anthropic's AI assistant).

Cover two needs, and label which one each item serves:

1. **PM craft** — writing specs and PRDs, synthesising user research and feedback, competitive analysis, roadmapping, writing release notes, preparing stakeholder updates, analysing product data.
2. **PM who builds** — using Claude Code or Cowork to make working prototypes without an engineer, and knowing where that stops being a good idea.

## Where to look

Search these specifically. Do not stop at the first page of results.

- Anthropic's free courses at claude.com/resources/courses and anthropic.skilljar.com — including Cowork content
- Anthropic Help Center at support.claude.com
- Maven — there are live cohort courses aimed specifically at PMs
- Coursera, Udemy, LinkedIn Learning, Reforge — PM-focused AI courses
- Product management newsletters and blogs — Lenny's Newsletter, Every, and similar
- YouTube channels covering AI for product work
- Reddit r/ProductManagement and r/ClaudeAI — search for posts by PMs about what actually worked

## What counts as "best" — in this priority order

1. **Is it still accurate?** Claude's interface and features change every few months. This is the single most important test.
2. **Does it teach doing, not just watching?** Prefer real templates, worked examples, and copyable prompts over "AI will change product management" essays.
3. **Is the source trustworthy?** Official Anthropic material, practising PMs, established product educators. Downrank SEO spam and thought-leadership with no substance.
4. **Is it honest about limits?** Uprank anything clear about where AI-generated specs and prototypes break down. Downrank anything promising PMs can replace their engineering team.

Popularity — views, ratings, subscriber counts — is a **tiebreaker only**, never a ranking signal.

## A specific warning

This space is full of high-engagement, low-substance content — LinkedIn-style posts and expensive cohort courses that mostly restate what everyone already knows. Judge by whether someone could actually do something new after consuming it.

Cohort courses are also time-bound and expensive. If you list one, record the price and the next start date in `notes`, and mark `cost` accurately.

## Hard rules

- Every item needs a URL you actually opened or saw in search results. **Never invent an item, a link, a price, or a length.**
- If you cannot verify a detail, write `UNVERIFIED` for that field. Do not guess.
- If you cannot find a live link at all, leave the item out entirely.
- Do not copy the description from the source page. Write your own honest sentence, including what is weak about it.
- Prefer the original source URL, never an aggregator's link.
- Flag anything published more than about 12 months ago as possibly outdated.
- Aim for 15–30 items. Quality over quantity.

## What to save

Save two files in the working folder. Replace `YYYY-MM-DD` with today's date.

### 1. `claude-research-pm-YYYY-MM-DD.md`

A readable report containing:

- A table with columns: Title | URL | Author/Source | Format | Level | Time | Cost | Tier | PM craft or PM builds | Why it's good | Skip if
- **Dead or moved links** you found while searching
- **Looks outdated** — items that appear stale, and why
- **Avoid** — thought-leadership with no teaching value, SEO spam, overpriced courses, with URLs
- **Cohort courses** — prices and next start dates, since these change often
- **Gaps** — what PMs clearly need but nobody has made

### 2. `claude-research-pm-YYYY-MM-DD.json`

A JSON array, one object per item, using **exactly** these field names:

```json
{
  "title": "",
  "url": "",
  "author": "",
  "roles": ["pm"],
  "level": "",
  "topics": [],
  "format": "",
  "time": "",
  "cost": "",
  "language": "en",
  "tier": "",
  "summary": "What it teaches, in plain language. One or two sentences.",
  "who_for": "Who specifically should use this.",
  "skip_if": "When someone should NOT bother with this. Be honest.",
  "published": "YYYY-MM-DD or UNVERIFIED",
  "checked": "today's date",
  "status": "live",
  "notes": "For cohort courses: price and next start date. Otherwise anything odd."
}
```

## Allowed values — use these exactly, nothing else

| Field | Allowed values |
|---|---|
| `level` | `never-used`, `basic`, `confident`, `builder` |
| `topics` | `chat-prompting`, `claude-code`, `cowork`, `skills`, `mcp`, `agents`, `safety` |
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
