# Attack: a researcher
Written as someone who is a researcher, at 2026-08-27. Site version: 22e4532.

I am a postdoc. I have one hour before a supervision meeting. I want to know three
things: does Claude invent citations, may I paste an unpublished manuscript into it, and
what does my publisher expect me to declare. I am trained to distrust a claim with no
source behind it. This site's entire pitch is that it does the judging for me, so it is
going to get judged on exactly that.

Evidence: the live site at `https://mojtaba-alehosseini.github.io/learn-claude/` (all
pages HTTP 200, checked with `curl -s -o /dev/null -w "%{http_code}"`), the deployed
`data/items.js` (624,541 bytes, byte-identical header to local `data/items.json`),
`python docs/attack/role-view.py researcher …`, and `docs/attack/00-facts.md`. Where I
computed something myself, the command is in the text.

---

## 1. The first 60 seconds

The home page is one sentence with two blanks: "I'm **a [role]** and I've **[level]**."
Underneath it, live, in the tally line:

> 353 resources, checked by hand.

I read that and I stopped. Then I clicked "How we check", which is one link away in the
nav, and the same site told me, live, from the same data:

> Right now: 353 resources — 98 read by ai, 212 skimmed, 43 found only. Nothing is read
> in full yet, and the cards say so.

Both strings pulled with `javascript_tool` on the live pages
(`document.getElementById('tally').textContent`).

So "checked by hand" is the front-door claim, and the second page says a human has read
none of it in full and has not opened 43 of them at all. Those are not two ways of
saying the same thing. One of them is marketing. In my job that is the difference
between a methods section and a press release, and I noticed it inside a minute.

The badge vocabulary is where the real problem sits. From `assets/js/ui.js:47-56`:

- `reviewed` → **"Read in full"** — "We went through all of it, and a person checked the notes."
- `ai-reviewed` → **"Read by AI"** — "AI read all of it. No person has checked the notes yet."
- `previewed` → **"Skimmed"** — "We read the outline or a free sample."
- `listed` → **"Found only"** — "We found it and sorted it. Nobody has looked at the content yet."

Count of `reviewed` across the whole catalogue: **0** (00-facts.md). So the top of the
ladder is decorative. What I am actually being offered, for my role, is this
(`python docs/attack/role-view.py researcher --counts`):

```
tiers:   {'ai-reviewed': 14, 'previewed': 24, 'listed': 3}
```

14 items where an AI read it and no person confirmed. 24 where somebody looked at the
outline. 3 where nobody opened it. That is my whole shelf.

I want to be precise about why "Read by AI" is not an acceptable warrant. It is not that
AI reading is worthless. It is that the recommendation and the check come from the same
process. A model wrote the "For:" line, wrote the "Skip if:" line, and then the badge
certifies that a model read the thing. There is no independent step anywhere in that
loop. In a review that is called self-report, and it is not evidence. The site knows
this — it wrote the disclaimer itself, in the tooltip — and then it built a whole
homepage claim ("checked by hand") on top of the thing the disclaimer denies.

Second thing I noticed in the first minute: the tooltip is the *only* place those four
words are explained on a card, and it is a `title=` attribute (`ui.js:121`). On a phone
there is no hover. See section 7.

## 2. Does the front door work for me (all four levels, with counts)

I answered "a researcher" and then each of the four levels. Counts confirmed three ways
— 00-facts.md, `role-view.py --counts`, and live in the browser
(`window.LC.items().filter(i => i.roles.indexOf('researcher') !== -1)` grouped by level,
returned `{"all":41,"never-used":6,"basic":19,"confident":14,"builder":2}`).

| level shown as | key | count |
|---|---|---|
| never used Claude | never-used | **6** |
| used it a little | basic | **19** |
| used it a lot | confident | **14** |
| built things with it | builder | **2** |

**never used Claude — 6 cards, and it is one course four times.**

```
python docs/attack/role-view.py researcher never-used
```

1. Lesson 1: Introduction to AI Fluency | AI Fluency: Framework & Foundations Course |
2. Lesson 2B: The 4D Framework | AI Fluency: Framework & Foundations Course
3. Claude 101
4. AI Fluency for Students
5. AI Fluency: Framework & Foundations
6. Anthropic Academy — Courses hub

Four of the six have "AI Fluency" in the title (verified: `sum(1 for i in nu if 'ai
fluency' in i['title'].lower())` → 4). Two of those four are individual *lessons* pulled
out of the course that is also card 5. Card 6 is the hub page that contains cards 3, 4
and 5. So six cards, two actual things: Claude 101, and AI Fluency.

Publisher mix at this level: `{'Anthropic': 4, 'Anthropic Academy': 1, 'Coursera': 1}` —
and the Coursera one is also Anthropic's AI Fluency course. A directory that says on
every page "It is not affiliated with Anthropic" has given a beginner researcher a
beginner shelf that is 6 for 6 Anthropic material.

