# Attack 3 summary — ten roles, one hostile hour each

Ten agents, one per role, two batches of five, no shared context. None of them saw
`scripts/test-search.py`, `data/`, or each other's files. Agreement between files is
therefore independent corroboration rather than consensus.

Site version attacked: `9deb0db`, 6 September 2026. Every claim below traces to a numbered
finding in one of the ten files; a point with no parent was deleted rather than softened.

---

## 1. The one finding that is really one finding

### 1.1 The site cannot be shared. **10 of 10 files.**

Every one of the 588 resource pages serves `<title>Resource — Learn Claude</title>` and
`og:title` with the same value. Browse serves "Browse — Learn Claude" for every filter
combination; Paths serves "Paths — Learn Claude". There is no `og:image`, no `og:url`, no
canonical. The per-page title is written by JavaScript, which no crawler runs.

Ten hostile strangers, given an hour each and no instruction to look at metadata, all found
this. Four of them named it their single worst finding. The designer traced the whole chain
and closed it: **every one of those pages carries a "Copy link" button.** The site built a
share mechanism and did not build the share preview.

> "Five links pasted into a Slack channel unfurl as five identical grey cards. The best
> sentence on the site — the 'Design system drift review' Skip line — arrives looking like
> spam." — designer, §10.1

The reason this is one finding rather than a metadata detail is what the site is. It has no
analytics, no accounts, no ads and no newsletter. **Its only distribution is one person
sending another person a link.** That is the mechanism, and the preview at the end of it
says nothing.

The developer put the cost precisely: *"The whole product is one named judgment about one
named thing, and the unit you send to a colleague has no name in the preview."* (§10.F1)

---

## 2. What most roles hit

### 2.1 Search does not agree with itself. **All 10 ran the test; 7 report it as a fault.**

Every agent asked one of its own questions a second time in different words. Seven came
back with two different shelves for one intent, and the pattern is the same every time: the
wording that fails is the plain-English one.

| role | wording A → rank of the right card | wording B → rank of the same card |
|---|---|---|
| teacher | "is it safe to put **pupil** names into Claude" → **15th** | "…**student** names…" → **3rd** |
| business owner | "is my customer data safe if I paste it into Claude" → **17th** | "does Anthropic train on the files I upload" → **1st** |
| not a coder | "how do I stop claude from making things up" → **1st** | "why does claude give me answers that are not true" → **34th** |
| student | "will my professor know i used claude for my essay" | "can my university detect ai writing in my assignment" — **no overlap in the top three** |
| analyst | "How do I stop Claude getting my numbers wrong" → **11th of 77** | "why does Claude give me a different total every time" → **2nd** |

The teacher isolated the mechanism to one word: **`pupil` returns 0 of 588; `student`
returns 36.** Asked alone the site is honest — *"No match for 'pupil'. Browse everything
instead."* Asked inside a sentence, the other words rescue the query into twenty confident
wrong results with no signal that it failed. (teacher §10.1)

**A reader never learns they picked the bad synonym.** That is the harm, and it is worse
than a miss: a miss sends you elsewhere, a confident wrong answer ends the search.

### 2.2 "Newest first" is not newest first. **6 of 10 report it as a fault; all 10 checked a sort.**

The control sorts on `published` alone and treats every undated row as the beginning of
time, so `Updated` counts for nothing and 442 undated cards sink below every dated one.

- teacher: the most recently updated card, "What are artifacts and how do I use them?"
  (Updated 3 Sep 2026), lands at **62 of 67**.
- researcher: two cards the site *itself* flags "over a year ago, may not match Claude
  today" rank **1st and 2nd**; a card marked Updated 1 Sep 2026 is **last of 16**.
- analyst: "AI prompt engineering: A deep dive" (Published 5 Sep 2024, flagged old) is
  first; "Let Claude use your computer in Cowork" (Updated 2 Sep 2026) is last.

Three agents noted independently that **"Shortest first" is correct**, so the machinery
works and only this label lies. It harms exactly the reader who believed the site's own
warning that Claude changes every few months.

### 2.3 The picks block and the sort control ignore each other. **3 of 10.**

