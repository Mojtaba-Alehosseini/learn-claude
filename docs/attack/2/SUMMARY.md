# Attack 2 summary — ten roles, one hostile hour each

Ten agents, one per role, each visiting the **live site** as that person at all four levels.
Written 2026-09-05 against 635 resources, 37 pick cells, 7 paths. They did not see each
other's files, this brief, the data model, or Attack 1.

Attack 1 ran 2026-08-27 against 353 resources and no picks. `REGRESSION.md` re-tests what it
found. This file is what is true now.

Files: `01-non-technical` · `02-student` · `03-researcher` · `04-teacher` · `05-developer` ·
`06-data-analyst` · `07-pm` · `08-designer` · `09-business-founder` · `10-writer-marketer`.

**Ten of ten came back with the same finding at number one or number two.** That has not
happened before.

---

## 1. The one finding that is really one finding

### 1.1 A tier that says nobody looked, above a paragraph describing what is inside. **8 of 10 roles.**
`[01 §12.1] [02 §12.1] [03 §12.1] [04 §12.1] [05 §12.2] [07 S3] [08 §12.1] [10 §12.1]`

The badge and its printed definition:

> **Found only.** We found it and sorted it. **Nobody has looked at the content yet.**

And on the same page, every time. Measured: **36 of 36** `listed` items carry both a `who_for`
and a `skip_if`, with a median summary of 214 characters and a three-item "What it teaches"
list. Not one is a bare link.

What the agents quoted, from six different cards:

- *"The Melbourne, Warwick or Tulane pages give you more usable templates for that."* — a
  comparison against three other named institutional pages `[03]`
- *"Nothing in it visibly tells you to check Claude's arithmetic, which for a project built on
  sales numbers is the omission that matters. **Ninety guided minutes**."* `[01] [05] [08]`
- *"kept current through August 2026"* and *"This adds little beyond a summary and local policy
  links"* `[02]`
- *"at its own submission volume the false-positive rate would have wrongly flagged thousands
  of papers a year, and Turnitin would not explain how the score is produced"* `[04]`
- *"the recording is labelled 2025"* — on a card whose date line says **"No publish date
  given"** `[07]`
- *"This is a lookup reference, not a tutorial, **and it is enormous.**"* `[05] [10]`

You cannot know a course runs ninety minutes, or omits an arithmetic warning, or is enormous,
without opening it.

**Eight roles reached the same conclusion independently, and it is the conclusion that
matters:** once one badge is provably false, the other two stop meaning anything. The
researcher: *"no badge on the site means anything, including the 501 that say Skimmed."* The
writer: *"once the badges are gone, this is a list of links — which is precisely what the site
says it exists to not be."* The designer: *"I have no way to tell which notes came from reading
and which came from a model filling in a template."*

Six of the ten named this as **the one thing that would make them leave**.

Attack 1 found it at 43 of 43 `[05 §9.4] [02 §9.7]`. It is now 36 of 36. Nothing about it has
changed.

---

## 2. What most roles hit

### 2.1 The site's three trust claims disagree with the site's own data. **10 of 10.**
`[01 §12.2] [02 §12.9] [03 §12.11-12] [04 §12.10] [05 §12.1] [06 §11] [07 S1] [08 §12.2] [09 §12.3] [10 §12.2-3]`

Three separate sentences, three separate places, all refuted by the numbers the site itself
generates:

| Where | Claim | What the data says |
|---|---|---|
| `index.html`, first screen | **"635 resources, checked by hand."** | 0 at the tier defined as "a person checked the notes" |
| `how-we-check.html`, first line | **"We would rather have 70 resources we can vouch for than 700 we cannot."** | 635 shipped, 0 vouchable by its own top-tier definition |
| `how-we-check.html`, "What we do" | **"We find material, read it, and write two things"** | false for 537 of 635 (85%) |
| `how-we-check.html`, "What we will not do" | **"We do not list something we cannot open."** | six lines above *"Paid courses usually stop here, because we cannot see inside them"* — 501 items |

The developer put the structural point best: the counts on that page are **generated**, so the
page now automatically publishes its own contradiction and refreshes it on every build. That is
a good instrument pointed at a sentence nobody updated.

Every role that read `how-we-check.html` came away trusting the site **less**, and several said
so with regret — the page is well written and unusually candid everywhere else. The
certification paragraph was praised by five agents by name.

### 2.2 Search fails plain-English questions. **10 of 10.**
Every agent, sections 8 of every file.

