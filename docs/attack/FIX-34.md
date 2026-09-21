# Fix prompt — four rulings, a class of silent script, and what a thing needs

Paste everything below the line into Claude Code, in the project folder.

---

The links unfurl. The new rules found a second superseded step and a script that
printed its own failure and exited 0. Four rulings, one generalisation, then the last
Attack 3 finding still on the site.

# Rulings

1. **The path `why` is selectable.** It is the site's argument for the step; a person
   should be able to quote it. Lift the `why` block above the stretched link — the text
   selects, the rest of the step stays one click. Cards stay as D12 ruled.
2. **Description cap: 160.** The `For:` line whole when it fits; cut at a word
   boundary with an ellipsis when it does not; `Skip if:` appended only when both fit.
   One debugger's heuristic is not a spec. Replace the typed 200 and the comment with
   this rule and the measured median. The real check is a paste into Teams or Slack,
   and that is on my list.
3. **D5 wording: "price on the page."** Nothing more. The reason we do not copy the
   number lives on the method page, where the other rules are. "Varies by country" was
   true for seven rows and a guess for fifteen.
4. **Constraint 5, the middle version.** A pick's `who_for` must name the cell's role
   or name nobody in particular. Naming other roles *as well* is fine — "Researchers
   and graduate students" passes in both cells. Naming only somebody else fails — "Any
   analyst" in the student cell. Apply it to the 20 notes; the validator names what it
   rejects; re-pick what it names.

# The generalisation — a script that cannot say no

FIX-31 audited every pipe. `build-paths.py` was not piped; it printed "NOT PUBLISHED"
and returned 0, so a rejected path vanished from the site with the build green. That
is a class: any script with a reject path that does not exit non-zero.

- List every script under `scripts/` that can reject, skip, or drop something. For
  each: does the reject path exit non-zero, and does `test-gates.py` plant it? Table in
  the round record.
- Every reject path exits non-zero. Every one gets a planted fault in `test-gates.py`.
  Eleven faults today; the table says how many it should be.
- Add to the docstring of `test-gates.py`, so the next auditor reads it first: *a gate
  fails in two ways — its status is swallowed, or it never had one.*

# D4 — what a thing needs is not what it costs

The cost chip is the resource's own price. Sixteen analyst cards say `free` while
needing a paid data subscription, and one says `free` four lines above "Before this —
Paid Claude plan". The chip is not lying; it is answering a different question than
the reader asked.

- **New field `needs[]`**, from a short vocabulary: `paid-claude-plan`, `mac`,
  `windows`, `connector:<name>`, `data-subscription:<name>`, `github-account`,
  `api-key`. Add to the vocabulary only with a reason in the copy deck.
- **Record it from the page**, not the card. Start with every row whose card already
  says "Before this", every row tagged `data-analyst`, and every `confident` and
  `builder` row that mentions Cowork, a connector or a plan. Checkpoint at 40 rows —
  show me the field beside the card's own words, and stop if the page and the card
  disagree more than a few times.
- **Render it as its own chip**, beside cost, only when it holds something paid or
  platform-bound — a Mac, a paid plan, a subscription. "Free · needs a paid Claude
  plan" is the honest card. Define both chips on `how-we-check.html`.
- **The Time filter is unchanged**; `needs` is not a filter this round. If it earns
  one, Attack 4 will say so.

# D3 — the ladder, stated per role

No mechanism. After constraint 5 re-runs, measure each role's four cells: count, and
how many picks are role-specific. Part 11 gets one sentence per role that names the
rung the catalogue runs out at, pointing at STATUS.md for the numbers. The developer's
exception is stated as an exception.

# Small

- The `skip_if` lines: measure how many complete the sentence "Skip if you…" and how
  many do not. One number in the record, no rewrite — the developer's closing answer
  is a style question, and the number decides whether it is worth a round.

# Not yours

STATUS.md "Needs a person" and part 10. The human test, and the paste into Teams.

# Commits

The four rulings, the script audit and its planted faults, the `needs` vocabulary,
the data pass, the chip, the ladder sentences, the skip measurement — one job each.
`FIX-34.md` with the round. Push. Finish with what surprised you, what you got wrong,
whether it was in CLAUDE.md — and how many scripts could not say no.


---

# The round, as run

Started 2026-09-07, finished 2026-09-21. Every gate green, every gate bitten.

## The four rulings