Tier mix at this level: `{'previewed': 6}`. Every single one is "Skimmed". Nobody read
any of my six starting points.

And card 1's "For:" line is written for somebody else entirely:

> For: People starting the AI Fluency course, and **teachers deciding whether to set it
> for a class.**

Also note the title ends in a stray pipe — `…Foundations Course |` — a raw YouTube title
pasted in without editing, and it renders that way on the card.

Nothing at this level mentions hallucination or fabricated citations. I checked:

```
python -c "... for i in R: if 'hallucinat' in blob or 'fabricat' in blob: print(level, tier, title)"
→ basic:     Plan your literature review (use-case)
  confident: Connect and integrate your local Zotero library with Claude Cowork
  confident: Claude AI and Literature Reviews: An Experiment in Utility and Ethical Use
  confident: Claude for medical literature search: Avoid hallucinations
  builder:   Claude Skills for Academics (Beginner Tutorial, Part 2)
```

Zero at never-used. For an academic, that ordering is backwards to the point of being
negligent. See 9.1.

**used it a little — 19 cards, and the first one is for a product manager.**

Card 1, in the real on-screen order (default sort, `browse.js:111-113`, reproduced by
role-view.py), live at `browse.html?role=researcher&level=basic`:

> **Read by AI** — Claude for Product Managers: Synthesizing User Research — Enterpret
> For: A PM sitting on 5-10 interview transcripts who wants synthesis rather than a tidy
> summary, and who wants to catch confident misreads before they reach a roadmap deck.
> Skip if: … the guide admits quality drops past that and then steers you toward paid
> tooling, **including its own MCP server**.

`roles: ["pm","researcher"]`, `source: Enterpret`. The single best-checked, first-listed
thing a researcher is shown is a SaaS vendor's content-marketing page for product
managers, and the site's own note says it upsells you its product. I did not come here
for a roadmap deck.

Cards 2, 4, 5, 6 are Elsevier, ICMJE, IEEE and Nature AI policy pages. Add card 18
(Princeton, "Disclosing the Use of AI") and that is 5 of 19 that teach me nothing at all
about using Claude. They are publisher rules. Useful — I do need them — but they are not
Claude training, and four of them occupy the top six slots.

**used it a lot — 14 cards.** The best of the whole role sits here: a peer-reviewed
study (see section 5). It also contains the worst thing on the site (see 9.2).

**built things with it — 2 cards, and one of them says "Beginner" in the title.**

```
python docs/attack/role-view.py researcher builder
1. [Skimmed] Claude Skills for Academics (Beginner Tutorial, Part 2)
2. [Skimmed] zotero-mcp (54yyyu)
```

Live confirmation at `browse.html?role=researcher&level=builder`: count text reads
"2 resources. Remove a filter to see more." The top of the ladder — the shelf for
somebody who has *built things* — is a beginner tutorial and a GitHub repo. Both
"Skimmed". Both with **no publish date**. The card even says:

> Skip if: You've never used Claude — start with Part 1.

Part 1 sits at `confident`, one level down, and is not linked from here. A skip-if that
tells me to go somewhere and then does not tell me where is not judgement, it is a
loose end.

**The two extremes together: 8 cards, 8 "Skimmed", 0 "Read by AI", 0 "Read in full".**

## 3. What the catalogue actually gives me (are these really for me?)

No. "A researcher" is not one audience here. It is at least six, glued together by a
tag. Reading the `For:` lines back:

- **Clinician / biomedical**: "Clinicians/researchers who want to use Claude on
  literature safely"; "Any author submitting to medical/biomedical journals" (ICMJE).
- **Humanities / library scholar**: the Library Trends study; "Non-technical academics
  wanting approachable, research-focused guidance".
- **Grad student**: "PhD/grad students wanting responsible AI habits" (AI Fluency for
  Students); "A final-year or postgraduate student whose work may end up in a thesis".
- **Quant with R/Python**: "Faculty/postdocs/advanced grad students with basic prompting
  **+ some R/Python**" (AI Horizons seminar, paid).
- **Spreadsheet analyst**: "Excel-to-analysis beginners. Assumes no coding."
- **Product manager**: "A PM sitting on 5-10 interview transcripts."

Counted: **11 of 41** have a `For:` line that never names a researcher-shaped person at
all — no "research", "academ", "phd", "postdoc", "scholar", "scientist", "faculty",
"thesis", "grad", "clinician" or "author" anywhere in it. Command shown in section 9.3.

Format mix, from 00-facts.md: video 12, article 9, docs 8, course 6, repo 3, podcast 2,
hands-on 1. The `article` bucket is where this falls apart for me. Nine items carry the
same "article" chip:

