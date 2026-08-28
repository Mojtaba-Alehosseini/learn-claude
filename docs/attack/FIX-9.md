# Fix prompt — the seminar's level, and the data-analyst path

Paste everything below the line into Claude Code, in the project folder.

---

Strong round. Three things I want to name, because they are the habits worth keeping:

You caught that WebFetch called a paywalled essay "completely readable" and then went
back and re-checked *every* ambiguous cost decision in a browser — including four in the
opposite direction, which found a `free` entry that was actually gated. That is the same
shape as the runner-versus-laptop finding, and you generalised it instead of patching the
instance.

You found that the truth was already in the data: 51 of 62 mangled publishers had a
correct `author` sitting beside the wrong `source`.

And you pushed back on a decision I made. Rounding up is only the safer error while it
stays smaller than the error it replaces — a five-hour course called "several days"
overstates by more than `half-day` understated. You left it and put the real figure where
a reader sees it. That was right.

Two things now.

## 1. The seminar's `level` — the last field on that entry

I checked: `time`, `cost`, `tier` and `skip_if` are all correct now. `level: confident`
is the one you flagged and did not settle.

You already have what you need. Its own page says two contradictory things — "no prior
experience with AI tools or programming" against "a working knowledge of at least one
statistical computing language". You chose the stricter reading for `prerequisites`.
Make `level` agree with that choice, or explain why the two fields should differ.

One line either way. This is a small thing but it is the last inconsistency on an entry
that cost $995 and had four wrong fields a day ago.

## 2. Build the data-analyst path

You said the role can support one. I checked: 38 resources at `previewed` or better, and
`never-used` now has a real first step in *Upload files to Claude* — which is exactly the
gap you named two rounds ago as "no first step that is about data".

Same standard as the five that exist. Read `scripts/build-paths.py` first:

- 5 or 6 steps, referenced by URL, every step at least `previewed`
- **every step carries a `why`** that explains its position, not its content
- time and cost computed, never claimed
- the role-coverage check must pass

Three things specific to this one:

**The arc should be about data, not about Claude.** The writer path worked because it had
a real spine — learn it, stop it sounding like AI, disclose it honestly. This role's
equivalent is something like: get your data in front of it → make it actually calculate
rather than guess → know what it does with what you uploaded. You found that last piece
yourself when you added *How long do you store my data?*

**Confidentiality is not optional here.** A data analyst pastes other people's data. You
rejected Craig Hewitt's page because one sentence about training was wrong — on the page
where being wrong matters most. Whatever you pick for that step, hold it to that bar.

**Name the terminal, as you did for the PM path.** If a step needs Claude Code, its `why`
says so in the first clause. `confident` has 12 entries and several are Claude Code; a
data analyst who lives in Excel should be able to stop before that and still have gained
something.

Then tell me the weakest step, as you did last time — the one you would replace first.

## Not now

- **Designer.** Your spec names the three things that would change the answer. I would
  rather find them than pad it.
- **The email address**, and **nothing being `reviewed`.** Both still mine.

---

Two commits. Run to the end. Finish with what surprised you and what you got wrong —
those sections have caught a real fault in every single round, including one of your own
`skip_if` lines last time.
