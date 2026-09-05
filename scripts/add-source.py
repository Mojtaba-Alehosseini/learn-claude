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
    ("productimpactpod.com", "Product Impact", False),

    # ---------------------------------------------------------------------------
    # Written out 2026-08-27, from each entry's own `author` field. Before this, 60
    # hosts fell through to prettify() and the publisher line on 51 cards read a
    # squashed domain fragment - "Ccforeveryone", "Artificialcorner", "Uxwritinghub",
    # "Aifluencyframework" - or, worse, named the wrong organisation entirely:
    # "Libguides" for two different university libraries, "Codes" for
    # vincent.codes.finance, "Stkate" for St. Catherine University.
    #
    # prettify() is not at fault and is not being replaced: it is the last resort, and
    # a last resort that reads badly is doing its job, because it makes the gap
    # visible. The gap is what was never closed.
    # ---------------------------------------------------------------------------
    ("nngroup.com", "Nielsen Norman Group", False),
    ("aakashg.com", "Aakash Gupta", False),
    # These four happen to come out right in prettify(), which is exactly why they are
    # written down: nobody should have to re-derive whether a correct-looking name was
    # chosen or guessed.
    ("every.to", "Every", False),
    ("learn.g2.com", "G2", False),
    ("gov.uk", "GOV.UK", False),
    ("kenny-kane.com", "Kenny Kane", False),
    ("academy.score.org", "SCORE", False),
    ("aiassessmentscale.com", "AI Assessment Scale", False),
    ("aifluencyframework.org", "AI Fluency Framework", False),
    ("airtree.vc", "Airtree", False),
    ("ajjuliani.com", "A.J. Juliani", False),
    ("alliekmiller.com", "Allie K. Miller", False),
    ("artificialcorner.com", "Artificial Corner", False),
    ("artofstyleframe.com", "Art of Styleframe", False),
    ("beutlerink.com", "Beutler Ink", False),
    ("ccforeveryone.com", "CC for Everyone", False),
    ("cianfrani.dev", "Louis Cianfrani", False),
    ("clauderesearcher.com", "Claude Researcher", False),
    ("codecademy.com", "Codecademy", False),
    ("dayofai.org", "MIT RAISE", False),
    ("designerup.co", "DesignerUp", False),
    ("eigent.ai", "Eigent AI", False),
    ("enterpret.com", "Enterpret", False),
    ("ethicscentral.org", "SPJ Ethics Central", False),
    ("intodesignsystems.com", "Into Design Systems", False),
    ("journalism.co.uk", "Journalism.co.uk", False),
    ("learning-claude.com", "Learning Claude", False),
    ("libguides.princeton.edu", "Princeton University Library", False),
    # Was printing "Und" - and "Open on Und" on the resource page. Two Attack 2
    # agents hit it. The breadcrumb reads "University of North Dakota > Research
    # Guides > Chester Fritz Library"; the library is already in `author`.
    ("libguides.und.edu", "University of North Dakota", False),
    ("libguides.stkate.edu", "St. Catherine University Library", False),
    ("libguides.tulane.edu", "Tulane University Libraries", False),
    ("localizelikeapro.com", "Localize Like A Pro", False),
    ("lszabo.me", "Laszlo Szabo", False),
    # Was printing "Master". Its own logo and copyright line say "Master.dev".
    ("master.dev", "Master.dev", False),
    # These four were mapped to their own domain to stop prettify() producing "Pl"
    # and friends. That solved the mangling and left a bare domain where a
    # publisher name belongs, which is the same fault one step later. Names read
    # off each site on 2026-09-05.
    ("mcpservers.org", "Awesome MCP Servers", False),
    ("modelcontextprotocol.io", "Model Context Protocol", False),
    ("monash.edu", "Monash University", False),
    ("niemanlab.org", "Nieman Lab", False),
    ("permissionless.krispuckett.com", "Kris Puckett", False),
    ("prodmgmt.world", "Prodmgmt World", False),
    ("productschool.com", "Product School", False),
    ("ranthebuilder.cloud", "Ran the Builder", False),
    ("reforge.com", "Reforge", False),
    ("sachinrekhi.com", "Sachin Rekhi", False),
    ("snyk.io", "Snyk", False),
    ("ssdnodes.com", "SSD Nodes", False),
    ("studentguidetoai.org", "Elon University", False),
    ("theopennotebook.com", "The Open Notebook", False),
    ("unesco.org", "UNESCO", False),
    ("uschamber.com", "US Chamber of Commerce", False),
    ("uxwritinghub.com", "UX Writing Hub", False),
    ("vanderbilt.edu", "Vanderbilt University", False),
    ("vincent.codes.finance", "Vincent Gregoire", False),
    ("willfrancis.com", "Will Francis", False),
    ("wotai.co", "WotAI", False),
    ("wrightmode.com", "Wright Mode", False),
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
    ("qwe.edu.pl", "QWE AI Academy", False),
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
PLATFORMS = ("youtube.com", "youtu.be",
             # Added 2026-08-27. The same argument as YouTube, and it had the same
             # effect: "Substack" was the publisher on 11 cards and "Medium" on 4,
             # while every one of those entries already recorded a real author.
             # "Libguides" was the publisher on two different university libraries -
             # one name for two institutions, which is worse than ugly.
             #
             # A Medium *publication* is not on this list. UX Collective and Design
             # Systems Collective have their own editors and their own standards, and
             # they stay mapped by name above. The test is whether the host chooses
             # what appears on it.
             "substack.com", "medium.com", "libguides.com", "buzzsprout.com",
             "kit.com", "bearblog.dev", "podcasts.apple.com")