Fifty-seven queries, ten visitors, each in their own words - the count is the row count
of `SUITE` in `scripts/test-search.py`, where all 57 now live. Scores the agents gave
themselves:

| Role | Useful top-three slots |
|---|---|
| researcher | 1 clean of 5 |
| student | 5 of 15 |
| writer | 5 of 15 |
| data-analyst | 2 of 5 queries clean |
| developer | 2 of 5 |
| teacher | 1 of 5 |
| non-technical | 5 of 15 |
| designer | 3 of 7 |
| PM | 1 clean, 2 partial, 2 failed |
| business-founder | 1 of 5 clean, 1 broken before it ran |

The failures have five distinct named causes, and they are not the August cause:

1. **No stemming.** `hallucinated references` and `hallucinations` return **disjoint** answer
   sets; `Reduce hallucinations` is #1 for one and absent from the other `[03]`.
2. **No synonyms.** `marking essays` -> 2 results, both for students. `grading` -> 3 results,
   #1 is *"Demystifying evals for AI agents"* `[04]`.
3. **No British spelling.** `prioritisation` -> 1 result, `prioritization` -> 1 different
   result, neither about prioritisation `[07]`.
4. **No tie-break.** `claude code hooks` -> top three all score **34.64**, so the order is
   file order; the real hooks tutorial is 5th `[05]`.
5. **`skip_if` and `who_for` are not in the index.** `stop claude inventing pixel values` does
   not return the card containing the phrase "invented pixel values" `[08]`.

And the two that sting most: `em dash` -> **0 results** on a site stocking four resources about
AI writing tells `[10]`. `typography` -> **0 results** on a design directory `[08]`.

Repeatedly the site **owns the right answer and cannot find it**: "What are Projects?" is
absent from 33 results for *make claude remember my stuff* — while being the site's own pick
for that reader and step 4 of its only beginner path `[01]`.

### 2.3 The detail page shows less than the card that linked to it. **5 of 10.**
`[03 §12.6] [04 §12.3-4] [06 §12.3] [08 §12.7] [09 §12.2, 12.4]`

Confirmed in source. `resource.js` prints `item.published` directly and never reads
`fresh.note` or `fresh.updatedNote`, so:

- **96 items** carry an `updated` date the card shows and the page does not. For **44** of them
  it is the only date evidence they have, so the detail page falls back to "No publish date
  given" and nothing else.
- **17 items** carry the card's *"Published over a year ago — may not match Claude today"*
  warning, which the page silently drops.

Neither view ever shows both the date and the verdict. And the page that loses the warning is
the one produced by the site's own **Copy link** button.

### 2.4 The staleness warning replaces the date it is warning about. **6 of 10.**
`[01 §12.7] [02 §12.4] [05 §12.9] [06 §12.10] [07 S2] [09 §12.10]`

17 cards print the phrase *instead of* the number. Behind it: **16 Aug 2023**, 5 Sep 2024, 19
Dec 2024, 22 May 2025, 12 Jun 2025. A three-year-old document and a fifteen-month-old document
get the identical string, against a home page promising *"We show the date."*

One card manages both at once — *"Published over a year ago"* directly above *"Updated 1 Aug
2025"*, which is the date it is hiding `[02]`.

### 2.5 Answering both front-door questions honestly is punished. **9 of 10.**
`[01 §12.9] [02 §12.3] [03 §2] [04 §12.2] [05 §17] [07 S3] [08 §12.13] [09 §12.8] [10 §12.7]`

| Role at "built things with it" | Results | Picks |
|---|---|---|
| student | **0** | none |
| teacher | **2** | none |
| writer | **3** | none |
| non-technical | 8 | two |
| PM | 58 | **two** |

Three of forty cells have no picks block and **the block simply is not there** — no heading, no
sentence, no explanation. The page changes shape and says nothing. Meanwhile the 0-result state
*does* speak, well: *"We have nothing for this combination yet. It's on the list."*

The teacher's two results include a medical-anatomy app demo. The writer's three are two GitHub
repos and a personal blog, all Skimmed, two undated. The level filter is exact match, so
answering the top level *hides* the 63 other writer resources rather than ranking them.

Both two-pick cells were picked on **31 Aug**, the oldest date in `picks.json`; every other cell
is 4-5 Sep. *"That is not restraint, that is an unfinished pass with a heading that adapts to
hide it."* `[07]`

