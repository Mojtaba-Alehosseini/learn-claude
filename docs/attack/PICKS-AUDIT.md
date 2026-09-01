# Audit of the 37 picks cells — read, not sampled

Written 31 August 2026, after the picks shipped. The checkpoint before shipping covered
three cells; the other 34 went live unread. This is that reading: every cell, every
reason sentence, every runner-up line, and all 22 stored justifications.

The bars are the project's own, from FIX-15:

1. **The reason bar.** Every reason says why this pick beat the pool. If someone who
   read the title would already know it, it is not doing work.
2. **Card-answerable.** Every sentence must be writable from the card fields alone.
3. **Self-contradiction.** No pick whose own `skip_if` or `who_for` argues against the
   cell's role or level.
4. **Justifications are reasons, not permits.** Each shared-topic note must explain why
   the clash serves the reader, not merely acknowledge it.

---

## What the reading found

| | count |
|---|---|
| Cells read | 37 |
| Pick reasons read | 109 |
| Runner-up lines read | 107 |
| Stored justifications read | 22 |
| **Reasons failing check 1** (does no work / leads with machinery) | **1** |
| **Reasons failing check 2** (not answerable from the card) | **8** |
| **Picks failing check 3** (card argues against the cell) | **0** |
| **Justifications failing check 4** (a permit, not a reason) | **0** of 22 |
| Quality verdicts ("best") in stored copy | **8**, all in runner-up lines |
| Mechanical faults | **1** (a typo in a stored note) |
| **Total changes made** | **18** |

Check 2 was the weak one, and the pattern behind it is worth naming: every one of the
eight rested on something true that the reader could not check — a fact from `notes`
(stripped from the browser mirror), a count I had in my head rather than in the pool, or
a relationship between resources no card states. None were invented. All eight were
unverifiable, which on this site is the same fault wearing better clothes.

### The cause of the check-2 cluster, and its fix

`card_view()` in `scripts/pick-candidates.py` did not include `summary`. The picker was
therefore handed **less than the reader sees** — summary is the most prominent field on
a rendered card — so it reached for facts from elsewhere to fill the gap. `summary` is
now in `card_view`, with a note saying why, and `notes` is explicitly kept out: it never
reaches the browser, so a reason resting on it could never be checked by anyone.

Two reasons that leaned on the summary (`developer|confident` on the Frontend Masters
course, `developer|builder` on the Agent SDK workshop) were checked and **left alone** —
both claims are in the summary, which is on the card, so a reader can verify them.

---

## The mechanical sweep

| check | result |
|---|---|
| Headings count-honest | pass — 35 cells of three, 2 of two, each heading agreeing |
| `picked_by: "ai"` present | pass — 37 of 37 |
| `picked_on` present and a date | pass — 37 of 37 |
| Runner-up records complete (2–3, each with a reason) | pass — 107 lines |
| Fingerprints match current pools | pass — 37 of 37 |
| No "best", "top", "recommended" | **8 found, 8 fixed**; 5 further hits cleared |

The five cleared hits are not quality claims and were left as written:

- `developer|basic`, `developer|confident` — "Anthropic's best-practices docs" and
  "the best-practices pick". That is the page's **name**.
- `developer|builder` (twice) — "reverses several of its recommendations". Describing
  what an article does, not recommending anything.
- `teacher|basic` — "with skills on top". The idiom, not a ranking.

---

## Every change, old and new

### Check 2 — not answerable from the card

**researcher|basic** — ICMJE Recommendations — Use of AI in Publishing *(reason)*  
*Why:* NOT CARD-ANSWERABLE: 'the umbrella body the others cite' is outside knowledge; no card says it. Replaced with a comparison the three cards do support.  
*Was:* Three journal-policy candidates, and this is the umbrella body the others cite - one policy slot, and it goes to the broadest authority.  
*Now:* Three journal-policy candidates, and this is the only one not tied to a single publisher - IEEE and Elsevier each bind their own journals, where this covers any medical or biomedical submission.

