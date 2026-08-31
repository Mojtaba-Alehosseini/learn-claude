/* Arriving at Browse with a question already asked must answer it.
 *
 * The home page field builds `browse.html?q=<a sentence>` and sends the visitor
 * straight in. For a while nothing on that route loaded the ranked index, so the first
 * render fell through to the AND-substring match in browse.js and no English sentence
 * survived it: 7 of the 9 benchmark sentences below returned 0, and the same query
 * typed into the box one keystroke later returned the right answer. The count line then
 * blamed the role — "0 resources for a product manager" with 56 in the catalogue.
 *
 * scripts/test-search.py cannot catch that. It tests the ranking function, and the
 * ranking function was never the problem; the trigger was. So this runs the real
 * browse.js against a small DOM stub and asserts what a visitor actually sees.
 *
 *     node scripts/test-browse-query.js
 *
 * Exit 1 if any benchmark sentence returns nothing through a ?q= URL, if the index is
 * not requested before the first render, or if the count line attributes a search miss
 * to the role filter.
 *
 * The stub deliberately starts with window.LC_SEARCH_INDEX undefined, exactly as a
 * browser does, so search.js has to be asked for it. Setting it up front would make the
 * test pass without the fix.
 */

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const ROOT = path.dirname(__dirname);
const read = p => fs.readFileSync(path.join(ROOT, p), "utf8");

/* The same nine sentences scripts/test-search.py uses. Kept in step by hand; if that
   list changes and this one does not, the two tests disagree and that is visible. */
const BENCHMARK = [
  "help me write my thesis faster",
  "i keep getting generic answers",
  "how do i make claude read my pdfs",
  "where do i even start",
  "stop claude inventing fake citations",
  "build an agent that uses my own tools",
  "teach my class to use ai honestly",
  "clean up a messy spreadsheet",
  "how do i build an mcp server",
];

const ELEMENT_IDS = ["clearAll", "filtersPrimary", "filtersMore", "moreToggle", "moreGlyph",
  "q", "sort", "appliedChips", "count", "results", "empty", "picks", "openSheet", "closeSheet",
  "sheet", "sheetBody", "sheetConfirm"];

function fakeElement(id) {
  const el = {
    id, value: "", textContent: "", innerHTML: "", className: "", children: [],
    dataset: {}, style: {},
    classList: {
      _s: new Set(),
      add(c) { this._s.add(c); }, remove(c) { this._s.delete(c); },
      contains(c) { return this._s.has(c); },
      toggle(c, on) { on === undefined ? (this._s.has(c) ? this._s.delete(c) : this._s.add(c))
                                       : (on ? this._s.add(c) : this._s.delete(c)); },
    },
    addEventListener() {}, removeEventListener() {}, focus() {},
    setAttribute() {}, getAttribute() { return null; },
    querySelector() { return null; }, querySelectorAll() { return []; },
    closest() { return null; }, contains() { return false; },
    getClientRects() { return []; }, appendChild() {},
  };
  return el;
}

