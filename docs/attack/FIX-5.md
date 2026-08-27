# Fix prompt — the two promises the site makes and cannot keep

Paste everything below the line into Claude Code, in the project folder.

---

Both paths are good, and finding the `norm()` collision before it shipped was the real
work in that round — that is the third file where the same trap has appeared, and you
were the one who went looking.

Designer and data-analyst stay uncovered until I find the resources on your shopping
list. That is research, not code, and it is mine.

These two are code, and both are the site failing a promise it prints on its own pages.

## 1. "Found something wrong? Tell us." — there is no way to tell anyone

`how-we-check.html` says a dead link or an out-of-date note is the worst thing that can
happen to a site like this, and then offers no route. No email, no link, no form. I
checked: zero `mailto:` and zero issue links across all five pages.

Build the route. Two places it belongs:

- **On every resource page** — a quiet link that reports *this specific resource*, with
  the title and URL already filled in. Someone who finds a dead link is looking at the
  dead link; making them go elsewhere and describe it loses most reports.
- **On "How we check"** — the general one, under that paragraph.

Use a prefilled GitHub issue against `Mojtaba-Alehosseini/learn-claude`. The repo is
already public, it costs nothing, and it keeps reports in one place with a history.

**But say this plainly in your answer:** a GitHub issue asks a teacher or a student to
have a GitHub account, and most will not. Tell me what fraction of the site's audience
that shuts out, and whether you think an email address should sit alongside it. Do not
add an email without asking me — that is my inbox and my spam.

Keep it quiet in the design. It is not a call to action; it is an escape hatch for the
one person in a hundred who spots something wrong.

## 2. Nothing re-checks the links

Every `checked` date on the site is August 2026 and nothing will ever move it. In six
months every date is a lie, and the date is the whole premise — `README.md` says so:
*"When something drifts out of date, the date says so before we do."*

Add a scheduled GitHub Action, weekly, that:

- requests every URL in `data/items.json`
- opens an issue listing anything that 404s or has stopped resolving
- **does not** edit `data/items.json` and does not commit anything

That last rule matters. A job that silently flips `status: dead` would let a
misconfigured user-agent quietly delete good resources. It reports; a person decides.

Two things you already know that this must handle:

- **Roughly 20 hosts return 403 to a bot and are fine in a browser** — Udemy, DataCamp,
  Medium. A checker that reports those as dead every week is a checker I will start
  ignoring by week three. Separate "gone" from "blocked us", and only shout about "gone".
- `education.gov.au` returns nothing to an automated request and is live. It is already
  recorded in that resource's `notes`.

## What would make this wrong

- A report link that opens a blank issue form. If the reporter has to describe which
  resource they mean, most will not bother.
- A weekly job that cries wolf about 403s.
- Anything that writes to `data/items.json` on a schedule.
- Touching `checked` dates. Re-checking a link is not the same as re-reading a resource,
  and only the second one earns a new date. Say so in the issue text.

---

One commit each. Short answers. On the GitHub-account question, give me your
recommendation and the number behind it, then stop and let me decide.
