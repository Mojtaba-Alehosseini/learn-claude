# What the `cost` field means

**`cost` is what it costs to consume this resource, not what it costs to use what it
teaches.**

That is the whole rule. Everything below is the working-out.

## Why it needed writing down

The field had been filled in two different ways by the same hand. On 2026-08-27, before
this was settled:

- *Get started with Claude Design* — a free Help Center page about a paid feature — read
  `free`.
- *Use Claude for Excel* — a free Help Center page about a paid feature — read
  `subscription`.

Both are Anthropic Help Center articles. Both cost nothing to read. Both describe
something that needs a paid plan. A reader filtering on `free` saw one of them.

## The test

Ask one question: **what does it cost me to read, watch or work through this?**

Not: what does it cost me to do the thing afterwards. That belongs in `skip_if`, where it
already is on every one of these — *"You are on a free plan. The add-in needs Pro, Max,
Team or Enterprise."*

| value | means |
|---|---|
| `free` | open it and consume it, no account, no money |
| `free-account` | free, but you must register before you can consume it |
| `paid-once` | one payment, and you own it |
| `subscription` | recurring payment, and access stops when it stops |

## What changed on 2026-08-27

Fourteen entries. Every one was tested with an unauthenticated request, and the ambiguous
ones were opened in a real browser as well.

**Eleven moved to `free`** — four from `subscription`, seven from `free-account`. All
Anthropic, Figma or Academy pages that answer a stranger in full with no sign-in:
Use Claude for Excel; Use research on Claude; Working smarter with Claude in PowerPoint;
the Product Management plugin page; the two Academy use-case pages; Delegating your first
task in Cowork; both Figma MCP help pages; Use Claude for Education; What are Projects?

**Two were mislabelled inside the paid values.** *PM Operating System* on
news.aakashg.com read `paid-once` and is a recurring Substack paywall, so
`subscription`. *Mushtaq Bilal* read `paid-once` while our own notes said the gate is an
email subscription, which costs nothing, so `free-account`.

**One moved the other way**, which is the part worth noticing. *Head of Claude Code: What
happens after coding is solved* read `free` and is behind a Substack paywall that closes
it after about 6,000 characters. The rule is not a licence to relabel everything `free`;
it is a question, and sometimes the answer is worse than what was recorded.

**Five stayed `subscription` after being checked rather than assumed:** Sachin Rekhi,
Lenny's *Everyone should be using Claude Code more*, Department of Product, Product
Compass, and Every's *Claude Code for Product Managers*. All five are genuinely truncated
mid-article. Two neighbours on the same hosts are not — Lenny's *How I AI* episode and
Every's product-management guide both open in full — so this is a per-article question,
never a per-host one.

## The one place the rule is uncomfortable

The two `claude-cookbooks` repos stay `free-account`, and strictly the rule says `free`:
you can read a notebook on GitHub without an account. But a notebook you never run has
not been consumed — its whole value is in running it, and running it needs an Anthropic
API key, which needs an account and then costs money per call.

So: **for a resource whose value only exists once you run it, consuming it means running
it.** `free-account` is the closest the four values reach; there is no usage-based value
in the vocabulary and this run did not invent one. If that ever matters enough, it is a
vocabulary change and it needs its own decision.

## Two things that are not `cost` faults

Medium's meter — several entries sit on Medium or its publications and read `free`. Their
`skip_if` lines already say the meter may close the page. A meter that lets most readers
through is not a subscription requirement, and marking those `subscription` would hide
genuinely free reading behind a filter.

Checking hosts instead of pages. Both false readings found in this sweep came from
assuming a host: Lenny's has free posts and paid posts, Every has free guides and paid
essays. Test the URL.

## How to check one

An unauthenticated request tells you most of it:

```bash
curl -sSL -A "Mozilla/5.0" "$URL" | grep -ioE "paid subscriber|sign in to read|enroll in course|keep reading with"
```

Treat a hit as a question rather than an answer. Substack puts *paid subscriber* in the
subscribe widget on free posts too, and a raw fetch can return text that a browser then
hides. When it matters, open the page and count the characters — that is what separated
the two Lenny's posts above, and a fetch had called Every's paywalled essay "completely
readable" minutes before a browser showed the gate.
