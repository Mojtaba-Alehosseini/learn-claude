# Attack plan — 10 roles, 10 files, 1 summary

A long job. This file exists so that nothing is invented, nothing is confused, and
nothing is skipped. Read it before each batch and again before the synthesis.

## The rule that matters most

**No number may be invented.** Every figure comes from one of three places:

1. `docs/attack/00-facts.md` — already measured, authoritative
2. a command run in this session, with the command shown
3. the live site, opened in a browser

If a claim has none of those behind it, it does not go in the file. "Probably",
"likely", "seems" are banned in findings. They are allowed in the *opinion* section, and
only there.

## The 10 roles — fixed, in this order

| # | role key | shown to a visitor as | resources |
|---|---|---|---|
| 1 | `non-technical` | not a coder | 68 |
| 2 | `student` | a student | 41 |
| 3 | `researcher` | a researcher | 41 |
| 4 | `teacher` | a teacher | 47 |
| 5 | `developer` | a developer | 94 |
| 6 | `data-analyst` | working with data | 37 |
| 7 | `pm` | a product manager | 56 |
| 8 | `designer` | a designer | 29 |
| 9 | `business-founder` | running a business | 54 |
| 10 | `writer-marketer` | a writer | 41 |

Ten. Not nine, not eleven. Tick each one off in the tracker below as its file lands.

## What each agent does

One agent per role. It is **that person**, not a reviewer being polite. It wants to
learn Claude today, it has an hour, and it is unimpressed. It must be hostile — a
finding that flatters the site is worthless here.

It does all of this:

1. Opens `https://mojtaba-alehosseini.github.io/learn-claude/` and answers the two
   questions honestly as that role, at **every one of the four levels**.
2. Follows through to Browse. Reads the actual cards it is given — titles, `Skip if:`,
   dates, badges.
3. Opens Paths. Is there a route for this person? Follows one if there is.
4. Opens two or three resource pages and judges whether it would click through.
5. Searches the way this person would phrase it — three real sentences in their own
   vocabulary, not keywords.
6. Looks at the whole thing on a phone-width viewport.

## What each agent writes

Fixed path: `docs/attack/NN-<role>.md`, e.g. `docs/attack/08-designer.md`.

Fixed sections, all of them, in this order. An empty section is written as "nothing
found" — it is never deleted, because a missing section reads as a skipped step:

```
# Attack: <role shown to a visitor>
Written as someone who is <role>, at <date>. Site version: <git short sha>.

## 1. The first 60 seconds
## 2. Does the front door work for me       (all four levels, with counts)
## 3. What the catalogue actually gives me  (are these really for me?)
## 4. Paths
## 5. The card and the resource page
## 6. Search, in my words
## 7. On a phone
## 8. Content quality — the three worst entries I was shown, quoted
## 9. Everything that is broken, ranked                (evidence for each)
## 10. The one thing that would make me leave and not come back
## 11. What is genuinely good                          (be honest, but brief)

## Checklist — every line ticked or the file is not finished
- [ ] I opened the live site
- [ ] I tried all four levels
- [ ] I quoted at least 5 real titles or lines from the site
- [ ] Every number I used is in 00-facts.md or I show the command
- [ ] I looked at a phone width
- [ ] I found at least one thing nobody has mentioned before
```

**Agents find. Agents do not fix.** No edits to any file outside `docs/attack/`.

## Running order

Two batches of five, so nothing overloads and I can check the first five before
committing to the rest.

- Batch A: non-technical, student, researcher, teacher, developer
- Batch B: data-analyst, pm, designer, business-founder, writer-marketer

After each batch: confirm all five files exist, have all 11 sections, and have a
completed checklist. **A file that fails this is re-run, not patched by hand.**

## Then the summary

Read all ten files. Write `docs/attack/SUMMARY.md`:

- What every role hit — a problem 8 of 10 people have is structural, not a detail
- What only one role hit, where it is severe enough to matter anyway
- The findings ranked by how much they cost a real visitor, not by how easy they are
- Anything the ten files disagree about, named as a disagreement rather than averaged
- What is genuinely good, so it does not get refactored away later
- The decisions that are Morteza's and not mine

Then verify: every claim in the summary traces to a numbered finding in one of the ten
files. A summary point with no parent is deleted.

## Tracker

| # | role | file written | 11 sections | checklist done |
|---|---|---|---|---|
| 1 | non-technical | 01-non-technical.md | 11/11 | yes |
| 2 | student | 02-student.md | 11/11 | yes |
| 3 | researcher | 03-researcher.md | 11/11 | yes |
| 4 | teacher | 04-teacher.md | 11/11 | yes |
| 5 | developer | 05-developer.md | 11/11 | yes |
| 6 | data-analyst | 06-data-analyst.md | 11/11 | yes |
| 7 | pm | 07-pm.md | 11/11 | yes |
| 8 | designer | 08-designer.md | 11/11 | yes |
| 9 | business-founder | 09-business-founder.md | 11/11 | yes |
| 10 | writer-marketer | 10-writer-marketer.md | 11/11 | yes |
| — | SUMMARY.md | SUMMARY.md | n/a | 161 citations, 0 broken |

## Already known — do not present these as new

They are in `00-facts.md` and I found them before this exercise. An agent may confirm or
sharpen them, but the value is in what is *not* on this list.

- 4 roles have no path: data-analyst, pm, designer, writer-marketer
- designer is the thinnest role at 29, and has 1 resource at never-used
- 0 of 353 are `reviewed` — the best badge is empty
- "Found something wrong? Tell us." has no way to tell anyone
- 171 of 353 have no publish date
- Nothing re-checks the links; every `checked` date is August 2026
