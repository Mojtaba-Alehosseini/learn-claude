#!/usr/bin/env python3
"""
Give every item a human-readable `source` — the publisher, as a reader would name it.

The card shows "Anthropic" or "Coursera", not "support.claude.com". Deriving it in the
browser means every page reimplements the same guesswork, so we do it once here.

Also sets `official`: true when the publisher is Anthropic. The site uses that to say
"from Anthropic" rather than implying we are affiliated with them.

    python3 scripts/add-source.py
    python3 scripts/add-source.py --check     # list anything still unmapped
"""

import json
import re
import sys
import collections

ITEMS = "data/items.json"

# Longest match wins, so put specific hosts before their parent domain.
NAMES = [
    ("anthropic.skilljar.com", "Anthropic Academy", True),
    ("academy.claude.com", "Anthropic Academy", True),
    ("support.claude.com", "Claude Help Center", True),
    ("privacy.claude.com", "Claude Privacy Center", True),
    ("platform.claude.com", "Claude Platform docs", True),
    ("code.claude.com", "Claude Code docs", True),
    ("docs.claude.com", "Claude docs", True),
    ("claude.com", "Anthropic", True),
    ("anthropic.com", "Anthropic", True),
    ("github.com", "GitHub", False),
    ("youtube.com", "YouTube", False),
    ("youtu.be", "YouTube", False),
    ("coursera.org", "Coursera", False),
    ("udemy.com", "Udemy", False),
    ("datacamp.com", "DataCamp", False),
    ("deeplearning.ai", "DeepLearning.AI", False),
    ("freecodecamp.org", "freeCodeCamp", False),
    ("frontendmasters.com", "Frontend Masters", False),
    ("pluralsight.com", "Pluralsight", False),
    ("linkedin.com", "LinkedIn Learning", False),
    ("maven.com", "Maven", False),
    ("skillshare.com", "Skillshare", False),
    ("oreilly.com", "O'Reilly", False),
    ("edx.org", "edX", False),
    ("substack.com", "Substack", False),
    ("medium.com", "Medium", False),
    ("towardsdatascience.com", "Towards Data Science", False),
    ("uxdesign.cc", "UX Collective", False),
    ("dev.to", "DEV", False),
    ("reddit.com", "Reddit", False),
    ("news.ycombinator.com", "Hacker News", False),
    ("wikipedia.org", "Wikipedia", False),
    ("figma.com", "Figma", False),
    ("nature.com", "Nature", False),
    ("ieee.org", "IEEE", False),
    ("icmje.org", "ICMJE", False),
    ("elsevier.com", "Elsevier", False),
    ("simonwillison.net", "Simon Willison", False),
    ("claudelog.com", "ClaudeLog", False),
    ("builder.io", "Builder.io", False),
    ("lennysnewsletter.com", "Lenny's Newsletter", False),
    ("learning.northeastern.edu", "Northeastern University", False),
    ("tomsguide.com", "Tom's Guide", False),
    ("forbes.com", "Forbes", False),
    ("sba.gov", "US Small Business Administration", False),
    ("effortlessacademic.com", "Effortless Academic", False),
    ("ccforpms.com", "Claude Code for PMs", False),
    ("productcompass.pm", "The Product Compass", False),
    ("creatoreconomy.so", "Creator Economy", False),
    ("designsystemscollective.com", "Design Systems Collective", False),
    ("aihorizons.io", "AI Horizons", False),
    ("mediacopilot.ai", "Media Copilot", False),
    ("spj.org", "Society of Professional Journalists", False),
    ("cornell.edu", "Cornell University", False),
    ("harvard.edu", "Harvard University", False),
    ("mit.edu", "MIT", False),
    ("stanford.edu", "Stanford University", False),
]

# TLDs we strip before making a name. Anything ending in one of these loses it.
TLDS = ("com", "org", "net", "io", "ai", "co", "dev", "edu", "gov", "me", "so", "cc",
        "pm", "sh", "app", "tech", "xyz", "info", "news", "blog", "uk", "de", "fr")


def prettify(host):
    """Fallback for an unmapped host. Take the registrable name, not the suffix —
    productcompass.pm must not come out as 'Pm'."""
    h = re.sub(r"^(www|blog|docs|help|learn|support|academy|guides?)\.", "", host)
    parts = [p for p in h.split(".") if p]
    while len(parts) > 1 and parts[-1] in TLDS:
        parts.pop()
    name = parts[-1] if parts else host
    return name.replace("-", " ").title()


# Hosts that publish nothing themselves — the channel or account is the real publisher.
# Naming the platform here would put "YouTube" on 72 cards and hide the fact that 20 of
# them are Anthropic's own videos.
PLATFORMS = ("youtube.com", "youtu.be")

# Channels that are Anthropic speaking in their own voice.
OFFICIAL_AUTHORS = {"anthropic", "claude", "anthropic ai", "claude by anthropic"}


def source_for(url, author=""):
    host = re.split(r"/+", url)[1].lower()

    if any(host == d or host.endswith("." + d) for d in PLATFORMS):
        name = (author or "").strip()
        if not name:
            return "YouTube", False
        return name, name.lower() in OFFICIAL_AUTHORS

    for domain, name, official in NAMES:
        if host == domain or host.endswith("." + domain):
            return name, official
    return prettify(host), False


def main():
    items = json.load(open(ITEMS, encoding="utf-8"))
    unmapped = collections.Counter()

    for x in items:
        name, official = source_for(x["url"], x.get("author", ""))
        x["source"] = name
        x["official"] = official
        host = re.split(r"/+", x["url"])[1].lower()
        if not any(host == d or host.endswith("." + d) for d, _, _ in NAMES):
            unmapped[host] += 1

    if "--check" in sys.argv:
        print(f"{len(unmapped)} unmapped hosts, {sum(unmapped.values())} items:")
        for h, n in unmapped.most_common(30):
            print(f"   {n:3}  {h:38} -> {prettify(h)}")
        return

    json.dump(items, open(ITEMS, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    c = collections.Counter(x["source"] for x in items)
    off = sum(1 for x in items if x["official"])
    print(f"{len(items)} items, {len(c)} distinct sources")
    print(f"official Anthropic: {off} ({100*off/len(items):.0f}%)")
    print("top:", " · ".join(f"{k} {v}" for k, v in c.most_common(10)))
    print(f"unmapped hosts using the fallback name: {len(unmapped)}")


if __name__ == "__main__":
    main()
