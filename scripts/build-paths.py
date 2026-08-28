#!/usr/bin/env python3
"""
Build the ordered paths.

A path is the answer to the question nobody else answers: "where do I start, and in
what order?" Search finds you one thing. A path hands you a route.

Every step here was chosen by hand from data/items.json and carries a `why` — the
reason it sits at that position rather than another. If a step has no reason to be
where it is, it does not belong in the path.

Steps are referenced **by URL**, never by id. An id is a machine detail that can be
regenerated; the URL is what a person can verify by opening it. An earlier version of
this file referenced ids that were assigned by list position, and when the catalogue
grew every path silently re-pointed at different resources while still printing
confident `why` text. Referencing the URL makes that failure impossible.

Rules kept:
- Every URL referenced must exist in items.json. The script fails loudly if not.
- No path mixes paid and free without saying so; the total cost is computed, not claimed.
- Total time is computed from the real `time` field, not guessed.
- A path only ships if every step is at least `previewed`. We do not sequence things
  nobody has looked at. This is enforced, not just documented.

Writes:
    data/paths.json          the paths themselves
    data/items.json          each item gains `paths`: [{path, step}] so a card can say
                             "Step 2 of 6 in Your first week with Claude"
"""

import json
import sys

ITEMS = "data/items.json"
OUT = "data/paths.json"

MINUTES = {"under-15min": 12, "under-1hr": 45, "half-day": 210, "multi-day": 600}

