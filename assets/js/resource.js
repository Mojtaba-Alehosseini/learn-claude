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

  /* A bare browse.html here threw away the role and level the reader had just
     chosen and dropped them into all 635 - on a phone, at the top of a page hundreds
     of screens long. Filters live only in the URL, so the referrer has them. Only our
     own browse page is trusted, and only its query string is used. */
  function backHref() {
    try {
      var r = new URL(document.referrer);
      if (r.origin === location.origin && /(^|\/)browse\.html$/.test(r.pathname) &&
          r.search) {
        return "browse.html" + r.search;
      }
    } catch (e) { /* no referrer, or not a URL we can read */ }
    return "browse.html";
  }

  var fresh = LC.freshness(item);
  var author = LC.authorLine(item);

  function list(title, arr) {
    if (!arr || !arr.length) return "";
    return '<section class="section"><h2 class="h2">' + title + '</h2><ul class="prose">' +
      arr.map(function (s) {
        return '<li style="margin-top:var(--space-8)">— ' + LC.esc(LC.sentence(s)) + '</li>';
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
    '<p class="meta"><a href="' + backHref() + '">← Back to browse</a></p>' +

    '<div class="resource-head" style="margin-top:var(--space-24)">' +
      '<div class="chip-row">' + LC.badge(item.tier) + '</div>' +
      '<h1 class="h1" style="margin-top:var(--space-12)">' + LC.esc(item.title) + '</h1>' +
      '<p class="meta" style="margin-top:var(--space-8)">' +
        LC.publisher(item) + author + '</p>' +
      '<div class="chip-row" style="margin-top:var(--space-16)">' + LC.chips(item) + '</div>' +
      (item.summary
        ? '<p class="prose" style="margin-top:var(--space-24)">' +
          LC.esc(item.summary) + '</p>'
        : '') +
    '</div>' +

    '<div class="resource-actions">' +
      '<a class="btn btn-primary" href="' + LC.esc(item.url) + '" ' +
         'target="_blank" rel="noopener noreferrer">Open on ' + LC.esc(item.source) + '</a>' +
      '<button type="button" class="btn btn-secondary" id="copy">Copy link</button>' +
    '</div>' +

    (item.status === "dead"
      ? '<p class="prose flag-dead" style="margin-top:var(--space-16)">' +
        'This link no longer works. We have left it here so you know we checked.</p>' : '') +

    /* The catalogue has carried status "outdated" on a handful of rows for months and
       nothing rendered it, because this branch only ever asked about "dead". A flag
       the reader never sees is the same as no flag. */
    (item.status === "outdated"
      ? '<p class="prose flag-outdated" style="margin-top:var(--space-16)">' +
        'We marked this out of date at the last check. Parts of it no longer match ' +
        'Claude.</p>' : '') +

    list("What it teaches", item.teaches) +

    (item.who_for
      ? '<section class="section"><h2 class="h2">Who it\'s for</h2>' +
        '<p class="prose">' + LC.esc(item.who_for) + '</p></section>'
      : '') +

    '<section class="section"><h2 class="h2">Skip it if</h2>' +
      '<p class="prose">' + LC.esc(item.skip_if) + '</p></section>' +

    list("Before this", item.prerequisites) +
    pathBlock +

    '<section class="section"><h2 class="h2">How we checked this one</h2>' +
      '<p class="prose"><strong>' + LC.esc(tier.label) + '.</strong> ' +
      LC.esc(tier.tip) + ' <a href="how-we-check.html">How we check</a>.</p></section>' +

    /* This line used to rebuild the dates by hand and drop two things the card
       already showed: the Updated date, which 96 items carry and which for 44 of them
       is the only date evidence there is, and the "over a year ago" warning on 17.
       So the page reached from a shared link said less than the card that linked to
       it. It now takes both from LC.freshness, the same source the card uses.
       It keeps the real date as well as the warning rather than swapping one for the
       other: the card has room for one and this page has room for both. */
    '<p class="provenance">' +
      LC.esc(fresh.checked) +
      (LC.fmtDate(item.published)
        ? ' · Published ' + LC.esc(LC.fmtDate(item.published))
        : ' · No publish date given') +
      (fresh.updatedNote ? ' · ' + LC.esc(fresh.updatedNote) : '') +
      ' · Found through ' + LC.esc(item.source) +
    '</p>' +

    (fresh.cls === 'flag-outdated'
      ? '<p class="provenance flag-outdated">' + LC.esc(fresh.note) + '</p>' : '') +

    /* The escape hatch. Sits under the provenance line, in the same quiet type, because
       it belongs to the same conversation: here is what we know about this and when we
       last looked, and here is what to do if we got it wrong. */
    '<p class="report"><a href="' + LC.esc(LC.reportUrl(item)) + '" ' +
      'target="_blank" rel="noopener noreferrer">Something wrong with this one? Tell us' +
      '</a> — opens a GitHub issue with the details already filled in.</p>';

  var copy = document.getElementById("copy");
  var copyTimer = null;

  /* One timer, always cleared before the next. Two faults lived here: a second click
     1.5s after the first was cut short by the first click's timer, and the branch where
     the clipboard is refused set "Press Ctrl+C" with no timer at all, so the button
     never said "Copy link" again for the life of the page. Both messages now clear
     themselves, and only the most recent one is counting. */
  function say(text) {
    copy.textContent = text;
    clearTimeout(copyTimer);
    copyTimer = setTimeout(function () { copy.textContent = "Copy link"; }, 1600);
  }

  copy.addEventListener("click", function () {
    navigator.clipboard.writeText(location.href)
      .then(function () { say("Copied"); })
      .catch(function () { say("Press Ctrl+C"); });
  });
})();
