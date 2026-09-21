#!/usr/bin/env python3
"""
The stemmer. One function, twenty-odd rules, no dependency.

    from stem import stem
    stem("hallucinations")   -> "hallucin"

It is applied in exactly two places and they must be the same place: when the index is
built (`build-search-index.py`) and when a query is parsed (`test-search.py`, and its
mirror in `assets/js/search.js`). A stemmer used on one side only is worse than none -
it guarantees the query and the index disagree.

WHY NOT PORTER

Because this has to run identically in Python and in a browser with no build step, and
because a person has to be able to read it and predict what it does to their word. Porter
is 200 lines with a measure function; this is a suffix table applied to a fixed point.

THE RULES, AND THE TWO THAT WERE ARGUED

`ations/ation/ating/ated/ates/ate` are **removed**, not mapped to `at`. Mapping to `at`
collapses hallucinate/hallucinated/hallucination equally well, but leaves `citation` at
`citat` while `cite`, `cited` and `citing` reach `cit` - and half of Attack 2's cause 1 is
a citation query. Removal plus the trailing-`e` rule brings all four to `cit`.

`ise -> ize` and `isation -> ization` sit here rather than in the spelling-pairs step,
because they are suffixes and the same fixed point handles them: `prioritise`,
`prioritize`, `prioritisation` and `prioritization` all reach `prioritiz`. The remaining
British and American families - `-our/-or`, `-re/-er`, doubled `l` - are not suffixes and
belong to the pairs table.

MINIMUM STEM 3

`citation` -> `cit` is three characters. At a minimum of four the citation family does not
collapse at all, which is the fault this exists to fix. The cost is collisions - `site`
and `sit` become one term - so `build-search-index.py` prints the vocabulary count and the
largest collision groups, and a person reads them once.
"""

import re

MIN_STEM = 3

# Applied longest first, to a fixed point. A rule fires only if what is left is at least
# MIN_STEM characters, so short words survive untouched.
# (suffix, replacement, minimum stem this rule may leave).
#
# The third column exists because of one word. "cheated" ends in "ated", and at a minimum
# of 3 the -ate family cuts it to "che" before the -ed rule ever sees it. Requiring 4 from
# the short -ate members sends "cheated" to the -ed rule and "cheat", while "citation" ->
# "cit" still passes at 3 through the longer -ation rule. It also fixes create/creating/
# created, which all reach "creat" for the same reason.
RULES = [
    ("ational", "ate", 3),
    ("ization", "ize", 3),
    ("isation", "ize", 3),
    ("iveness", "ive", 3),
    ("fulness", "ful", 3),
    ("ousness", "ous", 3),
    ("ations", "", 3),
    ("ation", "", 3),
    ("ating", "", 4),
    ("ated", "", 4),
    ("ates", "", 4),
    ("ate", "", 4),
    ("ions", "", 3),
    ("ion", "", 3),
    ("edly", "", 3),
    ("ies", "y", 3),
    ("ing", "", 3),
    ("ise", "ize", 3),
    ("ed", "", 3),
    ("es", "", 3),
    ("s", "", 3),
    ("e", "", 3),
]

# No suffix rule reaches these, and the suite needs all three families.
IRREGULAR = {
    "made": "mak", "making": "mak", "make": "mak", "makes": "mak",
    "wrote": "writ", "written": "writ",
    "ran": "run", "run": "run", "running": "run", "runs": "run",
    "found": "find", "finding": "find", "finds": "find", "find": "find",
    "taught": "teach", "teaching": "teach", "teaches": "teach", "teach": "teach",
}

DOUBLED = re.compile(r"([bdfgklmnprt])\1$")


def stem(word):
    """One word to its stem. Lower-case in, lower-case out."""
    w = str(word).lower()
    if w in IRREGULAR:
        return IRREGULAR[w]
    if len(w) <= MIN_STEM:
        return w
    for _pass in range(4):
        before = w
        for suffix, replacement, floor in RULES:
            if not w.endswith(suffix):
                continue
            cut = w[:len(w) - len(suffix)] + replacement
            if len(cut) < max(MIN_STEM, floor):
                continue
            # "running" -> "runn" -> "run". Only right after an -ing or -ed removal:
            # elsewhere a doubled letter is part of the word ("skill", "address").
            if replacement == "" and suffix in ("ing", "ed") and DOUBLED.search(cut):
                cut = cut[:-1]
            w = cut
            break
        if w == before:
            break
    return w


if __name__ == "__main__":
    import sys
    for a in sys.argv[1:]:
        print("%-20s -> %s" % (a, stem(a)))
