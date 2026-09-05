# UX copy deck

**Date:** 2026-08-19
**Covers:** every string the site shows.
**Rule:** if a string is not in this file, it does not go on the site.

---

## Voice

Plain, calm, honest. A well-made reference book, not a product launch.

The site's whole claim is that it tells you the truth about learning material,
including when not to bother. The copy has to sound like it means that. One
overclaiming sentence undoes the premise.

**Do**

- Sentence case everywhere. Buttons, headings, labels, badges.
- Say the number. "77 resources", not "lots of resources".
- Name the limit out loud. "We have not watched this one."
- Verb first on buttons. "Show me", "Start here", "See all courses".
- Short sentences. English is a second language for many readers.

**Do not**

- No exclamation marks.
- No "simply", "just", "easy", "seamless", "unlock", "supercharge", "curated".
- No "please". The interface is not asking a favour.
- No "click here". The link text names the destination.
- No emoji.
- Never claim we reviewed something we did not.

---

## Naming — pick one word and never vary it

| Concept | Always call it | Never |
|---|---|---|
| One entry in the directory | **resource** | item, entry, content, asset, piece |
| The whole set | **the directory** | database, catalogue, library, collection |
| An ordered set of resources | **path** | track, journey, curriculum, roadmap |
| The two-question opener | **the two questions** | quiz, wizard, onboarding, survey |
| How thoroughly we checked | **how we checked it** | tier, rating, score, grade, quality level |
| The date we last verified | **checked** | updated, verified, last seen, reviewed on |

`tier` stays as the field name in the data. Readers never see the word.

---

## Global

### Site name and tagline

**Name:** Learn Claude
**Tagline:** Find what's worth your time.

### Navigation

| Item | Label |
|---|---|
| Home | Learn Claude *(the wordmark links home)* |
| Browse | Browse |
| Paths | Paths |
| About | How we check |
| Skip link | Skip to content |

Three links. No dropdowns. No tabs.

### Footer

> Not affiliated with Anthropic. We link to other people's work and say what we think of it.
> Every one checked and given a reason to skip it. The date is on every resource.
> (Never "checked by hand": the tier that means a person checked the notes has a count
> of zero. D2, 2026-09-05.)

Columns: **The directory** (Browse · Paths) · **About** (How we check · Why we say skip · Contact) · **Built with** (Sources · Changelog).

---

## Home — the first screen

### The sentence

The interactive line the visitor completes. Each blank opens a set of choices.

> I'm a **[role]** and I've **[level]**.

Button under it: **Show me**

Two blanks, not three. Time was cut on 2026-08-19 — measured against the real catalogue,
adding it emptied half of all possible answers. It lives in the filters instead.

Search below the sentence, placeholder:

> Or describe what you want to do…

Real examples to rotate as placeholder text — all plain, all things people actually type:

- `help me write my thesis faster`
- `I keep getting generic answers`
- `how do I make Claude read my PDFs`
- `where do I even start`

### The choice sets

**Role** — chip labels

| Value | Label |
|---|---|
| `non-technical` | not a coder |
| `student` | a student |
| `researcher` | a researcher |
| `teacher` | a teacher |
| `developer` | a developer |
| `data-analyst` | working with data |
| `pm` | a product manager |
| `designer` | a designer |
| `business-founder` | running a business |
| `writer-marketer` | a writer |

Prompt above the chips: **Who are you?**

**Level**

| Value | Label |
|---|---|
| `never-used` | never used Claude |
| `basic` | used it a little |
| `confident` | used it a lot |
| `builder` | built things with it |

Prompt: **How much Claude do you know?**

**Time** — a filter, not an entry question. Labels used in the filter panel and on cards:

| Value | Label |
|---|---|
| `under-15min` | 15 min |
| `under-1hr` | 1 hour |
| `half-day` | half a day |
| `multi-day` | several days |

Shortened 2026-08-29 for the path step card, where the time chip shares a 200px tile
corner with a cost chip — "Sign-up needed" and "one hour" do not fit one row. Checked in
all three places this drives: the Browse filter rail heading ("Time" above "15 min", "1
hour", "half a day", "several days" — reads as a list, not a sentence, so the shorter
forms are fine unparsed), the chip row on every card, and the new tile corner on a path
step.

### Below the fold — what this is

**Heading:** Every link here has a reason.

**Body:**

> There is a lot of material about Claude and no easy way to tell what is worth your
> time. So we read it, and we write down who each one is for — and who should skip it.
> Every resource shows the date we last checked it.

**Three points, each one line:**

| Heading | Line |
|---|---|
| We say when to skip | Every resource has a line telling you when not to bother. |
| We show the date | AI material goes stale in months. You can see how old ours is. |
| We say how we checked | Read in full, skimmed, or only found. We never claim more. |

**Link:** How we check →

---

## Browse

**Heading:** Browse

