# Attack 3: a researcher
Written as a researcher, 2026-09-06. Site version: 9deb0db.

I am a postdoc. I read and screen literature, I write manuscripts, and I review for two
journals. My single fear is a fabricated citation reaching a paper with my name on it.
I judge a tool on provenance: who read this, when, and can I check it.

---

## 1. The first 60 seconds

I opened `https://mojtaba-alehosseini.github.io/learn-claude/`.

The page says "Find what's worth your time." and under it a sentence with two blanks:
"I'm a [role] and I've [level]." Below that, three promises:

- "We say when to skip — Every entry has a `Skip if:` line. A link with no judgment is
  just a list, and lists are what made this hard in the first place."
- "We say how we checked — Four levels, and we do not round up. If nobody has opened it,
  the card says so."
- "We show the date — Claude changes every few months. You can see when we last looked,
  and whether the thing is old."

That is the correct pitch for me. It is the pitch of a methods section, not of a landing
page. No sign-up. No cookie banner. No email capture. The footer says "Learn Claude is an
independent directory. It is not affiliated with Anthropic."

I clicked "a researcher". The sentence completed itself — "I'm a researcher and I've
never used Claude." — and a line appeared: "19 resources match so far." A microscope was
drawn beside it. Small thing, but it told me the site knows what a researcher is.

**Watching without touching.** I left the home page alone and took screenshots at 0s, 3s
and 7s. An attract loop runs: it lights one role chip at a time and swaps the drawing
beside it — a node graph, a house, a coffee mug. I sampled the DOM every 900 ms for
12.6 s. The `<h1>` never changed: `"Find what's worth your time."` at every sample. The
loop moves the chips and the picture. It never once fills in the sentence "I'm a [role]
and I've [level]." So the one thing the loop could demonstrate — that the sentence
becomes a real sentence — is the one thing it does not demonstrate. I only learned that
by clicking.

Sixty-second verdict: I stayed. That is more than most directories get from me.

---

## 2. Does the front door work for me (all four levels, with what I was shown)

I answered "a researcher" and then each level in turn, and followed through to Browse
each time.

### never used Claude — `browse.html?role=researcher&level=never-used` — "19 resources"

"Start with these three":

1. **Claude 101** — Anthropic Academy — course, half a day, free
2. **Upload files to Claude (Help Center)** — Claude Help Center · Anthropic
3. **Generative AI Literacy** — Harvard University · Harvard Library

The reason under pick 2 is written for me and not for a generic beginner: "the only
candidate that names the ceilings before you hit them - 500MB in a chat against 30MB in a
Project, twenty files either way, which is exactly the wall a first manuscript runs into."
The reason under pick 3 says "The pool's first non-Anthropic voice ... the ROBOT test, a
checklist for deciding whether to believe what a tool claims about itself, which a
researcher needs before the first upload and not after."

That is good work. It is also, on the evidence of the other 16, the exception.

Of the 19 cards, **6 are Anthropic Academy connector documentation for biomedical
databases**: bioRxiv/medRxiv, Candid, ChEMBL, ClinicalTrials.gov, Open Targets, PubMed.
STATUS.md records this cell as `17 / 5p / 2x` — 17 eligible, 5 publishers, **2 items not
published by Anthropic**. So a researcher who has never opened Claude is handed a shelf
where two voices out of seventeen are independent, and a third of the shelf is drug
discovery.

### used it a little — `?role=researcher&level=basic` — "20 resources"

This is the best cell on the site for me. Picks:

1. **Plan your literature review** — Anthropic Academy — "Read by AI"
2. **3 Mind Blowing Claude & Consensus Research Workflows | No Coding** — Dr Amina Yonis
3. **ICMJE Recommendations — Use of AI in Publishing** — ICMJE

Behind them: **Nature Portfolio — Artificial Intelligence (AI) editorial policy**,
**IEEE — Author Guidelines for AI-Generated Text**, **Elsevier — Generative AI policies
for journals**, **Disclosing the Use of AI** (Princeton University Library). Four journal
bodies and a university library page, in one screen. Nothing else I have used collects
those.

The pick reason for #1 does something I have not seen a directory do: it states what the
source omits. "with our own note adding what the page omits: it never warns about
fabricated references."

### used it a lot — `?role=researcher&level=confident` — "32 resources"

Picks: **Connect and integrate your local Zotero library with Claude Cowork**,
**Verify statistics from raw data**, **Claude Cowork for Academics: Full Setup & Use
Cases**. All three are the right kind of thing.

