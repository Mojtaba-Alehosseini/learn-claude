# The questions rewrite, read cold

FIX-30 asked for twenty rows at random, read cold, with a one-word verdict each.

**How the read was made cold.** `tmp/sample.py` draws twenty rows with a fixed seed and
prints their `questions[]` and nothing else — no title, no summary, no id. I read the four
questions, said what page I thought they belonged to and whether a person would type them,
and only then ran the same script with `--reveal`. The verdict below is the verdict I gave
before the title appeared.

**What the verdicts mean.**

- **good** — I named the page from the questions alone, and the questions read like typing.
- **generic** — the questions are honest but name a category, not this page. Somebody
  looking for this row would not type them, and somebody typing them wants a different row.
- **loose** — the subject-naming question paraphrases the page instead of using the page's
  own name. Findable, but it gives away a word the page owns.
- **collides** — the questions fit this row and at least one other row equally well.

## The twenty

| # | row | verdict |
|---|---|---|
| 1 | Teaching AI Fluency (Anthropic Academy) | good |
| 2 | Set up your design system in Claude Design | good |
| 3 | Write in my voice | good |
| 4 | Nature Portfolio — Artificial Intelligence (AI) editorial policy | good |
| 5 | What are skills? | good |
| 6 | Claude AI Comprehensive Guide | generic |
| 7 | Create a custom webpage | good |
| 8 | Prompt engineering best practices for 2026 | good |
| 9 | Draft investment memos | good |
| 10 | Claude Researcher — source-first literature review workflows | good |
| 11 | Introducing Claude for Teachers | good |
| 12 | Git Worktrees Explained — Run Multiple AI Agents in Parallel | good |
| 13 | Analyze campaign performance | good |
| 14 | Using the Open Targets Connector in Claude | good |
| 15 | How to Spot AI Writing, According to Wikipedia | good |
| 16 | Use Claude for Excel | good |
| 17 | Claude Cowork in 5 Minutes | loose |
| 18 | MCP Python SDK | good |
| 19 | Analyze patterns in user feedback (use case) | good |
| 20 | Anthropic Claude for Absolute Beginners | good |

Nineteen of the twenty I placed correctly from the questions alone. The one I could not
place was number 6.

## The three that are not clean

**6 — Claude AI Comprehensive Guide, `generic`.** Its subject-naming question is "claude
course with a certificate". That is a category, not this page. Reading the questions cold I
could not tell which course it was, and neither could a reader. The page's own name never
appears. This is the failure the subject-naming rule exists to prevent, and the rule did
not save the row because I applied it to the *kind* of thing rather than to the *name* of
the thing.

**17 — Claude Cowork in 5 Minutes, `loose`.** The subject-naming question is "claude cowork
quick start". The page calls itself *in 5 Minutes*; a reader who saw it recommended and
half-remembers the name types the name. Findable by luck, not by the rule.

**19 — Analyze patterns in user feedback, marked `good` cold, and it is not.** I placed the
row correctly, so the cold verdict stands as recorded. Revealing it showed something the
cold read could not: three rows in the catalogue answer this — *Analyze patterns in user
feedback*, *Feedback synthesis to prioritized themes*, and *Themes across all feedback
channels* — and my questions for this one do not say what is different about it. The cold
read cannot catch a collision, because a collision is a fact about the other rows. That is
a limit of this method, written down so the next sample is not read as proof of more than
it shows.

## What this sample does not measure

It says nothing about ranking. A row can have questions a person would type and still lose
to a better-matching row, and a row with weak questions can win because nothing competes.
The suite number is the ranking measure; this is the writing measure.
