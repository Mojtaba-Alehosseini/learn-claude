# Research task: the best Claude learning content for writers, editors, and marketers

You have been given this file as your task. Read it, do the research, save the results as files, and show them to me.

## Setup

- Check today's date first. Use it as the `checked` date on every item.
- Use web search heavily. **Never answer from memory** — content about AI tools goes stale within months, so anything you "remember" is probably wrong or outdated.
- This is a long job. Work through it properly rather than quickly. If you can run several searches in parallel, do it.
- Make a task list so I can follow your progress.

## Who this is for

**Writers, editors, and marketers** — journalists, copywriters, content strategists, communications staff, translators — who want to learn **Claude** (Anthropic's AI assistant).

Focus on: drafting and editing, keeping a consistent voice, research and fact-checking, structuring long documents, editorial workflows, translation and localisation, SEO and content planning, email and campaign copy, and — importantly — **how to make AI-assisted writing not sound like AI**.

Also cover disclosure and ethics: when AI use should be declared, and what publishers and employers now require.

## Where to look

Search these specifically. Do not stop at the first page of results.

- Anthropic's free courses at claude.com/resources/courses and anthropic.skilljar.com
- Anthropic Help Center at support.claude.com — projects, memory, style
- Cowork content — relevant for document-heavy work
- Newsroom and publisher AI policies — several major outlets have published theirs
- Style guides and professional bodies that have issued AI guidance
- Writing and marketing newsletters and blogs
- YouTube channels covering AI for writing, with heavy scepticism applied
- Coursera, Udemy, LinkedIn Learning, Skillshare — writing and marketing AI courses
- Reddit r/writing, r/copywriting, r/marketing, r/ClaudeAI

## What counts as "best" — in this priority order

1. **Is it still accurate?** Claude's interface and features change every few months. This is the single most important test.
2. **Does it teach doing, not just watching?** Prefer real before-and-after examples, editing exercises, and copyable prompts.
3. **Is the source trustworthy?** Official Anthropic material, working writers and editors, established educators. Downrank SEO spam — which is unusually dense in this category.
4. **Does it produce writing a professional would accept?** Uprank anything that teaches editing, voice control, and removing AI tells. Downrank anything that treats a first draft as a finished product.

Popularity — views, ratings, subscriber counts — is a **tiebreaker only**, never a ranking signal.

## Specific warnings

- **Content-farm output.** A very large share of "AI writing" content is itself AI-generated SEO filler. You can usually tell: no specific examples, no named author, generic headings, no criticism of the tool. Put these in the Avoid list.
- **Volume-over-quality advice.** Content teaching people to publish fifty articles a week is harmful to a professional writer's reputation and to search rankings. Flag it in `skip_if`.

Also valuable and rarely covered: material on **detecting and removing AI writing tells** — the stock phrases, the rule-of-three constructions, the inflated transitions. If you find good resources on this, prioritise them.

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

### 1. `claude-research-writer-marketer-YYYY-MM-DD.md`

A readable report containing:

- A table with columns: Title | URL | Author/Source | Format | Level | Time | Cost | Tier | Writing use | Why it's good | Skip if
- **Dead or moved links** you found while searching
- **Looks outdated** — items that appear stale, and why
- **Avoid** — AI-generated content farms and volume-over-quality advice, with URLs
- **Disclosure policies** — newsroom, publisher, and professional-body AI policies, with URLs and dates
- **Gaps** — what writers clearly need but nobody has made

### 2. `claude-research-writer-marketer-YYYY-MM-DD.json`

A JSON array, one object per item, using **exactly** these field names:

```json
{
  "title": "",
  "url": "",
  "author": "",
  "roles": ["writer-marketer"],
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
  "notes": "If the resource itself looks AI-generated, say so. Plus anything odd."
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
