#!/usr/bin/env python3
"""
Test search against real sentences real visitors typed.

This mirrors assets/js/search.js exactly - same index, same IDF, same admit gate, same
floor. If the ranking is wrong here it is wrong on the site, and vice versa. Run it
after any change to the enrichment or the index.

    python3 scripts/test-search.py            # the recorded suite; exits 1 on a regression
    python3 scripts/test-search.py --strict   # also fails when a known-bad query moves
    python3 scripts/test-search.py "some sentence"   # ad hoc, prints the top three

No API key and no network. An earlier version embedded the query through Gemini and
blended 55% semantic with 45% keyword, which measured well but could never be what the
site does: a static page cannot hold an API key. Testing a pipeline the browser cannot
run told us nothing useful, so both sides now run the same algorithm.

WHERE THE QUERIES COME FROM
---------------------------
Every query below was written by one of the ten agents in Attack 2 (2026-09-05), in the
voice of the role it was playing, before it had seen this file or any other. Nobody
wrote them to make the search look good. The nine sentences the suite used before this
round were written by me, which is the sample-size problem `search.js` still has in its
own header comment: eight self-authored benchmark sentences is not a search evaluation.

Each row records the agent's verdict on what it actually got:

    ok   - the top result was the right one. This is asserted. Breaking it exits 1.
    bad  - the top result was wrong. The reason is the agent's, quoted. Not asserted,
           because these are known open findings, not regressions - but the top result
           of the day is recorded, and --strict fails when it moves, so the note cannot
           quietly stop being true.

A `bad` row that starts returning the right answer is good news and the row should be
promoted to `ok`. --strict is how you find out that happened.

One caveat on the ranks. This suite ranks the whole catalogue; the agents were
browsing with their role filter applied, so a handful of rows have a different #1
here than the transcript records. Where that happens the row records what this
file sees, and the finding is unchanged either way.
"""

import json
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stem import stem  # noqa: E402

ITEMS = "data/items.json"
KW = "data/search-keywords.json"

STOP = set("""a an and are as at be but by can do does for from get go had has have how i
if in into is it its me my not of on or our so than that the their them then there these
this to up us was we were what when where which who why will with you your""".split())

MIN_IDF_SCORE = 0.05   # below this a word is in almost everything and means nothing
MIN_IDF_ADMIT = 0.7    # below this a word may rank a resource but not admit it
FLOOR_FRACTION = 0.30
FLOOR_ABSOLUTE = 2.0
PREFIX_WEIGHT = 0.3    # retired with the prefix bonus; kept so the constant list reads
STEM_WEIGHT = 0.5      # an expansion scores below the word the person typed
TIE = 0.001            # scores within this of each other are a tie, not an order