| tier | source shown | what it actually is |
|---|---|---|
| ai-reviewed | **Jhu** | peer-reviewed study, Library Trends 73(3):355-380 |
| ai-reviewed | Enterpret | SaaS vendor marketing guide |
| ai-reviewed | Anthropic | vendor use-case page |
| ai-reviewed | Anthropic | vendor news post |
| ai-reviewed | Effortless Academic | blog post |
| previewed | Effortless Academic | blog post |
| ai-reviewed | Effortless Academic | blog post |
| ai-reviewed | **Lszabo** | personal blog |
| previewed | **Clauderesearcher** | anonymous single-purpose site |

One peer-reviewed paper and eight blog and marketing posts, all wearing the identical
"article" chip. There is no `paper`, `preprint` or `peer-reviewed` value in
`LC.FORMAT` (`ui.js:34-37`: video, course, docs, article, hands-on, podcast, repo). For
a directory aimed at researchers, having no way to say "this one went through peer
review" is a category error, not a missing nice-to-have. Three of the nine come from
one blog.

Vendor concentration: 13 of my 41 carry `official: true` — Anthropic's own courses,
docs, news pages and channel videos. That is 32% of everything I am shown, from the
company selling the product, on a site whose footer says "It is not affiliated with
Anthropic". The footer is true and beside the point.

## 4. Paths

There is one for me: **"Using Claude for research without embarrassing yourself"** — 5
steps, about 2 hours, "some paid steps", roles `["researcher","student"]`. The framing is
good. Its intro is the best sentence on the site:

> The order matters more here than anywhere else. The failure modes are specific and the
> consequences are public.

Then I audited it against the items it points at
(`data/paths.json` joined to `data/items.json`):

```
step 1  level=confident roles=data-analyst  tier=ai-reviewed cost=free          published=UNVERIFIED
        Reduce hallucinations
step 2  level=basic     roles=researcher    tier=ai-reviewed cost=free-account  published=UNVERIFIED
        What are Projects?
step 3  level=confident roles=researcher    tier=ai-reviewed cost=paid-once     published=2025-02-01
        Claude AI and Literature Reviews: An Experiment in Utility and Ethical Use
step 4  level=confident roles=researcher    tier=ai-reviewed cost=free          published=UNVERIFIED
        Connect and integrate your local Zotero library with Claude Cowork
step 5  level=basic     roles=researcher    tier=ai-reviewed cost=free          published=2026-01-01
        ICMJE Recommendations — Use of AI in Publishing
```

**Step 1 is not in my role.** `roles: ["data-analyst"]`. It is one of 353 items and it is
not one of my 41 — it does not appear anywhere in `role-view.py researcher never-used |
basic | confident | builder`. The path that exists to stop a researcher embarrassing
himself opens with a document the researcher filter hides. If I had come in through
Browse instead of Paths, I would never have seen it.

**5 of 5 steps are `ai-reviewed`.** Zero `reviewed`. So on the one route where the site
itself says the consequences are public, no human has confirmed a single step. And
`assets/js/paths.js` prints this, twice, in its own empty states:

> We only publish a path once every step in it has been checked.

"Checked" there means something different from "checked" in the badge system, and the
difference is exactly the human. That is a word doing two jobs, and the second job is
hiding the first.

**Is the sequence defensible?** The shape is right — failure mode, then workspace, then
evidence, then your own library, then disclosure. Two problems with the content:

- Step 5, ICMJE, is the medical/biomedical body. The path's own `why` says *"This is not
  optional and most people learn it too late."* The card for the same item says
  *"Skip if: Your field follows a different body (still align with your target
  journal)."* The path calls mandatory what the card calls skippable. I am not in
  medicine. Which of the site's two sentences do I obey?
- Step 3 is the only paid step (`paid-once`, Project MUSE). "Some paid steps", plural,
  for one. Step 2 also needs an account. Step 4 is labelled **free**, and it requires
  Claude Cowork — which the site's own card at `confident` says out loud: *"skip if you
  are still deciding whether to pay for Claude — Cowork requires a paid plan."* So the
  path's cost line understates the real cost by a subscription.

**Does it stop me embarrassing myself?** Partly. It puts hallucinated citations first,
which is right. But it puts them first behind a card my role cannot see, at a level
above the one it advertises (path level `basic`; 3 of 5 steps are `confident`), and the
one step that actually documents the failure with data is behind a paywall.

The Paths index page never shows which roles a path is for — `paths.js index()` renders
title, `for`, step count, time and cost, and nothing else. The role mapping exists in the
data and is invisible on screen. I had to guess which of the three paths was mine from
the title.

## 5. The card and the resource page

I opened three, live.

**(a) `listed` tier — `resource.html?id=r-0ccfc4f72a`.** This is the one that made me
close the tab. The full rendered page text, pulled from the live DOM:

> **Found only**
> Mushtaq Bilal — Claude for Academic Writing & Research
> Kit · Mushtaq Bilal, PhD · podcast · one hour · **pay once**
>
> **What it teaches**
> — automate systematic review screening with claude
> — apply claude code to academic writing tasks
>
> **Skip it if**
> [allegation redacted 2026-08-27: an unsourced claim about a named individual. The cited source contains no support for it and no other source was ever given. Removed from data/items.json and from every file that repeated it.]
>
> **How we checked this one**
> Found only. We found it and sorted it. **Nobody has looked at the content yet.**

