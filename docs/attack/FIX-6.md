# Fix prompt — the 79 `Skip if:` lines that say nothing

Paste everything below the line into Claude Code, in the project folder.

---

Excellent round. The laptop-versus-runner finding was the important one, and you caught
it by re-reading your own claim rather than moving on.

Park the email question — we will discuss that later. This one is about the quality of
the site itself, and it is the most important content job left.

## The problem, measured

`Skip if:` is the reason this site exists. `README.md` says a link with no judgment is
just a list. Yet **79 of 352 entries have a `skip_if` under 70 characters**, and the
worst of them do nothing but negate the title:

```
"ClaudeR (R + RStudio MCP)"                  ->  "You don't use R."
"Use Claude for Excel"                       ->  "You don't use Excel."
"Claude Code and Figma: Set up the MCP …"    ->  "You don't use Figma."
"Guide to the Figma MCP server"              ->  "You're not using MCP."
"Connect and integrate your local Zotero …"  ->  "You don't use Zotero."
"What are Projects?"                         ->  "You already use Projects."
```

A reader who has read the title already knows all of that. It clears the empty check and
fails the reader — which is worse than blank, because nothing flags it.

Your own measurement showed the split by `checked` date: 19–20 August averages 41–57
characters, 21–22 August averages 134–167. The later ones are the standard.

## The test that decides it

**Would someone who has just read the title, source and format already know this?**

If yes, the line is doing no work. That is the rule — not a character count. A short line
can pass: "Skip if your data cannot leave your laptop" is short and tells me something
the title never did.

A good `skip_if` names one of these:

- a **prerequisite** the title hides — a paid plan, a terminal, an account, a specific OS
- a **scope limit** — it covers X but stops before Y, which is what most people came for
- a **staleness or accuracy risk** — figures from a version that has moved
- a **mismatch of depth** — too introductory if you already do this daily, or the reverse
- **who it is genuinely wrong for**, in their own words

## The hard rule: derive, never invent

Every rewritten line must come from something the entry already records — `summary`,
`who_for`, `teaches`, `notes`, `level`, `cost`, `time`, `format` — or from opening the
source and reading it.

**If you cannot ground a line in one of those, open the URL.** If you still cannot, leave
the line as it is and list it for me. An honest weak line beats a confident invented one,
and we have already had one invented claim reach the live site this week.

Where you open a source and read it, that entry's tier may be wrong in our favour — say
so rather than silently upgrading it.

## Do it in three batches, and stop after the first

1. **The 12 shortest first.** Rewrite those, show me every before and after, and stop.
   I want to check the voice before you do seventy more.
2. Then the rest under 40 characters.
3. Then the remainder under 70.

Anything you could not ground goes in a list at the end of each batch, with the reason.

## What would make this wrong

- A house style. These should not all begin "Skip if". The 22 August lines vary, and that
  variation is what stops the card reading as a form.
- Padding a real short line to look substantial.
- Touching `who_for`, `summary`, or any other field. Only `skip_if`.
- Rewriting a line that already passes the test just because it is short.

---

Batch 1 only. One commit. Show me all 12 before and after, and tell me how many of the 79
you expect to survive untouched.