### 2.6 The role filter returns other people's jobs. **6 of 10.**
`[01 §12.5] [02 §12.6] [03 §12.4] [05 §12.5] [06 §12.11] [07 S1]`

Counted by hand, from the cards' own `For:` lines:

- **PM|builder: 12 of 58** name a different job — *"Sales reps prepping for a call"*, *"In-house
  counsel or legal ops triaging a high volume of standard NDAs"*, *"Litigation or research
  attorneys"*, *"Recruiters or hiring managers assembling an offer package"*, *"Buy-side equity
  research analysts"*.
- **non-technical|never-used: 21 of 68** — five US healthcare-coding connectors (ICD-10,
  Medicare Part B, NPI registry, CLEAR biometric ID), eight nonprofit fundraising pages, one
  Blender connector.
- **researcher|never-used: 9 of 21** are Anthropic Academy *clinical* connector pages.
- **developer|never-used: 2 of the 4 non-pick results** are a 3D-modelling connector and a
  medical-billing connector.
- **student: 10 of 79**, four of them inside the ten-item "used it a lot" cell.

And the other direction, unchanged since August: the Vanderbilt page on AI-detector false
accusations — whose own note singles out **non-native English writers** — is `roles:
["teacher"]` and unreachable from the student filter `[02]`.

### 2.7 "about 81 minutes". **10 of 10.**

Every single agent found it. `build-paths.py` prints the raw integer below 90 minutes and rounds
to hours above. Next to "about 4 hours" and "about 2 hours" it reads, in the designer's words,
*"as a script output on a page selling human judgment."*

### 2.8 The keyboard path to the first result. **7 of 10.**
`[01 §10] [02 §10] [03 §10] [04 §12.8] [07 §10] [08 §10] [10 §10]`

Between **24 and 30 tab stops** before result #1, because `<main id="main">` opens with the
whole filter rail. The skip link saves four stops and leaves 24 filter controls in the way.
There is no "skip to results".

The teacher found the sharper version: **the skip link does not move focus at all.** `<main>`
has no `tabindex="-1"`, so the fragment scrolls and `document.activeElement` falls back to
`<body>` — the next Tab starts over at the top of the document. Reproduced on index, browse and
resource. Confirmed in source: none of the five pages sets it.

The designer found the third: **the focus ring on every filter button is clipped by its own
scrolling rail** and renders as two loose horizontal lines, one of them under the *previous*
label.

Everything else in the accessibility work was praised, repeatedly and specifically, by seven
agents: the `role="checkbox"`/`aria-checked` filters, the `aria-live` count, the whole-card
focus ring, the forced-colors block, the properly built modal filter sheet with Escape and
focus return, and `aria-labelledby` on the picks region with "Everything else" deliberately
outside it.

### 2.9 The picks block: real judgment, undermined by three things. **10 of 10 tested it.**

Every agent that could tested whether the picks are the top three rows. **Every one found they
are not**, by a different method:

- 36 of 37 cells differ from the default sort `[06]`
- one pick sits at **position 78 of 79** `[09]`; another at **23 of 44** `[02]`
- overlap with the default top three: 1/3, 1/3, 2/3 `[04]`

The reasons were the most-praised writing on the site. *"Three journal-policy candidates, and
this is the only one not tied to a single publisher"* `[03]`. *"The decision layer the pool's
twelve single-feature intros each lack"* `[05]`. *"the two picks above are the why-safe and the
how-fast, this is the what"* `[09]`.

The three faults:

**(a) The reasons state facts the cards deny.** `[05 §12.3]` — the strongest single new finding
of the round.

> *"The deepest **non-Anthropic** material in the pool ... by the SDK's own engineer"* — card
> title: **"Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic"**
> *"the pool's **strongest non-Anthropic voice**"* — card author: **"Created by Anthropic,
> adapted for the DataCamp platform"** (used in two cells)

Systematic, not a typo: `official: false` means "not on an Anthropic domain" and is being read
as "not from Anthropic." Independence is the exact axis these sentences sell.

**(b) The reason sometimes paraphrases the card's own Skip-if, four centimetres above it.**
`[01 §12.8] [08 §12.6]` — 15 of 109 picks share three or more verbatim six-word runs with the
same card's notes; one shares eleven.

**(c) The picks contradict the card under them.** `[03 §12.8] [07 S1]` — pick 2 for a researcher
is sold as *"the retention answer from the company itself"* above a card reading *"If your data
sits on Team, Enterprise or the API ... **this is the wrong page**."* Pick 2 for a PM is one of
only two "start here" items and its own `who_for` reads *"Engineering teams tired of
re-answering the same onboarding and ownership questions."*

