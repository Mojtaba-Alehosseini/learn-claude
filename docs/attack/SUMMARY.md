# Attack summary — ten roles, 139 findings

Ten agents, one per role, each attacking the live site as that person. Written
2026-08-27 against site version `22e4532`. Every point below cites the file and the
numbered finding it came from, in the form `[04 §9.2]`. A point with no parent was
deleted rather than softened.

**Ten of ten roles came back BADLY SERVED.** Not one agent returned pleased.

Files: `01-non-technical` 16 findings · `02-student` 16 · `03-researcher` 15 ·
`04-teacher` 11 · `05-developer` 12 · `06-data-analyst` 13 · `07-pm` 12 ·
`08-designer` 16 · `09-business-founder` 12 · `10-writer-marketer` 16. Total 139.

---

## 1. What nearly every role hit — structural, not detail

These were found independently. The agents did not see each other's files.

### 1.1 The home page's search box returns zero. Seven of ten roles. — the worst thing here
`[01 §9.15] [02 §9.1] [06 §9.1] [07 §9.1] [08 §9.1] [09 §9.1] [10 §9.1]`

The home page invites a sentence — "Or describe what you want to do…" — and submits it
to `browse.html?q=…`. The ranked index is loaded only from Browse's own `input`
handler, so arriving by that URL never loads it. Browse falls back to an AND-substring
match, which no English sentence survives.

Confirmed by me directly, not only by the agents:

```
"how do I cite Claude"            role=student   -> 0
"I don't know where to start"     role=none      -> 0
"how do I stop students cheating" role=teacher   -> 0
"will it fabricate citations"     role=researcher-> 0
```

The same query typed into Browse returns 9, 4, 23, 17 results depending on role
`[07 §9.1] [08 §9.1]`. One keystroke — a spacebar — turns 0 into the right answer
`[06 §9.1] [10 §9.1]`. The data-analyst measured the blast radius against the project's
own benchmark: **7 of the 9 sentences in `scripts/test-search.py` return 0 through this
path** `[06 §9.1]`.

It then misreports itself. With a role set and a query that failed, the count line
prints **"0 resources for a product manager"** while holding 56, because the empty-state
message is computed without looking at `q` `[07 §9.2] [06 §9.4] [02 §9.12]`. The empty
state advises "browse by role instead" — which is what the visitor was already doing
`[01 §9.8] [02 §9.9]`.

This is the single most expensive fault on the site: it is the primary call to action,
it fails silently, it blames the visitor, and the correct answer is one keystroke away.

### 1.2 The site grades its own checking, and the grade is mostly unearned. Seven of ten.
`[02 §9.7] [03 §9.8] [04 §9.1] [05 §9.1] [06 §9.2] [07 §9.7] [10 §9.11]`

That 0 of 353 are `reviewed` is on the known list. What is not:

- **0 of 78 videos and 0 of 54 courses have been checked past the outline**, catalogue
  wide `[05 §9.1]`. All 37 `previewed` developer videos are free and on YouTube, so
  `how-we-check.html`'s stated excuse — that paid courses cannot be seen inside — covers
  none of them `[05 §9.1]`.
- Every one of the 43 `listed` cards — "Nobody has looked at the content yet" — still
  ships a full set of judgements about that content `[05 §9.4] [02 §9.7]`.
- For the teacher, **all 8** policy and integrity cards are `listed` and 6 of 8 undated
  `[04 §9.1]`. For the writer, 28 of 41 verdicts come from an outline, 1 from nothing,
  0 from a human read `[10 §9.11]`.
- `ui.js` claims in a comment that the tiers were checked, while `notes` — the field
  holding the actual evidence — is never rendered `[06 §9.2] [03 §9.10]`.

The researcher put it most sharply: the site's one differentiator is its checking, and
the home page says "checked by hand" while `how-we-check.html` says otherwise, one click
apart `[03 §9.7]`.