**researcher|confident** — Verify statistics from raw data *(reason)*  
*Why:* NOT CARD-ANSWERABLE: the 'hundred-fold unit error' lives only in `notes`, which is stripped from the browser mirror. A reader could never verify it.  
*Was:* The rarest habit in the pool - checking a paper's numbers against its own raw data, with a worked example that catches a hundred-fold unit error.  
*Now:* The rarest habit in the pool - recomputing a paper's statistics from the authors' own raw data before citing it, which nothing else here does - and its card is clear you need both the manuscript and that raw data to try it.

**student|confident** — Verify statistics from raw data *(reason)*  
*Why:* NOT CARD-ANSWERABLE: same notes-only 'hundred-fold unit error' claim as researcher|confident.  
*Was:* The rarest skill in the pool: checking a paper's numbers against its own raw data before leaning on it - the worked example catches a real hundred-fold unit error, which is the argument in one line.  
*Now:* The rarest skill in the pool: recomputing a paper's statistics from the authors' own raw data before leaning on it - and its card is honest that this needs the manuscript and the raw data together, not the paper's text alone.

**developer|confident** — Best practices for Claude Code *(reason)*  
*Why:* NOT CARD-ANSWERABLE: 'half the other candidates cite it' cannot be checked from any card, and 'the densest thing in the pool' is a quality verdict.  
*Was:* Written for exactly this cell - installed, daily use, still mediocre - and the densest thing in the pool: half the other candidates cite it, and it is read by AI in full where they are skimmed.  
*Now:* Its who_for is this cell almost word for word - installed, used daily, still getting mediocre results - and it is corrective by design, which its own card says only works once you have your own bad habits to match it against.

**pm|confident** — How I AI: Claude Code for product managers, with Teresa Torres *(reason)*  
*Why:* NOT CARD-ANSWERABLE: 'famous' is not on the card and does no work.  
*Was:* The proof this level needs: a famous non-developer running her own research system in the terminal, demonstrated rather than claimed - the argument the written candidates make, shown working.  
*Now:* The proof this level needs: a non-developer's real terminal setup demonstrated rather than described - and its card is straight that you get the shape of the system and rebuild the files yourself.


### Check 2 — false or misleading as written

**developer|basic** — Prompt engineering best practices for 2026 *(reason)*  
*Why:* FALSE: claimed 'the only AI-read candidate in the pool'; the pool holds two.  
*Was:* The only AI-read candidate in the pool, and the craft layer under every tool pick - a short ordered list of fixes rather than another product tour.  
*Now:* The craft layer under both tool picks above: this is the pool's fix for answers coming out generic, ordered as things to try today rather than another product tour.


### Check 2 — ambiguous enough to read as false

**researcher|basic** — Plan your literature review *(reason)*  
*Why:* AMBIGUOUS: 'the only candidate read in full' reads as false (ten are). The intended narrower claim is now stated explicitly, and is true.  
*Was:* The only candidate read in full that walks a research workflow end to end - and our note adds the caveat the page itself omits, that it never warns about fabricated references.  
*Now:* Ten candidates here have been read in full, and this is the only one of them that walks a research workflow end to end rather than stating a policy or explaining a feature - with our own note adding what the page omits: it never warns about fabricated references.

**researcher|confident** — Connect and integrate your local Zotero library with Claude Cowo *(reason)*  
*Why:* AMBIGUOUS: 'the pool's one AI-read walkthrough' reads as a tier claim; four candidates are ai-reviewed. Rewritten to the distinction that is actually true.  
*Was:* The pool's one AI-read walkthrough of connecting Claude to the library you already trust - and honest that working from your own sources reduces the fabrication risk without removing it.  
*Now:* The only candidate that connects Claude to the reference library you already keep, rather than to a database it searches fresh - and honest that working from your own sources reduces the fabrication risk without removing it.


### Check 1 — the reason did not do the work

**non-technical|never-used** — Claude 101 (DataCamp) *(reason)*  
*Why:* WEAK: led with the publisher constraint ('the slot could not go to Claude 101 without doubling a publisher') rather than with why the reader should open it.  
*Was:* The structured-course slot could not go to Anthropic's own Claude 101 without doubling a publisher, and this one earns it anyway: built explicitly for people who have never opened an AI chat tool, and it ends where the official course does not - at Skills and connectors.  
*Now:* Built explicitly for people who have never opened an AI chat tool, and it ends where the official beginner course stops - with a tour of Projects, Skills and connectors, so one course covers the basics and what comes after them.


