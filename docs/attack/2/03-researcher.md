# Attack 2: a researcher
Written as an academic researcher, 2026-09-05. Live site only:
`https://mojtaba-alehosseini.github.io/learn-claude/`. Chrome, desktop 1280x900 and
mobile 375x812.

I am an academic. I want to know three things: does Claude invent citations, may I paste
an unpublished manuscript into it, and what does my publisher expect me to declare. I am
trained to distrust a claim with no source behind it. The site's pitch is that it does
the judging for me, so it gets judged on exactly that.

Where I state a count I computed it from the site's own shipped `data/items.js` and
`picks.js`, not from a page's prose.

---

## 1. First 60 seconds

Landing page. One sentence — "Find what's worth your time." — then a fill-in-the-blank
headline: **"I'm a [role] and I've [level]."** Ten role chips. An illustration cycles
beside it (mug, microscope) and the matching chip highlights itself. It is calm and it is
not a landing page trying to sell me a newsletter. Good.

Two problems inside the minute:

- At 1280x720 the **second question is below the fold and the submit button is above
  it**. I see "Who are you?", ten chips, a search box and an orange **Show me** button.
  "How much Claude do you know?" is off-screen. A two-question form where the button sits
  above question two.
- **"635 resources, checked by hand."** By the time I reached `how-we-check.html` I
  learned that *nothing* has been checked by a hand. The page's own words: **"Nothing is
  read in full yet, and the cards say so."** The home page says checked by hand; the
  methodology page says nobody has read anything. Those are the first and the last claim
  I encounter, and they contradict.

I clicked "a researcher". The role chips vanished, replaced by the level question, and a
live counter appeared: **"83 resources match so far."** That is genuinely nice.

---

## 2. The front door, all four levels

URL pattern is `browse.html?role=researcher&level=<level>`. Each level, what I got:

| Level | Count | What is actually in it |
|---|---|---|
| never used Claude | 21 | 19 of 21 are Anthropic's own. 9 of 21 are Anthropic Academy *medical connector* pages. |
| used it a little | 21 | ICMJE, IEEE, Elsevier, Nature, lit-review workflow. The good cell. |
| used it a lot | 21 | Zotero, statistics verification, PubMed/hallucination workflows. Also good. |
| built things with it | 20 | 18 of 20 Anthropic's own. All 17 in "Everything else" are pharma/clinical connectors. |

**Level 1 is the wrong shelf.** A person who has never opened Claude and told the site
they are a researcher is handed:

> "Using the CMS Coverage Connector in Claude — **For:** Medical coders, billers, and
> prior authorization specialists checking whether Medicare will pay for a service."

> "Using the NPI Registry Connector in Claude — **For:** Healthcare administrators,
> credentialing staff, and healthcare recruiters who need to verify a provider's National
> Provider Identifier."

Medicare billing is not research. I am not a US healthcare recruiter. Nine of my
twenty-one first-day resources are Anthropic connector pages for clinical and pharma
operations.

**Level 4 is worse, in the opposite direction.** All twenty of "built things with it" —
Benchling, BioRender, Medidata, Owkin, 10x Genomics, scVI-Tools, Nextflow, "Prior Auth
Review", "Clinical Trial Protocol Draft Generation" — and **not one page about writing,
citation, disclosure or journal policy**. Level 2 had ICMJE, IEEE, Elsevier and Nature.
Level 4 has none of them. The site's model of a researcher who has *got better* at Claude
is a wet-lab biologist with an enterprise Benchling tenant. If I am a historian, an
economist, a sociologist or an engineer, the top level of my role is empty of my field
and full of pharma.

**Who it harms:** every non-life-sciences academic, which is most academics. Levels 1 and
4 send them into a catalogue that has visibly nothing for them, while levels 2 and 3 —
which do — sit between.

The counters, incidentally, are honest. Picking "a student" + "built things with it"
shows **"0 resources match so far."** *before* you submit, and the destination says: *"We
have nothing for this combination yet. It's on the list. Loosen the level, or browse
everything."* Three of forty role-level cells are zero-or-near-zero (student|builder = 0,
teacher|builder = 2, writer-marketer|builder = 3). Told up front. Fine.

---

## 3. What the catalogue gives me

The cards do the thing the site promises. Real example, quoted whole:

> **"How up-to-date is Claude's training data?"**
> **Skip if:** "It states the limit and offers no way round it: web search, which is the
> actual answer, is never mentioned. Read it for the dates, then go and turn search on.
> The page also carries no visible publication date — it says only 'updated this week' —
> so the cutoffs it lists are current on the day you read it and not before."

