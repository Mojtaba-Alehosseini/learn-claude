# Regression sweep — every Attack 1 high finding, re-tested

Attack 1 ran 2026-08-27 against site version `22e4532` and 353 resources. Nine rounds of
change since; the catalogue is now 635. This re-tests what that run rated high.

**Method.** `tmp/regression.py` measures each finding against today's `data/items.json`,
`paths.json`, the shipped JS and the served HTML. The `?q=` deep link was additionally
re-run against the **live site** in a browser, because a source comment claiming a fix is
not a fix. Every figure below came out of one of those two, not out of memory.

**One note on the brief.** It asked for "96-character lines". No Attack 1 finding uses that
phrase. The only "96" in `SUMMARY.md` is §2.5 — the filter grid dead-ending on 96.2% of
combinations — so that is what I re-tested, and it is in the table.

---

## The table

| # | Attack 1 finding | Roles then | Fixed in | Still fixed today |
|---|---|---|---|---|
| §1.1 | Home-page `?q=` deep link returns 0 and blames the visitor | 7/10 | `browse.js` boot path — index fetched *before* first render when `q` is present | **Yes. Verified live.** |
| §1.2 | Verdicts published for content nobody opened | 7/10 | — | **No. Unchanged, at 1.7x the scale.** |
| §1.3 | Paths have `roles` and throw them away; steps tagged for other roles | 6/10 | `paths.js` / `home.js` / `browse.js` all read `.roles`; paths rebuilt | **Yes, and completely.** |
| §1.4 | Duplicates the pipeline cannot see | 6/10 | URL + normalised-title de-dup with an allow-list file | **Yes.** |
| §1.5 | 42 KB of `notes` downloaded by every visitor, rendered by nothing | 6/10 | `notes` removed from the browser mirror | **Yes for the shipping. No for the prices.** |
| §1.6 | Role tags wrong in both directions | 5/10 | — | **No.** |
| §1.7 | Publisher names machine-mangled | 5/10 | 49 hosts mapped, 7 platforms added (`a169b73`) | **The named cases, yes. The class, no — it came back with the harvest.** |
| §2.1 | Unsourced allegation against a named real academic | 1/10 | Removed from `items.json` and every file that repeated it | **Yes. Gone, and nothing like it returned.** |
| §2.2 | Every shared link previews as "Resource — Learn Claude" | 1/10 | — | **No. Unchanged.** |
| §2.3 | Eight cards claim to be steps in paths they are not in | 2/10 | `|| x.paths` fallback removed from `ui.js` | **Yes.** |
| §2.4 | `Skip if:` written by two hands; tautologies; label repeated | 2/10 | Rewritten — median length 38 -> 188 chars | **Half. The tautologies are gone; the doubled label is not.** |
| §2.5 | Filter grid dead-ends 96% of the time on the biggest role | 1/10 | — | **No. Marginally worse, and still no tier axis.** |
| §2.9 | "What it teaches" is raw lowercase model output | 2/10 | `PROPER` map in `ui.js` re-cases single words at render | **Half, and the half it misses is the product's own name.** |

---

## The evidence, finding by finding

### §1.1 — the `?q=` deep link. Fixed, and verified live.

The four sentences that returned **0** in August, re-run today against
`https://mojtaba-alehosseini.github.io/learn-claude/`:

| Query | Aug 2026 | Today | First result today |
|---|---|---|---|
| `?q=how do I cite Claude&role=student` | 0 | **3** | Referencing AI and Acknowledging AI Use |
| `?q=I don't know where to start` | 0 | **27** | Introduction to Claude (code-along) |
| `?q=how do I stop students cheating&role=teacher` | 0 | **17** | AI & Academic Integrity |
| `?q=will it fabricate citations&role=researcher` | 0 | **5** | Claude for medical literature search: Avoid hallucinations |

Four of four now return results, and the top result is on-topic in all four. The count line
no longer misreports either — it reads `3 resources for "how do I cite Claude"`, quoting the
query back.

The mechanism is in `browse.js` with the measurement written next to it: *"when there is a
query, fetch the index before the first render rather than after it. Rendering first and
correcting afterwards would only replace a wrong answer with a flicker."*

**Note for the current round.** This is fixed and the ten agents still filed search as a top
finding — but for a different reason. August's fault was *the index never loaded*. Today's is
*the index ranks badly*: no stemming, no synonyms, no tie-break, and `skip_if`/`who_for` are
not indexed at all. Same symptom, different cause, and the old cause has not returned.

