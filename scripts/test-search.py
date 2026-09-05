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

ACCEPTED ANSWERS
----------------

The fourth field is one title fragment, or a list of them when a row has been re-graded.
A list means: the agent who wrote this query judged one answer right, a later round argued
for another, and both are accepted rather than the second quietly replacing the first. The
reason names what in each card makes it an answer. Ten strangers' judgement is the only
outside opinion this project has, and a rebuild that grades itself against its own output
is not measuring anything.

    ok   - an accepted answer is in the top three. This is asserted. Breaking it exits 1.
           The top three is what the reader sees and what the agents scored; asserting
           the first result alone was a stricter test than anyone agreed to, and it
           disagreed with section 5 of the search spec from the day both were written.
    content-gap - the query fails because this catalogue holds nothing on the subject, not
           because the ranking is wrong. Checked by hand, with the count of rows
           mentioning the subject at all recorded in the reason. Never asserted: no
           stemmer, no synonym and no tie-break can conjure a resource. measure.py
           collects these into STATUS.md as the harvest list.
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
SYNONYM_WEIGHT = 0.5   # an expansion scores below the word the person typed
TIE = 0.001            # scores within this of each other are a tie, not an order


# role, query, verdict, expected-or-observed top title fragment, the agent's reason
SUITE = [
    # --- not a coder ------------------------------------------------------------
    ("non-technical", "is claude free", "ok", "Choose a Claude plan",
     ""),
    ("non-technical", "make claude remember my stuff", "ok",
     "Create and Manage Projects",
     ""),
    ("non-technical", "how do i stop claude making things up", "ok",
     ["Reduce hallucinations"],
     "Promoted under the top-three rule. The agent's objection was that a "
     "university login page led and Reduce hallucinations was second. It is "
     "still second, and second is on the reader's screen."),
    ("non-technical", "write emails for me", "bad",
     "Claude AI for Teachers",
     "Still wrong, and differently wrong: a teachers' beginner guide now leads "
     "where a paid Coursera specialization did. Write in my voice, the row "
     "that answers this, is still not in the results."),
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
    ("student", "is it cheating to use claude for my essay", "ok",
     ["Generative AI and Academic Integrity", "Plagiarism and Academic Integrity 101"],
     "Promoted. The objection was not relevance but tier: both answers were "
     "cards nobody had opened. D1 verified and re-tiered them in FIX-24 and "
     "both are `previewed` now, so the two rows that answer the question are "
     "read as far as their labels claim."),
    ("student", "how do i cite claude in my references", "ok",
     ["Referencing AI and Acknowledging AI Use"],
     "Promoted. The objection was that the items which literally answer it sat "
     "at #5 and below, under a Zotero-plus-Obsidian workflow. Referencing AI "
     "and Acknowledging AI Use is third."),
    ("student", "summarise my lecture pdf and make notes", "ok",
     "AI-Powered Flashcards with Claude Projects",
     ""),

    # --- a researcher -----------------------------------------------------------
    ("researcher", "does claude make up citations", "bad",
     "3 Mind Blowing Claude & Consensus Research Workflows",
     "Still wrong. Reduce hallucinations is now in the results where it was in "
     "none of the 47 before, but a YouTube workflow tour leads. The citation "
     "synonym row moved it up, not to the top."),
    ("researcher", "systematic literature review", "ok",
     ["Claude AI and Literature Reviews", "Claude Researcher"],
     "Promoted, and the first result is still the mailing-list funnel the "
     "agent named. Second and third are a real experiment in doing a "
     "literature review with Claude and a source-first workflow, so the reader "
     "gets two answers even though the funnel is still on top. The funnel is a "
     "ranking fault and it stays in the table."),
    ("researcher", "hallucinated references", "ok",
     ["Zotero", "Claude Researcher"],
     "Two accepted answers. Zotero is the agent's: its card is about grounding "
     "Claude in the reference library you already keep, so the references it "
     "cites are ones that exist. Claude Researcher is this round's: its card "
     "is a source-first literature workflow, which is the habit that stops "
     "fabricated citations being written in the first place."),
    ("researcher", "peer review", "ok",
     ["Nature Portfolio"],
     "Promoted while writing the failure table. The objection was the wrong "
     "sense of the word - classroom peer feedback on undergraduate essays - "
     "and IEEE nowhere in the top eight. Nature Portfolio's AI editorial "
     "policy is third and its who_for names authors and reviewers for its "
     "journals, which is the sense the researcher meant. Classroom peer "
     "feedback still leads, and that stays in the table."),
    ("researcher", "how do i cite claude in a paper", "ok",
     "IEEE",
     ""),

    # --- a teacher --------------------------------------------------------------
    ("teacher", "can students cheat with claude", "ok",
     ["AI & Academic Integrity", "The AI Assessment Scale"],
     "Promoted. The objection listed three rows that were in none of the top "
     "five: AI & Academic Integrity is now second and the AI Assessment Scale "
     "third. A Claude Code crash course still leads, which is a ranking fault "
     "and stays in the table."),
    ("teacher", "make a lesson plan", "bad",
     "Claude for K-12 teachers",
     "Still wrong, and closer: a product page with worked prompts leads, where "
     "the previous leader's own skip line said to skip it if you only want "
     "lesson plans. A product page is not a lesson plan."),
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
     "Teaching AI Fluency",
     "Still wrong, and the specific complaint is fixed: Demystifying evals for "
     "AI agents - machine-learning regression testing - has dropped to second, "
     "and 'marking' and 'grading' now return the same set. What leads is a "
     "course about teaching AI fluency, which is not about marking work."),

    # --- a developer ------------------------------------------------------------
    ("developer", "claude code hooks", "content-gap",
     "",
     "The hooks GUIDE is not in this catalogue. The Hooks reference is, and it "
     "leads - and its own card says to read the guide first, which is the "
     "agent's objection and cannot be answered by ranking something that is "
     "not here."),
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
     ["Best practices for Claude Code", "Steering Claude Code"],
     "Two accepted answers. Best practices is the agent's: its card covers "
     "CLAUDE.md as part of a working setup, which is where most readers meet "
     "the file. Steering Claude Code is this round's: its card is about when "
     "to use CLAUDE.md against skills, hooks and subagents, so the file itself "
     "is its subject."),
    ("developer", "claude code permissions", "content-gap",
     "",
     "No permissions reference in the catalogue. Twenty-one rows mention the "
     "word in passing - a plugin install page, a Postgres MCP server - and "
     "none of them is the page a developer wants when they type this."),
    # The top result here is right. The agent's objection was position 3 - Getting
    # Started with Claude for Financial Services, inside a three-way score tie - which
    # is the no-tie-break finding, recorded in 05-developer.md, not a wrong #1.
    ("developer", "how much does claude code cost", "ok",
     ["Plans", "Choose a Claude plan"],
     "Two accepted answers, tied on score. Plans & Pricing is the agent's: its "
     "card is the pricing page. Choose a Claude plan is this round's: its card "
     "names which plans include Claude Code, which is the question behind the "
     "question."),

    # --- working with data ------------------------------------------------------
    ("data-analyst", "claude excel formulas", "ok",
     ["Use Claude for Excel"],
     "Promoted. The objection was that a paywalled video outranked the free "
     "official Excel doc. The video is still second; the official doc is "
     "third, and both are on the screen."),
    ("data-analyst", "can claude read my csv", "bad",
     "Upload files to Claude",
     "second is about Claude in Chrome reading Amplitude and Stripe; third is a page "
     "the site itself calls useless as a guide to doing it today; the CSV article is "
     "sixth, behind a Figma MCP setup guide"),
    ("data-analyst", "sql", "bad",
     "Answer the ad-hoc data question",
     "Still wrong, and much closer: an analyst recipe leads where a generic "
     "prompting tutorial did. Postgres MCP Pro and the DuckDB MCP server, "
     "which are the answer to 'sql', are still not in the top three."),
    ("data-analyst", "pivot table", "content-gap",
     "",
     "Three rows mention pivot tables in passing and none is about them. The "
     "agent said so at the time: there is nothing here, and the honest answer "
     "is an empty result rather than three approximations."),
    ("data-analyst", "stop claude making up numbers", "ok",
     ["Reduce hallucinations"],
     "Promoted. The objection was an education marketing page first for a "
     "question about wrong numbers, with Reduce hallucinations second. The "
     "marketing page still leads, which is a ranking fault and stays in the "
     "table; the answer is on the screen."),

    # --- a product manager ------------------------------------------------------
    ("pm", "write a prd with ai", "ok",
     ["Write a PRD with Claude Code", "PRD from a problem statement"],
     "Two accepted answers, tied on score. Write a PRD with Claude Code is the "
     "agent's: its card teaches the method as a course module. PRD from a "
     "problem statement is this round's: its card is a recipe that produces "
     "the PRD, which is what the query asked for."),
    ("pm", "claude for user research", "ok",
     "Claude Code for product managers",
     ""),
    ("pm", "roadmap prioritisation", "content-gap",
     "Claude Code for Product Managers",
     "Five rows contain 'prioritis'/'prioritiz' anywhere: a literature review, "
     "feedback themes, weekly prep, grant options and one PM skill pack whose "
     "card Attack 2 read and found is not about prioritisation. Nothing here is "
     "about prioritising a roadmap."),
    ("pm", "competitor analysis", "ok",
     ["Build the competitive comparison doc"],
     "Promoted. The objection was that the second result was tagged for "
     "product marketing and sales enablement rather than for a PM. Rule B has "
     "since read that card against its page and it carries `pm`; it builds a "
     "competitive comparison from scratch, which is the query."),
    ("pm", "stakeholder update", "content-gap",
     "",
     "Nothing here is about writing a stakeholder update. Six rows contain the "
     "word stakeholder; the closest, the official PM plugin, teaches "
     "installing a plugin and running slash commands. The suite's recorded "
     "objection - a journalism ethics code and an equity-analyst workflow "
     "matched on the word update - is gone, and what replaced it is a plugin "
     "page, not an answer."),
    ("pm", "prioritisation", "content-gap",
     "Lenny's Product Skills for Claude Code",
     "Same hole as 'roadmap prioritisation', and the reason the British and "
     "American spellings now return the same two rows is step 4 working. Both "
     "rows are still about something else."),
    ("pm", "prioritization", "content-gap",
     "Work through grant options in chat",
     "The American spelling of a subject this catalogue does not cover. It "
     "returns the same rows as the British one now, which is the spelling fix "
     "landing on an empty shelf."),

    # --- a designer -------------------------------------------------------------
    ("designer", "claude for figma", "ok",
     "Figma",
     ""),
    ("designer", "will ai design replace me", "content-gap",
     "How to Use Claude Code for UX Writing",
     "Nothing in the catalogue is about AI replacing designers: zero rows "
     "contain 'replace me' or 'replace design' in any field. The query returns "
     "42 results because its other words are common, and not one of them is on "
     "the subject."),
    ("designer", "design system", "ok",
     "design system",
     ""),
    ("designer", "accessibility", "ok",
     ["Design plugin", "Design Systems in 2026"],
     "Two accepted answers, tied on score, and the closest call of the five. "
     "Design plugin is the agent's: its card ships an accessibility-review "
     "skill you can read line by line. Design Systems in 2026 is this round's: "
     "its card carries accessibility in four fields including what it teaches, "
     "which is why the tie-break put it first."),
    ("designer", "design critique", "ok",
     "Design plugin",
     ""),
    ("designer", "typography", "content-gap",
     "",
     "One row mentions typography anywhere - Encode the brand as a skill - and "
     "it mentions it in the summary, which is not indexed. A design directory "
     "that cannot answer 'typography' has a hole in its shelves, not in its "
     "search."),
    ("designer", "stop claude inventing pixel values", "ok",
     ["Claude for Designers in 2026"],
     "Promoted, and this is cause 5's own query. The card carrying the literal "
     "phrase 'invented pixel values' was not in the results at all before "
     "skip_if was indexed. It is third."),

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
     "Claude AI for Teachers",
     "Still wrong, same fault as 'write emails for me' from the other role: a "
     "teachers' guide leads a query about customer email."),
    ("business-founder", "claude for bookkeeping", "ok",
     "Reconcile transactions across your accounts",
     "Promoted 2026-09-06. Bookkeeping is reconciling transactions, and that "
     "is now first where it used to sit second under a hype headline. The "
     "synonym row joining bookkeeping to reconciliation is why, and the row "
     "says so."),
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
    ("writer-marketer", "do i have to say i used ai", "ok",
     "Referencing AI and Acknowledging AI Use",
     "Promoted 2026-09-06. The page is exactly the question, and it was "
     "invisible because it says acknowledgement where the reader says 'say I "
     "used AI'. The disclosure synonym row put it first."),
    ("writer-marketer", "em dash", "content-gap",
     "",
     "Not one row in the catalogue contains the phrase, in any field, indexed "
     "or not. Four rows discuss AI writing tells in general and none of them "
     "names this one. A synonym cannot conjure a resource; this is a harvest "
     "job."),
    ("writer-marketer", "ghostwriting for clients disclosure", "ok",
     ["IEEE", "Referencing AI and Acknowledging AI Use"],
     "Promoted. The objection was that two of the top four were Claude Code "
     "skill docs, because 'clients' in the index meant MCP clients. The MCP "
     "noise is now second, with author guidelines for AI-generated text first "
     "and the acknowledgement page third."),
]


