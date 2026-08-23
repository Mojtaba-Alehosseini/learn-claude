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

  function index() {
    if (!paths.length) {
      out.innerHTML = '<h1 class="h1">Paths</h1>' +
        '<div class="empty prose"><strong>No paths are ready yet.</strong>' +
        'We only publish a path once every step in it has been checked.</div>';
      return;
    }

    var html = '<h1 class="h1">Paths</h1>' +
      '<p class="lede" style="margin-top:var(--space-16)">A short list, in order. ' +
      'Start at the top.</p><div class="path-list" style="margin-top:var(--space-48)">';

    paths.forEach(function (p) {
      var rows = stepsWithItems(p);
      html += '<article class="path-header">' +
        '<h2 class="h2"><a href="paths.html?id=' + LC.esc(p.id) + '">' +
          LC.esc(p.title) + '</a></h2>' +
        '<p class="prose" style="margin-top:var(--space-8)">' + LC.esc(p["for"]) + '</p>' +
        '<p class="path-stats">' + p.step_count + ' steps · ' +
          LC.esc(p.total_time_label) + ' · ' + LC.esc(p.cost) + '</p>' +
        '<ol class="chip-row" style="margin-top:var(--space-16)">' +
          rows.slice(0, 6).map(function (r, i) {
            return '<li class="chip">' + (i + 1) + '. ' +
                   LC.esc(r.item.title.slice(0, 44)) +
                   (r.item.title.length > 44 ? "…" : "") + '</li>';
          }).join("") +
        '</ol></article>';
    });

    html += '</div><p class="meta" style="margin-top:var(--space-48)">' +
            'We do not track your progress. Nothing here needs an account.</p>';
    out.innerHTML = html;
  }

  /* ----------------------------------------------------------- one path ---- */

  function one(p) {
    var rows = stepsWithItems(p);
    document.title = p.title + " — Learn Claude";

    var html = '<p class="meta"><a href="paths.html">← All paths</a></p>' +
      '<h1 class="h1" style="margin-top:var(--space-16)">' + LC.esc(p.title) + '</h1>' +
      '<p class="lede" style="margin-top:var(--space-16)">' + LC.esc(p.intro) + '</p>' +
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
  if (!id) { index(); return; }

  var p = paths.filter(function (x) { return x.id === id; })[0];
  if (!p) {
    out.innerHTML = '<h1 class="h1">Paths</h1>' +
      '<div class="empty prose"><strong>This path isn\'t ready.</strong>' +
      'We only publish a path once every step in it has been checked. ' +
      '<a href="paths.html">See the paths that are ready</a>.</div>';
    return;
  }
  one(p);
})();
