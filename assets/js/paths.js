/* Paths — the index of routes, and a single route.
 *
 * Search finds you one thing. A path answers the question nobody else answers: in what
 * order. Each step therefore carries a `why` explaining why it sits at that position
 * and not another, and that sentence is ours — it gets the same weight `Skip if:` gets
 * on a card, because it is the same kind of judgment.
 *
 * One file serves both screens: with ?id= it draws that path, without it the index.
 */

(function () {
  "use strict";

  var LC = window.LC;
  var paths = LC.paths();
  var out = document.getElementById("content");

  function stepsWithItems(p) {
    return p.steps.map(function (s) {
      return { step: s, item: LC.byId(s.item) };
    }).filter(function (r) { return r.item; });
  }

  /* ---------------------------------------------------------------- index ---- */

  /* Every path in paths.json carries a `roles` list saying who it is for. Nothing read
     it. So a teacher arriving from the two questions was shown three paths, the first
     headed "Anyone", and never told which — if any — was hers; and the four roles with
     no path at all were never told that either, which is the more expensive half.
     A path that names someone and then hides from them is worse than no path. */
  function namesRole(p, role) {
    return (p.roles || []).indexOf(role) !== -1;
  }

  function whoFor(p) {
    var labels = (p.roles || []).map(function (r) { return LC.ROLE[r] || r; });
    if (!labels.length) return "";
    return '<p class="path-stats">For ' + LC.esc(labels.join(", ")) + '</p>';
  }

  function pathCard(p, role) {
    var rows = stepsWithItems(p);
    var href = "paths.html?id=" + encodeURIComponent(p.id) +
               (role ? "&role=" + encodeURIComponent(role) : "");
    return '<article class="path-header">' +
      '<h2 class="h2"><a href="' + LC.esc(href) + '">' + LC.esc(p.title) + '</a></h2>' +
      '<p class="prose" style="margin-top:var(--space-8)">' + LC.esc(p["for"]) + '</p>' +
      whoFor(p) +
      '<p class="path-stats">' + p.step_count + ' steps · ' +
        LC.esc(p.total_time_label) + ' · ' + LC.esc(p.cost) + '</p>' +
      '<ol class="chip-row" style="margin-top:var(--space-16)">' +
        rows.slice(0, 6).map(function (r, i) {
          return '<li class="chip">' + (i + 1) + '. ' +
                 LC.esc(r.item.title.slice(0, 44)) +
                 (r.item.title.length > 44 ? "…" : "") + '</li>';
        }).join("") +
      '</ol></article>';
  }

  function index(role) {
    if (!paths.length) {
      out.innerHTML = '<h1 class="h1">Paths</h1>' +
        '<div class="empty prose"><strong>No paths are ready yet.</strong>' +
        'We only publish a path once every step in it has been checked.</div>';
      return;
    }

    var label = role && LC.ROLE[role] ? LC.ROLE[role] : null;
    var mine = label ? paths.filter(function (p) { return namesRole(p, role); }) : [];
    var rest = label ? paths.filter(function (p) { return !namesRole(p, role); }) : paths;

    var html = '<h1 class="h1">Paths</h1>' +
      '<p class="lede" style="margin-top:var(--space-16)">A short list, in order. ' +
      'Start at the top.</p>';

    if (label && mine.length) {
      html += '<h2 class="h2" style="margin-top:var(--space-48)">For ' + LC.esc(label) +
              '</h2><div class="path-list" style="margin-top:var(--space-24)">' +
              mine.map(function (p) { return pathCard(p, role); }).join("") + '</div>';
    } else if (label) {
      /* Say it outright. Showing other people's routes and letting the reader work out
         that none of them is theirs is how the old page failed four roles at once. */
      html += '<div class="empty prose" style="margin-top:var(--space-32)">' +
              '<strong>There is no path for ' + LC.esc(label) + ' yet.</strong>' +
              'A path is only published once every step in it has been checked, and we ' +
              'have not finished one for you. Browse by role instead — ' +
              '<a href="browse.html?role=' + encodeURIComponent(role) + '">' +
              'everything we have for ' + LC.esc(label) + '</a>.</div>';
    }

    if (rest.length) {
      if (label) {
        html += '<h2 class="h2" style="margin-top:var(--space-48)">' +
                (mine.length ? "Other paths" : "The paths that do exist") + '</h2>';
      }
      html += '<div class="path-list" style="margin-top:var(--space-24)">' +
              rest.map(function (p) { return pathCard(p, role); }).join("") + '</div>';
    }

    html += '<p class="meta" style="margin-top:var(--space-48)">' +
            'We do not track your progress. Nothing here needs an account.</p>';
    out.innerHTML = html;
  }

  /* ----------------------------------------------------------- one path ---- */

  function one(p, role) {
    var rows = stepsWithItems(p);
    document.title = p.title + " — Learn Claude";
    var label = role && LC.ROLE[role] ? LC.ROLE[role] : null;

    var html = '<p class="meta"><a href="paths.html' +
      (role ? "?role=" + encodeURIComponent(role) : "") + '">← All paths</a></p>' +
      '<h1 class="h1" style="margin-top:var(--space-16)">' + LC.esc(p.title) + '</h1>' +
      '<p class="lede" style="margin-top:var(--space-16)">' + LC.esc(p.intro) + '</p>' +
      whoFor(p) +
      /* If they arrived as a role this path does not name, say so here rather than let
         them work through six steps written for somebody else. */
      (label && !namesRole(p, role)
        ? '<p class="prose" style="margin-top:var(--space-16)"><strong>This one is not ' +
          'written for ' + LC.esc(label) + '.</strong> You are welcome to follow it, but ' +
          'it was put together for someone else.</p>'
        : '') +
      '<p class="path-stats">' + p.step_count + ' steps · ' +
        LC.esc(p.total_time_label) + ' · ' + LC.esc(p.cost) + '</p>' +
      '<div class="step-list">';

    rows.forEach(function (r, i) {
      var it = r.item, fresh = LC.freshness(it);
      html += '<div class="step">' +
        '<div><span class="step-num">' + (i + 1) + '</span></div>' +
        '<div>' +
          '<p class="caption">Step ' + (i + 1) + '</p>' +
          '<h2 class="h2" style="margin-top:var(--space-4)">' +
            '<a href="' + LC.esc(LC.href(it)) + '">' + LC.esc(it.title) + '</a></h2>' +
          '<p class="card-source meta">' + LC.publisher(it) + '</p>' +
          '<div class="chip-row" style="margin-top:var(--space-12)">' +
            LC.badge(it.tier) + LC.chips(it) + '</div>' +
          /* Ours, and the reason the path exists. Serif, full size. */
          '<p class="step-why">' + LC.esc(r.step.why) + '</p>' +
          /* This view's one clay element, on step 1 only.
             A path is a sequence with a first step, so unlike Browse or the path index
             there genuinely is one thing to press, and the page had no verb on it at
             all. It is deliberately NOT on the path index: five cards exist there so
             the reader can choose between them, and colouring one is an argument that
             page is not making. Points at our own resource page rather than straight
             out, because that page carries the Skip if line and the report link, and
             sending someone past those is the whole thing this site exists to prevent. */
          (i === 0
            ? '<p style="margin-top:var(--space-16)">' +
              '<a class="btn btn-primary" href="' + LC.esc(LC.href(it)) + '">' +
              'Start with this</a></p>'
            : '') +
          '<p class="card-foot"><span>' + LC.esc(fresh.checked) + '</span>' +
            (fresh.note ? '<span class="' + fresh.cls + '">' + LC.esc(fresh.note) +
                          '</span>' : '') + '</p>' +
        '</div></div>';
    });

    html += '</div><p class="meta" style="margin-top:var(--space-32)">' +
            'We do not track your progress. Nothing here needs an account.</p>';
    out.innerHTML = html;
  }

  /* -------------------------------------------------------------------- go ---- */

  var id = LC.param("id");
  /* Carried through from Browse and from the two questions, so the index can answer
     "is any of this for me" instead of leaving the reader to guess. Ignored unless it
     is a role we actually have. */
  var role = LC.param("role");
  if (role && !LC.ROLE[role]) role = "";

  if (!id) { index(role); return; }

  var p = paths.filter(function (x) { return x.id === id; })[0];
  if (!p) {
    out.innerHTML = '<h1 class="h1">Paths</h1>' +
      '<div class="empty prose"><strong>This path isn\'t ready.</strong>' +
      'We only publish a path once every step in it has been checked. ' +
      '<a href="paths.html' + (role ? "?role=" + encodeURIComponent(role) : "") +
      '">See the paths that are ready</a>.</div>';
    return;
  }
  one(p, role);
})();
