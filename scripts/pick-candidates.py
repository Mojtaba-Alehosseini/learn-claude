#!/usr/bin/env python3
"""
The deterministic half of "Start with these three".

Browse can already narrow 618 resources to the 70 that fit a person. It has never said
which to open first, so the judgment on this site is per-item and nothing is comparative.
This script builds the pool a model is then allowed to choose three from — and it does
that work in plain code, with no model involved, for one reason: a model must never be
able to launder a resource nobody has looked at into a recommendation.

    python3 scripts/pick-candidates.py                     # every cell, with counts
    python3 scripts/pick-candidates.py --cell designer:basic     # the candidates, as JSON

## What "eligible" means, and why each rule is here

  role in item.roles          the cell is a person, not a topic
  item.level == level         exact. A `builder` reading `never-used` material is being
                              sent backwards, and "close enough" is how that happens
  status == "live"            a dead link cannot be a recommendation
  tier != "listed"            `listed` means nobody has looked at the content. We cannot
                              say "open this first" about something we have not opened.
                              This is the rule that makes the pre-filter non-negotiable
  not flagged out of date     the same rule the card prints, and the same definition as
                              LC.effectiveDate in assets/js/ui.js: the LATER of
                              `published` and `updated`, more than 365 days old.
                              `UNVERIFIED` is NOT stale — hundreds of rows publish no date
                              at all and the site says so rather than guessing, so
                              guessing here would contradict the card

## What the picker is told about dates

Every candidate carries `published`, `updated` and `date_source`, so the picker can see
not just when a resource is from but whether we can stand behind that. The rule:

    At equal fit, a dated resource beats an undated one. When that rule decides a slot,
    the reason must say so in one clause.

Equal fit is the whole condition. A better-fitting undated resource still wins - most of
the catalogue is undated, and at `builder` level every single candidate is, so a rule
that preferred dates outright would empty those cells rather than improve them. The
measurement behind that is in scripts/validate-picks.py.

## What this does not do

It does not rank. Ordering the survivors by tier or date would be a quality claim, and
78% of the catalogue is `previewed`, meaning we read an outline. We cannot judge quality
from an outline. What can be judged is fit and order — which three to open first — and
that is a comparative judgment made downstream, then labelled as made by a model.
"""

import argparse
import hashlib
import importlib.util
import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITEMS = os.path.join(ROOT, "data", "items.json")
VALIDATOR = os.path.join(ROOT, "scripts", "validate-catalogue.py")

STALE_DAYS = 365          # matches LC.freshness in assets/js/ui.js

# Order is meaningful and a set cannot carry it: `never-used -> builder` is a progression,
# and sorted() would render it basic, builder, confident, never-used. So the order lives
# here and the MEMBERSHIP is checked against assets/js/ui.js on every run — if a role is
# ever added there and not here, this stops rather than silently skipping a cell.
ROLES = ["non-technical", "student", "researcher", "teacher", "developer", "data-analyst",
         "pm", "designer", "business-founder", "writer-marketer"]
LEVELS = ["never-used", "basic", "confident", "builder"]

# Below this, three-out-of-three is not a judgment, so no picks are made and Browse shows
# the cell as it does today.
MIN_POOL = 4


