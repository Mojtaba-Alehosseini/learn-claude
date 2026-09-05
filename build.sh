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
cd "$(dirname "$0")"

echo "1/6  stable ids (derived from URL, never from list position)"
python3 scripts/stable-ids.py

echo
echo "2/6  publisher names and the official flag"
python3 scripts/add-source.py | head -3

echo
echo "3/6  learning paths"
python3 scripts/build-paths.py | tail -3

echo
echo "4/6  search index"
python3 scripts/build-search-index.py --keywords
# Fifty-seven sentences ten hostile strangers actually typed at the site, with the
# result each of them got. Twenty-two are asserted; the rest are recorded failures,
# and the run says so out loud rather than hiding them. Exits 1 only when a query
# that used to work stops working.
python3 scripts/test-search.py | tail -2
# One algorithm, two runtimes, all 57 queries. Amendment 3 to the search spec: ten samples
# is a place for drift to hide, and Python and the browser had already disagreed once.
python3 scripts/test-search.py --emit tmp/py-top3.json > /dev/null
node scripts/test-search-runtimes.js tmp/py-top3.json | tail -1
# Every synonym row carries the reason it exists, like every skip_if.
python3 scripts/validate-synonyms.py
# The stemmer's word families, taken from the failing suite lines.
python3 scripts/test-stem.py | tail -1

echo
echo "4b/6 sitemap, generated rather than typed"
python3 scripts/build-sitemap.py

echo
echo "5/6  data as loadable javascript"
python3 scripts/build-data-js.py

echo
echo "6/6  measured status, and the freshness exclusions"
# Writes docs/STATUS.md, which THE-PROJECT.md and README point at instead of repeating
# the numbers. It also prints every live resource the freshness rule keeps out of the
# picks pools: that exclusion used to be silent, and a wrong date once hid a live
# resource from every pool for ten months without one step going red.
python3 scripts/measure.py --status
python3 scripts/test-measure.py > /dev/null
# Four sentences the site is not allowed to say again - see D2 in FIX-24.md.
python3 scripts/test-copy-claims.py
# The no-typed-numbers rule, reaching picks.json at last. A pick's reason ships on the
# card, and eleven of them were counting pools that had moved underneath them.
python3 scripts/check-typed-numbers.py | tail -1
# Advisory, printed, never enforced: picks whose own card names another reader or
# turns this one away. FIX-15's audit reported zero of these because it read the
# pick's reason instead of the pick's card against the cell.
python3 scripts/audit-pick-contradictions.py | tail -1
# Advisory too: cards whose own prose puts them in a lower time bucket than their
# chip. The no-typed-numbers rule reached docs and UI strings but never the
# catalogue, and Attack 2 found the gap three times.
python3 scripts/audit-time-chips.py | tail -1

echo
echo "Done. Open index.html."
