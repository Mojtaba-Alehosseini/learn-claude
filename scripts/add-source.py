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
    # Institutions whose registrable name is an abbreviation nobody reads as a
    # publisher. prettify() gets these right in the sense that Jhu really is the
    # registrable name of jhu.edu - it is just not what the organisation is called.
    ("jhu.edu", "Johns Hopkins University Press", False),
    ("csun.edu", "California State University, Northridge", False),
    ("syr.edu", "Syracuse University", False),
    ("unsw.edu.au", "UNSW Sydney", False),
    ("unimelb.edu.au", "University of Melbourne", False),
    ("northumbria.ac.uk", "Northumbria University", False),
    ("pitt.edu", "University of Pittsburgh", False),
    ("eric.ed.gov", "ERIC", False),
    ("europa.eu", "European Commission", False),
    ("education.gov.au", "Australian Department of Education", False),
    ("qwe.edu.pl", "qwe.edu.pl", False),
    ("harvard.edu", "Harvard University", False),
    ("mit.edu", "MIT", False),
    ("stanford.edu", "Stanford University", False),
]

# Two-label public suffixes. These have to be known, because the label to their left is
# the name and the label to their right is not.
MULTI_SUFFIXES = {
    "ac.uk", "co.uk", "gov.uk", "org.uk", "sch.uk", "nhs.uk",
    "edu.au", "gov.au", "com.au", "org.au", "net.au",
    "ac.nz", "co.nz", "govt.nz", "edu.pl", "edu.sg", "edu.hk", "ac.jp", "co.jp",
    "ac.za", "co.za", "gov.in", "ac.in", "edu.in", "com.br", "com.mx", "ed.gov",
}

# Labels that are plumbing, never a publisher. Only used for the last-resort guard
# below, where nothing meaningful survived the suffix strip.
SUBDOMAIN_NOISE = ("www", "blog", "docs", "help", "learn", "support", "academy",
                   "guide", "guides", "gov", "edu", "ac", "co")


def prettify(host):
    """Fallback for an unmapped host: the registrable name, never a suffix.

    This used to work off a hardcoded tuple of TLDs and return whatever label was left,
    so any suffix missing from that tuple became the publisher. Live on the site, that
    produced "Open on Pl" for qwe.edu.pl, "Open on Vc" for airtree.vc, "Found through
    To" for every.to, plus "Ac", "Au", "Eu", "Ed" and "Gov" - 20 cards naming a
    top-level domain as the publisher. A blocklist of suffixes fails open on every
    suffix nobody thought of, which is all of them eventually.

    So take the label immediately left of the public suffix instead. Unknown suffixes
    are then handled correctly by default rather than incorrectly.
    """
    h = host.lower().strip(".")
    parts = [p for p in h.split(".") if p]

    # Drop a known two-label suffix, else a single trailing label.
    if len(parts) >= 3 and ".".join(parts[-2:]) in MULTI_SUFFIXES:
        parts = parts[:-2]
    elif len(parts) >= 2:
        parts = parts[:-1]

    # The registrable name is now the rightmost label left standing; subdomains sit to
    # its left and take care of themselves. An earlier version stripped them explicitly
    # and that broke education.gov.au, whose name really is "education".
    name = parts[-1] if parts else h
    if not name or name in SUBDOMAIN_NOISE:
        # Nothing meaningful survived - gov.uk is the whole name, not "gov".
        return host.replace("www.", "").upper() if len(host) <= 12 else host
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
