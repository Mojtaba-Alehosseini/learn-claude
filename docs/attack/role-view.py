#!/usr/bin/env python3
"""
Show exactly what one role is given, in the order Browse puts it on screen.

Written for the attack exercise so that ten agents quote the cards a visitor is really
shown rather than whichever ones they happened to scroll past. It reproduces the default
"Best checked first" sort from assets/js/browse.js:111-113 — tier rank, then most
recently checked, then title — so row 1 here is the first card on the page.

    python3 docs/attack/role-view.py <role> [level]
    python3 docs/attack/role-view.py designer never-used
    python3 docs/attack/role-view.py pm --counts

Reads data/items.json, which was checked byte-for-byte against the deployed
data/items.js on 2026-08-27 and is identical.
"""

import collections
import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ITEMS = os.path.join(ROOT, "data", "items.json")

# assets/js/ui.js LC.TIER — order is meaningful, most thoroughly checked first.
TIER_RANK = {"reviewed": 0, "ai-reviewed": 1, "previewed": 2, "listed": 3}
TIER_LABEL = {"reviewed": "Read in full", "ai-reviewed": "Read by AI",
              "previewed": "Skimmed", "listed": "Found only"}
LEVELS = ["never-used", "basic", "confident", "builder"]


def load():
    return json.load(open(ITEMS, encoding="utf-8"))


def for_role(items, role, level=None):
    out = [i for i in items if role in i.get("roles", [])]
    if level:
        out = [i for i in out if i.get("level") == level]
    # browse.js:111-113, default sort
    out.sort(key=lambda i: (TIER_RANK.get(i.get("tier"), 9),
                            [-ord(c) for c in (i.get("checked") or "")],
                            i.get("title", "")))
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    if not args:
        raise SystemExit(__doc__)
    role = args[0]
    level = args[1] if len(args) > 1 else None
    items = load()

    if role not in {r for i in items for r in i.get("roles", [])}:
        raise SystemExit("No such role: %s" % role)

    if "--counts" in flags:
        all_for_role = for_role(items, role)
        print("%s: %d total" % (role, len(all_for_role)))
        by_level = collections.Counter(i["level"] for i in all_for_role)
        for lv in LEVELS:
            print("  %-12s %3d" % (lv, by_level.get(lv, 0)))
        print("  tiers:   %s" % dict(collections.Counter(i["tier"] for i in all_for_role)))
        print("  formats: %s" % dict(collections.Counter(i["format"] for i in all_for_role)))
        print("  free:    %d" % sum(1 for i in all_for_role if i["cost"] == "free"))
        print("  no date: %d" % sum(1 for i in all_for_role
                                    if i.get("published") == "UNVERIFIED"))
        print("  only this role: %d" % sum(1 for i in all_for_role if len(i["roles"]) == 1))
        return

    rows = for_role(items, role, level)
    print("%s%s — %d card%s, in the order Browse shows them"
          % (role, (" / " + level) if level else "", len(rows), "" if len(rows) == 1 else "s"))
    print()
    for n, i in enumerate(rows, 1):
        print("%2d. [%s] %s" % (n, TIER_LABEL.get(i["tier"], i["tier"]), i["title"]))
        print("    %s · %s · %s · %s · checked %s · published %s"
              % (i["source"], i["format"], i["time"], i["cost"], i["checked"],
                 i.get("published")))
        print("    For:     %s" % i["who_for"])
        print("    Skip if: %s" % i["skip_if"])
        print("    %s" % i["url"])
        print()


if __name__ == "__main__":
    main()
