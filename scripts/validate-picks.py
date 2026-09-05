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

## The principle the constraints answer to

**A constraint may reject a set of picks; it may never pull an item into one.**

Ruled 2026-08-31, from a real fault. pm|builder's pool holds 55 candidates from three
publishers (53 Anthropic Academy, one Every, one Maven). The no-two-from-one-publisher
rule therefore made every legal three-pick set include the Maven course - a $3,000
certification the picker had not otherwise chosen. The set was legal and the reasoning
was honest, and it was still wrong: a rule built to reject monocultures had become a
rule that promoted an item into a "start with" slot. That inverts it.

So a legal set must come from the picker's own ranked shortlist - its picks and its
runners-up. An item may be lifted into the set by a constraint knocking out something
above it; it may never be hauled in from below the cut to satisfy a count. Where no
legal three exist inside the shortlist, the cell ships two and says why in
`two_pick_cause`. Two honest picks beat three where the third is the checker's choice.

## Why an undated resource is still a candidate

Asked and answered 5 September 2026, with the counterfactual measured rather than
argued. If `published: UNVERIFIED` were excluded from the pre-filter:

    cells falling below MIN_POOL (4)   3 -> 13 of 40
    cells becoming completely empty    1 ->  8 of 40

and every `builder` cell in the catalogue would hold ZERO candidates. Not few - zero.
`pm|builder` has 55 eligible resources and not one of them carries a date, because
advanced material is overwhelmingly Anthropic Academy pages and Academy prints no dates
at all. Excluding the undated would not raise the bar, it would delete the top half of
the site.

So undated stays eligible. What changes is the tie-break below.

## The tie-break: at equal fit, a dated resource wins

The picker is told that where two candidates fit the cell equally well, the one whose
date we can stand behind takes the slot - and that when that rule decided it, the reason
says so in one clause, so a reader can see the tie was broken on evidence rather than on
taste. "Equal fit" is doing real work there: this is a tie-break, not a ranking factor.
A better-fitting undated resource still beats a worse-fitting dated one, every time.

Applies from the next re-pick onward. The 37 cells already picked were judged before the
rule existed and are not re-run for it - re-picking a cell to apply a tie-break that
would not have changed the outcome is churn, and where it would have changed the outcome
we would be reversing a judgment on a rule that did not exist when it was made.

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
import collections
import itertools
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


# A two-pick cell must say which of these put it there. Never a bare count of two:
# "only two" is a fact about the catalogue or about the shortlist, and which one it is
# changes what a reader should conclude.
# `constraints-jointly-unsatisfiable` added 2026-09-06 (R4). It is not the shortlist
# refusing a third pick, it is the rules refusing one: with three publishers the cap
# is one each, and if those publishers offer fewer formats between them than the
# format rule wants, no legal third pick exists at all. Blaming the shortlist for
# that made the cell read as thin when it was the constraints disagreeing.
TWO_PICK_CAUSES = ("publisher-thin", "rule-carried-third-refused",
                   "constraints-jointly-unsatisfiable")


# Optional on a runner-up, and machine-readable so a class of mistake can be counted
# rather than remembered. Added 2026-09-05 after Attack 2 found two picks whose own card
# named a different reader or excluded this one - the FIX-15 audit had reported zero
# self-contradictions, because it read each pick's reason against the pick rather than
# the pick's own who_for and skip_if against the CELL. Three cells were re-cut; the
# displaced picks carry this cause so the next audit starts from a record instead of a
# memory.
RUNNER_CAUSES = {
    "contradicted-its-own-card",
    # Added 2026-09-06 with Rule A. A pick that leaves because the level it sat at
    # was redefined did not lose an argument, and the record should not imply it
    # did.
    "re-levelled-out-of-the-pool",
    # Added 2026-09-06 with Rule B. A pick that leaves because a role tag its own card
    # denies was dropped did not lose an argument either - and it is a different fault
    # from a level being redefined, so it gets its own word.
    "re-tagged-out-of-the-pool",
}


# A claim about the pool that no script can check: whether this really is the only
# candidate that walks a workflow end to end, whether every safety page here is
# Anthropic's. They were all true when written. Pools move; sentences do not.
POOL_CLAIM = re.compile(
    r"\b(the only|only one|the one candidate|the pool's one|every |all of|none of|"
    r"no other|nothing else|everything else|never explain|always)\b", re.I)