Then the pool turns into a life-sciences catalogue. Inside the 29 "Everything else"
cards I count these Anthropic Academy pages: Genomic data analysis; Getting Started with
Claude for Life Sciences; Instrument Data to Allotrope; Scientific Problem Selection;
scVI-Tools bioinformatics skill bundle; single-cell-rna-qc; Preclinical study analysis;
BioRender; Owkin; Scholar Gateway; Synapse.org; ToolUniverse; Map your lit review; Turn
research into presentations; Chart your data. Fifteen of twenty-nine, from one publisher.

If I ran a wet lab this would be a gift. I do not. STATUS.md gives this cell as
`31 / 15p / 13x`, so the publisher spread is genuinely better than the never-used cell —
but the *volume* is Anthropic Academy's, and volume is what I scroll past.

### built things with it — `?role=researcher&level=builder` — "6 resources"

The page says: **"6 resources. Remove a filter to see more."**

Picks: **Claude Skills for Academics (Beginner Tutorial, Part 2)**, **zotero-mcp
(54yyyu)**, **How to use the Nextflow Deployment agent skill with Claude Code**. The
other three: 10x Genomics, Benchling, **ClaudeR (R + RStudio MCP)**.

Two of six are for a general researcher (zotero-mcp, ClaudeR). Three are bench biology.
STATUS.md gives `6 / 3p / 3x`.

**The "remove a filter" line is not clickable.** I inspected it: it is
`<p class="result-count">` with plain text inside. No link, no button. The empty state
*does* offer one-click escapes — I checked `?checked=reviewed` and got "We have nothing
for this combination yet. It's on the list. Loosen the level, or see everything for this
role, or browse everything." with live links. So the site has the affordance and does not
use it at 6 results, only at 0.

### Verdict on the front door

It works. Four honest answers, four different shelves, and the shelves really are
different. The failure is not the door. It is that "a researcher" is one word for a
population that splits, and the catalogue's centre of mass is a life scientist.

---

## 3. What the catalogue actually gives me (are these really for me?)

Mostly yes, with two structural problems.

**It is not one role.** I typed nothing about biology and I was handed ChEMBL, Open
Targets, single-cell RNA QC, Benchling, Owkin tumour slides, 10x Genomics and Nextflow.
Every one of those cards is well written. Every one of them is for somebody else. A
second question — "wet lab or not" — would fix more for me than any amount of ranking
work.

**The best card in my pool is not tagged to me the way I would search for it.**
"Reduce hallucinations" (Claude Platform docs) is in my `confident` pool. Its own words
are: "Who it's for — **Any analyst** worried about confidently-wrong output" and "Skip it
if — You want data-specific step-by-step recipes rather than general guardrails." The
card never says citation, reference, paper, manuscript or literature. But the researcher
path calls it "step 1 of 5" and labels it **"Start with this"** with the reason
"Fabricated citations are the one mistake that ends careers." The path knows what this
page is for. The card does not. See section 6 for what that costs.

**What is genuinely mine.** The journal-policy set (ICMJE, Nature, IEEE, Elsevier), the
Zotero route with both a terminal and a GUI option, the peer-reviewed study of Claude on
a literature review, and "Verify statistics from raw data". Those four things are the
reason I did not close the tab.

---

## 4. Paths

There are 7 paths. One is mine:

**"Using Claude for research without embarrassing yourself"** — "Researchers and
academics who want the speed without the retraction." — "For a researcher, a student" —
"5 steps · about 2 hours · some paid steps".

The title is the best sentence on the site. I followed it
(`paths.html?id=research-with-claude`):

1. **Reduce hallucinations** — "Start with the failure, not the feature. Fabricated
   citations are the one mistake that ends careers, and this is the clearest account of
   when they happen and how to cut them." Marked "Start with this".
2. **What are Projects?** — "Projects is where a literature review actually lives. Set it
   up before you have forty loose chats."
3. **Claude AI and Literature Reviews: An Experiment in Utility and Ethical Use** —
   "Now read someone who actually tried it and reported what broke, with the guard rails
   from step 1 in place." Chip: `pay once`.
4. **Connect and integrate your local Zotero library with Claude Cowork** — "Connect your
   own library. Until Claude can see your actual sources, everything above is a demo."
5. **ICMJE Recommendations — Use of AI in Publishing** — "Before you submit anything,
   read what the ICMJE expects you to declare."

All five are "Read by AI". The order is argued, not assumed. I would follow this.

**Is there a route at my level?** No. The path carries a role and no level. It starts at
"What are Projects?", a Help Center page the site itself files under `basic`. I have used
Claude for a year. Steps 1 and 2 are a re-read for me, and there is no marker saying
"start at 3 if you already have Projects". Every other path on the page has the same
shape: role, no level. So the answer to "is there a path at my level rather than at the
start" is that the site does not have levels for paths at all.

