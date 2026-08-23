/* Home — two questions, one sentence, one drawing.
 *
 * The screen asks role and level and nothing else. Time was cut after measuring it:
 * asking all three returned a median of zero results, and a first screen that hands
 * back nothing is worse than a first screen that asks less. Time survives as a filter
 * on Browse, where a reader can see what removing it does.
 *
 * The illustration answers both halves of the sentence — there are 40 drawings, one per
 * role per level — so it has to change when either blank changes, not only the role.
 */

(function () {
  "use strict";

  var LC = window.LC;
  var items = LC.items();

  var state = { role: null, level: null, open: "role", showB: false };
  var fading = false, target = null, attract = null;

  var el = {};
  ["roleBlank", "levelBlank", "roleText", "levelText", "roleSet", "levelSet",
   "roleOptions", "levelOptions", "q", "go", "artA", "artB", "tally"].forEach(function (id) {
    el[id] = document.getElementById(id);
  });

  function art(role, level) {
    return "assets/icons/roles/" + (role || "non-technical") + "/" +
           (level || state.level || "never-used") + ".png";
  }

  /* Cross-fade rather than swap, so the change registers as an answer to what you just
     clicked instead of a flicker. 220ms, matching --dur-base in the stylesheet: if this
     number is shorter than the CSS transition, the next fade starts before the last one
     finished and both drawings show at once. */
  var FADE_MS = 220;
  function fadeTo(src) {
    target = src;
    if (fading) return;
    var showing = state.showB ? el.artB : el.artA;
    if (showing.getAttribute("src") === src) return;
    fading = true;
    var next = state.showB ? el.artA : el.artB;
    next.src = src;
    next.style.opacity = "1";
    showing.style.opacity = "0";
    state.showB = !state.showB;
    setTimeout(function () {
      fading = false;
      var now = (state.showB ? el.artB : el.artA).getAttribute("src");
      if (target && target !== now) fadeTo(target);
    }, FADE_MS);
  }

  /* Before anyone has chosen, the drawing cycles slowly. It is the only hint that the
     underlined words are buttons. It stops the moment a choice is made, and never runs
     for someone who asked for reduced motion. */
  function startAttract() {
    if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    var keys = Object.keys(LC.ROLE), i = 0;
    attract = setInterval(function () {
      if (state.role) { stopAttract(); return; }
      i = (i + 1) % keys.length;
      fadeTo(art(keys[i], "never-used"));
    }, 2600);
  }
  function stopAttract() { if (attract) { clearInterval(attract); attract = null; } }

  function chipHTML(map, chosen, value) {
    return '<button type="button" class="chip-choice" data-value="' + value + '" ' +
           'aria-pressed="' + (chosen === value) + '">' + LC.esc(map[value]) + '</button>';
  }

  function render() {
    el.roleOptions.innerHTML = Object.keys(LC.ROLE)
      .map(function (v) { return chipHTML(LC.ROLE, state.role, v); }).join("");
    el.levelOptions.innerHTML = Object.keys(LC.LEVEL)
      .map(function (v) { return chipHTML(LC.LEVEL, state.level, v); }).join("");

    el.roleText.textContent = state.role ? LC.ROLE[state.role] : "a [role]";
    el.levelText.textContent = state.level ? LC.LEVEL[state.level] : "[level]";

    el.roleSet.classList.toggle("hidden", state.open !== "role");
    el.levelSet.classList.toggle("hidden", state.open !== "level");
    el.roleBlank.setAttribute("aria-expanded", String(state.open === "role"));
    el.levelBlank.setAttribute("aria-expanded", String(state.open === "level"));

    /* Say the real number before they click, so "Show me" is never a disappointment. */
    var n = items.filter(function (it) {
      return (!state.role || it.roles.indexOf(state.role) !== -1) &&
             (!state.level || it.level === state.level);
    }).length;
    el.tally.textContent = (state.role || state.level)
      ? LC.countText(n) + " match so far."
      : LC.countText(items.length) + ", checked by hand.";
  }

  el.roleOptions.addEventListener("click", function (e) {
    var b = e.target.closest("[data-value]"); if (!b) return;
    stopAttract();
    state.role = b.dataset.value;
    state.open = "level";
    fadeTo(art(state.role));
    render();
  });

  el.levelOptions.addEventListener("click", function (e) {
    var b = e.target.closest("[data-value]"); if (!b) return;
    stopAttract();
    state.level = b.dataset.value;
    state.open = "";
    fadeTo(art(state.role || "non-technical", state.level));
    render();
  });

  el.roleBlank.addEventListener("click", function () {
    state.open = state.open === "role" ? "" : "role"; render();
  });
  el.levelBlank.addEventListener("click", function () {
    state.open = state.open === "level" ? "" : "level"; render();
  });

  /* Whatever they answered becomes the Browse URL, so the second screen opens already
     filtered instead of showing all 353 and making them start again. */
  el.go.addEventListener("submit", function (e) {
    e.preventDefault();
    var p = new URLSearchParams();
    if (state.role) p.set("role", state.role);
    if (state.level) p.set("level", state.level);
    var q = el.q.value.trim();
    if (q) p.set("q", q);
    location.href = "browse.html" + (p.toString() ? "?" + p.toString() : "");
  });

  el.artA.src = art("non-technical", "never-used");
  render();
  startAttract();
})();