### Quality verdicts removed

**business-founder|confident** — Quickly prep for your week *(runner)*  
*Why:* BANNED WORD: 'the best single workflow of the forty-one' is a quality ranking.  
*Was:* The best single workflow of the forty-one, but one workflow cannot beat a policy, a system, or source you can audit.  
*Now:* Strong on its own, but forty-one candidates here run one task each, and the picks are a policy, a system and source you can audit - each of which outlasts a single workflow.

**data-analyst|builder** — Metrics deep-dive to narrative *(runner)*  
*Why:* BANNED WORD: 'the best narrative automation in the pool'.  
*Was:* The best narrative automation in the pool, lost to the ad-hoc queue - which serves every analyst rather than product analysts specifically.  
*Now:* Automates the weekly narrative end to end, but its who_for names product analysts specifically, where the ad-hoc queue pick serves every analyst in this cell.

**data-analyst|confident** — Prompting strategies for financial analysis *(runner)*  
*Why:* BANNED WORD: 'the best prompt-pairs here'.  
*Was:* The best prompt-pairs here, but they need Daloopa and Kensho connectors already licensed - a gate most analysts at this level cannot open.  
*Now:* Built on bad-prompt/good-prompt pairs, which teach quickly - but its card says it assumes Daloopa and Kensho connectors already licensed, a gate most analysts at this level cannot open.

**pm|builder** — PRD from a problem statement *(runner)*  
*Why:* BANNED WORD: 'the best single workflow here'.  
*Was:* The best single workflow here - it interviews you before it writes - but a workflow is not a build, and the Academy slot went to the agent.  
*Now:* It interviews you before it writes, which no other workflow here does - but a workflow is not a build, and the one Academy slot went to the agent.

**pm|confident** — My Simple Claude Cowork System (for normal people) *(runner)*  
*Why:* BANNED WORD: 'the best Cowork-side candidate'.  
*Was:* The best Cowork-side candidate, but the pool's centre of gravity at this level is the move to Claude Code, and there were three slots.  
*Now:* The one Cowork-side candidate that builds a repeatable system rather than showing single wins - but this level's centre of gravity is the move to Claude Code, and there were three slots.

**researcher|confident** — Claude for medical literature search: Avoid hallucinations *(runner)*  
*Why:* BANNED WORD: 'the best citation guardrail in the pool'.  
*Was:* The PMID habit is the best citation guardrail in the pool, but a second article would have collapsed the format spread - and the habit itself is one line you now know.  
*Now:* Its PMID habit - treat any reference without one as invented - is a citation guardrail nothing else here states so plainly, but a second article would have collapsed the format spread, and the habit itself is one line you now have.

**student|never-used** — Claude AI Tutorial for Beginners (Step-by-Step) *(runner)*  
*Why:* BANNED WORD: 'the best generic walkthrough'.  
*Was:* The best generic walkthrough, but Pitt's twenty minutes cover the same start and add Learning Mode and the hallucination warning a student needs on day one.  
*Now:* A calm, current walkthrough, but Pitt's twenty minutes cover the same start and add Learning Mode and the hallucination warning a student needs on day one.

**writer-marketer|basic** — How Anthropic's Growth Marketing team cut ad creation from 30 mi *(runner)*  
*Why:* BANNED WORD: 'the best marketing proof in the pool'.  
*Was:* The best marketing proof in the pool, but it is a case study of their team, not a method for yours.  
*Now:* Real numbers from a real marketing team, but it is a case study of theirs, not a method for yours.


### Mechanical

**designer|confident** — - *(note)*  
*Why:* TYPO: MCC -> MCP.  
*Was:* ... (the ux-writing repo, the Figma MCC docs) ...  
*Now:* ... (the ux-writing repo, the Figma MCP docs) ...


---

## Per-cell verdict