On the label: **"picked by AI" raised trust for four agents and lowered it for three.** The
split is clean and worth reading. Raised: it stops you imagining a curator who is not there
`[02]`, and it is consistent with the badges `[06]`. Lowered: it reads as a byline slot on a
site with no other byline, so the unlabelled prose implies a person who does not exist `[10]`;
and all 37 cells are `picked_by: "ai"`, so it implies a contrast the data does not have `[09]`.

Also measured: **all 109 picks are `previewed` or `ai-reviewed`. Zero are read in full.** 70 of
109 have no publication date `[03]`.

### 2.10 The picks disappear the moment anyone asks a question. **2 of 10, and structural.**
`[09 §12.7] [10 §12.5]`

`picksCell()` returns `null` when `q` is non-empty or any extra filter is set. So the site's
best editorial work is invisible to anyone who searches, or who clicks "15 min" because they
have fifteen minutes. No message; it just evaporates.

---

## 3. Ranked by what it costs a real visitor

| # | Finding | Roles | Kind |
|---|---|---|---|
| 1 | Unread tiers carry full verdicts about the content | 8/10 | decision |
| 2 | "Checked by hand" / "70 rather than 700" / "we read it" all false | 10/10 | decision |
| 3 | Search fails plain-English questions, five named causes | 10/10 | decision |
| 4 | Answering the top level honestly returns 0-3 results and no picks | 9/10 | decision |
| 5 | The detail page drops the Updated date and the staleness warning | 5/10 | **mechanical** |
| 6 | The role filter returns other people's jobs | 6/10 | decision |
| 7 | The staleness warning replaces the date | 6/10 | decision |
| 8 | Pick reasons call Anthropic material non-Anthropic | 1/10 | **mechanical** |
| 9 | 24-30 tabs to the first result; the skip link moves no focus | 7/10 | **mechanical** (the skip link) / decision (the rail) |
| 10 | Picks vanish on any search or third filter, silently | 2/10 | decision |
| 11 | `status: "outdated"` is in the data and never rendered | 1/10 | **mechanical** |
| 12 | Time chips contradict the card's own text and break the filter | 3/10 | decision |
| 13 | "Skip if:" repeats its own label on 157 cards | 3/10 | **mechanical** |
| 14 | "about 81 minutes" | 10/10 | **mechanical** |
| 15 | Publisher names still slugs: "Und", "Master", `qwe.edu.pl` | 2/10 | decision (new rows keep arriving) |
| 16 | og:title is "Resource — Learn Claude" on all 635 | 2/10 | decision (needs a build step) |
| 17 | Sitemap lists 353 of 635, and 35 of those ids are dead | 1/10 | **mechanical** |
| 18 | "Back to browse" discards the filters | 2/10 | **mechanical** |
| 19 | The 0-result dead end has no clickable escape | 2/10 | **mechanical** |
| 20 | "Try fewer words" advised for a one-word query | 2/10 | **mechanical** |
| 21 | Tier badge explanation is a mouse-only tooltip | 2/10 | decision |
| 22 | No tier filter | 3/10 | decision |
| 23 | Lowercase "Claude code" in 164 bullets on 112 pages | 4/10 | decision (the map is single-word) |
| 24 | The home attract loop reads as a selection already made | 4/10 | decision |
| 25 | "Best checked first" degrades to alphabetical / is overridden by relevance | 3/10 | decision |
| 26 | "98 read by ai" lowercased in the trust sentence | 3/10 | **mechanical** |
| 27 | Path signpost is a dead `<span>` on the card, a link on the page | 1/10 | **mechanical** |
| 28 | "Browse 1 Claude resources" never singularises | 1/10 | **mechanical** |
| 29 | Prices exist and are never a field ($995 buried in a skip_if) | 3/10 | decision |
| 30 | No path above beginner level; none for a teacher or a business | 4/10 | decision |

---

## 4. Two lists

### 4a. Mechanical — fixed this round, in one commit

Every one is a wrong label, a dead control, a dropped field, or a contradiction with no
judgment call inside it.

