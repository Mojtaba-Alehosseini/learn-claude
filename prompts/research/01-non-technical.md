# Research task: the best Claude learning content for non-technical people

You have been given this file as your task. Read it, do the research, save the results as files, and show them to me.

## Setup

- Check today's date first. Use it as the `checked` date on every item.
- Use web search heavily. **Never answer from memory** — content about AI tools goes stale within months, so anything you "remember" is probably wrong or outdated.
- This is a long job. Work through it properly rather than quickly. If you can run several searches in parallel, do it.
- Make a task list so I can follow your progress.

## Who this is for

People who want to learn **Claude** (Anthropic's AI assistant) and who are **non-technical**: no coding background, no terminal, no API. Think of a nurse, an HR manager, a lawyer, an office administrator, a small-shop owner. They use Claude in a browser or the desktop app.

Focus on: the Claude chat app, Claude Cowork, writing and summarizing, working with documents and files, connecting Claude to tools they already use, and understanding what Claude can and cannot do.

**Exclude** anything that needs the command line, an API key, or programming knowledge. If a resource assumes the reader can code, leave it out.

## Where to look

Search these specifically. Do not stop at the first page of results.

- Anthropic's own free courses at claude.com/resources/courses and anthropic.skilljar.com — especially the "AI Fluency" family and anything about Cowork
- Anthropic Help Center at support.claude.com — underrated, written for non-developers
- The official Claude YouTube channel (youtube.com/@claude)
- YouTube more broadly, but be selective — see the warning below
- LinkedIn Learning, Udemy, Coursera, Skillshare — search for Claude courses aimed at general professionals
- Independent blogs and newsletters that write for non-technical readers
- Reddit r/ClaudeAI — look for highly upvoted posts by people who describe themselves as "non-coder" or "non-technical"

## What counts as "best" — in this priority order

1. **Is it still accurate?** Claude's interface and features change every few months. A well-made video from a year ago may teach screens that no longer exist. This is the single most important test.
2. **Does it teach doing, not just watching?** Prefer content with real examples, exercises, and prompts the reader can copy and try.
3. **Is the source trustworthy?** Official Anthropic material, known educators, real practitioners. Downrank SEO spam and channels farming views.
4. **Is it genuinely right for a non-technical person?** Many "beginner" resources quietly assume technical knowledge. Check.

Popularity — views, ratings, subscriber counts — is a **tiebreaker only**, never a ranking signal. Popular often means beginner clickbait.

## A specific warning

Real complaint from this audience: many YouTube videos spend the first ten minutes on a personal story about making money with AI before saying anything useful. If you find this, still list the item if it is otherwise good, but say so plainly in the `skip_if` field. This is exactly the kind of judgment the directory exists to provide.

## Hard rules

- Every item needs a URL you actually opened or saw in search results. **Never invent an item, a link, a rating, or a length.**
- If you cannot verify a detail, write `UNVERIFIED` for that field. Do not guess.
- If you cannot find a live link at all, leave the item out entirely.
- Do not copy the description from the source page. Write your own honest sentence, including what is weak about it.
- Prefer the original source URL, never an aggregator's link.
- Flag anything published more than about 12 months ago as possibly outdated.
- Aim for 15–30 items. Quality over quantity — 15 verified items beats 40 guesses.

## What to save

Save two files in the working folder. Replace `YYYY-MM-DD` with today's date.

### 1. `claude-research-non-technical-YYYY-MM-DD.md`

A readable report containing:

- A table with columns: Title | URL | Author/Source | Format | Level | Time | Cost | Tier | Why it's good | Skip if
- **Dead or moved links** you found while searching
- **Looks outdated** — items that appear stale, and why
- **Avoid** — anything that looks like SEO spam or a scam, with URLs, so it can be blocklisted
- **Gaps** — what this audience clearly needs but nobody has made

### 2. `claude-research-non-technical-YYYY-MM-DD.json`

A JSON array, one object per item, using **exactly** these field names:

```json
{
  "title": "",
  "url": "",
  "author": "",
  "roles": ["non-technical"],
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
  "notes": "Anything odd — outdated screens, hype-heavy intro, paywall."
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