/* One page load. Returns what the visitor would see. */
function loadBrowse(search) {
  const els = {};
  ELEMENT_IDS.forEach(id => { els[id] = fakeElement(id); });

  const loadCalls = [];
  let firstRenderAt = null;
  let renders = 0;

  const sandbox = {
    console, URLSearchParams, Promise, setTimeout, clearTimeout, Math, JSON, Date, RegExp,
    location: { search, pathname: "/browse.html" },
    history: { replaceState() {} },
  };
  sandbox.window = sandbox;
  sandbox.self = sandbox;
  sandbox.document = {
    title: "",
    body: fakeElement("body"),
    head: { appendChild(node) { if (node.onload) node.onload(); } },
    activeElement: null,
    getElementById: id => els[id] || null,
    createElement: () => {
      /* search.js injects a <script> to fetch the index. Model that: the browser would
         run data/search-keywords.js, which sets window.LC_SEARCH_INDEX. Record the call
         so the test can prove the index was actually requested. */
      const node = { set src(v) { loadCalls.push(v); }, onload: null, onerror: null };
      return node;
    },
    addEventListener() {},
    querySelectorAll: () => [],
  };
  sandbox.matchMedia = () => ({ matches: false, addEventListener() {}, addListener() {} });

  const ctx = vm.createContext(sandbox);
  vm.runInContext(read("data/items.js"), ctx);
  vm.runInContext(read("data/paths.js"), ctx);
  vm.runInContext(read("assets/js/ui.js"), ctx);
  vm.runInContext(read("assets/js/search.js"), ctx);

  /* The index is NOT present at boot, exactly as in a browser. It arrives only when
     search.js asks for it, at which point the stubbed <script> "loads" it. */
  const indexSource = read("data/search-keywords.js");
  const realCreate = sandbox.document.createElement;
  sandbox.document.createElement = () => {
    const node = {
      set src(v) { loadCalls.push(v); },
      onload: null, onerror: null,
    };
    /* head.appendChild fires onload; run the index script first so onload sees it. */
    sandbox.document.head.appendChild = n => {
      vm.runInContext(indexSource, ctx);
      if (n.onload) n.onload();
    };
    return node;
  };

  /* Count renders by watching the element browse.js writes results into. */
  let resultsHTML = "";
  Object.defineProperty(els.results, "innerHTML", {
    get() { return resultsHTML; },
    set(v) {
      resultsHTML = v;
      renders++;
      if (firstRenderAt === null) firstRenderAt = loadCalls.length;
    },
  });

  vm.runInContext(read("assets/js/browse.js"), ctx);

  return new Promise(resolve => {
    setTimeout(() => {
      const cards = (resultsHTML.match(/class="card"/g) || []).length;
      resolve({
        cards,
        count: els.count.textContent,
        empty: els.empty.innerHTML,
        indexRequested: loadCalls.length > 0,
        indexRequestedBeforeFirstRender: firstRenderAt === null ? false : firstRenderAt > 0,
        renders,
      });
    }, 50);
  });
}

(async () => {
  let failures = 0;
  const fail = m => { console.log("FAIL  " + m); failures++; };
  const ok = m => console.log("ok    " + m);

  console.log("Arriving at browse.html?q=<sentence>, the way the home page sends you\n");

  for (const q of BENCHMARK) {
    const r = await loadBrowse("?q=" + encodeURIComponent(q));
    const label = '"' + q + '"';
    if (r.cards > 0 && r.indexRequestedBeforeFirstRender) {
      ok(label.padEnd(42) + r.cards + " result(s)");
    } else if (r.cards === 0) {
      fail(label.padEnd(42) + "0 results — " + (r.empty ? "empty state shown" : "nothing"));
    } else {
      fail(label.padEnd(42) + "results, but the index was not requested before the first render");
    }
  }

  console.log("");

  /* The second fault: a search miss must not be reported as a role miss. */
  /* Real words rank against the index; this is nonsense that matches nothing, checked
     with `python3 scripts/test-search.py "qqqzzz xxvvbb"` -> 0 results. */
  const miss = await loadBrowse("?role=pm&q=" + encodeURIComponent("qqqzzz xxvvbb"));
  if (miss.cards !== 0) {
    fail("expected the nonsense query to match nothing, got " + miss.cards);
  } else if (/resources for a product manager/.test(miss.count)) {
    fail('count blames the role for a search miss: "' + miss.count + '"');
  } else if (!/qqqzzz/.test(miss.count)) {
    fail('count does not mention the query that failed: "' + miss.count + '"');
  } else {
    ok('a search miss is attributed to the search, not the role: "' + miss.count + '"');
  }

  /* And a role with no query must keep its own sentence. */
  const roleOnly = await loadBrowse("?role=pm");
  if (/resources for a product manager/.test(roleOnly.count)) {
    ok('a role with no query still reads: "' + roleOnly.count + '"');
  } else {
    fail('role-only count changed unexpectedly: "' + roleOnly.count + '"');
  }

  console.log("");
  if (failures) {
    console.log(failures + " failure(s). A visitor arriving with a question is not being answered.");
    process.exit(1);
  }
  console.log("All " + BENCHMARK.length + " benchmark sentences answered through a ?q= URL.");
})();