| ruling | what changed |
|---|---|
| **1 — the path `why` is selectable** | The step's argument sits above the stretched link, the same way the CTA button already did. The text selects, a click on the words does nothing, and every other part of the step still opens the resource in one click. Cards unchanged. |
| **2 — the description cap is 160** | The `For:` line whole where it fits, cut on a word boundary with an ellipsis where it does not, and the `Skip if:` sentence appended only where both fit. The checker reads the generator's cap rather than keeping a copy, and refuses any built page past it. |
| **3 — "price on the page"** | The chip says where the number is and nothing more. The method page names seats as well as countries. The copy deck carries the string and why the old one was cut. |
| **4 — constraint 5, the middle version** | A pick's `For:` line must name this cell's role or name nobody in particular. Naming other roles as well is fine. Run against the catalogue it rejects nothing and prints no notes — the twenty cross-role picks it used to list every run are simply legal. |

### What the rulings measured

The description change is worth a number, because it cost something. Under the old
rule most served descriptions ran past what a preview shows; under the new one none
does. The price of that: far fewer resource pages now carry both halves of the
description, because the `Skip if:` sentence only goes in where the pair fits. The
figures are in the build output and in the table below.

| after the cap moved | |
|---|---|
| longest served description | 160 characters |
| descriptions past the cap | 0 |
| median | 115 characters |
| resource pages carrying both halves | 71 of 585 |
| resource pages whose `For:` line is cut | 39 |

Constraint 5's strict version was measured before it was rejected: it flagged twenty-one
picks, twenty of which were cross-role resources doing nothing wrong. The middle version
flags none today, because the one row it was written for was rewritten last round.

## The script audit — can it say no?

Every file under `scripts/`, read by hand on 21 September 2026. FIX-31 audited the other
half of this question: whether a gate's status survives the shell. This asks whether the
script had a status to begin with.

**The classes.** *rejects* — refuses its input and the build must stop. *drops* — leaves
something out of its output. *reports* — prints a finding and ships anyway, by design.
*none* — no reject path: a library, a transform, a one-off tool.

| script | run by | can reject / drop / report | exits non-zero on it | planted in test-gates |
|---|---|---|---|---|
| `validate-catalogue.py` | build, CI | rejects an invalid row | yes | yes (listed row with a verdict) |
| `test-validate-catalogue.py` | build, CI | rejects a rule that stopped biting | yes | — *(it is itself a bite test)* |
| `stable-ids.py` | build | rejects a hash collision | yes | — *(no input can produce one without a duplicate URL, which the validator rejects first)* |
| `add-source.py` | build | reports a guessed publisher over a hand-written one | n/a — it guesses, it does not drop | — |
| `build-paths.py` | build | rejects a path: too short, too thin, superseded | yes, since FIX-33 | yes (superseded step) |
| `build-search-index.py` | build, CI | rejects a missing API key (embeddings stage only) | yes | — *(build.sh runs `--keywords`, which has no reject path)* |
| `test-search.py` | build, CI | rejects a regressed query, a gap with no evidence | yes | yes (query forced to miss; gap with no evidence) |
| `test-search-runtimes.js` | build, CI | rejects a disagreement between Python and the browser | yes | — |
| `validate-synonyms.py` | build | rejects a synonym with no reason | yes | yes |
| `test-stem.py` | build | rejects a stem that moved | yes | — |
| `test-role-buckets.py` | build | rejects a bucket that stopped matching | yes | — |
| `check-questions.py` | build | rejects a question that is a suite query | yes | yes |
| `check-self-retrieval.py` | build | rejects a row its own questions cannot find | yes | — |
| `test-gap-claims.py` | build | rejects a content gap with no pages opened | yes | yes |
| `build-og-card.py` | build | **skips** regenerating where Pillow is absent | no, on purpose | yes, by consequence — `check-share-pages.py` fails if the committed card is gone |
| `build-share-pages.py` | build | rejects a shell whose head it cannot find | yes | yes (moved head anchor) |
| `build-sitemap.py` | build | drops nothing — it lists the generator's manifest | n/a | — |
| `check-share-pages.py` | build | rejects a page with no title, no image, a wrong canonical, a description past the cap | yes | yes (placeholder head; description past the cap) |
| `build-data-js.py` | build | **dropped a missing source and returned zero** | **yes, since this round** | **yes, new (a mirror source that vanished)** |
| `fetch-publisher-marks.py` | by hand | rejects a host it cannot reach | yes | — |
| `test-browse-query.js` | build, CI | rejects a benchmark sentence that stops answering | yes | — |
| `test-fresh-line.py` | build | rejects a surface that builds its own freshness line | yes | yes |
| `measure.py` | build, CI | reports exclusions and drift; writes STATUS.md | n/a — it measures, it does not judge | — |
| `test-measure.py` | build, CI | rejects a measurement that stopped adding up | yes | — |
| `build-attack-facts.py` | build | rejects a briefing with no markers to write into | yes | — |
| `validate-picks.py` | build, CI | rejects a dead, ineligible or misaddressed pick | yes | yes (dead pick) |
| `test-validate-picks.py` | build, CI | rejects a pick rule that stopped biting | yes | — *(it is itself a bite test)* |
| `test-copy-claims.py` | build, CI | rejects a copy claim the data does not support | yes | — |
| `check-typed-numbers.py` | build | rejects a typed count in a reason or a document | yes | yes |
| `audit-pick-contradictions.py` | build | **reports** picks worth re-reading | no, by design | — |
| `audit-time-chips.py` | build | **reports** cards whose prose and chip disagree | no, by design | — |
| `test-gates.py` | build, CI | rejects a planted fault the build did not catch | yes | — *(it is the harness)* |
| `check-links.py` | CI | reports dead and blocked links | n/a | — |
| `report-dead-links.py` | CI | rejects a link report it cannot read | yes | — |
| `validate-report.py` | CI | rejects a malformed report | yes | — |
| `pre-commit.py` | hook | rejects control characters, an invalid catalogue | yes | — |
| `commit-msg.py` | hook | rejects a typed count in a message | yes | — |
| `install-hooks.py` | by hand | rejects a repository it cannot find | yes | — |
| `pick-candidates.py` | library, by hand | rejects an unknown cell | yes | — |
| `stem.py` | library | none | n/a | — |
| `measure-use-cases.py` | by hand | reports | n/a | — |
| `audit-levels.py` | by hand | reports | n/a | — |
| `audit-role-tags.py` | by hand, library | reports; rejects nothing, adds nothing | n/a | — |
| `enrich-items.py` | by hand | rejects a missing API key | yes | — |
| `normalise-icon.py` | by hand | rejects a file it cannot read | yes | — |
| `make-fillable-icon.py` | by hand | rejects bad arguments | yes | — |
| `make-placeholder-format-icons.py` | by hand | none | n/a | — |
| `a11y-audit.js` | by hand | reports | n/a | — |