**Step 1 contradicts itself on prerequisites.** The path badges it "Start with this". Its
own resource page carries "Before this — Basic prompting experience with Claude."

**The paid step never says the price.** See finding 5.

---

## 5. The card and the resource page

I opened four resource pages. I would click through on three of them.

**`resource.html?id=r-146910f648` — ICMJE Recommendations.** Summary: "Authoritative
policy: disclose AI use in cover letter and manuscript; AI cannot be an author or be cited
as author; AI-generated material is not an acceptable primary source." Out-link:
`https://www.icmje.org/recommendations/browse/artificial-intelligence/`. That is the real
address. **I would click.** One complaint, and for a policy document it is the whole
complaint: the footer reads "Checked 5 Sep 2026 · No publish date given". The ICMJE
Recommendations are revised on a schedule. Which revision am I about to read? The site
does not know and does not tell me to check. For a policy page, the version *is* the
content.

**`resource.html?id=r-4ccc667a90` — Zotero + Claude Cowork.** Skip line: "You are hoping
this ends the fabricated-citation problem. Working from your own library reduces the risk
without removing it, and you still check every reference it hands back." That is the
sentence I would have written. **I would click.**

**`resource.html?id=r-69ee3c03e3` — Claude AI and Literature Reviews.** Byline: "Johns
Hopkins University Press · Max Sparkman & Alan Witt, **Library Trends 73(3):355-380**".
Footer: "Checked 5 Sep 2026 · **No publish date given** · Found through Johns Hopkins
University Press". The page prints a volume, an issue and a page range, and in the same
breath says it does not know when it was published. Those two lines cannot both be true.
I could construct the citation from what is on screen and still not have a year.
**I would click, and I would be annoyed on arrival.**

**`resource.html?id=r-9f57e8bf80` — a stripped `listed` card.** "Found only. We found it
and sorted it. Nobody has looked at the content yet." and "Skip it if — You want something
we have read. We have not opened this one yet."

**Do the stripped cards read as honest or broken?** Honest. That is a clean statement of
ignorance and I respect it. One crack: the same card asserts `podcast`, `half a day` and
`subscription`. Length and price are claims about content. If nobody opened it, the site
does not know it is half a day long, and it is asking me to pay for a subscription to
something it has not seen.

**Can I find out what the badge means?** Three answers, and only one of them is a full
yes.

- On a **resource page**: yes, in plain text. "How we checked this one — Read by AI. AI
  read all of it. No person has checked the notes yet. How we check."
- With a **screen reader** on Browse: yes. The card's title link carries
  `aria-describedby="tierdesc-previewed"` and the target text is
  "We read the outline or a free sample. We have not seen the whole thing."
- With a **keyboard and eyes** on Browse: no. The badge is
  `<span class="badge badge-previewed" title="We read the outline or a free sample...">`.
  A `<span>` with no `tabindex`. A `title` tooltip does not open on keyboard focus. A
  sighted keyboard user cannot reach the definition from the card at all.

---

## 6. Search, in my words

Five sentences, typed into the Browse search box the way I would actually type them.

| # | what I typed | top 3 I was shown | verdict | why |
|---|---|---|---|---|
| 1 | how do I stop Claude from making up references in my literature review | 1. Claude Researcher — source-first literature review workflows 2. 3 Mind Blowing Claude & Consensus Research Workflows \| No Coding (Dr Amina Yonis) 3. Plan your literature review (Anthropic Academy) | ok | #1 is a citation-checking protocol, #2's card names the exact fear ("worried about Claude inventing citations"). The site's own "Start with this" answer, Reduce hallucinations, only reaches #4. |
| 2 | does my journal require me to declare that I used AI in the methods section | 1. ICMJE Recommendations — Use of AI in Publishing 2. Nature Portfolio — Artificial Intelligence (AI) editorial policy 3. IEEE — Author Guidelines for AI-Generated Text | ok | The three bodies that would actually rule on it, in a defensible order. Best result the site gave me. |
| 3 | can Claude read the PDFs in my Zotero library | 1. zotero-mcp (54yyyu) 2. zotero-mcp-setup (GUI installer) 3. Connect and integrate your local Zotero library with Claude Cowork | ok | Exact. Putting the GUI installer next to the terminal project answers the question I did not ask yet. |
| 4 | is it safe to upload an unpublished manuscript I am peer reviewing | 1. Nature Portfolio — Artificial Intelligence (AI) editorial policy 2. Peer and AI Review of Student Writing with Marit MacArthur and Anna Mills (Derek Bruff) 3. Claude AI and Literature Reviews: An Experiment in Utility and Ethical Use | ok | It barely earns this. Nature's policy does cover reviewers, so a useful answer is at #1. But #2 is a classroom podcast matched on the words "peer" and "review", and the blunt answer — the IEEE card's "a reviewer may not put a manuscript through a public AI tool at all" — sits at #5. On the highest-stakes question I have, the site made me scroll. |
| 5 | how do I check whether the statistics in a paper are actually reproducible | 1. Verify statistics from raw data (Anthropic Academy) 2. ClaudeR (R + RStudio MCP) 3. Claude for medical literature search: Avoid hallucinations | ok | #1 is precisely the task and its skip line tells me what I must have first ("Needs both the published manuscript PDF and the authors' own raw data XLSX"). #2 is the right tool for doing it. |

