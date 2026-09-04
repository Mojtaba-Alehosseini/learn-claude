# Ground truth for Attack 2

**Site version attacked: `5c7372d`. Written 2026-09-05.**

## Where the numbers are

**[docs/STATUS.md](../STATUS.md).** Every count this file used to hold by hand is
generated there on every build: catalogue size, publishers, the tier ladder, formats,
levels, costs, the official ratio, the `UNVERIFIED` count, the `date_source`
provenance table, the full per-cell grid with publisher and non-Anthropic counts, the
thin and empty cells, the freshness exclusions, and the last link check.

The August version of this file wrote those out by hand and every one of them is now
wrong — it says 353 resources and 3 paths. That is the whole reason this section is a
pointer. **If an agent's number disagrees with STATUS.md, STATUS.md wins.**

For the per-role, per-level view a visitor actually gets on screen:

    python3 docs/attack/role-view.py <role> [level]
    python3 docs/attack/role-view.py designer never-used

It reproduces Browse's default sort, so row 1 is the first card on the page.

---

## What changed since Attack 1 — the things an attacker should know exist

Attack 1 ran on a site with 353 resources, 3 paths, no picks block and no date
provenance. Everything below is new since then. It is listed so that an agent does not
waste its hour rediscovering that a feature exists — the value is in judging whether
it *works*.

- **"Start with these three"** on Browse: when a visitor sets exactly one role and one
  level and nothing else, a block appears above the results naming three resources to
  open first, each with a one-sentence reason, labelled `picked by AI · <date>`. It
  covers 37 of the 40 role-and-level cells. Two cells ship **two** picks, not three,
  with a heading that says two. One cell is empty and says so.
- **A second date line.** Cards can now show `Updated <date>` as well as, or instead
  of, `Published <date>`. A page that gives only a revision date shows "No publish
  date given" *and* an Updated line.
- **Month-only dates.** A card may say `Updated May 2026` with no day, because that is
  all its page prints.
- **Three quarters of cards now say "No publish date given."** That number went up
  deliberately: every stored date was checked against its own page and any that could
  not be traced was cleared.
- **Card links changed shape.** The whole card is still one click target, but the link
  is now the title alone rather than the entire card.
- **Seven paths**, one for every role — Attack 1 found four roles with none.
- **A repaired path.** `writing-you-sign` lost a step when its resource vanished and
  is now four steps.

---

## Already known — do not present these as new

An agent may sharpen or contradict these. It earns nothing by rediscovering them.

- **0 resources are `reviewed`.** The top badge on the ladder is empty by design and
  only a person can change it.
- **The report link needs a GitHub account.** Most of the audience does not have one.
- **The catalogue is 61% Anthropic's own material**, stated on `how-we-check.html`.
- **`non-technical|builder` has no independent material at all** and `student|builder`
  is empty.
- **21 items sit on hosts that refuse automated checking**, so their links are
  confirmed by a person or not at all.
- **No analytics, no tracking, no accounts.** By design, and not an oversight.

---

## The rule that has not changed

**No number may be invented.** Every figure comes from STATUS.md, a command shown in
the file, or the live site. "Probably", "likely" and "seems" are banned in findings
and allowed only in the opinion section.

**A finding is a claim.** It carries the URL, what was done, what was seen, what a
reasonable person expected instead, and who it harms. An attacker who cannot reproduce
something does not report it.