PATHS = [
    {
        "id": "first-week",
        "title": "Your first week with Claude",
        "for": "Anyone who has just opened Claude and does not know what to do next.",
        "roles": ["non-technical", "student", "teacher", "business-founder"],
        "level": "never-used",
        "intro": "Six short steps. Nothing here takes more than an hour, and you can "
                 "stop after step 3 and still be better off than most people.",
        "steps": [
            {"url": "https://ruben.substack.com/p/claude",
             "why": "Start here because most confusion is not about prompting — it is not "
             "knowing that Claude is several different products. Five minutes now saves a "
             "week of looking in the wrong place."},
            {"url": "https://support.claude.com/en/articles/8114491-get-started-with-claude",
             "why": "Now open the thing itself and do one real task. Reading about it any "
             "longer is procrastination."},
            {"url": "https://anthropic.skilljar.com/claude-101",
             "why": "By now you have had a generic, disappointing answer. Anthropic's own "
             "beginner course is the fix, and it is the single highest-value hour here."},
            {"url": "https://support.claude.com/en/articles/9517075-what-are-projects",
             "why": "Once you repeat a task twice, you need somewhere to keep the context. "
             "Projects is that place. Learning this earlier would have been abstract."},
            {"url": "https://claude.com/resources/tutorials/why-do-ai-models-hallucinate",
             "why": "Before you trust Claude with anything that matters, understand exactly "
             "how it fails. This is the step people skip and later regret."},
            {"url": "https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork",
             "why": "Last, because working on your own files only makes sense once you "
             "trust the answers. Read it before you point Claude at anything real."},
        ],
    },
    {
        "id": "claude-code-start",
        "title": "Getting good at Claude Code",
        "for": "Developers who have installed Claude Code and are getting mediocre results.",
        "roles": ["developer"],
        "level": "basic",
        "intro": "The gap between installing Claude Code and being fast with it is "
                 "configuration and habits, not model quality. Six steps, roughly a day "
                 "of reading spread over a week of practice.",
        "steps": [
            # academy.claude.com, not anthropic.skilljar.com. The two rows were the same course
            # harvested from both hosts; the skilljar one was merged away on 2026-08-27
            # because the catalogue's own note said that host is the old one and
            # redirects. This list is where a path really lives, so it has to change here.
            {"url": "https://academy.claude.com/courses/claude-code-101",
             "why": "Anthropic's own course. Do this before reading anyone's tips, so you "
             "know which behaviours are the tool and which are the person writing about it."},
            {"url": "https://code.claude.com/docs/en/best-practices",
             "why": "The best-practices page. Densest thing written about Claude Code, and "
             "everything after this assumes you have read it."},
            {"url": "https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models",
             "why": "Read this third and not later, because it invalidates a lot of "
             "2025-era advice you will otherwise absorb."},
            {"url": "https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions",
             "why": "Now that your setup is right, this is where the speed comes from — "
             "knowing which commands quietly destroy your prompt cache mid-session."},
            {"url": "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents",
             "why": "Context engineering is the skill that separates people who get good "
             "output from people who get plausible output. It only makes sense once you "
             "have felt a long session degrade."},
            {"url": "https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code",
             "why": "Last, because orchestration is worth nothing until single sessions "
             "are reliable. Names the failure modes you will have hit by now."},
        ],
    },
    {
        "id": "writing-you-sign",
        "title": "Using Claude on work you put your name to",
        "for": "Writers and marketers whose byline goes on it, and who would rather not "
               "explain themselves later.",
        "roles": ["writer-marketer"],
        "level": "basic",
        "intro": "Five steps, all free, about two hours. The order runs from what job "
                 "Claude has, through the tells everyone else is trained to spot, to "
                 "what you owe the reader. The last step is the one people skip and it "
                 "is the one with consequences.",
        "steps": [
            {"url": "https://restructurednews.substack.com/p/claude-editor",
             "why": "First, decide what job it has. This is a writer using Claude as an "
             "editor rather than a ghostwriter, and settling that question now is what "
             "makes every later step a craft problem instead of an ethics problem."},
            {"url": "https://kenny-kane.com/blog/claude-ai-for-writing",
             "why": "Now the craft, at length, with that relationship already fixed. Read "
             "this second and it reads as technique; read it first and it reads as "
             "permission to hand over the keyboard."},
            {"url": "https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing",
             "why": "Third, learn the symptoms before trying to treat them. Wikipedia's "
             "editors have catalogued what AI prose actually looks like, and you cannot "
             "prompt your way out of a tell you cannot name."},
            {"url": "https://willfrancis.com/how-to-stop-claude-writing-like-an-ai/",
             "why": "Only now is this useful. It is the treatment for the symptoms in step "
             "3 — read in the other order it is a list of fixes for problems you have not "
             "learned to see yet."},
            {"url": "https://ethicscentral.org/the-ethics-of-using-ai/",
             "why": "Last, and last on purpose: everything above makes the work harder to "
             "detect, which is exactly why disclosure has to be the step you finish on. "
             "Craft is what you owe the page. This is what you owe the reader."},
        ],
    },
    {
        "id": "pm-without-engineering",
        "title": "Product work without waiting for engineering",
        "for": "Product managers who have the question, the users and the context, and "
               "keep having to queue for someone else's sprint.",
        "roles": ["pm"],
        "level": "basic",
        "intro": "Five steps, all free, about two hours. Steps 1 to 4 need nothing but a "
                 "browser — stop after step 4 and you can already synthesise research, "
                 "keep it somewhere, delegate the repeatable parts and know what is safe "
                 "to paste in. Step 5 needs a terminal, and it is fair to decide that is "
                 "not your job.",
        "steps": [
            {"url": "https://www.enterpret.com/guides/claude-for-product-managers-synthesizing-user-research",
             "why": "Start with the work only you do. Synthesising research is where "
             "Claude pays for itself fastest and it needs no setup at all — a chat window "
             "and the interviews you already have."},
            {"url": "https://www.youtube.com/watch?v=GJ5jTgcbRHA",
             "why": "Second, because one good synthesis is a party trick and a repeatable "
             "one is a habit. Projects is where a product area stops being forty loose "
             "chats you cannot find again."},
            {"url": "https://haverin.substack.com/p/claude-cowork-for-product-managers",
             "why": "Third: hand over the parts that repeat. This comes after Projects "
             "because delegation without somewhere to put the output just moves the mess."},
            {"url": "https://support.claude.com/en/articles/13364135-use-claude-cowork-safely",
             "why": "Fourth, and deliberately not first. Safety guidance is abstract until "
             "you know what you would actually delegate — which step 3 just taught you. "
             "Read it before the first time you point Cowork at real customer data."},
            {"url": "https://www.productcompass.pm/p/claude-code-beginners-guide",
             "why": "This step needs a terminal, and if that is a no then stop here — the "
             "four above stand on their own. It is last because it is the only one that "
             "asks you to change how you work rather than what you work on, and because "
             "the PM shelf leans heavily on Claude Code; this is the gentlest way in."},
        ],
    },
    {
        "id": "research-with-claude",
        "title": "Using Claude for research without embarrassing yourself",
        "for": "Researchers and academics who want the speed without the retraction.",
        "roles": ["researcher", "student"],
        "level": "basic",
        "intro": "The order matters more here than anywhere else. The failure modes are "
                 "specific and the consequences are public.",
        "steps": [
            {"url": "https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations",
             "why": "Start with the failure, not the feature. Fabricated citations are the "
             "one mistake that ends careers, and this is the clearest account of when they "
             "happen and how to cut them."},
            {"url": "https://support.claude.com/en/articles/9517075-what-are-projects",
             "why": "Projects is where a literature review actually lives. Set it up "
             "before you have forty loose chats."},
            {"url": "https://muse.jhu.edu/article/961199",
             "why": "Now read someone who actually tried it and reported what broke, with "
             "the guard rails from step 1 in place."},
            {"url": "https://effortlessacademic.com/connect-and-integrate-your-local-zotero-library-with-claude-cowork/",
             "why": "Connect your own library. Until Claude can see your actual sources, "
             "everything above is a demo."},
            {"url": "https://www.icmje.org/recommendations/browse/artificial-intelligence/",
             "why": "Before you submit anything, read what the ICMJE expects you to "
             "declare. This is not optional and most people learn it too late."},
        ],
    },
    {
        "id": "numbers-you-can-defend",
        "title": "Analysing your own data without getting the numbers wrong",
        "for": "Analysts with a spreadsheet, a deadline, and somebody who will ask where "
               "the number came from.",
        "roles": ["data-analyst"],
        "level": "never-used",
        "intro": "Five steps, all free, about two hours. The arc is your data rather "
                 "than Claude: get it in front of the model, know what happens to it, "
                 "then learn the difference between Claude reading your numbers and "
                 "Claude actually running them. Only the last step needs a terminal, and "
                 "you can stop before it.",
        "steps": [
            {"url": "https://support.claude.com/en/articles/8241126-upload-files-to-claude",
             "why": "Nothing below works until your data is in front of Claude, and every "
             "other guide in this catalogue assumes you did this already. It is also the "
             "only step that tells you what will be refused — the size ceilings differ "
             "between a chat and a Project — before you find out the slow way."},
            {"url": "https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data",
             "why": "Second, and second on purpose. The writing path puts disclosure last "
             "because a writer discloses at publication, after the craft. An analyst "
             "decides at upload, before anything: once somebody else's data is pasted, "
             "reading the retention terms afterwards changes nothing. Anthropic's own "
             "numbers, and narrow ones — consumer plans only, and the page never once "
             "says the word attachment."},
            {"url": "https://anthropic.com/news/analysis-tool",
             "why": "Now the idea the rest of the path rests on: Claude can run real code "
             "against your file instead of reasoning about the numbers in prose. Here for "
             "the concept and not the click-path — it predates Excel and Cowork and its "
             "screens have moved."},
            {"url": "https://www.qwe.edu.pl/tutorial/claude-csv-data-analysis/",
             "why": "Fourth, because step 3 is only half of it: Claude has that "
             "code-running mode and does not always reach for it. This is where a "
             "capability becomes a habit, and it is the step that explains every total "
             "that has ever come back confidently wrong."},
            {"url": "https://ccforeveryone.com/guides/claude-code-for-data-analysts",
             "why": "This one needs a terminal, so stop here if that is not your working "
             "day — the four steps above stand on their own and an analyst who lives in "
             "Excel has already got the whole point. If it is, this is where checking "
             "becomes reproducible: rerunnable scripts over silent cell edits, argued "
             "from Panko's finding that 94% of spreadsheets already contain errors."},
        ],
    },
]