| cell | picks | verdict |
|---|---|---|
| `business-founder\|basic` | 3 | clean |
| `business-founder\|builder` | 3 | clean |
| `business-founder\|confident` | 3 | changed — banned word |
| `business-founder\|never-used` | 3 | clean |
| `data-analyst\|basic` | 3 | clean |
| `data-analyst\|builder` | 3 | changed — banned word |
| `data-analyst\|confident` | 3 | changed — banned word |
| `data-analyst\|never-used` | 3 | clean |
| `designer\|basic` | 3 | clean |
| `designer\|builder` | 3 | clean |
| `designer\|confident` | 3 | changed — typo |
| `designer\|never-used` | 3 | clean |
| `developer\|basic` | 3 | changed — false |
| `developer\|builder` | 3 | clean |
| `developer\|confident` | 3 | changed — not card-answerable |
| `developer\|never-used` | 3 | clean |
| `non-technical\|basic` | 3 | clean |
| `non-technical\|builder` | 2 | clean |
| `non-technical\|confident` | 3 | clean |
| `non-technical\|never-used` | 3 | changed — weak |
| `pm\|basic` | 3 | clean |
| `pm\|builder` | 2 | changed — banned word |
| `pm\|confident` | 3 | changed — banned word; not card-answerable |
| `pm\|never-used` | 3 | clean |
| `researcher\|basic` | 3 | changed — ambiguous; not card-answerable |
| `researcher\|builder` | 3 | clean |
| `researcher\|confident` | 3 | changed — ambiguous; banned word; not card-answerable |
| `researcher\|never-used` | 3 | clean |
| `student\|basic` | 3 | clean |
| `student\|confident` | 3 | changed — not card-answerable |
| `student\|never-used` | 3 | changed — banned word |
| `teacher\|basic` | 3 | clean |
| `teacher\|confident` | 3 | clean |
| `teacher\|never-used` | 3 | clean |
| `writer-marketer\|basic` | 3 | changed — banned word |
| `writer-marketer\|confident` | 3 | clean |
| `writer-marketer\|never-used` | 3 | clean |

23 cells came through unchanged. 14 were touched; none needed a pick dropped or
swapped, so no structural change was made and none is being proposed.

---

## Check 3, and two things it turned up that are not mine to fix

No pick has a `skip_if` or `who_for` that argues against its cell's **level** — that
check came through clean across all 109. Two picks have a `who_for` that names a
**different role** than the cell they appear in. Neither is a bad pick; both are cases
where the catalogue's card copy is narrower than the resource, and the picks feature is
simply the first thing to have shown it.

**`What are Projects?`** — tagged for five roles, and its `who_for` reads *"Researchers
wanting a reusable, context-rich setup per paper/topic."* It is picked in
`business-founder|basic` and `non-technical|basic`, so a business owner is shown a card
that says **For: Researchers**. Projects is genuinely universal; the card is not. Fixing
it means rewriting a `who_for`, which is catalogue copy, so it waits for you.

**`Generate an AI policy`** — `who_for` reads *"Nonprofit leadership drafting AI
governance for the first time."* It is picked in `business-founder|confident`. Same
shape: the resource serves any organisation writing its first AI policy, the card names
one sector. This one carries a single role tag, so the new role-breadth check below
cannot see it — the signature is different.

---

## Check 4 — the 22 justifications

