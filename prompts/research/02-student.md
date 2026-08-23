# Research task: the best Claude learning content for students

You have been given this file as your task. Read it, do the research, save the results as files, and show them to me.

## Setup

- Check today's date first. Use it as the `checked` date on every item.
- Use web search heavily. **Never answer from memory** — content about AI tools goes stale within months, so anything you "remember" is probably wrong or outdated.
- This is a long job. Work through it properly rather than quickly. If you can run several searches in parallel, do it.
- Make a task list so I can follow your progress.

## Who this is for

**Students** — university and upper-secondary — who want to learn **Claude** (Anthropic's AI assistant) for studying.

Focus on: studying and revising, understanding difficult material, reading and summarizing papers, note-taking, writing assignments honestly, preparing for exams, managing a research project, and — importantly — **academic integrity**: what is allowed, what counts as cheating, how to disclose AI use.

Include content aimed at students in any subject, not just computer science. A history student and a biology student both need this.

## Where to look

Search these specifically. Do not stop at the first page of results.

- Anthropic's free courses at claude.com/resources/courses and anthropic.skilljar.com — there is an "AI Fluency for students" course, find it and anything similar
- Anthropic's Campus program at claude.com/programs/campus — see what universities it links to
- University library guides and academic-skills centres — many universities publish their own AI guidance. These are high quality and nobody indexes them
- University academic-integrity policies about AI use, especially any that are well written and general enough to be useful
- The official Claude YouTube channel (youtube.com/@claude)
- YouTube study-skills channels that cover AI tools
- Coursera, edX, Udemy — student-oriented AI courses
- Reddit r/ClaudeAI and student subreddits — what students actually ask

## What counts as "best" — in this priority order

1. **Is it still accurate?** Claude's interface and features change every few months. This is the single most important test.
2. **Does it teach doing, not just watching?** Prefer real examples and exercises.
3. **Is the source trustworthy?** Official Anthropic material, universities, known educators. Downrank SEO spam and channels farming views.
4. **Is it honest about academic integrity?** Downrank anything that teaches students to hide AI use or beat detectors. Uprank anything that teaches genuine learning with AI rather than outsourcing thinking.

Popularity — views, ratings, subscriber counts — is a **tiebreaker only**, never a ranking signal.

## A specific warning

There is a large amount of content aimed at students that is effectively "how to cheat without getting caught". Do not list it as a learning resource. If it is prominent enough that people will find it anyway, put it in the Avoid section with the URL so it can be blocklisted.

Also watch for content that encourages students to let AI do their thinking for them. Flag this in `skip_if`.

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

### 1. `claude-research-student-YYYY-MM-DD.md`

A readable report containing:

- A table with columns: Title | URL | Author/Source | Format | Level | Time | Cost | Tier | Why it's good | Skip if
- **Dead or moved links** you found while searching
- **Looks outdated** — items that appear stale, and why
- **Avoid** — SEO spam, scams, or "how to cheat" content, with URLs, so it can be blocklisted
- **University guides worth following** — any institution publishing consistently good AI guidance
- **Gaps** — what students clearly need but nobody has made

### 2. `claude-research-student-YYYY-MM-DD.json`

A JSON array, one object per item, using **exactly** these field names:

```json
{
  "title": "",
  "url": "",
  "author": "",
  "roles": ["student"],
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
  "notes": "Anything odd — outdated screens, integrity concerns, paywall."
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
