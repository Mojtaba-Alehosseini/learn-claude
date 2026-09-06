#!/usr/bin/env bash
# Rebuild everything the site reads, in the order the steps depend on each other.
#
# Run this after editing anything in data/ or research/. Each step is safe to re-run.
#
#   ./build.sh
#
# Then just open index.html. There is no server to start — the data loads through
# <script> tags rather than fetch(), so the site works straight from the folder.

set -e
# Every gate in this file used to be piped through `tail` so the output stays short, and a
# pipeline's status is the last command's - so `tail` returned 0 over the top of every
# failing check, and had since the first one was added. The search suite exited 1 on eight
# regressions in FIX-30 and this file said "Done. Open index.html." CI ran the same command
# without a pipe and stopped the deploy, which is how it was found.
#
# pipefail alone is not enough. `cmd | head -3` makes the producer die of SIGPIPE, which
# pipefail then reports as a failure - a gate that goes red for the wrong reason is a gate
# people learn to ignore. So no gate is piped at all: `gate` captures the output, prints
# the last few lines when it passes and every line when it fails, and returns the command's
# own status. Failure is exit status, never text.
#
# scripts/test-gates.py plants a failure in each gate and asserts this file goes red.
set -o pipefail
cd "$(dirname "$0")"

# gate <lines-to-show-on-success> <command...>
gate() {
  local n="$1"; shift
  local out status
  set +e
  out="$("$@" 2>&1)"
  status=$?
  set -e
  if [ "$status" -ne 0 ]; then
    printf '%s\n' "$out"
    echo "FAILED (exit $status): $*" >&2
    return "$status"
  fi
  if [ "$n" -gt 0 ]; then
    printf '%s\n' "$out" | tail -n "$n"
  fi
  return 0
}

echo "1/7  the catalogue itself, before anything is generated from it"
# CI checked these two and this file never did, so a fault in items.json was found on the
# server rather than on the machine that wrote it. Order matters: the steps below rewrite
# ids, paths and the index off items.json, so a fault checked afterwards has already been
# copied into three more files.
gate 1 python3 scripts/validate-catalogue.py
# And prove the validator still bites.
gate 1 python3 scripts/test-validate-catalogue.py

echo
echo "2/7  stable ids (derived from URL, never from list position)"
gate 0 python3 scripts/stable-ids.py

echo
echo "3/7  publisher names and the official flag"
gate 3 python3 scripts/add-source.py

echo
echo "4/7  learning paths"
gate 3 python3 scripts/build-paths.py

echo
echo "5/7  search index"
gate 0 python3 scripts/build-search-index.py --keywords
# Fifty-seven sentences ten hostile strangers actually typed at the site, with the
# result each of them got. Most are asserted; the rest are recorded failures, and the
# run says so out loud rather than hiding them. Exits 1 only when a query that used to
# work stops working.
gate 2 python3 scripts/test-search.py
# One algorithm, two runtimes, every query. Amendment 3 to the search spec: ten samples
# is a place for drift to hide, and Python and the browser had already disagreed once.
gate 0 python3 scripts/test-search.py --emit tmp/py-top3.json
gate 1 node scripts/test-search-runtimes.js tmp/py-top3.json
# Every synonym row carries the reason it exists, like every skip_if.
gate 1 python3 scripts/validate-synonyms.py
# The stemmer's word families, taken from the failing suite lines.
gate 1 python3 scripts/test-stem.py
# Which bucket Rule B sends a card to, on the sentences that were getting it wrong.
gate 1 python3 scripts/test-role-buckets.py
# questions[] is the highest-weighted field and the suite is the judge; a query written
# into the data would be a pass bought with the answer sheet.
gate 1 python3 scripts/check-questions.py
# And a row has to be findable by its own questions. FIX-30 replaced pages' own nouns
# with near-synonyms and only the suite noticed, on the rows it happened to cover.
gate 1 python3 scripts/check-self-retrieval.py
# A content gap says the catalogue holds nothing. Every gap recorded before FIX-30 was
# written from cards and every one was wrong; a gap now carries the pages it opened.
gate 1 python3 scripts/test-gap-claims.py

echo
echo "5b/7 sitemap, generated rather than typed"
gate 0 python3 scripts/build-sitemap.py

echo
echo "6/7  data as loadable javascript"
gate 0 python3 scripts/build-data-js.py
# A visitor arriving from the home page with ?q=<a sentence> must get an answer. Runs
# here because it loads the generated data/*.js the browser loads. The fault it guards
# was never in the ranking function - it was in the trigger, and the ranking test passed
# happily throughout.
gate 1 node scripts/test-browse-query.js

echo
echo "7/7  measured status, the picks, and the freshness exclusions"
# Writes docs/STATUS.md, which THE-PROJECT.md and README point at instead of repeating
# the numbers. It also prints every live resource the freshness rule keeps out of the
# picks pools: that exclusion used to be silent, and a wrong date once hid a live
# resource from every pool for ten months without one step going red.
gate 20 python3 scripts/measure.py --status
gate 0 python3 scripts/test-measure.py
# The picks are a committed model judgment, and they rot two ways: a stale pool (warned,
# dated, ships) and a dead or ineligible pick (fails). CI checked these and this file
# did not, so a wrong pick reached the server before it reached the person who made it.
gate 1 python3 scripts/validate-picks.py
gate 1 python3 scripts/test-validate-picks.py
# Four sentences the site is not allowed to say again - see D2 in FIX-24.md.
gate 1 python3 scripts/test-copy-claims.py
# The no-typed-numbers rule, reaching picks.json at last. A pick's reason ships on the
# card, and eleven of them were counting pools that had moved underneath them.
gate 1 python3 scripts/check-typed-numbers.py
# Advisory, printed, never enforced: picks whose own card names another reader or
# turns this one away. FIX-15's audit reported zero of these because it read the
# pick's reason instead of the pick's card against the cell.
gate 1 python3 scripts/audit-pick-contradictions.py
# Advisory too: cards whose own prose puts them in a lower time bucket than their
# chip. The no-typed-numbers rule reached docs and UI strings but never the
# catalogue, and Attack 2 found the gap three times.
gate 1 python3 scripts/audit-time-chips.py

echo
echo "Done. Open index.html."