def claim_lines(cell):
    """Every reason in this cell that asserts something about the whole pool."""
    out = []
    for kind in ("picks", "runners_up"):
        for p in cell.get(kind) or []:
            m = POOL_CLAIM.search(p.get("reason") or "")
            if m:
                out.append((kind, p.get("url"), m.group(0).strip(), p.get("reason")))
    return out


def allowed_picks(pool):
    """(max from one publisher, CEILING on pick count) for this pool.

    A ceiling, not a quota - see the principle above. 3 picks normally; a 2-publisher
    pool still reaches 3 (2+1); a 1-publisher pool cannot exceed 2 without becoming the
    monoculture the rule exists to stop. A cell may always ship one fewer than its
    ceiling when its own shortlist holds no legal candidate for the last slot.
    """
    pubs = {x.get("source", "") for x in pool}
    if len(pubs) >= 3:
        return 1, 3          # every pick from a different publisher
    if len(pubs) == 2:
        return 2, 3
    return 2, 2


def max_distinct_formats(pool, k, max_per_pub):
    """The most distinct formats any LEGAL k-item selection from this pool can span.

    "Legal" means within the per-publisher cap, which is the whole point: the old code
    counted formats across the pool and ignored the cap, so it could demand a spread no
    permitted selection can reach. teacher|confident is the case that exposed it - three
    publishers, cap of one each, and two of the three publish only articles, so every
    legal three-pick set spans two formats while the rule asked for three.

    Exact, not estimated. The search runs over distinct (publisher, format) pairs rather
    than items, because two items sharing both contribute nothing new: a pool of eighty
    rarely has more than thirty pairs, and choosing three from thirty is four thousand
    combinations.
    """
    pairs = sorted({(x.get("source", ""), x.get("format")) for x in pool})
    if not pairs or k <= 0:
        return 0
    best = 0
    for combo in itertools.combinations(pairs, min(k, len(pairs))):
        counts = collections.Counter(pub for pub, _f in combo)
        if any(c > max_per_pub for c in counts.values()):
            continue
        best = max(best, len({f for _p, f in combo}))
        if best == min(k, len({f for _p, f in pairs})):
            break
    return best