| # | What | Where | Change |
|---|---|---|---|
| M1 | The detail page drops the `Updated` date (96 items) and the "over a year ago" warning (17 items) that the card shows | `assets/js/resource.js` | render `fresh.updatedNote` and `fresh.note` alongside the published date |
| M2 | `status: "outdated"` is set on 3 items and only `"dead"` is rendered | `assets/js/resource.js` | render an advisory for `outdated` |
| M3 | "about 81 minutes" | `scripts/build-paths.py` | round below 90 minutes the same way as above it |
| M4 | "98 read by ai" — the tier label lowercased inside the trust sentence | `how-we-check.html` | stop lowercasing a proper label |
| M5 | Skip link scrolls but moves no focus, on all five pages | `*.html` | `tabindex="-1"` on `<main id="main">` |
| M6 | "Back to browse" throws the reader's filters away | `assets/js/resource.js` | carry the referring browse query when it is one of ours |
| M7 | The 0-result dead end has no clickable way out | `assets/js/browse.js` | make "browse everything" a link |
| M8 | "Try fewer words" advised to someone who typed one word | `assets/js/browse.js` | only advise it when there is more than one word |
| M9 | "Browse 1 Claude resources" | `assets/js/browse.js` | singularise |
| M10 | The path signpost is a `<span>` on the card and a link on the resource page | `assets/js/ui.js` | make it the same link in both places |
| M11 | `Skip if:` repeats its own label on 157 of 635 cards | `data/items.json` | prefix stripped on all 157; every change in [MECHANICAL-LOG.md](MECHANICAL-LOG.md) |
| M12 | `sitemap.xml` lists 353 of 635 resources and 35 ids that no longer exist | new `scripts/build-sitemap.py`, wired into `build.sh` | generated from the data every build: 646 urls, 0 dead |
| M13 | Pick reasons describe Anthropic material as "non-Anthropic" (3 of 6) | `data/picks.json` + `scripts/validate-picks.py` | false clause deleted, nothing added; and a check so a fourth cannot ship |

**Verified, not assumed.** Every one of these was opened in a browser against a local
server after the change: the two dropped date lines on `r-7d24e5faa2` and `r-f86a3e8189`,
the outdated advisory, the back link carrying `?role=designer&level=basic`, the card pill
resolving to `paths.html?id=judging-ai-design-work`, both dead ends' links, the singular
tab title on `?q=turnitin`, the one-word empty state on `?q=typography`, and the skip link
now landing focus on `MAIN#main` instead of falling back to `<body>`.

**Three things came out of the fixing that were not in the plan.**

*The 157 `Skip if` edits are logged in full.* One file, `MECHANICAL-LOG.md`, before and
after for every line. Nothing but the leading label was touched; a mid-sentence "Skip also
if" is correct English and was left alone. Median length is unchanged at 187 characters,
so no argument was shortened.

*M13 got a check as well as a correction.* Removing three false sentences does not stop a
fourth. `validate-picks.py` now refuses a pick reason that claims to be non-Anthropic when
the item's own author or title says Anthropic, with the message *"official means the
domain, not the author"* — which is the actual confusion. Proved it fires by putting one
of the three claims back: exit 1, naming the cell and quoting the card. The three genuinely
independent claims (Harvard, freeCodeCamp, Doan Winkel) were left alone.

*M12 became a generator rather than an edit.* `sitemap.xml` was typed once and never
touched. Hand-fixing it would have put it back where it was inside a month, so
`scripts/build-sitemap.py` writes it from the data on every build, with `lastmod` from each
row's own `checked` date. 646 URLs, **0 dead ids, 0 items missing** — measured after
generating, not assumed.

**Two judgment calls inside the mechanical work, both yours to reverse.**

1. **M10 costs one tab stop on 35 cards.** The card was deliberately one focus stop, and
   seven agents praised that. Making the path pill a link adds a second stop to the 35
   cards that carry a path. I made it a link because a filled, eye-catching pill that is
   not clickable is a dead control, and the resource page already linked the same string —
   but the trade is real and it is against a decision that was made on purpose.
2. **The wording of the new `outdated` advisory is mine.** *"We marked this out of date at
   the last check. Parts of it no longer match Claude."* The field was already set on three
   rows; only the sentence is new.

### 4b. Decisions — yours, with the evidence

Not touched. Each one is a question about what the site is, not a defect with an obvious repair.

1. **May an unread item carry a verdict?** Finding 1.1, eight roles, six of them naming it as
   the thing that would make them leave. Three answers exist: read the 36, strip their prose to
   a title and a link, or rename the tier so the badge and the body agree. All three are yours.
2. **"635 resources, checked by hand."** The line is on the first screen, it is the reason
   people stay, and the site's own generated numbers refute it. Same for the 70-vs-700 line and
   "we find material, read it".
