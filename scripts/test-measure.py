#!/usr/bin/env python3
"""
Prove scripts/measure.py's output is what it claims to be.

    python3 scripts/test-measure.py

## Why this file exists

measure.py is the file everything else quotes. THE-PROJECT.md part 3 and README's
"Where it stands" are pointers to the STATUS.md it writes, so a wrong number here becomes
a wrong number in every document at once, silently, on the next build.

It has already happened. On 2026-09-05 a loop added to `measure()` reused the name `n`
for a notes string; `n` already held the row count, so `"resources"` came out as a
sentence of prose. Nothing caught it until a `%d` format raised a TypeError three
functions later — and had that key been rendered with `%s` instead, STATUS.md would have
published a paragraph of notes where the catalogue size belongs and no step would have
gone red.

So this checks three things a shadowed name or a wrong type cannot survive:

  1. **Types.** Every count is an int, every ratio is an int, every date is a string that
     parses. A string where a number belongs fails here rather than in a format string.
  2. **Partitions sum.** Tier, level, format, cost and status each partition the whole
     catalogue, so each must total the row count exactly. `date_source` partitions the
     rows carrying a real date, so it must total those. A bucket that does not add up
     means a row was counted twice, dropped, or classified into a value nobody declared.
  3. **Internal agreement.** The per-cell grid, the picks totals and the derived lists
     have to agree with the raw catalogue rather than with each other.

None of this validates the catalogue — that is validate-catalogue.py's job. This asks
only whether measure.py described it correctly.
"""

import importlib.util
import io
import json
import os
import sys
from datetime import date

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Every key that must be a plain non-negative integer.
INT_KEYS = ("resources", "paths", "path_steps", "publishers", "hosts", "official",
            "unverified", "with_updated", "cells_with_picks", "picks", "runners_up")

# Buckets that partition the whole catalogue: each must sum to `resources`.
WHOLE_PARTITIONS = ("tier", "format", "level", "cost", "status")


def main():
    m_mod = load("measure", os.path.join(ROOT, "scripts", "measure.py"))
    pc = load("pick_candidates", os.path.join(ROOT, "scripts", "pick-candidates.py"))
    items = json.load(io.open(os.path.join(ROOT, "data", "items.json"),
                              encoding="utf-8"))
    m = m_mod.measure()
    n = len(items)
    fails = []

    def check(ok, msg):
        if ok:
            print("ok    " + msg)
        else:
            print("FAIL  " + msg)
            fails.append(msg)

    # ---- 1. types -------------------------------------------------------------
    bad_types = [(k, type(m.get(k)).__name__) for k in INT_KEYS
                 if not isinstance(m.get(k), int) or isinstance(m.get(k), bool)]
    check(not bad_types,
          "every count is an int (%s)" % (bad_types or "%d keys" % len(INT_KEYS)))

    neg = [k for k in INT_KEYS if isinstance(m.get(k), int) and m[k] < 0]
    check(not neg, "no count is negative")

    gen = m.get("generated")
    ok_gen = isinstance(gen, str)
    if ok_gen:
        try:
            date(*(int(x) for x in gen.split("-")))
        except Exception:                                # noqa: BLE001
            ok_gen = False
    check(ok_gen, "`generated` is a parseable date string (%r)" % gen)

    for key in WHOLE_PARTITIONS + ("date_source",):
        d = m.get(key)
        ok = isinstance(d, dict) and all(isinstance(v, int) for v in d.values())
        check(ok, "`%s` is a dict of ints" % key)

    # ---- 2. partitions sum ----------------------------------------------------
    for key in WHOLE_PARTITIONS:
        total = sum(m[key].values())
        check(total == n, "`%s` sums to the catalogue (%d of %d)" % (key, total, n))

    ds_total = sum(m["date_source"].values())
    check(ds_total == n,
          "`date_source` (including \"(none)\") covers every row (%d of %d)"
          % (ds_total, n))

    dated = sum(1 for i in items
                if (i.get("published") not in (None, "UNVERIFIED"))
                or (i.get("updated") not in (None, "UNVERIFIED")))
    sourced = ds_total - m["date_source"].get("(none)", 0)
    check(sourced == dated,
          "rows with a real date equal rows with a `date_source` (%d vs %d)"
          % (sourced, dated))

    # ---- 3. internal agreement -------------------------------------------------
    check(m["resources"] == n, "`resources` matches items.json (%d)" % m["resources"])
    check(m["official"] == sum(1 for i in items if i.get("official")),
          "`official` matches a direct count")
    check(m["unverified"] == sum(1 for i in items
                                 if i.get("published") == "UNVERIFIED"),
          "`unverified` matches a direct count")
    check(m["with_updated"] == sum(1 for i in items if i.get("updated")),
          "`with_updated` matches a direct count")

    cells = m["cells"]
    check(len(cells) == len(pc.ROLES) * len(pc.LEVELS),
          "the cell grid is %d x %d = %d cells"
          % (len(pc.ROLES), len(pc.LEVELS), len(cells)))

    today = date.today()
    role, level = pc.ROLES[0], pc.LEVELS[0]
    live = len(pc.eligible(items, role, level, today))
    check(cells["%s|%s" % (role, level)]["eligible"] == live,
          "a sampled cell matches pick-candidates (%s|%s = %d)" % (role, level, live))

    check(all(isinstance(c["eligible"], int) and isinstance(c["publishers"], int)
              and isinstance(c["non_anthropic"], int) for c in cells.values()),
          "every cell's three counts are ints")

    check(all(c["non_anthropic"] <= c["eligible"] for c in cells.values()),
          "no cell claims more independent items than it has items")
    check(all(c["publishers"] <= c["eligible"] for c in cells.values()),
          "no cell claims more publishers than items")

    empty = [k for k, c in cells.items() if c["eligible"] == 0]
    check(sorted(empty) == sorted(m["empty_cells"]),
          "`empty_cells` matches the grid (%d)" % len(empty))

    thin = [k for k, c in cells.items() if 0 < c["eligible"] < pc.MIN_POOL]
    check(sorted(thin) == sorted(k for k, _ in m["thin_cells"]),
          "`thin_cells` matches the grid (%d)" % len(thin))

    zero = [k for k, c in cells.items()
            if c["eligible"] > 0 and c["non_anthropic"] == 0]
    check(sorted(zero) == sorted(k for k, _, _ in m["zero_non_anthropic"]),
          "`zero_non_anthropic` matches the grid (%d)" % len(zero))

    picks = json.load(io.open(os.path.join(ROOT, "data", "picks.json"),
                              encoding="utf-8"))["cells"]
    check(m["cells_with_picks"] == len(picks), "`cells_with_picks` matches picks.json")
    check(m["picks"] == sum(len(c["picks"]) for c in picks.values()),
          "`picks` matches picks.json")
    check(m["runners_up"] == sum(len(c["runners_up"]) for c in picks.values()),
          "`runners_up` matches picks.json")

    # ---- 4. the rendered file carries no unformatted placeholders --------------
    text = m_mod.render(m, pc)
    leftovers = [tok for tok in ("%d", "%s", "%%d", "{}") if tok in text]
    check(not leftovers,
          "STATUS.md has no unformatted placeholders (%s)" % (leftovers or "clean"))

    print()
    if fails:
        print("%d check(s) failed:" % len(fails))
        for f in fails:
            print("  - " + f)
        return 1
    print("measure.py describes the catalogue correctly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