### 1.3 The Paths page has role data and throws it away. Six of ten.
`[01 §9.2] [04 §9.2] [06 §9.7] [07 §9.9] [08 §9.4] [10 §9.8]`

`paths.json` tags every path with `roles`. No JavaScript anywhere reads it
`[04 §9.2] [08 §9.4]`. Consequences, all verified live:

- The four roles with no path are never told so. `paths.html?role=designer` silently
  shows three paths for other people, the first headed "Anyone" `[08 §9.4] [07 §9.9]`.
- The roles that *do* have a path cannot reach it from the two questions they just
  answered `[01 §9.2] [04 §9.2]`. The front door never mentions paths at all
  `[05 §9.9]`.
- Worse, the paths are not built from the roles they name. Both paths naming a student
  contain **0 of 6 and 0 of 5** steps tagged `student` `[02 §9.2]`. Step 1 of the
  researcher path is tagged `data-analyst` only `[03 §9.6] [01 §9.9]`. Four of six steps
  in the founder's path are tagged for other roles `[09 §9.5]`. 1 of 17 path steps
  carries the writer's tag `[10 §9.8]`.

So "has a path: yes" is true in the data and invisible, or wrong, on the site.

### 1.4 The catalogue contains duplicates, and the pipeline cannot see them. Six of ten.
`[01 §9.16] [02 §9.15] [03 §9.5] [05 §9.2] [09 §9.3] [10 §9.5]`

De-duplication is by normalised URL, so the same course harvested from two domains
survives as two entries `[03 §9.5]`. Live: `academy.claude.com` and
`anthropic.skilljar.com` both carry "Claude Code 101", one chipped "one hour", one "a
half day", **both claiming to be step 1 of the same path** `[05 §9.2]`. Because the
build picked the `half-day` row, the developer path's advertised "about 6 hours" would
have read "about 3 hours" had it picked the other identical row `[05 §9.2]`.

"Getting started with Claude in Excel" exists twice with *opposite cost answers* — one
`subscription`, one `free` — and the founder is shown the free one `[09 §9.3]`. Where a
duplicate touches the researcher, the researcher gets the worse copy every time
`[03 §9.5]`.

My own catalogue validator does not catch any of this: it checks path → item, never
item → path, and de-dupes on URL only.

### 1.5 42 KB of the best writing on the site is downloaded by every visitor and never shown. Six of ten.
`[01 §9.14] [03 §9.10] [04 §9.8] [06 §9.3] [07 §9.4] [08 §9.10]`

The `notes` field is shipped to every browser and rendered by nothing `[06 §9.3]`. It
holds what the site most needs to say:

- the security instruction *"Use read-only/least-privilege role. Replaces the archived,
  vulnerable @modelcontextprotocol/server-postgres"* — on a card that is tier `listed`
  and asks for production database credentials `[06 §9.2]`
- the caution *"CAUTION: some content promotes making AI text 'pass' as human"*
  `[03 §9.10]`
- **the prices.** 11 of 13 paid PM resources show no price anywhere on the site, and the
  prices are sitting in `notes` `[07 §9.4] [09 §9.8]`
- exact runtimes, thrown away for four coarse buckets `[06 §9.13] [08 §9.10]`

### 1.6 Role tags are wrong in both directions. Five of ten.
`[01 §9.12] [02 §9.8] [05 §9.11] [08 §9.8] [09 §9.9]`

29 of 54 founder `For:` lines never mention anyone who runs anything `[09 §9.9]`. 20 of
56 PM lines never name a product manager and 3 name a different job `[07 §9.10]`. 8 of
47 teacher cards open `For:` with "A student" `[04 §9.5]`. 11 of 41 researcher cards
address somebody else `[03 §9.3]`. A Stripe designer's shader podcast sits on the
teacher's "used it a lot" shelf `[04 §9.6]`.

And in the other direction, the material a role needs is locked away from it: both
academic-integrity resources are `student`-only, unreachable from the teacher filter
`[04 §9.2]`; all four resources on disclosing AI use exclude the writer `[10 §9.4]`;
both pricing pages are `business-founder`-only `[01 §9.8] [02 §9.3]`.

