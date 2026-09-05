#!/usr/bin/env python3
"""
Rule A: does the card say "built things with it", or does it say "used it a lot"?

    python3 scripts/audit-levels.py            # what would move, and why
    python3 scripts/audit-levels.py --apply    # move it, and log every change

THE DEFINITION (ux-copy.md carries the reader-facing version)

  built things with it   wrote code against the API; built a skill, an agent, a
                         connector or an automation; or set up Claude Code.

  used it a lot          everything else that assumes fluency - including running a
                         recipe in Cowork with connectors attached, which is using
                         Claude hard rather than building with it.

WHY

Attack 2's developer agent counted 148 rows from one prompt-recipe gallery, 78 of them
filed at `builder`, and made the argument in a line: a prompt recipe is not building.
The D12 measurement then showed the gallery is 43% of that level. "Account tracking" -
fifteen minutes, Cowork, a Salesforce connector - was sitting beside "Claude Agent SDK".

HOW IT DECIDES

A row moves only where something SAYS which it is, and silence leaves it alone. Moving
down needs positive evidence of the using kind and no building evidence anywhere in the
card. Moving up needs evidence that cannot mean anything else - a SKILL.md, an SDK, an
MCP server, an API key - because a mention of Claude Code is not the same as being about
setting it up.

The evidence is the card's own words, plus one thing outside them: a URL under
academy.claude.com/use-cases/, which is the publisher's own filing and a stronger
statement than a three-line card can make. It is still only half the test; a gallery row
whose card names a building act stays, which is why "Encode the brand as a skill" is
untouched.

Every decision prints the phrase that produced it, so a wrong one is visible rather than
buried in a count.
"""

import io
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "data", "items.json")
LEVELS = ["never-used", "basic", "confident", "builder"]
FIELDS = ("title", "summary", "who_for", "skip_if")

# Each entry is (pattern, what it is evidence of). Ordered by how load-bearing it is, so
# the phrase printed beside a move is the strongest one found rather than the first.
BUILDS = [
    (r"\bSKILL\.md\b", "authoring a skill file"),
    (r"\bCLAUDE\.md\b", "a Claude Code project file"),
    (r"\bclaude code\b", "Claude Code"),
    (r"\bagent sdk\b|\bpython sdk\b|\btypescript sdk\b", "an SDK"),
    (r"\bmcp server\b|\bbuild an mcp\b|\bwrite an mcp\b", "an MCP server"),
    (r"\bapi key\b|\bmessages api\b|\bthe claude api\b|\bapi call\b|\bapi request\b",
     "the API"),
    # The gap was two words and "Encode the brand as a skill" fell through it - a row
    # the ruling names as one that stays at builder. Forty characters covers the way
    # these titles are actually written without reaching into the next sentence.
    (r"\b(build|write|author|create|encode|ship|turn)\w*\b[^.]{0,40}?\b"
     r"(skill|agent|subagent|connector|mcp server|plugin|hook)s?\b", "building one"),
    (r"\bgithub action\b|\bci pipeline\b|\bin ci\b", "automation in CI"),
    (r"\bhooks?\b(?!\s+(?:you|them))", "hooks"),
    (r"\bsubagents?\b", "subagents"),
    (r"\bterminal\b|\bcommand line\b|\bthe cli\b", "a terminal"),
    (r"\bnpm\b|\bpip install\b|\buvx\b|\bdocker\b", "an install step"),
    (r"\bwrite (?:the )?code\b|\bwriting code\b|\bcodebase\b|\bpull requests?\b",
     "writing code"),
    # Added after the first cut moved "Building effective agents" and "Effective context
    # engineering for AI agents" out of `builder`. A list of phrases never covers a
    # subject, so these name the subject instead of the verb.
    (r"\bbuild\w*\b[^.]{0,40}\bagents?\b|\bagents?\b[^.]{0,30}\bin production\b",
     "building agents"),
    (r"\bcontext engineering\b", "context engineering"),
    (r"\borchestrat\w+\b", "orchestration"),
    (r"\bevals?\b|\bevaluation harness\b", "evals"),
    (r"\btool use\b|\bfunction calling\b|\bstructured outputs?\b", "the tool loop"),
    (r"\bprompt caching\b|\btoken budget\b|\bcontext window\b", "context mechanics"),
    (r"\bbedrock\b|\bvertex ai\b|\bself-host\w*\b|\bdeploy\w*\b", "deployment"),
    (r"\bmanaged agents?\b|\bagent harness\b|\bautonomous\b", "an agent runtime"),
    (r"\bmcp\b", "MCP"),
]

