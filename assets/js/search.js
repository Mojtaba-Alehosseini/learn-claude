/* Learn Claude — search.
 *
 * The index is built offline by scripts/build-search-index.py from the hidden fields
 * Gemini wrote for every resource: `keywords`, `questions` and `teaches`. Those are
 * deliberately written in the words a beginner types rather than the words a course
 * markets itself with, which is why a sentence like "stop claude inventing fake
 * citations" finds the hallucination guide even though they share no words.
 *
 * Everything here is plain text matching against a static file. No API call is made at
 * query time — not as an optimisation, but because a query-time embedding would need an
 * API key, and there is no way to put a key in a static page without giving it away.
 *
 * Measured on the eight benchmark sentences in scripts/test-search.py, keyword matching
 * alone puts the right resource first in seven of them. That is why the 532 KB of
 * embeddings are not loaded here: they cannot be used without a key, and the file we
 * can ship gets the ranking right on its own.
 */

(function () {
  "use strict";

  var INDEX_URL = "data/search-keywords.js";

  var STOP = ("a an and are as at be but by can do does for from get go had has have how i " +
    "if in into is it its me my not of on or our so than that the their them then there these " +
    "this to up us was we were what when where which who why will with you your").split(" ");
  var STOPSET = Object.create(null);
  STOP.forEach(function (w) { STOPSET[w] = 1; });

  var index = null;
  var loading = null;

  /* The stemmer, mirrored from scripts/stem.py rule for rule. Both sides must agree or
     the index and the query stop meeting: scripts/test-search-runtimes.js runs all 57
     suite queries through both and fails the build if a single top three differs.

     The two rules that were argued, in the same words as the spec: the -ate family is
     REMOVED rather than mapped to "at", because mapping leaves "citation" at "citat"
     while cite/cited/citing reach "cit"; and the minimum stem is 3, not 4, because
     "citation" -> "cit" is three characters. The third column is the minimum a rule may
     leave, which is 4 for the short -ate members so that "cheated" reaches "cheat"
     instead of "che". */
  var MIN_STEM = 3;
  var RULES = [
    ["ational", "ate", 3], ["ization", "ize", 3], ["isation", "ize", 3],
    ["iveness", "ive", 3], ["fulness", "ful", 3], ["ousness", "ous", 3],
    ["ations", "", 3], ["ation", "", 3],
    ["ating", "", 4], ["ated", "", 4], ["ates", "", 4], ["ate", "", 4],
    ["ions", "", 3], ["ion", "", 3],
    ["edly", "", 3], ["ies", "y", 3], ["ing", "", 3], ["ise", "ize", 3],
    ["ed", "", 3], ["es", "", 3], ["s", "", 3], ["e", "", 3]
  ];
  var IRREGULAR = {
    made: "mak", making: "mak", make: "mak", makes: "mak",
    wrote: "writ", written: "writ",
    ran: "run", run: "run", running: "run", runs: "run",
    found: "find", finding: "find", finds: "find", find: "find",
    taught: "teach", teaching: "teach", teaches: "teach", teach: "teach"
  };
  var DOUBLED = /([bdfgklmnprt])\1$/;

  function stem(word) {
    var w = String(word).toLowerCase();
    if (Object.prototype.hasOwnProperty.call(IRREGULAR, w)) return IRREGULAR[w];
    if (w.length <= MIN_STEM) return w;
    for (var pass = 0; pass < 4; pass++) {
      var before = w;
      for (var i = 0; i < RULES.length; i++) {
        var suffix = RULES[i][0], replacement = RULES[i][1], floor = RULES[i][2];
        if (w.length < suffix.length) continue;
        if (w.slice(w.length - suffix.length) !== suffix) continue;
        var cut = w.slice(0, w.length - suffix.length) + replacement;
        if (cut.length < Math.max(MIN_STEM, floor)) continue;
        if (replacement === "" && (suffix === "ing" || suffix === "ed") &&
            DOUBLED.test(cut)) {
          cut = cut.slice(0, -1);
        }
        w = cut;
        break;
      }
      if (w === before) break;
    }
    return w;
  }

  /* An expansion scores below the word the person typed. Same factor, same sentence, as
     the spec and as scripts/test-search.py. */
  var STEM_WEIGHT = 0.5;

  function words(s) {
    var out = [], m = String(s).toLowerCase().match(/[a-z0-9]+/g) || [];
    for (var i = 0; i < m.length; i++) {
      if (m[i].length > 1 && !STOPSET[m[i]]) out.push(m[i]);
    }
    return out;
  }

  /* Loaded on the first keystroke rather than with the page. The index is ~255 KB and
     most visitors filter by role instead of typing, so they never pay for it.
     Injected as a <script> rather than fetched, because fetch is blocked on file://
     and the site has to work opened straight from a folder. */
  function load() {
    if (index) return Promise.resolve(index);
    if (window.LC_SEARCH_INDEX) {
      index = window.LC_SEARCH_INDEX;
      return Promise.resolve(index);
    }
    if (loading) return loading;
    loading = new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = INDEX_URL;
      s.onload = function () {
        index = window.LC_SEARCH_INDEX;
        if (!index) { reject(new Error("index script loaded but set nothing")); return; }
        resolve(index);
      };
      s.onerror = function () { reject(new Error("could not load " + INDEX_URL)); };
      document.head.appendChild(s);
    }).catch(function (e) {
      loading = null;
      console.error("search index did not load:", e);
      throw e;
    });
    return loading;
  }

  /* Returns { byId: {id: score}, order: [id, ...] } best first, or null when the index
     is not ready. Callers fall back to plain substring matching until then. */
  function rank(query) {
    if (!index) return null;
    var q = String(query || "").toLowerCase().trim();
    if (!q) return null;

    var n = index.ids.length;
    var scores = new Float64Array(n);
    var exact = new Uint8Array(n);   // did this resource match a whole query word?
    var qw = words(q);

    for (var i = 0; i < qw.length; i++) {
      var w = qw[i];
      var posts = index.words[w];
      if (posts) {
        /* Inverse document frequency. On a site where every resource is about Claude,
           the word "claude" appears in nearly all of them and tells us nothing, while
           "citations" appears in a handful and tells us almost everything. Without this
           the common words dominate and a precise question returns most of the
           catalogue. */
        var idf = Math.log(n / posts.length);
        if (idf < 0.05) continue;          // in almost everything: pure noise
        for (var j = 0; j < posts.length; j++) {
          scores[posts[j][0]] += posts[j][1] * idf;
          if (idf > 0.7) exact[posts[j][0]] = 1;   // only a selective word admits
        }
      }
      /* Someone types "hallucinations" and the page says "hallucinated". The stem map
         holds only stems covering more than one word, and a stem hit ranks without
         admitting: a morphological cousin may lift a resource the reader's own word
         already found, and may never put one in front of them on its own. This replaces
         a 5-char prefix bonus whose own comment called it a stand-in for stemming. */
      /* One union across the whole stem group, scored once. Per-cousin IDF would pay a
         rare inflection far more than the family is worth. */
      var cousins = (index.stems && index.stems[stem(w)]) || [];
      var union = Object.create(null), any = false;
      for (var c2 = 0; c2 < cousins.length; c2++) {
        var p2 = index.words[cousins[c2]];
        if (!p2) continue;
        for (var m2 = 0; m2 < p2.length; m2++) {
          var pi = p2[m2][0];
          if (!(pi in union) || p2[m2][1] > union[pi]) { union[pi] = p2[m2][1]; any = true; }
        }
      }
      if (any) {
        var count = 0, kk;
        for (kk in union) count++;
        var idf2 = Math.log(n / count);
        if (idf2 >= 0.05) {
          for (kk in union) scores[kk] += union[kk] * idf2 * STEM_WEIGHT;
        }
      }
    }

    /* A whole phrase appearing in the query is a much stronger signal than its words
       appearing separately: "claude code" should beat "claude" plus "code". */
    for (var phrase in index.phrases) {
      if (q.indexOf(phrase) !== -1) {
        var ids = index.phrases[phrase];
        for (var z = 0; z < ids.length; z++) { scores[ids[z]] += 6; exact[ids[z]] = 1; }
      }
    }

    var best = 0;
    for (var a = 0; a < n; a++) if (scores[a] > best) best = scores[a];
    if (!best) return { byId: {}, order: [] };

    /* Two gates, and the first matters more. A prefix hit may *rank* a resource but
       must never *admit* one on its own, or "stop claude inventing fake citations"
       returns 252 rows and the count line quietly becomes a lie. To appear at all, a
       resource has to match a whole query word or phrase; then it also has to be
       within a reasonable fraction of the best hit. */
    var floor = Math.max(best * 0.30, 2.0);

    var keep = [];
    for (var b = 0; b < n; b++) if (exact[b] && scores[b] >= floor) keep.push(b);
    keep.sort(function (x, y) { return scores[y] - scores[x]; });

    var byId = Object.create(null), order = [];
    for (var c = 0; c < keep.length; c++) {
      var id = index.ids[keep[c]];
      byId[id] = scores[keep[c]];
      order.push(id);
    }
    return { byId: byId, order: order };
  }

  /* Guards against the index being built from a different items.json than the page
     loaded — the failure that silently scrambled the learning paths. */
  function check(items) {
    if (!index) return true;
    var have = {}, missing = 0;
    items.forEach(function (x) { have[x.id] = 1; });
    index.ids.forEach(function (id) { if (!have[id]) missing++; });
    if (missing) {
      console.error("search index is stale: " + missing + " of " + index.ids.length +
        " indexed ids are not in items.json. Run scripts/build-search-index.py");
      return false;
    }
    return true;
  }

  window.LCSearch = { load: load, rank: rank, check: check,
    ready: function () { return !!index; } };
})();
