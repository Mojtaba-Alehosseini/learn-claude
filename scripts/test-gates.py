#!/usr/bin/env python3
"""
The bite test for the thing that runs the bite tests.

    python3 scripts/test-gates.py            # every planted fault must turn the build red
    python3 scripts/test-gates.py --list     # what it plants, without running anything

WHY THIS EXISTS

Every validator in scripts/ has a test that proves it catches its own faults. Not one of
them proved that `build.sh` could see the catch. For an unknown number of rounds it could
not: every gate was piped through `tail`, a pipeline reports the last command's status, and
`tail` never fails. The search suite exited 1 on eight broken queries and the build printed
"Done. Open index.html." The deploy found it, which is the wrong place to find it.

So this plants a fault, runs the whole build, and asserts it goes red. It is deliberately
crude - a copy of the working tree per fault, a real `./build.sh` in it, and the exit
status - because anything cleverer would be testing something other than what runs.

WHAT IT PLANTS

One fault per gate that has a fault worth planting, including the four FIX-31 named: a
dead pick, a `listed` row carrying a verdict, a typed count in a pick's reason, and a
suite query forced to miss. Each names the gate it should trip, and the run fails if the
build goes red at the wrong step - a fault that trips an earlier gate proves nothing about
the one it was aimed at.

The control comes first: an untouched copy must build green. If that fails, nothing below
it means anything.
"""

import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "tmp", "node_modules", "_site", "reference", "scratch-icons",
             "__pycache__"}
SKIP_EXT = {".pdf", ".png", ".jpg", ".jpeg", ".webp", ".mp4", ".woff", ".woff2"}


# --- the faults ------------------------------------------------------------------

def _items(root):
    p = os.path.join(root, "data", "items.json")
    return p, json.load(io.open(p, encoding="utf-8"))


