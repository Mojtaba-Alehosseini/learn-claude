# Deep research prompts — how to use them

**Created:** 2026-08-16
**Written for:** Claude Cowork (or Claude Code). Each file is a self-contained task.

Ten task files, one per role in our taxonomy. Every file contains only the task — no
notes, no wrapper text. Nothing needs to be trimmed before handing it over.

## Handing one to someone

1. Send them the file.
2. Tell them to drop it into a Cowork session and say something like *"do this."*
3. That's it. The file tells Cowork to check the date, research, save two output files, and show them.

They send back the two files it produced.

## What comes back

Two files per run:

- `claude-research-<role>-YYYY-MM-DD.md` — readable report with a table plus the flagged sections (dead links, outdated, avoid, gaps)
- `claude-research-<role>-YYYY-MM-DD.json` — the machine-readable version, matching the field names in `docs/specs/2026-08-19-directory-spec.md`

The JSON is what actually matters. If a report comes back without it, or with wrong
field names, ask for a re-run rather than fixing it by hand.

## Controlled vocabulary

Every file includes this table. Values outside it get rejected on ingest.

| Field | Allowed values |
|---|---|
| `level` | `never-used`, `basic`, `confident`, `builder` |
| `topics` | `chat-prompting`, `claude-code`, `cowork`, `skills`, `mcp`, `agents`, `api`, `safety` |
| `format` | `video`, `course`, `docs`, `article`, `hands-on`, `podcast`, `repo` |
| `time` | `under-15min`, `under-1hr`, `half-day`, `multi-day` |
| `cost` | `free`, `free-account`, `paid-once`, `subscription` |
| `tier` | `ai-reviewed` (docs/article only), `previewed`, `listed` |

Note: some roles get a narrower `topics` list. Non-technical, teacher, business, and
writer files drop `claude-code` and `api` on purpose — that content is not for them.

### About the tier field — changed 2026-08-19

There are now four tiers. A research run may use three of them.

| Tier | Who may set it | Meaning |
|---|---|---|
| `reviewed` | **Human only** | Full content consumed and a person confirmed it |
| `ai-reviewed` | Gemini pipeline, any format · a research run, **docs and article only** | Full content consumed by AI, no person checked |
| `previewed` | A research run | Syllabus, outline or free sample only |
| `listed` | A research run | Metadata only, content not checked |

A research run is web search. It can read a docs page or an article in full. It cannot
watch a two-hour course. So `ai-reviewed` on a `video` or `course` is rejected on ingest,
and `reviewed` is rejected always. See `docs/specs/2026-08-19-directory-spec.md`, section 7.

## The files

| File | Role | Output prefix |
|---|---|---|
| `01-non-technical.md` | People with no coding background | `claude-research-non-technical-` |
| `02-student.md` | University and school students | `claude-research-student-` |
| `03-researcher.md` | Researchers and academics | `claude-research-researcher-` |
| `04-teacher.md` | Teachers and educators | `claude-research-teacher-` |
| `05-developer.md` | Software developers and engineers | `claude-research-developer-` |
| `06-data-analyst.md` | Data analysts and data scientists | `claude-research-data-analyst-` |
| `07-product-manager.md` | Product managers | `claude-research-pm-` |
| `08-designer.md` | Designers and creatives | `claude-research-designer-` |
| `09-business-founder.md` | Founders, business owners, operations | `claude-research-business-founder-` |
| `10-writer-marketer.md` | Writers, editors, marketers | `claude-research-writer-marketer-` |

## What to expect

Roughly 15–30 items per run, 20–35 for developers. Anything much larger usually means
it stopped verifying and started listing from memory.

## Checking a report before trusting it

- **Open three or four URLs at random.** If any 404, discard the whole report.
- **Missing `checked` dates** means it did not actually verify.
- **Any item marked `reviewed`** is a lie — that tier is for humans only. **`ai-reviewed` on a video or course** is also a lie. The validator rejects both.
- **Descriptions that read like marketing copy** were probably copied from the source page. The files forbid this. Real judgment contains criticism.
- **An empty Avoid section** on the business-founder or writer runs means the filter did not work. Those categories are full of junk.

## Role-specific traps built into the files

- **05-developer** — must report star count *and* last-push date for every repo, plus name collisions.
- **09-business-founder** — hard filter with named criteria; hype content goes to a separate Avoid list, not the main list.
- **03-researcher** — must flag any resource teaching literature review without warning about fabricated citations.
- **02-student** — "how to beat AI detectors" content goes to Avoid, never the main list.
- **10-writer-marketer** — must say when the resource *itself* looks AI-generated.
- **04-teacher** — must flag vendor webinars disguised as training, and AI-detector promotion.
