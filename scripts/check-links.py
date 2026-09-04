#!/usr/bin/env python3
"""
Ask every URL in the catalogue whether it is still there.

`checked` is the site's whole premise - README.md says "When something drifts out of
date, the date says so before we do" - and nothing has ever re-asked. Every `checked`
date is August 2026 and no process would ever move one.

## What to do with each verdict

The convention, ruled 2026-09-04 after an expired webinar and a moved Excel page turned
up in the same round:

  ok       nothing to do.
  moved    a permanent redirect (301 or 308). This is a FAULT, not a pass. The catalogue
           holds a URL that no longer resolves to itself, and ids are derived from URLs,
           so picks and paths point at the old one. Open the destination, take the new
           URL, and re-read the card against the new page - a moved page is often a
           rewritten page. The Excel article moved to claude.com/docs and gained a
           prompt-injection warning the old card never mentioned.
  gone     the resource is dead. If it has a destination, follow the `moved` procedure.
           If it has none, REMOVE the row. The catalogue carries no `status: dead` rows -
           "0 dead links" is a swept number, not a labelled one - and an expired one-off
           event, which is what the first `gone` turned out to be, is not something a
           reader could ever open again.
  blocked  the host refuses automation. This is NOT evidence the page is dead. These are
           unverifiable by machine and need a person; docs/STATUS.md lists them with the
           date a person last confirmed each.
  wobbly   a timeout or an odd status. Re-run before believing it.

This reports. It does not fix, it does not write data/items.json, and it does not
commit. A job that silently flipped `status: dead` would let one misconfigured
user-agent quietly delete good resources from a catalogue nobody was watching, and the
failure would look exactly like success.

    python3 scripts/check-links.py                # human-readable
    python3 scripts/check-links.py --json out.json

Exit code is 0 whether or not links are gone. A checker is not a test; a dead link out
in the world is not this repository failing to build.

## Gone versus blocked us

Roughly a fifth of the catalogue sits behind hosts that answer a script with 403 while
serving a browser perfectly - Udemy, DataCamp, Medium and friends. A checker that calls
those dead every week is a checker that gets ignored by week three, and then the one
real dead link scrolls past with them. So the two are separated and only "gone" is
shouted about:

  gone      404 or 410. The host answered and said there is nothing here.
  blocked   401, 403, 429, or a host in data/link-check-allow.txt. The host answered
            and declined to answer *us*. Says nothing about the resource.
  wobbly    5xx, timeout, connection reset. The host had a bad day. Reported quietly,
            because three bad weeks running is worth a look and one is not.

data/link-check-allow.txt carries hosts known to refuse automation, with the reason.
education.gov.au is the awkward one: it returns nothing at all to an automated request
and is perfectly alive, which is already recorded in that resource's own `notes`.
"""

import argparse
import collections
import datetime
import json
import re
import os
import ssl
import sys
import urllib.error
import urllib.request
from urllib.parse import urlparse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITEMS = os.path.join(ROOT, "data", "items.json")
ALLOW = os.path.join(ROOT, "data", "link-check-allow.txt")

# A real browser string. Not to sneak past anything - the hosts that block automation
# block it on other signals too - but because some servers 400 an empty user-agent and
# that would be our bug, not theirs.
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36")

TIMEOUT = 20

GONE = {404, 410}
BLOCKED = {401, 403, 429, 451}


def load_allowlist():
    hosts = {}
    if not os.path.exists(ALLOW):
        return hosts
    for line in open(ALLOW, encoding="utf-8"):
        raw = line.strip()
        if not raw or raw.startswith("#"):
            continue
        host, _, reason = raw.partition("#")
        hosts[host.strip().lower()] = reason.strip()
    return hosts


def _load_host():
    """Imported, not reimplemented — see the note on host() in scripts/stable-ids.py.

    This line used to be `.lstrip("www.")`, which strips a set of characters rather than
    a prefix and quietly turned wotai.co into otai.co. The same wrong line existed in
    validate-catalogue.py. Two copies of a host-normaliser is how norm() ended up with
    three definitions and a bug in each, so there is now one.
    """
    import importlib.util
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stable-ids.py")
    spec = importlib.util.spec_from_file_location("stable_ids", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.host


host_of = _load_host()

# Pages on Intercom's template - the Claude Help Center is the big one - print a
# LAST-UPDATED date, not a publication date, and it drifts by design. That is not a
# cosmetic difference: a stored 2025-05-05 on a page that now prints March 2026 put a
# live resource over the freshness threshold, so the picks pre-filter dropped it from
# every pool for ten months and nothing went red. Parsing the printed date on every
# weekly run turns that silent drift into a reported number.
DATED_HOSTS = ("support.claude.com", "privacy.claude.com")

MONTHS = {m: i + 1 for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june",
     "july", "august", "september", "october", "november", "december"])}

