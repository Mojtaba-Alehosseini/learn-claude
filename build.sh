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

echo
echo "Done. Open index.html."
