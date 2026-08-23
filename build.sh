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

echo "1/5  stable ids (derived from URL, never from list position)"
python3 scripts/stable-ids.py

echo
echo "2/5  publisher names and the official flag"
python3 scripts/add-source.py | head -3

echo
echo "3/5  learning paths"
python3 scripts/build-paths.py | tail -3

echo
echo "4/5  search index"
python3 scripts/build-search-index.py --keywords

echo
echo "5/5  data as loadable javascript"
python3 scripts/build-data-js.py

echo
echo "Done. Open index.html."