### 1.7 Publisher names are machine-mangled. Five of ten.
`[02 §9.5] [04 §9.10] [06 §9.11] [09 §9.7] [10 §9.9]`

Live on resource pages: **"Open on Pl"**, **"Open on Vc"**, **"Found through To"**,
"Unesco", "Eu", "Gov", "Aiassessmentscale", "Jhu". Nine of the writer's publishers are
domain slugs and one is a top-level domain `[10 §9.9]`. This breaks a rule stated in
`ui.js` itself, across 61 of 353 cards `[09 §9.7]`.

---

## 2. Found by one role, severe enough to matter anyway

### 2.1 An unsourced allegation against a named, real academic — the most urgent item here
`[03 §9.2]`

A catalogue entry carries an integrity allegation against a named individual — *"he has
promoted AI-'humanizer' tricks to defeat AI detection"* — on an entry tiered `listed`,
meaning nobody has opened the source. The same page simultaneously prints "What it
teaches" bullets and "Nobody has looked at the content yet."

The search ranks it **#1** for "systematic literature review", 54% clear of second place
`[03 §9.2]`. It is published, it names a person, and no human verified it. Ranked first
here not by visitor cost but because it is the only finding that can produce a letter.

### 2.2 Every link the site publishes previews as "Resource — Learn Claude"
`[08 §9.5]`

All 353 resource pages ship the same `og:title`, no `og:image`, and no `<noscript>`.
`browse.html?role=designer` serves 4,189 bytes in which the word "designer" occurs zero
times. A directory whose only growth engine is people sharing links has disabled the
preview on every page it owns.

### 2.3 Eight cards claim to be steps in paths they are not in
`[01 §9.3] [05 §9.3]`

Verified live: `resource.html?id=r-3b409df1d4` renders "This is step 1 of 6 in
first-week" — printing the raw internal slug — and links to a path whose six steps do
not include it `[05 §9.3]`. One card renders two false blocks at once `[01 §9.3]`. Cause
is a `|| x.paths` fallback in `ui.js` resurrecting a stale field `[01 §9.3]`.

### 2.4 `Skip if:` was written twice, by two hands, and never reconciled
`[06 §9.5] [10 §9.6]`

Two agents found this by different methods and agree. Split on the `checked` date: items
checked 19 Aug have a median `Skip if:` of 38 characters and tautologies like *"You
don't use R."*; items checked 20–22 Aug run 115–169 characters with real reasons
`[06 §9.5]`. The writer confirmed it by **punctuation** — 18 Aug cards use em dashes and
never open with "Skip if", 22 Aug cards use spaced hyphens and always do; site-wide it
is 77 em dash against 84 spaced hyphen `[10 §9.6]`.

Related and visible: 16 of 41 student cards and 18 of 41 writer cards render as
**"Skip if: Skip if …"** because the stored text repeats the label `[02 §9.6] [10 §9.7]`.

### 2.5 The filter grid dead-ends 96% of the time on the biggest role
`[05 §9.6]`

94 resources and six filter axes, and 96.2% of combinations return nothing `[05 §9.6]`.
Four filter chips are dead ends for the founder `[09 §9.10]`, two for the data-analyst
`[06 §9.12]`. There is no way to filter by how well something was checked — the site's
own differentiator is not an axis `[03 §9.12]`.

### 2.6 A finished event is still on sale as a course
`[09 §9.6]`

An SBA webinar dated 5 August 2026 is listed as something you can take. Its URL returns
200, so "0 dead links" never catches it.

### 2.7 The topic vocabulary cannot express a teacher's job
`[04 §9.7]`

Eight topics exist. None can express academic integrity or classroom policy. 25 of the
teacher's 47 cards fall into `safety`, which is doing all the work `[04 §9.7]`.

### 2.8 The role named `writer-marketer` has nothing for a marketer
`[10 §9.2]`

