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
   * 166 of 347 resources publish no date at all, measured 2026-08-27 with
   *   python3 -c "import json;d=json.load(open('data/items.json',encoding='utf-8'));print(sum(1 for i in d if i.get('published')=='UNVERIFIED'),'of',len(d))"
   * The figure that stood here said 176 of 353 and had been wrong for some time; a bare
   * number in a comment rots silently, so this one carries the date it was taken and the
   * command that takes it again. Mostly documentation, which is
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

  /* "What it teaches" is the first block on a resource page, and all 970 of its bullets
     came out of a model in lower case: "— start and organize conversations in claude".
     It reads as unfinished, and it is the first thing anyone sees.
     Fixed on the way to the screen rather than in the data. The bullets are generated,
     so rewriting 970 of them in items.json would only need doing again the next time
     they are regenerated, and it would bury a mechanical change inside 970 content
     diffs. The proper nouns are listed rather than guessed: capitalising every word
     would give Title Case, and capitalising none leaves "claude" in a sentence about
     Claude. Anything not on the list is left exactly as written. */
  var PROPER = {
    claude: "Claude", anthropic: "Anthropic", mcp: "MCP", github: "GitHub",
    api: "API", apis: "APIs", pdf: "PDF", pdfs: "PDFs", csv: "CSV", csvs: "CSVs",
    sql: "SQL", json: "JSON", ai: "AI", llm: "LLM", llms: "LLMs", excel: "Excel",
    slack: "Slack", figma: "Figma", zotero: "Zotero", youtube: "YouTube",
    obsidian: "Obsidian", notion: "Notion", jetbrains: "JetBrains", docker: "Docker",
    python: "Python", javascript: "JavaScript", jupyter: "Jupyter", cowork: "Cowork",
    "claude.md": "CLAUDE.md", ide: "IDE", cli: "CLI", ui: "UI", ux: "UX",
    seo: "SEO", pdfs: "PDFs", rag: "RAG", vscode: "VS Code"
  };

  LC.sentence = function (s) {
    var t = String(s == null ? "" : s);
    t = t.replace(/[A-Za-z][A-Za-z.]*/g, function (w) {
      var hit = PROPER[w.toLowerCase()];
      return hit && w === w.toLowerCase() ? hit : w;
    });
    return t.charAt(0).toUpperCase() + t.slice(1);
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

  /* Where a reader tells us something is wrong.
     how-we-check.html has said "Found something wrong? Tell us." since the site went up,
     and offered no way to tell anyone: zero mailto: and zero issue links across all five
     pages. The person who finds a dead link is looking at the dead link, so the report
     starts from there with the details already filled in. Sending them somewhere else to
     describe which of 347 resources they meant loses most reports before they are made.
     Quiet by design. This is not a call to action, it is an escape hatch for the one
     reader in a hundred who spots something. */
  var REPO = "https://github.com/Mojtaba-Alehosseini/learn-claude";
  var SITE = "https://mojtaba-alehosseini.github.io/learn-claude/";
  var NL = "\n";

  LC.reportUrl = function (item) {
    var title, lines;
    if (item) {
      title = "Problem with: " + item.title;
      lines = [
        "Resource: " + item.title,
        "Link:     " + item.url,
        "Our page: " + SITE + "resource.html?id=" + item.id,
        "",
        "What is wrong? A dead link, a description that does not match, something out of",
        "date, or written for someone else. A sentence is plenty.",
        "",
        "",
        "---",
        "Reported from the resource page, so the three lines above filled themselves in."
      ];
    } else {
      title = "Something is wrong on Learn Claude";
      lines = [
        "Which page or resource is this about?",
        "",
        "",
        "What is wrong?",
        "",
        "",
        "---",
        "Reported from " + SITE + "how-we-check.html"
      ];
    }
    return REPO + "/issues/new?title=" + encodeURIComponent(title) +
           "&body=" + encodeURIComponent(lines.join(NL));
  };

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
      /* byId is built from the live paths.json, so it is the whole truth about which
         steps exist. The `|| x.paths` fallback that used to sit here read a stored field
         instead whenever byId had no entry - which is precisely when the item is in no
         path at all, so the fallback only ever fired when it was wrong. Eight cards
         printed a step number for a path they were not in, with the raw slug on screen. */
      c.paths = byId[x.id] || [];
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