The picks are pinned above the results and are not re-ordered by the sort under them, so
"Shortest first" shows a half-day course in position 2 (pm §10.5) and the designer read the
whole block as outside the control that appears to govern it (§10.4).

### 2.4 The tier badge is undefined on a phone. **7 of 10.**

On a card the badge is a `<span title="…">`. A `title` tooltip opens on hover and nowhere
else — not on tap, not on keyboard focus. "Skimmed" is therefore an undefined word on every
card for every phone reader, on the site's own second pillar. On the resource page it is a
real link, which is why several agents found the inconsistency rather than the absence.

**This is a known, deliberate trade** — see §5 — and Attack 3 is the first field evidence
of what it costs.

### 2.5 Nothing that costs money says what it costs. **8 of 10.**

Four rows site-wide carry a price chip. Every agent that looked at a paid row in its own
role found none: 0 of 5 for the business owner, 0 of 5 for the writer, 0 of 5 in the
analyst's role, the teacher's single paid item, and a top-three **pick** for a non-coder.

The business owner's closing answer is the whole argument: *"A directory that tells me
precisely when to skip a free thing and then goes silent the moment money is involved has
quit at the point I needed it."*

**The cause is a rule, not an oversight** — see §5. What no agent could discover is that
the rule exists.

### 2.6 The home page's attract loop never fills its own sentence. **8 of 10 mention it; 3 measured it.**

The role chips cycle every ~2.5s, and the headline stays literally `I'm a [role] and I've
[level].` The student sampled it across 21 seconds and eight times; the pm sampled
`p.display` eight times. The loop animates the evidence and never delivers the payoff.

### 2.7 The level ladder runs out one rung early for most roles. **7 of 10.**

Not the same complaint as "the catalogue is thin". The complaint is that **answering the
front door honestly is punished**, which Attack 2 also found, and the shape is now sharper:

- teacher at the top level: 1 of 2 cards is a developer doc about building an SVG app.
- student at "used it a lot": 9 items, and the first pick's own line reads *"For: Any
  analyst worried about confidently-wrong output."*
- not a coder at "used it a lot": 12 of 14 non-pick cards need a Mac, a connector, a paid
  data subscription or the reader's tax returns.
- analyst at "built things with it": 7 of 12 are `code`, 7 of 12 are GitHub repos.
- writer at "used it a lot": 13 of 24 are single-recipe marketing and fundraising pages.

The developer is the exception and says so: `developer|builder` is *"59 cards of real
mechanism… genuinely advanced, not a course listing."*

---

## 3. What one role hit that matters anyway

### 3.1 The empty state tells a reader the site has nothing for their job, and it is false. **5 of 10 reached it; 2 chased it.**

`browse.html?role=<any>&checked=reviewed` returns:

> **We have not covered this role yet.** It's on the list. Browse everything instead.

The business owner has 153 resources. The PM has 112. The developer, the site's largest
role, gets the same sentence. The cause is that nothing anywhere is `reviewed` — the top
rung is empty by design — and **the message blames whichever filter is set rather than the
one that emptied the result.** With no role selected, the same empty result correctly says
"Nothing matches all of those."

The most natural move for a sceptic — filter to the highest quality bar — makes the site
falsely deny it serves their profession. (business-founder §10.1, pm §10.1)

### 3.2 A pick reason cites a sentence its own card does not contain. **1 of 10.**

`pm|builder` recommends a $3,000 course partly because *"its own card is straight that
thirteen reviews is thin evidence"*. The words "thirteen", "13" and "review" appear nowhere
on that card, whose actual objection is *"a sales page built on testimonials, hiring
screenshots and countdown urgency"*. (pm §9.1)

This is the same class as Attack 2's M13, where three pick reasons called Anthropic material
non-Anthropic. That fault got a validator; **this variant of it did not**, because the check
looks only for the non-Anthropic claim.

### 3.3 Path pages throw away the `Updated` date, on every path. **1 of 10.**