**Result count** — always exact:

- `77 resources`
- `1 resource`
- `12 resources for a researcher who has never used Claude`

When the two questions return very few results, say so and offer the way out:
`6 resources. Remove a filter to see more.`

**Search field label:** Search
**Search placeholder:** Title, topic, or what you want to do

**Sort control label:** Sort
Options: **Best checked first** · **Newest first** · **Shortest first**

### Start with these three *(the picks block)*

Shown only when exactly one role and one level are set and nothing else narrows the
list — the landing state of the home page's two questions. Any further filter or a
search hides the block: it must never recommend something the reader just excluded.

**Heading:** `Start with these three` — or `Start with these two` when the cell holds
two picks. One cell does (non-technical + built things with it): its candidate pool has
a single publisher, and the publisher cap holds that cell at two rather than let three
same-source picks masquerade as a choice. The heading must always agree with the count;
a "three" heading over two cards is the page miscounting in its own voice.

**Label:** `picked by AI · 31 Aug 2026` — the honesty label, same ladder as the tier
badges. Nothing may imply a person chose these. The date is `picked_on` from
data/picks.json, formatted like every other date on the site.

**Per-card reason** — one sentence under each picked card, saying why it beat the pool
rather than what it is (the card already says what it is). Held to the same bar as
`Skip if`: if someone who read the title would already know it, it is not doing work.
Written by the model at pick time, stored in data/picks.json, validated non-empty.

**Below the block:** `Everything else for you (67)` — the same results as before,
minus the three picks shown above. Nothing is hidden; the count line above the block
still counts everything.

These strings live in `LC.PICKS_UI` in assets/js/ui.js. This section and that object
change together or not at all.

### Filter panel

**Heading:** Filters
**Clear control:** Clear all
**Applied filter chip:** `researcher ×` — the × has aria-label `Remove filter: researcher`

Group headings, in this order:

1. **Role**
2. **Level**
3. **Time**
4. — divider — **More filters** *(collapsed by default)*
5. **Topic**
6. **Format**
7. **Cost**

Time stays visible in the panel — it is a useful filter, just not a good opening question.

**Cost labels**

| Value | Label |
|---|---|
| `free` | free |
| `free-account` | sign-up needed |
| `paid-once` | pay once |
| `subscription` | subscription |

Shortened 2026-08-29 for the same reason as Time above: the path step card's tile
cannot hold "free, sign-up needed" and "1 hour" in the same 200px corner. "Free" was
also redundant — every value in this row that is not `free` is a sign-up or a payment,
so pairing one with the word "free" answers a question the chip was not asked.

**Format labels:** video · course · docs · article · hands-on · podcast · code

**Topic labels:** chat and prompting · Claude Code · Cowork · Skills · connectors · agents · API · limits and safety

Mobile: filters open in a bottom sheet.
Sheet title: **Filters** · confirm button: **Show 24 resources** · dismiss: **Close**

---

## The resource card

Order of information on every card:

1. Badge — how we checked it
2. Title
3. Source and author
4. Three chips: format · time · cost
5. Who it's for
6. Skip if
7. Footer: checked date, plus a flag if it looks old

**Labels**

| Element | Copy |
|---|---|
| Who it's for | `For:` |
| Skip line | `Skip if:` |
| Checked date | `Checked 19 Aug 2026` |
| Outdated flag | `Published over a year ago — may not match Claude today` |
| Dead link | `This link no longer works` |
| In a path | `Step 2 of 6 in Your first week with Claude` |

`Skip if:` is set in the serif and carries more visual weight than `For:`. It is the
reason the site exists.

### Dates on a card

Two lines, and the card only ever shows what it actually knows.

**Published line** — one of:

- `Published 12 Jun 2026` — the page gave a publication date.
- `Published over a year ago — may not match Claude today` — it did, and it is old.
  This is the only one that takes the outdated colour.
- `No publish date given` — the page gave none. Said plainly rather than left blank,
  because a blank reads as an oversight and this is a fact about the source.

**Updated line** — `Updated 2 Sep 2026`, shown only when the page tells us when it was
last revised, and never otherwise.

Why two lines rather than one. Intercom-templated pages — the whole Claude Help Center —
print a last-updated date and never a publication date. Writing that into `published`
made cards state a publication date the page had never given, and 34 rows were doing
exactly that until 5 September 2026. `updated` is a real date or absent; it is never
`UNVERIFIED`, because absent already means "we do not know" and a second spelling of that
is a second thing to keep in step.

**The outdated flag measures from the later of the two.** A GOV.UK collection published
in June 2025 and revised in May 2026 is not a year stale, and saying so was wrong in
substance while being right about `published`. The string lives in `LC.UPDATED_PREFIX`
in `assets/js/ui.js`; that constant and this section change together.

### How-we-checked badges

Colour never carries this alone. The word is always present.