Across all 353: `content marketing` 0, `email marketing` 0, `press release` 0,
`search engine` 0, `seo` 2 — and 0 on the writer's own shelf.

### 2.9 "What it teaches" is raw lowercase model output on all 353 pages
`[07 §9.5] [10 §9.15]`

The first block a visitor reads on every resource page. Live: *"build and ship ai
products using claude code"*; `CLAUDE.md` rendered as *"write an effective compact
claude md file"*. 116 of 116 bullets on the writer's shelf start lowercase
`[10 §9.15]`.

---

## 3. Ranked by what it costs a real visitor

Not by how easy it is to fix.

| # | Finding | Roles | Parent |
|---|---|---|---|
| 1 | Home-page search returns 0 and blames the visitor | 7/10 | `[02 §9.1]` +6 |
| 2 | Verdicts published for content nobody opened | 7/10 | `[05 §9.1]` +6 |
| 3 | Paths unreachable, or built from other roles' steps | 6/10 | `[02 §9.2]` +5 |
| 4 | Named-individual allegation, unverified, ranked #1 | 1/10 | `[03 §9.2]` |
| 5 | Duplicates with contradictory cost and duration | 6/10 | `[05 §9.2]` +5 |
| 6 | Prices exist and are never shown | 3/10 | `[07 §9.4]` +2 |
| 7 | `free` chip is false where a paid plan is required | 3/10 | `[01 §9.1]` +2 |
| 8 | Eight cards claim false path membership | 2/10 | `[05 §9.3]` |
| 9 | Role tags wrong in both directions | 5/10 | `[09 §9.9]` +4 |
| 10 | Every shared link previews as "Resource — Learn Claude" | 1/10 | `[08 §9.5]` |
| 11 | Publisher names machine-mangled, 61 of 353 | 5/10 | `[09 §9.7]` +4 |
| 12 | Time labels are upper bounds printed as fact | 3/10 | `[08 §9.3]` +2 |
| 13 | Phone: 64–67% of first screen is chrome | 3/10 | `[07 §9.11]` +2 |

---

## 4. Where the ten files disagree — named, not averaged

### 4.1 The search box that collapses after both answers
`[04 §9.11] [05 §9.8]`

Two agents independently filed this as a defect: "Answering both questions removes the
search box" `[04 §9.11]`, "The front door deletes the search box for answering its own
questions" `[05 §9.8]`.

That behaviour was added deliberately, this week, on Morteza's instruction. The agents
did not know that. Their objection stands on its own terms and is worth reading: they
argue the free-text box is the escape hatch for exactly the person the two questions
failed. It interacts badly with §1.1 — the box is the *only* producer of `?q=` URLs, and
those URLs return 0. **This is a genuine design disagreement, not a bug report.**

### 4.2 Whether `Skip if:` should outrank `For:` on a card
`[08 §9.6]`

The designer filed the card typography as a defect: `Skip if:` renders 20px black serif
while `For:` renders 16px grey sans, so "the rejection outranks the recommendation on
every card" `[08 §9.6]`. The stylesheet says this is intentional — `site.css` calls
`.card-skip` "The reason the site exists… If this ever reads as a footnote, the card is
wrong." Agent and author disagree about the product, not the code.

### 4.3 A number in the shipped code has drifted from the data
`[05 §9.12] [09 §9.12]`

`ui.js` states in a comment that "176 of 353 resources publish no date". The measured
figure in `00-facts.md`, and in the live data, is **171**. Two agents caught it.

### 4.4 My own tooling was wrong, and one agent caught it
`[09 §9.11]`

The founder reported that `docs/attack/role-view.py` — the helper I wrote and gave to
all ten agents — does not reproduce the site's card order exactly. **Correct.** I
verified it: my Python sorts titles by ASCII, the live site uses `localeCompare`.

