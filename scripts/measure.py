#!/usr/bin/env python3
"""
Every number the documentation quotes, computed from data/ rather than typed.

    python3 scripts/measure.py              # human-readable, to stdout
    python3 scripts/measure.py --status     # write docs/STATUS.md
    python3 scripts/measure.py --json       # the same figures as JSON

## Why this exists

Hand-written counts have rotted twice in three rounds, and both times the rule against
it was already written down. On 2026-08-31 START-HERE.md was cut back to a pointer
because it still said "353 resources, 3 paths" months after both were wrong, and the fix
came with a line saying counts live in THE-PROJECT.md because a second copy of a figure
is how one stale file becomes two. Four days later THE-PROJECT.md and README were
themselves stale by twenty rows, one round after that sentence was written.

So discipline is not the fix. The fix is that no number in the documentation is typed by
a person. THE-PROJECT.md part 3 and README's "Where it stands" now point at
docs/STATUS.md, which this script writes and build.sh regenerates.

Historical numbers stay written by hand, in THE-PROJECT.md part 9 - "the catalogue went
from 354 to 618 after duplicate merges" describes what a past run did and is not a claim
about today. The test is whether the sentence would become false as data changes.
"""

import argparse
import importlib.util
import io
import json
import os
import re
import sys
from collections import Counter
from datetime import date

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITEMS = os.path.join(ROOT, "data", "items.json")
PATHS = os.path.join(ROOT, "data", "paths.json")
PICKS = os.path.join(ROOT, "data", "picks.json")
LINKS = os.path.join(ROOT, "data", "link-check.json")
STATUS = os.path.join(ROOT, "docs", "STATUS.md")


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def measure(today=None):
    pc = _load("pick_candidates", os.path.join(ROOT, "scripts", "pick-candidates.py"))
    today = today or date.today()
    items = json.load(io.open(ITEMS, encoding="utf-8"))
    paths = json.load(io.open(PATHS, encoding="utf-8"))
    picks = json.load(io.open(PICKS, encoding="utf-8"))["cells"]
    n = len(items)

    cells, thin, empty, zero_indep, pubthin = {}, [], [], [], []
    for role in pc.ROLES:
        for level in pc.LEVELS:
            pool = pc.eligible(items, role, level, today)
            key = "%s|%s" % (role, level)
            pubs = {x.get("source", "") for x in pool}
            indep = sum(1 for x in pool if not x.get("official"))
            cells[key] = {"eligible": len(pool), "publishers": len(pubs),
                          "non_anthropic": indep, "picked": key in picks}
            if not pool:
                empty.append(key)
            elif len(pool) < pc.MIN_POOL:
                thin.append((key, len(pool)))
            if pool and indep == 0:
                zero_indep.append((key, len(pool), len(pubs)))
            if pool and len(pubs) < 3:
                pubthin.append((key, len(pubs), len(pool)))

    # Live resources the freshness rule keeps out of every pool. Silent exclusion is how
    # a good resource disappeared for ten months without one step going red.
    excluded = []
    for it in items:
        if it.get("status") != "live" or it.get("tier") == "listed":
            continue
        age = pc.days_old(pc.effective_date(it), today)
        if age is not None and age > pc.STALE_DAYS:
            excluded.append({"title": it["title"], "url": it["url"],
                             "published": it.get("published"),
                             "updated": it.get("updated"), "days": age,
                             "source": it.get("source", ""),
                             "roles": it.get("roles", []), "level": it.get("level")})
    excluded.sort(key=lambda x: -x["days"])

    # Rows whose date was dropped because no machine could read the page. Each needs a
    # person to open it once; until then the catalogue says it does not know.
    unreadable = []
    for it in items:
        note = it.get("notes") or ""
        if "cannot be read by machine" in note or "security challenge" in note \
                or "no extractable text" in note:
            m = re.search(r"the stored published date (\S+) could not be confirmed", note)
            unreadable.append({"title": it["title"], "url": it["url"],
                               "dropped": m.group(1) if m else "unknown",
                               "source": it.get("source", "")})

    # Resources back in the pools not because they got newer but because the evidence
    # for their date was lost. The honest cost of "never round up".
    re_entered = []
    for it in items:
        note = it.get("notes") or ""
        if "cannot be read by machine" in note and it.get("published") == "UNVERIFIED":
            m = re.search(r"the stored published date (\S+)", note)
            old_date = m.group(1) if m else None
            if old_date and pc.days_old(old_date, today) and \
                    pc.days_old(old_date, today) > pc.STALE_DAYS:
                re_entered.append({"title": it["title"], "url": it["url"],
                                   "was": old_date,
                                   "days": pc.days_old(old_date, today)})

    link = {}
    if os.path.exists(LINKS):
        try:
            raw = json.load(io.open(LINKS, encoding="utf-8"))
            link = {"when": raw.get("when"), "counts": raw.get("counts", {}),
                    "blocked": raw.get("blocked", [])}
        except Exception:
            link = {}

    return {
        "generated": str(today),
        "resources": n,
        "paths": len(paths),
        "path_steps": sum(len(p.get("steps", [])) for p in paths),
        "publishers": len({i.get("source", "") for i in items}),
        "hosts": len({i["url"].split("/")[2].replace("www.", "") for i in items}),
        "tier": dict(Counter(i["tier"] for i in items)),
        "format": dict(Counter(i["format"] for i in items)),
        "level": dict(Counter(i["level"] for i in items)),
        "cost": dict(Counter(i["cost"] for i in items)),
        "status": dict(Counter(i["status"] for i in items)),
        "official": sum(1 for i in items if i.get("official")),
        "unverified": sum(1 for i in items if i.get("published") == "UNVERIFIED"),
        "with_updated": sum(1 for i in items if i.get("updated")),
        "date_source": dict(Counter(i.get("date_source") or "(none)" for i in items)),
        "cells": cells,
        "cells_with_picks": len(picks),
        "picks": sum(len(c["picks"]) for c in picks.values()),
        "runners_up": sum(len(c["runners_up"]) for c in picks.values()),
        "thin_cells": thin,
        "empty_cells": empty,
        "zero_non_anthropic": zero_indep,
        "publisher_thin": pubthin,
        "excluded_by_freshness": excluded,
        "unreadable_by_machine": unreadable,
        "re_entered_on_lost_evidence": re_entered,
        "link_check": link,
    }


