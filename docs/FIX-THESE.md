# Fix prompt — after the deploy review

Paste everything below the line into Claude Code, in the project folder.

---

The site is live and the deploy works. I had the last session's work reviewed and four
things came back. Two are real, one is a judgement call I want your opinion on, and one
is a decision only I can make. **Do not rebuild anything.** Read `CLAUDE.md` and
`README.md` first.

Work through them in this order. Show me the measurement before you change a design
value — that rule has already saved us once.

---

## 1. Body copy may now be too thin — measure it, then tell me

Last session found that `Tiempos Fine Regular` is a damaged file (Chrome's OTS rejects
it: `CFF : Failed validating CharStrings INDEX`) and switched weight 400 to
`Tiempos Fine Light`. **That diagnosis is correct** — I re-checked it independently with
`ots-sanitize`. Exactly two files fail: `Tiempos Fine Regular` and `Tiempos Fine Bold`.
Everything else passes. Note that `fontTools` parses all 12 without complaint, so only
OTS catches this.

But the replacement may have overcorrected. Rendered ink coverage at 20px:

```
Tiempos Fine Light        59.3% solid   <- what is live now
Tiempos Fine Medium       65.9%
system serif (~Georgia)   68.4%   <- what everyone was actually reading before
```

`Fine` is Klim's **display** cut. Neither Light nor Medium is drawn for 20px running
text, which is why Medium looked bold to you and Light may look weak. That measurement
came from PIL, not Chrome, so treat it as directional only.

**Do this:** open the live site in a real browser at 20px and compare the `Skip if:`
line — the heaviest sentence on the site — in three states: Tiempos Fine Light (now),
Tiempos Fine Medium, and the Georgia fallback. Look at it at 100% and at 200% zoom.
Then give me a recommendation and your reasoning. Options include using Georgia
deliberately rather than by accident. Do not change it before I answer.

## 2. Nothing validates `items.json` in CI — fix this

You correctly left `validate-report.py` out of the workflow: it validates incoming
research reports, not the catalogue, and exits 1 on `items.json`. That was right, but it
left the gap open. A broken entry now deploys silently.

Write a validator for the catalogue itself and run it in `.github/workflows/deploy.yml`
**before** `build.sh`, so a bad commit fails the build instead of shipping.

It must fail on:

- any required field empty — `url`, `title`, `source`, `summary`, `who_for`,
  `skip_if`, `checked`, `tier`, `status`, `level`, `format`, `time`, `cost`, `roles`,
  `topics`, `id`
- **an empty `skip_if`** — this is the product, not a field
- any value outside the controlled vocabulary (the lists are in `assets/js/ui.js`)
- a duplicate `id` or a duplicate normalised `url`
- an `id` that is not the URL-derived hash `scripts/stable-ids.py` would produce
- a `published` that is neither `UNVERIFIED` nor a real `YYYY-MM-DD`
- any path step in `data/paths.json` pointing at an id that does not exist

Report every failure at once, not just the first. Then prove it works: break something
on a scratch branch, watch the workflow go red, fix it, watch it go green.

## 3. The home `h1` — your call, and I may be wrong

`index.html` now has `<h1 class="meta">Find what's worth your time.</h1>`. That is the
small grey eyebrow line, not the visible heading. The page's largest text is the
interactive sentence, `I'm a [role] and I've [level]`.

Arguments both ways, and I do not think this is clear cut:

- **Leave it.** The sentence contains two buttons. Wrapping interactive controls in a
  heading is worse than a size mismatch, and "Find what's worth your time" genuinely
  describes the page. WCAG does not require the `h1` to be the biggest text.
- **Change it.** A sighted screen reader user gets a heading that is visually the
  smallest thing on the page.

Look at what a screen reader would actually announce, tell me which you would ship, and
say why. If you think it is fine as is, say so — I would rather hear that than have you
change it to look responsive.

## 4. The fonts — my decision, but give me the facts first

I already chose to ship them and I know the risk. Before I settle it for good, get me
the numbers:

- **How many font files are committed, and how many does the CSS actually load?** I am
  told it is 48 committed and 6 loaded. Confirm it.
- If that is right, the 42 unused files are pure exposure with no benefit. Deleting
  those changes nothing visually and is not a design decision.

Do that check and report. Then stop — whether the remaining 6 stay is mine to decide,
not yours to fix.

---

When each item is done, commit it on its own with a message that says what was wrong and
how you know it is fixed. Short answers to me. Ask before anything large.