3. **Search.** Five named causes, all real, all fixable, all a rebuild: stemming, synonyms,
   spelling variants, a tie-break, and indexing `skip_if`/`who_for`. Fifty queries are now in
   `scripts/test-search.py` as the instrument that measures whether any of it works.
4. **Whether to offer four levels the catalogue cannot stock.** The teacher's proposal, quoted:
   *"If the top two cells stay at 9 and 2, do not offer the levels. Say this site is for
   teachers new to Claude and I will respect it."*
5. **What a role tag has to be true of.** 12 of 58 PM cards name a different job in their own
   words. Either the tag is wrong or the `For:` line is, and the site currently ships both.
6. **Whether the staleness warning should replace the date or sit beside it.**
7. **Whether the picks block should say why a cell has two picks, or none.**
8. **Whether picks should survive a search.** Currently the site hides its best work from its
   most engaged visitor.
9. **Whether price is a field.** $995 is currently a clause inside a `skip_if`.
10. **Whether "how well checked" is a filter axis.** It is the stated differentiator and you
    cannot filter on it.
11. **Whether the tier badge's meaning should be reachable without a mouse.**
12. **Whether the catalogue's composition is the product.** 291 of 635 from one host; 148 of
    those are one prompt-recipe gallery; 78 of those are filed at "built things with it".
13. **Whether the site names its "we", and which AI wrote what.** Four agents raised it
    unprompted; the writer's version is the sharpest, because the path the site built *for
    writers* ends on disclosure.
14. **The time buckets.** Three agents found a card whose chip says "half a day" and whose own
    text says fifteen minutes — and the Time filter then hides it from someone with fifteen
    minutes.
15. **Publisher names.** The August fix was a lookup table; 282 rows have arrived since and
    nobody held them to it. The decision is whether new rows must pass the same gate.

---

## 5. Where the agents were wrong

Recorded because the method depends on it.

- **"30 tabs called Resource."** `[01 §12.12]` The served HTML does carry
  `<title>Resource — Learn Claude</title>`, but `resource.js` sets `document.title` from the
  item on load. The **tab is fine**; the **social preview is not**, because crawlers do not run
  the script. Half the finding stands, the half about tabs does not.
- **The teacher chased a phantom** — "the home page navigates itself" — for about fifteen
  minutes, then read `home.js`, found no such code, and **discarded it rather than filing it**.
  Two other agents reported shared-browser interference and dropped observations for the same
  reason. That is the method working.
- **The business founder dropped two observations** it could not attribute to the site, and
  said so in its method note.
- **My own keyword probe for finding 2.6 over-counts** — it flags 204 of 235 founder cards, which
  is not credible. The numbers used above are the agents' hand-reads, not the probe.

---

## 6. What ten hostile strangers praised, unprompted

Worth recording, because none of them was trying to be kind.

- **The `Skip if:` line.** Named the best idea in the category by all ten. *"never treat any
  detector score as proof against a student - false accusations fall hardest on non-native
  English writers."* *"it carries an explicit prompt-injection warning."* *"most of this is
  claims, logos and testimonials."* *"Check its pricing against claude.com/pricing before
  repeating any of it."*
- **Path step reasons that justify position, not merit.** Ten of ten. *"Learning this earlier
  would have been abstract."* *"Craft is what you owe the page. This is what you owe the
  reader."* *"Second, and second on purpose."*
- **The picks are real selection.** Every agent that tested it confirmed it, and several said
  the reasons are the best writing on the site.
- **43% vs 61%.** The picker is measurably *less* vendor-tilted than the pool it draws from, and
  only 1 of 37 cells is all-Anthropic `[03]`.
- **Mobile.** No horizontal overflow at 375px on any page, any role. No tap target under 24px.
- **The accessibility work underneath**, praised by seven agents with specifics.
- **The tier vocabulary itself.** *"AI read all of it. No person has checked the notes yet"* is
  a sentence almost nobody would ship — which is exactly why finding 1.1 costs so much.
- **The certification paragraph** — a stated exclusion with a stated reason. Five agents.
- **The empty state.** *"We have nothing for this combination yet. It's on the list."*
- **No account, no tracking, no cookie wall, no newsletter** — and the footer says so.
- **Every count on the site is generated and correct.** Three agents verified the arithmetic
  independently and all three found it exact. The developer noted the consequence: *"That is why
  I could catch the contradiction — and that is a feature."*
