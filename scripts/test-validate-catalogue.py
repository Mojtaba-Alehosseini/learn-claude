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
import importlib.util
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

# A case that changes `url` without also correcting `id` fails for id-mismatch (rule 4)
# regardless of what the case is actually testing. That's harmless for a case that
# expects a fault anyway, but it breaks a "must pass" case for the wrong reason - so the
# few cases below that invent a URL use this to keep `id` honest, the same way
# scripts/stable-ids.py itself would.
_spec = importlib.util.spec_from_file_location(
    "stable_ids", os.path.join(ROOT, "scripts", "stable-ids.py"))
_stable_ids = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_stable_ids)
make_id = _stable_ids.make_id


# The shared host normaliser, unit-tested here rather than in a file of its own because
# two of this validator's rules stand on it and CI already runs this file. It replaced
# `.lstrip("www.")` in three places on 2026-08-29 - lstrip strips a SET of characters,
# not a prefix, so it ate the leading w of any host that had one.
HOST_CASES = [
    # (url, expected host)
    ("https://www.example.com/a",        "example.com"),
    ("https://example.com/a",            "example.com"),
    ("https://WWW.Example.COM/a",        "example.com"),
    # The five the catalogue actually holds, plus the one Morteza named. Every one of
    # these came back short before the fix.
    ("https://weather.com/forecast",     "weather.com"),
    ("https://wotai.co/blog/x",          "wotai.co"),
    ("https://w3schools.com/html",       "w3schools.com"),
    ("https://willfrancis.com/x/",       "willfrancis.com"),
    ("https://warwick.libguides.com/x",  "warwick.libguides.com"),
    # The nastiest one: the prefix strips correctly and then the real name loses its w.
    ("https://www.wrightmode.com/x",     "wrightmode.com"),
    # A host that is only the prefix. Stripping leaves nothing, and that is correct -
    # there is no name here to keep.
    ("https://www./x",                   ""),
    ("",                                 ""),
]


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

    # The one that got through. "Plans & Pricing" carried this exact shape for months:
    # `n/a` was already in PLACEHOLDERS and the entry still passed, because the match was
    # on the whole string and anything after the placeholder made it unequal.
    ("skip_if is a placeholder with an excuse after it",
     lambda i, p: i[0].update(
         {"skip_if": "N/A - always verify pricing here rather than in third-party posts."}),
     "skip_if says nothing"),

    ("skip_if opens with TBD",
     lambda i, p: i[0].update({"skip_if": "TBD: nobody has written this one yet."}),
     "skip_if says nothing"),

    # And the other half, which matters more than the two above. The opener rule must not
    # reject a real sentence that happens to start with a word from the placeholder list.
    # A rule that rejects this is a rule somebody switches off the first time it is in
    # the way, and then the two cases above stop being caught as well.
    ("skip_if legitimately opens with None",
     lambda i, p: i[0].update(
         {"skip_if": "None of the examples are in Python, so you are translating as you "
                     "read if that is your language."}),
     None),                                   # None = this one must PASS

    ("skip_if legitimately opens with Anyone",
     lambda i, p: i[0].update(
         {"skip_if": "Anyone who has already built a server will find the first half slow."}),
     None),

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

    # The reverse of the step-role rule above. A path may promise "For a teacher" on the
    # index while not one step underneath it is tagged teacher - which is exactly what
    # both student-facing paths did.
    # Real role names throughout, so this fails only for the reason under test. An
    # invented name like "astronaut" would trip the vocabulary rule first and the case
    # would pass without ever exercising this one.
    ("a path declares a role no step serves",
     lambda i, p: p[0].__setitem__("roles", ["designer"]),
     "and not one of its"),

    ("a path declares a role that exactly one step serves - must pass",
     lambda i, p: (
         p[0].__setitem__("roles", ["designer"]),
         next(x for x in i if x["id"] == p[0]["steps"][0]["item"])["roles"].append("designer")
     ),
     None),

    # One course harvested from two hosts is two cards, and the URL de-dupe cannot see
    # it - two URLs really are two resources to stable-ids.py. This is the check that
    # notices, and the allowance file is what stops it becoming a nuisance.
    ("the same title on two different hosts",
     lambda i, p: i[1].update({"title": i[0]["title"],
                               "url": "https://www.udemy.com/" + i[1]["id"],
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

    # The title check above cannot see a URL collision hiding behind two different-
    # looking titles, which is exactly how four migrated-to-Academy duplicates sat in
    # the real catalogue past it on 2026-08-29 - one had "(Academy)" appended to its
    # title, nothing else different. This is the check that should have caught them.
    ("the same URL ending on two different hosts",
     lambda i, p: (i[0].update({"url": "https://www.coursera.org/a/shared-slug-xyz",
                                "id": make_id("https://www.coursera.org/a/shared-slug-xyz")}),
                   i[1].update({"url": "https://www.udemy.com/b/shared-slug-xyz",
                                "id": make_id("https://www.udemy.com/b/shared-slug-xyz")})),
     "URL ending"),

    # Same trailing segment, same host: a URL problem the rules above already cover, not
    # this one's business. Must not double-report.
    #
    # Real hosts rather than example.org since D15 (2026-09-05), which makes an unmapped
    # host a catalogue fault: a fixture that trips an unrelated rule reports the wrong
    # failure. What these two cases measure is same-host versus cross-host, and that is
    # unchanged - this pair shares one host, the pair above uses two.
    ("the same URL ending twice on one host - not this rule's business",
     lambda i, p: (i[0].update({"url": "https://www.coursera.org/a/shared-slug-xyz",
                                "id": make_id("https://www.coursera.org/a/shared-slug-xyz")}),
                   i[1].update({"url": "https://www.coursera.org/b/shared-slug-xyz",
                                "id": make_id("https://www.coursera.org/b/shared-slug-xyz")})),
     None),

    # The case the rule exists to get right without also getting this wrong. Every video
    # on youtube.com ends its path in the literal word "watch" - the real identity is in
    # the query string. Comparing bare trailing segments would make this URL collide
    # with any other host's page that happens to end in "/watch" too, for a reason that
    # has nothing to do with either resource. Must not fire.
    ("a youtube.com video does not falsely collide with an unrelated /watch page",
     lambda i, p: (i[0].update({"url": "https://www.youtube.com/watch?v=AAAAAAAAAAA",
                                "id": make_id("https://www.youtube.com/watch?v=AAAAAAAAAAA")}),
                   i[1].update({"url": "https://www.coursera.org/some/path/watch",
                                "id": make_id("https://www.coursera.org/some/path/watch")})),
     None),

    # The consequence of the lstrip bug, at catalogue level, which is the half a unit
    # test cannot show. It never raised a false alarm - it silenced a real one. Both
    # duplicate rules skip a group whose rows share a single host, so a mis-trim that
    # maps two DIFFERENT hosts onto one string makes a genuine cross-host duplicate look
    # like a same-host one and disappear. www.wrightmode.com and rightmode.com are two
    # different sites; under `.lstrip("www.")` both became "rightmode.com" and this
    # duplicate went unreported.
    ("a real cross-host duplicate is not hidden by www-stripping",
     lambda i, p: (i[0].update({"title": "Shared Title For The W Test",
                                "url": "https://www.wrightmode.com/a-guide",
                                "id": make_id("https://www.wrightmode.com/a-guide")}),
                   i[1].update({"title": "Shared Title For The W Test",
                                "url": "https://rightmode.com/a-guide",
                                "id": make_id("https://rightmode.com/a-guide")})),
     "the same title on 2 hosts"),

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


# The role-breadth warning is advisory, so nothing goes red when it is wrong - which is
# exactly why it needs a test. Its first implementation matched substrings, so "engineer"
# matched inside "engineering"; the fix for that was written through a shell heredoc that
# ate the escapes, leaving a matcher that matched EVERYTHING. Every role then counted as
# named, no item ever had exactly one, and the check reported zero findings while looking
# healthy. Both failure directions are pinned below.
ROLE_WORD_CASES = [
    # (card text, role, should this text be read as naming that role?)
    ("four prompt engineering practitioners talk through prompts", "developer", False),
    ("written for engineers shipping to production", "developer", True),
    ("for working designers evaluating the tool", "designer", True),
    ("a course on design systems", "designer", True),
    ("teachers and lecturers planning a term", "teacher", True),
    ("owners doing their own numbers", "business-founder", True),
    ("analysts fielding ad-hoc questions", "data-analyst", True),
    # The matcher must not be a rubber stamp: a card that names nobody names nobody.
    ("a short guided tour of the product", "developer", False),
    ("a short guided tour of the product", "teacher", False),
]


def main():
    good_items = json.load(open(ITEMS, encoding="utf-8"))
    good_paths = json.load(open(PATHS, encoding="utf-8"))

    tmp = tempfile.mkdtemp(prefix="lc-validate-")
    failures = []
    try:
        host_bad = [(u, want, _stable_ids.host(u))
                    for u, want in HOST_CASES if _stable_ids.host(u) != want]
        if host_bad:
            for u, want, got in host_bad:
                print("FAIL  host(%r) -> %r, wanted %r" % (u, got, want))
                failures.append("host(%r) gave %r, wanted %r" % (u, got, want))
        else:
            print("ok    host() strips the www. prefix and nothing else (%d urls)"
                  % len(HOST_CASES))

        _vspec = importlib.util.spec_from_file_location("validate_catalogue_uut",
                                                        VALIDATOR)
        vc = importlib.util.module_from_spec(_vspec)
        _vspec.loader.exec_module(vc)
        word_bad = [(t, r, want) for t, r, want in ROLE_WORD_CASES
                    if vc._names_role(" %s " % t, r) != want]
        if word_bad:
            for t, r, want in word_bad:
                print("FAIL  _names_role(%r, %r) should be %s" % (t, r, want))
                failures.append("_names_role(%r, %r) wanted %s" % (t, r, want))
        else:
            print("ok    role words match on word boundaries, both ways (%d cases)"
                  % len(ROLE_WORD_CASES))

        planted = copy.deepcopy(good_items)
        planted[0].update({"roles": ["designer", "teacher", "student"],
                           "who_for": "Working designers evaluating the tool.",
                           "summary": "A critique of one product's output quality."})
        if [t for t, _, _ in vc.role_breadth_warnings(planted)
                if t == planted[0]["title"][:52]]:
            print("ok    a planted one-persona card under 3 roles is reported")
        else:
            print("FAIL  the role-breadth check missed a planted mis-tag")
            failures.append("role_breadth_warnings missed a planted mis-tag")

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
        print("%d of %d checks did not do their job:" % (len(failures), len(CASES) + 4))
        for f in failures:
            print("  - " + f)
        return 1
    # +2, not +1: the untouched-catalogue check, and the host() unit phase above it.
    print("All %d checks caught their fault. data/ was not touched." % (len(CASES) + 4))
    return 0


if __name__ == "__main__":
    sys.exit(main())