`paths.js` renders `checked` and the staleness note and never renders `updatedNote`. Attack
2 fixed exactly this on the resource page as M1. **The same bug survived on a third
surface** — and it is the surface built for people who cannot yet judge a resource
themselves. (data-analyst §10.5)

### 3.4 The writer's own path ends on superseded guidance. **1 of 10.**

"Using Claude on work you put your name to" finishes at *"The Ethics of Using AI"* (SPJ),
whose own summary says it was "prompted by the 2023 CNET AI-byline controversy". Its date
line says "No publish date given", so the "over a year ago" warning never fires. Its skip
line says *"predates SPJ's 2026 Code of Ethics revision (see next entry)"* — and the path
page does not render skip lines, there is no next entry on the resource page, and the
current document is in the catalogue **unlinked**. A writer follows the site's own route on
the one subject with legal consequences and finishes on superseded guidance believing it is
current. (writer §10.1)

### 3.5 Cards chipped `free` that are not free. **1 of 10, and it is a vocabulary question.**

16 of 34 cards on the analyst's main shelf carry the `free` chip while naming paid Daloopa,
S&P Global or Kensho subscriptions, invitations or Enterprise plans.
`resource.html?id=r-1e88a43d53` shows chip `free` four lines above *"Before this — Paid
Claude plan"*. `how-we-check.html` never defines what the cost chips mean.
(data-analyst §10.2)

### 3.6 The site's best writer resource is not tagged for a writer. **1 of 10.**

*"Write in my voice"* is result 3 for an unfiltered search and **absent from all 20 results
with `role=writer-marketer` set**. The writer also found *"Analyze fundraising performance"*
carrying a skip line that diagnoses its own mis-filing — *"the page's own category chip says
Marketing, but the actual content is nonprofit development work"* — while still filed under
"a writer". (writer §10.2, §10.3)

### 3.7 Craft faults a designer found and nobody else would. **1 of 10.**

The stretched `::after` card link makes the `For:` and `Skip if:` prose unselectable, so the
site's best sentences cannot be copied. The `<h1>` is a 16 px caption while the 68 px
sentence beside it is a `<p>`. Browse unfiltered renders all 588 cards into a 321,320 px
page — 396 phone screens, no pagination. (designer §10.7, §10.9, §10.6)

---

## 4. Ranked by what it costs a real visitor

| # | Finding | Roles | Kind |
|---|---|---|---|
| 1 | Every shared link previews as an unnamed placeholder, on a site whose only distribution is sharing | 10/10 | **decision** (needs a build step) |
| 2 | Search returns a different shelf for two wordings of one question, silently | 7/10 | decision |
| 3 | The quality filter makes the site falsely deny it serves a role | 5/10 | **mechanical** |
| 4 | "Newest first" ignores every `Updated` date and buries the undated | 6/10 | **mechanical** |
| 5 | The level ladder runs out a rung early for seven roles | 7/10 | decision |
| 6 | Paths drop the `Updated` date — Attack 2's M1 on a third surface | 1/10 | **mechanical** |
| 7 | The tier badge is undefined on a phone | 7/10 | decision (a known trade) |
| 8 | Nothing paid says what it costs | 8/10 | decision (a rule nobody can discover) |
| 9 | A pick reason quotes a sentence its card does not contain | 1/10 | **mechanical** |
| 10 | `free` on rows gated behind a paid subscription | 1/10 | decision (vocabulary) |
| 11 | The writer's path ends on superseded guidance with the current document unlinked | 1/10 | decision |
| 12 | Pick reasons print build machinery — "Rule B removed that something from this pool on 2026-09-06" | 1/10 | **mechanical** |
| 13 | The attract loop never fills its own sentence | 8/10 | **mechanical** |
| 14 | The picks block ignores the sort control above it | 3/10 | decision |
| 15 | The site's best writer resource is invisible under the writer filter | 1/10 | decision |
| 16 | Judgment sentences cannot be selected or copied | 1/10 | decision |
| 17 | Browse unfiltered is 396 phone screens with no pagination | 1/10 | decision |
| 18 | Heading order inverted — `<h1>` is the caption | 1/10 | **mechanical** |

---

## 5. Where the agents were wrong

