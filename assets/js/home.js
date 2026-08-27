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

  var state = { role: null, level: null, open: "role", showB: false,
                artRole: null, artLevel: null };
  var fading = false, target = null, attract = null;

  /* Set while the pointer or the keyboard is resting on a chip. A preview moves the
     drawing and nothing else — it is not a choice, and it is undone on the way out. */
  var previewing = null;

  var el = {};
  ["roleBlank", "levelBlank", "roleText", "levelText", "roleSet", "levelSet",
   "roleOptions", "levelOptions", "chooser", "q", "go", "artA", "artB",
   "tally"].forEach(function (id) {
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
  var REDUCED = matchMedia("(prefers-reduced-motion: reduce)");

  /* The stylesheet drops every duration to nothing under reduced motion. This constant
     did not, so the lock outlived the transition it was matching: the drawing still
     arrived up to 220ms after the click, now as a hard cut, for exactly the people who
     asked for no motion. Read at call time rather than once, so changing the system
     setting takes effect without a reload. */
  function fadeMs() { return REDUCED.matches ? 0 : FADE_MS; }

  /* Run fn once the image can paint, exactly once, whatever happens.
     `load` and `error`, not decode(). decode() reads like the honest signal and was
     tried here first: on an <img> that has just been given its first src it returns a
     promise that never settles at all — not resolved, not rejected, still pending after
     2.5 seconds. That left `fading` true for good and froze the whole attract cycle on
     the first tick. The timeout is the backstop for the same reason: `fading` gates
     every later swap, so a drawing that never arrives must never hold the lock. */
  function whenPainted(img, fn) {
    if (img.complete && img.naturalWidth) { fn(); return; }
    var done = false, timer = null;
    function once() {
      if (done) return;
      done = true;
      clearTimeout(timer);
      img.removeEventListener("load", once);
      img.removeEventListener("error", once);
      fn();
    }
    img.addEventListener("load", once);
    img.addEventListener("error", once);
    timer = setTimeout(once, 2000);
  }

  function fadeTo(src) {
    target = src;
    if (fading) return;
    var showing = state.showB ? el.artB : el.artA;
    if (showing.getAttribute("src") === src) { markFromSrc(src); return; }
    fading = true;
    var next = state.showB ? el.artA : el.artB;
    next.src = src;

    /* Wait for the file before raising it. Setting src and opacity in the same breath
       assumes the drawing is already there; on a cold cache it is not, so the incoming
       element was brought to full opacity still holding the previous generation's
       picture, or nothing at all. There are 40 of these, about a megabyte, and only the
       fonts are preloaded. A cached image is ready immediately, so every swap after the
       first costs nothing. */
    whenPainted(next, function () {
      next.style.opacity = "1";
      showing.style.opacity = "0";
      markFromSrc(src);
      state.showB = !state.showB;
      setTimeout(function () {
        fading = false;
        var now = (state.showB ? el.artB : el.artA).getAttribute("src");
        if (target && target !== now) fadeTo(target);
      }, fadeMs());
    });
  }

  /* Ask for a drawing. fadeTo does the marking, at the moment the picture changes. */
  function showArt(role, level) {
    state.artRole = role || "non-technical";
    state.artLevel = level || "never-used";
    fadeTo(art(state.artRole, state.artLevel));
  }

  function mark(row, value) {
    Array.prototype.forEach.call(row.children, function (b) {
      if (value && b.dataset.value === value) b.setAttribute("data-showing", "");
      else b.removeAttribute("data-showing");
    });
  }

  /* Mark from the file that is going on screen, never from what was asked for.
     fadeTo holds a request back while an earlier fade is still running, so a mark set at
     request time can arrive before the picture does. Reading the src at the moment it is
     committed means the chip and the drawing cannot disagree — and it stays true when a
     background tab throttles the timers to a crawl. */
  function markFromSrc(src) {
    var p = src.split("/");                       /* .../roles/<role>/<level>.png */
    mark(el.roleOptions, p[p.length - 2]);
    /* The level row is marked only when a level was really asked for. Every drawing
       needs some level, so it falls back to never-used; marking that chip on a fallback
       would show a choice nobody made. */
    var levelAsked = state.level || (previewing && previewing.kind === "level");
    mark(el.levelOptions, levelAsked ? p[p.length - 1].replace(".png", "") : null);
  }

  /* Re-mark whatever is on screen. Needed on the first render, which builds the rows,
     and harmless afterwards, when the buttons survive and keep their marks. */
  function markShowing() {
    var img = state.showB ? el.artB : el.artA;
    markFromSrc(img.getAttribute("src") || art("non-technical", "never-used"));
  }

  /* Before anyone has chosen, the drawing cycles slowly. It is the only hint that the
     underlined words are buttons. It stops the moment a choice is made, and never runs
     for someone who asked for reduced motion. */
  function startAttract() {
    if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    stopAttract();   /* hovering pauses and leaving restarts, so never stack two */
    var keys = Object.keys(LC.ROLE);
    var i = keys.indexOf(state.artRole);
    attract = setInterval(function () {
      if (state.role) { stopAttract(); return; }
      i = (i + 1) % keys.length;
      showArt(keys[i], "never-used");
    }, 2600);
  }
  function stopAttract() { if (attract) { clearInterval(attract); attract = null; } }

  function chipHTML(map, chosen, value) {
    return '<button type="button" class="chip-choice" data-value="' + value + '" ' +
           'aria-pressed="' + (chosen === value) + '">' + LC.esc(map[value]) + '</button>';
  }

  /* Build a row once, then only change what differs.
     Replacing innerHTML on every render put the new button and its `data-showing` into
     the same style resolution, so there was no value to move from and the 220ms fade
     this file and the stylesheet both promise never ran on a click — only on hover,
     which is the one path that does not call render(). The buttons themselves never
     change. Only which one is pressed does. */
  function fillRow(row, map, chosen) {
    if (!row.children.length) {
      row.innerHTML = Object.keys(map)
        .map(function (v) { return chipHTML(map, chosen, v); }).join("");
      return;
    }
    Array.prototype.forEach.call(row.children, function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.value === chosen));
    });
  }

  function render() {
    fillRow(el.roleOptions, LC.ROLE, state.role);
    fillRow(el.levelOptions, LC.LEVEL, state.level);

    el.roleText.textContent = state.role ? LC.ROLE[state.role] : "a [role]";
    el.levelText.textContent = state.level ? LC.LEVEL[state.level] : "[level]";

    el.roleSet.classList.toggle("hidden", state.open !== "role");
    el.levelSet.classList.toggle("hidden", state.open !== "level");
    el.roleBlank.setAttribute("aria-expanded", String(state.open === "role"));
    el.levelBlank.setAttribute("aria-expanded", String(state.open === "level"));

    /* The search field is the other way in — "or describe what you want to do". Once
       both blanks are filled it is offering an alternative to a question already
       answered, so it collapses and leaves "Show me" alone.
       Unless something has been typed into it. Hiding a field while still submitting
       what it holds would send a query the reader can no longer see, so anything typed
       keeps it on screen.
       Only re-checked here, on a chip click, and deliberately not on every keystroke:
       deleting your last character would otherwise collapse the field under your own
       cursor. It goes away when you answer the second question, which is a decision you
       just made, and never while you are typing. The stylesheet does the moving; this
       only says when. */
    el.go.classList.toggle("answered",
      !!(state.role && state.level) && !el.q.value.trim());

    /* Say the real number before they click, so "Show me" is never a disappointment. */
    var n = items.filter(function (it) {
      return (!state.role || it.roles.indexOf(state.role) !== -1) &&
             (!state.level || it.level === state.level);
    }).length;
    el.tally.textContent = (state.role || state.level)
      ? LC.countText(n) + " match so far."
      : LC.countText(items.length) + ", checked by hand.";

    /* Only does work on the first render, when fillRow builds the buttons. After that
       the same nodes stay in place and keep the mark they already have. */
    markShowing();
  }

  el.roleOptions.addEventListener("click", function (e) {
    var b = e.target.closest("[data-value]"); if (!b) return;
    stopAttract();
    previewing = null;
    state.role = b.dataset.value;
    state.open = "level";
    showArt(state.role, state.level);
    render();
  });

  el.levelOptions.addEventListener("click", function (e) {
    var b = e.target.closest("[data-value]"); if (!b) return;
    stopAttract();
    previewing = null;
    state.level = b.dataset.value;
    state.open = "";
    showArt(state.role, state.level);
    render();
  });

  /* Point at an option and the drawing shows it.
     A preview changes the picture and nothing else. The sentence keeps its blanks, no
     chip becomes pressed, and leaving puts the drawing back where it was. The attract
     cycle only pauses, because it is the one hint that the underlined words are buttons
     and brushing past a chip should not take that away for good.

     Guarded on (hover: hover). A touch screen fires mouseover on the tap that is already
     a click, so on a phone the preview would only fight the choice. focusin does the
     same work for a keyboard, which has no hover at all. */
  var CAN_HOVER = matchMedia("(hover: hover)").matches;

  function preview(kind, value) {
    stopAttract();
    previewing = { kind: kind, value: value };
    if (kind === "role") showArt(value, state.level);
    else showArt(state.role, value);
  }

  function endPreview() {
    if (!previewing) return;
    previewing = null;
    /* With a choice made there is something to go back to. With nothing chosen there is
       not, so the drawing stays where the pointer left it and the cycle picks up from
       there. Snapping back to the first role would be a jump that answers nothing. */
    if (state.role || state.level) showArt(state.role, state.level);
    else markShowing();
    if (!state.role) startAttract();
  }

  function chipIn(row, node) {
    var b = node && node.closest ? node.closest("[data-value]") : null;
    return b && row.contains(b) ? b : null;
  }

  [["mouseover", "mouseout"], ["focusin", "focusout"]].forEach(function (pair) {
    var pointer = pair[0] === "mouseover";
    el.chooser.addEventListener(pair[0], function (e) {
      if (pointer && !CAN_HOVER) return;
      var b = chipIn(el.roleOptions, e.target);
      if (b) return preview("role", b.dataset.value);
      b = chipIn(el.levelOptions, e.target);
      if (b) preview("level", b.dataset.value);
    });
    el.chooser.addEventListener(pair[1], function (e) {
      if (pointer && !CAN_HOVER) return;
      /* Moving from one chip to the next stays inside the chooser. Only a real exit
         ends the preview, or the drawing would flicker back between every two chips. */
      if (e.relatedTarget && el.chooser.contains(e.relatedTarget)) return;
      endPreview();
    });
  });

  el.roleBlank.addEventListener("click", function () {
    state.open = state.open === "role" ? "" : "role"; render();
  });
  el.levelBlank.addEventListener("click", function () {
    state.open = state.open === "level" ? "" : "level"; render();
  });

  /* Whatever they answered becomes the Browse URL, so the second screen opens already
     filtered instead of showing everything and making them start again. */
  el.go.addEventListener("submit", function (e) {
    e.preventDefault();
    var p = new URLSearchParams();
    if (state.role) p.set("role", state.role);
    if (state.level) p.set("level", state.level);
    var q = el.q.value.trim();
    if (q) p.set("q", q);
    location.href = "browse.html" + (p.toString() ? "?" + p.toString() : "");
  });

  state.artRole = "non-technical";
  state.artLevel = "never-used";
  el.artA.src = art(state.artRole, state.artLevel);
  render();
  startAttract();
})();