### §1.2 — verdicts for content nobody opened. Not fixed; larger.

```
tiers: previewed 501, ai-reviewed 98, listed 36, reviewed 0
listed items carrying BOTH skip_if and who_for: 36 of 36
videos checked past the outline:  0 of 101   (Aug: 0 of 78)
courses checked past the outline: 0 of 58    (Aug: 0 of 54)
```

Every one of the 36 "Found only" items — the tier whose printed definition is *"Nobody has
looked at the content yet"* — still carries a full who-for and a full skip-if. August found
43 of 43. Today it is 36 of 36. The proportion did not move.

Eight of the ten agents this round found it independently, and every one of them named it
their number one. It is the same finding, one round older.

### §1.3 — paths and roles. Fixed, and completely.

August: *"Both paths naming a student contain 0 of 6 and 0 of 5 steps tagged `student`. Step
1 of the researcher path is tagged `data-analyst` only. 1 of 17 path steps carries the
writer's tag."*

Today, steps carrying a role their own path names:

```
first-week 6/6   claude-code-start 6/6   writing-you-sign 4/4
pm-without-engineering 5/5   research-with-claude 5/5
numbers-you-can-defend 5/5   judging-ai-design-work 5/5
```

36 of 36. `paths.js`, `home.js` and `browse.js` all read `.roles`, and `index.html` links
paths from the front door.

This round's path complaints are all different ones: no path above beginner level, no path
for a teacher, no path for the largest role, the "about 81 minutes" label, and paths hiding
the `Skip if:` line. None of those is the August fault.

### §1.4 — duplicates. Fixed.

```
duplicate normalised titles: 1 group, 0 not on the allow list
duplicate URLs: 0
```

The August case — "Claude Code 101" living on two domains with different time chips, both
claiming step 1 of the same path — cannot recur: de-duplication now runs on normalised title
as well as URL, and the one surviving collision is recorded in `data/duplicate-titles.txt`
with a reason. No agent this round reported a duplicate.

### §1.5 — the 42 KB nobody sees. Fixed for the shipping. Not for the prices.

`data/items.js` is 764,992 bytes and **the string `"notes"` does not appear in it.** The
field stays in `items.json` on 621 items as the working record and never reaches a browser.
That is the finding closed.

The half that is not closed is the one August cared about most: **the prices are still
invisible.** `cost` is still four buckets — `free`, `free-account`, `paid-once`,
`subscription` — with no price field anywhere. The researcher this round found the $995
seminar's figure buried mid-sentence in its `skip_if`; the founder found a paid Udemy course
with no price on the page at all. Same gap, new hiding place.

### §1.6 — role tags. Not fixed.

A crude keyword probe over `who_for` flags 204 of 235 business-founder cards, 129 of 170 PM
cards and 123 of 163 non-technical cards as never naming that reader. **That probe
over-counts** — a card can serve a reader without using the job title — so I am not reporting
it as the finding. The hand-read numbers from this round are the evidence:

- PM|builder: **12 of 58** cards name a *different* job in their own `For:` line — sales reps,
  in-house counsel, litigation attorneys, recruiters, buy-side equity analysts.
- non-technical|never-used: **21 of 68**, including five US healthcare-coding connectors and
  eight nonprofit fundraising pages.
- student: **10 of 79**, four of them in the ten-item "used it a lot" cell.
- data-analyst: *"Prompting 101"* (`For: Developers`) and *"Analyze patterns in user feedback"*
  (`For: Designers and product managers`).

And the other direction is unchanged too: the Vanderbilt Turnitin page — whose own note is
about false accusations against **non-native English writers** — is still `roles: ["teacher"]`
and unreachable from the student filter.

### §1.7 — publisher names. The named cases fixed; the class returned.

August's specific list is gone: no "Pl", no "Vc", no "To", no "Jhu". `a169b73` mapped 49
hosts by name and added 7 platforms.

But the mapping is a lookup table, and 282 resources have been harvested since. Today, of 171
distinct sources:

- still short or slug-shaped: **`Und`** (University of North Dakota, via `libguides.und.edu`),
  **`Master`** (`master.dev`), **`bri`**, **`Zhiyang`**