**The answer to the question.** Two scripts could not say no, and both were found by
asking rather than by a failure. `build-paths.py` was the one that started this, fixed in
FIX-33. `build-data-js.py` is the new one: it printed "missing — skipped" for any of the
five files the site loads at startup and returned zero, so a build that lost
`data/items.json` would have deployed an empty Browse page, green.

Three more are deliberate and stay as they are, each with its cover written down:
`build-og-card.py` skips where Pillow is absent and `check-share-pages.py` fails if the
committed card is not there; `audit-pick-contradictions.py` and `audit-time-chips.py`
report and ship, because turning either into a rejection is a ruling about the cards they
name, not a plumbing fix.

### The `needs` pass — the checkpoint

Rows opened on 21 September 2026, in the order the spec sets: the shortlist is the
cards that already name something, and within it the rows whose words point at a
chip the site would draw.

| # | resource | the page says | the card said | recorded |
|---|---|---|---|---|
| 1 | [Use Claude for Excel](https://claude.com/docs/office-agents/excel) | Claude for Excel is generally available to Pro, Max, Team, and Enterprise plans. | paid claude plan / the add-in needs Pro, Max, Team or Enterprise | `paid-claude-plan` |
| 2 | [Getting Started with Claude for Financial Serv](https://academy.claude.com/tutorials/getting-started-with-claude-for-financial-services) | Valid licenses to connect to your preferred data providers. Daloopa subscription for fundamentals and KPIs. S&P Global subscription for Capital IQ Financials. Contact our Sales tea | a purchased Claude for Financial Services engagement / licensed access to the connected data providers | `paid-claude-plan`, `data-subscription:daloopa`, `data-subscription:s-and-p-global` |
| 3 | [Using Daloopa for financial analysis](https://academy.claude.com/tutorials/using-daloopa-for-financial-analysis) | You will need to contact Daloopa to get access to the MCP server. For Organization Owners: Admin settings to add the custom connector. | a Daloopa relationship, Claude org-admin rights / access is by invitation only | `data-subscription:daloopa`, `connector:daloopa` |
| 4 | [Using Databricks for Data Analysis](https://academy.claude.com/tutorials/using-databricks-for-data-analysis) | The Databricks integration consists of three separate connectors, each requiring separate setup, to access organizational data through Unity Catalog. | a Databricks workspace with Unity Catalog, Claude org-admin rights | `data-subscription:databricks`, `connector:databricks` |
| 5 | [Using LSEG for financial market data analysis](https://academy.claude.com/tutorials/using-lseg-for-financial-market-data-analysis) | You will need to contact LSEG to get access to the MCP server. | an LSEG relationship, Claude org-admin rights / invitation-only | `data-subscription:lseg`, `connector:lseg` |
| 6 | [Using PitchBook for investment research](https://academy.claude.com/tutorials/using-pitchbook-for-investment-research) | Users must possess Single Sign-On (SSO) credentials and a seat-based, unlimited, or trial PitchBook license. | PitchBook Premium (seat-based, unlimited, or trial license) with SSO | `data-subscription:pitchbook`, `connector:pitchbook` |
| 7 | [Using the Blackbaud connector in Claude](https://academy.claude.com/tutorials/using-the-blackbaud-connector-in-claude) | Connect to your Blackbaud environment. Sign in with your Blackbaud ID. Secure access to your Raiser's Edge NXT fundraising data. Blackbaud marketplace admins and organization owner | a Blackbaud account, a marketplace admin install | `data-subscription:blackbaud`, `connector:blackbaud` |
| 8 | [How to install and use the Claude for Small Bu](https://academy.claude.com/tutorials/how-to-install-the-claude-for-small-business-plugin) | You'll need the Claude desktop app on a Pro, Max, Team, or Enterprise plan. | claude desktop app installed, claude pro max or team subscription | `paid-claude-plan` |
| 9 | [Get started with Claude Design (Help Center)](https://support.claude.com/en/articles/14604416-get-started-with-claude-design) | Claude Design is available in beta on Pro, Max, Team, and Enterprise plans. It isn't available on the Free plan. | claude account / Claude Design needs Pro, Max, Team or Enterprise | `paid-claude-plan` |
| 10 | [Set up your design system in Claude Design](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design) | Claude Design is available in beta on Pro, Max, Team, and Enterprise plans. It isn't available on the Free plan. | claude design workspace set up, existing design system | `paid-claude-plan` |
| 11 | [Draft investment memos](https://academy.claude.com/use-cases/draft-investment-memos) | This workflow uses capabilities available to Claude for Enterprise customers. Financial data connectors may require existing subscriptions or licenses with the underlying providers | (draft investment memos) connectors to Daloopa and S&P Global | `paid-claude-plan`, `data-subscription:daloopa`, `data-subscription:s-and-p-global` |
| 12 | [Build financial models](https://academy.claude.com/use-cases/build-financial-models) | Claude for Excel is currently in beta as a research preview. Join the waitlist to get access. Enable connections to S&P Global, Daloopa, and Box. | (build financial models) enable connections to S&P Global, Daloopa and Box | `paid-claude-plan`, `data-subscription:daloopa`, `data-subscription:s-and-p-global` |
| 13 | [15 Claude Tips for Everyday Data Analysis](https://www.linkedin.com/learning/15-claude-tips-for-everyday-data-analysis) | Start my 1-month free trial / Join now - the course content sits behind a LinkedIn Learning subscription. | linkedin learning subscription | — |
| 14 | [Claude for financial services overview](https://academy.claude.com/tutorials/claude-for-financial-services-overview) | No requirement stated. The page lists Daloopa and Morningstar as available integrations and does not say either is required. | Claude for Financial Services, a Daloopa and/or Morningstar account / real use needs Claude for Financial Services plus  | — |
| 15 | [Prompting strategies for financial analysis](https://academy.claude.com/tutorials/prompting-strategies-for-financial-analysis) | No requirement stated. Daloopa and Kensho/S&P Global appear as sources Claude can reach; the page does not say a subscription is needed. | assumes Daloopa and Kensho/S&P Global connectors are already available to you | — |
| 16 | [Answer the ad-hoc data question](https://academy.claude.com/use-cases/answer-the-adhoc) | If your admin manages plugins and it's not available yet, skip this; nothing below requires it. Want to try this task before setting anything up? Add your files to a working folder | Claude Cowork, schema export, Databricks/Snowflake connector | — |
| 17 | [Working smarter with Claude in PowerPoint](https://academy.claude.com/tutorials/working-smarter-with-claude-in-powerpoint) | No requirement stated. | paid claude plan (pro, max, team, or enterprise), microsoft 365 account, powerpoint installed | — |
| 18 | [Financial analysis workflows with Claude](https://academy.claude.com/tutorials/financial-analysis-workflows-with-claude) | Using each provider's data may require a separate subscription or API key from that provider. The examples assume you have the necessary integrations enabled. | licensed access to Daloopa, S&P Global or FactSet | — |
| 19 | [Getting started with Claude for nonprofits](https://academy.claude.com/tutorials/getting-started-with-claude-for-nonprofits) | 501(c)(3) organizations, K-12 schools, and qualifying healthcare organizations must verify their nonprofit status. Make sure you have admin permissions. | nonprofit status verifiable through Goodstack | — |
| 20 | [Analyze fundraising performance](https://academy.claude.com/use-cases/analyze-fundraising-performance) | For most organizations, uploading exported CSV or Excel files works perfectly. The connectors are an optional enhancement. | two years of channel-level fundraising data, optional connectors | — |
| 21 | [Build an 'Ask the Company' agent](https://academy.claude.com/use-cases/ask-the-company) | Confluence access comes through the Atlassian Rovo connector. Snowflake is listed as an optional connector. None is mandated to begin. | (ask the company) engineering teams tired of re-answering the same questions | — |
| 22 | [Claude Code on Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock) | Prerequisites: an AWS account with Amazon Bedrock access enabled; access to desired Claude models; appropriate IAM permissions. | aws account with appropriate permissions, claude code installed | — |
| 23 | [AI Fluency for Nonprofits](https://academy.claude.com/courses/ai-fluency-for-nonprofits) | Access to an AI chat tool for hands-on practice; any chatbot will work. | basic familiarity with claude or ai chat | — |

**Opened:** 23. **Given a value:** 12. **The page and the card agreed:** 19. **The page said nothing the card asserted:** 4. **The page contradicted the card:** 0.

- **15 Claude Tips for Everyday Data Analysis** — The cost chip already says `subscription`. The vocabulary has no word for the host's own paywall, and it should not: that is what cost means.
- **Claude for financial services overview** — The sibling page, Getting Started with Claude for Financial Services, does state it. This one is an overview and states nothing, so nothing is recorded here.
- **Answer the ad-hoc data question** — The card lists the connector as a prerequisite and the page says in as many words that nothing below requires it. Not a contradiction about the world - the page offers a path without it that the card does not mention.
- **Working smarter with Claude in PowerPoint** — The Office add-ins do need a paid plan - the Excel page says so plainly. This PowerPoint page does not, and the page is the evidence.
- **Financial analysis workflows with Claude** — A conditional, naming no single provider, so there is no one subscription to record.
- **Getting started with Claude for nonprofits** — Nonprofit eligibility is not a vocabulary word, and should not become one for a single row.
- **Claude Code on Amazon Bedrock** — An AWS account is not in the vocabulary. It is also the opposite of a paid Claude plan: this page is how you use Claude Code without one.


## D4 — what a thing needs is not what it costs

The field, the vocabulary and the rule are in
[`specs/2026-09-07-needs-field.md`](../specs/2026-09-07-needs-field.md). A value has to be
drawable and it has to be written down: `ui.js` says what the interface can render, the
copy deck says why the word exists, and `validate-catalogue.py` rejects a value missing
from either. Both halves are planted in the bite test, which needed the copy deck to
become an argument the tests can replace — the same way the `reviewed` allowance already
was.

The chip sits beside the cost chip, one per card, ordered by what costs a reader most to
find out late: the plan, then the subscription, then the machine. Everything else is on
the resource page under **Also needs**, because a connector is free to switch on and a
GitHub account is free.

## D3 — the ladder, per role

`measure.py` writes it on every build, and part 11 says one sentence per role pointing at
it. The rung a role runs out at is the first with no picks, or with none addressed to that
reader.

The first version of that measurement counted only picks naming the role, and four roles
came out running out at `never-used` — where a card saying "Anyone who has never opened
Claude" is exactly the right card. It now uses the test the picks validator uses: names
the role, or names nobody in particular. **A measurement that contradicts the rule the
site enforces is measuring the wrong thing**, and it took a nonsensical answer to notice.

The developer is stated in part 11 as the exception it is. It reaches `builder` like most
roles; its pool there is an order of magnitude deeper than any of theirs. Every claim this
site makes about the advanced end being usable is, underneath, a claim about one role's
shelf.

## The skip lines, measured and not touched

Of the skip lines in the catalogue, fewer than half finish the sentence the card starts —
*Skip if you…*. The figure is in STATUS.md's catalogue table, regenerated on every build.
No rewrite: the number is there so the round that decides the style argues from it.

## What surprised me

**The docs gate crashed instead of reporting.** It found ten typed counts in two new
specs and then died printing the first of them, because the line held a character the
Windows console encoding cannot represent. The build went red, which is right, and it went
red saying `UnicodeEncodeError` instead of saying what it found. Five scripts already
guarded their stdout; thirty-five did not. The same crash could hit a gate on its way to
printing a pass, and nobody could tell which from the exit status.

**The planted fault for the mirror had to be aimed twice.** Four of the five files that
mirror are read by a gate that runs earlier, so removing one goes red for a reason that
has nothing to do with the mirror — and the harness refuses a fault that trips the wrong
gate. That rule caught me. The publisher marks are read there and nowhere else, and they
are also the mildest of the five: the page degrades rather than breaking. Which is the
point. A rule that only fired on the fatal ones would still ship a page asking for a file
nobody wrote.

**Reading pages found a third bucket.** The spec expected a page and a card to agree or to
disagree. Across the rows opened, most agreed and **none contradicted** — but several
pages state nothing at all while the card asserts a requirement, and in at least one of
those the card is right and the evidence sits on a sibling page. A card is more often
ahead of its page than wrong about it. So the stop rule counts contradictions, not
silences, and that is a widening of the ruled rule which is said here rather than done
quietly.

## What I got wrong

**I gave a library a guard it could not use.** The pass that reconfigured stdout tested
for a top-level `import sys` with a substring search, and `stem.py` has one inside its own
`__main__` block. The guard went in, the import did not, and the next build stopped at the
search index with a `NameError` thrown by the stemmer. A substring search answers a
different question from an AST walk.

**The ladder's first measurement was nonsense and I nearly shipped it.** Four roles
"running out" at the beginner rung, because beginner cards address nobody in particular.
Caught by reading the table, not by a check.

**The slugs read badly and the articles were wrong.** `data-subscription:lseg` rendered as
"needs a Lseg subscription". A slug is lowercase and hyphenated so a validator can check
it; a company name is neither, and an article follows a sound rather than a letter.

**The data pass is short of its checkpoint.** Twenty-three rows opened of the forty the
spec asks for, and the reason is mine rather than the data's: reading pages one at a time
is expensive and the round had to ship. The shortlist is on disk in order and the opened
rows are marked, so resuming is a matter of continuing down it. Nothing was stopped by the
stop rule.

## Was it in CLAUDE.md

Three of the four, yes.

- *"Verify before claiming done: run it, open it, check the links."* The ladder table was
  wrong in a way no check could see and reading it caught it. So was the article in "a
  Lseg subscription".
- *"A check whose failure cannot be seen is not a check."* This round's whole
  generalisation, and the docs gate crashing was the same rule wearing a different face: a
  gate that falls over while reporting has not refused anything.
- *"Numbers anywhere a reader will read them are generated or measured, never typed."* The
  ladder and the skip figure both went into `measure.py` rather than into prose, and the
  docs gate made me date the counts in my own new spec.
- The one that is not in CLAUDE.md is the substring-versus-AST mistake, and it does not
  belong there. It belongs in the habit of testing what you assert rather than what is
  easy to grep.

## Not done

STATUS.md "Needs a person", THE-PROJECT part 10, the human test, and the paste into Teams.


## The gates

Every gate has a bite test: the fault is planted, the whole build runs, and it has
to go red at the gate meant to catch it. Three were added this round.

| planted fault | the build goes red saying |
|---|---|
| a listed row carrying a verdict | 'tier is listed' |
| a question that is a suite query | 'check-questions.py' |
| a suite query forced to miss | 'REGRESSION' |
| a content gap with no evidence | 'A content gap is a claim about the' |
| a synonym with no reason | 'validate-synonyms.py' |
| a dead pick | 'validate-picks.py' |
| a typed count in a pick's reason | 'check-typed-numbers.py' |
| a live count typed into a document | 'state a count with no date beside ' |
| a surface building its own freshness line | 'never asks for the freshness line' |
| a mirror source that vanished | 'every one of these is a file the s' |
| a served description past the cap | 'and the cap is' |
| a path step the catalogue knows is superseded | 'superseded step' |
| share pages keeping their placeholder head | "serves the shell's placeholder" |

An untouched copy builds green.

