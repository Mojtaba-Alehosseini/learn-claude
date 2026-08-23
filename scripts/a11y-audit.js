/* Accessibility audit for Learn Claude.
 *
 * There is no build step and no test runner in the browser, so this is written to be
 * pasted into a DevTools console on any page of the site. It reports; it does not fix.
 *
 *     LC_A11Y()
 *
 * What it cannot see: whether a focus ring is visible against the pixel behind it,
 * whether the reading order matches the visual order, and whether a screen reader says
 * something sensible. Those need a person. Everything here is the part a machine can be
 * trusted with — contrast arithmetic, names, roles, order, and target size.
 */
function LC_A11Y() {
  var out = { page: location.pathname + location.search, fail: [], warn: [], pass: [] };
  function fail(id, msg) { out.fail.push(id + ': ' + msg); }
  function warn(id, msg) { out.warn.push(id + ': ' + msg); }
  function pass(id, msg) { out.pass.push(id + ': ' + msg); }

  function label(el) {
    var t = el.tagName.toLowerCase();
    var c = (typeof el.className === 'string' && el.className.trim())
      ? '.' + el.className.trim().split(/\s+/).join('.') : '';
    var txt = (el.innerText || el.value || '').trim().replace(/\s+/g, ' ').slice(0, 40);
    return t + c + (txt ? ' "' + txt + '"' : '');
  }

  /* ---- colour ---------------------------------------------------------- */
  function rgb(s) {
    var m = String(s).match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    var p = m[1].split(',').map(parseFloat);
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  }
  function lum(c) {
    var f = [c.r, c.g, c.b].map(function (v) {
      v /= 255;
      return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * f[0] + 0.7152 * f[1] + 0.0722 * f[2];
  }
  function over(fg, bg) {
    if (fg.a >= 1) return fg;
    return {
      r: fg.r * fg.a + bg.r * (1 - fg.a),
      g: fg.g * fg.a + bg.g * (1 - fg.a),
      b: fg.b * fg.a + bg.b * (1 - fg.a),
      a: 1
    };
  }
  function ratio(a, b) {
    var l1 = lum(a), l2 = lum(b);
    return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
  }
  function effectiveBg(el) {
    var node = el, stack = [];
    while (node && node.nodeType === 1) {
      var c = rgb(getComputedStyle(node).backgroundColor);
      if (c && c.a > 0) { stack.push(c); if (c.a >= 1) break; }
      node = node.parentElement;
    }
    var base = { r: 255, g: 255, b: 255, a: 1 };
    for (var i = stack.length - 1; i >= 0; i--) base = over(stack[i], base);
    return base;
  }

  /* ---- 1. document ----------------------------------------------------- */
  var lang = document.documentElement.getAttribute('lang');
  if (lang) { pass('lang', lang); } else { fail('lang', 'html element has no lang attribute'); }
  if (document.title) { pass('title', document.title); } else { fail('title', 'page has no title'); }

  /* ---- 2. landmarks ---------------------------------------------------- */
  var mains = document.querySelectorAll('main, [role=main]');
  if (mains.length === 1) { pass('landmark-main', 'exactly one main'); }
  else { fail('landmark-main', mains.length + ' main landmarks, expected 1'); }
  ['header,[role=banner]', 'nav,[role=navigation]', 'footer,[role=contentinfo]'].forEach(function (sel) {
    var name = sel.split(',')[0];
    if (document.querySelector(sel)) { pass('landmark', name + ' present'); }
    else { warn('landmark', 'no ' + name); }
  });

  /* ---- 3. skip link ---------------------------------------------------- */
  var firstAnchor = document.querySelector('a[href^="#"]');
  if (firstAnchor && /skip/i.test(firstAnchor.innerText)) {
    var href = firstAnchor.getAttribute('href');
    var tgt = document.querySelector(href);
    if (tgt) { pass('skip-link', firstAnchor.innerText.trim() + ' to ' + href); }
    else { fail('skip-link', 'points at ' + href + ', which does not exist'); }
  } else {
    warn('skip-link', 'no skip link found as the first in-page anchor');
  }

  /* ---- 4. headings ----------------------------------------------------- */
  var hs = [].slice.call(document.querySelectorAll('h1,h2,h3,h4,h5,h6'));
  var h1s = hs.filter(function (h) { return h.tagName === 'H1'; });
  if (h1s.length === 1) { pass('h1', h1s[0].innerText.trim().slice(0, 50)); }
  else { fail('h1', h1s.length + ' h1 elements, expected 1'); }
  var prev = 0, badOrder = 0;
  hs.forEach(function (h) {
    var lvl = +h.tagName[1];
    if (prev && lvl > prev + 1) {
      badOrder++;
      fail('heading-order', 'h' + prev + ' jumps to h' + lvl + ' at "' + h.innerText.trim().slice(0, 40) + '"');
    }
    prev = lvl;
  });
  if (!badOrder) { pass('heading-order', hs.length + ' headings, no skipped level'); }

  /* ---- 5. names on interactive things ---------------------------------- */
  function accName(el) {
    var l = (el.getAttribute('aria-label') || '').trim();
    if (l) return l;
    var by = el.getAttribute('aria-labelledby');
    if (by) {
      var n = document.getElementById(by);
      if (n && n.innerText.trim()) return n.innerText.trim();
    }
    var t = (el.innerText || '').trim();
    if (t) return t;
    var ttl = (el.getAttribute('title') || '').trim();
    if (ttl) return ttl;
    var img = el.querySelector('img[alt]');
    return img ? img.alt.trim() : '';
  }
  var nameFails = 0;
  [].slice.call(document.querySelectorAll('a[href], button, [role=button]')).forEach(function (el) {
    if (!accName(el)) {
      nameFails++;
      fail('name', 'no accessible name on ' + label(el) + ' ' + (el.getAttribute('href') || ''));
    }
  });
  [].slice.call(document.querySelectorAll('input, select, textarea')).forEach(function (el) {
    if (el.type === 'hidden') return;
    var has = el.getAttribute('aria-label') || el.getAttribute('aria-labelledby') ||
      (el.id && document.querySelector('label[for="' + CSS.escape(el.id) + '"]')) || el.closest('label');
    if (!has) { nameFails++; fail('label', 'unlabelled form control ' + label(el)); }
  });
  if (!nameFails) { pass('names', 'every link, button and form control has a name'); }

  /* ---- 6. images ------------------------------------------------------- */
  var noAlt = [].slice.call(document.images).filter(function (i) {
    return !i.hasAttribute('alt') && i.getAttribute('aria-hidden') !== 'true' &&
           i.getAttribute('role') !== 'presentation';
  });
  if (noAlt.length) {
    fail('img-alt', noAlt.length + ' images with no alt: ' +
      noAlt.slice(0, 3).map(function (i) { return String(i.src).split('/').pop(); }).join(', '));
  } else {
    pass('img-alt', document.images.length + ' img elements, all have alt or are hidden');
  }

  /* ---- 7. contrast ----------------------------------------------------- */
  var seen = {}, worst = [];
  [].slice.call(document.querySelectorAll('body *')).forEach(function (el) {
    if (el.children.length) return;
    var txt = (el.innerText || '').trim();
    if (!txt) return;
    var r = el.getBoundingClientRect();
    if (!r.width || !r.height) return;
    var s = getComputedStyle(el);
    if (s.visibility === 'hidden' || s.display === 'none' || +s.opacity === 0) return;
    var bg = effectiveBg(el);
    var fg = over(rgb(s.color) || { r: 0, g: 0, b: 0, a: 1 }, bg);
    var cr = ratio(fg, bg);
    var px = parseFloat(s.fontSize), bold = +s.fontWeight >= 700;
    var large = px >= 24 || (px >= 18.66 && bold);
    var need = large ? 3 : 4.5;
    var key = s.color + '|' + [bg.r, bg.g, bg.b].map(Math.round).join(',') + '|' + s.fontSize + '|' + s.fontWeight;
    if (seen[key]) return;
    seen[key] = 1;
    if (cr < need) {
      worst.push({
        ratio: +cr.toFixed(2), need: need, size: s.fontSize, weight: s.fontWeight,
        color: s.color, bg: 'rgb(' + [bg.r, bg.g, bg.b].map(Math.round).join(',') + ')',
        el: label(el)
      });
    }
  });
  out.contrast = worst.sort(function (a, b) { return a.ratio - b.ratio; });
  if (worst.length) { fail('contrast', worst.length + ' distinct text and background pairs below AA, see out.contrast'); }
  else { pass('contrast', 'every distinct text and background pair meets AA'); }

  /* ---- 8. focus order and tabindex ------------------------------------- */
  var FOCUSABLE = 'a[href],button,input,select,textarea,[tabindex]:not([tabindex="-1"]),[contenteditable=true]';
  var f = [].slice.call(document.querySelectorAll(FOCUSABLE)).filter(function (el) {
    if (el.disabled) return false;
    var s = getComputedStyle(el);
    if (s.visibility === 'hidden' || s.display === 'none') return false;
    var r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  });
  var positive = f.filter(function (el) { return +(el.getAttribute('tabindex') || 0) > 0; });
  if (positive.length) { fail('tabindex', positive.length + ' elements use a positive tabindex, which overrides DOM order'); }
  else { pass('tabindex', 'no positive tabindex'); }
  var jumps = [];
  for (var i = 1; i < f.length; i++) {
    var a = f[i - 1].getBoundingClientRect(), b = f[i].getBoundingClientRect();
    if (b.top < a.top - 24) jumps.push(label(f[i - 1]) + '  ->  ' + label(f[i]));
  }
  out.focusableCount = f.length;
  out.focusJumps = jumps;
  if (jumps.length) { warn('focus-order', jumps.length + ' places where tab moves up the page, see out.focusJumps'); }
  else { pass('focus-order', f.length + ' focusable elements, tab order follows the visual order'); }

  /* ---- 9. focus indicator ---------------------------------------------- */
  var fvRules = 0, killed = 0;
  [].slice.call(document.styleSheets).forEach(function (ss) {
    var list;
    try { list = ss.cssRules; } catch (e) { return; }
    [].slice.call(list || []).forEach(function (r) {
      if (!r.selectorText) return;
      if (/:focus-visible/.test(r.selectorText)) fvRules++;
      else if (/:focus\b/.test(r.selectorText) && /outline:\s*(none|0)/.test(r.cssText)) killed++;
    });
  });
  if (fvRules) { pass('focus-visible', fvRules + ' focus-visible rules'); }
  else { fail('focus-visible', 'no focus-visible rule, so keyboard users get the browser default or nothing'); }
  if (killed) { warn('focus-visible', killed + ' rules remove the outline on focus with no focus-visible replacement'); }

  /* ---- 10. live regions ------------------------------------------------ */
  var live = [].slice.call(document.querySelectorAll('[aria-live],[role=status],[role=alert]'));
  if (live.length) {
    pass('live-region', live.map(function (n) {
      return (n.getAttribute('aria-live') || n.getAttribute('role')) + ' "' + n.innerText.trim().slice(0, 40) + '"';
    }).join(' | '));
  } else {
    warn('live-region', 'no live region, so a result count that changes is not announced');
  }

  /* ---- 11. target size, WCAG 2.2 AA asks for 24 by 24 ------------------ */
  var small = f.filter(function (el) {
    var r = el.getBoundingClientRect();
    return r.width < 24 || r.height < 24;
  }).map(function (el) {
    var r = el.getBoundingClientRect();
    return label(el) + '  ' + Math.round(r.width) + 'x' + Math.round(r.height);
  });
  out.smallTargets = small;
  if (small.length) { warn('target-size', small.length + ' targets under 24 by 24 css px, see out.smallTargets'); }
  else { pass('target-size', 'every target is at least 24 by 24'); }

  /* ---- 12. duplicate ids ----------------------------------------------- */
  var ids = {}, dupes = [];
  [].slice.call(document.querySelectorAll('[id]')).forEach(function (el) {
    ids[el.id] = (ids[el.id] || 0) + 1;
    if (ids[el.id] === 2) dupes.push(el.id);
  });
  if (dupes.length) { fail('duplicate-id', dupes.join(', ')); }
  else { pass('duplicate-id', 'all ids unique'); }

  /* ---- 13. reduced motion ---------------------------------------------- */
  var rm = false;
  [].slice.call(document.styleSheets).forEach(function (ss) {
    var list;
    try { list = ss.cssRules; } catch (e) { return; }
    [].slice.call(list || []).forEach(function (r) {
      if (r.media && /prefers-reduced-motion/.test(r.conditionText || r.media.mediaText)) rm = true;
    });
  });
  if (rm) { pass('reduced-motion', 'a prefers-reduced-motion block exists'); }
  else { warn('reduced-motion', 'no prefers-reduced-motion block'); }

  out.summary = out.fail.length + ' fail, ' + out.warn.length + ' warn, ' + out.pass.length + ' pass';
  return out;
}
