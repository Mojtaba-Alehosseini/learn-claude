/* Browse — filtering, search, sorting, and the mobile sheet.
 *
 * State lives in the URL. That is not a detail: it means a filtered view can be sent to
 * someone, bookmarked, or reached from the home screen's two questions, and the back
 * button behaves the way a reader expects rather than dumping them at an empty list.
 *
 * Filtering is synchronous over an in-memory array of ~350 rows, which is fast enough
 * that there is no spinner anywhere in this file. Speed is the feature; a loading state
 * would advertise the opposite.
 */

(function () {
  "use strict";

  var LC = window.LC;

  var AXES = [
    { key: "roles",     param: "role",     label: "Role",   labels: LC.ROLE,   icons: true,  primary: true },
    { key: "levels",    param: "level",    label: "Level",  labels: LC.LEVEL,  primary: true },
    { key: "times",     param: "time",     label: "Time",   labels: LC.TIME,   primary: true },
    { key: "topics",    param: "topic",    label: "Topic",  labels: LC.TOPIC },
    { key: "formats",   param: "format",   label: "Format", labels: LC.FORMAT },
    { key: "costs",     param: "cost",     label: "Cost",   labels: LC.COST },
    /* Single checkbox, not a picklist — "official" only has one meaningful state to
       filter on. It reuses the same axis machinery (matches/toggle/URL/chip) rather
       than a one-off branch, so it behaves like every other filter for free. */
    { key: "officials", param: "official", label: "Source", labels: { yes: "Official Anthropic only" } }
  ];

  var items = [];
  var sel = { roles: [], levels: [], times: [], topics: [], formats: [], costs: [], officials: [] };
  var q = "";
  var sort = "best";
  var moreOpen = false;

  var el = {};
  ["clearAll", "filtersPrimary", "filtersMore", "moreToggle", "moreGlyph", "q", "sort",
   "appliedChips", "count", "results", "empty", "openSheet", "closeSheet", "sheet",
   "sheetBody", "sheetConfirm"].forEach(function (id) {
    el[id] = document.getElementById(id);
  });

  /* ----------------------------------------------------------- URL state ---- */

  function readURL() {
    var p = new URLSearchParams(location.search);
    AXES.forEach(function (a) {
      var v = p.get(a.param);
      sel[a.key] = v ? v.split(",").filter(function (x) { return a.labels[x]; }) : [];
    });
    q = p.get("q") || "";
    sort = p.get("sort") || "best";
    el.q.value = q;
    el.sort.value = sort;
  }

  function writeURL() {
    var p = new URLSearchParams();
    AXES.forEach(function (a) {
      if (sel[a.key].length) p.set(a.param, sel[a.key].join(","));
    });
    if (q) p.set("q", q);
    if (sort !== "best") p.set("sort", sort);
    var s = p.toString();
    history.replaceState(null, "", s ? "?" + s : location.pathname);
  }

  /* ----------------------------------------------------------- filtering ---- */

  function anyFilters() {
    return AXES.some(function (a) { return sel[a.key].length > 0; });
  }

  function matches(it, ranked) {
    for (var i = 0; i < AXES.length; i++) {
      var a = AXES[i], chosen = sel[a.key];
      if (!chosen.length) continue;
      var val = a.key === "roles" ? it.roles
              : a.key === "topics" ? it.topics
              : a.key === "levels" ? [it.level]
              : a.key === "times" ? [it.time]
              : a.key === "formats" ? [it.format]
              : a.key === "officials" ? [it.official ? "yes" : "no"]
              : [it.cost];
      var hit = false;
      for (var j = 0; j < val.length; j++) if (chosen.indexOf(val[j]) !== -1) hit = true;
      if (!hit) return false;
    }
    if (!q.trim()) return true;
    if (ranked) return ranked.byId[it.id] !== undefined;
    /* Until the index has loaded, fall back to plain substring so typing is never dead. */
    var hay = (it.title + " " + it.summary + " " + it.who_for + " " + it.source).toLowerCase();
    return q.toLowerCase().split(/\s+/).every(function (t) { return hay.indexOf(t) !== -1; });
  }

  function results() {
    var ranked = (q.trim() && window.LCSearch) ? window.LCSearch.rank(q) : null;
    var out = items.filter(function (it) { return matches(it, ranked); });

    out.sort(function (a, b) {
      /* Someone who typed a sentence asked a question. Relevance is the only honest
         answer to it, so it overrides the catalogue ordering. */
      if (ranked && sort === "best") {
        var d = (ranked.byId[b.id] || 0) - (ranked.byId[a.id] || 0);
        if (d) return d;
        return a.tierRank - b.tierRank;
      }
      if (sort === "newest") {
        if (a.sortDate !== b.sortDate) return a.sortDate < b.sortDate ? 1 : -1;
        return a.tierRank - b.tierRank;
      }
      if (sort === "shortest") {
        return a.timeRank - b.timeRank || a.tierRank - b.tierRank ||
               a.title.localeCompare(b.title);
      }
      return a.tierRank - b.tierRank ||
             (b.checked || "").localeCompare(a.checked || "") ||
             a.title.localeCompare(b.title);
    });
    return out;
  }

  /* --------------------------------------------------------------- views ---- */

  function optionHTML(a, value) {
    var on = sel[a.key].indexOf(value) !== -1;
    var icon = "";
    if (a.icons) {
      var lv = sel.levels[0] || "never-used";
      icon = '<span class="filter-icon" aria-hidden="true" style="background-image:url(\'' +
             'assets/icons/roles/' + value + '/' + lv + '.png\')"></span>';
    }
    return '<button type="button" class="filter-option" role="checkbox" ' +
           'aria-checked="' + on + '" data-axis="' + a.key + '" data-value="' + value + '">' +
           '<span class="filter-box" aria-hidden="true">' + (on ? "✓" : "") + '</span>' +
           icon + '<span>' + LC.esc(a.labels[value]) + '</span></button>';
  }

  function groupHTML(a) {
    return '<div class="filter-group" role="group" aria-label="' + a.label + '">' +
           '<h3 class="caption">' + a.label + '</h3>' +
           Object.keys(a.labels).map(function (v) { return optionHTML(a, v); }).join("") +
           '</div>';
  }

  function renderFilters() {
    el.filtersPrimary.innerHTML =
      AXES.filter(function (a) { return a.primary; }).map(groupHTML).join("");
    el.filtersMore.innerHTML =
      AXES.filter(function (a) { return !a.primary; }).map(groupHTML).join("");
    el.filtersMore.classList.toggle("hidden", !moreOpen);
    el.moreToggle.setAttribute("aria-expanded", String(moreOpen));
    el.moreGlyph.textContent = moreOpen ? "−" : "+";
    el.clearAll.classList.toggle("hidden", !anyFilters());

    /* The sheet is the same controls, so it is built from the same function rather
       than a second copy that can drift out of step. */
    el.sheetBody.innerHTML = AXES.map(groupHTML).join("");
  }

  function renderChips() {
    var html = "";
    AXES.forEach(function (a) {
      sel[a.key].forEach(function (v) {
        html += '<button type="button" class="chip-applied" data-remove="' + a.key +
                '" data-value="' + v + '" aria-label="Remove filter: ' +
                LC.esc(a.labels[v]) + '">' + LC.esc(a.labels[v]) +
                ' <span aria-hidden="true">×</span></button>';
      });
    });
    el.appliedChips.innerHTML = html;
  }

  /* The count is exact and never rounded. When it gets low it also offers the way out,
     because a dead end with no suggestion is the most common way a filter UI fails. */
  function renderCount(n) {
    /* A search narrows the list as much as any filter does, so it has to be part of
       this sentence. Leaving it out produced a confident falsehood: with a role chosen
       and a query that matched nothing, the line read "0 resources for a product
       manager" while the catalogue held 56 of them. The zero came from the search, and
       the sentence blamed the role. */
    var searching = !!q.trim();
    var onlyRole = !searching &&
                   sel.roles.length && !sel.levels.length && !sel.times.length &&
                   !sel.topics.length && !sel.formats.length && !sel.costs.length &&
                   !sel.officials.length;
    var text = LC.countText(n);
    if (onlyRole && sel.roles.length === 1) {
      text = n + " resources for " + LC.ROLE[sel.roles[0]];
    } else if (searching) {
      /* The applied-filter chips already show which role is on, so naming it again here
         only makes a live-region announcement longer. Attribute the count to the query
         and let the chips speak for the filters. */
      text = LC.countText(n) + " for “" + q.trim() + "”";
    }
    if (n > 0 && n <= 6 && anyFilters()) text += ". Remove a filter to see more.";
    el.count.textContent = text;
    el.sheetConfirm.textContent = n === 1 ? "Show 1 resource" : "Show " + n + " resources";
  }

  function renderEmpty(n) {
    if (n) { el.empty.innerHTML = ""; return; }
    var msg;
    if (q.trim()) {
      /* <bdi> around the query. It is the reader's text, not ours, and it can be
         right-to-left: a Persian search sat inside our left-to-right sentence and put
         its punctuation on the wrong side. bdi isolates it without guessing a
         direction. */
      /* Two different dead ends, and they need two different ways out. Telling someone
         who arrived with a role already applied to "browse by role instead" sends them
         back to what they were doing when they got stuck; the useful move there is to
         drop the role and search everything. */
      msg = "<strong>No match for “<bdi>" + LC.esc(q) + "</bdi>”.</strong>" +
            (sel.roles.length
              ? "Try fewer words, or clear the role filter to search all " +
                items.length + "."
              : "Try fewer words, or browse by role instead.");
    } else if (sel.roles.length && !anyOtherThanRole()) {
      msg = "<strong>We have not covered this role yet.</strong>" +
            "It's on the list. Browse everything instead.";
    } else {
      msg = "<strong>Nothing matches all of those.</strong>" +
            "Try removing one filter — time is usually the one to loosen.";
    }
    el.empty.innerHTML = '<div class="empty prose">' + msg + '</div>';
  }

  function anyOtherThanRole() {
    return sel.levels.length || sel.times.length || sel.topics.length ||
           sel.formats.length || sel.costs.length || sel.officials.length;
  }

  function render() {
    var out = results();
    renderFilters();
    renderChips();
    renderCount(out.length);
    renderEmpty(out.length);
    el.results.innerHTML = out.map(function (it) { return LC.card(it); }).join("");
    document.title = "Browse " + out.length + " Claude resources — Learn Claude";
    writeURL();
  }

  /* --------------------------------------------------------------- events ---- */

  function toggle(axis, value) {
    var a = sel[axis], i = a.indexOf(value);
    if (i === -1) a.push(value); else a.splice(i, 1);
    render();
  }

  document.addEventListener("click", function (e) {
    var opt = e.target.closest("[data-axis]");
    if (opt) { toggle(opt.dataset.axis, opt.dataset.value); return; }
    var rm = e.target.closest("[data-remove]");
    if (rm) { toggle(rm.dataset.remove, rm.dataset.value); return; }
  });

  el.moreToggle.addEventListener("click", function () { moreOpen = !moreOpen; render(); });

  el.clearAll.addEventListener("click", function () {
    AXES.forEach(function (a) { sel[a.key] = []; });
    render();
  });

  var searchAsked = false;

  /* Wait for a gap in the typing before redrawing.
     A redraw is not cheap: it re-filters every item, rebuilds both filter panels and
     every card, rewrites the title, and calls history.replaceState. Doing all of that
     per keystroke had three costs beyond the work itself. The result count lives in an
     aria-live region, so every letter announced a new number over the last one. Safari
     throttles replaceState at roughly 100 calls in 30 seconds, which a long query
     reaches. And on mobile with the sheet open, rebuilding the sheet body dropped focus
     to the document until the next Tab.
     150ms is below the point where a redraw reads as delayed, and no CSS transition is
     paired with this, so there is no duration it has to match. */
  var TYPING_PAUSE = 150;
  var typingTimer = null;

  el.q.addEventListener("input", function (e) {
    q = e.target.value;
    clearTimeout(typingTimer);
    typingTimer = setTimeout(function () {
      render();
      /* Fetch the ranked index on the first keystroke, then redraw when it lands so the
         very first thing typed still gets a ranked answer. */
      if (q && window.LCSearch && !window.LCSearch.ready() && !searchAsked) {
        searchAsked = true;
        window.LCSearch.load().then(render).catch(function () {});
      }
    }, TYPING_PAUSE);
  });

  el.sort.addEventListener("change", function (e) { sort = e.target.value; render(); });

  function openSheet() {
    el.sheet.classList.remove("hidden");
    document.body.style.overflow = "hidden";
    el.closeSheet.focus();
  }
  function closeSheet() {
    el.sheet.classList.add("hidden");
    document.body.style.overflow = "";
    el.openSheet.focus();
  }
  el.openSheet.addEventListener("click", openSheet);
  el.closeSheet.addEventListener("click", closeSheet);
  el.sheetConfirm.addEventListener("click", closeSheet);

  /* Everything the Tab key is allowed to reach inside the sheet.
     Read fresh on every keypress, never cached: render() rebuilds the filter controls
     inside the sheet each time a box is ticked, so a cached list goes stale at once. */
  var SHEET_STOPS = 'a[href], button:not([disabled]), input:not([disabled]), ' +
                    'select:not([disabled]), textarea:not([disabled]), ' +
                    '[tabindex]:not([tabindex="-1"])';

  function sheetStops() {
    return Array.prototype.filter.call(
      el.sheet.querySelectorAll(SHEET_STOPS),
      function (n) { return n.getClientRects().length > 0; }
    );
  }

  /* Escape closes the sheet. Tab stays inside it.
     aria-modal="true" is on the sheet already, and it does not do the second job — it
     tells a screen reader to keep its virtual cursor in the dialog, and has no effect on
     the Tab key. Without this, Tab walks out of the sheet and into the 400-odd links of
     the page behind, which is still fully focusable under a position:fixed panel. The
     focus ring then sits under the sheet, where nobody can see it. */
  document.addEventListener("keydown", function (e) {
    if (el.sheet.classList.contains("hidden")) return;

    if (e.key === "Escape") { closeSheet(); return; }
    if (e.key !== "Tab") return;

    var stops = sheetStops();
    if (!stops.length) return;
    var first = stops[0], last = stops[stops.length - 1];

    /* Focus can start outside the sheet — a click on the page behind puts it there.
       Send it back in rather than let Tab carry on down the page. */
    if (!el.sheet.contains(document.activeElement)) {
      e.preventDefault();
      first.focus();
      return;
    }
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  });

  /* ----------------------------------------------------------------- go ---- */

  items = LC.items();
  if (!items.length) {
    el.count.textContent = "";
    el.empty.innerHTML = '<div class="empty prose"><strong>The directory didn\'t load.</strong>' +
      'Reload the page. If it keeps happening, the site is broken and we want to know.</div>';
    return;
  }
  readURL();

  /* A visitor can arrive here with the question already asked — the home page field
     builds browse.html?q=<a sentence> and sends them straight in. Until now nothing on
     that route loaded the ranked index, so the first render fell through to the
     AND-substring match at the top of this file, which no English sentence survives.
     Measured before this line existed: 7 of the 9 benchmark sentences in
     scripts/test-search.py returned 0 that way, and the same query typed into the box
     one keystroke later returned the right answer.
     So: when there is a query, fetch the index before the first render rather than
     after it. Rendering first and correcting afterwards would only replace a wrong
     answer with a flicker. If the index cannot be fetched, render anyway — the
     substring fallback is poor but it is better than a blank page. */
  if (q.trim() && window.LCSearch && !window.LCSearch.ready()) {
    searchAsked = true;
    el.count.textContent = "Searching…";
    window.LCSearch.load().then(render).catch(render);
  } else {
    render();
  }
})();
