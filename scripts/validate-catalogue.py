#!/usr/bin/env python3
"""
Validate the catalogue itself, before anything is built from it.

This is not scripts/validate-report.py. That one checks an incoming research report on
its way in, and it rejects data/items.json by design. Nothing checked the catalogue
after the merge, so a broken entry could reach the live site without one step going
red. This closes that.

    python3 scripts/validate-catalogue.py
    python3 scripts/validate-catalogue.py <items.json> <paths.json>   # for the tests

It reports every fault it finds, then exits 1. It never prints only the first, because
fixing one fault and pushing again to discover the next is how a five-minute repair
becomes an afternoon.

The controlled vocabularies are read out of assets/js/ui.js, not copied here. A copy is
a second source of truth, and the second source is always the one nobody updates. If a
label is added to the site it is legal here the moment it is added there, and if the
shape of ui.js ever changes this stops with an error rather than quietly passing
everything.

The id rule is imported from scripts/stable-ids.py for the same reason. An id is a hash
of the normalised URL. Re-implementing either half here would let this file bless ids
that stable-ids.py would not produce.
"""

import importlib.util
import json
import os
import re
import sys

# This prints em dashes. A Windows console defaults to cp1252 and raises on them, so a
# real fault would be reported as a UnicodeEncodeError instead of as the fault.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITEMS = os.path.join(ROOT, "data", "items.json")
PATHS = os.path.join(ROOT, "data", "paths.json")
UI_JS = os.path.join(ROOT, "assets", "js", "ui.js")
STABLE_IDS = os.path.join(ROOT, "scripts", "stable-ids.py")

# Every field that must be present and must not be empty. roles and topics are lists,
# so "not empty" means at least one entry, not merely that the key exists.
REQUIRED = ["url", "title", "source", "summary", "who_for", "skip_if", "checked",
            "tier", "status", "level", "format", "time", "cost", "roles", "topics", "id"]

LIST_FIELDS = {"roles", "topics"}

# The one vocabulary with no map in ui.js. The site never lists these — it only asks
# `item.status === "dead"` in ui.js and resource.js — so there is nothing to read.
STATUS = {"live", "dead", "outdated"}

DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Ways of writing "I did not fill this in". They pass an empty check and fail the
# reader, which is worse than an empty field because nothing flags them.
PLACEHOLDERS = {"n/a", "na", "none", "nobody", "no one", "no-one", "nil", "tbd",
                "todo", "unknown", "unclear", "everyone", "anyone", ""}


# ------------------------------------------------------------------ ui.js ----

def js_object_keys(source, name):
    """Return the top-level keys of `LC.<name> = { ... }` in a JavaScript file.

    Written as a character scan rather than a regular expression because LC.TIER holds
    an object per key, and a regular expression that survives one level of nesting is a
    regular expression nobody can correct later.
    """
    start = source.find("LC." + name + " =")
    if start == -1:
        raise SystemExit(
            "validate-catalogue.py cannot find LC.%s in assets/js/ui.js.\n"
            "The vocabularies are read from that file on purpose. Either the name "
            "changed or the file moved; fix this script rather than copying the list "
            "into it." % name)
    brace = source.find("{", start)
    depth, i, in_str, quote, esc = 0, brace, False, "", False
    keys, body_start = [], brace + 1
    while i < len(source):
        c = source[i]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == quote:
                in_str = False
        elif c in "\"'":
            in_str, quote = True, c
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                body = source[body_start:i]
                break
        i += 1
    else:
        raise SystemExit("Unbalanced braces reading LC.%s from assets/js/ui.js" % name)

    # Keys sit at depth 1 of the captured body. Walk it the same way and take every
    # quoted string that is immediately followed by a colon.
    depth, i, in_str, quote, esc, cur, cur_start = 0, 0, False, "", False, "", 0
    while i < len(body):
        c = body[i]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == quote:
                in_str = False
                j = i + 1
                while j < len(body) and body[j] in " \t\r\n":
                    j += 1
                if depth == 0 and j < len(body) and body[j] == ":":
                    keys.append(cur)
            else:
                cur += c
        elif c in "\"'":
            in_str, quote, cur = True, c, ""
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        i += 1
    if not keys:
        raise SystemExit("Read no keys from LC.%s in assets/js/ui.js" % name)
    return set(keys)


def load_vocabularies():
    src = open(UI_JS, encoding="utf-8").read()
    return {
        "roles":  js_object_keys(src, "ROLE"),
        "level":  js_object_keys(src, "LEVEL"),
        "time":   js_object_keys(src, "TIME"),
        "cost":   js_object_keys(src, "COST"),
        "format": js_object_keys(src, "FORMAT"),
        "topics": js_object_keys(src, "TOPIC"),
        "tier":   js_object_keys(src, "TIER"),
        "status": STATUS,
    }


