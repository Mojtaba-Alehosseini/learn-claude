# Prompt to run the attack

Paste everything below the line into Claude Code, in the project folder.

---

Big job, long session. **Read `docs/attack/PLAN.md` first and follow it exactly** — it
exists so nothing gets invented, confused or skipped. `docs/attack/00-facts.md` holds
the measured ground truth; if any agent's number disagrees with it, that file wins.

Ten roles, one agent each, each one attacking the live site as that person. Two batches
of five, as the plan says. After batch A, check all five files against the tracker
before you start batch B.

The four things I care about most, in order:

1. **Hostility.** An agent that comes back pleased has failed. These people have an hour
   and no patience. If a role is badly served, I want to read exactly how it feels, in
   that person's voice, with the real titles they were shown quoted back at me.
2. **Evidence.** Every number from `00-facts.md`, a command you show, or the live site.
   No "probably" in a finding.
3. **All eleven sections, all ten files.** An empty section says "nothing found". It is
   never deleted.
4. **Nobody fixes anything.** Findings only. No edits outside `docs/attack/`.

The plan has an "already known" list at the bottom — six things I found before this
exercise. Agents may sharpen them, but I am paying for what is *not* on that list.

When all ten are in, read them all and write `docs/attack/SUMMARY.md` to the structure
in the plan. Then verify: every point in the summary must trace back to a numbered
finding in one of the ten files. A summary point with no parent gets deleted, not
softened.

Commit the ten files and the summary. Tell me, short: how many roles are badly served,
the single worst finding, and anything the ten agents disagreed about.