Three claims are correct as observations and wrong as faults. They are here rather than in
the ranked list because acting on them would make the site worse.

**"No price on the paid rows" is a rule, not an omission.** `ui.js:445` records that a price
is stored only where the page prints the same number for every reader, which rules out every
marketplace that prices by country. Four rows qualify. Eight agents hit the symptom and none
could discover the rule — **which is the real finding**: the rule is right and invisible.

**"The badge is mouse-only" is half true and deliberate.** On a card the meaning is carried
by `aria-describedby` on the title link, so a screen reader hears it; the card keeps its
single focus stop, which seven Attack 2 agents praised by name. A sighted phone reader still
gets nothing. The trade is documented at `ui.js:345` and the cost is now measured.

**"4 roles have no path" is stale — and that one is mine.** The designer checked and found
seven paths. That line was in `PLAN.md`'s "already known" list from Attack 1, and I refreshed
`00-facts.md` for this round and left it. An agent had to correct my own briefing.

---

## 6. Where the ten files disagree

**Is the site's honesty a feature or a shrug?** The developer: naming one DTU researcher plus
Claude, and admitting a person has read zero resources end to end, *"raised my trust rather
than lowering it"*. The writer, whose whole trade is disclosure, wants it on the home page:
burying it three clicks in is *"the same instinct as an 8pt 'assisted by AI' footer"*. Both
read the same page. Neither is wrong.

**Is `builder` honest or a trap?** The developer says it is genuinely advanced and the best
shelf on the site. The analyst says the same level for their role is a developer shelf and
*"the one level I would honestly pick tells me my honest answer was wrong."* The rule that
made `builder` mean building did what it was asked; the supply behind it is uneven by role.

**Does search work?** The developer got something useful in the top three for all five
questions and the same #1 for two wordings. Seven other roles got two different shelves for
one intent. The difference is vocabulary: the developer's words are the catalogue's words.

---

## 7. What ten hostile strangers praised, unprompted

- **The `Skip if:` line.** Named by every role that answered the closing question. The
  business owner would come back "for the `Skip if:` lines and nothing else."
- **The paths' reasons.** Five agents said the paths explain *why* each step is where it is
  and that nothing else does. The non-coder would return for one path and only that.
- **The picks' comparative reasoning.** The designer: reasons that compare rather than
  promote. The student would forward two of three beginner picks to their course.
- **The honesty of the tier ladder**, including the empty top rung, from the developer.
- **The engineering under the interface.** The designer, who was looking for faults: zero
  horizontal overflow, 44 px targets, `:focus-visible` on the card via `:has()`,
  `prefers-reduced-motion`, `forced-colors`.
- **The journal-policy shelf** (researcher) and **the integrity shelf** (student) — two
  independent readers calling one cell the best thing on the site.

---

## 8. The closing answers, in their own words

Every agent was asked: *would you come back to this site, and what one thing would make you?*
Ten answers, verbatim in their files, gathered here.

| role | come back? | the one thing |
|---|---|---|
| not a coder | Yes — for the path, and only that | A second path: "Your second month", for someone with a browser, a work laptop and no permission to install anything |
| student | Once, for the integrity pages | Make the nine items at "used it a lot" actually be for a student with an essay due — or say plainly there are only three and why |
| researcher | Yes, bookmarked — not to search it | Put the path's own reasoning into the text the search reads, then ask the same question two ways and check the same card comes back |
| teacher | Yes, but only to send the beginner cell to colleagues | Make the search say *I don't know* instead of guessing |
| developer | Yes, monthly, bookmarked to one cell | Make the Skip lines finish the sentence "Skip if you…" |
| analyst | Yes, once, "as a raid not a home" | Make `free` mean free |
| pm | Yes, for one page, not the site | Make a pasted link say what the thing is |
| designer | Only if someone pastes a link and the preview makes me click | Give each resource page its own served `<title>`/`og:title`, with the `For:` line as the description |
| business owner | Yes, for the `Skip if:` lines and nothing else | Put the price on the card |
| writer | Yes, for one shelf and the skip lines | Put the AI disclosure on the home page, and a date on everything you recommend |

