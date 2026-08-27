#!/usr/bin/env python3
"""
Turn a link-check result into an issue, and only when there is something to say.

Reads the JSON that scripts/check-links.py writes and decides whether it is worth
anyone's attention. The whole design goal is that this can be trusted in week thirty,
which means it must almost never be wrong:

  - `gone` (404/410) is the only thing that opens an issue. `blocked` never does. About
    a fifth of the catalogue is behind hosts that refuse automation and serve browsers
    fine, and a weekly issue naming them is how a report gets filtered to trash.
  - A single open thread, not one issue a week. If a `dead-links` issue is already open
    it gets a comment instead, so a link that stays dead for a month is one conversation
    rather than four identical tickets.
  - A sanity valve. If more than a fifth of the catalogue reads as gone in one run, that
    is a runner with broken DNS, not seventy dead links. It says so and files nothing.

Never writes data/items.json. Never commits. Requires GH_TOKEN and REPO in the
environment; the workflow supplies both.

    python3 scripts/report-dead-links.py link-check.json
    python3 scripts/report-dead-links.py link-check.json --dry-run
"""

import argparse
import json
import os
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

LABEL = "dead-links"
# Above this share of the catalogue, believe the network is broken rather than the web.
IMPLAUSIBLE = 0.20


def gh(*args, check=True):
    return subprocess.run(["gh", *args], capture_output=True, text=True,
                          encoding="utf-8", errors="replace", check=check)


def body_for(gone, wobbly, counts, checked, run_url):
    lines = []
    one = len(gone) == 1
    lines.append("The weekly link check found **%d resource%s the host says %s gone** "
                 "(404 or 410)." % (len(gone), "" if one else "s", "is" if one else "are"))
    lines.append("")
    for r in gone:
        lines.append("- **%s**" % r["title"])
        lines.append("  - %s — HTTP %s" % (r["url"], r["detail"]))
        lines.append("  - https://mojtaba-alehosseini.github.io/learn-claude/resource.html?id=%s"
                     % r["id"])
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("**What this does not mean.** A link that answers 403 is not in this "
                 "list. Roughly a fifth of the catalogue sits behind hosts that refuse "
                 "automated requests and serve a browser perfectly, and calling those "
                 "dead every week is how a report like this gets ignored. This run saw "
                 "**%d blocked** and **%d wobbly** (5xx or no answer); neither is in the "
                 "list above." % (counts.get("blocked", 0), counts.get("wobbly", 0)))
    lines.append("")
    lines.append("**Open each one in a browser before doing anything.** The check can be "
                 "wrong and the web can be having a bad morning.")
    lines.append("")
    lines.append("**Do not move the `checked` date.** Re-checking that a link still "
                 "resolves is not the same as re-reading the resource, and only the "
                 "second earns a new date. If a link is genuinely gone the honest edit "
                 "is `status: dead`, which the site already renders as \"This link no "
                 "longer works\" while leaving the card in place so a reader knows it "
                 "was checked rather than quietly dropped.")
    lines.append("")
    lines.append("Nothing was changed automatically. %d URLs were asked. "
                 "[Full run](%s)." % (checked, run_url or "n/a"))
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("result")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    data = json.load(open(args.result, encoding="utf-8"))
    results = data["results"]
    counts = data.get("counts", {})
    checked = data.get("checked", len(results))
    gone = [r for r in results if r["verdict"] == "gone"]
    wobbly = [r for r in results if r["verdict"] == "wobbly"]
    run_url = os.environ.get("RUN_URL", "")

    print("checked %d · gone %d · blocked %d · wobbly %d"
          % (checked, len(gone), counts.get("blocked", 0), len(wobbly)))

    if checked and len(gone) / checked > IMPLAUSIBLE:
        print("%d of %d reading as gone is not %d dead links, it is a broken runner. "
              "Filing nothing." % (len(gone), checked, len(gone)))
        return 0

    if not gone:
        print("Nothing gone. No issue filed.")
        return 0

    body = body_for(gone, wobbly, counts, checked, run_url)
    if args.dry_run:
        print("\n--- issue that would be filed ---\n")
        print(body)
        return 0

    if not os.environ.get("GH_TOKEN"):
        sys.exit("GH_TOKEN is not set. This is meant to run from the workflow.")

    existing = gh("issue", "list", "--label", LABEL, "--state", "open",
                  "--json", "number", "--limit", "1", check=False)
    open_issues = json.loads(existing.stdout or "[]") if existing.returncode == 0 else []

    if open_issues:
        n = str(open_issues[0]["number"])
        gh("issue", "comment", n, "--body", body)
        print("Commented on the open #%s rather than filing a second one." % n)
    else:
        gh("label", "create", LABEL, "--description",
           "Links the weekly check reported as gone", "--color", "B60205", check=False)
        r = gh("issue", "create", "--title",
               "%d link%s gone" % (len(gone), "" if len(gone) == 1 else "s"),
               "--label", LABEL, "--body", body, check=False)
        print(r.stdout.strip() or r.stderr.strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
