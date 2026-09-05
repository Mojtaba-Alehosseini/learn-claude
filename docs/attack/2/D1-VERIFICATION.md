# D1 — all 36 `listed` items opened, one by one

Ruling: *"An unread item may not carry a verdict. Verify, re-tier, or strip."*

Every one of the 36 was opened on **2026-09-05**. 33 by fetching the page, 3 that machines
cannot read — a YouTube playlist, a `403` university host and a government host that blocks
automated requests — driven in a real browser instead. One is a PDF; its text was extracted
locally after the fetch returned binary.

**Nothing here was decided from memory.** Each row below is a comparison between what the
card claims and what the page says, with the page quoted.

---

## What the verification found, before the outcomes

**The prose was not invented. The tier was wrong.** That is the headline, and it is the
opposite of the cheaper assumption. Card after card matched the page exactly, including
claims no one could make without reading:

- *Hooks reference* — "every lifecycle event, the JSON input and output schema, exit codes,
  and the async, HTTP, prompt and MCP-tool hook variants" and **"it is enormous"**. All five
  confirmed; the page carries a `<Tip>` pointing beginners at a separate guide, exactly as the
  card says, and the fetch truncated mid-table.
- *Vanderbilt / Turnitin* — all four specifics: the false-positive arithmetic
  (*"Vanderbilt submitted 75,000 papers to Turnitin in 2022... around 750 student papers could
  have been incorrectly labeled"*), *"Turnitin gives no detailed information as to how it
  determines if a piece of writing is AI-generated"*, the non-native-English-speaker warning,
  and the date *"Aug 16, 2023"*.
- *Education Report (educators)* — "about 74,000", "22 Northeastern faculty", "around 57%",
  then research, then assessment. **Every number exact.**
- *UNESCO* — "Fifteen teacher competencies across five dimensions and three progression levels
  - acquire, deepen, create." The page: *"15 competencies across five dimensions"*, *"three
  progression levels: Acquire, Deepen, Create"*. Exact — and this card's `notes` had warned
  *"the framework details here come from search results and secondary summaries only - open it
  yourself before citing."* Someone did, today, and the summaries were right.
- *AIAS* — five levels named correctly, *"task redesign"* as the stated main job, and the
  card's claim that it *"deliberately refuses to name a 'best' level"* matched by the page's
  *"Each represents a different kind of task rather than a hierarchy."*
- *Sales Analysis (Coursera)* — including the **negative** claim. The card says nothing on the
  page tells you to check Claude's arithmetic. Checked: it does not.

**And the `notes` field had been honest all along.** Repeatedly it said what the card did not:
*"Repo contents not reviewed."* *"Individual videos not watched."* *"I read a detailed
third-party description of the repo, not the skill files."* *"Metadata and summaries only."*
The provenance was recorded correctly in the one field the site never renders, while the card
printed the confident version. That is the whole fault in one sentence.

---

## Outcomes

| Outcome | Count |
|---|---|
| **Verified — promoted to `previewed` unchanged** | 28 |
| **Verified — promoted, with a clause corrected from the page** | 5 |
| **Stripped — stays `listed`, prose removed** | 3 |

**33 of 36 survived verification.**

---

## The three that were stripped

### 11. Head of Claude Code (Boris Cherny) — `r-9f57e8bf80`
The card summarises the episode: *"not hand-editing code since November 2025, how the tool
went from an internal hack to a large share of public GitHub commits."*

The page: **paywalled.** *"This post is for paid subscribers"*; only the introduction and
episode description are readable. The card's own `notes` say: *"Not listened to, so claims
made in the episode are not checked here."*

So the card states what was said in an episode nobody heard, on a page nobody could open past
the gate. The one claim I could verify — the skip_if, *"There is almost nothing here you can
copy into your terminal"* — is correct, and it does not save the rest.

### 14. Ralph — `r-d24581da69`
Two claims fail, and the safety one matters most.

- Card: *"nothing here reviews the code it writes."* README: *"Ralph will... Run quality checks
  (typecheck, tests)... Commit if checks pass"*, and *"Ralph only works if there are feedback
  loops."* **Contradicted.**
- Card: *"asks lettered multiple-choice clarifying questions."* The README describes clarifying
  questions but not that format. **Unsupported.**
- The card's `notes` cite *"about 9,755 stars per Snyk's February 2026 count."* The repo shows
  **21.7k**. A third-party count, six months stale, off by a factor of two.

`notes` again admitted it: *"I read a detailed third-party description of the repo, not the
skill files."*

### 27. "Anthropic launched Claude for Teachers. We blocked it for our district." — `r-76de44b7a7`
The worst of the three, and the one an attacker flagged as citable.

The card states a specific legal argument as the article's: *"FERPA lets a vendor act as a
'school official' only where the district designates it and keeps direct control, and an
individual teacher cannot make that designation on the district's behalf."*

**The article does not make that argument.** It does not invoke the school-official concept at
all. Its actual objection is procedural — that Anthropic marketed to individual teachers before
shipping the district offering: *"teachers could inadvertently make unauthorized disclosures of
protected student information while believing they were using the product exactly as
intended."*

`notes`: *"I have not read it end to end - metadata and summaries only."*

The teacher agent in Attack 2 quoted the FERPA sentence and said a teacher might carry it to a
head of department. It would have been a legal claim attributed to a source that never made it.

---

## The five corrected, with the page quoted

Each of these had a supported description and one clause the page contradicts or has outgrown.
The clause is replaced by what the page says; nothing is added.

| # | id | Clause removed | Why |
|---|---|---|---|
| 2 | `r-9878646d22` | "it exists because the older @modelcontextprotocol/server-postgres was archived as vulnerable" | The README says the reference server is archived. It does not say vulnerable, and does not give that as the reason this exists. Also: the README's own protection is SQL parsing (*"we parse the SQL before execution using the pglast library"*), not a read-only role. |
| 4 | `r-33e0c1904b` | "it is added as a custom connector rather than a one-click install" | Outgrown. The README now offers a managed service: *"Point any MCP-compatible client at `https://mcp.tableau.com` and complete the OAuth sign-in flow."* Self-hosting still needs PAT/OAuth env vars, which the card is right about. |
| 5 | `r-68b6652318` | "budget half a day, most of it setup" | Contradicted. The README now advertises *"zero-config setup with uvx"* with automated installers that configure MCP for desktop apps. Everything else on this card — including the exact "Reviewer Zero" claim, *"systematically verifying that every p-value, coefficient, and confidence interval in your paper matches the code that produced it"* — is right. |
| 19 | `r-960acd1524` | "aimed slightly higher up the ladder than undergraduate coursework guides" | Contradicted. The page explicitly covers student coursework: *"Princeton University students must confirm AI is permitted by an instructor and disclose the use of AI in any academic work."* It also gives no templates of its own — it links two external generators. |
| 35 | `r-6da5a506f4` | "A 74-page toolkit" | Measured: **79 pages**. And the `notes` claimed *"scanned PDF; no extractable text, so no readable date"* — false. The text extracts cleanly and the cover reads **"October 2024"**, with PDF metadata `/Author U.S. Department of Education`. |

---

## Things the verification fixed that D1 did not ask for

Recorded, not acted on beyond the notes, because they are date and provenance facts rather
than tier decisions.

- **`r-6da5a506f4` has a publication date after all.** "October 2024", printed on the cover
  and in the PDF metadata. The catalogue carries `UNVERIFIED` because a fetch returned binary.
- **`r-967880ec2e` is year-scoped after all.** The card's `notes` warn *"It is not year-scoped,
  so it may mix the 2025 and 2026 events."* The playlist description says: *"Code with
  Claude—our first developer conference—took place on May 22, 2025 in San Francisco."* One
  event, 20 videos.
- **`r-521c6b7dca` has a transcript.** `notes` said *"transcript availability not verified."*
  It is there, under the player, in full.
- **`r-6a15e8b9c3` (EU) has a datable current version.** `notes` said the date could not be
  confirmed. The page says the original is 2022 and an update was prepared for 2026 by the
  Working Group on the Ethical Use of AI and Data in Education.

---

## The full table

`V` = verified as written. `C` = verified, one clause corrected. `S` = stripped.

| # | id | Title | Outcome | The check that decided it |
|---|---|---|---|---|
| 1 | `r-bcd03ac245` | Sales Analysis with Claude | V | 1.5 hours ✓, Claude Pro required ✓, no verification advice ✓, no coding ✓ |
| 2 | `r-9878646d22` | Postgres MCP Pro | C | read/write + EXPLAIN + index tuning + health ✓; "archived as vulnerable" ✗ |
| 3 | `r-298096d0e3` | MotherDuck / DuckDB MCP | V | local + cloud ✓, read-only by default ✓, managed remote endpoint ✓ |
| 4 | `r-33e0c1904b` | Tableau MCP (official) | C | official ✓, Cloud/Server + PAT/OAuth ✓, mcp.tableau.com ✓; "not one-click" outgrown |
| 5 | `r-68b6652318` | ClaudeR | C | MCP ✓, R protocol ✓, Reviewer Zero ✓ quoted; "half a day of setup" ✗ |
| 6 | `r-4f437b4495` | Hooks reference | V | every claim including "it is enormous" ✓ |
| 7 | `r-26b52d229f` | claude-quickstarts | V | runnable API starters ✓, API not Claude Code ✓, 17.6k stars |
| 8 | `r-e683190d69` | claude-agent-sdk-python | V | source + changelog + issues ✓, bundles the CLI ✓ (quoted) |
| 9 | `r-7773ad4116` | claude-code-action | V | official CI action ✓, @claude on issues and PRs ✓, review ✓ |
| 10 | `r-967880ec2e` | Code w/ Claude playlist | V | 20 videos; keynote ✓, Claude Code + MCP breakouts ✓, Canva/Databricks/Shopify/Sourcegraph ✓ |
| 11 | `r-9f57e8bf80` | Head of Claude Code | **S** | paywalled; summary describes an episode never heard |
| 12 | `r-cd019b4ce7` | Building a Claude Project (Northeastern) | V | recording ✓, handout + faculty FAQ ✓, labelled 2025 ✓ |
| 13 | `r-e7cf466f6e` | compound-engineering-plugin | V | all five skills ✓, install command exact ✓, agent-agnostic ✓ |
| 14 | `r-d24581da69` | Ralph | **S** | "nothing reviews the code it writes" contradicted by the README |
| 15 | `r-3bac54ee56` | Education Report (students) | V | one million conversations ✓, CS 36.8% vs 5.4% ✓, research not how-to ✓ |
| 16 | `r-16c564ede1` | Claude for higher education | V | sales page ✓, logos + contact-sales ✓, no pricing ✓ |
| 17 | `r-e7a2c56f78` | Using AI for Writing Feedback | V | student guide, feedback before submission ✓, Northeastern-specific ✓ |
| 18 | `r-8b7a1fe21d` | Claude Enterprise at Syracuse | V | students/faculty/staff ✓, no training on data ✓, prompting primer ✓ |
| 19 | `r-960acd1524` | Disclosing the Use of AI (Princeton) | C | disclosure guide ✓; "higher up the ladder than coursework" ✗ |
| 20 | `r-19d3c9dd56` | Using AI in university (UNSW) | V | "Levels of AI Assistance framework" ✓ named on the page |
| 21 | `r-504ad565db` | AI for Students (Monash) | V | FIT1059 "AI for Everyone" ✓, Foundations module ✓ (403 to machines; read in a browser) |
| 22 | `r-25cc7a8b0d` | 2026 Student Guide to AI | V | third annual ✓, subtitle exact ✓, human capabilities not tool features ✓ |
| 23 | `r-0723e82a39` | Generative AI and Academic Integrity (CSUN) | V | "Last Updated: Aug 27, 2026" ✓, hub of links ✓ — "adds little" is fair |
| 24 | `r-44f5f08b9e` | PAIRR prompts | V | copyable prompts ✓, CC BY-NC ✓, demonstration bots ✓, not paywalled ✓ |
| 25 | `r-521c6b7dca` | Peer and AI Review (podcast) | V | both researchers ✓, PAIRR process ✓, Oct 14 2025 ✓, transcript present |
| 26 | `r-ea39152439` | Education Report (educators) | V | 74,000 ✓, 22 faculty ✓, 57% ✓ — every figure exact |
| 27 | `r-76de44b7a7` | We blocked it for our district | **S** | the FERPA "school official" argument is not in the article |
| 28 | `r-1b3a17375f` | AI in assignment design (Cornell) | V | syllabus policy language ✓, error analysis ✓ quoted, metacognition ✓ |
| 29 | `r-3ef5584cd6` | The AI Assessment Scale | V | five levels named exactly ✓, task redesign ✓, refuses a "best" level ✓ |
| 30 | `r-1b663b7646` | Vanderbilt / Turnitin | V | 75,000 papers, ~750 flagged, no explanation given, non-native writers — all ✓ |
| 31 | `r-6b4b766e56` | Australian Framework | V | ministers ✓, 2024 review endorsed June 2025 ✓, audience list ✓ (blocks machines; read in a browser) |
| 32 | `r-b19d02a867` | UNESCO framework | V | 15 competencies, five dimensions, Acquire/Deepen/Create — exact |
| 33 | `r-6a15e8b9c3` | EU ethical guidelines | V | AI Act + GDPR ✓, guiding questions and scenarios ✓, EU-specific ✓ |
| 34 | `r-11991cab3c` | Day of AI (MIT RAISE) | V | free ✓, all K-12 grade bands ✓, workshops ✓, registration needed ✓ |
| 35 | `r-6da5a506f4` | Empowering Education Leaders | C | US Dept of Education ✓, October 2024 ✓; "74-page" is 79 |
| 36 | `r-6a6a4daf55` | AP Sets New AI Standards | V | headlines/summaries allowed ✓, human review required ✓, no AI photography ✓ |

---

## One interpretation I made, and how to reverse it

The ruling is binary: supported → `previewed`, unsupported → strip. Five cards had a supported
description and **one** clause the page contradicts or has outgrown — a setup time that got
easier, a page count off by five, a connector that became one-click. Stripping those would have
deleted accurate work over a stale detail; promoting them unchanged would have shipped a
sentence the page denies.

So I corrected the clause from the page and promoted, and every one is logged above with the
page quoted.

**If you would rather they were stripped, that is five ids and a one-line change.** They are
rows 2, 4, 5, 19 and 35.