That is a reviewer's note, not a blurb. Several are better than the resource they
describe.

Three things a citing reader notices immediately.

**Publisher names are mangled.** `libguides.und.edu` is printed as source **"Und"** — the
card reads "Und · Chester Fritz Library". That is the University of North Dakota.
`master.dev` is printed as **"Master"**. Another is printed as the raw domain
**"qwe.edu.pl"**. In a directory whose whole selling point is judgment about sources, the
publisher field is derived from the domain and sometimes derives nonsense.

**"pay once" is not a price.** Ten paid items in 635. The chip on the card says `pay
once`. The actual figure is buried in prose — `Academic Research with Claude (live
seminar)` is **$995**, and you only learn that if you read to the middle of its Skip-if
line. Nine of those ten paid items carry the **Skimmed** badge: recommended without
having been seen inside.

**No DOIs.** `Claude AI and Literature Reviews: An Experiment in Utility and Ethical Use`
carries the byline *"Max Sparkman & Alan Witt, Library Trends 73(3):355-380"* — journal,
volume, issue, page range — and no DOI, and no publication date (see section 7).

---

## 4. Paths

There is a route for me: **"Using Claude for research without embarrassing yourself"** —
*"Researchers and academics who want the speed without the retraction."* Five steps, ~2
hours, "some paid steps". This is the best thing on the site.

Every step reason justifies its **position**, not just the resource:

1. Reduce hallucinations — *"Start with the failure, not the feature. Fabricated citations
   are the one mistake that ends careers."*
2. What are Projects? — *"Set it up before you have forty loose chats."*
3. Claude AI and Literature Reviews — *"Now read someone who actually tried it and
   reported what broke, with the guard rails from step 1 in place."*
4. Zotero + Cowork — *"Until Claude can see your actual sources, everything above is a
   demo."*
5. ICMJE — *"Before you submit anything, read what the ICMJE expects you to declare."*

Step 3 explicitly depends on step 1. Step 4 explicitly invalidates steps 1-3 without it.
That is real sequencing.

Three failures.

**a) The path drops the "Skip if:" line.** Path pages show the step reason, the tier, and
the checked date. No "Skip if:", no "For:". So step 5's reason ends **"This is not
optional and most people learn it too late."** — while the browse card for the same item
says:

> **Skip if:** "Your field follows a different body (still align with your target
> journal)."

ICMJE is the International Committee of *Medical Journal Editors*. For a non-medical
researcher it *is* optional. The path states the opposite, flatly, and hides the sentence
that corrects it. The home page's own promise is *"Every entry has a Skip if: line. A link
with no judgment is just a list."* The paths — the most opinionated product on the site —
are that list.

**b) All five sources have no publication date.** Every step: "No publish date given". A
path about not embarrassing yourself in print, built on five undated sources.

**c) Step 3 is a paywall with no exit.** `muse.jhu.edu` Library Trends, "pay once", no
figure. No free alternative offered, no "skip if you have no institutional access". You
are five steps in and the middle one is a till.

I also read the data path. Its step 4 is **`qwe.edu.pl · QWE AI Academy`** — a `.edu.pl`
domain with no identifiable institution, whose own Skip-if line begins *"One idea makes it
worth **the unknown byline**"*, tier **Skimmed**, no publication date, no author. The site
knows the byline is unknown and made it a required step in a curated path about getting
numbers right. I would reject that source in a review.

Small thing: the paths index truncates step titles mid-word — *"ICMJE Recommendations —
Use of AI in Publish..."*, *"Connect and integrate your local Zotero libr..."* — and one
path is billed as **"about 81 minutes"** next to siblings billed "about 4 hours". A
machine number wearing prose.

---

## 5. The card and the resource page

Resource pages are well built: H1 plus five H2s, 14 tab stops, `rel="noopener noreferrer"`
on the outbound link, "Open on <publisher>", and a plain-English tier explanation. I would
click through from most of these. The Skip-if lines are the reason.

Then two defects.

**The staleness warning exists on the list and not on the page.** `Building effective
agents`:

- Browse card: *"Checked 5 Sep 2026 / **Published over a year ago — may not match Claude
  today**"*
- Resource page `resource.html?id=r-7d24e5faa2`: *"Checked 5 Sep 2026 · Published 19 Dec
  2024 · Found through Anthropic"* — **no warning at all.**

Neither page shows both the date and the flag. The page you land on from a search engine,
or from the site's own "Copy link", is the one without the flag.