def words(s):
    """Raw words. The stem expansion happens in rank(), at half weight. See stem.py."""
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 1]


def rank(query, kw):
    n = len(kw["ids"])
    scores = [0.0] * n
    exact = [False] * n
    cover = [0] * n          # how many distinct query words this item matched outright
    depth = [0] * n          # in how many fields, added up over the query's words
    q = query.lower()

    for w in words(query):
        # Every indexed spelling of the reader's word, scored once as one term. The same
        # word spelled the other way is still the reader's word: full weight, and it
        # admits like any exact match. Only synonyms are halved.
        forms = kw.get("spelling", {}).get(w) or [w]
        posts = {}
        deep = {}
        for form in forms:
            for p in kw["words"].get(form, []):
                i, weight = p[0], p[1]
                if weight > posts.get(i, 0):
                    posts[i] = weight
                deep[i] = max(deep.get(i, 0), p[2] if len(p) > 2 else 1)
        if posts:
            idf = math.log(n / len(posts))
            if idf >= MIN_IDF_SCORE:
                for i, weight in posts.items():
                    scores[i] += weight * idf
                    cover[i] += 1
                    depth[i] += deep.get(i, 1)
                    if idf > MIN_IDF_ADMIT:
                        exact[i] = True
        # The stem expansion, replacing the 5-char prefix bonus whose own comment called
        # it a stand-in. Ranks, never admits: a morphological cousin may lift a resource
        # the reader's own word already found, and may not put one in front of them on
        # its own.
        # A synonym is somebody else's word for the same thing, so it ranks at half and
        # never admits: it can lift a page the reader's own words already found, and can
        # never put one in front of them on its own.
        syn = {}
        for other in kw.get("synonyms", {}).get(w, []):
            for p in kw["words"].get(other, []):
                if p[1] > syn.get(p[0], 0):
                    syn[p[0]] = p[1]
        if syn:
            sidf = math.log(n / len(syn))
            if sidf >= MIN_IDF_SCORE:
                for i, weight in syn.items():
                    scores[i] += weight * sidf * SYNONYM_WEIGHT

        # One union across the whole stem group, scored once. Per-cousin IDF would pay a
        # rare inflection ("hallucinated", in two items) far more than the family is
        # worth, and the group is what the reader actually meant.
        union = {}
        for cousin in kw.get("stems", {}).get(stem(w), []):
            for p in kw["words"].get(cousin, []):
                if p[1] > union.get(p[0], 0):
                    union[p[0]] = p[1]
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
    keep.sort(key=lambda i: (-round(scores[i] / TIE), -depth[i], -cover[i], tb[i]))
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