def expected_two_pick_cause(pool):
    """Which cause a two-pick cell must declare, given its pool.

    One publisher means the pool itself caps the cell at two - `publisher-thin`.

    Otherwise, ask whether a legal three-pick set could satisfy the format rule at all.
    Where it cannot - three publishers, cap of one each, and only two formats reachable -
    the missing third is the rules disagreeing with each other, not a shortlist being
    fussy: `constraints-jointly-unsatisfiable`.

    Everything else is the shortlist's doing - `rule-carried-third-refused`.
    """
    pubs = {x.get("source", "") for x in pool}
    if len(pubs) < 2:
        return "publisher-thin"
    max_per_pub, ceiling = allowed_picks(pool)
    if max_distinct_formats(pool, ceiling, max_per_pub) < ceiling and \
            len({x.get("format") for x in pool}) >= ceiling:
        return "constraints-jointly-unsatisfiable"
    return "rule-carried-third-refused"


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
    if cell.get("claims_checked_on") and \
       not DATE.match(str(cell.get("claims_checked_on"))):
        err("claims_checked_on = %r is not YYYY-MM-DD" % cell.get("claims_checked_on"))
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
        # A reason may not claim independence the data denies. `official` means "not
        # published on an Anthropic domain", and three reasons read it as "not from
        # Anthropic": two praised Claude 101 as the pool's non-Anthropic voice while its
        # own author line said "Created by Anthropic, adapted for the DataCamp
        # platform", and one called a talk non-Anthropic material in the same sentence
        # that credited the SDK's own engineer. Independence is the axis those sentences
        # were selling, so getting it backwards is not a wording slip.
        reason = str(p.get("reason") or "")
        if "non-anthropic" in reason.lower().replace(" ", "-"):
            author = str(it.get("author") or "")
            said = (author if "anthropic" in author.lower()
                    else (it["title"] if "anthropic" in it["title"].lower() else ""))
            if said:
                err("pick %r calls itself non-Anthropic, and its own card says %r "
                    "— official means the domain, not the author"
                    % (it["title"][:40], said[:70]))
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
        if r.get("cause") is not None and r["cause"] not in RUNNER_CAUSES:
            err("runner-up %s has cause %r, which is not one of %s"
                % (r.get("url"), r["cause"], ", ".join(sorted(RUNNER_CAUSES))))

    # The four constraints, against what the pool allows.
    if pick_items and pool:
        max_per_pub, ceiling = allowed_picks(pool)
        pool_pubs = {x.get("source", "") for x in pool}
        cause = str(cell.get("two_pick_cause") or "").strip()

        if len(picks) > ceiling:
            err("%d picks where this pool allows at most %d (%d publisher%s in pool)"
                % (len(picks), ceiling, len(pool_pubs),
                   "" if len(pool_pubs) == 1 else "s"))
        elif len(picks) == 2:
            want = expected_two_pick_cause(pool)
            if not cause:
                err("two picks and no two_pick_cause. A bare count of two says nothing; "
                    "this pool wants %r." % want)
            elif cause not in TWO_PICK_CAUSES:
                err("two_pick_cause is %r — must be one of %s"
                    % (cause, ", ".join(TWO_PICK_CAUSES)))
            elif cause != want:
                err("two_pick_cause is %r but this pool has %d publisher%s, which means "
                    "%r" % (cause, len(pool_pubs),
                            "" if len(pool_pubs) == 1 else "s", want))
            else:
                notes.append("  %-28s two picks, cause %s" % (key, cause))
        elif len(picks) < 2:
            err("%d pick(s) — a single card is not a set" % len(picks))
        elif cause:
            err("two_pick_cause is %r on a %d-pick cell, where it means nothing"
                % (cause, len(picks)))

        by_pub = {}
        for it in pick_items:
            by_pub.setdefault(it.get("source", ""), []).append(it)
        for pub, group in by_pub.items():
            if len(group) > max_per_pub:
                err("%d picks from %r where this pool allows %d per publisher"
                    % (len(group), pub, max_per_pub))
        if len(pool_pubs) < 3:
            notes.append("  %-28s publisher-thin pool: %d publisher%s, cap is %d per "
                         "publisher, ceiling %d, %d picks"
                         % (key, len(pool_pubs), "" if len(pool_pubs) == 1 else "s",
                            max_per_pub, ceiling, len(picks)))

        if any(not x.get("official") for x in pool) and \
           all(it.get("official") for it in pick_items):
            err("every pick is official Anthropic and the pool offers %d that are not"
                % sum(1 for x in pool if not x.get("official")))

        of_fmt = lambda x: x.get("format")
        in_pool = {of_fmt(x) for x in pool}
        in_picks = [of_fmt(it) for it in pick_items]
        # The most a LEGAL selection can span, not the most the pool contains. See
        # max_distinct_formats: the old line ignored the publisher cap and could demand
        # a spread no permitted set of picks can reach.
        want = max_distinct_formats(pool, len(pick_items), max_per_pub)
        if len(set(in_picks)) < want:
            err("picks span %d formats where %d picks under a cap of %d per publisher "
                "could span %d (the pool holds %d formats in all)"
                % (len(set(in_picks)), len(pick_items), max_per_pub, want, len(in_pool)))

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
        # The re-pick is not finished when three URLs are chosen. Every sentence that
        # claims something about the pool has to be read against the pool as it is now.
        claims = claim_lines(cell)
        if claims:
            warn("...and %d of its sentences claim something about that pool. Re-read "
                 "each one before closing this cell, then set claims_checked_on to the "
                 "day you did:" % len(claims))
            for kind, url, phrase, reason in claims:
                warn("      %-10s \"%s\"  %s" % (kind, phrase, url[-52:]))

    # Closing a cell means saying the sentences were re-read, not only that three URLs
    # were chosen. A picked_on ahead of claims_checked_on is a re-pick that refreshed the
    # fingerprint and left the prose behind - the exact failure FIX-25 found eleven of.
    claims = claim_lines(cell)
    checked = str(cell.get("claims_checked_on") or "")
    if claims and checked and checked < str(cell.get("picked_on") or ""):
        err("re-picked on %s but its %d pool claims were last read on %s. A cell does "
            "not close until its own sentences have been read against the pool it now "
            "has." % (cell.get("picked_on"), len(claims), checked))
    elif claims and not checked:
        warn("%d sentence(s) claim something about this pool and none has been re-read "
             "since the claim was written. Set claims_checked_on when you next open "
             "this cell." % len(claims))
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