Read those three blocks together. On one page the site (i) tells me what the resource
teaches, (ii) accuses a **named, identifiable real academic** of promoting techniques to
evade AI-detection — which in my world is a research-integrity allegation, not a
preference — and (iii) states that nobody has looked at the content. All three cannot be
true. If nobody opened it, the "What it teaches" bullets are invented and the allegation
is unsourced. There is no citation for the accusation anywhere on the page. I would not
publish that sentence about a colleague without a reference, and neither should a site
whose whole selling point is that it does the checking.

The publisher line says **"Kit"**. Kit is a newsletter platform. The button says "Open on
Kit". The provenance line says "Found through Kit". Cost is "pay once" with no price.

**(b) `ai-reviewed` tier — `resource.html?id=r-69ee3c03e3`.** The best item in my role,
and the site mangles the one field I judge sources by:

> **Read by AI**
> Claude AI and Literature Reviews: An Experiment in Utility and Ethical Use
> **Jhu** · Max Sparkman & Alan Witt, Library Trends 73(3):355-380 · article · one hour ·
> pay once
> … **Open on Jhu**

"Jhu" is `muse.jhu.edu` with the subdomain shaved off. This is Johns Hopkins University
Press / Project MUSE, and it is the only peer-reviewed source I have. `ui.js:125-126`
states the rule the data is breaking, in its own comment: *"Named because it is the
publisher, not the platform: a video on Anthropic's channel is from Anthropic, not 'from
YouTube'."* The rule is written down and not applied. Same failure gives me `Lszabo`,
`Clauderesearcher`, `Ccforeveryone`, `Kit`, and — for
`github.com/anthropics/prompt-eng-interactive-tutorial`, a repo in Anthropic's own
organisation with `author: "Anthropic"` — the source **"GitHub"** and `official: false`.
Anthropic's own tutorial is not marked official. Anthropic's marketing page is.

Second problem with this page. It is `cost: paid-once`, behind Project MUSE, and it is
badged "Read by AI — **AI read all of it.**" The how-we-check page states the opposite
policy in writing: *"Skimmed … Paid courses usually stop here, because we cannot see
inside them."* So either the rule was broken here, or the AI read an abstract and the
badge over-claims. I cannot tell which, and it is step 3 of my path.

**(c) the card render — `r-2546202143`.** Pulled `LC.card()` output from the live page.
The byline reads:

> Clauderesearcher · Independent (unaffiliated with Anthropic)

Neither half of that is a name. One is a domain slug, the other is a disclaimer sitting
in the author field. `published: UNVERIFIED`. Badge: Skimmed. And the summary claims it
teaches "PRISMA discipline" — PRISMA is a formal systematic-review reporting standard. An
undated, unauthored, skimmed web page making a PRISMA claim is precisely the thing I
would reject from a student's reference list.

**What the pages hide.** Every item carries a `notes` field. `grep -rn "notes"
assets/js/*.js` returns two hits, both inside tooltip strings — **`notes` is never
rendered anywhere**. Here is what is being withheld from me:

- Princeton disclosure entry: *"I confirmed it is live and **read the headings, not the
  full page**, so this is metadata-level only."*
- LinkedIn entry: *"Metadata only (course behind subscription)."*
- Mushtaq Bilal entry: *"**CAUTION:** some content promotes making AI text 'pass' as
  human, which conflicts with publisher disclosure rules."*

That is the honest methods section. It exists, it is written, and the site does not show
it. That single decision is the difference between a directory I would cite and one I
would not.

## 6. Search, in my words

Reproduced with `assets/js/search.js`'s algorithm via `scripts/test-search.py` (its
docstring: same index, same IDF, same admit gate, same floor as the browser).

**"systematic literature review"** — 7 results. Rank 1, by a margin of 54% over rank 2:

```
  62.3 [listed]      Mushtaq Bilal — Claude for Academic Writing & Research
  40.5 [ai-reviewed] Claude AI and Literature Reviews: An Experiment in Utility…
  39.0 [previewed]   Claude Researcher — source-first literature review workflows
  31.5 [ai-reviewed] Plan your literature review (use-case)
```

The most common query in my working life returns, at the very top, a **paid** resource
that **nobody at the site has opened**, by a person the site itself flags for
detection-evasion tactics. It ranks there because the enrichment pipeline wrote the
keyword "systematic review screening" and the `teaches` bullet "automate systematic
review screening with claude" — for an item nobody read. Machine-written keywords, on
unread content, hoisted to number one on the query that matters most. See 9.2.

**"will it fabricate citations"** — 7 results.