- still raw domains printed as a publisher: **`qwe.edu.pl`**, **`ranthebuilder.cloud`**,
  `mcpservers.org`, `prodmgmt.world`, `Journalism.co.uk`, `freeCodeCamp.org`, `Builder.io`

Two agents hit "Und" without prompting; the student found it on the resource page's primary
button, which reads **"Open on Und"**. The fix worked on the rows it was run against and does
not hold new rows to the same standard.

### §2.1 — the unsourced allegation. Fixed, and nothing like it came back.

The named-individual claim is gone from `items.json`. I scanned all 635 items' `summary`,
`skip_if`, `who_for` and `notes` for allegation-shaped words. Ten hit, and every one is
legitimate topical content: six about Claude *fabricating* citations, two about protecting
students from false *accusations* (Vanderbilt, St. Catherine), one about incorrect responses,
one about a journalist's standards file. No item accuses a person of anything.

This was Attack 1's most urgent finding — the only one that could produce a letter. It is
closed.

### §2.2 — shared-link previews. Not fixed.

`resource.html` still ships:

```
<title>Resource — Learn Claude</title>
<meta property="og:title" content="Resource — Learn Claude">
```

All 635 resource pages share one title and one social preview, next to a **Copy link** button.
Two agents found it independently this round without knowing it was an August finding. The
developer added a new consequence August did not measure: `sitemap.xml` lists **353** resource
URLs — the August count — of which **35 point at ids that no longer exist**, and the first URL
in the file renders "Not found" at HTTP 200.

### §2.3 — false path membership. Fixed.

35 items carry a path field; **0 of them are absent from the path they name.** The `|| x.paths`
fallback in `ui.js` that resurrected a stale field is gone, and no card prints a raw internal
slug. No agent reported one.

### §2.4 — `Skip if:` written twice. Half fixed.

Fixed: the tautologies. `skip_if` median length is now **188 characters** (August: 38 on the
19-Aug batch), and only **3 of 635** are under 40 characters. Nothing now reads *"You don't
use R."*

Not fixed: the doubled label. **157 of 635 (25%)** still open by repeating the heading they sit
under — "Skip if: **Skip if** you do not write shell scripts." The writer counted thirteen
consecutive offenders on one screen and noted that 104 other cards use the correct convention,
so both hands are still in the file. Two more use the field for the opposite of its label,
opening **"Nothing —"**.

### §2.5 — the filter dead-end. Not fixed; marginally worse.

Biggest role is now `business-founder` (235 items, up from developer's 94).

```
role + one value on all five other axes: 3487 of 3584 return 0  (97.3%)
```

August measured 96.2%. Growing the catalogue by 80% did not open the grid, because the new
material clusters: 291 of 635 items come from one host, and 78 of the 148 fifteen-minute
recipes all sit at one level.

And the sub-finding is untouched: **`browse.html` still offers no tier filter.** The
four-level ladder is the site's stated differentiator and is not an axis you can filter on.
Three agents asked for it by name this round.

### §2.9 — lowercase `teaches` bullets. Half fixed.

**1,365 of 1,365 bullets still start lowercase in the data.** `ui.js` re-cases at render from a
hardcoded `PROPER` map of about 36 single words, so `csv` becomes `CSV` — and `claude code`
does not, because `code` is not in the map and the map is single-word only.

Result, live on `resource.html?id=r-4d17281029`, four consecutive bullets under an H1 that
spells it correctly:

> Install Claude **code** across **macos linux and windows** environments

Two agents found this independently, one measuring **164 bullets across 112 resource pages**
rendering "Claude code", "Claude skills", "Claude projects". Also unchanged: **1,252 of the
1,365 bullets contain no comma at all.**

---

## What the sweep says

Six of thirteen fully fixed, two half fixed, five not fixed.

The six that closed are all **mechanism** faults: a load order, a missing field read, a
de-dup key, a stale fallback, a bad row, a payload. Each had one place to change and it stayed
changed.

The five that did not close are all **policy** faults — decisions the site has not made rather
than code it has not written: whether an unread item may carry a verdict, what a role tag has
to be true of, whether a shared link needs a name, whether the checking ladder is something you
can filter by, whether the prices get a field.

And §1.7 is the interesting one, because it is neither. It was fixed correctly, for every row
that existed on the day it was fixed, by a lookup table — and 282 rows arrived afterwards that
nobody held to it. That is not regression. That is a fix that does not run on new material.
