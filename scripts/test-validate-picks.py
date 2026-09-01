#!/usr/bin/env python3
"""
Prove that scripts/validate-picks.py actually bites.

Same contract as test-validate-catalogue.py: take the real files, break one thing at a
time in a temporary directory, and check the validator says no for the right reason.
The real data/ files are never written to. A validator nobody has seen fail is not a
validator — that lesson is now written in three places in this repository, which is one
more than it should have needed.

    python3 scripts/test-validate-picks.py
"""

import copy
import json
import os
import shutil
import subprocess
import sys
import tempfile

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VALIDATOR = os.path.join(ROOT, "scripts", "validate-picks.py")
ITEMS = os.path.join(ROOT, "data", "items.json")
PICKS = os.path.join(ROOT, "data", "picks.json")


def run(items, picks, tmp):
    ip = os.path.join(tmp, "items.json")
    pp = os.path.join(tmp, "picks.json")
    json.dump(items, open(ip, "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(picks, open(pp, "w", encoding="utf-8"), ensure_ascii=False)
    r = subprocess.run([sys.executable, VALIDATOR, ip, pp],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def first_cell(picks):
    return next(iter(sorted(picks["cells"])))


def cell_pick_item(items, picks, which=0):
    """The catalogue row behind pick `which` of the first cell."""
    cell = picks["cells"][first_cell(picks)]
    url = cell["picks"][which]["url"]
    return next(x for x in items if x["url"] == url)


# (name, break_it(items, picks), phrase-or-None). None = must still pass (exit 0).
CASES = [
    ("a picked resource goes dead",
     lambda i, p: cell_pick_item(i, p).update({"status": "dead"}),
     "must never ship"),

    ("a picked resource vanishes from the catalogue",
     lambda i, p: i.remove(cell_pick_item(i, p)),
     "not in the catalogue"),

    # The tier rule is the one that makes the pre-filter non-negotiable: `listed` means
    # nobody looked at the content, and the model must not be able to keep recommending
    # something that has been demoted since it chose.
    ("a picked resource is demoted to listed",
     lambda i, p: cell_pick_item(i, p).update({"tier": "listed"}),
     "no longer passes the pre-filter"),

    ("picked_by claims something other than ai",
     lambda i, p: p["cells"][first_cell(p)].update({"picked_by": "morteza"}),
     "only authorised value"),

    ("the fingerprint is deleted",
     lambda i, p: p["cells"][first_cell(p)].pop("fingerprint"),
     "staleness cannot be detected"),

    ("a pick loses its reason sentence",
     lambda i, p: p["cells"][first_cell(p)]["picks"][0].update({"reason": "good"}),
     "no working reason"),

    ("the runners-up record is emptied",
     lambda i, p: p["cells"][first_cell(p)].update({"runners_up": []}),
     "record of what lost"),

    # Constraint 1. Rewrite every pick's publisher to one name — three from one
    # publisher is never legal, whatever the pool looks like.
    ("three picks from one publisher",
     lambda i, p: [cell_pick_item(i, p, n).update({"source": "One Pub"})
                   for n in range(len(p["cells"][first_cell(p)]["picks"]))],
     "allows"),

    # Constraint 4's escape hatch must be a hatch, not a hole: a shared primary topic
    # with the justification stripped is a fault.
    ("a topic clash with its justification stripped",
     lambda i, p: (
         [cell_pick_item(i, p, n).update({"topics": ["agents"]})
          for n in range(2)],
         p["cells"][first_cell(p)].pop("note", None)),
     "no justification"),

    # Ruling 2026-08-31: a constraint may reject a set, never pull an item into one.
    # A cell that ships two must say which of the two causes put it there - the
    # catalogue's shape, or its own shortlist. "Only two" with no cause says nothing.
    ("two picks with no declared cause",
     lambda i, p: p["cells"]["pm|builder"].pop("two_pick_cause"),
     "no two_pick_cause"),

    ("two picks with the wrong cause for the pool",
     lambda i, p: p["cells"]["pm|builder"].update(
         {"two_pick_cause": "publisher-thin"}),
     "which means"),

    ("a cause invented outside the vocabulary",
     lambda i, p: p["cells"]["pm|builder"].update({"two_pick_cause": "felt right"}),
     "must be one of"),

    ("a three-pick cell claiming a two-pick cause",
     lambda i, p: p["cells"]["designer|basic"].update(
         {"two_pick_cause": "publisher-thin"}),
     "where it means nothing"),

    # The stale half must NOT fail the build: shrink the first cell's pool by retiering
    # a non-picked candidate. Warned, dated, shipped.
    ("pool drift is a warning, not an error",
     lambda i, p: _drift(i, p),
     None),
]


def _drift(items, picks):
    """Demote one eligible-but-unpicked candidate so the pool fingerprint moves."""
    cell = picks["cells"][first_cell(picks)]
    role, level = cell["role"], cell["level"]
    picked = {q["url"] for q in cell["picks"]}
    for x in items:
        if (role in (x.get("roles") or []) and x.get("level") == level
                and x.get("status") == "live" and x.get("tier") != "listed"
                and x["url"] not in picked):
            x["tier"] = "listed"
            return
    raise AssertionError("no unpicked candidate to demote — pick a bigger first cell")


def main():
    good_items = json.load(open(ITEMS, encoding="utf-8"))
    good_picks = json.load(open(PICKS, encoding="utf-8"))

    tmp = tempfile.mkdtemp(prefix="lc-picks-")
    failures = []
    try:
        code, out = run(good_items, good_picks, tmp)
        if code != 0:
            failures.append("the untouched picks were rejected:\n" + out)
            print("FAIL  untouched picks")
        else:
            print("ok    untouched picks pass")

        for name, break_it, phrase in CASES:
            items = copy.deepcopy(good_items)
            picks = copy.deepcopy(good_picks)
            break_it(items, picks)
            code, out = run(items, picks, tmp)

            if phrase is None:
                if code == 0 and "stale" in out:
                    print("ok    %s" % name)
                elif code == 0:
                    print("FAIL  %s — passed but never said stale" % name)
                    failures.append(name + ": no stale warning\n" + out)
                else:
                    print("FAIL  %s — rejected but should have shipped" % name)
                    failures.append(name + ":\n" + out)
                continue

            if code == 0:
                print("FAIL  %s — validator said the picks were fine" % name)
                failures.append(name + ": not caught")
            elif phrase not in out:
                print("FAIL  %s — failed for the wrong reason" % name)
                failures.append("%s: wanted %r, got:\n%s" % (name, phrase, out))
            else:
                print("ok    %s" % name)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    if failures:
        print("%d of %d checks did not do their job:" % (len(failures), len(CASES) + 1))
        for f in failures:
            print("  - " + f)
        return 1
    print("All %d checks caught their fault. data/ was not touched." % (len(CASES) + 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
