#!/usr/bin/env python3
"""
Give every resource an id that is derived from its URL instead of its position.

Why this exists. Ids used to be assigned by list order — `item-0121` meant "the 121st
row in items.json". When the catalogue grew from 253 to 288 rows, every position after
the first insertion shifted, and every hand-written reference to an id silently began
pointing at a different resource. Two of the three learning paths were scrambled that
way, and nothing failed loudly: step 1 of the beginner path became a tutorial on
building an MCP server with Docker, under a `why` that talked about orientation.

A position is not an identity. The URL is the identity — it is what makes two rows the
same resource — so the id is a hash of it. Rows can now be added, removed or sorted in
any order and every reference still resolves.

    python3 scripts/stable-ids.py
    python3 scripts/stable-ids.py --check    # report, change nothing
"""

import hashlib
import json
import sys
from urllib.parse import urlparse

ITEMS = "data/items.json"


TRACKING = ("utm_", "si=", "feature=", "fbclid=", "gclid=", "ref=", "ref_src=")


def norm(url):
    """Same normalisation the merge uses, so one resource cannot get two ids.

    The query string is kept, minus tracking junk. Dropping it wholesale looks tidy
    and is wrong: a YouTube URL carries its identity in `?v=`, so stripping the query
    collapsed every video on the site to `youtube.com/watch` — one id shared by all of
    them, and a dedupe step that discarded every video after the first.
    """
    url = url.strip().rstrip("/").lower()
    if "?" not in url:
        return url
    base, _, query = url.partition("?")
    keep = [p for p in query.split("&")
            if p and not any(p.startswith(t) for t in TRACKING)]
    return base + ("?" + "&".join(sorted(keep)) if keep else "")


def host(url):
    """The hostname, lowercased, with a leading `www.` removed.

    Lives here, next to norm(), because it answers the same question — what makes two
    URLs the same thing — and because it had already been written three times elsewhere,
    wrongly in two of them. This is the third definition of a URL rule in this codebase
    that turned out to be a bug; norm() was the first. One definition, imported.

    The prefix is removed by hand rather than with `.lstrip("www.")`, which is the bug
    this replaces. lstrip takes a SET of characters, not a prefix, so it eats any leading
    run of `w` and `.`:

        weather.com          -> eather.com
        wotai.co             -> otai.co
        w3schools.com        -> 3schools.com
        www.wrightmode.com   -> rightmode.com    (prefix stripped, then the real w too)

    Five hosts in the catalogue were being mis-trimmed this way on 2026-08-29. Nothing
    had broken yet, and the reason is worth stating because it is the dangerous kind of
    luck: the duplicate checks in validate-catalogue.py skip a group whose rows all share
    one host. A mis-trim that maps two *different* hosts onto one string does not raise a
    false alarm — it silences a real one. The failure mode of this bug is a check that
    quietly stops checking.
    """
    h = (urlparse(str(url or "")).netloc or "").lower()
    return h[4:] if h.startswith("www.") else h


def make_id(url):
    return "r-" + hashlib.sha1(norm(url).encode("utf-8")).hexdigest()[:10]


def main():
    check = "--check" in sys.argv
    items = json.load(open(ITEMS, encoding="utf-8"))

    old_ids = [x.get("id") for x in items]
    new_ids = [make_id(x["url"]) for x in items]

    if len(set(new_ids)) != len(new_ids):
        seen, dupes = set(), set()
        for i in new_ids:
            (dupes if i in seen else seen).add(i)
        sys.exit(f"Hash collision or duplicate URL: {dupes}")

    changed = sum(1 for a, b in zip(old_ids, new_ids) if a != b)
    print(f"{len(items)} resources, {changed} ids change")

    if check:
        for x, a, b in list(zip(items, old_ids, new_ids))[:5]:
            print(f"   {a} -> {b}  {x['title'][:50]}")
        return

    for x, new in zip(items, new_ids):
        x["id"] = new
    json.dump(items, open(ITEMS, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    print("Now rebuild anything that stores these ids:")
    print("  python3 scripts/build-search-index.py --keywords")
    print("  python3 scripts/build-paths.py")
    print("  python3 scripts/build-data-js.py")


if __name__ == "__main__":
    main()