def _validator():
    spec = importlib.util.spec_from_file_location("validate_catalogue", VALIDATOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def check_vocabulary(mod):
    """Membership only — order is this file's business, the words are ui.js's."""
    vocab = mod.load_vocabularies()
    for name, mine, theirs in (("roles", ROLES, vocab["roles"]),
                               ("levels", LEVELS, vocab["level"])):
        if set(mine) != set(theirs):
            missing = sorted(set(theirs) - set(mine))
            extra = sorted(set(mine) - set(theirs))
            sys.exit("scripts/pick-candidates.py is out of step with assets/js/ui.js on "
                     "%s.\n  in ui.js but not here: %s\n  here but not in ui.js: %s\n"
                     "Fix the list at the top of this file rather than the vocabulary."
                     % (name, missing or "none", extra or "none"))


def effective_date(item):
    """The later of `published` and `updated`, or None if neither is a real date.

    THE freshness rule, and the same one as LC.effectiveDate in assets/js/ui.js - two
    languages, one definition, so they share a name and a note. Change one, change the
    other.

    Age is measured from the later date because that is what the flag is asking: might
    this not match Claude today? A page published in June 2025 and revised in May 2026 is
    not a year stale. Before `updated` existed, one field was doing two jobs and the
    answer was wrong in substance while being right about `published`.
    """
    p = item.get("published")
    u = item.get("updated")
    p = p if p and p != "UNVERIFIED" else None
    u = u if u and u != "UNVERIFIED" else None
    if p and u:
        return max(p, u)
    return p or u


def date_floor(d):
    """A month-only date becomes the first of that month - its oldest possible day.

    "2026-06" is what Coursera prints ("Last update: June 2026") and it is a fact, not a
    broken date. For the staleness question the honest reading is the earliest day it
    could mean, because "never round up" applies to age as much as to precision.
    Mirrors LC.dateFloor in assets/js/ui.js.
    """
    if not d:
        return d
    return d + "-01" if len(d) == 7 else d


def days_old(published, today):
    """None when there is no real date. Not zero, and not infinity — unknown.

    Takes a date string, not an item, so callers that already know which date they mean
    can use it directly. For the freshness question always pass effective_date(item).
    """
    if not published or published == "UNVERIFIED":
        return None
    try:
        y, m, d = (int(x) for x in str(date_floor(published)).split("-"))
    except (ValueError, TypeError):
        return None
    from datetime import date
    return (today - date(y, m, d)).days


def is_eligible(item, role, level, today):
    if role not in (item.get("roles") or []):
        return False
    if item.get("level") != level:
        return False
    if item.get("status") != "live":
        return False
    if item.get("tier") == "listed":
        return False
    age = days_old(effective_date(item), today)
    if age is not None and age > STALE_DAYS:
        return False
    return True


def eligible(items, role, level, today):
    """Sorted by URL, not by relevance. The order here must carry no opinion — the
    comparative judgment happens downstream and must not be quietly pre-seeded by
    whatever order items.json happens to be in."""
    out = [x for x in items if is_eligible(x, role, level, today)]
    return sorted(out, key=lambda x: x["url"])


def fingerprint(pool):
    """Identity of the pool a set of picks was chosen from.

    Membership plus tier. Membership because that is what "the pool" means; tier because
    a pick's reason often leans on it ("the only one anybody has read in full"), so a
    tier change can invalidate a comparative call without changing who is in the room.
    Anything finer would churn on a typo fix in a skip_if and train people to ignore it.
    """
    basis = "\n".join("%s\t%s" % (x["url"], x["tier"]) for x in pool)
    return "sha1:" + hashlib.sha1(basis.encode("utf-8")).hexdigest()[:16]


def card_view(item):
    """What a reader sees on the card, plus one field they do not: the primary topic.

    Deliberately not the whole row. The model is ranking our notes, and handing it fields
    the reader never sees would let it justify a pick with something nobody can check.
    `summary` was missing here until 2026-08-31 and had to be added: it is the most
    prominent field on the rendered card, so leaving it out handed the picker LESS than
    the reader sees, and the audit found reasons resting on facts that live only in the
    summary. Card-answerable has to mean answerable from the card the reader is looking
    at. `notes` stays out, deliberately - it is stripped from the browser mirror, so a
    reason resting on it could never be checked by anyone.

    The one exception is `primary_topic` (topics[0]): constraint 4 in
    scripts/validate-picks.py binds on it, and a picker that cannot see a constraint's
    input can only satisfy it by luck. It is constraint plumbing, not judgment material -
    a reason sentence that leans on it instead of on the card text is a bad reason.
    """
    return {
        "url": item["url"],
        "primary_topic": (item.get("topics") or [None])[0],
        "title": item["title"],
        "summary": item.get("summary", ""),
        "publisher": item.get("source", ""),
        "official": bool(item.get("official")),
        "format": item.get("format"),
        "time": item.get("time"),
        "cost": item.get("cost"),
        "tier": item.get("tier"),
        "who_for": item.get("who_for", ""),
        "skip_if": item.get("skip_if", ""),
        "teaches": item.get("teaches") or [],
        "published": item.get("published"),
        "checked": item.get("checked"),
    }


def load(today=None):
    from datetime import date
    mod = _validator()
    check_vocabulary(mod)
    items = json.load(open(ITEMS, encoding="utf-8"))
    return items, (today or date.today())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cell", help="role:level, e.g. designer:basic")
    ap.add_argument("--compact", action="store_true",
                    help="with --cell: one short block per candidate instead of JSON")
    ap.add_argument("--today", help="YYYY-MM-DD, for reproducible runs")
    args = ap.parse_args()

    from datetime import date
    today = None
    if args.today:
        y, m, d = (int(x) for x in args.today.split("-"))
        today = date(y, m, d)
    items, today = load(today)

    if args.cell:
        role, _, level = args.cell.partition(":")
        if role not in ROLES or level not in LEVELS:
            sys.exit("--cell wants role:level from the vocabulary. Got %r." % args.cell)
        pool = eligible(items, role, level, today)
        if args.compact:
            print("POOL %d  %s  %s|%s" % (len(pool), fingerprint(pool), role, level))
            for x in pool:
                c = card_view(x)
                print()
                print("- %s" % c["title"])
                print("  %s | %s | %s | %s | %s | off=%s | topic=%s | pub=%s"
                      % (c["publisher"], c["format"], c["time"], c["cost"], c["tier"],
                         "T" if c["official"] else "F", c["primary_topic"],
                         c["published"] or "?"))
                print("  W: %s" % c["who_for"])
                print("  S: %s" % c["skip_if"])
            return 0
        json.dump({
            "cell": "%s|%s" % (role, level),
            "role": role,
            "level": level,
            "pool_size": len(pool),
            "fingerprint": fingerprint(pool),
            "candidates": [card_view(x) for x in pool],
        }, sys.stdout, indent=2, ensure_ascii=False)
        print()
        return 0

    decide, thin, empty = [], [], []
    print("%-18s %s" % ("", "  ".join("%-12s" % l for l in LEVELS)))
    for role in ROLES:
        row = []
        for level in LEVELS:
            n = len(eligible(items, role, level, today))
            row.append("%-12s" % (n if n else "-"))
            cell = "%s|%s" % (role, level)
            (empty if n == 0 else thin if n < MIN_POOL else decide).append((cell, n))
        print("%-18s %s" % (role, "  ".join(row)))

    print()
    print("%d cells need a decision (pool of %d or more)" % (len(decide), MIN_POOL))
    print("%d have three or fewer candidates — shown as-is, no picks: %s"
          % (len(thin), ", ".join("%s (%d)" % c for c in thin) or "none"))
    print("%d empty: %s" % (len(empty), ", ".join(c for c, _ in empty) or "none"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