# role, query, verdict, expected-or-observed top title fragment, the agent's reason
SUITE = [
    # --- not a coder ------------------------------------------------------------
    ("non-technical", "is claude free", "ok", "Choose a Claude plan",
     ""),
    ("non-technical", "make claude remember my stuff", "ok",
     "Create and Manage Projects",
     ""),
    ("non-technical", "how do i stop claude making things up", "bad",
     "Claude for Education Is Made for Learning",
     "the safety question every new user asks, answered with a university login "
     "page; Reduce hallucinations is second"),
    ("non-technical", "write emails for me", "bad",
     "Real-World AI for Everyone",
     "a multi-week paid Coursera specialization first, a teachers' guide second, "
     "and deleting promotional mail third; Write in my voice is not in the ten"),
    ("non-technical", "use claude on my excel file", "ok", "Upload files to Claude",
     ""),

    # --- a student --------------------------------------------------------------
    ("student", "will my university know i used ai", "bad",
     "Generative AI and Academic Integrity",
     "the top answer to the most frightening question a student has is a Found only "
     "card the site says nobody opened"),
    ("student", "help me revise for exams", "ok",
     "How to Use AI to Help You Prepare for Quizzes and Exams",
     ""),
    ("student", "is it cheating to use claude for my essay", "bad",
     "Generative AI and Academic Integrity",
     "the two highest-ranked answers to the highest-stakes question are both items "
     "nobody has read"),
    ("student", "how do i cite claude in my references", "bad",
     "Documenting Your AI Use",
     "documenting, not citing; the two items that literally answer it sit at #5 and "
     "below, under a Zotero-plus-Obsidian workflow"),
    ("student", "summarise my lecture pdf and make notes", "ok",
     "AI-Powered Flashcards with Claude Projects",
     ""),

    # --- a researcher -----------------------------------------------------------
    ("researcher", "does claude make up citations", "bad",
     "Claude AI for Researchers",
     "Use Claude for Excel is second; Reduce hallucinations and Why do AI models "
     "hallucinate? are in none of the 47"),
    ("researcher", "systematic literature review", "bad",
     "Mushtaq Bilal",
     "the site's own card calls the top result a mailing-list funnel where every "
     "post is behind a subscribe form, and ranks it first"),
    ("researcher", "hallucinated references", "ok",
     "Zotero",
     ""),
    ("researcher", "peer review", "bad",
     "Peer and AI Review of Student Writing",
     "wrong sense of the word - classroom peer feedback on undergraduate essays; "
     "IEEE, which carries the one sentence a reviewer needs, is not in the top eight"),
    ("researcher", "how do i cite claude in a paper", "ok",
     "IEEE",
     ""),

    # --- a teacher --------------------------------------------------------------
    ("teacher", "can students cheat with claude", "bad",
     "Claude Code Crash Course For Developers",
     "a video for experienced web developers; the AIAS, AI & Academic Integrity and "
     "the Vanderbilt detector piece are none of them in the top five"),
    ("teacher", "make a lesson plan", "bad",
     "How Teachers Can Create Interactive Classroom Activities",
     "the top result's own Skip if says to skip it if you only need lesson plans; "
     "#5 is an autonomous coding agent"),
    ("teacher", "marking essays", "bad",
     "Claude for Education Is Made for Learning",
     "two results for the most common teacher task on earth, both aimed at students"),
    ("teacher", "ai policy for school", "ok",
     "Australian Framework for Generative AI in Schools",
     ""),
    ("teacher", "is claude safe for students", "ok",
     "Claude for Teachers",
     ""),
    ("teacher", "grading", "bad",
     "Demystifying evals for AI agents",
     "machine-learning regression testing; marking, grading, feedback and rubric are "
     "four different searches for one job because there are no synonyms"),

    # --- a developer ------------------------------------------------------------
    ("developer", "claude code hooks", "bad",
     "Hooks reference",
     "the top three tie to two decimal places so the order is file order; the top "
     "result's own card says read the guide first, this is a lookup reference"),
    ("developer", "how do i stop claude touching my tests", "bad",
     "Red Green Refactor is OP With Claude Code",
     "the right answer is second; third is a career podcast the site's own card says "
     "has almost nothing you can copy into your terminal"),
    ("developer", "mcp server oauth", "ok",
     "Build an MCP Server from Scratch",
     ""),
    ("developer", "reduce token usage", "bad",
     "A Guide to Claude Code 2.0",
     "eight results, second is a designer's Figma article matched on cheaper; the "
     "catalogue's own page on how context affects cost never appears"),
    ("developer", "claude.md", "ok",
     "Best practices for Claude Code",
     ""),
    ("developer", "claude code permissions", "bad",
     "Claude Code Essentials",
     "third result is Using Databricks for Data Analysis"),
    # The top result here is right. The agent's objection was position 3 - Getting
    # Started with Claude for Financial Services, inside a three-way score tie - which
    # is the no-tie-break finding, recorded in 05-developer.md, not a wrong #1.
    ("developer", "how much does claude code cost", "ok",
     "Plans",
     ""),

    # --- working with data ------------------------------------------------------
    ("data-analyst", "claude excel formulas", "bad",
     "15 Claude Tips for Everyday Data Analysis",
     "a paywalled video outranks the free official Excel doc, and the word formulas "
     "contributes nothing - the item that writes formulas is sixth"),
    ("data-analyst", "can claude read my csv", "bad",
     "Upload files to Claude",
     "second is about Claude in Chrome reading Amplitude and Stripe; third is a page "
     "the site itself calls useless as a guide to doing it today; the CSV article is "
     "sixth, behind a Figma MCP setup guide"),
    ("data-analyst", "sql", "bad",
     "Anthropic's Prompt Engineering Interactive Tutorial",
     "a generic prompting tutorial and a PM course beat Postgres MCP Pro and the "
     "DuckDB MCP server for the query sql"),
    ("data-analyst", "pivot table", "bad",
     "Claude Code for Data Analysis",
     "there is nothing here on pivot tables; instead of the honest empty state it "
     "returns three items, one of them a skill for making Claude stop writing like "
     "an AI"),
    ("data-analyst", "stop claude making up numbers", "bad",
     "Claude for Education Is Made for Learning",
     "a marketing page about education, first, for a question about wrong numbers; "
     "Reduce hallucinations is second"),

    # --- a product manager ------------------------------------------------------
    ("pm", "write a prd with ai", "ok",
     "Write a PRD with Claude Code",
     ""),
    ("pm", "claude for user research", "ok",
     "Claude Code for product managers",
     ""),
    ("pm", "roadmap prioritisation", "bad",
     "Claude Code for Product Managers",
     "nothing about prioritisation; the top hit is paywalled at the roadmap section "
     "by its own Skip if, and two of three want a credit card"),
    ("pm", "competitor analysis", "bad",
     "Getting started with research in Claude.ai",
     "a generic research video for a competitor query; second is tagged for product "
     "marketing and sales enablement; third is a paid course the site says has a "
     "weak quality signal"),
    ("pm", "stakeholder update", "bad",
     "Product Management Plugin",
     "a journalism ethics code and a buy-side equity-analyst workflow in the top "
     "three, both matched on the word update"),
    ("pm", "prioritisation", "bad",
     "Lenny's Product Skills for Claude Code",
     "one result, not about prioritisation - and the American spelling returns a "
     "different single result, also not about prioritisation"),
    ("pm", "prioritization", "bad",
     "Work through grant options in chat",
     "one result: Work through grant options in chat, for grant administrators"),

    # --- a designer -------------------------------------------------------------
    ("designer", "claude for figma", "ok",
     "Figma",
     ""),
    ("designer", "will ai design replace me", "bad",
     "How to Use Claude Code for UX Writing",
     "the highest-intent query a designer types, answered with a CSV tutorial second; "
     "AI Can't Replace Real Research in Empathy Mapping is 32nd of 47"),
    ("designer", "design system", "ok",
     "design system",
     ""),
    ("designer", "accessibility", "ok",
     "Design plugin",
     ""),
    ("designer", "design critique", "ok",
     "Design plugin",
     ""),
    ("designer", "typography", "bad",
     "",
     "zero results on a design directory, and the empty state advises Try fewer "
     "words to someone who typed one word"),
    ("designer", "stop claude inventing pixel values", "bad",
     "3 Mind Blowing Claude",
     "the card containing the literal phrase invented pixel values is not in the top "
     "three, because skip_if and who_for are not in the index"),

    # --- running a business -----------------------------------------------------
    ("business-founder", "how much does claude cost", "ok",
     "Plans",
     ""),
    ("business-founder", "claude for invoices", "ok",
     "Organize your business finances",
     ""),
    ("business-founder", "is my data safe", "ok",
     "Is my data used for model training",
     ""),
    ("business-founder", "write customer emails", "bad",
     "Real-World AI for Everyone",
     "the top hit costs money and nobody watched it; the second is a teachers' guide"),
    ("business-founder", "claude for bookkeeping", "bad",
     "Anthropic Just Dropped Claude for Small Businesses",
     "the right answer is second, under a hype headline"),
    ("business-founder", "keep my own voice", "bad",
     "Using AI for Writing Feedback",
     "top result is a Found only card, flagged over a year old, aimed at a student, "
     "on a card that tells you to go find a human instead"),

    # --- a writer ---------------------------------------------------------------
    ("writer-marketer", "make my writing not sound like ai", "ok",
     "How to Stop Claude Writing Like an AI",
     ""),
    # Unfiltered this returns the Education Report first; the agent saw Warwick first
    # because it was browsing with role=writer-marketer applied. Same finding either
    # way - a freelance writer with a client gets academic-integrity pages.
    ("writer-marketer", "do i have to say i used ai", "bad",
     "Anthropic Education Report",
     "three academic-integrity pages for a freelance writer with a client; The "
     "Ethics of Using AI, step 4 of this reader's own path, is not surfaced"),
    ("writer-marketer", "em dash", "bad",
     "",
     "zero results, on a site stocking four resources about AI writing tells - and "
     "the empty state says Try fewer words to someone who typed two"),
    ("writer-marketer", "ghostwriting for clients disclosure", "bad",
     "IEEE",
     "two of the top four are Claude Code skill-authoring docs, because clients in "
     "the index means MCP clients"),
]


