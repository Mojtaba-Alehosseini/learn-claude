/* One algorithm, two runtimes — proved on the whole suite, not on a sample.
 *
 *     python3 scripts/test-search.py --emit tmp/py-top3.json
 *     node scripts/test-search-runtimes.js tmp/py-top3.json
 *
 * scripts/test-search.py and assets/js/search.js implement the same ranking twice, in two
 * languages, and every round adds something they both have to learn: stemming, spelling
 * groups, synonym expansion, a tie-break. The suite only ever ran the Python one, so a
 * browser that disagreed would have shipped unnoticed — and one did. Before the tie-break
 * existed, Python and the browser returned different first results for "hallucinated
 * references": same index, same scores, two sort implementations, two answers.
 *
 * Amendment 3 to the spec: all 57 queries, not ten samples. The drift this exists to catch
 * is exactly the kind that shows up on the queries nobody would have chosen as a sample.
 */

"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const ROOT = path.resolve(__dirname, "..");
const read = p => fs.readFileSync(path.join(ROOT, p), "utf8");

function loadBrowserRanker() {
  const sandbox = { console, Promise, Math, JSON, Object, Array, Float64Array,
    Uint8Array, Int32Array, RegExp, String, Number };
  sandbox.window = sandbox;
  sandbox.self = sandbox;
  sandbox.document = {
    head: { appendChild(node) { if (node.onload) node.onload(); } },
    createElement: () => ({ set src(v) {}, onload: null, onerror: null }),
  };
  const ctx = vm.createContext(sandbox);
  /* The index the browser would have loaded, handed over directly. */
  sandbox.LC_SEARCH_INDEX = JSON.parse(read("data/search-keywords.json"));
  vm.runInContext(read("assets/js/search.js"), ctx);
  sandbox.LCSearch.load();
  return sandbox.LCSearch;
}

function main() {
  const emitted = process.argv[2];
  if (!emitted) {
    console.error("usage: node scripts/test-search-runtimes.js <python top-3 json>");
    console.error("produce it with: python3 scripts/test-search.py --emit <path>");
    return 2;
  }
  const expected = JSON.parse(fs.readFileSync(emitted, "utf8"));
  const search = loadBrowserRanker();

  const differ = [];
  for (const row of expected.queries) {
    const ranked = search.rank(row.query);
    const mine = (ranked ? ranked.order : []).slice(0, 3);
    const theirs = row.top3;
    if (mine.length !== theirs.length || mine.some((id, i) => id !== theirs[i])) {
      differ.push({ query: row.query, role: row.role, python: theirs, browser: mine });
    }
  }

  console.log(`Runtimes: ${expected.queries.length} queries through both rankers.`);
  if (differ.length === 0) {
    console.log("Python and the browser return the same top three for every one.");
    return 0;
  }
  console.log(`${differ.length} query/queries where they disagree:`);
  for (const d of differ) {
    console.log(`  "${d.query}" (${d.role})`);
    console.log(`      python : ${d.python.join(", ") || "(nothing)"}`);
    console.log(`      browser: ${d.browser.join(", ") || "(nothing)"}`);
  }
  console.log("");
  console.log("The site and its test are not running the same algorithm. Whichever is");
  console.log("right, the other one is what a visitor gets.");
  return 1;
}

process.exit(main());
