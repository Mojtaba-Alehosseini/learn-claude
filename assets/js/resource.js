/* One resource.
 *
 * The page has one job: give someone enough to decide whether to spend their time,
 * then get out of the way. So the order runs decide-first — what it teaches, who it
 * helps, who should not bother — and the outward link is the only clay element.
 *
 * Optional sections are omitted entirely rather than shown empty. Most resources have
 * no prerequisites and are not in a path, and a page full of "None" reads as broken.
 */

(function () {
  "use strict";

  var LC = window.LC;
  var out = document.getElementById("content");

  var item = LC.byId(LC.param("id"));

  if (!item) {
    out.innerHTML = '<h1 class="h1">Not found</h1>' +
      '<div class="empty prose"><strong>We could not find that resource.</strong>' +
      'It may have been removed. <a href="browse.html">Browse everything</a> instead.</div>';
    return;
  }

  document.title = item.title + " — Learn Claude";

  var fresh = LC.freshness(item);
  var author = item.author && item.author !== item.source
    ? " · " + LC.esc(item.author) : "";

  function list(title, arr) {
    if (!arr || !arr.length) return "";
    return '<section class="section"><h2 class="h2">' + title + '</h2><ul class="prose">' +
      arr.map(function (s) {
        return '<li style="margin-top:var(--space-8)">— ' + LC.esc(s) + '</li>';
      }).join("") + '</ul></section>';
  }

  /* Where this sits in a route, if it sits in one. Someone who arrived from search
     should be told there is an order they are stepping into the middle of. */
  var pathBlock = "";
  if (item.paths && item.paths.length) {
    pathBlock = item.paths.map(function (p) {
      return '<section class="section"><h2 class="h2">Where this fits</h2>' +
        '<p class="prose">This is step ' + p.step + ' of ' + p.of + ' in ' +
        '<a href="paths.html?id=' + LC.esc(p.path) + '">' +
        LC.esc(p.pathTitle || p.path) + '</a>. The order matters — the path says why.</p>' +
        '</section>';
    }).join("");
  }

  var tier = LC.TIER[item.tier] || LC.TIER.listed;

  out.innerHTML = '' +
    '<p class="meta"><a href="browse.html">← Back to browse</a></p>' +

    '<div class="resource-head" style="margin-top:var(--space-24)">' +
      '<div class="chip-row">' + LC.badge(item.tier) + '</div>' +
      '<h1 class="h1" style="margin-top:var(--space-12)">' + LC.esc(item.title) + '</h1>' +
      '<p class="meta" style="margin-top:var(--space-8)">' +
        LC.publisher(item) + author + '</p>' +
      '<div class="chip-row" style="margin-top:var(--space-16)">' + LC.chips(item) + '</div>' +
      '<p class="prose" style="margin-top:var(--space-24)">' + LC.esc(item.summary) + '</p>' +
    '</div>' +

    '<div class="resource-actions">' +
      '<a class="btn btn-primary" href="' + LC.esc(item.url) + '" ' +
         'target="_blank" rel="noopener noreferrer">Open on ' + LC.esc(item.source) + '</a>' +
      '<button type="button" class="btn btn-secondary" id="copy">Copy link</button>' +
    '</div>' +

    (item.status === "dead"
      ? '<p class="prose flag-dead" style="margin-top:var(--space-16)">' +
        'This link no longer works. We have left it here so you know we checked.</p>' : '') +

    list("What it teaches", item.teaches) +

    '<section class="section"><h2 class="h2">Who it\'s for</h2>' +
      '<p class="prose">' + LC.esc(item.who_for) + '</p></section>' +

    '<section class="section"><h2 class="h2">Skip it if</h2>' +
      '<p class="prose">' + LC.esc(item.skip_if) + '</p></section>' +

    list("Before this", item.prerequisites) +
    pathBlock +

    '<section class="section"><h2 class="h2">How we checked this one</h2>' +
      '<p class="prose"><strong>' + LC.esc(tier.label) + '.</strong> ' +
      LC.esc(tier.tip) + ' <a href="how-we-check.html">How we check</a>.</p></section>' +

    '<p class="provenance">' +
      LC.esc(fresh.checked) +
      (LC.fmtDate(item.published)
        ? ' · Published ' + LC.esc(LC.fmtDate(item.published))
        : ' · No publish date given') +
      ' · Found through ' + LC.esc(item.source) +
    '</p>';

  var copy = document.getElementById("copy");
  copy.addEventListener("click", function () {
    navigator.clipboard.writeText(location.href).then(function () {
      copy.textContent = "Copied";
      setTimeout(function () { copy.textContent = "Copy link"; }, 1600);
    }).catch(function () { copy.textContent = "Press Ctrl+C"; });
  });
})();