Extent, measured: card #1 is right for 9 of 10 roles, with first divergence at positions
5–31. For **student it diverges at position 1** — the live site shows "Acknowledging AI
tools and technologies" first, my helper showed "AI Student Research Guide". Same cards,
same tier grouping, alphabetical neighbours swapped.

No finding in any of the ten files rests on a position-1 claim, so nothing above is
invalidated. But agents' "position N" statements deeper in a list may be off by a few
places, and that is my error, not theirs.

---

## 5. What is genuinely good — do not refactor this away

Every agent was told to be brief here, and every agent still found something.

- **`Skip if:` is the right idea and no competitor has it.** Where it was written
  properly — the 20–22 August generation — it is the most useful line on the card
  `[06 §9.5] [10 §9.6]`.
- **The tier vocabulary is honest in design.** "Nobody has looked at the content yet" is
  a sentence almost no directory would print. The problem is that the grades are
  unearned, not that the scale is wrong `[05 §9.1] [03 §9.7]`.
- **"No publish date given" refuses to invent a date** `[08 §9.16] [10 §9.14]`.
- **The count is honest before you click.** All five numbers the non-technical agent
  checked matched ground truth exactly, including the zero `[01 §11]`.
- **0 dead links across 353** `[09 §9.6]` — though two agents note this catches neither
  a finished event nor a duplicate, both of which return 200.
- **The two-question front door is genuinely fast.** "Four clicks, a live count before I
  commit, and a sentence instead of a form. It is the best-written thing on the site"
  `[10 §11]`.
- **Somebody curated well at least once.** The writer found four correct choices in a
  row on AI-detection anxiety — "How to Stop Claude Writing Like an AI",
  "Wikipedia:Signs of AI writing", "How to Spot AI Writing, According to Wikipedia" —
  with search returning the right one first `[10 §11]`. When the catalogue is good it is
  very good, which is what makes §2.4 worth fixing rather than abandoning.
- **The ranked engine itself is fine.** 59.4 for the right answer on a real sentence; the
  engine is not the problem, the trigger is `[10 §11]` — see §1.1.

---

## 6. Decisions that are Morteza's, not mine

1. **The search box collapse** (§4.1). Two agents call it a defect; it was your call
   this week. Their argument is about the escape hatch, and it deserves an answer rather
   than a revert.
2. **Whether `Skip if:` should dominate the card** (§4.2). The stylesheet states an
   intent; a designer disagrees with it. That is a product question.
3. **The named-individual allegation** (§2.1). Whether it is defensible, sourced, or
   should come down is not a call I will make for you. It is live now.
4. **Whether ten roles is too many.** Six roles have fewer than 50 resources and four
   have no path. No agent recommended cutting roles; several observed that thin roles
   are filled by relabelling other roles' content `[08 §9.2] [07 §9.6] [09 §9.9]`.
5. **Whether "a writer" should be split from "a marketer"** `[10 §9.2] [10 §9.3]`.

---

## 7. Method and its limits

- Ten agents, run in two batches of five, no shared context. Agreement between files is
  therefore independent corroboration, not consensus.
- Every agent was given the six already-known items and told not to claim them as new.
  All ten found at least one thing outside that list.
- The deployed `data/items.js` was verified **byte-identical** to `data/items.json`
  before the run, and every role count matched `00-facts.md` exactly. Quoting the local
  data is quoting the live site.
- Browser access was contended across five concurrent agents. Each file states how it
  checked; several fell back to `curl` plus the shipped JavaScript, which is why so many
  findings cite `browse.js` line numbers rather than screenshots.
- The card-order caveat in §4.4 applies to every "position N" claim in the ten files.
- Gate applied before this summary was written: all ten files have 11/11 sections, a
  complete checklist, at least 11 numbered findings, and zero hedge words outside
  section 11.
- Traceability: 157 citations in this file resolve to a numbered finding, 0 broken, all
  ten files cited. Points in §5 cite `§11` rather than a finding number, because the
  plan does not number section 11 — those parents are locatable but unnumbered, and that
  is stated here rather than hidden by dropping the section.
