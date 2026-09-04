Write in ASD-STE100. never do anything before asking me.
# Project: Claude Teaching Website

## What this is
A curated, categorized directory of the best tutorials, courses, and videos for learning
Claude and other AI tools — filtered by level, field, and role, so people can find what
actually fits them instead of drowning in options.

## How to talk to me (Morteza)
- Short. Simple. Direct. No long explanations unless I ask.
- Answer first, then (only if needed) one or two lines of reasoning.
- No preamble ("Great question!", "Let me...", "I'll now..."). Just do it.
- No recaps of what you just did step by step. One or two sentences on the outcome.
- Bullet lists over paragraphs. Bold sparingly.
- If I ask "what do you think?" — give a real opinion, including disagreement.
- Ask me a question when it actually changes what you'd do. Otherwise pick a sane
  default, say which one you picked in one line, and move on.
- English is not my first language. Write plainly.

## Working rules
- Save all deliverables to this folder. Nothing useful should live only in chat.
- Before building anything new: brainstorm → spec → plan → build. Don't jump to code.
- Specs go in `docs/specs/YYYY-MM-DD-<topic>.md`.
- Research output goes in `research/` as markdown with sources and dates.
- Every claim about a course/tool/price/link must have a source URL and the date checked.
  AI-tool content goes stale in months — always search, never answer from memory.
- Prefer one file that does one thing. Split when a file gets long.
- Verify before claiming done: run it, open it, check the links.
- Shell hygiene: never put a regex or a backslash through a heredoc — write scripts to a
  file and run the file. Commit messages via `git commit -F`. Never background a command
  that backgrounds itself; confirm a job started before reporting it running.
- Numbers anywhere a reader or I will read them — docs, path intros, UI strings, commit
  messages that state a count — are generated or measured, never typed.
  `scripts/measure.py` writes `docs/STATUS.md` on every build; docs point at it.
- A commit does one job. If a file change serves two jobs, the second waits.
- Scratch files go in `tmp/` — gitignored — never outside the repo.

## Tech defaults (unless we decide otherwise)
- Static site, no backend. Data lives in a JSON/YAML file, site reads from it.
- Plain HTML/CSS/JS or a static generator. No heavy framework unless there's a reason.
- Deploy: free static hosting (GitHub Pages / Cloudflare Pages / Netlify).
- Must work on mobile. Search and filter must be instant, client-side.

## Content rules for the directory
- Every entry needs: title, link, source/author, format, level, field/role, length,
  language, free vs paid, date published, date we checked it.
- Say *why* an entry is good and *who* it's for. A link with no judgment is worthless —
  that's the whole point of the site.
- Prefer official/primary sources first, then well-known independent ones.
- Mark anything older than ~12 months as possibly outdated.
- Never invent a course, link, or review. If it isn't verified, it doesn't ship.