All 22 pass: each states what the shared topic hides rather than merely noting the
clash, usually by naming the distinct subjects. The weakest is
`data-analyst|never-used`, whose middle clause (*"at six candidates the spread is what
it is"*) edges toward a permit — but the sentence that follows does the work (*"The
subjects are a mechanic, a policy answer, and a course"*), so it stands.

Two of the 22 are worth reading as the strongest examples of what a justification is
supposed to do: `designer|basic`, which explains that the topic axis records *surfaces*
and not subjects and then names the three subjects; and `non-technical|builder`, which
explains why the alternatives under other primaries were platform-gated niches rather
than general builds.

---

## Appendix — the Puckett signature, generalised

`scripts/validate-catalogue.py` now prints a warning for any item that tags **3 or more
roles while its card text names only one persona**. It is a warning and never an error,
and it never auto-fixes: breadth is usually correct, and only a person can tell a broad
resource from a mis-tagged one.

First run: **32 items**. Verdicts below.

| item | card names | also tagged | verdict |
|---|---|---|---|
| Introduction to Claude Cowork | business-founder | data-analyst, designer, non-technical, writer-marketer | **worth a look** — who_for names owners and ops; the designer and writer-marketer tags are the thinnest of the five. |
| Get started with Claude Cowork (Help Center) | non-technical | business-founder, teacher | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Reduce hallucinations | data-analyst | researcher, student | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Everyone should be using Claude Code more | non-technical | business-founder, pm | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Why do AI models hallucinate? | non-technical | business-founder, student, teacher | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Everyday Productivity with Claude Cowork | pm | business-founder, non-technical, writer-marketer | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Anthropic Claude for Absolute Beginners | pm | business-founder, non-technical, student, writer-marketer | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Mastering Claude Cowork & AI Agents in 5 hours | business-founder | non-technical, pm | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Stop using Claude like ChatGPT — 10 prompts that unl | writer-marketer | business-founder, non-technical, pm, student, teacher | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| My Claude AI Review (2026): Is It Worth the Hype? | non-technical | business-founder, student, writer-marketer | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| What are Projects? | researcher | business-founder, non-technical, student, teacher | **narrow card** — Projects serves every role; the who_for names researchers only. Same shape as the Puckett fault. Yours to rule on. |
| Getting started with research in Claude.ai | researcher | business-founder, pm, student | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Lesson 1: Introduction to AI Fluency | AI Fluency: F | teacher | non-technical, researcher, student | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Lesson 2B: The 4D Framework | AI Fluency: Framework  | non-technical | pm, researcher, student, teacher | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Lesson 7: Effective prompting techniques (Deep Dive) | non-technical | researcher, student, teacher, writer-marketer | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| AI prompt engineering: A deep dive | developer | data-analyst, pm, researcher, writer-marketer | **worth a look** — a deep dive framed for developers, tagged to five roles. Possibly right, possibly the Puckett shape. |
| Claude AI Tutorial for Beginners (Step-by-Step) | business-founder | non-technical, student, teacher | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Full Claude Tutorial: Beginner to Advanced in 19 Min | pm | business-founder, non-technical, writer-marketer | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| FULL Claude Tutorial For Beginners in 2026! (FULL CO | business-founder | non-technical, writer-marketer | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| NEW: Claude's 'Super Prompts' Will Save You DAYS of  | writer-marketer | business-founder, non-technical, pm, researcher | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| My Simple Claude Cowork System (for normal people) | non-technical | business-founder, pm | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Get started in Claude Cowork in three steps | business-founder | non-technical, pm | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Getting good at Claude: A research-backed curriculum | business-founder | pm, teacher | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| How to select the right effort setting for Claude Co | business-founder | non-technical, pm | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Tokens: why some inputs cost more than others | non-technical | data-analyst, developer | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Writing an AI diligence statement | business-founder | non-technical, pm | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Connect your tools to unlock a smarter, more capable | business-founder | non-technical, pm | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Navigating the Claude desktop app: Chat, Claude Cowo | business-founder | developer, non-technical, pm | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| How context affects Claude's performance and cost | business-founder | developer, non-technical | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Using Claude Design for presentations and slide deck | business-founder | non-technical, pm | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Chart your data in conversation with Claude before y | data-analyst | researcher, student | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |
| Write in my voice | non-technical | business-founder, pm | breadth is right — genuinely general material, and the who_for cannot name ten personas without becoming useless |

So: **3 to look at, 29 cleared as genuine breadth.** The check earns its place by having found `What are Projects?` independently of the reading above — the two agree, which is the first time a heuristic here has confirmed a judgment rather than replaced it.

---

## What this audit did not do

- **No pick was dropped or swapped.** Nothing read badly enough to need it, and that
  would have been a structural change requiring your say-so.
- **No catalogue copy was edited.** The two narrow `who_for` lines above are reported,
  not fixed.
- **No accessibility pass.** Out of scope this round. Nothing in the picks block tripped
  an a11y fault while reading it: the block is a `<section>` with an `aria-label`, the
  heading is a real `<h2>`, and the reason is a `<p>` after the card rather than inside
  the link. Whether the count line still announces correctly with the block inserted
  above it is **not verified** and belongs in that pass.