def words(s):
    """Raw words. The stem expansion happens in rank(), at half weight. See stem.py."""
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 1]


def rank(query, kw):
    n = len(kw["ids"])
    scores = [0.0] * n
    exact = [False] * n
    cover = [0] * n          # how many distinct query words this item matched outright
    q = query.lower()

    for w in words(query):
        posts = kw["words"].get(w)
        if posts:
            idf = math.log(n / len(posts))
            if idf >= MIN_IDF_SCORE:
                for i, weight in posts:
                    scores[i] += weight * idf
                    cover[i] += 1
                    if idf > MIN_IDF_ADMIT:
                        exact[i] = True
        # The stem expansion, replacing the 5-char prefix bonus whose own comment called
        # it a stand-in. Ranks, never admits: a morphological cousin may lift a resource
        # the reader's own word already found, and may not put one in front of them on
        # its own.
        # One union across the whole stem group, scored once. Per-cousin IDF would pay a
        # rare inflection ("hallucinated", in two items) far more than the family is
        # worth, and the group is what the reader actually meant.
        union = {}
        for cousin in kw.get("stems", {}).get(stem(w), []):
            for i, weight in kw["words"].get(cousin, []):
                if weight > union.get(i, 0):
                    union[i] = weight
        if union:
            idf2 = math.log(n / len(union))
            if idf2 >= MIN_IDF_SCORE:
                for i, weight in union.items():
                    scores[i] += weight * idf2 * STEM_WEIGHT

    for phrase, ids in kw["phrases"].items():
        if phrase in q:
            for i in ids:
                scores[i] += 6
                exact[i] = True

    best = max(scores) if scores else 0
    if not best:
        return []
    floor = max(best * FLOOR_FRACTION, FLOOR_ABSOLUTE)
    keep = [i for i in range(n) if exact[i] and scores[i] >= floor]
    # Scores are floats built by addition, so "equal" means equal to a tolerance rather
    # than bit-identical. Everything inside TIE of each other is ordered by the
    # precomputed tie-break: tier, then how recently checked, then title.
    tb = kw.get("tiebreak") or list(range(n))
    keep.sort(key=lambda i: (-round(scores[i] / TIE), -cover[i], tb[i]))
    return [(kw["ids"][i], scores[i]) for i in keep]


