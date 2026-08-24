/* Learn Claude — shared vocabulary and rendering.
 *
 * Every page needs the same three things: the words we show for each stored value,
 * the resource card, and honest date handling. They live here so a label can never
 * drift between two screens.
 *
 * All display strings come from docs/design/ux-copy.md. If a word needs changing it
 * changes here and nowhere else.
 */

(function () {
  "use strict";

  var LC = {};

  /* ------------------------------------------------------------- labels ---- */

  LC.ROLE = {
    "non-technical": "not a coder", "student": "a student", "researcher": "a researcher",
    "teacher": "a teacher", "developer": "a developer", "data-analyst": "working with data",
    "pm": "a product manager", "designer": "a designer",
    "business-founder": "running a business", "writer-marketer": "a writer"
  };
  LC.LEVEL = {
    "never-used": "never used Claude", "basic": "used it a little",
    "confident": "used it a lot", "builder": "built things with it"
  };
  LC.TIME = {
    "under-15min": "15 minutes", "under-1hr": "one hour",
    "half-day": "a half day", "multi-day": "several days"
  };
  LC.COST = {
    "free": "free", "free-account": "free, sign-up needed",
    "paid-once": "pay once", "subscription": "subscription"
  };
  LC.FORMAT = {
    "video": "video", "course": "course", "docs": "docs", "article": "article",
    "hands-on": "hands-on", "podcast": "podcast", "repo": "code"
  };
  LC.TOPIC = {
    "chat-prompting": "chat and prompting", "claude-code": "Claude Code",
    "cowork": "Cowork", "skills": "Skills", "mcp": "connectors",
    "agents": "agents", "api": "API", "safety": "limits and safety"
  };

  /* Order is fixed and meaningful: most thoroughly checked first. */
  LC.TIER = {
    "reviewed":    { label: "Read in full", rank: 0, cls: "badge-reviewed",
                     tip: "We went through all of it, and a person checked the notes." },
    "ai-reviewed": { label: "Read by AI", rank: 1, cls: "badge-ai-reviewed",
                     tip: "AI read all of it. No person has checked the notes yet." },
    "previewed":   { label: "Skimmed", rank: 2, cls: "badge-previewed",
                     tip: "We read the outline or a free sample. We have not seen the whole thing." },
    "listed":      { label: "Found only", rank: 3, cls: "badge-listed",
                     tip: "We found it and sorted it. Nobody has looked at the content yet." }
  };

  LC.TIME_RANK = { "under-15min": 0, "under-1hr": 1, "half-day": 2, "multi-day": 3 };

  /* ---------------------------------------------------------- utilities ---- */

  var MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

  /* The apostrophe matters as much as the double quote. Not every value written through
     here lands between double quotes: the format icon below is interpolated into
     style="background:url('…')", where a single quote is the delimiter. Nothing in the
     catalogue contains one today, but an escaper that only covers the quote it happens
     to meet is the wrong escaper. */
  LC.esc = function (s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  };

  /* "2026-03-04" -> "4 Mar 2026". Returns "" for UNVERIFIED, never a guess. */
  LC.fmtDate = function (iso) {
    if (!iso || iso === "UNVERIFIED") return "";
    var m = /^(\d{4})-(\d{2})-(\d{2})/.exec(iso);
    if (!m) return "";
    return Number(m[3]) + " " + MONTHS[Number(m[2]) - 1] + " " + m[1];
  };

  /* Three date states, and the third is the common one.
   *
   * 176 of 353 resources publish no date at all — mostly documentation, which is
   * maintained continuously and simply does not print one. Saying nothing would let a
   * reader assume it is current; inventing a date would be worse. So we say we do not
   * know, and lean on `checked`, which we always know because we did it ourselves. */
  LC.freshness = function (item) {
    var out = { checked: "Checked " + LC.fmtDate(item.checked), note: "", cls: "" };
    if (item.status === "dead") {
      out.note = "This link no longer works";
      out.cls = "flag-dead";
      return out;
    }
    var pub = LC.fmtDate(item.published);
    if (!pub) {
      out.note = "No publish date given";
      out.cls = "";
      return out;
    }
    var age = (Date.now() - Date.parse(item.published)) / 86400000;
    if (age > 365) {
      out.note = "Published over a year ago — may not match Claude today";
      out.cls = "flag-outdated";
    } else {
      out.note = "Published " + pub;
    }
    return out;
  };

  LC.countText = function (n) {
    return n === 1 ? "1 resource" : n + " resources";
  };

  /* ------------------------------------------------------------- pieces ---- */

  LC.badge = function (tier) {
    var t = LC.TIER[tier] || LC.TIER.listed;
    return '<span class="badge ' + t.cls + '" title="' + LC.esc(t.tip) + '">' +
           LC.esc(t.label) + '</span>';
  };

  /* Named because it is the publisher, not the platform: a video on Anthropic's
     channel is from Anthropic, not "from YouTube". */
  LC.publisher = function (item) {
    var s = LC.esc(item.source || "");
    if (item.official) {
      return '<span class="publisher-official">' + s + '</span>';
    }
    return s;
  };

  /* "Anthropic Academy · Anthropic" says the same thing twice. Only show the author
     when it adds a name the publisher line does not already carry. */
  LC.authorLine = function (item) {
    var a = (item.author || "").trim(), src = (item.source || "").trim();
    if (!a || !src) return "";
    var al = a.toLowerCase(), sl = src.toLowerCase();
    if (al === sl || al.indexOf(sl) !== -1 || sl.indexOf(al) !== -1) return "";
    return " · " + LC.esc(a);
  };

  LC.chips = function (item) {
    return [LC.FORMAT[item.format] || item.format,
            LC.TIME[item.time] || item.time,
            LC.COST[item.cost] || item.cost]
      .map(function (c) { return '<span class="chip">' + LC.esc(c) + '</span>'; })
      .join("");
  };

  LC.href = function (item) { return "resource.html?id=" + encodeURIComponent(item.id); };

  /* --------------------------------------------------------------- card ---- */

  /* Fixed order, and it is not arbitrary: how well we checked it, what it is, what it
     costs you, who it helps, then who should not bother. `Skip if:` sits last and
     heaviest because it is the judgment nobody else on the internet gives you. */
  LC.card = function (item, opts) {
    opts = opts || {};
    var fresh = LC.freshness(item);
    var author = LC.authorLine(item);

    var pathLine = "";
    if (!opts.hidePath && item.paths && item.paths.length) {
      var p = item.paths[0];
      pathLine = '<span class="card-path">Step ' + p.step + ' of ' + p.of +
                 ' in ' + LC.esc(p.pathTitle || p.path) + '</span>';
    }

    var icon = '<span class="card-icon" aria-hidden="true" style="background:url(\'' +
               'assets/icons/formats/' + LC.esc(item.format) +
               '-alpha.png\') center/contain no-repeat"></span>';

    return '' +
      '<a class="card" href="' + LC.esc(LC.href(item)) + '">' +
        '<div class="card-top">' +
          '<div>' + LC.badge(item.tier) +
            '<div class="card-title">' + LC.esc(item.title) + '</div>' +
            '<div class="card-source meta">' + LC.publisher(item) + author + '</div>' +
          '</div>' + icon +
        '</div>' +
        '<div class="chip-row" style="margin-top:var(--space-12)">' + LC.chips(item) + '</div>' +
        '<p class="card-for"><strong>For:</strong> ' + LC.esc(item.who_for) + '</p>' +
        '<p class="card-skip"><span class="label">Skip if:</span> ' +
           LC.esc(item.skip_if) + '</p>' +
        pathLine +
        '<div class="card-foot">' +
          '<span>' + LC.esc(fresh.checked) + '</span>' +
          (fresh.note ? '<span class="' + fresh.cls + '">' + LC.esc(fresh.note) + '</span>' : '') +
        '</div>' +
      '</a>';
  };

  /* --------------------------------------------------------------- data ---- */

  /* Loaded from data/*.js as globals, so the site works opened straight from a folder
     as well as from a server. See scripts/build-data-js.py for why. */
  LC.items = function () {
    var raw = window.LC_ITEMS || [];
    var paths = window.LC_PATHS || [];
    var byId = {};
    paths.forEach(function (p) {
      p.steps.forEach(function (s) {
        (byId[s.item] = byId[s.item] || []).push(
          { path: p.id, step: s.step, of: p.step_count, pathTitle: p.title });
      });
    });
    return raw.map(function (x) {
      var c = Object.create(x);
      c.paths = byId[x.id] || x.paths || [];
      c.tierRank = (LC.TIER[x.tier] || LC.TIER.listed).rank;
      c.timeRank = LC.TIME_RANK[x.time] != null ? LC.TIME_RANK[x.time] : 9;
      c.sortDate = x.published && x.published !== "UNVERIFIED" ? x.published : "0000";
      return c;
    });
  };

  LC.paths = function () { return window.LC_PATHS || []; };

  LC.byId = function (id) {
    var all = LC.items();
    for (var i = 0; i < all.length; i++) if (all[i].id === id) return all[i];
    return null;
  };

  LC.param = function (name) {
    return new URLSearchParams(location.search).get(name) || "";
  };

  window.LC = LC;
})();