**The same question asked two ways.** I asked "how do I stop Claude from making up
references in my literature review", then asked it again as "Claude gave me a citation
that does not exist, how do I avoid that".

**The site did not agree with itself.** Not one card appears in both top threes. Wording A
returned Claude Researcher / Dr Amina Yonis / Plan your literature review. Wording B
returned Claude for medical literature search: Avoid hallucinations / Claude is providing
incorrect or misleading responses / **Remote MCP Servers directory**, with **Hooks in
Claude Code — Full Theory + Practical Use** at #4 and **Using Claude Cowork for legal** at
#5. Wording B returned 11 results and "Reduce hallucinations" was not among them.

I tried a third wording from the home page — "how do I keep Claude from inventing
references" — and got 58 results, with "Design Systems in 2026: Turn Your System into a
Claude Skill" at #4. I searched all 58 titles: **"Reduce hallucinations" is not in them.**

---

## 7. On a phone

I set the viewport to 375x812 and went through home, Browse and a resource page.

It holds up. `document.documentElement.scrollWidth` is 375 on Browse — no horizontal
scroll. Nothing is clipped. The illustration is dropped, which is the right call.

The filter rail becomes `display:none` and a "Filters" button appears. Tapping it opens a
full-height sheet. I measured it: the sheet is 375x812, its `.sheet-body` scrolls
(`scrollHeight` 2286 against `clientHeight` 650), body scroll is locked, and the sheet is
footed by a pinned **"Show 32 resources"** button at y=744-796, inside the viewport. Every
option is a 44 px row. That is a competent mobile sheet, not a desktop panel squeezed.

Two small things. The level question is `display:none` until a role is chosen, so on a
phone the first screen is one question, not two — that is better, not worse. And "How
well checked" sits about 2030 px down inside a 650 px scroller, so filtering by provenance
on a phone is three and a half swipes into a list.

Mobile is the part of this site I have the least to say about, which is a compliment.

---

## 8. What changed since Attack 2 — my verdict on each

**Does the level filter return work at my level, or undergraduate material?**
It returns work at my level. `never-used` gave me orientation pages, `basic` gave me
journal policy, `confident` gave me Zotero and statistics verification, `builder` gave me
MCP servers. The ladder is real. What it does not do is separate a wet-lab researcher from
me, and at `confident` that costs me fifteen of twenty-nine cards.

**Do the stripped `listed` cards read as honest or broken?**
Honest. "Skip it if — You want something we have read. We have not opened this one yet."
is a better sentence than most sites manage about anything. The crack is that the same
card still asserts `half a day` and `subscription` about content nobody opened.

**Can I find out what the "how well checked" badge means?**
On a resource page, yes, in plain text. With a screen reader on Browse, yes, via
`aria-describedby`. With a keyboard and working eyes on Browse, no — the badge is a bare
`<span>` with a `title` attribute, and `title` needs a mouse.

**Does the ladder mean anything if the top rung is empty?**
Less than it should. I clicked "Read in full" on Browse. Sitewide, `?checked=reviewed`
returns **"Browse 0 Claude resources"**. STATUS.md agrees: `reviewed` 0 of 588. The
ladder is still worth having — "Read by AI" against "Skimmed" against "Found only" is
information I use. But offering an empty rung as a filter, with no note beside it on
Browse, means the one control aimed straight at a provenance-minded reader always returns
nothing. The explanation exists and is good — how-we-check.html opens with "Today the
count read in full is zero" — but it is one click away from the place I clicked.

**Do the date lines make the site look maintained?**
Maintained, and unusually careful. "Checked 5 Sep 2026" on card after card, one day before
I looked. "Published 12 Jun 2025 · over a year ago, may not match Claude today" is exactly
the flag I want. "No publish date given" on three quarters of cards reads as rigour, not
neglect — until the card also prints "Library Trends 73(3):355-380", at which point it
reads as a rule applied without looking.

**Does naming one person and Claude as "we" raise or lower my trust?**
It raises it, sharply. This is the paragraph that decided me:

> "One person makes this site - a researcher at the Technical University of Denmark,
> working on it outside their job. ... The reading is done by Claude, at the level each
> card's label claims and no further ... A person sets the rules, decides what the labels
> are allowed to say, and reads the arguments - and has not yet read a single resource end
> to end, which is why the strongest label has the count you can see above it."

That is a methods and conflict-of-interest statement. It declares the instrument, the
operator, and the limit. I would accept that in a paper.

One thing stops it short of full marks: **it is unsigned.** "a researcher at the Technical
University of Denmark" is a description, not a name. I can only recover the name by
reading the GitHub URL behind "Tell us"
(`github.com/Mojtaba-Alehosseini/learn-claude/issues/new?...`). An accountability
statement that does not name the accountable person is doing half the job.

**The picks block.** All four of my cells shipped three picks under a heading saying
three. I never saw a two-pick cell or an empty one, so I cannot judge that. The pick
*reasons* are the best writing on the site.

**The five collection cards.** I did not trip over them in any of my four pools. One
reached me through search ("Using Claude Cowork for legal", #5 for a citation question).
I looked at "Use cases for Legal": "For: Someone who owns a legal or compliance function
... Skip if: You have no legal function. **This is a menu, not a lesson**". Clear. No
complaint.

**The social preview title.** Broken. See finding 3.

**The home attract loop.** Runs, and never demonstrates the sentence. See section 1.

**The sort control.** Broken. See finding 2.

**Paths above beginner level.** Do not exist. See section 4.

---

## 9. Content quality — the three worst entries I was shown, quoted

The home page promises "Every entry has a `Skip if:` line. A link with no judgment is just
a list." These three have a `Skip if:` line with no skip in it.

**1. Using the ClinicalTrials.gov Connector in Claude** — Anthropic Academy
> Skip if: Free and fully open, no account needed - skip only if trial registry data
> genuinely isn't what you're researching.

"Free and fully open, no account needed" is a feature list. The word "genuinely" is doing
sales work. This tells me to skip only if I do not want the thing, which is true of
everything and useful about nothing.

**2. Using the Open Targets Connector in Claude** — Anthropic Academy
> Skip if: Fully open (CC0 data, Apache 2.0 connector code, no account needed) - skip only
> if target-disease association scoring for drug discovery isn't your work.

Same shape, same publisher, same failure. Licence terms in the skip slot.

**3. Use Claude Cowork safely** — Claude Help Center · Anthropic Help Center
> Skip if: Nothing — worth reading before your first real Cowork task regardless of
> experience level.

This one says out loud that the field has been abandoned. "Nothing" is not a skip
condition; it is an endorsement wearing the label of a warning. This card was in my
`basic` pool, and its own footer says "Step 4 of 5 in **Product work without waiting for
engineering**" — a product manager's path, in a researcher's shelf.

The pattern across all three: when the publisher is Anthropic and the page is a connector
or a safety note, the skip line stops being a judgment and becomes a summary of the
product. Compare it with what the site does when it is trying — "Academic Research with
Claude (live seminar)": *"It costs $995 and that is not the whole price: it also expects a
Claude Pro or Team subscription ... Its own page cannot decide whether you need Python or
R - one section says no programming experience is needed and another says a working
knowledge of a statistical language - so assume the stricter one."* That is a review. The
three above are not.

---

## 10. Everything that is broken, ranked (evidence for each)

Ranked by what it costs a reader, not by how hard it is to fix.

### 1. Search cannot find the site's own answer to the one thing researchers are afraid of

- **URL:** `browse.html` search box, and `browse.html?q=...`
- **What I did:** typed the fabricated-citation problem three ways.
- **What I saw:**
  - "how do I stop Claude from making up references in my literature review" → 12 results;
    "Reduce hallucinations" at **#4**.
  - "Claude gave me a citation that does not exist, how do I avoid that" → 11 results;
    "Reduce hallucinations" **absent from all 11**. Results 3, 4 and 5 were "Remote MCP
    Servers directory", "Hooks in Claude Code — Full Theory + Practical Use | CampusX",
    "Using Claude Cowork for legal: answer fast questions on past decisions".
  - "how do I keep Claude from inventing references" (submitted from the home page) → 58
    results; **"Reduce hallucinations" absent from all 58**; "Design Systems in 2026: Turn
    Your System into a Claude Skill" at #4.
- **Expected:** the card the site labels "Start with this" for this exact problem, in the
  top three, for any of the three wordings.
- **Mechanism, so this is not a guess:** how-we-check.html says search "reads the title,
  the hidden questions and keywords, what a resource teaches, who it is for and who should
  skip it". Every one of those fields on that card is on the page and none of them
  contains the words citation, reference, paper or manuscript. Title "Reduce
  hallucinations"; who it's for "Any analyst worried about confidently-wrong output";
  skip "You want data-specific step-by-step recipes"; teaches "...direct source
  quotations... prevent false claims". The path knows what the page is for; the card does
  not, and search only reads the card.
- **Who it harms:** the reader with the most to lose. The person typing that sentence is
  minutes away from a fabricated reference in a manuscript.

### 2. "Newest first" puts the oldest first and the newest last

- **URL:** `browse.html?role=researcher&level=never-used`, Sort → "Newest first"
- **What I did:** captured the order of the 16 cards under each of the three sort options.
- **What I saw**, under "Newest first":
  - #1 "Lesson 1: Introduction to AI Fluency..." — *"Published 12 Jun 2025 · over a year
    ago, may not match Claude today"*
  - #2 "Lesson 2B: The 4D Framework..." — *"Published 12 Jun 2025 · over a year ago, may
    not match Claude today"*
  - #16 (last) "AI: Artificial Intelligence Resources: Claude" — *"Updated 1 Sep 2026"*
  - #12 "How up-to-date is Claude's training data?" — *"Updated 1 Sep 2026"*
- **Expected:** the two items the site itself flags as over a year old are not the two it
  offers first when I ask for the newest.
- **Who it harms:** exactly the reader who understands the site's own warning about
  staleness and reaches for the control that should honour it. Both flagged cards are
  video lessons; a researcher who watches them first is watching the oldest material in
  the pool because the site put it first.
- **Not a blanket sort bug:** "Shortest first" is correct — it puts the thirteen 15-minute
  cards ahead of PubMed (1 hour), AI Fluency (half a day) and the Courses hub (several
  days).

### 3. Every resource page shares as "Resource — Learn Claude"

- **URL:** any `resource.html?id=...`
- **What I did:** read the metadata on
  `resource.html?id=r-69ee3c03e3` and `?id=r-4ccc667a90`.
- **What I saw:** `<title>` is correct and per-resource — "Claude AI and Literature
  Reviews: An Experiment in Utility and Ethical Use — Learn Claude". But
  `og:title` is the constant string **"Resource — Learn Claude"** and `og:description` is
  the constant **"What this resource teaches, who it is for, who should skip it, and how
  thoroughly we checked it."** No `og:url`, no `og:image`, no `rel=canonical`. Browse has
  the same split: `<title>` "Browse 19 Claude resources — Learn Claude", `og:title`
  "Browse — Learn Claude".
- **Expected:** the resource title in the preview. The site went to the trouble of making
  the document title dynamic and stopped one line short.
- **Who it harms:** anyone recommending one specific thing. The site puts a **"Copy link"**
  button on every resource page — it built the affordance for the action its metadata
  breaks. If I paste the ICMJE card into a lab channel to settle an argument, my
  colleagues see a grey box that says "Resource". Every resource on the site previews
  identically, so a thread with three of them looks like the same link three times.

### 4. The top rung of the ladder returns zero everywhere, with no note where you click

- **URL:** `browse.html?checked=reviewed`
- **What I saw:** "Browse 0 Claude resources — Learn Claude", "0 resources", "We have
  nothing for this combination yet."
- **Evidence:** STATUS.md — `reviewed` / "Read in full" / **0** / 0%.
- **Expected:** the filter that a provenance-minded reader reaches for first either says
  "0 by design, here is why" beside itself, or is not offered as a live control.
- **Who it harms:** me, and only me — the reader who filters by how well something was
  checked before reading anything. Everyone else never touches it. The explanation on
  how-we-check.html is excellent and is not where the click happens.

### 5. `pay once` with no price, on the paid step of my own path

- **URL:** `resource.html?id=r-69ee3c03e3`; also the card in
  `browse.html?role=researcher&level=confident`
- **What I saw:** chips read `article`, `1 hour`, `pay once`. The skip line says "It costs
  money and it is a study, not a method". No figure anywhere on the card or the page. The
  path summary says "5 steps · about 2 hours · **some paid steps**" and never names one.
- **Expected:** a number, because the site does this elsewhere — "Academic Research with
  Claude (live seminar)" shows `pay once` **and** `from $995` side by side.
- **Who it harms:** anyone deciding whether to follow the path. Step 3 of 5 is a gate with
  an unknown toll. On a Project MUSE article that could be five dollars or fifty.
- **Same fault, worse case:** the `listed` card "Head of Claude Code: What happens after
  coding is solved (Boris Cherny)" carries a `subscription` chip on content the site says
  "Nobody has looked at" — an unpriced recurring charge for an unread page.

### 6. "a researcher" is one role for two jobs, and the catalogue's centre is a wet lab

- **URL:** `browse.html?role=researcher&level=confident` (32) and `...&level=never-used`
  (19)
- **What I saw:** at `confident`, fifteen of the twenty-nine non-pick cards are Anthropic
  Academy pages for genomics, single-cell RNA QC, preclinical studies, Benchling, Owkin,
  BioRender, Allotrope and Synapse.org. At `never-used`, six of nineteen are biomedical
  database connectors.
- **Evidence for the publisher concentration:** STATUS.md, `researcher|never-used` =
  `17 / 5p / 2x` — two non-Anthropic items among seventeen eligible.
- **Expected:** a filter, a sub-role, or a ranking that does not hand a social scientist
  tumour pathology slides.
- **Who it harms:** every researcher outside the life sciences, which is most of us.

### 7. "Skip if" is a sales line on the connector cards

Three quoted verbatim in section 9. The site's central promise is that the skip line
carries judgment. On the Anthropic Academy connector family it carries licence terms and
"skip only if you do not want this". Harm: the promise is what made me trust the other
cards, and a reader who checks two of these learns to skim the field.

### 8. My path's step 3 is badged "Read by AI" on a page STATUS.md says a machine cannot read

- **What the site shows:** `resource.html?id=r-69ee3c03e3` — badge "Read by AI", and in
  plain text "Read by AI. **AI read all of it.** No person has checked the notes yet."
  Out-link `https://muse.jhu.edu/article/961199`.
- **What STATUS.md records:** that same URL is listed under **"Pages no machine can read
  (9)"**, whose header states "Their host refuses automated requests or serves a
  challenge, so the date we held could not be confirmed and was dropped."
- **Expected:** one of the two statements withdrawn. A page whose host refuses automated
  requests, behind a `pay once` wall, cannot also have been read in full by an automated
  reader.
- **Who it harms:** the reader who came here *because* the site labels its provenance. The
  label is the product. A label that contradicts the project's own generated record is
  worse than no label.

### 9. "We do not list something whose page we cannot open" against 21 items nobody has opened

- **What the site says**, how-we-check.html, under "What we will not do": "We do not list
  something whose page we cannot open."
- **What STATUS.md records:** "Hosts that block the weekly check (**21 items**)" across 12
  hosts — datacamp.com, medium.com, udemy.com, forbes.com, uxdesign.cc,
  designsystemscollective.com, students.unimelb.edu.au, monash.edu, education.gov.au,
  ethicscentral.org, spj.org, niemanlab.org — with "last confirmed by a person" reading
  **never** for every one of them.
- **Expected:** the sentence on the public page matches the record. As written it claims
  every listed page has been opened; 21 have been opened by nobody, machine or person.
- **Who it harms:** anyone who read that sentence and stopped checking, which is what the
  sentence is for.

### 10. Bibliographic detail printed beside "No publish date given"

- **URL:** `resource.html?id=r-69ee3c03e3`
- **What I saw:** byline "Max Sparkman & Alan Witt, **Library Trends 73(3):355-380**" and
  footer "Checked 5 Sep 2026 · **No publish date given**".
- **Expected:** where a card already carries volume, issue and pages, the date rule should
  notice it has most of a citation in hand.
- **Related:** the ICMJE card, `resource.html?id=r-146910f648`, also says "No publish date
  given" for a policy document whose whole meaning is its revision.
- **Who it harms:** anyone who has to cite the thing, which for these two cards is the
  entire audience.

### 11. The tier badge on Browse cannot be reached by a sighted keyboard user

- **What I saw:** `<span class="badge badge-previewed" title="We read the outline or a
  free sample. We have not seen the whole thing.">Skimmed</span>` — a `<span>`, no
  `tabindex`. The definition is delivered to screen readers through
  `aria-describedby="tierdesc-previewed"` on the card's title link.
- **Expected:** 00-facts states the definition is "meant to be reachable from a card
  without a mouse". It is reachable without eyes, and reachable with a mouse. It is not
  reachable with a keyboard and eyes.

### 12. The home page's two headline buttons have no accessible name

- **URL:** `index.html`
- **What I saw:** the accessibility tree renders the headline as
  `generic "I'm and I've ."` containing `button [ref_11]` and `button [ref_13]` — two
  buttons, neither with a name. The visible text `[role]` and `[level]` sits in unlabelled
  child spans.
- **Expected:** a screen reader user hears the site's central question. They hear
  "I'm and I've" and two unnamed buttons.

### 13. Enter does not submit the home page search

- **URL:** `index.html`
- **What I did:** focused the box, typed "how do I keep Claude from inventing references",
  confirmed `document.getElementById('q').value` held the sentence and
  `document.activeElement.id` was `q`, then pressed Return. Then pressed Return again.
- **What I saw:** `location.href` stayed at `.../index.html` both times. Clicking the
  "Show me" button with the same text in the box navigated to
  `browse.html?q=how+do+I+keep+Claude+from+inventing+references`.
- **Expected:** the form is `<form class="search-row" id="go">` with one text input and one
  `type="submit"` button. Typing a sentence and pressing Enter is how people search.
- **Who it harms:** anyone who uses the "Or describe what you want to do…" box the way its
  placeholder invites — as a sentence, ended with a keystroke.

### 14. The thin-cell offer is a sentence, not a click

- **URL:** `browse.html?role=researcher&level=builder`
- **What I saw:** "6 resources. **Remove a filter to see more.**" inside
  `<p class="result-count">`. No link, no button.
- **Expected:** what the 0-result state does — "Loosen the level, or see everything for
  this role, or browse everything", with live links. The site has the pattern and applies
  it only at zero.

---

## 11. The one thing that would make me leave and not come back

Finding 1. I typed the sentence that describes my worst professional fear, in the plainest
English I have, and the site's own designated answer to that fear did not come back — not
in the top three, not in the top eleven, and in one wording not in any of the 58 results
it returned.

That is not a ranking complaint. This site's entire claim on my attention is that somebody
judged this material so I would not have to. The judgment exists here — "Start with the
failure, not the feature. Fabricated citations are the one mistake that ends careers" is a
better sentence than I would have written. It is written on the path page and it is not
written on the card, and the search only reads the card. So the site knows the answer and
cannot hand it to me when I ask.

If I asked twice and got two unrelated sets of results, I would conclude the judgment is
not really there and the confident tone is decoration. I would close the tab. I would not
open it again.

---

## 12. What is genuinely good (honest, brief)

- **The journal-policy set.** ICMJE, Nature Portfolio, IEEE and Elsevier in one screen at
  `?role=researcher&level=basic`. Nobody else has collected these next to a tool guide.
- **The path title.** "Using Claude for research without embarrassing yourself." It knows
  what the job is.
- **The path's step reasons.** "Start with the failure, not the feature." "Until Claude
  can see your actual sources, everything above is a demo." Five steps, five arguments.
- **Skip lines when they are trying.** The $995 seminar card, which catches its own source
  contradicting itself on whether Python is required, and tells you to assume the stricter
  reading. The Zotero card, which refuses to claim the fabrication problem is solved.
- **"Who we is."** A named institution, a stated method, an admitted limit, and no claim of
  affiliation. I would accept that paragraph in a paper.
- **The `listed` tier.** Three cards that say "We have not opened this one yet" instead of
  padding. Most directories would have written a summary from the title.
- **Dates on every card, and a stale flag.** "over a year ago, may not match Claude today"
  is the right sentence in the right place.
- **Mobile.** The filter sheet with a pinned "Show 32 resources" footer is better built
  than the desktop rail it replaces.
- **No account, no tracking, no email capture, no "certification" upsell** — and a
  paragraph explaining that last one: "Anthropic runs a real certification, but it is open
  to members of the Claude Partner Network, not to the public."

---

## 13. Would I come back, and what one thing would make me?

Yes, but for one thing, and not the thing the site thinks it is.

I would come back for the journal-policy shelf and the research path. That is a real
contribution — four publishers' AI rules, a Zotero route, and a peer-reviewed study of
Claude actually failing at a literature review, with a person's argument attached to each.
I have not seen that anywhere else and I would bookmark the path URL directly, because
that is where the value is concentrated.

I would not come back to *search* it. I asked it my worst fear in three different ways and
got three different answers, and the one it had prepared for exactly that question never
appeared. Once you learn that, you stop trusting the box and start scrolling the shelf,
and at that point it is a bookmark, not a tool.

The one thing that would bring me back properly: **make the search find what the site
already knows.** The path already contains the sentence "Fabricated citations are the one
mistake that ends careers, and this is the clearest account of when they happen and how to
cut them." That sentence is not on the card, so the card is invisible to anyone who types
the problem instead of the product name. Put the path's reasoning into the thing that
search reads, then ask it the question two ways and check that the same card comes back
both times.

And while you are there: sign the "How we check" page. It says a researcher at DTU wrote
it. I had to read a GitHub URL to find out who. A methods statement without an author is
the one part of this site that does not practise what the rest of it preaches.

---

## Checklist
- [x] I opened the live site
- [x] I tried all four levels
- [x] I quoted at least 5 real titles or lines from the site
- [x] Every number I used is in 00-facts.md, STATUS.md, or quoted from the site
- [x] I looked at a phone width
- [x] I read no file under scripts/ or data/
- [x] I found at least one thing nobody has mentioned before
