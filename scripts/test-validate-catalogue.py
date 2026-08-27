#!/usr/bin/env python3
"""
Prove that scripts/validate-catalogue.py actually bites.

A validator nobody has seen fail is not a validator. This takes the real catalogue,
breaks it one way at a time in a temporary directory, and checks the validator says no
and says why. The real data/ files are never written to.

    python3 scripts/test-validate-catalogue.py

Exit 1 if any rule fails to catch its fault, or if the untouched catalogue is rejected.
"""

import copy
import json
import os
import shutil
import subprocess
import sys
import tempfile

# The validator writes em dashes. A Windows console defaults to cp1252 and dies on them,
# which would turn a passing test run into a stack trace.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VALIDATOR = os.path.join(ROOT, "scripts", "validate-catalogue.py")
ITEMS = os.path.join(ROOT, "data", "items.json")
PATHS = os.path.join(ROOT, "data", "paths.json")


def run(items, paths, tmp, allowance=0):
    """Write the three inputs out and run the validator over them.

    The allowance goes to a temporary file too. Testing it against the committed one
    could only ever prove that `reviewed` is rejected; passing our own proves the other
    half — that raising the number by hand is what lets it through.
    """
    ip = os.path.join(tmp, "items.json")
    pp = os.path.join(tmp, "paths.json")
    ap = os.path.join(tmp, "allowance.txt")
    json.dump(items, open(ip, "w", encoding="utf-8"), ensure_ascii=False)
    json.dump(paths, open(pp, "w", encoding="utf-8"), ensure_ascii=False)
    open(ap, "w", encoding="utf-8").write("# written by the tests" + os.linesep
                                          + str(allowance) + os.linesep)
    r = subprocess.run([sys.executable, VALIDATOR, ip, pp, ap],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


# Each case: a name, a function that breaks a good copy, and a phrase the output must
# contain. The phrase matters — a validator that fails for the wrong reason is not
# catching the fault, it is only failing.
CASES = [
    ("required field emptied",
     lambda i, p: i[0].update({"summary": "   "}),
     "summary is missing or empty"),

    ("required list emptied",
     lambda i, p: i[0].update({"roles": []}),
     "roles is missing or empty"),

    ("skip_if emptied",
     lambda i, p: i[0].update({"skip_if": ""}),
     "skip_if is missing or empty"),

    ("skip_if is a placeholder",
     lambda i, p: i[0].update({"skip_if": "N/A."}),
     "skip_if says nothing"),

    ("role outside the vocabulary",
     lambda i, p: i[0].update({"roles": ["astronaut"]}),
     "is not in the vocabulary"),

    ("tier outside the vocabulary",
     lambda i, p: i[0].update({"tier": "read-twice"}),
     "is not in the vocabulary"),

    ("format outside the vocabulary",
     lambda i, p: i[0].update({"format": "webinar"}),
     "is not in the vocabulary"),

    ("duplicate id",
     lambda i, p: i[1].update({"id": i[0]["id"]}),
     "duplicate id"),

    ("the same url twice",
     lambda i, p: i[1].update({"url": i[0]["url"], "id": i[0]["id"]}),
     "same URL as row"),

    # The tracking suffix must not buy a second identity. This is the rule that stops
    # one resource entering the catalogue twice because somebody pasted a share link.
    ("the same url with tracking junk on the end",
     lambda i, p: i[1].update({"url": i[0]["url"] + "?utm_source=newsletter",
                               "id": i[0]["id"]}),
     "same URL as row"),

    ("id not derived from the url",
     lambda i, p: i[0].update({"id": "r-0000000000"}),
     "run scripts/stable-ids.py"),

    ("published is not a date",
     lambda i, p: i[0].update({"published": "spring 2025"}),
     "neither UNVERIFIED nor YYYY-MM-DD"),

    ("published is UNVERIFIED — must be allowed",
     lambda i, p: i[0].update({"published": "UNVERIFIED"}),
     None),                                   # None = this one must PASS

    ("checked is not a date",
     lambda i, p: i[0].update({"checked": "last week"}),
     "checked = 'last week' is not YYYY-MM-DD"),

    ("path step points at a missing id",
     lambda i, p: p[0]["steps"][0].update({"item": "r-deadbeef00"}),
     "which is not in items.json"),

    # The same relationship read the other way. Checking only path -> item let the
    # reverse rot for weeks: build-paths.py appended to each item's `paths` field and
    # never cleared it, so a step removed from a path kept its claim and eight cards
    # printed a step number for a path that did not contain them.
    ("an item claims a step in a path that does not list it",
     lambda i, p: i[0].update({"paths": [{"path": p[0]["id"], "step": 1,
                                          "of": len(p[0]["steps"])}]}),
     "does not list it there"),

    ("an item claims the right path but the wrong step number",
     lambda i, p: i.__setitem__(
         next(n for n, x in enumerate(i) if x["id"] == p[0]["steps"][0]["item"]),
         dict(i[next(n for n, x in enumerate(i) if x["id"] == p[0]["steps"][0]["item"])],
              paths=[{"path": p[0]["id"], "step": 99, "of": len(p[0]["steps"])}])),
     "does not list it there"),

    # One course harvested from two hosts is two cards, and the URL de-dupe cannot see
    # it - two URLs really are two resources to stable-ids.py. This is the check that
    # notices, and the allowance file is what stops it becoming a nuisance.
    ("the same title on two different hosts",
     lambda i, p: i[1].update({"title": i[0]["title"],
                               "url": "https://example.org/" + i[1]["id"],
                               "id": i[1]["id"]}),
     "the same title on 2 hosts"),

    # The same title twice on one host is a URL problem, not a harvest problem, and the
    # rules above already cover it. This must not double-report.
    ("the same title twice on one host - not this rule's business",
     lambda i, p: i[1].update({"title": i[0]["title"]}) if
                  __import__("urllib.parse", fromlist=["urlparse"]).urlparse(i[1]["url"]).netloc
                  == __import__("urllib.parse", fromlist=["urlparse"]).urlparse(i[0]["url"]).netloc
                  else i[1].update({"title": i[0]["title"],
                                    "url": i[0]["url"].rsplit("/", 1)[0] + "/other-thing"}),
     None),

    # The rule the README singles out. It cannot be checked directly — no file shows who
    # did what — so what is checked is the appearance of a claim nobody has authorised.
    ("an entry claims tier: reviewed when none is allowed",
     lambda i, p: i[0].update({"tier": "reviewed"}),
     "claim `tier: reviewed`"),

    ("two claim it when none is allowed",
     lambda i, p: [i[0].update({"tier": "reviewed"}), i[1].update({"tier": "reviewed"})],
     "2 entries claim"),

    # And the other half: the check must not simply forbid `reviewed` forever, or the
    # first genuine review would be unshippable and the check would be deleted.
    ("one claims it and the allowance says one — must pass",
     lambda i, p: i[0].update({"tier": "reviewed"}),
     None, 1),

    ("two claim it and the allowance says only one",
     lambda i, p: [i[0].update({"tier": "reviewed"}), i[1].update({"tier": "reviewed"})],
     "2 entries claim", 1),
]


def main():
    good_items = json.load(open(ITEMS, encoding="utf-8"))
    good_paths = json.load(open(PATHS, encoding="utf-8"))

    tmp = tempfile.mkdtemp(prefix="lc-validate-")
    failures = []
    try:
        code, out = run(good_items, good_paths, tmp)
        if code != 0:
            failures.append("the untouched catalogue was rejected:\n" + out)
            print("FAIL  untouched catalogue")
        else:
            print("ok    untouched catalogue passes")

        for case in CASES:
            name, break_it, phrase = case[0], case[1], case[2]
            allowance = case[3] if len(case) > 3 else 0   # reviewed cases set their own
            items = copy.deepcopy(good_items)
            paths = copy.deepcopy(good_paths)
            break_it(items, paths)
            code, out = run(items, paths, tmp, allowance)

            if phrase is None:
                if code == 0:
                    print("ok    %s" % name)
                else:
                    print("FAIL  %s — rejected but should have passed" % name)
                    failures.append(name + ":\n" + out)
                continue

            if code == 0:
                print("FAIL  %s — validator said the catalogue was fine" % name)
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