# Imported, not reimplemented. The version that used to live here was
#     url.rstrip("/").split("?")[0].lower()
# which throws the query string away — and a YouTube video's identity is its ?v=. Every
# one of the 71 youtube.com/watch resources in the catalogue collapsed to a single key,
# so a path step given a video URL silently resolved to whichever video happened to be
# last in items.json. The three original paths never referenced a video, so nothing
# caught it until one did: step 2 of the product-manager path asked for "Getting started
# with projects in Claude.ai" and was handed "Master Claude for Excel in 10 Minutes".
#
# This is the same fault the README warns about for ids, in a second place nobody had
# looked. stable-ids.py already normalises correctly — it keeps the query and drops only
# tracking parameters — so use that one and stop maintaining two answers to one question.
def _load_norm():
    import importlib.util, os
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stable-ids.py")
    spec = importlib.util.spec_from_file_location("stable_ids", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.norm


norm = _load_norm()


def main():
    items = json.load(open(ITEMS, encoding="utf-8"))
    missing_id = [x for x in items if not x.get("id")]
    if missing_id:
        sys.exit(f"{len(missing_id)} items have no id. Run scripts/stable-ids.py first.")
    by_id = {x["id"]: x for x in items}
    by_url = {norm(x["url"]): x for x in items}

    RANK = {"reviewed": 3, "ai-reviewed": 2, "previewed": 1, "listed": 0}
    MIN_TIER = 1        # previewed. Below this we have not looked at the content.
    out = []
    problems = []

    for p in PATHS:
        steps = []
        minutes = 0
        costs = set()
        weakest = 3
        too_thin = []
        for n, s in enumerate(p["steps"], 1):
            x = by_url.get(norm(s["url"]))
            if not x:
                problems.append(f"{p['id']} step {n}: no resource with url {s['url']}")
                continue
            if RANK[x["tier"]] < MIN_TIER:
                too_thin.append(f"step {n} is '{x['tier']}' — {x['title'][:50]}")
            minutes += MINUTES.get(x["time"], 45)
            costs.add(x["cost"])
            weakest = min(weakest, RANK[x["tier"]])
            steps.append({
                "step": n,
                "item": x["id"],
                "title": x["title"],
                "url": x["url"],
                "time": x["time"],
                "cost": x["cost"],
                "tier": x["tier"],
                "why": s["why"],
            })
        if len(steps) < 3:
            problems.append(f"{p['id']}: only {len(steps)} steps — too short to publish")
            continue

        # The rule this file has always claimed, now actually enforced. Sequencing a
        # resource nobody has opened is exactly the thing the site exists to not do.
        if too_thin:
            problems.append(f"{p['id']}: below '{list(RANK)[::-1][MIN_TIER]}' — "
                            + "; ".join(too_thin))
            continue

        hours = minutes / 60
        out.append({
            "id": p["id"],
            "title": p["title"],
            "for": p["for"],
            "roles": p["roles"],
            "level": p["level"],
            "intro": p["intro"],
            "step_count": len(steps),
            "total_minutes": minutes,
            "total_time_label": (f"about {round(minutes)} minutes" if minutes < 90
                                 else f"about {hours:.0f} hours"),
            "cost": "free" if costs <= {"free", "free-account"} else "some paid steps",
            "weakest_tier": [k for k, v in RANK.items() if v == weakest][0],
            "steps": steps,
        })

    # `paths` on an item is a projection of the paths above, so it has to be rebuilt
    # from nothing every run. It used to be appended to and never cleared, which meant a
    # step removed from a path kept its claim forever: eight cards ended up printing
    # "This is step 1 of 6 in first-week" for paths whose six steps did not include them,
    # and two items carried a stale step count from when a path was three steps long. A
    # field derived from other data must be derived, not accumulated.
    for it in items:
        it.pop("paths", None)

    for p in out:
        for s in p["steps"]:
            entry = {"path": p["id"], "step": s["step"], "of": p["step_count"]}
            by_id[s["item"]].setdefault("paths", []).append(entry)

    json.dump(out, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    json.dump(items, open(ITEMS, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    for p in out:
        print(f"{p['title']}")
        print(f"   {p['step_count']} steps · {p['total_time_label']} · {p['cost']} "
              f"· weakest step is '{p['weakest_tier']}'")
        for s in p["steps"]:
            print(f"     {s['step']}. [{s['time']:11}] {s['title'][:56]}")
    if problems:
        print("\nNOT PUBLISHED:")
        for m in problems:
            print("   " + m)
    print(f"\n{len(out)} path(s) -> {OUT}")


if __name__ == "__main__":
    main()
