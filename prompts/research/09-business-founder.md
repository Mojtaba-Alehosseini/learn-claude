# Research task: the best Claude learning content for founders, business owners, and operations

You have been given this file as your task. Read it, do the research, save the results as files, and show them to me.

## Setup

- Check today's date first. Use it as the `checked` date on every item.
- Use web search heavily. **Never answer from memory** — content about AI tools goes stale within months, so anything you "remember" is probably wrong or outdated.
- This is a long job. Work through it properly rather than quickly. If you can run several searches in parallel, do it.
- Make a task list so I can follow your progress.

## Who this is for

**Founders, small business owners, and operations people** — including consultants and admin staff — who want to learn **Claude** (Anthropic's AI assistant) for running a business.

Focus on: automating repetitive admin, handling email and documents, customer support workflows, financial and sales analysis, market and competitor research, hiring and onboarding material, writing proposals and contracts, connecting Claude to business tools (CRM, accounting, project management) through MCP, and knowing which tasks to automate and which to leave alone.

Also cover the practical basics: which Claude plan makes sense for a small team, what data should not be put into an AI tool, and what the real cost is.

## Where to look

Search these specifically. Do not stop at the first page of results.

- Anthropic's free courses at claude.com/resources/courses and anthropic.skilljar.com — there is an "AI Fluency for Small Businesses" course and a nonprofits variant, find both
- Anthropic Help Center at support.claude.com — plans, privacy, team features
- Cowork content — this is the most relevant Claude surface for this audience
- MCP servers for business tools — github.com/modelcontextprotocol and community lists
- Coursera, Udemy, LinkedIn Learning, Skillshare — small-business AI courses
- Business and automation YouTube channels
- Chambers of commerce, small-business associations, and government business-support programmes that publish AI guidance
- Reddit r/smallbusiness, r/Entrepreneur, r/ClaudeAI

## What counts as "best" — in this priority order

1. **Is it still accurate?** Claude's interface, plans, and features change every few months. This is the single most important test.
2. **Does it teach doing, not just watching?** Prefer concrete workflows someone could set up the same afternoon.
3. **Is the source trustworthy?** Official Anthropic material, real operators, established business educators. Downrank SEO spam and affiliate content.
4. **Is it honest about money?** Uprank content that gives real costs and real limits. Downrank anything promising large passive income.

Popularity — views, ratings, subscriber counts — is a **tiebreaker only**, never a ranking signal.

## A specific warning — read this carefully

**This is the worst category for scam and hype content.** A documented, common complaint: videos that spend the first ten minutes on a story about an "AI agency making $40,000 a month" before teaching anything.

Apply a hard filter. Put an item in the **Avoid** list, not the main list, if it:

- Promises a specific income figure
- Sells an "AI agency" or "AI automation business" opportunity
- Is mainly a funnel to a paid community, coaching programme, or Skool group
- Uses urgency or scarcity language ("before it's too late", "while this still works")
- Has a thumbnail with money, a rented car, or a shocked face

If an item is genuinely useful but has a hype-heavy opening, keep it in the main list and say exactly that in `skip_if` — for example, "skip the first 8 minutes, the useful part starts after".

Also: much content in this space is affiliate marketing for a tool other than Claude. Note it in `notes` when you see it.

## Hard rules

- Every item needs a URL you actually opened or saw in search results. **Never invent an item, a link, a price, or a length.**
- If you cannot verify a detail, write `UNVERIFIED` for that field. Do not guess.
- If you cannot find a live link at all, leave the item out entirely.
- Do not copy the description from the source page. Write your own honest sentence, including what is weak about it.
- Prefer the original source URL, never an aggregator's link.
- Flag anything published more than about 12 months ago as possibly outdated.
- Aim for 15–30 items in the main list. A short honest list is far better than a long one padded with hype.

## What to save

Save two files in the working folder. Replace `YYYY-MM-DD` with today's date.

### 1. `claude-research-business-founder-YYYY-MM-DD.md`

A readable report containing:

- A table with columns: Title | URL | Author/Source | Format | Level | Time | Cost | Tier | Business use | Why it's good | Skip if
- **Dead or moved links** you found while searching
- **Looks outdated** — items that appear stale, and why
- **Avoid — scam and hype list.** This section matters as much as the main list. Include the URL and one line on why, for every item that failed the filter above, so they can be blocklisted.
- **Gaps** — what small businesses clearly need but nobody has made

### 2. `claude-research-business-founder-YYYY-MM-DD.json`

A JSON array, one object per item, using **exactly** these field names:

```json
{
  "title": "",
  "url": "",
  "author": "",
  "roles": ["business-founder"],
  "level": "",
  "topics": [],
  "format": "",
  "time": "",
  "cost": "",
  "language": "en",
  "tier": "",
  "summary": "What it teaches, in plain language. One or two sentences.",
  "who_for": "Who specifically should use this.",
  "skip_if": "When someone should NOT bother. If there is a hype intro, say where the useful part starts.",
  "published": "YYYY-MM-DD or UNVERIFIED",
  "checked": "today's date",
  "status": "live",
  "notes": "Affiliate links, upsells, funnels — say so plainly. Plus anything odd."
}
```

## Allowed values — use these exactly, nothing else

| Field | Allowed values |
|---|---|
| `level` | `never-used`, `basic`, `confident`, `builder` |
| `topics` | `chat-prompting`, `cowork`, `skills`, `mcp`, `agents`, `safety` |
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