```
  20.5 [ai-reviewed] Claude for medical literature search: Avoid hallucinations
  20.5 [previewed]   Claude AI for Researchers: Projects, Skills, Cowork & Consensus…
  19.6 [ai-reviewed] Use Claude for Excel                      ← data-analyst
  19.6 [ai-reviewed] Use research on Claude
  19.6 [ai-reviewed] Claude AI and Literature Reviews…
  19.6 [previewed]   3 Mind Blowing Claude & Consensus Research Workflows | No Coding
  11.8 [previewed]   Getting started with Claude in Excel      ← data-analyst
```

Two of seven results for "will it fabricate citations" are about **Excel**. And
"Reduce hallucinations" — the document the path calls the clearest account of fabricated
citations — **does not appear at all**. It is findable only if I already know its exact
title (`test-search.py "reduce hallucinations"` → rank 1, 49.7). The site's own step 1 is
invisible to the question step 1 exists to answer.

**"can I use this on unpublished data"** — 53 results. Top ten, every one of them:

```
  11.7 [ai-reviewed] Is my data used for model training? (Privacy Center)  roles=business-founder
  11.7 [previewed]   AI Fluency for Nonprofits                             roles=business-founder
  11.7 [previewed]   15 Claude Tips for Everyday Data Analysis             roles=data-analyst
  … 7 more, all data-analyst
```

Researcher-tagged hits in the whole 53: **7**. None in the top ten. Rephrased as "will my
unpublished manuscript be used for training" → 27 results, top hit still
business-founder-only, results 2 and 3 for writer-marketer.

The question of whether I may paste an unpublished manuscript, an NDA'd industry dataset
or participant data into Claude is the question that decides whether I use this tool at
all. The site has the right answer — "Is my data used for model training? (Privacy
Center)" — and has not tagged it for researchers. Across my whole 41, exactly **2**
items mention confidentiality at all, and both are journal AI-policy pages (Nature,
IEEE), not data-handling guidance. Command in 9.4.

## 7. On a phone

I tested at 375×812 by loading `browse.html?role=researcher&level=basic` in an iframe at
that width on the live site and reading its computed styles:

```
{"innerWidth":372,"mq768":true,"railDisplay":"none","barDisplay":"block",
 "barText":"Filters","count":"19 resources","cards":19,
 "bodyScrollWidth":357,"bodyClientWidth":357,"horizontalOverflow":false}
```

The layout is fine. Filter rail hidden, a 69px "Filters" bar pinned to the bottom, no
horizontal overflow, all 19 cards present, search and sort both reachable. Consistent
with the `@media (max-width: 768px)` block at `assets/css/site.css:590-630`, which also
fixes footer link targets to 44px. Somebody did this properly.

Two things are wrong anyway.

**The badge is unexplained on touch.** Measured on the phone-width page: the first
badge's text is `"Read by AI"` and its explanation lives entirely in
`title="AI read all of it. No person has checked the notes yet."`. A `title` attribute
does not open on a touch screen. So on a phone the four words that carry the site's
entire epistemic claim — Read in full / Read by AI / Skimmed / Found only — are bare
labels with no definition anywhere on the page. The definitions are on how-we-check,
which is a separate page in the nav. On a phone this site's central feature is mute.

**19 cards is 12.8 screens.** Measured: page height 10,352px against an 809px viewport;
first card 591px tall, median card 442px. The `For:` and `Skip if:` prose is what makes
cards tall, and it is also the thing worth reading — but at three to four cards per
thumb-scroll I have to swipe through 13 screens to see one level of one role, with no
way to collapse anything and no tier filter to cut it down.

## 8. Content quality — the three worst entries I was shown, quoted

**Worst — "Mushtaq Bilal — Claude for Academic Writing & Research"** (`confident`,
`listed`, `paid-once`, `published: UNVERIFIED`, source "Kit"). Verbatim from the live
resource page:

> **Skip it if** — [allegation redacted 2026-08-27: an unsourced claim about a named individual. The cited source contains no support for it and no other source was ever given. Removed from data/items.json and from every file that repeated it.]

and, on the same page:

> Found only. We found it and sorted it. Nobody has looked at the content yet.

An unsourced integrity allegation against a named academic, on an entry nobody opened,
which the search engine then ranks **first** for "systematic literature review". Every
part of that is wrong, and they compound. If the site believes the allegation, this entry
should not be in the catalogue at all — you do not "recommend, but". If it does not
believe it well enough to open the thing, it should not publish the sentence.

**Second — "15 Claude Tips for Everyday Data Analysis"** (`basic`, `listed`,
`subscription`, source "LinkedIn Learning"). Its `For:` line is:

> Researchers with LinkedIn Learning access wanting quick data tips.

Its URL is `https://www.linkedin.com/learning/topics/claude` — a topic hub, not the
course. And the same course is in the catalogue **twice**, under two ids:

| id | roles | tier | url |
|---|---|---|---|
| `r-204c63428f` | data-analyst | previewed | `…/learning/15-claude-tips-for-everyday-data-analysis` |
| `r-a38414af15` | **researcher** | listed | `…/learning/topics/claude` |

Same title, same 21-minute runtime, same `published: 2026-04-14`. The data-analyst gets
the real course page and a "Skimmed" badge. The researcher gets a topic hub and a
"nobody looked at it" badge. Both URLs return HTTP 200 (`curl -o /dev/null -w
"%{http_code}"`), which is exactly why the "0 dead links" number caught nothing: the
link works, it just does not go to the thing the card names. See 9.5.

**Third — "AI Fluency: Framework & Foundations"** (`never-used`, `previewed`, listed as
`course · half-day`). The URL is `https://www.anthropic.com/ai-fluency` — Anthropic's
product landing page. The identical course exists twice more in the catalogue, with the
actual course URLs, and neither copy is mine:

| id | roles | url |
|---|---|---|
| `r-c0fa677417` | business-founder, non-technical | `anthropic.skilljar.com/ai-fluency-framework-foundations` |
| `r-74b6ca831a` | non-technical, teacher, student, business-founder | `coursera.org/learn/ai-fluency-framework-foundations` |
| `r-225ab27b7b` | **researcher** | `anthropic.com/ai-fluency` |

Everybody else gets the course. The researcher gets the marketing page, described as a
"course" that takes "half a day".

Dishonourable mention for tone. This is in my `confident` shelf, verbatim:

> **NEW: Claude's 'Super Prompts' Will Save You DAYS of Work (Full Tutorial + Demo)**

and this in `basic`:

> **3 Mind Blowing Claude & Consensus Research Workflows | No Coding**

To the site's credit, the Skip-if on the first one says the quiet part: *"The title is
louder than the calm, analytical content."* But I am scanning a list. I bounce off "Mind
Blowing" before I reach the note that explains it.

## 9. Everything that is broken, ranked

**9.1 — The one thing a researcher must learn first is absent from where a researcher
starts.** Zero of my 6 `never-used` cards mention hallucination or fabricated citations
(command in section 2). The first mention arrives at `basic`, on "Plan your literature
review (use-case)", whose own Skip-if reads: *"You need explicit citation-verification
guidance — the page does not warn about fabricated references, so add that step
yourself."* Real coverage does not appear until `confident` — two levels above where a
new user lands. A researcher can read the entire beginner shelf of a site built for
researchers and never be told the tool invents references.

**9.2 — An unread, paid, integrity-flagged entry ranks #1 for the most important query
in the role.** `test-search.py "systematic literature review"` → rank 1 at 62.3,
`tier: listed`, `cost: paid-once`, with the detection-evasion Skip-if quoted in section
8. Cause: `keywords` and `teaches` were machine-generated for an item nobody opened, and
the ranking treats those invented terms as evidence. The site's weakest tier is
outranking its peer-reviewed one because unread items get the same enrichment treatment
as read ones.

**9.3 — "Researcher" is not one audience, and 11 of 41 cards are addressed to somebody
else.** Command:
```
python -c "... not any(k in who_for.lower() for k in ('research','academ','phd','postdoc',
  'scholar','scientist','faculty','thesis','grad','clinician','author'))"
→ 11 of 41
```
Including the first card at `basic` (written for "A PM"), a `never-used` card written for
"teachers deciding whether to set it for a class", and "Excel-to-analysis beginners.
Assumes no coding." Lab scientist, clinician, humanities scholar, grad student, PM and
spreadsheet analyst are being served one shelf.