def load():
    items = json.load(open(ITEMS, encoding="utf-8"))
    kw = json.load(open(KW, encoding="utf-8"))
    by_id = {x["id"]: x for x in items}
    stale = [i for i in kw["ids"] if i not in by_id]
    if stale:
        sys.exit("Index is stale: %d indexed ids are not in items.json. "
                 "Run scripts/build-search-index.py" % len(stale))
    return by_id, kw


def adhoc(queries):
    by_id, kw = load()
    for q in queries:
        hits = rank(q, kw)
        print('\n"%s"   %d result(s)' % (q, len(hits)))
        if not hits:
            print("   nothing - this is a gap in the hidden keywords")
        for iid, s in hits[:3]:
            x = by_id[iid]
            print("   %6.1f  [%-22s] %s" % (s, ",".join(x["roles"][:2]), x["title"][:56]))
    return 0


def main():
    args = [a for a in sys.argv[1:] if a != "--strict"]
    strict = "--strict" in sys.argv
    if args:
        return adhoc(args)

    by_id, kw = load()
    fails, changed, xpass = [], [], []
    ok_n = bad_n = 0

    for role, q, verdict, frag, why in SUITE:
        hits = rank(q, kw)
        top = by_id[hits[0][0]]["title"] if hits else ""
        matched = bool(frag) and frag.lower() in top.lower()

        if verdict == "ok":
            ok_n += 1
            if matched:
                print("  ok    %-16s %-42s -> %s" % (role, q[:42], top[:44]))
            else:
                fails.append((role, q, frag, top, len(hits)))
                print("  FAIL  %-16s %-42s -> %s" % (role, q[:42], top[:44] or "(0 results)"))
        else:
            bad_n += 1
            # A known-bad row: frag is what it returned on 2026-09-05, "" for none.
            still = (matched if frag else not hits)
            if still:
                print("  bad   %-16s %-42s -> %s" % (role, q[:42], top[:44] or "(0 results)"))
            elif hits:
                changed.append((role, q, frag, top))
                print("  MOVED %-16s %-42s -> %s" % (role, q[:42], top[:44]))
            else:
                changed.append((role, q, frag, "(0 results)"))
                print("  MOVED %-16s %-42s -> (0 results)" % (role, q[:42]))

    print()
    print("%d queries: %d recorded good, %d recorded bad." % (len(SUITE), ok_n, bad_n))

    if fails:
        print()
        print("REGRESSION - a query that used to return the right result no longer does:")
        for role, q, frag, top, n in fails:
            print('  "%s" (%s)' % (q, role))
            print("      expected #1 to contain %r" % frag)
            print("      got %r (%d result(s))" % (top or "nothing", n))

    if changed:
        print()
        print("MOVED - a known-bad query no longer returns what it returned on 2026-09-05.")
        print("Re-judge it: if it is right now, change its verdict to \"ok\" and put the")
        print("new title in. If it is still wrong, update the recorded title and the reason.")
        for role, q, frag, top in changed:
            print('  "%s" (%s): %r -> %r' % (q, role, frag or "nothing", top))

    if fails:
        return 1
    if changed and strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