DATE_RE = re.compile(
    r"([A-Z][a-z]+)\s+(\d{1,2}),\s+(\d{4})")          # "March 16, 2026"
RELATIVE_RE = re.compile(
    r"[Uu]pdated\s+(today|yesterday|this week|over|last|\d+\s+\w+\s+ago)")


def printed_date(html):
    """(iso-date-or-None, what-the-page-said). None means no calendar date was printed.

    A relative phrase - "updated this week" - is only true on the day it is read, so it
    is reported as drift-unknown rather than converted into a date we would then print
    as fact. That is the same rule the catalogue applies in `published`.
    """
    rel = RELATIVE_RE.search(html)
    m = DATE_RE.search(html)
    if m:
        mon = MONTHS.get(m.group(1).lower())
        if mon:
            return ("%04d-%02d-%02d" % (int(m.group(3)), mon, int(m.group(2))),
                    m.group(0))
    if rel:
        return None, rel.group(0)
    return None, ""


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """Stop on a permanent redirect so it can be reported instead of followed.

    urllib follows 301 and 308 silently, which is why the catalogue carried a moved
    Excel URL through a full link check that called it "ok". Temporary redirects (302,
    303, 307) are still followed - those are load balancers and locale routing, not a
    resource changing address.
    """

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if code in (301, 308):
            raise _Moved(newurl, code)
        return urllib.request.HTTPRedirectHandler.redirect_request(
            self, req, fp, code, msg, headers, newurl)


class _Moved(Exception):
    def __init__(self, newurl, code):
        Exception.__init__(self, newurl)
        self.newurl, self.code = newurl, code


def check(url, want_body=False):
    """Return (verdict, detail, body). Verdict: ok, moved, gone, blocked or wobbly."""
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, method="GET", headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.9",
    })
    opener = urllib.request.build_opener(_NoRedirect,
                                         urllib.request.HTTPSHandler(context=ctx))
    try:
        with opener.open(req, timeout=TIMEOUT) as r:
            body = ""
            if want_body:
                try:
                    body = r.read(400000).decode("utf-8", "replace")
                except Exception:                # noqa: BLE001
                    body = ""
            return "ok", str(r.status), body
    except _Moved as e:
        return "moved", "%d -> %s" % (e.code, e.newurl), ""
    except urllib.error.HTTPError as e:
        if e.code in GONE:
            return "gone", str(e.code), ""
        if e.code in BLOCKED:
            return "blocked", str(e.code), ""
        return "wobbly", str(e.code), ""
    except urllib.error.URLError as e:
        return "wobbly", "no response (%s)" % (getattr(e, "reason", e),), ""
    except Exception as e:                      # noqa: BLE001 - a checker must not crash
        return "wobbly", type(e).__name__, ""


def _blocked_summary(results, allow):
    """Blocked hosts, grouped, for STATUS.md. A bot-wall is not evidence of death, so
    these carry the date a PERSON last confirmed them rather than a machine verdict."""
    seen = collections.Counter(r["host"] for r in results if r["verdict"] == "blocked")
    human = load_human_checks()
    return [{"host": h, "count": c, "last_human_check": human.get(h, "never")}
            for h, c in sorted(seen.items(), key=lambda kv: -kv[1])]