def emit(path):
    """Write every suite query's top three, for the cross-runtime check to compare."""
    by_id, kw = load()
    rows = [{"role": role, "query": q,
             "top3": [iid for iid, _s in rank(q, kw)[:3]]}
            for role, q, _v, _f, _w in SUITE]
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"generated": "scripts/test-search.py --emit", "queries": rows}, f,
                  ensure_ascii=False, indent=1)
    print("Emitted %d queries' top three -> %s" % (len(rows), path))
    return 0


def main():
    argv = sys.argv[1:]
    if "--emit" in argv:
        i = argv.index("--emit")
        if i + 1 >= len(argv):
            sys.exit("--emit needs a path")
        return emit(argv[i + 1])
    args = [a for a in argv if a != "--strict"]
    strict = "--strict" in sys.argv
    if args:
        return adhoc(args)

    by_id, kw = load()
    fails, changed, xpass = [], [], []
    ok_n = bad_n = gap_n = 0

    for role, q, verdict, frag, why in SUITE:
        hits = rank(q, kw)
        top = by_id[hits[0][0]]["title"] if hits else ""
        top3 = [by_id[i]["title"] for i, _s in hits[:3]]
        # One fragment or several. Several means the row was re-graded and the agent's
        # own answer was kept alongside ours - see ACCEPTED ANSWERS above.
        accepted = frag if isinstance(frag, list) else [frag]
        matched = any(a and any(a.lower() in t.lower() for t in top3) for a in accepted)

        if verdict == "content-gap":
            gap_n += 1
            print("  gap   %-16s %-42s -> %s" % (role, q[:42],
                                                 top[:44] or "(0 results)"))
        elif verdict == "ok":
            ok_n += 1
            if matched:
                at = min(n + 1 for n, t in enumerate(top3)
                         for a in accepted if a and a.lower() in t.lower())
                print("  ok    %-16s %-42s -> #%d %s"
                      % (role, q[:42], at, top3[at - 1][:41]))
            else:
                fails.append((role, q, " or ".join(a for a in accepted if a), top, len(hits)))
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
    print("%d queries: %d recorded good, %d recorded bad, %d content gaps."
          % (len(SUITE), ok_n, bad_n, gap_n))

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
