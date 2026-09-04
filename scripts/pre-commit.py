#!/usr/bin/env python3
"""
The pre-commit hook. Two checks, both local mirrors of things that have already shipped.

Installed by scripts/install-hooks.py, which writes a two-line .git/hooks/pre-commit
that calls this file. The logic lives here, in the repository, because a hook inside
.git/ is invisible to review and is not there at all on a fresh clone.

## 1. Control characters in tracked text

A backspace byte (0x08) has been written into this repository twice, both times the same
way: a regex containing `\\b` passed through a shell heredoc, which ate the backslash and
left the literal control character. The second time it produced a matcher that matched
everything - so the check reported zero findings, looked healthy, and had silently
stopped checking. It was caught only because a drop from 32 findings to 0 was too
convenient to believe.

CLAUDE.md now forbids putting a regex or a backslash through a heredoc. A rule is not a
guard, and that rule has been broken one commit after being written. This is the guard:
the byte cannot enter a tracked text file at all.

Tab, newline and carriage return are allowed. Everything else below 0x20, plus 0x7f, is
not. Binary files - images, fonts, PDFs - are skipped by extension and by a null-byte
sniff.

## 2. The catalogue validator

CI already runs it. Running it here too means the failure arrives before the commit
rather than after the push, which is the difference between fixing a thing and fixing a
thing plus a broken build on the default branch.

    python3 scripts/pre-commit.py            # check what is staged
    python3 scripts/pre-commit.py --all      # check every tracked file
"""

import argparse
import os
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Anything that is legitimately not text. Checked before the null sniff, because a font
# or an icon has every right to hold control bytes.
BINARY_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".woff",
              ".woff2", ".ttf", ".otf", ".eot", ".zip", ".gz", ".mp4", ".webm",
              ".pyc", ".so", ".dll", ".exe"}

ALLOWED_CONTROL = {0x09, 0x0a, 0x0d}          # tab, newline, carriage return


def git(*args):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return r.stdout.splitlines()


def staged_files():
    return [f for f in git("diff", "--cached", "--name-only", "--diff-filter=ACM") if f]


def all_files():
    return [f for f in git("ls-files") if f]


def control_chars(path):
    """[(line_no, col, byte)] for every disallowed control character."""
    full = os.path.join(ROOT, path)
    if os.path.splitext(path)[1].lower() in BINARY_EXT:
        return []
    try:
        raw = open(full, "rb").read()
    except OSError:
        return []
    if b"\x00" in raw:
        return []                                       # binary, not our business
    hits = []
    line = 1
    col = 0
    for b in raw:
        if b == 0x0a:
            line += 1
            col = 0
            continue
        col += 1
        if (b < 0x20 and b not in ALLOWED_CONTROL) or b == 0x7f:
            hits.append((line, col, b))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true",
                    help="check every tracked file, not only what is staged")
    args = ap.parse_args()

    files = all_files() if args.all else staged_files()
    if not files:
        print("pre-commit: nothing staged.")
        return 0

    bad = []
    for f in files:
        for line, col, b in control_chars(f):
            bad.append((f, line, col, b))

    if bad:
        print("pre-commit: control characters in tracked text.")
        print()
        for f, line, col, b in bad[:40]:
            name = {0x08: "BACKSPACE - a heredoc ate a backslash",
                    0x0c: "FORM FEED", 0x1b: "ESCAPE", 0x7f: "DELETE"}.get(
                        b, "control 0x%02x" % b)
            print("  %s:%d:%d  0x%02x  %s" % (f, line, col, b, name))
        if len(bad) > 40:
            print("  ... and %d more" % (len(bad) - 40))
        print()
        print("A backspace here is almost always a regex that went through a heredoc:")
        print("`\\\\b` became a literal 0x08 and the pattern now matches something else,")
        print("usually everything. Write the script to tmp/ and run the file instead.")
        print("CLAUDE.md, Working rules.")
        return 1

    print("pre-commit: %d file(s) clean of control characters." % len(files))

    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts",
                                                     "validate-catalogue.py")],
                       cwd=ROOT, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print()
        print("pre-commit: the catalogue validator says no.")
        print((r.stdout or "") + (r.stderr or ""))
        return 1
    print("pre-commit: catalogue valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
