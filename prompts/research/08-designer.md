# Research task: the best Claude learning content for designers and creatives

You have been given this file as your task. Read it, do the research, save the results as files, and show them to me.

## Setup

- Check today's date first. Use it as the `checked` date on every item.
- Use web search heavily. **Never answer from memory** — content about AI tools goes stale within months, so anything you "remember" is probably wrong or outdated.
- This is a long job. Work through it properly rather than quickly. If you can run several searches in parallel, do it.
- Make a task list so I can follow your progress.

## Who this is for

**Designers and creatives** — UX/UI designers, graphic designers, illustrators, 3D artists, creative directors — who want to learn **Claude** (Anthropic's AI assistant).

Focus on: turning designs into working prototypes, writing UX copy and microcopy, design research and synthesis, accessibility review, design systems and documentation, working with Figma through MCP, handoff specs for developers, and using Claude Code or Cowork to build something real without an engineer.

Note that Claude is a text and code assistant, **not an image generator**. Content about Midjourney or image models is out of scope unless it is genuinely about a Claude workflow.

## Where to look

Search these specifically. Do not stop at the first page of results.

- Anthropic's free courses at claude.com/resources/courses and anthropic.skilljar.com — including Cowork content
- Anthropic Help Center at support.claude.com
- Claude Code docs at code.claude.com/docs — designers increasingly use it for prototyping
- Figma MCP and design-tool MCP servers — github.com/modelcontextprotocol and community lists
- Design blogs and newsletters that cover AI seriously
- YouTube channels covering AI for design and prototyping
- Coursera, Udemy, LinkedIn Learning, Skillshare, Domestika — design-focused AI courses
- Reddit r/UXDesign, r/web_design, r/ClaudeAI — search for posts by designers about real workflows

## What counts as "best" — in this priority order

1. **Is it still accurate?** Claude's interface and integrations change every few months. This is the single most important test.
2. **Does it teach doing, not just watching?** Prefer real projects, working files, and copyable prompts over "the future of design" talks.
3. **Is the source trustworthy?** Official Anthropic material, practising designers, established design educators. Downrank SEO spam and tool vendors.
4. **Does it respect craft?** Uprank content that treats AI as a tool inside a real design process. Downrank content that presents design as something AI can just do for you — this audience will reject it, correctly.

Popularity — views, ratings, subscriber counts — is a **tiebreaker only**, never a ranking signal.

## Specific warnings

- **Off-topic image-generation content.** Much "AI for designers" content is really about Midjourney or Stable Diffusion. That is a different tool. Leave it out unless the Claude part is substantial.
- **Prototypes that look finished but are not.** A lot of content shows a beautiful AI-generated interface and skips accessibility, responsive behaviour, and real data. If a resource does this, say so in `skip_if`.

Also worth capturing: designers who have publicly documented shipping something real with Claude. Those accounts are more persuasive to this audience than any course.

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

### 1. `claude-research-designer-YYYY-MM-DD.md`

A readable report containing:

- A table with columns: Title | URL | Author/Source | Format | Level | Time | Cost | Tier | Design discipline | Why it's good | Skip if
- **Dead or moved links** you found while searching
- **Looks outdated** — items that appear stale, and why
- **Avoid** — SEO spam, and image-generation content mislabelled as Claude content, with URLs
- **Real case studies** — designers who publicly documented shipping something with Claude, with URLs
- **Gaps** — what designers clearly need but nobody has made

### 2. `claude-research-designer-YYYY-MM-DD.json`

A JSON array, one object per item, using **exactly** these field names:

```json
{
  "title": "",
  "url": "",
  "author": "",
  "roles": ["designer"],
  "level": "",
  "topics": [],
  "format": "",
  "time": "",
  "cost": "",
  "language": "en",
  "tier": "",
  "summary": "What it teaches, in plain language. One or two sentences.",
  "who_for": "Who specifically should use this. Say which design discipline.",
  "skip_if": "When someone should NOT bother with this. Be honest.",
  "published": "YYYY-MM-DD or UNVERIFIED",
  "checked": "today's date",
  "status": "live",
  "notes": "Tools assumed (Figma, code, etc.), plus anything odd."
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