def load_id_rule():
    spec = importlib.util.spec_from_file_location("stable_ids", STABLE_IDS)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.make_id, mod.norm


# ---------------------------------------------------------------- checks ----

def main(argv=None):
    """argv lets scripts/test-validate-catalogue.py point this at mutated copies in a
    temporary directory. Without it nothing could prove the rules bite without editing
    the real catalogue to break it."""
    argv = argv if argv is not None else sys.argv[1:]
    items_path = argv[0] if len(argv) > 0 else ITEMS
    paths_path = argv[1] if len(argv) > 1 else PATHS

    vocab = load_vocabularies()
    make_id, norm = load_id_rule()

    items = json.load(open(items_path, encoding="utf-8"))
    errors = []

    def bad(row, item, msg):
        title = str(item.get("title", ""))[:44] or "(no title)"
        errors.append("  row %-4d %-46s %s" % (row, title, msg))

    seen_ids, seen_urls = {}, {}

    for n, item in enumerate(items):
        # 1. required fields, present and not empty
        for f in REQUIRED:
            v = item.get(f)
            if f in LIST_FIELDS:
                empty = not isinstance(v, list) or len(v) == 0
            else:
                empty = v is None or (isinstance(v, str) and not v.strip())
            if empty:
                bad(n, item, "%s is missing or empty" % f)

        # 2. skip_if again, on its own terms. It is the reason the site exists, and a
        #    placeholder clears the empty check above while telling the reader nothing.
        #    Named forms rather than a length limit: the shortest real one in the
        #    catalogue is "You don't use R.", and a rule that rejects that is a rule
        #    that will be switched off the first time it is in the way.
        skip = str(item.get("skip_if", "")).strip()
        if skip and (skip.lower().strip(" .!-—") in PLACEHOLDERS or len(skip) < 8):
            bad(n, item, "skip_if says nothing: %r. Every entry has to name someone "
                         "this is wrong for." % skip)

        # 3. controlled vocabulary
        for f, allowed in vocab.items():
            v = item.get(f)
            if v is None:
                continue
            values = v if isinstance(v, list) else [v]
            for one in values:
                if one not in allowed:
                    bad(n, item, "%s = %r is not in the vocabulary (%s)"
                                 % (f, one, ", ".join(sorted(allowed))))

        # 4. the id must be the hash of the URL, not something written by hand
        url = item.get("url")
        if isinstance(url, str) and url.strip():
            want = make_id(url)
            if item.get("id") != want:
                bad(n, item, "id is %r but the URL gives %r — run scripts/stable-ids.py"
                             % (item.get("id"), want))
            key = norm(url)
            if key in seen_urls:
                bad(n, item, "same URL as row %d after normalising: %s"
                             % (seen_urls[key], key))
            else:
                seen_urls[key] = n

        # 5. duplicate ids
        iid = item.get("id")
        if iid:
            if iid in seen_ids:
                bad(n, item, "duplicate id %s, first seen at row %d" % (iid, seen_ids[iid]))
            else:
                seen_ids[iid] = n

        # 6. dates. published may say it does not know; checked never may, because we
        #    did the checking ourselves and always know when.
        pub = item.get("published")
        if pub is not None and pub != "UNVERIFIED" and not DATE.match(str(pub)):
            bad(n, item, "published = %r is neither UNVERIFIED nor YYYY-MM-DD" % pub)
        chk = item.get("checked")
        if chk is not None and not DATE.match(str(chk)):
            bad(n, item, "checked = %r is not YYYY-MM-DD" % chk)

    # 7. every path step must point at a resource that exists. This is the failure the
    #    id rewrite was built to prevent: a step that still renders, still prints a
    #    confident reason, and points at the wrong thing.
    path_errors = []
    if os.path.exists(paths_path):
        known = set(seen_ids)
        for path in json.load(open(paths_path, encoding="utf-8")):
            for step in path.get("steps", []):
                ref = step.get("item")
                if ref not in known:
                    path_errors.append(
                        "  path %-22s step %-3s points at %r, which is not in items.json"
                        % (path.get("id"), step.get("step"), ref))

    # ------------------------------------------------------------ report ----

    if not errors and not path_errors:
        n_paths = (len(json.load(open(paths_path, encoding="utf-8")))
                   if os.path.exists(paths_path) else 0)
        print("%d resources, %d paths — catalogue is valid." % (len(items), n_paths))
        return 0

    if errors:
        print("%d fault%s in %s:" % (len(errors), "" if len(errors) == 1 else "s", items_path))
        for e in errors:
            print(e)
    if path_errors:
        if errors:
            print()
        print("%d broken path step%s in %s:"
              % (len(path_errors), "" if len(path_errors) == 1 else "s", paths_path))
        for e in path_errors:
            print(e)
    print()
    print("Nothing was changed. Fix the data and run this again.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