**Ten yeses, and not one of them is a yes to the site.** Every single answer names a
bookmark, a cell, a page or a shelf — *"a raid not a home"*, *"one page, not the site"*,
*"for the path, and only that"*. Nobody said they would come back to Learn Claude. They said
they would come back to one thing inside it.

**Three of the ten name the same repair** — the pm, the designer and, by implication, every
role that found the share chain: make a pasted link say what it is. That is the first task
for the three real people, and it is not a coincidence that it is also §1.1.

---

## 9. Two lists

### 9a. Mechanical — fixed this round, in one commit

Every one is a wrong label, a dead control, a dropped field, or a contradiction with no
judgment call inside it. Logged individually in the round record.

| # | What | Where |
|---|---|---|
| M1 | `browse.html?role=X&checked=reviewed` says "We have not covered this role yet" | `browse.js` — `anyOtherThanRole()` omits `tiers` |
| M2 | "Newest first" ignores `Updated` and sinks every undated row | `ui.js` — `sortDate` reads `published` only |
| M3 | Path steps drop the `Updated` date — M1 of Attack 2 on a third surface | `paths.js` — renders `fresh.note`, never `fresh.updatedNote` |
| M4 | A pick reason quotes a sentence its card does not contain | `data/picks.json` — `pm|builder` |
| M5 | Pick reasons print internal machinery: "Rule B removed that something from this pool on 2026-09-06" | `data/picks.json` — two reader-facing reasons |
| M6 | The attract loop cycles the chips and never fills the headline | `home.js` |
| M7 | `pupil` returns nothing; `student` returns 36 | `data/synonyms.json` — a missing row |
| M8 | The `<h1>` is a caption and the 68 px sentence is a `<p>` | `index.html` |

### 9b. Decisions — yours, with the evidence

Not touched.

1. **The share chain.** §1.1, ten of ten, four calling it their worst finding, and three
   naming it as the one repair. A per-resource served title needs a build step: one HTML
   file per row, or a pre-render. This is the largest thing in this summary.
2. **Whether search should say "I don't know".** The teacher's closing answer, and
   `how-we-check.html` already promises it. Today a one-word miss is honest and a
   sentence-shaped miss is twenty confident wrong results.
3. **Whether the level ladder should be offered where the catalogue cannot stock it.**
   Attack 2 asked this. Seven roles now, with the shape named per role in §2.7.
4. **Whether the cost chips need a definition, and whether `free` may mean
   "free once you have a paid Claude plan".** §3.5.
5. **Whether the price rule should be visible.** §5. Eight agents hit a symptom whose cause
   is a documented rule none of them could find.
6. **Whether the tier badge's meaning must reach a sighted phone reader**, at the cost of
   the single-focus-stop card. §2.4 and §5.
7. **Whether the picks block should obey the sort control above it.** §2.3.
8. **Whether a path may end on a document its own skip line says is superseded**, when the
   current one is in the catalogue. §3.4.
9. **Whether the role filter is allowed to hide the best answer for that role.** §3.6.
10. **Whether the AI disclosure belongs on the home page.** The writer's argument, and the
    developer's opposite reading, are both in §6.
11. **Whether Browse needs pagination.** 396 phone screens, one role's finding, no reader
    has yet said they scrolled it.
12. **Whether the judgment sentences should be selectable.** The stretched card link is
    deliberate; the cost is that the site's best writing cannot be quoted.

---

## 10. Method and its limits

- Ten agents, two batches of five, each on its own browser tab, no shared context.
- **None of them read `scripts/` or `data/`.** Every one confirms it in its checklist. Every
  search query is therefore a hold-out, and all fifty join `scripts/test-search.py` with the
  verdict its author gave it — see the round record for the suite number before and after.
- Every file has 13/13 sections and a complete checklist.
- The four items deferred from Attack 2 were all tested by all ten: the share preview
  (§1.1), the attract loop (§2.6), the sort semantics (§2.2, §2.3) and paths above beginner
  level (§2.7, and no path exists at `builder` for any role).
- One agent corrected the briefing it was given (§5), which is the method working.