**The "Updated" line disappears too.** `Claude Design Fundamentals` carries `updated:
2026-05` in the data. Its resource page says only *"No publish date given"*. The one date
the site holds for that item is not shown on the item's own page.

**Copy link.** Pressing it turned the button's label into **"Press Ctrl+C"**. There is no
`aria-live` region anywhere on the page (0 found), so nothing is announced. A
screen-reader user presses the button, hears nothing, and is not told that a manual
keystroke is now required.

---

## 6. The picks block

**Are they the first three rows? No — and I checked.** For `researcher|used it a lot`, the
sort is "Best checked first" and the picks are all **Skimmed** items checked 18 Aug, 29 Aug
and 5 Sep, while "Everything else" opens with *"Anthropic's AI for Science Program"*, a
**Read by AI** item checked 5 Sep — which outranks all three on the default sort. The
picker reached past the top of the list. That is real work, not `head -3`.

**Do the reasons add something? Mostly yes.** They are comparative — they describe the
*pool*, not the resource:

> *"The actual course in a pool where the other course-shaped candidate is a catalog
> pointing at it."*
> *"Ten candidates here have been read in full, and this is the only one of them that
> walks a research workflow end to end rather than stating a policy or explaining a
> feature."*
> *"Three journal-policy candidates, and this is the only one not tied to a single
> publisher — IEEE and Elsevier each bind their own journals."*
> *"The rarest habit in the pool — recomputing a paper's statistics from the authors' own
> raw data before citing it, which nothing else here does."*

That third one is the best sentence on the site. It tells me *why not the other two*,
which is what a recommendation is.

**Do my three never-used picks feel independent? No.** Two of three are Anthropic's own,
out of a pool that is 19/21 Anthropic. And the third pick's own reason gives the game away:

> *"**The pool's first non-Anthropic voice**, and it is the only candidate that teaches you
> to judge an AI tool rather than to operate one."*

Selected because it is not Anthropic. And the card immediately under it says:

> **Skip if:** "**It is not about Claude.** Not one instruction here is Claude-specific."

So on a Claude directory, pick three is a page that is not about Claude, chosen for not
being Anthropic. That is a diversity quota being filled and narrated out loud.

Worse, pick two contradicts its own card. The pick reason sells it as *"the retention
answer from the company itself"*. The card says:

> **Skip if:** "It covers Free, Pro and Max only. If your data sits on Team, Enterprise or
> the API the answers are different and **this is the wrong page**."

University researchers are overwhelmingly on institutional Team/Enterprise plans or the
API. The "start here" sentence recommends it; the sentence below says it is the wrong page
for me. The pick reason does not carry the caveat, and the pick reason is what the block is
selling.

**Does "picked by AI" raise or lower trust? It raises it, and then the numbers lower it
again.** Naming the picker is right. Across all 37 pick cells, **47 of 109 picks (43%) are
Anthropic's own, against 61% of the catalogue** — the picker is measurably *less*
vendor-tilted than the pool it draws from, and only 1 of 37 cells is all-Anthropic. Credit
for that.

But: of those 109 picks, **81 are "Skimmed" and 28 are "Read by AI". Zero are "Read in
full."** Every "Start with these three" on this site points at something no person has
verified, and three-quarters at something nobody read all of. And **70 of 109 (64%) have
no publication date**. "Picked by AI" is honest about the picker. It is silent about the
fact that the picker was choosing between things nobody opened.

Also: 3 of 40 cells have no picks block at all. `student|builder` renders zero results and
no block, which is correct; the block is simply absent elsewhere with no explanation.

---

## 7. Dates and tier badges

Measured from the site's own data file, not estimated:

- **489 of 635 (77%) carry `published: "UNVERIFIED"`** which the card renders as **"No
  publish date given"**. Three in four.
- **96 carry an "Updated" date. 44 of those show "Updated <date>" with no publication date
  at all.**
- **3 show a month only** — "Updated May 2026", "Updated June 2026", "Updated February
  2026".
- Only **146 of 635** carry a real publication date.

**Does this look maintained or abandoned? Neither — it looks like a bibliography with the
year column deleted.** That is a specific and worse thing. An abandoned site has old
dates. This site has *"Checked 5 Sep 2026"* on almost everything, which reads as
maintained, sitting next to *"No publish date given"*, which means the one date that
determines whether the content is true is missing. "Checked" tells me when someone looked
at a page. It does not tell me when the page was written. For AI tooling those are months
apart and the second is the one that matters.