def pct(a, b):
    return 0 if not b else round(100.0 * a / b)


def render(m, pc):
    L = []
    w = L.append
    w("<!-- GENERATED by scripts/measure.py. Do not edit by hand: build.sh overwrites")
    w("     this file, and a number typed here would be silently replaced. Change the")
    w("     data, then run ./build.sh. -->")
    w("")
    w("# Status — measured %s" % m["generated"])
    w("")
    w("Every figure below is computed from `data/` at build time. Nothing here is typed.")
    w("THE-PROJECT.md and README point at this file rather than repeating it.")
    w("")
    w("## The catalogue")
    w("")
    w("| | |")
    w("|---|---|")
    w("| Resources | **%d** |" % m["resources"])
    w("| Distinct publishers | %d |" % m["publishers"])
    w("| Distinct hosts | %d |" % m["hosts"])
    w("| Learning paths | **%d**, %d steps |" % (m["paths"], m["path_steps"]))
    w("| Anthropic's own | %d of %d — **%d%%** |"
      % (m["official"], m["resources"], pct(m["official"], m["resources"])))
    w("| No publish date (`UNVERIFIED`) | %d of %d — %d%% |"
      % (m["unverified"], m["resources"], pct(m["unverified"], m["resources"])))
    w("| Carrying an `updated` date | %d of %d — %d%% |"
      % (m["with_updated"], m["resources"], pct(m["with_updated"], m["resources"])))
    w("")
    w("**Where every date came from.** `date_source` is required on any row carrying a")
    w("real date; a row with no date needs none, because \"we do not know\" is the whole")
    w("statement.")
    w("")
    w("| how we know | count |")
    w("|---|---|")
    for key, label in (("printed", "a person read it on the page"),
                       ("metadata", "parsed from JSON-LD or a meta tag"),
                       ("upload", "a video platform's upload date"),
                       ("intercom", "the Help Center's template"),
                       ("(none)", "no real date — `UNVERIFIED`")):
        w("| `%s` — %s | %d |" % (key, label, m["date_source"].get(key, 0)))
    w("")
    w("**How thoroughly we have checked**")
    w("")
    w("| level | shown as | count | share |")
    w("|---|---|---|---|")
    for key, label in (("reviewed", "Read in full"), ("ai-reviewed", "Read by AI"),
                       ("previewed", "Skimmed"), ("listed", "Found only")):
        c = m["tier"].get(key, 0)
        w("| `%s` | %s | **%d** | %d%% |" % (key, label, c, pct(c, m["resources"])))
    w("")
    for name, key in (("Format", "format"), ("Level", "level"), ("Cost", "cost"),
                      ("Status", "status")):
        parts = ["%d %s" % (v, k) for k, v in
                 sorted(m[key].items(), key=lambda kv: -kv[1])]
        w("**%s:** %s." % (name, " · ".join(parts)))
        w("")

    w("## \"Start with these three\"")
    w("")
    w("| | |")
    w("|---|---|")
    w("| Cells with picks | **%d** of 40 |" % m["cells_with_picks"])
    w("| Picks | %d |" % m["picks"])
    w("| Runners-up recorded | %d |" % m["runners_up"])
    w("")
    w("**Cells with three or fewer candidates** (shown as-is, no picks): %s"
      % (", ".join("`%s` (%d)" % t for t in m["thin_cells"]) or "none"))
    w("")
    w("**Empty cells:** %s" % (", ".join("`%s`" % c for c in m["empty_cells"]) or "none"))
    w("")
    w("**Pools with zero non-Anthropic material:** %s"
      % (", ".join("`%s` (%d items, %d publisher%s)"
                   % (k, n, p, "" if p == 1 else "s")
                   for k, n, p in m["zero_non_anthropic"]) or "none"))
    w("")
    w("**Publisher-thin pools** (fewer than 3 publishers, so the no-two-from-one rule")
    w("relaxes): %s"
      % (", ".join("`%s` (%d pub, %d items)" % t for t in m["publisher_thin"]) or "none"))
    w("")

    w("## Per cell — eligible / publishers / non-Anthropic")
    w("")
    w("| role | %s |" % " | ".join(pc.LEVELS))
    w("|---|%s" % ("---|" * len(pc.LEVELS)))
    for role in pc.ROLES:
        row = []
        for level in pc.LEVELS:
            c = m["cells"]["%s|%s" % (role, level)]
            row.append("%d / %dp / %dx" % (c["eligible"], c["publishers"],
                                           c["non_anthropic"]))
        w("| `%s` | %s |" % (role, " | ".join(row)))
    w("")

    w("## Live resources the freshness rule excludes from every pool")
    w("")
    w("A real `published` date more than %d days old. These still appear in Browse with"
      % pc.STALE_DAYS)
    w("the outdated flag; they are kept out of \"Start with these three\" because a")
    w("comparative recommendation should not point at something a year stale.")
    w("")
    w("**%d excluded.**" % len(m["excluded_by_freshness"]))
    w("")
    if m["excluded_by_freshness"]:
        w("| item | publisher | published | days | level |")
        w("|---|---|---|---|---|")
        for e in m["excluded_by_freshness"]:
            w("| %s | %s | %s | %d | %s |"
              % (e["title"][:58].replace("|", "\\|"), e["source"][:24],
                 e["published"], e["days"], e["level"]))
        w("")

    w("## Needs a person")
    w("")
    w("Everything below is generated from `data/`. It is the half of the backlog a")
    w("machine can see; the other half — the standing items no data can reveal — is in")
    w("[THE-PROJECT.md part 10](THE-PROJECT.md). Two halves, one list, no third copy.")
    w("")

    w("### Pages no machine can read (%d)" % len(m["unreadable_by_machine"]))
    w("")
    w("Their host refuses automated requests or serves a challenge, so the date we held")
    w("could not be confirmed and was dropped. One visit each settles it.")
    w("")
    if m["unreadable_by_machine"]:
        w("| item | publisher | date dropped | url |")
        w("|---|---|---|---|")
        for r in m["unreadable_by_machine"]:
            w("| %s | %s | %s | %s |"
              % (r["title"][:48].replace("|", "\\|"), r["source"][:22], r["dropped"],
                 r["url"]))
        w("")

    w("### Hosts that block the weekly check (%d items)"
      % sum(b.get("count", 0) for b in (m["link_check"].get("blocked") or [])))
    w("")
    w("A bot-wall is not evidence a page is dead. These can only ever be confirmed by a")
    w("person, and the date beside each is the last time one did.")
    w("")
    if (m["link_check"].get("blocked") or []):
        w("| host | items | last confirmed by a person |")
        w("|---|---|---|")
        for b in m["link_check"]["blocked"]:
            w("| %s | %s | %s |" % (b.get("host"), b.get("count"),
                                    b.get("last_human_check", "never")))
        w("")

    w("### Back in the pools because we lost the evidence (%d)"
      % len(m["re_entered_on_lost_evidence"]))
    w("")
    w("These are old. They are candidates again not because they were revised but")
    w("because their date could not be confirmed, and `UNVERIFIED` is deliberately not")
    w("stale. Opening one either restores its date or confirms it should go.")
    w("")
    if m["re_entered_on_lost_evidence"]:
        w("| item | date we had | age it implied |")
        w("|---|---|---|")
        for r in m["re_entered_on_lost_evidence"]:
            w("| %s | %s | %d days |"
              % (r["title"][:52].replace("|", "\\|"), r["was"], r["days"]))
        w("")

    w("### Cells with no independent material (%d)" % len(m["zero_non_anthropic"]))
    w("")
    w("Every candidate is Anthropic's own. No constraint can fix this; only material can.")
    w("")
    if m["zero_non_anthropic"]:
        w("| cell | items | publishers |")
        w("|---|---|---|")
        for k, n, p in m["zero_non_anthropic"]:
            w("| `%s` | %d | %d |" % (k.replace("|", "\\|"), n, p))
        w("")

    w("### Empty cells (%d)" % len(m["empty_cells"]))
    w("")
    w("A reader who answers both questions this way is told we have nothing. %s"
      % (", ".join("`%s`" % c.replace("|", "\\|") for c in m["empty_cells"])
         or "None — every combination has something."))
    w("")

    w("## Links")
    w("")
    lk = m["link_check"]
    if lk and lk.get("counts"):
        c = lk["counts"]
        w("Last full check: **%s**." % (lk.get("when") or "unknown"))
        w("")
        w("| verdict | count |")
        w("|---|---|")
        for k in ("ok", "moved", "blocked", "gone", "wobbly"):
            if k in c:
                w("| %s | %d |" % (k, c[k]))
        w("")
        if lk.get("blocked"):
            w("**Blocked hosts are unverifiable by machine** — they refuse automated")
            w("requests, so a bot-wall is not evidence a page is dead. Each was last")
            w("confirmed by a person on the date shown.")
            w("")
            w("| host | items | last confirmed by a person |")
            w("|---|---|---|")
            for b in lk["blocked"]:
                w("| %s | %s | %s |" % (b.get("host"), b.get("count"),
                                        b.get("last_human_check", "never")))
            w("")
    else:
        w("No machine-readable link report yet. Run:")
        w("")
        w("    python3 scripts/check-links.py --json data/link-check.json")
        w("")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", action="store_true", help="write docs/STATUS.md")
    ap.add_argument("--json", action="store_true", help="print the figures as JSON")
    args = ap.parse_args()

    pc = _load("pick_candidates", os.path.join(ROOT, "scripts", "pick-candidates.py"))
    m = measure()

    if args.json:
        json.dump(m, sys.stdout, indent=2, ensure_ascii=False)
        print()
        return 0

    text = render(m, pc)
    if args.status:
        io.open(STATUS, "w", encoding="utf-8", newline="\n").write(text)
        print("  docs/STATUS.md  %d resources, %d cells with picks, %d excluded by "
              "freshness" % (m["resources"], m["cells_with_picks"],
                             len(m["excluded_by_freshness"])))
        if m["excluded_by_freshness"]:
            print("  freshness excludes these live resources from every picks pool:")
            for e in m["excluded_by_freshness"]:
                print("    %-58s %s  %4d days  %s"
                      % (e["title"][:58], e["published"], e["days"], e["source"][:22]))
        return 0

    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