**9.4 — No researcher-tagged answer exists for the confidentiality question.** Only 2 of
41 items mention confidentiality at all (Nature and IEEE editorial policies; command:
grep of each item's full JSON for `privacy|confidential|training data|used for model|
gdpr|irb|anonym`). The correct answer is in the catalogue — "Is my data used for model
training? (Privacy Center)", `roles: ["business-founder"]` — and my role filter hides it.
Consequence: the site cannot answer whether I may paste an unpublished manuscript,
participant data, or NDA'd data into Claude.

**9.5 — The catalogue contains duplicate entries, and in every case that touches me, the
researcher gets the worse copy.** 5 duplicate titles site-wide; **3 of the 5 land in the
researcher role**:

| title | researcher's copy | the other role's copy |
|---|---|---|
| 15 Claude Tips for Everyday Data Analysis | `listed`, topic-hub URL | `previewed`, real course URL |
| AI Fluency: Framework & Foundations | marketing landing page | Skilljar course, Coursera course |
| AI Fluency for Students | Coursera copy | Skilljar copy |

Command: `collections.Counter(title.strip().lower())` over `data/items.json`, then
`Counter(url)` → **0** duplicate URLs. The de-duplication is URL-based, so a wrong URL
makes a duplicate invisible to the pipeline. That is why nobody has caught this.

**9.6 — Step 1 of the researcher path is not in the researcher role.** "Reduce
hallucinations", `roles: ["data-analyst"]`, `level: confident`. Verified: it is absent from
all four `role-view.py researcher <level>` listings. The path also advertises
`level: basic` while 3 of its 5 steps are `confident`, and labels step 4 `free` when the
site's own Cowork card says *"Cowork requires a paid plan."*

**9.7 — The site contradicts itself about how much human checking happened, on two pages
one click apart.** Home: "353 resources, checked by hand." How we check: "Nothing is read
in full yet." 43 items are badged "Nobody has looked at the content yet." Both strings
pulled live. Related: `paths.js` states twice that "We only publish a path once every
step in it has been checked," and every step of my path is `ai-reviewed` — no human.

**9.8 — "Read by AI" is applied to paid content that the site's own policy says cannot be
read.** how-we-check: *"Skimmed … Paid courses usually stop here, because we cannot see
inside them."* The Project MUSE paper (`cost: paid-once`) is nonetheless badged "Read by
AI — AI read all of it," and it is step 3 of my path. Either the policy was broken or the
badge over-claims; the reader cannot tell which, and there is no `notes` on screen to
say.

**9.9 — Two-thirds of my shelf cannot be dated.** 21 of 41 have no publish date
(`role-view.py researcher --counts` → `no date: 21`; site-wide 171 of 353 per
00-facts.md). Of the 20 that are dated, 6 are more than 12 months old (published before
2025-08-27). So **27 of 41 are either undated or over a year old**. The home page
promises: *"We show the date … You can see when we last looked, and whether the thing is
old."* For 21 of my 41 the second half of that sentence is unanswerable, and the card
just says "No publish date given". Every `checked` date in my role is 2026-08
(`Counter(checked[:7])` → `{'2026-08': 41}`).

**9.10 — The provenance the site actually recorded is hidden from the reader.** `notes`
is never rendered (`grep -rn "notes" assets/js/*.js` → only two tooltip strings). Withheld
text includes *"read the headings, not the full page, so this is metadata-level only"*,
*"Metadata only (course behind subscription)"* and *"CAUTION: some content promotes making
AI text 'pass' as human"*. The honest part of the methodology exists and is not shown.

**9.11 — Publisher names are auto-derived from domains, against the project's own written
rule.** `ui.js:125-126` states the rule; the data breaks it for `Jhu` (Johns Hopkins /
Project MUSE), `Kit` (a newsletter platform), `Lszabo`, `Clauderesearcher`,
`Ccforeveryone`, and — most damagingly — `GitHub` with `official: false` for
`github.com/anthropics/prompt-eng-interactive-tutorial`, whose `author` field literally
says "Anthropic". Anthropic's own tutorial is unofficial; Anthropic's marketing page is
official.

**9.12 — There is no way to filter by how well something was checked.** `AXES` in
`browse.js:17-24` is role, level, time, topic, format, cost. Tier is a *sort* option
("Best checked first"), never a filter. I cannot ask "show me only what a human read" —
which, given the answer is zero, the site might prefer I not discover, but the control's
absence is what stops me discovering it.

**9.13 — Cross-references inside `Skip if:` lines point at things I cannot reach.** The
Princeton card says: *"The Melbourne, Warwick or Tulane pages give you more usable
templates for that."* All three exist in the catalogue — `students.unimelb.edu.au`,
`warwick.libguides.com`, `libguides.tulane.edu` — and all three are `roles: ["student"]`,
so they never appear for a researcher. None of the three is hyperlinked; the Skip-if is
escaped plain text. I am sent to three places I cannot get to.

**9.14 — Titles are pasted in raw.** `Lesson 1: Introduction to AI Fluency | AI Fluency:
Framework & Foundations Course |` — trailing pipe included, rendered as-is on the card at
the very top of my `never-used` shelf. On the same shelf, a "course" whose URL is a
product landing page. Small things, but they are the first four cards a new researcher
sees.

**9.15 — Minor: the how-we-check tally lowercases the label.** Live text: "98 read by
ai". `how-we-check.html` builds it with `LC.TIER[t].label.toLowerCase()`, which turns
"Read by AI" into "read by ai". Also, the comment at `ui.js:88` says "176 of 353
resources publish no date at all"; the real figure is 171
(`sum(1 for i in items if i.get('published')=='UNVERIFIED')` → 171). Not visitor-facing,
but it is the same class of drift the site was built to prevent.

*Sharpening what was already known:* "Found something wrong? Tell us." has no route at
all — I grepped every HTML file for `mailto:`, "contact", or an issues link and found
none, and the outbound links on how-we-check are five internal pages and a stylesheet.
For a site asking academics to report errors, an error-reporting section with no channel
is worse than no section: it tells me somebody thought about corrections and then did not
build one.

## 10. The one thing that would make me leave and not come back

The badges are a measurement instrument with nothing behind them, and the site sells them
as the product.

"Read by AI" means an AI wrote the recommendation and an AI certifies the
recommendation. That is a closed loop with no external check, and 98 of 353 items — 14 of
my 41 — rest on it. "Found only" means nobody opened it, and the site still prints "What
it teaches" bullets and, in one case, an unsourced misconduct allegation about a named
academic. "Read in full" — the only tier that would mean a person stood behind anything —
is **0 of 353**.

The concrete version, and the reason I would not come back: I asked the question my field
asks most, "systematic literature review". The top answer was a **paid** resource that
**nobody at this site has opened**, ranked there by keywords a machine invented for
content it never read, carrying an accusation the site cannot support. Meanwhile the
peer-reviewed study that actually measured Claude's citation failures ranked second,
under a publisher name mangled to "Jhu".

That is not a directory with some gaps. That is a ranking system that systematically
prefers its own unverified metadata over its verified sources. Everything else in this
file is fixable. That one is the thing the site *is*.

And the tell is that the site knows. The `notes` field says "read the headings, not the
full page". The tooltip says "No person has checked the notes yet." The honest version
was written down and then not shown. I do not need this directory to be perfect. I need
it to show me its methods. It has them and it hides them.

## 11. What is genuinely good (be honest, but brief)

- **`Skip if:` is the right idea and it is the best thing here.** "Skip if you will not
  use Consensus - two of the three workflows depend on it" tells me more in one line than
  most directories manage in a paragraph. When it is written well it is genuinely
  decision-grade.
- **The four-tier honesty, as a design, is correct** — and unusual. Publishing "Nobody has
  looked at the content yet" on your own catalogue takes some nerve. The problem is the
  execution, not the concept.
- **The path framing is the best writing on the site.** "The failure modes are specific
  and the consequences are public" is exactly right about my world, and the ordering
  instinct — failure mode first, disclosure last — is what an experienced supervisor would
  say.
- **The journal-policy cluster is real value.** Elsevier, ICMJE, IEEE, Nature, Princeton
  in one place, each with a who/skip line, is something I would otherwise assemble by
  hand.
- **The phone layout is done properly**, and better than most sites I use daily: no
  overflow, real 44px targets, a thumb-reachable filter bar.
- **The one peer-reviewed source in the role is a genuinely good pick.** Sparkman & Witt,
  *Library Trends* 73(3) — comparing a Claude literature review against a human one — is
  precisely the evidence I wanted, and I would not have found it myself. It deserves a
  better publisher label than "Jhu".

## Checklist — every line ticked or the file is not finished
- [x] I opened the live site — all pages HTTP 200 via curl; home, how-we-check, browse
      (role=researcher, level=builder), and three resource pages driven live in my own
      Chrome tab (created and closed by me; four other agents were working concurrently
      and I touched no tab I did not create)
- [x] I tried all four levels — never-used 6, basic 19, confident 14, builder 2;
      confirmed against 00-facts.md, `role-view.py --counts`, and live
      `window.LC.items()` in the browser
- [x] I quoted at least 5 real titles or lines from the site — 20+, including "Claude for
      Product Managers: Synthesizing User Research", "Claude Skills for Academics
      (Beginner Tutorial, Part 2)", "Mushtaq Bilal — Claude for Academic Writing &
      Research", "Claude AI and Literature Reviews: An Experiment in Utility and Ethical
      Use", "3 Mind Blowing Claude & Consensus Research Workflows | No Coding", "NEW:
      Claude's 'Super Prompts' Will Save You DAYS of Work", "Lesson 1: Introduction to AI
      Fluency | AI Fluency: Framework & Foundations Course |", and the Skip-if lines
      quoted verbatim in sections 2, 4, 5 and 8
- [x] Every number I used is in 00-facts.md or I show the command — 41/6/19/14/2, 31 free,
      23 only-this-role, 0 reviewed, 98 ai-reviewed, 171 no-date all from 00-facts.md;
      21 no-date-in-role, 24 previewed, 3 listed, 13 official, 11 audience-mismatch,
      27 undated-or-stale, 5 duplicate titles, 0 duplicate URLs, 10,352px/12.8 screens
      each shown with the command or the live DOM read that produced it
- [x] I looked at a phone width — 375×812, live, computed styles read back; cross-checked
      against `assets/css/site.css:590-630`
- [x] I found at least one thing nobody has mentioned before — several. The duplicate
      entries where the researcher always gets the worse copy, invisible to the pipeline
      because de-duplication is URL-based and the researcher's URLs are wrong (9.5).
      Path step 1 is tagged `data-analyst` and is not in the role the path serves (9.6).
      The `notes` field — the site's real methods section — is never rendered (9.10).
      An unread, integrity-flagged, paid entry ranks #1 for "systematic literature
      review" on the strength of machine-invented keywords (9.2). Publisher names derived
      from domains, breaking a rule the codebase states in its own comment, which turns
      Johns Hopkins into "Jhu" and marks Anthropic's own repo unofficial (9.11).