The worst single instance: **`Claude AI and Literature Reviews: An Experiment in Utility
and Ethical Use`**, byline *"Library Trends 73(3):355-380"*, publication status: **"No
publish date given"**. The site holds the volume, the issue and the page range of a
peer-reviewed article and cannot state its year. It is step 3 of my path. I cannot put
that in a reference list from this page.

The site's methodology promises *"When something drifts out of date, the date says so
before we do."* With no publication date on 77% of entries, the date says nothing about 489
items.

**Tier badges.** The ladder is stated plainly and I like the ladder:

> **Read in full** — "We went through all of it and a person checked the notes."
> **Read by AI** — "AI read all of it. No person has checked the notes yet."
> **Skimmed** — "We read the outline or a free sample."
> **Found only** — "We found it and sorted it. **Nobody has looked at the content yet.**"

Distribution: **501 Skimmed, 98 Read by AI, 36 Found only.** The badges tell me the work
behind this site is one automated harvest with a language model writing the notes, and no
human editorial pass anywhere.

And then the ladder breaks — see finding 1 below.

---

## 8. Search, in my words

Five queries a researcher types. Every one recorded, with the top three.

**Q1 — `does claude make up citations`** -> *47 resources*
1. "Claude AI for Researchers: Projects, Skills, Cowork & Consensus Explained" — a feature
   tour.
2. **"Use Claude for Excel"** — a spreadsheet add-in.
3. "Use research on Claude" — about usage limits.

**Verdict: failed.** The one question I arrived with returns a spreadsheet add-in at
number two. The site *has* the right answers — `Reduce hallucinations` (Anthropic Platform
docs), `Why do AI models hallucinate?` — and neither appears anywhere in the 47. The
site's own best-matched card, *"3 Mind Blowing Claude & Consensus Research Workflows"*,
whose For-line literally reads *"...and are worried about Claude inventing citations"*, is
ranked **sixth**.

**Q2 — `systematic literature review`** -> *8 resources*
1. **"Mushtaq Bilal — Claude for Academic Writing & Research"**
2. "Claude AI and Literature Reviews: An Experiment in Utility and Ethical Use"
3. "Claude Researcher — source-first literature review workflows"

**Verdict: failed at #1, fine at #2-3.** The site's own card for the #1 result says: *"Skip
if: Skip if you will not hand over an email address: every post is behind a subscribe
form, so there is nothing to read until you sign up. Skip too if you want teaching rather
than marketing — the recent posts are almost all registration pages for his own webinars
and paid tools."* The site knows it is a mailing-list funnel and ranks it first.
Separately: the word "systematic" contributed nothing. No PRISMA screening, no dual
extraction, no risk-of-bias. Zero results about actual systematic reviews.

**Q3 — `hallucinated references`** -> *7 resources*
1. "Connect and integrate your local Zotero library with Claude Cowork"
2. "Claude Skills for Academics (Beginner Tutorial, Part 2)"
3. "Claude Researcher — source-first literature review workflows"

**Verdict: good results, broken engine.** These three are the right three. But `Reduce
hallucinations` is **not among them** — because I typed "hallucinated" and the page says
"hallucinations". I re-ran `hallucinations` alone: **6 results, "Reduce hallucinations" at
#1 and "Why do AI models hallucinate?" at #4** — neither of which appeared in Q3, and
neither of which appeared in Q1. **Three searches for one concept return three disjoint
answer sets.** There is no stemming; matching is literal substring.

**Q4 — `peer review`** -> *15 resources*
1. **"Peer and AI Review of Student Writing with Marit MacArthur and Anna Mills"** —
   classroom peer feedback on undergraduate essays.
2. "Claude AI and Literature Reviews"
3. "Nature Portfolio — Artificial Intelligence (AI) editorial policy" — correct and useful.

**Verdict: half failed.** #1 is the wrong sense of the word. And the site's own IEEE card
contains the single most important sentence in the catalogue for a reviewer — *"a reviewer
may not put a manuscript through a public AI tool at all"* — and IEEE does not make the top
eight, because the card says "reviewer" and I typed "peer review".

**Q5 — `how do I cite Claude in a paper`** -> *14 resources*
1. "IEEE — Author Guidelines for AI-Generated Text"
2. "Documenting Your AI Use"
3. "Referencing AI and Acknowledging AI Use"

**Verdict: correct.** The only clean run of the five. Below the fold it degrades — #4 is
*"Using Claude Cowork for legal: answer fast questions on past decisions"* and #5 is *"Using
Daloopa for financial analysis"*, matched on "paper" and "a" — but the top three are right.

**Score: 1 of 5 good, 1 of 5 half-right, 3 of 5 failed.** The failure mode is consistent:
literal substring OR-matching with no stemming, so natural questions return long lists
ranked by nothing that resembles relevance, while single keywords work.

