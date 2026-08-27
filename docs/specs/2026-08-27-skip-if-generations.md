# `Skip if:` was written by more than one hand — measured 2026-08-27

Two attack agents found this independently by different methods: the data-analyst by
length, the writer by punctuation. Both were right and both saw part of it. Measured
across all 352 entries, grouped by the date the entry was checked:

| checked | rows | median chars | mean | opens "Skip" | em dash | tautologies |
|---|---|---|---|---|---|---|
| 2026-08-18 | 65 | 90 | 91 | 1 (2%) | 38 (58%) | 2 |
| 2026-08-19 | 22 | **38** | 41 | 0 (0%) | 0 (0%) | 6 |
| 2026-08-20 | 50 | **50** | 57 | 0 (0%) | 13 (26%) | 2 |
| 2026-08-21 | 143 | 164 | 167 | 93 (65%) | 22 (15%) | 1 |
| 2026-08-22 | 72 | 130 | 134 | 71 (99%) | 2 (3%) | 0 |

Reproduce with the script at the bottom of this file.

## What the numbers actually say

It is not two clean generations. There are two separate splits that happen to overlap.

**A quality split.** 19 and 20 August are the weak days: medians of 38 and 50 characters
against 164 and 130 later. **72 entries, 20% of the catalogue.** Eight of those are
tautologies of the form "you don't use X" — a line that tells a reader nothing they did
not already know from the title:

```
 16  ClaudeR (R + RStudio MCP)         "You don't use R."
 20  Use Claude for Excel              "You don't use Excel."
 20  Claude Code and Figma: Set up …   "You don't use Figma."
 21  Guide to the Figma MCP server     "You're not using MCP."
 22  Tableau MCP (official)            "You don't use Tableau."
```

**A style split, and it does not fall on the same line.** 18 August is not short — its
median is 90 — but 58% of its lines use an em dash and only 1 of 65 opens with the word
"Skip". By 22 August, 99% open with "Skip" and 3% use an em dash. So 18 August is
well-written in a different voice, while 19 and 20 August are simply thin. Judging the
catalogue by punctuation alone would wrongly condemn 65 good entries.

Which is why the visible symptom is what it is: 16 of the student's 41 cards and 18 of
the writer's 41 render as "Skip if: Skip if …", because the later convention stores the
label inside the value and the card prints the label too.

## Not rewritten

72 entries is a fifth of the catalogue and `Skip if:` is the product. Rewriting them is
a content decision and it is Morteza's. This file exists so the size of the job is known
before anyone starts it.

Three things worth deciding at the same time, because they are the same decision:

1. Whether the stored value should contain the words "Skip if" at all. Today 165 of 352
   do and 187 do not, and the card prints the label either way — which is where
   "Skip if: Skip if …" comes from.
2. Whether the em-dash voice of 18 August or the "Skip if" voice of 22 August is the
   house style. Both read well. They do not read the same.
3. Whether a tautology should fail the build. `validate-catalogue.py` already rejects
   placeholders like "N/A."; "You don't use R." passes it and says just as little.

## Reproduce

```bash
python3 - <<'PY'
import json, io, statistics, collections, re
items = json.load(io.open('data/items.json', encoding='utf-8'))
g = collections.defaultdict(list)
for i in items: g[i['checked']].append(i)
for d in sorted(g):
    rows = g[d]; L = [len(i['skip_if']) for i in rows]
    opens = sum(1 for i in rows if i['skip_if'].lower().startswith('skip'))
    em = sum(1 for i in rows if '—' in i['skip_if'])
    taut = sum(1 for i in rows if re.match(r"^you (don'?t|do not|are not|aren'?t) (use|using)\b",
                                           i['skip_if'].lower()))
    print(d, len(rows), statistics.median(L), opens, em, taut)
PY
```
