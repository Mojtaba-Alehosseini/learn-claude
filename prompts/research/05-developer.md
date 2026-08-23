# Research task: the best Claude learning content for software developers

You have been given this file as your task. Read it, do the research, save the results as files, and show them to me.

## Setup

- Check today's date first. Use it as the `checked` date on every item.
- Use web search heavily. **Never answer from memory** — content about AI tools goes stale within months, so anything you "remember" is probably wrong or outdated.
- This is a long job. Work through it properly rather than quickly. If you can run several searches in parallel, do it.
- Make a task list so I can follow your progress.

## Who this is for

**Software developers and engineers** who want to learn **Claude** (Anthropic's AI assistant) for building and coding.

Focus on: Claude Code, the Claude API and SDKs, agent skills, subagents, the Model Context Protocol (MCP), building agents, CLAUDE.md and project configuration, testing and debugging with AI, hooks and automation, and running Claude on cloud platforms (Bedrock, Vertex AI).

Include both "getting started" and genuinely advanced material. This audience complains that most content stops at the beginner level.

## Where to look

Search these specifically. Do not stop at the first page of results.

- Anthropic's free courses at claude.com/resources/courses and anthropic.skilljar.com
- The three official documentation sites — they are separate, do not confuse them:
  - platform.claude.com/docs — API and SDK
  - code.claude.com/docs — Claude Code, including its best-practices page
  - support.claude.com — end users
- Anthropic's engineering blog at anthropic.com/engineering
- Anthropic's GitHub organisation (github.com/anthropics) and github.com/modelcontextprotocol
- DeepLearning.AI — several free Anthropic-built courses
- Frontend Masters, Pluralsight, Coursera, Udemy, freeCodeCamp, Maven
- ClaudeLog (claudelog.com) — strong independent Claude Code documentation
- simonwillison.net and steipete.me
- GitHub "awesome" lists for Claude Code, skills, and MCP servers
- YouTube channels that cover agentic engineering seriously
- Hacker News and Reddit r/ClaudeAI

## What counts as "best" — in this priority order

1. **Is it still accurate?** Claude Code changes fast. A tutorial from a year ago may use flags, commands, or file layouts that no longer exist. This is the single most important test — check the publish date against the current docs.
2. **Does it teach doing, not just watching?** Prefer working repos, real projects, and copyable configuration over talking-head overviews.
3. **Is the source trustworthy?** Official Anthropic material, Anthropic engineers, known practitioners. Downrank benchmark-chasing channels and SEO content farms.
4. **Does it go deep enough?** Uprank anything that gets past "here's how to install it".

Popularity — stars, views, ratings — is a **tiebreaker only**, never a ranking signal.

## Specific warnings

- **Verify GitHub repositories properly.** Check the star count *and* the last-push date. A repo with 20,000 stars and no commits for a year is a trap, and it will still rank first in search. Put the last-push date in `notes`.
- **Beware name collisions.** Several different repos share names like "awesome-claude-code". Check which one is actually maintained.
- **Beware abandoned lists.** Some highly-starred AI resource lists have not been touched in over a year and are not marked as archived.
- **Beware "vibe coding" hype content** that produces impressive demos and unmaintainable code. List it if it teaches something, but say so in `skip_if`.

## Hard rules

- Every item needs a URL you actually opened or saw in search results. **Never invent an item, a link, a star count, or a length.**
- If you cannot verify a detail, write `UNVERIFIED` for that field. Do not guess.
- If you cannot find a live link at all, leave the item out entirely.
- Do not copy the description from the source page or repo README. Write your own honest sentence, including what is weak about it.
- Prefer the original source URL, never an aggregator's link.
- Flag anything published more than about 12 months ago as possibly outdated. For this audience, six months is already old.
- Aim for 20–35 items. Quality over quantity.

## What to save

Save two files in the working folder. Replace `YYYY-MM-DD` with today's date.

### 1. `claude-research-developer-YYYY-MM-DD.md`

A readable report containing:

- A table with columns: Title | URL | Author/Source | Format | Level | Time | Cost | Tier | Last updated | Why it's good | Skip if
- **Dead or moved links** — Anthropic has renamed several docs URLs and repos, note any redirects
- **Abandoned but still ranking** — repos and lists with high stars and no recent activity, with last-push dates, so they can be blocklisted
- **Name collisions** — repos sharing a name, and which is the real one
- **Avoid** — SEO spam and content farms, with URLs
- **Gaps** — what developers clearly need but nobody has made

### 2. `claude-research-developer-YYYY-MM-DD.json`

A JSON array, one object per item, using **exactly** these field names:

```json
{
  "title": "",
  "url": "",
  "author": "",
  "roles": ["developer"],
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
  "notes": "For repos, ALWAYS include star count and last-push date. Otherwise anything odd."
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