# Evidence that a row is USING Claude hard rather than building it. A row moves down only
# when one of these matches AND nothing in BUILDS does - "the card says which it is",
# rather than "the card failed to say it builds", which is how the first cut came to move
# the canonical agent-engineering writing out of `builder`.
#
# "prompt" and "Projects" are deliberately NOT here. Every row in the catalogue is about
# prompting somewhere, and Projects appears in genuine building work; both matched
# everything and decided nothing.
USES = [
    (r"\bcowork\b", "Cowork"),
    (r"\bconnectors?\b", "a connector, used not built"),
    (r"\bsample skill\b|\bskill bundle\b|\bpre-?built skill\b",
     "a skill someone else built"),
    (r"\buse cases?\b|\brecipe\b", "a recipe"),
    # The title shape. "Using the Egnyte connector for data room management",
    # "How to use the single-cell-rna-qc skill with Claude" - the card opens by
    # saying it is about using a thing somebody else built. Anchored to the start
    # of the title so it cannot fire on "using" inside a sentence about building.
    (r"^(using|how to use)\b", "the title says using"),
]

# Only these four move a row UP. They cannot mean anything but building: you do not
# mention a SKILL.md, an SDK, an MCP server or an API key while using a recipe. A bare
# "Claude Code" would move 66 rows, and mentioning Claude Code is not the same as being
# about setting it up - the same error the first cut made downwards.
STRONG_UP = {"authoring a skill file", "an SDK", "an MCP server", "the API"}

BUILDS = [(re.compile(p, re.I), why) for p, why in BUILDS]
USES = [(re.compile(p, re.I), why) for p, why in USES]


def blob(it):
    return " ".join(str(it.get(f) or "") for f in FIELDS) + " " + \
           " ".join(it.get("teaches") or [])


def builds_evidence(it):
    text = blob(it)
    for rx, why in BUILDS:
        m = rx.search(text)
        if m:
            return why, m.group(0)
    return None, None


# The publisher's own filing. A row under this path is a use-case recipe because that is
# the shelf its publisher put it on, which is a stronger statement about what it is than
# anything a three-line card can manage.
GALLERY = "https://academy.claude.com/use-cases/"


def uses_evidence(it):
    text = blob(it)
    for rx, why in USES:
        # An anchored pattern is about the title's shape, so it is asked of the title
        # alone; the rest search the whole card.
        m = (rx.search(str(it.get("title") or "")) if rx.pattern.startswith("^")
             else rx.search(text))
        if m:
            return why, m.group(0)
    if it.get("url", "").startswith(GALLERY):
        return "the publisher files it under use-cases", "academy.claude.com/use-cases/"
    return None, None


def main():
    apply = "--apply" in sys.argv
    with io.open(P, encoding="utf-8") as f:
        items = json.load(f)

    before = Counter(x["level"] for x in items)
    down, up, stayed, weak_up = [], [], [], []

    for it in items:
        why, phrase = builds_evidence(it)
        if it["level"] == "builder" and not why:
            uw, up_ = uses_evidence(it)
            # Only where the card positively says it is the using kind. Silence leaves
            # the row where it is; see the note above USES.
            if uw:
                down.append((it, uw, up_))
            else:
                stayed.append(it)
        elif it["level"] == "confident" and why in STRONG_UP:
            up.append((it, why, phrase))
        elif it["level"] == "confident" and why:
            weak_up.append((it, why, phrase))

    print("MOVING DOWN - builder -> confident (%d)" % len(down))
    for it, why, phrase in down:
        print("  %-52s %s%s" % (it["title"][:52], why,
                                (" %r" % phrase) if phrase else ""))
    print()
    print("STAYED at builder because the card says neither (%d)" % len(stayed))
    for it in stayed[:20]:
        print("  %s" % it["title"][:72])
    if len(stayed) > 20:
        print("  ... and %d more" % (len(stayed) - 20))
    print()
    print("MOVING UP - confident -> builder (%d), on evidence that cannot mean "
          "anything else" % len(up))
    for it, why, phrase in up:
        print("  %-52s %s %r" % (it["title"][:52], why, phrase))
    print()
    print("Mentions building but is NOT moved up (%d) - a mention is not a subject; "
          "printed, never applied" % len(weak_up))
    for it, why, phrase in weak_up[:12]:
        print("  %-52s %s %r" % (it["title"][:52], why, phrase))
    if len(weak_up) > 12:
        print("  ... and %d more" % (len(weak_up) - 12))

    print()
    print("Levels before: %s" % ", ".join("%s %d" % (L, before[L]) for L in LEVELS))
    if apply:
        for it, _w, _p in down:
            it["level"] = "confident"
        for it, _w, _p in up:
            it["level"] = "builder"
        after = Counter(x["level"] for x in items)
        with io.open(P, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(items, ensure_ascii=False, indent=2) + "\n")
        print("Levels after:  %s" % ", ".join("%s %d" % (L, after[L]) for L in LEVELS))
        print("written: data/items.json")
    else:
        after = Counter(before)
        after["builder"] += len(up) - len(down)
        after["confident"] += len(down) - len(up)
        print("Levels after:  %s  (dry run)"
              % ", ".join("%s %d" % (L, after[L]) for L in LEVELS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