def _write(p, obj):
    io.open(p, "w", encoding="utf-8").write(
        json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def plant_listed_verdict(root):
    """A `listed` row carrying questions. Tier means nobody read it; a verdict says
    somebody did."""
    p, items = _items(root)
    for x in items:
        if x.get("tier") == "listed":
            x["questions"] = ["a verdict on a page nobody opened"]
            _write(p, items)
            return "gave a listed row a verdict: %s" % x["title"][:44]
    raise AssertionError("no listed row to plant in")


def plant_dead_pick(root):
    """A pick pointing at a row marked dead. 'Open this one first' about a page nobody
    can open is the site lying in its own voice."""
    picks = json.load(io.open(os.path.join(root, "data", "picks.json"), encoding="utf-8"))
    url = next(iter(picks["cells"].values()))["picks"][0]["url"]
    p, items = _items(root)
    for x in items:
        if x["url"] == url:
            x["status"] = "dead"
            _write(p, items)
            return "killed a picked row: %s" % x["title"][:44]
    raise AssertionError("the first pick is not in the catalogue")


def plant_typed_count(root):
    """A pick reason counting its own pool. The pool moves; the sentence does not."""
    p = os.path.join(root, "data", "picks.json")
    d = json.load(io.open(p, encoding="utf-8"))
    cell = next(iter(d["cells"].values()))
    cell["picks"][0]["reason"] += " Four of the eleven candidates are courses."
    io.open(p, "w", encoding="utf-8").write(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    return "counted a pool in a pick's reason"


def plant_broken_suite_query(root):
    """Strip the words the accepted answer is found by, so an asserted query misses."""
    p, items = _items(root)
    for x in items:
        if "Reduce hallucinations" in x["title"]:
            x["questions"] = ["a page about nothing in particular"]
            x["keywords"] = ["unrelated"]
            x["teaches"] = ["nothing this query asks about"]
            _write(p, items)
            return "blinded the answer to an asserted query: %s" % x["title"][:40]
    raise AssertionError("Reduce hallucinations is not in the catalogue")


def plant_question_is_a_suite_query(root):
    """A question written as a suite query is a pass bought with the answer sheet."""
    suite = io.open(os.path.join(root, "scripts", "test-search.py"),
                    encoding="utf-8").read()
    q = re.search(r'\("developer", "([^"]+)"', suite).group(1)
    p, items = _items(root)
    for x in items:
        if x.get("questions"):
            x["questions"][0] = q
            _write(p, items)
            return "wrote a suite query into a card: %r" % q
    raise AssertionError("no row carries questions")


def plant_evidence_free_gap(root):
    """A content gap is a claim about every row; without ruled_out it is only an
    opinion."""
    p = os.path.join(root, "scripts", "test-search.py")
    src = io.open(p, encoding="utf-8").read()
    marked = src.replace('("designer", "design critique", "ok",',
                         '("designer", "design critique", "content-gap",', 1)
    assert marked != src, "the anchor row is gone; pick another"
    io.open(p, "w", encoding="utf-8").write(marked)
    return "declared a content gap with no pages behind it"


def plant_typed_count_in_a_doc(root):
    """A live count in a document a reader reads. The rule has existed since August
    and docs/ had never been inside any check - FIX-31 found THE-PROJECT.md claiming a
    catalogue size two rounds old."""
    p = os.path.join(root, "docs", "THE-PROJECT.md")
    text = io.open(p, encoding="utf-8").read()
    io.open(p, "w", encoding="utf-8").write(
        text + "\n\nThe catalogue holds 999 resources and 42 paths.\n")
    return "typed a live catalogue count into THE-PROJECT.md"


def plant_missing_og_title(root):
    """A generated share page with its og:title stripped. The whole share chain is
    invisible from a browser - the tab title is written by JavaScript and is correct
    whatever the served head says - so the only way to know it still works is to read
    the built HTML, and the only way to know THAT still works is to break one."""
    import glob
    hits = sorted(glob.glob(os.path.join(root, "r", "*", "index.html")))
    if not hits:
        raise AssertionError("no share pages to plant in; did the generator run?")
    text = io.open(hits[0], encoding="utf-8").read()
    io.open(hits[0], "w", encoding="utf-8").write(
        re.sub(r'<meta property="og:title"[^>]*>\n', "", text, count=1))
    return "stripped og:title from %s" % os.path.basename(os.path.dirname(hits[0]))


def plant_synonym_without_reason(root):
    """Every synonym carries the reason it exists, like every skip_if."""
    p = os.path.join(root, "data", "synonyms.json")
    d = json.load(io.open(p, encoding="utf-8"))
    entries = d["entries"]
    row = entries[0] if isinstance(entries, list) else next(iter(entries.values()))
    row["why"] = ""
    io.open(p, "w", encoding="utf-8").write(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    return "removed a synonym row's reason"


# name, how to plant it, and a phrase the build must print when it goes red. The phrase
# rather than the script name, because a rule does not always live in the file that tests
# it: a content gap with no evidence is refused by test-search.py, which is where the rule
# is enforced, while test-gap-claims.py is that rule's own bite test.
FAULTS = [
    ("a listed row carrying a verdict", plant_listed_verdict,
     "tier is listed"),
    ("a question that is a suite query", plant_question_is_a_suite_query,
     "check-questions.py"),
    ("a suite query forced to miss", plant_broken_suite_query,
     "REGRESSION"),
    ("a content gap with no evidence", plant_evidence_free_gap,
     "A content gap is a claim about the whole catalogue"),
    ("a synonym with no reason", plant_synonym_without_reason,
     "validate-synonyms.py"),
    ("a dead pick", plant_dead_pick,
     "validate-picks.py"),
    ("a typed count in a pick's reason", plant_typed_count,
     "check-typed-numbers.py"),
    ("a live count typed into a document", plant_typed_count_in_a_doc,
     "state a count with no date beside it"),
    ("a share page with no og:title", plant_missing_og_title,
     "has no og:title"),
]


# --- running it ------------------------------------------------------------------

def copy_tree(dst):
    def ignore(d, names):
        return [n for n in names
                if n in SKIP_DIRS or os.path.splitext(n)[1].lower() in SKIP_EXT]
    shutil.copytree(ROOT, dst, ignore=ignore)
    os.makedirs(os.path.join(dst, "tmp"), exist_ok=True)


def run_build(root):
    env = dict(os.environ)
    # build.sh calls python3; Windows has no such name, and the shim the repo uses for
    # its own runs lives in tmp/bin, which is not copied.
    binp = os.path.join(root, "tmp", "bin")
    os.makedirs(binp, exist_ok=True)
    shim = os.path.join(binp, "python3")
    io.open(shim, "w", encoding="utf-8", newline="\n").write(
        '#!/bin/sh\nexec "%s" "$@"\n' % sys.executable.replace("\\", "/"))
    os.chmod(shim, 0o755)
    env["PATH"] = binp + os.pathsep + env.get("PATH", "")
    r = subprocess.run(["bash", "build.sh"], cwd=root, env=env,
                       capture_output=True, text=True, errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    if "--list" in sys.argv:
        for name, _fn, gate in FAULTS:
            print("  %-38s the build must print %r" % (name, gate))
        return 0

    # --only <substring>: plant one fault rather than all of them, for iterating on a
    # single gate without paying for a full pass.
    faults = FAULTS
    if "--only" in sys.argv:
        want = sys.argv[sys.argv.index("--only") + 1].lower()
        faults = [f for f in FAULTS if want in f[0].lower()]
        if not faults:
            print("no planted fault matches %r" % want)
            return 1

    tmp = tempfile.mkdtemp(prefix="lc-gates-")
    pristine = os.path.join(tmp, "pristine")
    failures = []
    try:
        copy_tree(pristine)

        code, out = run_build(pristine)
        if code != 0:
            print("FAIL  the control build is already red - nothing below means anything")
            print(out[-3000:])
            return 1
        print("ok    control: an untouched copy builds green")

        for name, plant, gate in faults:
            work = os.path.join(tmp, re.sub(r"\W+", "-", name))
            shutil.copytree(pristine, work)
            what = plant(work)
            code, out = run_build(work)
            shutil.rmtree(work, ignore_errors=True)
            if code == 0:
                failures.append((name, gate, "the build stayed green"))
                print("FAIL  %-38s build exit 0 - %s" % (name, what))
            elif gate not in out:
                failures.append((name, gate, "red, but never printed %r"
                                 % gate))
                print("FAIL  %-38s red at the wrong gate" % name)
            else:
                print("ok    %-38s red, saying %r"
                      % (name, gate[:34]))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    if failures:
        print("%d planted fault(s) the build could not see:" % len(failures))
        for name, gate, why in failures:
            print("  %-38s %s (%s)" % (name, why, gate))
        return 1
    print("%d planted fault(s), each turning the build red at the gate meant to "
          "catch it." % len(faults))
    return 0


if __name__ == "__main__":
    sys.exit(main())