| Value | Badge | Tooltip |
|---|---|---|
| `reviewed` | **Read in full** | We went through all of it, and a person checked the notes. |
| `ai-reviewed` | **Read by AI** | AI read all of it. No person has checked the notes yet. |
| `previewed` | **Skimmed** | We read the outline or a free sample. We have not seen the whole thing. |
| `listed` | **Found only** | We found it and sorted it. Nobody has looked at the content yet. |

---

## Resource detail

**Back link:** ← Back to browse
**Primary button:** Open on [source name]
**Secondary:** Copy link

Section headings:

- **What it teaches**
- **Who it's for**
- **Skip it if**
- **Before this** *(prerequisites; omit if empty)*
- **After this** *(next in path; omit if empty)*
- **How we checked this one**

Provenance line at the bottom:

> Checked 19 Aug 2026 · Published 4 Mar 2026 · Found through the Anthropic Academy catalogue

---

## Paths

**Heading:** Paths
**Intro:** A short list, in order. Start at the top.

**Path card:** `6 steps · about 3 hours · free`
**Step marker:** `Step 3`
**Completion note:** We do not track your progress. Nothing here needs an account.

---

## How we check *(the About page)*

**Heading:** How we check

**Opening:**

> We would rather read fewer resources in full than list more we have only skimmed.
> Today the count read in full is zero, and the label on every card says how far we got.

**Sections**

**What we do**

> We find material, read as far as the label says, and write two things: who it helps,
> and who should skip it.
> Then we write down the date. When something drifts out of date, the date says so before
> we do.

**How thorough we were**

> Four levels, and we do not round up.
>
> **Read in full** — we went through all of it and a person checked the notes.
> **Read by AI** — AI read all of it. No person has checked the notes yet.
> **Skimmed** — we read the outline or a free sample. Paid courses usually stop here, because we cannot see inside them.
> **Found only** — we found it and sorted it. Nobody has looked at the content yet.

**What we will not do**

> We do not copy anyone's description. We do not list something whose page we cannot
> open. A paid course is opened at its sales page; the label says so. We do not
> take money to rank a resource. We are not affiliated with Anthropic.

**About Claude certification**

> Anthropic runs a real certification, but it is open to members of the Claude Partner
> Network, not to the public. A lot of sites sell preparation for an exam most readers
> cannot sit. If you find one of those, that is why it is not in here.

**Found something wrong?**

> Tell us. A dead link or an out-of-date note is the worst thing that can happen to a site
> like this.

---

## Empty, loading, and error states

| State | Copy |
|---|---|
| No results after filtering | **Nothing matches all of those.** Try removing one filter — time is usually the one to loosen. |
| Search found nothing | **No match for "[query]".** Try fewer words, or browse by role instead. |
| A filter group is empty | Nothing here yet for this. |
| A role has no resources | **We have not covered this role yet.** It's on the list. Browse everything instead. |
| A role + level combination has no resources | **We have nothing for this combination yet.** It's on the list. Loosen the level, or browse everything. |
| A path is not built yet | **This path isn't ready.** We only publish a path once every step in it has been checked. |
| Data file failed to load | **The directory didn't load.** Reload the page. If it keeps happening, the site is broken and we want to know. |
| Loading | Loading the directory… |

Search is instant and client-side. There is no spinner in normal use — the loading string
exists only for a cold start on a slow connection.

---

## Accessibility strings

| Element | Text |
|---|---|
| Skip link | Skip to content |
| Search field | `aria-label`: Search resources |
| Filter toggle, mobile | `aria-label`: Open filters |
| Remove a chip | `aria-label`: Remove filter: [name] |
| Role icon | `alt`: "" — decorative, the label sits next to it |
| Level icon | `alt`: Level: used it a little |
| Time icon | `alt`: Takes about one hour |
| Badge | Word is real text, never an image |
| Result count | `aria-live="polite"` so filtering is announced |

---

## Page titles and meta

| Page | `<title>` |
|---|---|
| Home | Learn Claude — find what's worth your time |
| Browse | Browse 77 Claude resources — Learn Claude |
| Filtered | Claude resources for researchers — Learn Claude |
| Resource | [Title] — Learn Claude |
| Path | [Path name] — a path — Learn Claude |
| About | How we check — Learn Claude |

**Meta description, home:**

> A checked directory of the best places to learn Claude. Every entry says who it's for,
> when to skip it, and the date we last looked.

---

## Strings that need care when this is translated

- **"Skip if"** — the whole idea. Some languages need a full clause: *"Do not read this if…"*. Length matters more than brevity here.
- **"Found only"** — must not read as "not good". It means nobody checked yet.
- **"Read by AI"** — must stay clearly weaker than "Read in full".
- German and Finnish will run roughly 30% longer. Badges must wrap, not truncate.
- Dates are written out (`19 Aug 2026`) so no reader has to guess day-month order.