---

## 9. On a phone

375x812. Clean. `document.scrollWidth === clientWidth` — **no horizontal overflow anywhere
I looked**. Filters collapse into a fixed bottom "Filters" bar; search and sort stay at the
top; the picks block reflows to one column. Type is large and readable. Nothing is cut off.

Only nit: six link targets measure 24px tall (single-line card titles like "What are
Projects?"), under the 44px guideline. Multi-line titles are fine. The card body is not
clickable — only the title text is.

This is the strongest part of the build. It works.

---

## 10. Keyboard walk

Walked `browse.html?role=researcher&level=basic` and `resource.html?id=r-69ee3c03e3`.

**Good, and I checked it rather than assumed it:**
- Focus ring is real and visible: `outline: solid 2px rgb(20,20,19)` with 2px offset.
- Filter chips are `<button role="checkbox">` with correct `aria-checked="true"/"false"`,
  all focusable, Space and Enter work natively.
- "More filters" carries `aria-expanded="false"`.
- The result count is `aria-live="polite"` — filter changes are announced.
- The hidden mobile filter sheet is `display:none`, so its 38 duplicate checkboxes are
  **not** in the tab order. No trap.
- Resource page: 14 tab stops, clean H1-H2 outline, skip link, "Back to browse".

**Broken:**

- **"Skip to content" lands you 24 tabs from the first result.** The skip link targets
  `#main`, and the whole filter sidebar lives inside `<main>` before the results. From the
  skip target: 18 filter checkboxes, "Clear all", "More filters", search, sort, then two
  active filter chips — *then* result #1. There is no "skip to results". A keyboard user
  who clicks a result, reads it, and presses Back does all 29 tabs again to reach result
  #2.
- **Twenty-one results, zero headings.** Card titles are `<a>` inside `<div
  class="card-title">`. The heading outline of the browse page is: H1 Browse, H2 Filters,
  H3 Role/Level/Time/Topic/Format/Cost/Source, H2 "Start with these three", H2 "Everything
  else for you (18)". Not one heading for any of the 21 results. A screen-reader user
  cannot jump result to result by heading — the site's primary content is invisible to the
  primary navigation method.
- **No status region on "Copy link"** (0 `aria-live` regions on the resource page), and it
  swapped its own label to "Press Ctrl+C" silently.

---

## 11. How we check

**Less. Clearly less, and the page does it to itself.**

It opens with a principle:

> **"We would rather have 70 resources we can vouch for than 700 we cannot."**

Four paragraphs later it reports the outcome:

> **"Right now: 635 resources — 98 read by ai, 501 skimmed, 36 found only. Nothing is read
> in full yet, and the cards say so."**

By its own definition — "Read in full: We went through all of it and a person checked the
notes" — the site has **0 resources it can vouch for and 635 it cannot.** It states a
preference for 70-over-700 on a page reporting 635-and-zero. That is not candour, it is a
mission statement printed above its own contradiction.

Second contradiction, six lines apart:

> "We do not list something we cannot open."
> ...
> "**Skimmed** — We read the outline or a free sample. **Paid courses usually stop here,
> because we cannot see inside them.**"

It lists things it cannot open, and says so in the paragraph explaining why it cannot open
them. Nine of the ten paid items are Skimmed, including a $995 four-day seminar.

**On the 61%.** *"390 of those 635 (61%) are Anthropic's own — official just means who
published it, not how good it is, so the rest are here because they passed the same check,
not a lower one."* I verified it: 390/635 = 61.4%. Exact.

Is it candour or a shopfront confession? **Candour about the number, shopfront in the
fact.** The sentence is honest and the defence is a non-sequitur — "the rest passed the
same check" explains why the *other 39%* are trustworthy, not why the vendor holds 61%. And
the number is worse where it matters. In my own beginner cell it is **19 of 21 (90%)**; in
my expert cell **18 of 20 (90%)**. The site-wide 61% is the flattering version of a figure
that reaches 90% in two of my four cells. Disclosing the average while the distribution is
far worse in specific places is a partial disclosure.

The certification paragraph is the best on the site and I want to say so: *"Anthropic runs
a real certification, but it is open to members of the Claude Partner Network, not to the
public. A lot of sites sell preparation for an exam most readers cannot sit. If you find
one of those, that is why it is not in here."* That is a stated exclusion criterion with a
reason. More of that.

---

## 12. Everything broken, ranked

### 1. "Found only — nobody has looked at the content yet" — and then four paragraphs of judgment about the content. Severity: critical.

**URL:** `resource.html?id=r-960acd1524`
**Did:** Opened the only "Found only" item in my role.
**Saw:** Badge and explanation: **"Found only. We found it and sorted it. Nobody has looked
at the content yet."** On the same page:

> *Summary:* "Princeton's page on when and how to disclose AI use in research and
> scholarship, **aimed slightly higher up the ladder than undergraduate coursework
> guides**."
> *What it teaches:* "Determine when research scholarship requires formal AI disclosure" /
> "Apply institutional standards to thesis writing documentation"
> *Skip it if:* "You are writing ordinary coursework. **The Melbourne, Warwick or Tulane
> pages give you more usable templates for that.**"

That final sentence compares this page against three other named institutional pages on
template quality. You cannot make that judgment without reading four documents.

**Systematic, not one card:** all **36 of 36** "Found only" items carry a summary, a
who-it's-for, a skip-if (167 characters on average) and three "what it teaches" bullets.
Two more, quoted: *"Nothing in it visibly tells you to check Claude's arithmetic"* — a
claim about the interior of a course. *"It takes live database credentials and has..."* — a
security claim about an MCP server. Nobody looked at either.

**Expected:** a badge meaning "unread" produces a title, a link, and nothing else.
**Harms:** everyone, and it destroys the site's only trust mechanism. The tier ladder is
the product. If "Nobody has looked at this" and "Read by AI" produce identically confident
prose, no badge on the site means anything, including the 501 that say "Skimmed".

### 2. Search fails the question the site exists to answer. Severity: critical.

**URL:** `browse.html?q=does%20claude%20make%20up%20citations`
**Saw:** 47 results. **#2 is "Use Claude for Excel."** The site's two on-point pages —
`Reduce hallucinations`, `Why do AI models hallucinate?` — appear in **none** of the 47.
**Proof of cause:** `?q=hallucinations` -> 6 results, `Reduce hallucinations` at #1.
`?q=hallucinated references` -> 7 results, `Reduce hallucinations` absent. Literal
substring, no stemming. Three phrasings of one concept, three disjoint answer sets.
**Expected:** the top result for "does claude make up citations" is the page called "Reduce
hallucinations".
**Harms:** the researcher arriving with exactly the anxiety this site is best equipped to
answer. The good content exists and the search hides it behind vocabulary.

### 3. Seventy-seven percent of entries have no publication date, including a journal article with its volume and page range on screen. Severity: high.

**URL:** `resource.html?id=r-69ee3c03e3`
**Saw:** Byline *"Johns Hopkins University Press · Max Sparkman & Alan Witt, Library Trends
73(3):355-380"*. Footer: *"Checked 5 Sep 2026 · **No publish date given** · Found through
Johns Hopkins University Press"*. No DOI.
**Data:** 489/635 (77%) `published: "UNVERIFIED"`. 44 items show "Updated <date>" with no
publication date. 3 show a month only.
**Expected:** a directory whose home page advertises *"We show the date"* shows the date,
especially where the citation string is already on the card.
**Harms:** anyone who cites. "Checked" is when the site looked. Only "published" tells me
whether the content predates the model it describes. I cannot use this as a bibliography,
which is the only reason I would return.

### 4. Levels 1 and 4 of my role are the wrong shelf. Severity: high.

**URLs:** `browse.html?role=researcher&level=never-used`, `...&level=builder`
**Saw:** Level 1 — 9 of 21 are Anthropic Academy clinical connector pages ("Medical coders,
billers, and prior authorization specialists"; "Healthcare administrators, credentialing
staff, and healthcare recruiters"). 19 of 21 Anthropic-published. Level 4 — all 17
"Everything else" entries are pharma/biotech connectors and skills (Benchling, Medidata,
Owkin, 10x Genomics, Prior Auth Review, Clinical Trial Protocol). 18 of 20
Anthropic-published. **Zero** items about writing, citation, disclosure or journal policy
at level 4, where levels 2 and 3 have ICMJE, IEEE, Elsevier, Nature and the Library Trends
study.
**Expected:** "researcher" delivers research work, and getting more advanced does not
delete the journal-policy material.
**Harms:** every academic outside the life sciences — humanities, social sciences,
engineering, physics, most of the university. The site's first impression and its top tier
are both a pharma catalogue.

### 5. Paths hide the "Skip if:" line, and one path states the opposite of it. Severity: high.

**URL:** `paths.html?id=research-with-claude`
**Saw:** Step 5, ICMJE, reason: *"Before you submit anything, read what the ICMJE expects
you to declare. **This is not optional** and most people learn it too late."* Path pages
show no "Skip if:" and no "For:" for any step.
**Browse card for the same item:** *"**Skip if:** Your field follows a different body (still
align with your target journal)."*
**Expected:** the home page says *"Every entry has a Skip if: line. A link with no judgment
is just a list."* The paths are the most confident pages on the site and the only ones with
no Skip-if.
**Harms:** non-medical researchers, told flatly that a medical-journal body's rules are "not
optional" for them. Also step 4's caveat — *"Working from your own library reduces the risk
without removing it"* — vanishes on the path, which is precisely the sentence that keeps
someone checking their references.

### 6. The staleness warning appears on the list and not on the page. Severity: medium.

**URLs:** `browse.html?q=Building%20effective%20agents` vs `resource.html?id=r-7d24e5faa2`
**Saw:** Card — *"Checked 5 Sep 2026 / **Published over a year ago — may not match Claude
today**"*. Page — *"Checked 5 Sep 2026 · Published 19 Dec 2024 · Found through Anthropic"*,
no warning. Neither view shows both the flag and the date. Separately, `Claude Design
Fundamentals` holds `updated: 2026-05` and its resource page shows only "No publish date
given".
**Expected:** the detail page is a superset of the card.
**Harms:** anyone arriving from a search engine or from a link produced by the site's own
"Copy link" button — which is to say, the shared link is the version with the warning
removed.

### 7. Publisher names are derived from the domain and sometimes wrong. Severity: medium.

**URL:** `browse.html?role=researcher&level=never-used`
**Saw:** *"AI: Artificial Intelligence Resources: Claude — **Und** · Chester Fritz
Library"* (`libguides.und.edu` = University of North Dakota). Also source **"Master"** for
`master.dev`, and the raw domain **"qwe.edu.pl"** printed as a publisher.
**Expected:** correct attribution on a site whose product is judgment about sources.
**Harms:** a reader deciding whether to trust a source by its publisher, and the librarians
whose work is credited to "Und".

### 8. The picks block's one-liner contradicts the card underneath it. Severity: medium.

**URL:** `browse.html?role=researcher&level=never-used`
**Saw:** Pick 2 reason: *"the retention answer from the company itself, and the pool's only
candidate that addresses it at all."* Same card, 30 words above: *"**Skip if:** It covers
Free, Pro and Max only. If your data sits on Team, Enterprise or the API the answers are
different and **this is the wrong page**."* Pick 3 reason: *"The pool's first non-Anthropic
voice."* Same card: *"**Skip if:** **It is not about Claude.** Not one instruction here is
Claude-specific."*
**Expected:** the sentence saying "start here" survives contact with the sentence saying
"this is the wrong page".
**Harms:** university researchers, who are mostly on institutional Team/Enterprise plans —
the exact readers pick 2's own card excludes.

### 9. Every "Start with these three" points at unverified material. Severity: medium.

**Data across all 37 pick cells:** 109 picks — **81 Skimmed, 28 Read by AI, 0 Read in
full**. 70 of 109 (64%) have no publication date.
**Expected:** the block that says "start here" draws from the top of the verification
ladder, or says that it cannot.
**Harms:** the beginner, who by construction trusts the picks block most and can least
assess it. The label "picked by AI" discloses the picker and conceals that the picker chose
between things nobody opened.

### 10. Twenty-one results, zero headings; 24 tabs from the skip link to result #1. Severity: medium.

**URL:** `browse.html?role=researcher&level=basic`
**Saw:** Card titles are `<a>` inside `<div class="card-title">`, not headings. The page's
heading outline contains no result. `#main` contains the entire filter sidebar, so from the
skip target it is 24 further tab stops to the first result link and there is no "skip to
results".
**Expected:** results are headings; the skip link skips to results.
**Harms:** screen-reader and keyboard users, who cannot use heading navigation on the site's
primary content and re-tab the filter panel after every Back.

### 11. "We would rather have 70 we can vouch for than 700 we cannot" — on a page reporting 635 and zero. Severity: medium.

**URL:** `how-we-check.html`
**Saw:** That sentence, then *"Nothing is read in full yet"*. Also *"We do not list
something we cannot open"* six lines above *"Paid courses usually stop here, because we
cannot see inside them."*
**Expected:** either the stated policy or the reported outcome, not both.
**Harms:** the reader who reads the methodology page specifically because they want to know
how far to trust the rest — and finds the page arguing against itself.

### 12. Home page: "635 resources, checked by hand." Severity: medium.

**URL:** `index.html`
**Saw:** That sentence, under the hero. The methodology page: *"Nothing is read in full
yet"*; the only tier that involves a person is *"Read in full — a person checked the
notes"*, count **0**.
**Expected:** the first claim matches the last.
**Harms:** everyone, and it is the one line a visitor is most likely to read and least
likely to check.

### 13. Price is not a field. Severity: low.

`Academic Research with Claude (live seminar)` shows the chip **`pay once`**. The **$995**
is prose inside the Skip-if line, along with the fact that it also requires a Claude Pro or
Team subscription. 10 paid items total; 9 are Skimmed. No price sorting or filtering.

### 14. Two questions, one fold. Severity: low.

At 1280x720 the "Show me" button renders above "How much Claude do you know?".

### 15. "Copy link" says nothing to a screen reader. Severity: low.

`resource.html` has zero `aria-live` regions. The button relabelled itself to "Press
Ctrl+C" with no announcement.

---

## 13. The one thing that would make me leave

**"Found only — nobody has looked at the content yet"** printed above a paragraph comparing
that resource against three named alternatives.

Everything on this site is one bet: that somebody exercised judgment and will tell me how
much. The tier ladder is that promise made explicit, and it is the reason to prefer this
over a Google search. Finding 36 items where the badge says *unread* and the body delivers
a full comparative review means the badge is decoration. And once the "Found only" badge
means nothing, "Skimmed" means nothing either — and 501 of 635 entries say "Skimmed".

For me specifically it lands twice. The one thing I need from any tool touching my
bibliography is that it tells me what it does not know. A site that writes confident prose
about documents it admits it has not opened is doing the exact thing I am afraid of Claude
doing. The failure mode I came here to avoid is the failure mode of the site.

Close second: the Library Trends article with its volume, issue and page range on screen
and "No publish date given" underneath. That one told me in three seconds that I cannot
cite from this.

---

## 14. What is genuinely good

- **The "Skip if:" line is the best idea in this category.** *"It states the limit and
  offers no way round it: web search, which is the actual answer, is never mentioned."*
  *"The title is wrong for what this is."* *"Two hundred and fifty words is an orientation,
  not a tutorial."* These are review notes. Nobody else writes them.
- **The picks are not the top three rows, and I checked.** In `researcher|confident` the
  picker reached past a higher-ranked item to choose three lower-ranked ones. The reasons
  are comparative — *"Three journal-policy candidates, and this is the only one not tied to
  a single publisher"* — which is what a recommendation actually is.
- **43% vs 61%.** Across all 109 picks, Anthropic's share is 43% against a catalogue that
  is 61% Anthropic. Only 1 of 37 cells is all-Anthropic. The picker actively counteracts
  the vendor tilt. That is worth more than the disclosure paragraph.
- **Paths explain position, not just content.** *"Start with the failure, not the
  feature."* *"Until Claude can see your actual sources, everything above is a demo."*
  *"Second, and second on purpose."* Almost no learning-path site does this.
- **The tier vocabulary itself.** *"AI read all of it. No person has checked the notes
  yet."* Naming the reader as a machine is the right instinct, executed better than anyone
  else in this space, and undermined only by the Found-only cards.
- **Mobile is correct.** No overflow at 375px, filters in a bottom sheet, everything
  readable.
- **The empty state is honest.** *"We have nothing for this combination yet. It's on the
  list."* — and the counter says "0 resources match so far." before you commit.
- **The certification paragraph** — a stated exclusion criterion with a reason for it.
- **Real accessibility work underneath:** `role="checkbox"` with correct `aria-checked`,
  `aria-expanded` on the disclosure, `aria-live="polite"` on the result count, a visible
  2px focus ring, `rel="noopener noreferrer"` on outbound links, a working skip link.
  Somebody cared. They just did not put headings on the results.

The prose here is better than the machinery. Fix search, fix the dates, and stop writing
reviews of things nobody opened — and I would use this.

---

## Checklist
- [x] I opened the live site at all four levels of my role — 21 / 21 / 21 / 20
- [x] I quoted at least 5 real titles or lines from the site — 30+
- [x] Every number I used is computed from the shipped data, or the command is shown
- [x] I looked at a phone width — 375x812
- [x] I did one full keyboard walk — browse + resource
- [x] Five search queries in my own words, each with its verdict
- [x] I read the picks block and tested whether it is the top three rows — it is not
- [x] I found at least one thing nobody has mentioned before — the 36 "Found only" cards
      carrying full comparative reviews, including one that ranks three named institutional
      pages it says nobody opened
