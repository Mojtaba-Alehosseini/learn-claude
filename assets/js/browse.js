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
    { key: "roles",   param: "role",   label: "Role",   labels: LC.ROLE,   icons: true,  primary: true },
    { key: "levels",  param: "level",  label: "Level",  labels: LC.LEVEL,  primary: true },
    { key: "times",   param: "time",   label: "Time",   labels: LC.TIME,   primary: true },
    { key: "topics",  param: "topic",  label: "Topic",  labels: LC.TOPIC },
    { key: "formats", param: "format", label: "Format", labels: LC.FORMAT },
    { key: "costs",   param: "cost",   label: "Cost",   labels: LC.COST }
  ];

  var items = [];
  var sel = { roles: [], levels: [], times: [], topics: [], formats: [], costs: [] };
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
    var onlyRole = sel.roles.length && !sel.levels.length && !sel.times.length &&
                   !sel.topics.length && !sel.formats.length && !sel.costs.length;
    var text = LC.countText(n);
    if (onlyRole && sel.roles.length === 1) {
      text = n + " resources for " + LC.ROLE[sel.roles[0]];
    }
    if (n > 0 && n <= 6 && anyFilters()) text += ". Remove a filter to see more.";
    el.count.textContent = text;
    el.sheetConfirm.textContent = n === 1 ? "Show 1 resource" : "Show " + n + " resources";
  }

  function renderEmpty(n) {
    if (n) { el.empty.innerHTML = ""; return; }
    var msg;
    if (q.trim()) {
      msg = "<strong>No match for “" + LC.esc(q) + "”.</strong>" +
            "Try fewer words, or browse by role instead.";
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
           sel.formats.length || sel.costs.length;
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
  el.q.addEventListener("input", function (e) {
    q = e.target.value;
    render();
    /* Fetch the ranked index on the first keystroke, then redraw when it lands so the
       very first thing typed still gets a ranked answer. */
    if (q && window.LCSearch && !window.LCSearch.ready() && !searchAsked) {
      searchAsked = true;
      window.LCSearch.load().then(render).catch(function () {});
    }
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
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && !el.sheet.classList.contains("hidden")) closeSheet();
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
  render();
})();
