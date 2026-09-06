#!/usr/bin/env python3
"""A content gap has to carry the pages it ruled out. This proves the rule fires.

    python3 scripts/test-gap-claims.py

Every content gap this suite recorded before FIX-30 was written from cards rather than
pages, and every one was wrong when the pages were opened. The rule that came out of
that is in test-search.py: a `content-gap` row must carry a sixth field naming the
pages that were opened. A rule nothing tests is a comment, so this file feeds
`gap_claims` rows that should be refused and rows that should pass, and fails if the
refusal is not exactly where it should be.
"""
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location(
    "ts", os.path.join(ROOT, "scripts", "test-search.py"))
ts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ts)

GOOD = "https://example.com/page - the page never names the subject"

CASES = [
    # (label, row, should the rule complain?)
    ("a gap with no evidence at all",
     ("pm", "burndown chart", "content-gap", "", "nothing here covers it"), True),
    ("a gap whose evidence list is empty",
     ("pm", "burndown chart", "content-gap", "", "nothing here", []), True),
    ("a gap whose evidence names no page",
     ("pm", "burndown chart", "content-gap", "", "nothing here",
      ["I looked and there was nothing"]), True),
    ("a gap handed a bare string instead of a list",
     ("pm", "burndown chart", "content-gap", "", "nothing here", GOOD), True),
    ("a gap that opened one page and says what it said",
     ("pm", "burndown chart", "content-gap", "", "nothing here", [GOOD]), False),
    ("a gap that opened three",
     ("pm", "burndown chart", "content-gap", "", "nothing here",
      [GOOD, GOOD, GOOD]), False),
    ("an ok row, which the rule must leave alone",
     ("pm", "write a prd with ai", "ok", ["Write a PRD"], "fine"), False),
    ("a bad row, which the rule must leave alone",
     ("pm", "sql", "bad", "Something wrong", "the agent's reason"), False),
]

bad = 0
for label, row, expect in CASES:
    got = bool(ts.gap_claims([row]))
    if got != expect:
        bad += 1
        print("  WRONG  %s: expected %s, got %s"
              % (label, "a complaint" if expect else "silence",
                 "a complaint" if got else "silence"))

live = ts.gap_claims(ts.SUITE)
if live:
    bad += 1
    print("  The suite itself has a content gap with no pages behind it:")
    for q, why in live:
        print("    %-42s %s" % (q[:42], why))

if bad:
    print("%d case(s) wrong. The rule does not do what its header says." % bad)
    sys.exit(1)

print("Content gaps: %d case(s) checked, the refusal fires on evidence-free claims "
      "and stays quiet otherwise." % len(CASES))
