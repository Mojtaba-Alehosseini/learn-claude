#!/usr/bin/env python3
"""
Ask every URL in the catalogue whether it is still there.

`checked` is the site's whole premise - README.md says "When something drifts out of
date, the date says so before we do" - and nothing has ever re-asked. Every `checked`
date is August 2026 and no process would ever move one.

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
import json
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


def check(url):
    """Return (verdict, detail). Verdict is ok, gone, blocked or wobbly."""
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, method="GET", headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-GB,en;q=0.9",
    })
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
            return "ok", str(r.status)
    except urllib.error.HTTPError as e:
        if e.code in GONE:
            return "gone", str(e.code)
        if e.code in BLOCKED:
            return "blocked", str(e.code)
        return "wobbly", str(e.code)
    except urllib.error.URLError as e:
        return "wobbly", "no response (%s)" % (getattr(e, "reason", e),)
    except Exception as e:                      # noqa: BLE001 - a checker must not crash
        return "wobbly", type(e).__name__


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
    counts = collections.Counter()
    for n, it in enumerate(items, 1):
        url = it["url"]
        h = host_of(url)
        if h in allow:
            verdict, detail = "blocked", "known to refuse automation: " + (allow[h] or h)
        else:
            verdict, detail = check(url)
        counts[verdict] += 1
        results.append({"id": it["id"], "title": it["title"], "url": url,
                        "host": h, "verdict": verdict, "detail": detail})
        print("%4d/%d  %-8s %-6s %s" % (n, len(items), verdict, detail[:6], it["title"][:56]),
              flush=True)

    print()
    print("ok %d · gone %d · blocked %d · wobbly %d  (of %d)"
          % (counts["ok"], counts["gone"], counts["blocked"], counts["wobbly"], len(items)))

    if args.json:
        json.dump({"checked": len(items), "counts": dict(counts), "results": results},
                  open(args.json, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
        print("wrote " + args.json)

    return 0


if __name__ == "__main__":
    sys.exit(main())