# Channels that are Anthropic speaking in their own voice.
OFFICIAL_AUTHORS = {"anthropic", "claude", "anthropic ai", "claude by anthropic"}


def publisher_from_author(author):
    """A byline is not a publisher line. Trim one into the other.

    Reached only for hosts in PLATFORMS, where the account is the publisher and the
    `author` field is all we have. YouTube channel names arrive clean and pass straight
    through; a Substack or LibGuides author does not:

        "Anna Mills, College of Marin, with the PAIRR project team (UC Davis)"
                                                              -> "Anna Mills"
        "Doan Winkel (How to Teach With AI)"                  -> "Doan Winkel"
        "Derek Bruff, Intentional Teaching podcast"           -> "Derek Bruff"
        "University of Warwick Library"                       -> unchanged

    Cut at the first comma or opening bracket and nowhere else. Anything cleverer
    starts guessing which half of "Firstname Lastname (Publication)" the reader wanted,
    and both answers are defensible, so the rule stays boring and predictable.
    """
    name = re.split(r",| \(", (author or "").strip(), maxsplit=1)[0].strip()
    return name or (author or "").strip()


def source_for(url, author=""):
    host = re.split(r"/+", url)[1].lower()

    if any(host == d or host.endswith("." + d) for d in PLATFORMS):
        name = publisher_from_author(author)
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

    # This used to count every host missing from NAMES, and print prettify(host) beside
    # it. Both were wrong once PLATFORMS existed: a Substack post is handled by the
    # platform branch and never touches prettify, so the report was naming hosts that
    # were fine and showing a name the reader would never see. Count only the items that
    # really came out of the fallback, and show the name actually written.
    guessed = []
    for x in items:
        before = x.get("source", "")
        name, official = source_for(x["url"], x.get("author", ""))
        x["source"] = name
        x["official"] = official
        host = re.split(r"/+", x["url"])[1].lower()
        mapped = any(host == d or host.endswith("." + d) for d, _, _ in NAMES)
        platform = any(host == d or host.endswith("." + d) for d in PLATFORMS)
        if not mapped and not platform:
            unmapped[host] += 1
            guessed.append((host, name, x["title"]))
            # The failure that mangled "Product Impact" into "Productimpactpod" was
            # silent because only a total was printed. A guess that overwrites something
            # somebody wrote by hand says so, by name, every run.
            if before and before != name:
                print("  guessed %r over the %r that was already there -- %s"
                      % (name, before, x["title"][:52]))

    if "--check" in sys.argv:
        print(f"{len(unmapped)} hosts fall through to prettify(), "
              f"{sum(unmapped.values())} items:")
        for h, n in unmapped.most_common(40):
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
