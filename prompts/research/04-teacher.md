# Research task: the best Claude learning content for teachers and educators

You have been given this file as your task. Read it, do the research, save the results as files, and show them to me.

## Setup

- Check today's date first. Use it as the `checked` date on every item.
- Use web search heavily. **Never answer from memory** — content about AI tools goes stale within months, so anything you "remember" is probably wrong or outdated.
- This is a long job. Work through it properly rather than quickly. If you can run several searches in parallel, do it.
- Make a task list so I can follow your progress.

## Who this is for

**Teachers and educators** — school teachers, university lecturers, corporate trainers, instructional designers — who want to learn **Claude** (Anthropic's AI assistant).

Cover two different needs, and label which one each item serves:

1. **Using Claude for their own work** — lesson planning, making materials and worksheets, differentiating for different students, feedback and marking, admin.
2. **Teaching students about AI** — AI literacy curricula, classroom policies, assignment design that survives AI, how to talk to students about honest AI use.

Include content for school level and university level. Say which one each item is for.

## Where to look

Search these specifically. Do not stop at the first page of results.

- Anthropic's free courses at claude.com/resources/courses and anthropic.skilljar.com — there is a whole educator family here: "AI Fluency for educators", "Teaching AI Fluency", an "AI Fluency for pK-12 Educators" path. Find all of them and list each separately
- Anthropic's Campus program at claude.com/programs/campus
- Anthropic Help Center at support.claude.com
- Ministry of education and national curriculum guidance on AI in schools — several countries have published real guidance
- University teaching-and-learning centres — many publish excellent AI guidance that nobody indexes
- Teacher-focused YouTube channels and communities
- Coursera, edX, LinkedIn Learning — AI-for-educators courses
- Reddit r/Teachers and r/ClaudeAI — what teachers actually ask

## What counts as "best" — in this priority order

1. **Is it still accurate?** Claude's interface and features change every few months. This is the single most important test.
2. **Does it teach doing, not just watching?** Prefer real lesson examples, ready-to-use prompts, and worked classroom scenarios.
3. **Is the source trustworthy?** Official Anthropic material, education ministries, universities, practising teachers. Downrank SEO spam and AI-tool vendors selling to schools.
4. **Is it realistic about classrooms?** Uprank anything written by someone who has actually taught. Downrank content that ignores real constraints — no devices, no budget, mixed ability, safeguarding rules.

Popularity — views, ratings, subscriber counts — is a **tiebreaker only**, never a ranking signal.

## A specific warning

A lot of "AI for teachers" content is vendor marketing wearing a teacher costume — a free webinar that is really a product demo. List it only if it genuinely teaches something, and say so plainly in `notes`.

Also: content about AI detection tools is largely unreliable. If you find resources promoting AI detectors as a solution, flag that in `skip_if` — detection accuracy is contested and false accusations harm students.

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

### 1. `claude-research-teacher-YYYY-MM-DD.md`

A readable report containing:

- A table with columns: Title | URL | Author/Source | Format | Level | Time | Cost | Tier | Own work or teaching students | Why it's good | Skip if
- **Dead or moved links** you found while searching
- **Looks outdated** — items that appear stale, and why
- **Avoid** — SEO spam, vendor marketing disguised as training, AI-detector promotion, with URLs
- **National and institutional guidance** — official AI-in-education guidance with URLs and dates
- **Gaps** — what teachers clearly need but nobody has made

### 2. `claude-research-teacher-YYYY-MM-DD.json`

A JSON array, one object per item, using **exactly** these field names:

```json
{
  "title": "",
  "url": "",
  "author": "",
  "roles": ["teacher"],
  "level": "",
  "topics": [],
  "format": "",
  "time": "",
  "cost": "",
  "language": "en",
  "tier": "",
  "summary": "What it teaches, in plain language. One or two sentences.",
  "who_for": "Who specifically should use this. Say school or university, and own-work or teaching-students.",
  "skip_if": "When someone should NOT bother with this. Be honest.",
  "published": "YYYY-MM-DD or UNVERIFIED",
  "checked": "today's date",
  "status": "live",
  "notes": "Anything odd — vendor marketing, outdated screens, paywall."
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
