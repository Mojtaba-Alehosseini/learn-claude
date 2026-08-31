#!/usr/bin/env python3
"""
Validate data/picks.json — the "Start with these three" blocks — before anything ships.

The picks are a model's comparative judgment over the catalogue's own notes, made once
and committed. Two different things can go wrong with a committed judgment, and they
have different severities:

  STALE (warn, still ships)   The pool a cell was judged against has changed — grown,
                              shrunk, an item re-tiered. The picks are still real picks
                              of real resources; they are just dated, and the card says
                              when they were made. Re-picking needs a model run that CI
                              cannot do, so the build warns, names the cells, and ships.

  WRONG (error, build fails)  A picked URL is dead, gone from the catalogue, or no
                              longer passes the pre-filter in scripts/pick-candidates.py
                              (role/level drifted, tier dropped to `listed`, published
                              date aged past the freshness rule). A dead or ineligible
                              pick must never ship — "open this one first" about a page
                              nobody can open is the site lying in its own voice.

    python3 scripts/validate-picks.py                      # the real files
    python3 scripts/validate-picks.py <items.json> <picks.json>   # for the tests

## The four constraints, and how each degrades

Checked here in code, not trusted from the picking step — the picker is re-asked until
these pass, and this file is what "pass" means:

  1. publishers   No two picks from one publisher. Degrades only when the pool itself
                  has fewer than 3 publishers: then at most 2 from one publisher, and a
                  1-publisher pool caps the cell at 2 picks. Never 3 from one publisher
                  — that is the monoculture the rule exists to stop, and a pool that IS
                  a monoculture gets fewer picks, not a silent exception.
  2. official     At least one non-Anthropic pick whenever the pool offers one.
  3. formats      All distinct, where the pool allows it: required distinct formats =
                  min(pick count, distinct formats in pool).
  4. topics       On topics[0], and NOT the same shape as 3, because the data will not
                  carry it: measured 2026-08-31, every eligible pool is 30-90% dominated
                  by one primary topic (chat-prompting at basic levels, cowork or
                  claude-code at builder), so demanding distinct primaries would
                  systematically force worse-fitting picks in to satisfy a field. The
                  approved checkpoint cells themselves share primaries. So the rule is
                  fire-and-justify: two picks sharing a primary topic is an ERROR unless
                  the cell stores a justification in its `note` saying why the clash is
                  subjects, not sameness — the same swap-or-justify mechanism as the
                  model-level subject self-check, held in code. Where the pool has fewer
                  distinct primaries than picks, the clash is forced and needs no note.
                  Either way it is printed on every run. A "Claude Design" cluster still
                  hides inside one topic — that is what the subject self-check is for;
                  code checks what code can see and makes the rest auditable.

The publisher-thin cells are printed on every run, pass or fail. The relaxation must
never be silent: a cell running under the cap is a fact about the catalogue (the pool
is a near-monoculture), and hiding it would hide exactly what constraint 1 measures.
"""

import importlib.util
import json
import os
import re
import sys
from datetime import date

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITEMS = os.path.join(ROOT, "data", "items.json")
PICKS = os.path.join(ROOT, "data", "picks.json")

DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _pick_candidates():
    path = os.path.join(ROOT, "scripts", "pick-candidates.py")
    spec = importlib.util.spec_from_file_location("pick_candidates", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


PC = _pick_candidates()


def allowed_picks(pool):
    """(max from one publisher, required pick count) for this pool.

    3 picks normally. A 2-publisher pool still gets 3 (2+1). A 1-publisher pool gets 2 —
    the cap is the constraint holding its ground, not the cell being punished.
    """
    pubs = {x.get("source", "") for x in pool}
    if len(pubs) >= 3:
        return 1, 3          # every pick from a different publisher
    if len(pubs) == 2:
        return 2, 3
    return 2, 2


def check_cell(key, cell, pool, items_by_url):
    """One cell against one pool. Returns (errors, warns, notes) — strings, prefixed."""
    errors, warns, notes = [], [], []

    def err(msg):
        errors.append("  %-28s %s" % (key, msg))

    def warn(msg):
        warns.append("  %-28s %s" % (key, msg))

    picks = cell.get("picks") or []
    runners = cell.get("runners_up") or []

    # Label. Nothing may imply a person chose; "ai" is the only value with an allowance.
    if cell.get("picked_by") != "ai":
        err("picked_by is %r — the only authorised value is \"ai\". A human promotion "
            "path starts at an allowance of 0, like `reviewed`." % cell.get("picked_by"))
    if not DATE.match(str(cell.get("picked_on") or "")):
        err("picked_on = %r is not YYYY-MM-DD" % cell.get("picked_on"))
    if not str(cell.get("fingerprint") or "").startswith("sha1:"):
        err("fingerprint is missing — staleness cannot be detected without it")

    # Every pick: exists, live, eligible, carries its sentence and its subject.
    pick_items = []
    for p in picks:
        u = p.get("url")
        it = items_by_url.get(u)
        if it is None:
            err("pick %s is not in the catalogue" % u)
            continue
        pick_items.append(it)
        if it.get("status") != "live":
            err("pick %r has status %r — a dead pick must never ship"
                % (it["title"][:40], it.get("status")))
        role, level = cell.get("role"), cell.get("level")
        if not PC.is_eligible(it, role, level, date.today()):
            err("pick %r no longer passes the pre-filter for %s|%s (tier %s, "
                "published %s) — re-pick this cell"
                % (it["title"][:40], role, level, it.get("tier"), it.get("published")))
        if len(str(p.get("reason") or "").strip()) < 20:
            err("pick %s has no working reason sentence" % u)
        if not str(p.get("subject") or "").strip():
            err("pick %s has no subject line — the self-check cannot have run" % u)

    # Runners-up: the falsifiability record. 2 or 3, each with a reason.
    if not 2 <= len(runners) <= 3:
        err("%d runners-up recorded — the record of what lost needs 2 or 3"
            % len(runners))
    for r in runners:
        if r.get("url") not in items_by_url:
            err("runner-up %s is not in the catalogue" % r.get("url"))
        if len(str(r.get("reason") or "").strip()) < 20:
            err("runner-up %s has no reason for losing" % r.get("url"))

    # The four constraints, against what the pool allows.
    if pick_items and pool:
        max_per_pub, want_count = allowed_picks(pool)
        pool_pubs = {x.get("source", "") for x in pool}

        if len(picks) != want_count:
            err("%d picks where this pool requires %d (%d publisher%s in pool)"
                % (len(picks), want_count, len(pool_pubs),
                   "" if len(pool_pubs) == 1 else "s"))

        by_pub = {}
        for it in pick_items:
            by_pub.setdefault(it.get("source", ""), []).append(it)
        for pub, group in by_pub.items():
            if len(group) > max_per_pub:
                err("%d picks from %r where this pool allows %d per publisher"
                    % (len(group), pub, max_per_pub))
        if len(pool_pubs) < 3:
            notes.append("  %-28s publisher-thin pool: %d publisher%s, cap is %d per "
                         "publisher, %d picks" % (key, len(pool_pubs),
                         "" if len(pool_pubs) == 1 else "s", max_per_pub, want_count))

        if any(not x.get("official") for x in pool) and \
           all(it.get("official") for it in pick_items):
            err("every pick is official Anthropic and the pool offers %d that are not"
                % sum(1 for x in pool if not x.get("official")))

        of_fmt = lambda x: x.get("format")
        in_pool = {of_fmt(x) for x in pool}
        in_picks = [of_fmt(it) for it in pick_items]
        want = min(len(pick_items), len(in_pool))
        if len(set(in_picks)) < want:
            err("picks span %d formats where the pool offers %d and %d picks could "
                "span %d" % (len(set(in_picks)), len(in_pool), len(pick_items), want))

        # Constraint 4. Shared primary topic: justified, forced, or a fault.
        prim = lambda x: (x.get("topics") or [None])[0]
        pick_prims = [prim(it) for it in pick_items]
        shared = sorted({t for t in pick_prims if pick_prims.count(t) > 1})
        if shared:
            pool_prims = {prim(x) for x in pool}
            forced = len(pool_prims) < len(pick_items)
            note = str(cell.get("note") or "").strip()
            if forced:
                notes.append("  %-28s picks share primary topic %s — forced, the pool "
                             "has only %d distinct" % (key, "/".join(shared),
                                                       len(pool_prims)))
            elif len(note) >= 20:
                notes.append("  %-28s picks share primary topic %s — justified: %s"
                             % (key, "/".join(shared), note[:90]))
            else:
                err("two or more picks share primary topic %s and the cell carries no "
                    "justification — swap a pick, or say in `note` why the clash is "
                    "different subjects rather than sameness" % "/".join(shared))

    # Staleness — the honest kind. Warn, name it, ship it.
    if pool and cell.get("fingerprint") and \
       cell.get("fingerprint") == PC.fingerprint(pool):
        pass
    elif pool:
        warn("stale: the eligible pool has changed since these were picked on %s "
             "(%d candidates now). The picks still ship — the card carries the date — "
             "but this cell wants a re-pick." % (cell.get("picked_on"), len(pool)))
    if pool and len(pool) < PC.MIN_POOL:
        warn("stale: the pool has shrunk to %d, below the %d this feature requires. "
             "These picks should be retired, not re-picked." % (len(pool), PC.MIN_POOL))

    return errors, warns, notes


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    items_path = argv[0] if len(argv) > 0 else ITEMS
    picks_path = argv[1] if len(argv) > 1 else PICKS

    if not os.path.exists(picks_path):
        print("No %s yet — nothing to validate." % picks_path)
        return 0

    items = json.load(open(items_path, encoding="utf-8"))
    picks = json.load(open(picks_path, encoding="utf-8"))
    items_by_url = {x["url"]: x for x in items}
    today = date.today()

    errors, warns, notes = [], [], []
    cells = picks.get("cells") or {}

    for key, cell in sorted(cells.items()):
        role, _, level = key.partition("|")
        if role not in PC.ROLES or level not in PC.LEVELS:
            errors.append("  %-28s not a role|level from the vocabulary" % key)
            continue
        if cell.get("role") != role or cell.get("level") != level:
            errors.append("  %-28s key and body disagree on role/level" % key)
        pool = PC.eligible(items, role, level, today)
        e, w, n = check_cell(key, cell, pool, items_by_url)
        errors += e
        warns += w
        notes += n

    # The other direction: a cell that needs a decision and has none. New material can
    # open a cell (student|builder is empty today and will not always be). Warn — picking
    # needs a model run, and an absent block is the pre-feature state, not a lie.
    for role in PC.ROLES:
        for level in PC.LEVELS:
            key = "%s|%s" % (role, level)
            if key in cells:
                continue
            pool = PC.eligible(items, role, level, today)
            if len(pool) >= PC.MIN_POOL:
                warns.append("  %-28s %d candidates and no picks — this cell needs a "
                             "model run" % (key, len(pool)))

    for n in notes:
        print("note:" + n)
    if warns:
        print("%d cell%s stale or unpicked (the build still ships — picks carry their "
              "date):" % (len(warns), "" if len(warns) == 1 else "s"))
        for w in warns:
            print(w)
    if errors:
        if warns or notes:
            print()
        print("%d fault%s in %s:" % (len(errors), "" if len(errors) == 1 else "s",
                                     picks_path))
        for e in errors:
            print(e)
        print()
        print("A wrong pick must never ship. Fix the picks and run this again.")
        return 1

    print("%d cell%s of picks — all picks live, eligible and within constraint."
          % (len(cells), "" if len(cells) == 1 else "s"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
