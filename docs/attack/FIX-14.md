# Fix prompt — the two decisions, then run all 37

Paste everything below the line into Claude Code, in the project folder.

---

The three checkpoint cells hold. The reasons are comparative, answerable from the cards,
and they survive at pool sizes 10, 69 and 78. The 69-vs-70 reconciliation is accepted.
Go — with two decisions and one correction.

# Decision 1 — the two unsatisfiable cells

Your option 2, with its consequence stated plainly: **at most 2 picks from one publisher
when the pool has fewer than 3 publishers.**

- `data-analyst|builder` (2 publishers): 2 + 1 is legal. Three picks.
- `non-technical|builder` (1 publisher): the cap allows only **2 picks**. Show two, and
  the heading must say two — never a "three" heading over two cards.

The build prints every publisher-thin cell. The relaxation must never be silent.

Do not relax further. Three from one publisher is the exact masquerade the rule exists
to stop.

# Decision 2 — the topic blind spot, and why your proposed fix is not enough

Yes to a topic dimension — but check the vocabulary first. The topic axis is
`chat and prompting · Claude Code · Cowork · Skills · connectors · agents · API ·
limits and safety`. **"Claude Design" is not in it.** A code check over `topics[]` could
not have caught your own designer failure, because the clustering was at product level
and the field does not record products. So, two layers:

1. **Constraint 4, in code, graceful like formats:** no two picks share a primary topic,
   where the pool allows it. Primary = first entry of `topics[]`. It catches what the
   field can see.
2. **A subject self-check in the model step, for what the field cannot see.** After
   picking, the model states a one-line subject for each pick. If two or more match, it
   must swap or justify, and the justification is stored with the runners-up. You found
   the designer failure while writing the reason sentences — this makes that accident a
   step.

Make the designer|basic swap you proposed. The Help Center item goes to runners-up with
its reason. Its access-gating point (which plans can open Claude Design at all) was the
strongest thing about it — if the replacement's reason sentence is weaker than that,
stop and tell me instead of shipping it.

# Then run all 37

Everything in FIX-13 stands: URLs not ids, runners-up stored, `picked_by: "ai"` +
`picked_on`, the model told it is ranking our notes and not the resources, constraints
checked in code with reject-and-re-ask.

**Staleness, two different severities:**

- Pool changed (grew, shrank, item re-tiered): the build **warns** and names the stale
  cells. The picks still ship — `picked_on` is on the card, and re-picking needs a model
  run CI cannot do. Stale and dated is honest.
- A picked URL is dead, gone from the catalogue, or no longer passes the pre-filter:
  that is an **error** and the build fails. A dead pick must never ship.

**Validator:** `picks.json` gets its own rules — every pick URL exists and is live, tier
is not `listed`, counts and all four constraints hold for what the pool allows,
fingerprint present. Wire it into CI before `build.sh`, like the catalogue rules.

# The UI

As specced in FIX-13: only when both role and level are set. Picks block, then
"Everything else for you (N)". Three or fewer candidates → no block. Empty cell → say
so plainly. Every new reader-facing string goes into `ui.js` and
`docs/design/ux-copy.md` together — no drift.

Then open it in a real browser — a big cell, a thin cell, the two-pick cell, and
mobile. A headless pass has lied to us four times before.

# Commits

Check `git status` first — `items.json`, `paths.json`, `publisher-marks.json` and
`docs/attack/04-teacher.md` carry uncommitted changes from before this job. Anything
that is not part of this job gets its own commit or a question, not a ride-along.

Then: pipeline + `picks.json` + validator in one commit, Browse UI in a second.

# Not yours

Still mine: the email address, and that nothing is `reviewed`. Do not start either.

Finish with what surprised you and what you got wrong.