def load_human_checks():
    """data/blocked-checked-by-hand.txt - `host  YYYY-MM-DD` per line, # for comments."""
    path = os.path.join(ROOT, "data", "blocked-checked-by-hand.txt")
    out = {}
    if not os.path.exists(path):
        return out
    for line in open(path, encoding="utf-8"):
        line = line.split("#")[0].strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) >= 2:
            out[parts[0]] = parts[1]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", help="also write the full result here")
    ap.add_argument("--limit", type=int, help="check only the first N, for a dry run")
    args = ap.parse_args()

    allow = load_allowlist()
    items = json.load(open(ITEMS, encoding="utf-8"))
    if args.limit:
        items = items[:args.limit]

    results = []
    drift = []
    counts = collections.Counter()
    for n, it in enumerate(items, 1):
        url = it["url"]
        h = host_of(url)
        dated = any(h.endswith(d) for d in DATED_HOSTS)
        if h in allow:
            verdict, detail, body = "blocked", \
                "known to refuse automation: " + (allow[h] or h), ""
        else:
            verdict, detail, body = check(url, want_body=dated)

        row = {"id": it["id"], "title": it["title"], "url": url,
               "host": h, "verdict": verdict, "detail": detail}

        # Drift: the page prints a last-updated date newer than what we store.
        if dated and verdict == "ok" and body:
            iso, said = printed_date(body)
            row["page_date"] = iso
            row["page_says"] = said
            row["stored"] = it.get("published")
            stored = it.get("published")
            if iso and stored and stored != "UNVERIFIED" and stored != iso:
                # A stored calendar date that has fallen behind the page's. This is the
                # one that bites: it can push a live resource past the freshness rule
                # and out of every picks pool. "Anthropic's AI for Science Program"
                # stored 2025-05-05 while the page printed 2026-03-16, and was excluded
                # from every pool for ten months with nothing going red.
                row["drift"] = "stored %s, page prints %s" % (stored, iso)
                row["drift_class"] = "stale-stored-date"
                drift.append(row)
            elif iso and (stored == "UNVERIFIED" or stored is None):
                # Informational only, and deliberately NOT actioned. Intercom keeps a
                # calendar date in the HTML while showing "updated yesterday" to a
                # reader, so the machine can see a date the page does not display. It is
                # a LAST-UPDATED date, and `published` prints on the card as "Published
                # <date>" - writing it there would make the card state a publication
                # date that is false. UNVERIFIED already produces the right behaviour:
                # the card says no publish date is given, and UNVERIFIED is not stale,
                # so nothing is wrongly excluded. Reported so the drift is visible, not
                # so somebody converts it.
                row["drift"] = "UNVERIFIED here; page prints %s (last-updated)" % iso
                row["drift_class"] = "unverified-page-has-date"
                drift.append(row)

        counts[verdict] += 1
        results.append(row)
        print("%4d/%d  %-8s %-6s %s" % (n, len(items), verdict, detail[:6], it["title"][:56]),
              flush=True)

    print()
    print("ok %d · moved %d · gone %d · blocked %d · wobbly %d  (of %d)"
          % (counts["ok"], counts["moved"], counts["gone"], counts["blocked"],
             counts["wobbly"], len(items)))

    if counts["moved"]:
        print()
        print("MOVED - a permanent redirect is a fault, not a pass. The catalogue holds")
        print("a URL that no longer resolves to itself, and ids come from URLs:")
        for r in results:
            if r["verdict"] == "moved":
                print("  %-52s %s" % (r["title"][:52], r["detail"]))

    stale_stored = [r for r in drift if r.get("drift_class") == "stale-stored-date"]
    unver = [r for r in drift if r.get("drift_class") == "unverified-page-has-date"]

    if stale_stored:
        print()
        print("DATE DRIFT NEEDING ACTION on %d page%s. A stored calendar date has fallen"
              % (len(stale_stored), "" if len(stale_stored) == 1 else "s"))
        print("behind the page's own. This is the fault that hides a live resource from")
        print("every picks pool. Re-read and update `published`:")
        for r in stale_stored:
            print("  %-52s %s" % (r["title"][:52], r["drift"]))

    if unver:
        print()
        print("%d page%s stored UNVERIFIED while the HTML carries a last-updated date."
              % (len(unver), "" if len(unver) == 1 else "s"))
        print("Informational. Do NOT convert these: it is a last-updated date, `published`")
        print("prints as \"Published <date>\" on the card, and UNVERIFIED already gives the")
        print("right behaviour - an honest card and no false staleness.")
        for r in unver[:5]:
            print("  %-52s %s" % (r["title"][:52], r["drift"]))
        if len(unver) > 5:
            print("  ... and %d more, in the JSON report." % (len(unver) - 5))

    if args.json:
        json.dump({"when": str(datetime.date.today()),
                   "checked": len(items), "counts": dict(counts),
                   "drift": drift,
                   "blocked": _blocked_summary(results, allow),
                   "results": results},
                  open(args.json, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
        print("wrote " + args.json)

    return 0


if __name__ == "__main__":
    sys.exit(main())
