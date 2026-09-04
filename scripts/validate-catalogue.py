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

One rule here is not really a data check. "Only a person may write tier: reviewed" is a
statement about who did something, and a file cannot show that. So this does not test
provenance — it tests for the event. Nothing is `reviewed` today, so any appearance of
it is news, and news should stop the build until a person says otherwise. See
data/reviewed-allowance.txt.
"""

import importlib.util
import json
import os
import re
import sys
from urllib.parse import urlparse

# This prints em dashes. A Windows console defaults to cp1252 and raises on them, so a
# real fault would be reported as a UnicodeEncodeError instead of as the fault.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITEMS = os.path.join(ROOT, "data", "items.json")
PATHS = os.path.join(ROOT, "data", "paths.json")
UI_JS = os.path.join(ROOT, "assets", "js", "ui.js")
STABLE_IDS = os.path.join(ROOT, "scripts", "stable-ids.py")
ALLOWANCE = os.path.join(ROOT, "data", "reviewed-allowance.txt")
DUPE_TITLES = os.path.join(ROOT, "data", "duplicate-titles.txt")
DUPE_SLUGS = os.path.join(ROOT, "data", "duplicate-slugs.txt")

# Every field that must be present and must not be empty. roles and topics are lists,
# so "not empty" means at least one entry, not merely that the key exists.
REQUIRED = ["url", "title", "source", "summary", "who_for", "skip_if", "checked",
            "tier", "status", "level", "format", "time", "cost", "roles", "topics", "id"]

LIST_FIELDS = {"roles", "topics"}

# The one vocabulary with no map in ui.js. The site never lists these — it only asks
# `item.status === "dead"` in ui.js and resource.js — so there is nothing to read.
STATUS = {"live", "dead", "outdated"}

# How we know a date. Required on any row carrying a real `published` or `updated`;
# `UNVERIFIED` needs none, because "we do not know" is already the whole statement.
#
# Added 2026-09-05 after a sweep found 9 stored dates disagreeing with their own pages,
# one by nine months - and found that not one of the nine recorded where its date came
# from. The notes fields were careful about affiliate codes, paywalls and vendor bias,
# and silent on provenance, so a wrong date was unfalsifiable until a machine could read
# the page. This is the same move the site already made twice: never round up, and say
# what you actually know.
DATE_SOURCES = {
    "printed":  "a person read the date on the page",
    "metadata": "parsed from JSON-LD, article:published_time or dateModified",
    "upload":   "a video platform's upload date",
    "intercom": "the Help Center's Intercom template, read by the weekly parser",
}

DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Ways of writing "I did not fill this in". They pass an empty check and fail the
# reader, which is worse than an empty field because nothing flags them.
PLACEHOLDERS = {"n/a", "n\a", "n.a.", "not applicable", "na", "none", "nobody",
                "no one", "no-one", "nil", "tbd", "todo", "unknown", "unclear",
                "everyone", "anyone", ""}

# A placeholder with an excuse after it. "Plans & Pricing" carried
#   "N/A - always verify pricing here rather than in third-party posts."
# for months. `n/a` was already in the set above and the entry still passed, because the
# match was on the whole string: put anything after the placeholder and it is no longer
# equal to it. The line is still an empty line wearing a sentence.
#
# Only the forms that cannot begin a real sentence are listed here. "none", "everyone",
# "anyone", "unknown" and "nobody" are deliberately NOT in this set - "None of the
# examples are in Python" is a perfectly good skip_if, and a rule that rejects it is a
# rule somebody switches off the first time it is in the way.
PLACEHOLDER_OPENERS = ("n/a", "n\a", "n.a.", "na", "nil", "tbd", "todo",
                       "not applicable")


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


def load_allowance(path):
    """The number of entries permitted to claim `tier: reviewed`.

    Read as the last line that is not blank and not a comment, so the file can carry the
    explanation of why it exists next to the number it holds. A missing or unreadable
    file is a hard stop rather than a default of zero: silently assuming the strictest
    value would turn a deleted file into a mysterious build failure somewhere else.
    """
    if not os.path.exists(path):
        raise SystemExit(
            "%s is missing. It records how many entries may claim `tier: reviewed`. "
            "Restore it from git rather than guessing a number." % path)
    value = None
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#"):
            value = line
    try:
        return int(value)
    except (TypeError, ValueError):
        raise SystemExit("%s must end with a plain number. It ends with %r." % (path, value))


def load_allowed_titles(path):
    """Normalised titles permitted to appear on more than one host.

    Read the same way as the reviewed allowance: last-word-wins on each line, everything
    after a # is the reason. Missing file means nothing is allowed, which is the strict
    direction and is safe - it fails loudly rather than passing silently.
    """
    out = set()
    if not os.path.exists(path):
        return out
    for line in open(path, encoding="utf-8"):
        line = line.split("#", 1)[0].strip()
        if line:
            out.add(line)
    return out


# Words that make a role's claim on an item visible in its own card text. Deliberately
# generous: this feeds a WARNING, and a generous list means fewer false alarms in a check
# nobody is obliged to act on.
ROLE_WORDS = {
    # "anyone", "everyone" and "someone" are deliberately NOT here. They were, and on
    # 2026-09-04 they made the check fire on six freshly written entries whose who_for
    # opened "Anyone who..." - deliberately role-neutral copy for material that genuinely
    # serves every tagged role. That is the opposite of the fault this check exists for.
    # The Puckett fault is a who_for naming ONE persona under many tags; a who_for naming
    # NO persona is not mis-tagged, it is general. With the universal words removed such
    # an item matches zero roles and falls out of the len==1 test on its own.
    "non-technical":   ("non-technical", "non technical", "not a coder", "no coding",
                        "non-developer", "non-coder", "normal people"),
    "student":         ("student", "phd", "grad", "undergrad", "revision", "coursework"),
    "researcher":      ("research", "researcher", "academic", "scientist", "postdoc",
                        "clinician", "faculty", "literature", "paper"),
    "teacher":         ("teacher", "educator", "lecturer", "instructor", "professor",
                        "classroom", "teaching", "school", "syllabus", "student"),
    "developer":       ("developer", "engineer", "coder", "programmer", "technical",
                        "terminal", "codebase", "python", "git"),
    "data-analyst":    ("analyst", "data", "spreadsheet", "excel", "sql", "dataset"),
    "pm":              ("product manager", "pm", "product people", "product",
                        "roadmap", "prd"),
    "designer":        ("designer", "design", "ux", "ui", "figma", "prototype"),
    "business-founder": ("founder", "business", "owner", "entrepreneur", "ops",
                         "operations", "sales", "finance", "hr", "legal", "nonprofit",
                         "small business", "marketer", "marketing", "team lead"),
    "writer-marketer": ("writer", "marketer", "marketing", "content", "copy", "author",
                        "journalist", "editor", "manuscript"),
}


def _names_role(hay, role):
    """Does this card text name `role`, as a word rather than as a substring?

    Plain `in` was wrong and produced a false alarm on its first run: "engineer" is a
    substring of "engineering", so "prompt engineering practitioners" in a summary made
    an item look developer-only when its who_for was deliberately role-neutral. Matching
    on word boundaries with an optional plural keeps "designers" and "analysts" while
    refusing "engineering" for "engineer".
    """
    for w in ROLE_WORDS.get(role, (role,)):
        # Lookarounds rather than a backslash-b, on purpose. This pattern was first
        # written into the file through a shell heredoc, which ate both escapes and left
        # backspace characters instead: the matcher then matched everything, every role
        # counted as named, no item ever had exactly one, and the check reported zero
        # findings while looking perfectly healthy. A pattern with no backslash in its
        # source cannot fail that way.
        if re.search("(?<![a-z])%ss?(?![a-z])" % re.escape(w.strip()), hay):
            return True
    return False


def role_breadth_warnings(items):
    """Advisory only. Items whose who_for names ONE persona while carrying 3+ role tags.

    Written after a real fault, and deliberately not an error. On 2026-08-31 a Dive Club
    interview with a Stripe design manager carried five role tags — designer,
    non-technical, pm, student, teacher — while its who_for named designers and nobody
    else. Nothing broke until "start with these three" ran, at which point the publisher
    rule was about to seat that interview in teachers' picks. Browsing had never surfaced
    it; a comparative feature did.

    This cannot be an error and must never auto-fix, because breadth is often correct:
    Claude 101 genuinely serves every role, and its who_for cannot name ten personas
    without becoming useless. Only a person can tell a broad resource from a mis-tagged
    one. So this prints, and stops there.
    """
    out = []
    for item in items:
        roles = item.get("roles") or []
        if len(roles) < 3:
            continue
        hay = " %s %s " % (item.get("who_for", ""), item.get("summary", ""))
        hay = hay.lower()
        supported = [r for r in roles if _names_role(hay, r)]
        if len(supported) == 1:
            out.append((item.get("title", "")[:52], supported[0],
                        sorted(set(roles) - set(supported))))
    return out


def opening_share(items, field, n=3):
    """Share of `field` lines that share their first `n` words with another line.

    Measured once by hand on 2026-08-29, on skip_if: the 291 lines written in a single
    Academy run shared an opening 5% of the time, and the 333 written slowly over earlier
    rounds shared 12%. The conclusion at the time was that fast batches were not the
    problem. Two rounds later six who_for lines written in one batch all opened "Anyone
    who..." and nobody noticed until an unrelated check tripped on them - because that
    measurement had been taken once, by hand, and never again.

    So it runs every build now, on both fields. It PRINTS and never fails: a build that
    goes red on a copy statistic is a build that teaches people to edit copy until the
    number moves, which is worse than the monotony.
    """
    opens = {}
    for it in items:
        words = re.findall(r"[a-z']+", (it.get(field) or "").lower())
        if len(words) < n:
            continue
        key = " ".join(words[:n])
        opens.setdefault(key, []).append(it)
    shared = {k: v for k, v in opens.items() if len(v) > 1}
    total = sum(len(v) for v in opens.values())
    dup = sum(len(v) for v in shared.values())
    top = sorted(shared.items(), key=lambda kv: -len(kv[1]))[:5]
    return {"total": total, "shared": dup,
            "pct": 0 if not total else round(100.0 * dup / total),
            "distinct": len(opens),
            "largest": max([len(v) for v in opens.values()] or [0]),
            "top": [(k, len(v)) for k, v in top]}


# Measured 2026-09-05 on 635 rows and set as the floor, so this fires on REGRESSION
# rather than permanently. The 10% threshold it replaces was on the `shared` figure,
# which sat at 44% on its first run and can never fall below roughly 20% - "Skip if you"
# is the natural English opening for a field called skip_if, and a light that is always
# on is a light nobody reads. Variety is the figure that moves when a batch is written
# in one sitting with one sentence shape, which is the thing worth catching.
#
# Raise these when variety genuinely improves. Never lower them to make a build quiet.
VARIETY_BASELINE = {"skip_if": 63, "who_for": 74}


def report_monotony(items):
    """Print the opening-word share for skip_if and who_for. Warn above 10%.

    Two figures, because the first one alone turned out to carry no signal.

    `shared` is the measurement as specified: the share of lines whose first three words
    match another line's. On first run it was 44% for skip_if, and it will never fall
    below about 20%, because "Skip if you" is the natural English opening for a field
    called skip_if. A threshold that is permanently exceeded is a light that is always
    on, and nobody reads it.

    `variety` is the figure that moves: distinct openings as a share of lines, and the
    size of the largest single cluster. When a batch is written in one sitting with one
    sentence shape - six who_for lines all opening "Anyone who...", which is what
    actually happened on 2026-09-04 - variety falls and the largest cluster grows. That
    is the shape worth watching.

    Both print. Neither fails a build. A build that goes red on a copy statistic teaches
    people to edit copy until the number moves, which is worse than the monotony.
    """
    print("Copy openings (printed, never enforced - nobody edits copy to move a "
          "statistic):")
    for field in ("skip_if", "who_for"):
        m = opening_share(items, field)
        total = m["total"]
        variety = 0 if not total else round(100.0 * m["distinct"] / total)
        floor = VARIETY_BASELINE.get(field)
        flag = ""
        if floor is not None and variety < floor:
            flag = "  ** BELOW BASELINE %d%% - variety has fallen" % floor
        print("  %-8s variety %d%% (%d distinct openings for %d lines), largest "
              "cluster %d%s" % (field, variety, m["distinct"], total, m["largest"], flag))
        print("           shared %d%% share their first three words - see the note in "
              "the source for why this figure is not the one to watch" % m["pct"])
        for phrase, count in m["top"][:3]:
            print("             %-34s %d lines" % ('"' + phrase + '..."', count))
    print()


# Words and digits that count as a number when they sit next to a unit this site
# computes. "one" and "a" are deliberately absent - "one real course", "a week of
# practice" are prose, not arithmetic.
NUMBER_WORDS = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "fifteen", "twenty", "thirty", "forty", "fifty",
                "sixty", "ninety", "hundred")

# The units the build already computes and prints. A typed figure beside one of these is
# a second copy of a generated number.
COUNTED_UNITS = ("minute", "minutes", "hour", "hours", "day", "days", "week", "weeks",
                 "step", "steps", "resource", "resources", "publisher", "publishers",
                 "item", "items", "cell", "cells", "percent", "%")

_NUM_NEAR_UNIT = re.compile(
    r"(?<![\w-])(\d+(?:\.\d+)?|%s)\s+(?:[a-z-]+\s+){0,2}?(%s)\b"
    % ("|".join(NUMBER_WORDS), "|".join(u for u in COUNTED_UNITS if u != "%")),
    re.I)
_PCT = re.compile(r"(?<![\w-])(\d+(?:\.\d+)?)\s*%")


def typed_numbers(text):
    """Every figure in `text` that sits next to a unit the build computes."""
    hits = []
    for m in _NUM_NEAR_UNIT.finditer(text or ""):
        hits.append(m.group(0).strip())
    for m in _PCT.finditer(text or ""):
        hits.append(m.group(0).strip())
    return hits


def report_typed_numbers(paths_path, ui_js_path):
    """Print every typed figure in reader-facing prose. Warning, never an error.

    Written 2026-09-05 because the rule alone was not enough. `measure.py` was built to
    end hand-typed counts on 4 September; on 5 September a path intro said "about ninety
    minutes" against a build that computes 81 and prints it two lines above, and four
    other intros carried the same shape. The rule existed, it was written down, and it
    did not fire - because prose in a build script did not feel like documentation.

    Some of these are legitimate: "steps 1, 2, 4, 5 and 6 take fifteen minutes each" is
    an argument about shape that no computed total can make. So this prints and never
    fails. The point is only that a typed figure cannot sit there unseen.
    """
    found = []
    try:
        paths = json.load(open(paths_path, encoding="utf-8"))
    except Exception:                                    # noqa: BLE001
        paths = []
    for p in paths:
        for field, text in [("intro", p.get("intro", ""))]:
            for h in typed_numbers(text):
                found.append(("paths.json", "%s.%s" % (p.get("id"), field), h))
        for n, st in enumerate(p.get("steps", []), 1):
            for h in typed_numbers(st.get("why", "")):
                found.append(("paths.json", "%s.step%d.why" % (p.get("id"), n), h))

    try:
        src = open(ui_js_path, encoding="utf-8").read()
    except Exception:                                    # noqa: BLE001
        src = ""
    # No newlines inside the match: the first version allowed them, so a single "match"
    # ran from one quote through several lines of code and comments to the next quote,
    # and reported a figure from a comment as if it were a UI string. Comments are not
    # reader-facing; strings are.
    for m in re.finditer(r'"((?:[^"\\\n]|\\.){8,200})"', src):
        text = m.group(1)
        if not re.search(r"[a-z]{3}\s+[a-z]{3}", text, re.I):
            continue                                     # not a sentence
        for h in typed_numbers(text):
            found.append(("ui.js", text[:38] + "...", h))

    if not found:
        print("Typed numbers in reader-facing prose: none.")
        print()
        return
    print("Typed numbers in reader-facing prose (%d). Printed, never enforced - some are"
          % len(found))
    print("legitimate. The build computes steps, durations, costs and every count in")
    print("STATUS.md; a figure typed beside one of those is a second copy waiting to rot:")
    for where, field, hit in found:
        print("  %-11s %-34s %s" % (where, field[:34], hit))
    print()


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", str(t or "").lower()).strip()


def load_id_rule():
    """The URL rules, all three, from the one file that defines them.

    host() joins make_id and norm here for the reason the others are here: this file had
    its own copy, written as `.lstrip("www.")`, which strips a set of characters rather
    than a prefix and mapped wotai.co onto otai.co. See the note on host() in
    scripts/stable-ids.py for why that silenced rules 10 and 11 rather than tripping them.
    """
    spec = importlib.util.spec_from_file_location("stable_ids", STABLE_IDS)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.make_id, mod.norm, mod.host


# ---------------------------------------------------------------- checks ----

def main(argv=None):
    """argv lets scripts/test-validate-catalogue.py point this at mutated copies in a
    temporary directory. Without it nothing could prove the rules bite without editing
    the real catalogue to break it."""
    argv = argv if argv is not None else sys.argv[1:]
    items_path = argv[0] if len(argv) > 0 else ITEMS
    paths_path = argv[1] if len(argv) > 1 else PATHS
    allowance_path = argv[2] if len(argv) > 2 else ALLOWANCE

    vocab = load_vocabularies()
    make_id, norm, host = load_id_rule()

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
        low = skip.lower().strip(" .!-—")
        opener = any(low == o or low.startswith(o + " ") or low.startswith(o + ",")
                     or low.startswith(o + ":") or low.startswith(o + ";")
                     for o in PLACEHOLDER_OPENERS)
        if skip and (low in PLACEHOLDERS or opener or len(skip) < 8):
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

    # 8. `tier: reviewed` says a person read the whole thing. No file can show that a
    #    person did anything, so this does not try to check provenance. It checks for
    #    the event instead. Nothing is reviewed today, so the appearance of one is news,
    #    and news stops the build until a person raises the number by hand.
    allowance = load_allowance(allowance_path)
    claimed = [(n, it) for n, it in enumerate(items) if it.get("tier") == "reviewed"]
    tier_errors = []
    if len(claimed) > allowance:
        tier_errors.append(
            "%d entr%s claim `tier: reviewed`. %s allowed by %s."
            % (len(claimed), "y" if len(claimed) == 1 else "ies", allowance, allowance_path))
        tier_errors.append("")
        for n, it in claimed:
            tier_errors.append("  row %-4d %s" % (n, str(it.get("title", ""))[:60]))
        tier_errors.append("")
        tier_errors.append(
            "  `reviewed` means a person read all of it. If an automated stage wrote "
            "this, take it back out.")
        tier_errors.append(
            "  If a person really did finish %s, confirm each one and raise the number "
            "in that file by hand." % ("it" if len(claimed) == 1 else "them"))

    # 9. and the same check in the other direction. An item carries a `paths` field
    #    saying which step of which path it is, and the card prints it. Checking only
    #    path -> item let the reverse rot: build-paths.py appended to that field and
    #    never cleared it, so a step removed from a path kept its claim, and eight cards
    #    printed "This is step 1 of 6 in first-week" for a path whose six steps did not
    #    include them. Both directions have to agree or one of them is lying.
    if os.path.exists(paths_path):
        truth = {}
        for path in json.load(open(paths_path, encoding="utf-8")):
            for step in path.get("steps", []):
                truth.setdefault(step.get("item"), set()).add(
                    (path.get("id"), step.get("step"), len(path.get("steps", []))))
        for n, item in enumerate(items):
            for claim in item.get("paths") or []:
                key = (claim.get("path"), claim.get("step"), claim.get("of"))
                if key not in truth.get(item.get("id"), set()):
                    path_errors.append(
                        "  row %-4d %-40s claims step %s of %s in %r, and that path does "
                        "not list it there" % (n, str(item.get("title", ""))[:40],
                                               claim.get("step"), claim.get("of"),
                                               claim.get("path")))

    # 9b. and the third way this relationship can lie. Rule 7 catches a step that shares
    #     no role with its path. It does not catch the reverse: a path declaring a role
    #     that not one of its steps serves. Both paths naming a student contained zero
    #     steps tagged student, and the page said "For a student" anyway - a promise made
    #     on the index and broken by every step underneath it.
    if os.path.exists(paths_path):
        by_id = {i.get("id"): i for i in items}
        for path in json.load(open(paths_path, encoding="utf-8")):
            served = set()
            for step in path.get("steps", []):
                it = by_id.get(step.get("item"))
                if it:
                    served |= set(it.get("roles") or [])
            for role in path.get("roles") or []:
                if role not in served:
                    path_errors.append(
                        "  path %-22s declares role %r and not one of its %d steps is "
                        "tagged with it. Tag the steps that really serve that reader, or "
                        "drop the role from the path in scripts/build-paths.py."
                        % (path.get("id"), role, len(path.get("steps", []))))

    # 10. one course, harvested from two hosts, becomes two cards. The URL de-dupe
    #     cannot see it: two different URLs are two different resources as far as
    #     stable-ids.py is concerned, and correctly so. What it cost: the only developer
    #     path advertised "about 6 hours" purely because the build reached the
    #     anthropic.skilljar.com row for step 1 before the academy.claude.com row for the
    #     same course, which records a shorter time. Merged 2026-08-27, and the same path
    #     now reads "about 3 hours". A headline number should not depend on harvest order.
    allowed_titles = load_allowed_titles(DUPE_TITLES)
    by_title = {}
    for n, item in enumerate(items):
        by_title.setdefault(norm_title(item.get("title")), []).append((n, item))
    for title, rows in sorted(by_title.items()):
        if len(rows) < 2 or title in allowed_titles:
            continue
        hosts = {host(it.get("url")) for _, it in rows}
        if len(hosts) < 2:
            continue                      # same host twice is caught by the URL rules
        errors.append(
            "  %-4s %-46s the same title on %d hosts (%s). If they are one resource, "
            "merge them; if they are two, add the title to %s with the reason."
            % ("", str(rows[0][1].get("title", ""))[:46], len(hosts),
               ", ".join(sorted(hosts)), DUPE_TITLES))

    # 11. the same resource reachable at two different-looking URLs on two different
    #     hosts, with titles that happen to differ by a word or a dash. Rule 10 catches
    #     a collision in the reader-facing title; it cannot catch one in the URL, and
    #     that is exactly where four migrated-to-Academy duplicates hid on 2026-08-29 -
    #     one had "(Academy)" appended to its title, another an extra "- two classroom
    #     workflows", past the exact-title check three times before a person looking by
    #     hand found them.
    #
    #     The trailing path segment is usually the real identity of a resource - a slug
    #     is meant to be unique to the thing it names. youtube.com and youtu.be are the
    #     common exception: every video on those hosts ends in the literal word "watch",
    #     with the real identity in the query string (?v=<id>), so comparing bare
    #     trailing segments there would collide every video in the catalogue into one
    #     false group. Compare the full normalised URL instead for those two hosts -
    #     which already distinguishes by query string, and which rule 4 above already
    #     trusts for the same reason.
    GENERIC_PATH_HOSTS = {"youtube.com", "youtu.be"}

    # This used to carry its own correct copy of the www-stripping logic, written a week
    # after the two broken copies and never compared against them. Three definitions of
    # one rule, two of them wrong, is the shape of fault this file exists to catch in the
    # data - so it uses the shared host() now, like everything else.
    def url_slug(u, h):
        if h in GENERIC_PATH_HOSTS:
            return norm(u)
        seg = urlparse(str(u or "")).path.rstrip("/").rsplit("/", 1)[-1].lower()
        return seg or None

    allowed_slugs = load_allowed_titles(DUPE_SLUGS)   # same read, a different file
    by_slug = {}
    for n, item in enumerate(items):
        # `h`, not `host` - that name is the shared helper now, and rebinding it here
        # would leave every later row calling a string.
        h = host(item.get("url"))
        slug = url_slug(item.get("url"), h)
        if not h or not slug:
            continue
        by_slug.setdefault(slug, []).append((n, item, h))
    for slug, slug_rows in sorted(by_slug.items()):
        if len(slug_rows) < 2 or slug in allowed_slugs:
            continue
        slug_hosts = {h for _, _, h in slug_rows}
        if len(slug_hosts) < 2:
            continue                      # same host twice is a different fault, not this one
        errors.append(
            "  %-4s %-46s URL ending %r on %d hosts (%s). If they are one resource, "
            "merge them; if they are two, add the ending to %s with the reason."
            % ("", str(slug_rows[0][1].get("title", ""))[:46], slug, len(slug_hosts),
               ", ".join(sorted(slug_hosts)), DUPE_SLUGS))

    # ------------------------------------------------------------ report ----

    # ---- `date_source`: a real date must say how we know it ----------------------
    for n, item in enumerate(items):
        pub = item.get("published")
        upd = item.get("updated")
        has_real = ((pub and pub != "UNVERIFIED" and DATE.match(str(pub)))
                    or (upd and upd != "UNVERIFIED" and DATE.match(str(upd))))
        src = item.get("date_source")
        if has_real and not src:
            bad(n, item, "carries a real date and no `date_source`. A date whose "
                         "provenance nobody recorded cannot be checked, which is how a "
                         "nine-month error sat in this catalogue unnoticed. Use one of: "
                         + ", ".join(sorted(DATE_SOURCES)))
        elif src and src not in DATE_SOURCES:
            bad(n, item, "`date_source` = %r is not one of %s"
                         % (src, ", ".join(sorted(DATE_SOURCES))))
        elif src and not has_real:
            bad(n, item, "`date_source` = %r but no real date to source. Remove the "
                         "field when the dates are UNVERIFIED." % src)

    # ---- `updated`: a sibling of `published`, never a substitute for it ----------
    # Added 2026-09-05. `published` is when a resource first appeared; `updated` is when
    # its page was last revised. Intercom-templated hosts - the whole Claude Help Center -
    # print only the second, so writing it into `published` made cards state publication
    # dates the page never gave. Three rules keep the two honest:
    #
    #   1. `updated` is a real YYYY-MM-DD or absent. Never "UNVERIFIED": absent already
    #      means "we do not know", and a second spelling of the same idea is a second
    #      thing to keep in step.
    #   2. When both are real, updated >= published. A revision cannot precede the
    #      publication it revises, so the reverse is a data entry error, not a fact.
    #   3. `updated` alone is fine - a page can tell you when it was revised and never
    #      when it appeared, which is exactly the Help Center's shape.
    for n, item in enumerate(items):
        u = item.get("updated")
        if u is None:
            continue
        if u == "UNVERIFIED":
            bad(n, item, "`updated` is 'UNVERIFIED'. Leave the field out instead - "
                         "absent is the honest empty, and two spellings of 'we do "
                         "not know' is one too many.")
            continue
        if not DATE.match(str(u)):
            bad(n, item, "`updated` = %r is not YYYY-MM-DD" % (u,))
            continue
        p = item.get("published")
        if p and p != "UNVERIFIED" and DATE.match(str(p)) and u < p:
            bad(n, item, "`updated` %s is before `published` %s. A revision cannot "
                         "precede what it revises." % (u, p))

    # Both of these are advisory, printed before the verdict and never affecting it.
    report_monotony(items)
    report_typed_numbers(paths_path, UI_JS)

    # See the docstring on role_breadth_warnings for why this can only ever be a warning.
    breadth = role_breadth_warnings(items)
    if breadth:
        print("%d item%s tag 3+ roles while the card text names only one. Breadth is "
              "often right - this is a list to read, not a fault to fix:"
              % (len(breadth), "" if len(breadth) == 1 else "s"))
        for title, kept, others in breadth:
            print("  %-52s card names %-16s also tagged %s"
                  % (title, kept, ", ".join(others)))
        print()

    if not errors and not path_errors and not tier_errors:
        n_paths = (len(json.load(open(paths_path, encoding="utf-8")))
                   if os.path.exists(paths_path) else 0)
        print("%d resources, %d paths — catalogue is valid." % (len(items), n_paths))
        # A stale allowance is not a fault, but it does leave room nobody is using, so
        # say it out loud rather than let the headroom sit there unnoticed.
        if len(claimed) < allowance:
            print("Note: %s allows %d reviewed, %d claim it. Lower it when convenient."
                  % (allowance_path, allowance, len(claimed)))
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
    if tier_errors:
        if errors or path_errors:
            print()
        for e in tier_errors:
            print(e)
    print()
    print("Nothing was changed. Fix the data and run this again.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
