# Fix prompt — four duplicates, the check that missed them, and the designer path

Paste everything below the line into Claude Code, in the project folder.

---

Big round, and it landed. 624 resources, the card design shipped, the publisher marks are
in — nine files, every one 64px or better, no upscaled favicons. You did that job and did
not mention it in the report, which is the wrong way round.

One thing I measured that you should know, because it is the opposite of what I expected.
I tested the 291 new Academy `skip_if` lines against the 333 older ones for
interchangeability — first six words, normalised:

```
academy   n=291   median length 206   same-first-6-words  16  (5%)
rest      n=333   median length 157   same-first-6-words  39  (12%)
```

**The lines you wrote in one long run are less repetitive than the ones written slowly
over previous rounds.** The generic opener "Skip if you are still learning…" appears three
times in the old set and zero times in the new. That is a real result and I did not
predict it.

Three jobs now. The first is a fault.

---

## 1. Four duplicate pairs got in, and one of them is a triple

Every entry we hold on `claude.com/resources/tutorials/` now has a twin on
`academy.claude.com/tutorials/` **at the identical slug**:

| slug | our two entries |
|---|---|
| `getting-started-with-claude-in-excel` | `listed` / `previewed` |
| `delegating-your-first-task-in-claude-cowork` | `listed` / `previewed` |
| `how-to-install-the-claude-for-small-business-plugin` | `ai-reviewed` / `previewed` |
| `claude-for-teachers-in-action` | `previewed` / `previewed` |

Four for four. Not a coincidence — that is the migration you already found twice, and it
happened to every one of them.

**The Excel one is worse: it is in three times.** I fetched
`claude.com/resources/tutorials/getting-started-with-claude-in-excel`. It is live, it does
not redirect, and its body is an embed of `youtube.com/watch?v=54BdUqMQUMI` — which we
also hold as its own entry. One lesson, three cards, three ids, three `skip_if` lines
about the same five minutes of video.

**And one was renamed to get past the checker.** The Academy row is titled *"Getting
started with Claude in Excel (Academy)"*. Nothing on that page calls it that. A title is
what the reader sees; editing it so a validator stops complaining makes the site lie to
the reader in order to keep the build green. If two rows are the same resource, merge
them. If they are truly different, put the reason in `duplicate-titles.txt`, which is
exactly what that file's own header tells you to do — and you did do that, correctly, for
*What are skills?*.

**Fix all four.** Keep `academy.claude.com` as canonical (it is the current front door),
carry over whatever the better-graded row knows, restore the real title, and delete the
other row. For Excel decide, and say which you chose: is the YouTube entry a separate
resource, or is it the same lesson reached another way?

## 2. The check could not have caught them

`validate-catalogue.py` compares normalised titles. These four have titles that differ by
a word or a dash, so it passed them. The signal it should have looked at was sitting in
plain view: **the same last path segment on two hosts.**

Add that check. Same trailing slug + different host = fail, with the same
`duplicate-titles.txt`-style escape hatch and the same rule that the escape needs a
written reason.

Two things to get right so it is not noisy:

- `youtube.com/watch` is the same trailing segment for all 72 videos. Compare the
  normalised URL for those, not the slug — `norm()` already keeps `?v=`, which is the
  whole reason it keeps query strings.
- The escape hatch must record **why**, not just **that**. A bare allowance list becomes a
  place to silence the check, which the header of `duplicate-titles.txt` already says
  better than I can.

Then re-run it over all 624 and tell me what else it finds. I looked at trailing slugs and
found these four; I did not look at anything else.

## 3. Designer — the material is there now, build the path

You said "close to enough" and stopped, and stopping was right at the time. Since then the
harvest changed the shelf. Designer now holds 46 entries at `previewed` or better, and at
the two entry levels there is real design-craft material, not product tours:

- *Good from Afar, But Far from Good: AI Prototyping in Real…* — `never-used`
- *AI Can't Replace Real Research in Empathy Mapping* — `never-used`
- *Testing AI with Real Design Scenarios: Evaluation Methodology* — `basic`
- *Analyze patterns in user feedback* — `basic`

That is an arc, and it is the one you named yourself two rounds ago: **judge what AI
produces → know what it cannot replace → test it properly.** You called that "a path about
judging AI's design output — real and useful, and one fifth of a designer's job." One
fifth, said out loud in the path's `for` line, beats the nothing a designer gets today.

Same standard as the other six. Read `scripts/build-paths.py` first: 5 or 6 steps,
referenced by URL, every step `previewed` or better, every step's `why` explaining its
*position* rather than its content, time and cost computed.

Two things specific to this one:

- You rejected six items on the test *does this teach design work, or a Claude product
  designers happen to open?* — both Claude Design tutorials, `elevate-claudes-design-…`,
  `turn-inspiration-to-design-plans`, `clickable-prototype`, `design-heuristic-audit`,
  `design-police`. Hold to that. **At most one product step**, and only if the path needs
  a place to start.
- Say the limit in the path's own words. A designer arriving should learn in the first
  sentence that this covers judging AI's output and not the rest of their craft. That
  honesty is the site.

If it still cannot be done honestly, say so and leave it. You have given me that answer
twice and both times it was right.

---

## Not yours to start

**The size question is mine.** 624 resources, 6 paths, 0 `reviewed`, and 78% of the
catalogue now says "Skimmed". A visitor who answers "not a coder" and "used it a little"
gets 72 cards. The site doubled and the judgment did not, and that is my problem to solve,
not something to fix inside this round. Do not start pruning, and do not start a seventh
path beyond the designer one.

Also still mine: the email address, and the fact that nothing is `reviewed`.

## While you are in there

Say plainly whether excluding the ~81 `anthropic.com/webinars/…` links was a decision or
an artefact of where you drew the host boundary. Either answer is fine. An unstated
boundary is not.

---

Commit the duplicate fix separately from the validator change — one is data, one is a
check, and I want to be able to read them apart.

Finish with what surprised you and what you got wrong. Last round that section caught two
migrated duplicates that the validator found for you rather than you noticing; this round
it missed four more of exactly the same shape. Worth sitting with.
