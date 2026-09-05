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
  /* Short. A path step card puts this in a 200px tile corner next to a cost chip —
     "Sign-up needed" and "one hour" do not fit the same row, and they collided when
     tried. One vocabulary, not a chip variant: this same object drives the Browse
     filter rail and every card's chip row, so the words must read in all three
     places or they drift, which is the fault this file exists to prevent. */
  LC.TIME = {
    "under-15min": "15 min", "under-1hr": "1 hour",
    "half-day": "half a day", "multi-day": "several days"
  };
  /* "free, sign-up needed" was fine as a filter-panel label and too long for a path
     step tile: at 200px the tile cannot hold "free, sign-up needed" and "1 hour" on
     the same row, and it collided when tried. "Free" is also redundant on this one —
     every cost value in this catalogue that is not `free` is `free-account`,
     `paid-once` or `subscription`, so pairing it with the plain word "free" answers
     a question nobody who reads the chip is asking. */
  LC.COST = {
    "free": "free", "free-account": "sign-up needed",
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

  /* The card's second date line, shown only when a page tells us when it was last
     revised. "Updated" and not "Published": Intercom-templated pages - the whole Claude
     Help Center - print a last-updated date and never a publication date, and writing
     that into `published` would make the card state a publication date that is false.
     This string and docs/design/ux-copy.md change together. */
  LC.UPDATED_PREFIX = "Updated ";

  /* "Start with these three" on Browse. Every reader-facing string for the picks
     block lives here and in docs/design/ux-copy.md together, per the no-drift rule.
     The heading is count-dependent because one cell (a single-publisher pool) holds
     two picks, and a "three" heading over two cards would be the page miscounting
     in its own voice. "picked by AI" is the honesty label - same ladder as the tier
     badges, and nothing may imply a person chose. */
  LC.PICKS_UI = {
    heading3: "Start with these three",
    heading2: "Start with these two",
    by: "picked by AI",
    rest: "Everything else for you"
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
    if (m) { return Number(m[3]) + " " + MONTHS[Number(m[2]) - 1] + " " + m[1]; }
    /* A month with no day. Coursera prints "Last update: June 2026" and gives no day, so
       the card prints exactly that much and never invents one. The day is what is
       missing; the month is a fact and gets shown. */
    var mo = /^(\d{4})-(\d{2})$/.exec(iso);
    if (mo) { return MONTHS[Number(mo[2]) - 1] + " " + mo[1]; }
    return "";
  };

  /* Three date states, and the third is the common one.
   *
   * most of the catalogue publishes no date at all - the current figure is in
   * docs/STATUS.md, generated on every build. Measured once with
   *   python3 -c "import json;d=json.load(open('data/items.json',encoding='utf-8'));print(sum(1 for i in d if i.get('published')=='UNVERIFIED'),'of',len(d))"
   * The figure that stood here said 176 of 353 and had been wrong for some time; a bare
   * number in a comment rots silently, so this one carries the date it was taken and the
   * command that takes it again. Mostly documentation, which is
   * maintained continuously and simply does not print one. Saying nothing would let a
   * reader assume it is current; inventing a date would be worse. So we say we do not
   * know, and lean on `checked`, which we always know because we did it ourselves. */
  /* THE freshness rule. `published` is when a resource first appeared; `updated` is when
     its page was last revised, and only ever a real date - absent is the honest empty,
     never "UNVERIFIED".

     Age is measured from the LATER of the two, because that is the question the flag is
     actually asking: might this not match Claude today? A GOV.UK collection published in
     June 2025 and revised in May 2026 is not a year stale, and flagging it as such was
     wrong in substance while being right about `published`. One field was doing two jobs.

     scripts/pick-candidates.py has the same rule in Python, as `effective_date`, and its
     comment points back here. They cannot share code across two languages, so they share
     a name and a note instead. Change one, change the other. */
  LC.effectiveDate = function (item) {
    var p = item.published && item.published !== "UNVERIFIED" ? item.published : null;
    var u = item.updated && item.updated !== "UNVERIFIED" ? item.updated : null;
    if (p && u) { return u > p ? u : p; }
    return p || u || null;
  };

  /* A month-only date - "2026-06" - is what a page like Coursera actually gives: "Last
     update: June 2026", with no day. It is a fact, and the schema used to throw it away
     for not having a day, which is the schema being wrong rather than the page.

     For staleness it becomes the FIRST of that month: the earliest day the date could
     mean. Never round up applies here too - if June 2026 could mean the 1st or the 30th,
     the honest reading for "is this old?" is the one that makes it oldest. */
  LC.dateFloor = function (d) {
    if (!d) { return null; }
    return d.length === 7 ? d + "-01" : d;
  };

  LC.freshness = function (item) {
    var out = { checked: "Checked " + LC.fmtDate(item.checked), note: "", cls: "",
                updatedNote: "" };
    if (item.status === "dead") {
      out.note = "This link no longer works";
      out.cls = "flag-dead";
      return out;
    }

    var pub = LC.fmtDate(item.published);
    var upd = LC.fmtDate(item.updated);
    if (upd) { out.updatedNote = LC.UPDATED_PREFIX + upd; }

    var eff = LC.effectiveDate(item);
    if (!eff) {
      out.note = "No publish date given";
      out.cls = "";
      return out;
    }

    var age = (Date.now() - Date.parse(LC.dateFloor(eff))) / 86400000;
    if (age > 365) {
      /* D6. This used to REPLACE the date with the warning, so the one card where age
         decides was the one card that hid the number. Six of the ten Attack 2 agents
         found it, and the reason it matters is that the string covered 16 Aug 2023 and
         12 Jun 2025 identically - three years and fifteen months reading the same.
         The home page promises the date; the date is shown, and the warning stands
         beside it. Where the age comes from an `updated` and the page never gave a
         publication date, there is no number to show and the warning says only what it
         knows. */
      out.note = pub
        ? "Published " + pub + " · over a year ago, may not match Claude today"
        : "Over a year old — may not match Claude today";
      out.cls = "flag-outdated";
    } else if (pub) {
      out.note = "Published " + pub;
    } else {
      /* No publication date, but the page says when it was last revised. Saying nothing
         would imply we know nothing; saying "Published" would state a date the page
         never gave. So the card says neither, and the updated line carries the fact. */
      out.note = "No publish date given";
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

  /* The publisher's own mark, on a path step card, or nothing.
     The host-to-slug map is data/publisher-marks.json, built once by
     scripts/fetch-publisher-marks.py and mirrored here like every other data file — see
     scripts/build-data-js.py. Real means a file we hold: fetched at build time into
     assets/icons/publishers/<slug>.png, committed, never requested at render. A favicon
     service called per card would send every reader's browsing to a third party each
     time the page loads.
     Nine marks cover 61% of the catalogue, measured 2026-08-28. Every other host
     returns "" here and the corner stays empty. Initials in a lettered square were
     built and rejected — a lettered square is not a mark, it is an apology for not
     having one, and it would make 129 unrelated publishers look like they share a
     house style they do not share. */
  LC.publisherMark = function (item) {
    var marks = window.LC_PUBLISHER_MARKS || {};
    var host;
    try { host = new URL(item.url).hostname.replace(/^www\./, ""); }
    catch (e) { return ""; }
    var slug = marks[host];
    if (!slug) return "";
    return '<span class="sp-chip sp-mark"><img src="assets/icons/publishers/' +
           LC.esc(slug) + '.png" alt="" width="16" height="16"></span>';
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
     describe which of several hundred resources they meant loses most reports
     before they are made.
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
      /* This was a <span>. It is the only filled pill in the card's reading
         column, so it is the most eye-catching thing on the card, and it went
         nowhere - while the resource page linked the identical string. Two
         affordances for one string; now one. */
      pathLine = '<a class="card-path" href="paths.html?id=' +
                 encodeURIComponent(p.path) + '">Step ' + p.step + ' of ' + p.of +
                 ' in ' + LC.esc(p.pathTitle || p.path) + '</a>';
    }

    var icon = '<span class="card-icon" aria-hidden="true" style="background:url(\'' +
               'assets/icons/formats/' + LC.esc(item.format) +
               '-alpha.png\') center/contain no-repeat"></span>';

    /* An <article> holding ONE link, not one <a> wrapped round everything.
       Measured 2026-09-01 on browse: with the whole card as the anchor, each link's
       accessible name was every word on the card - 70 to 123 words, up to 689
       characters. A screen reader announced the tier, the publisher, three chips, the
       who_for, the whole skip_if and both dates as the NAME of one link, for every card
       in the list. The name is now the title alone; everything else stays readable as
       content. The whole card is still one click target: .card-title a::after spreads
       the link over the card, which is the same pattern the path step cards already use
       (see .sp-title a::after). Nothing moves on screen. */
    return '' +
      '<article class="card">' +
        '<div class="card-top">' +
          '<div>' + LC.badge(item.tier) +
            '<div class="card-title"><a href="' + LC.esc(LC.href(item)) + '">' +
              LC.esc(item.title) + '</a></div>' +
            '<div class="card-source meta">' + LC.publisher(item) + author + '</div>' +
          '</div>' + icon +
        '</div>' +
        '<div class="chip-row" style="margin-top:var(--space-12)">' + LC.chips(item) + '</div>' +
        /* A stripped card has no who_for at all. Under D1 a `listed` row carries a
           title, a link, a publisher and a format - the tier says nobody opened it, so
           there is nothing to say about who it helps. */
        (item.who_for
          ? '<p class="card-for"><strong>For:</strong> ' + LC.esc(item.who_for) + '</p>'
          : '') +
        '<p class="card-skip"><span class="label">Skip if:</span> ' +
           LC.esc(item.skip_if) + '</p>' +
        pathLine +
        '<div class="card-foot">' +
          '<span>' + LC.esc(fresh.checked) + '</span>' +
          (fresh.note ? '<span class="' + fresh.cls + '">' + LC.esc(fresh.note) + '</span>' : '') +
          (fresh.updatedNote ? '<span>' + LC.esc(fresh.updatedNote) + '</span>' : '') +
        '</div>' +
      '</article>';
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
