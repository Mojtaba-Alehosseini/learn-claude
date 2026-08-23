#!/usr/bin/env python3
"""
Validate a research report JSON before it goes anywhere near items.json.

Usage:
    python3 scripts/validate-report.py <file.json> [<file.json> ...]

Checks structure and vocabulary offline. Add --links to also check every URL
is alive (slow, needs network).

Add --pipeline if the file came from the Gemini analysis stage rather than from a
research run. Research runs may only claim tier 'previewed' or 'listed'; the
pipeline may also claim 'ai-reviewed' and 'reviewed'.

Exit code 1 if any ERROR is found. WARNINGs do not fail the run.
"""

import json
import re
import sys
import collections

ALLOWED = {
    "level": {"never-used", "basic", "confident", "builder"},
    "format": {"video", "course", "docs", "article", "hands-on", "podcast", "repo"},
    "time": {"under-15min", "under-1hr", "half-day", "multi-day"},
    "cost": {"free", "free-account", "paid-once", "subscription"},
    "tier": {"reviewed", "ai-reviewed", "previewed", "listed"},
    "status": {"live", "dead", "outdated"},
}

# Who may claim what. See docs/specs/2026-08-19-directory-spec.md section 7.
#   'reviewed'    — a person confirmed it. No automated stage may ever write it.
#   'ai-reviewed' — full content consumed by AI.
#                   A research run may claim it only for short text it can read in one
#                   fetch (docs, article). Never for video, course, podcast, repo.
#                   The Gemini pipeline may claim it for any format.
CONSUMED_TIERS = {"reviewed", "ai-reviewed"}
RESEARCH_READABLE_FORMATS = {"docs", "article"}

# Hidden fields written by the Gemini stage. Never shown on the site; they feed search.
# See docs/specs/2026-08-19-directory-spec.md section 9.
HIDDEN_LIST_FIELDS = ["keywords", "questions", "prerequisites", "teaches"]
MIN_KEYWORDS = 10
MIN_QUESTIONS = 3
TOPICS = {"chat-prompting", "claude-code", "cowork", "skills", "mcp", "agents", "api", "safety"}
ROLES = {"non-technical", "student", "researcher", "teacher", "developer",
         "data-analyst", "pm", "designer", "business-founder", "writer-marketer"}
REQUIRED = ["title", "url", "author", "roles", "level", "topics", "format",
            "time", "cost", "language", "tier", "summary", "who_for",
            "skip_if", "published", "checked", "status"]

# URL patterns that models invent. Left side is wrong, right side explains.
KNOWN_BAD_URLS = [
    (r"^https?://(www\.)?claude\.com/courses/",
     "claude.com/courses/<slug> does not exist. Anthropic Academy courses live at "
     "https://anthropic.skilljar.com/<slug>. The catalogue is at claude.com/resources/courses."),
    (r"^https?://docs\.anthropic\.com",
     "docs.anthropic.com now redirects. Use platform.claude.com/docs or code.claude.com/docs."),
    (r"^https?://(www\.)?github\.com/anthropics/anthropic-cookbook",
     "Renamed. Use github.com/anthropics/claude-cookbooks."),
    (r"^https?://(www\.)?github\.com/anthropics/anthropic-quickstarts",
     "Renamed. Use github.com/anthropics/claude-quickstarts."),
]

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def validate(path, check_links=False, pipeline=False):
    errors, warnings = [], []
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception as e:
        return [f"cannot parse JSON: {e}"], []

    if not isinstance(data, list):
        return ["top level is not a JSON array"], []

    seen_urls = collections.Counter()

    for i, item in enumerate(data):
        tag = f"[{i}] {str(item.get('title', '?'))[:45]}"

        for field in REQUIRED:
            if field not in item:
                errors.append(f"{tag}: missing field '{field}'")

        for field, allowed in ALLOWED.items():
            if field in item and item[field] not in allowed:
                errors.append(f"{tag}: {field}={item[field]!r} not allowed")

        for t in item.get("topics", []):
            if t not in TOPICS:
                errors.append(f"{tag}: topic {t!r} not allowed")
        for r in item.get("roles", []):
            if r not in ROLES:
                errors.append(f"{tag}: role {r!r} not allowed")
        if not item.get("roles"):
            errors.append(f"{tag}: roles is empty")
        if not item.get("topics"):
            warnings.append(f"{tag}: topics is empty")

        url = item.get("url", "")
        if not url.startswith("http"):
            errors.append(f"{tag}: url is not a URL: {url!r}")
        seen_urls[url] += 1
        for pattern, why in KNOWN_BAD_URLS:
            if re.match(pattern, url):
                errors.append(f"{tag}: BAD URL PATTERN {url}\n      -> {why}")

        if not DATE_RE.match(str(item.get("checked", ""))):
            errors.append(f"{tag}: checked={item.get('checked')!r} is not YYYY-MM-DD")

        pub = str(item.get("published", ""))
        if pub != "UNVERIFIED" and not DATE_RE.match(pub):
            errors.append(f"{tag}: published={pub!r} must be YYYY-MM-DD or UNVERIFIED")

        # skip_if is the whole point of the site
        if not str(item.get("skip_if", "")).strip():
            errors.append(f"{tag}: skip_if is empty — this field is the product")

        for field in ("summary", "who_for"):
            if not str(item.get(field, "")).strip():
                errors.append(f"{tag}: {field} is empty")

        tier = item.get("tier")
        fmt = item.get("format")

        if tier == "reviewed":
            errors.append(
                f"{tag}: tier='reviewed' means a person confirmed the judgment. "
                "No automated stage may write it. Use 'ai-reviewed'."
            )
        elif not pipeline and tier == "ai-reviewed" and fmt not in RESEARCH_READABLE_FORMATS:
            errors.append(
                f"{tag}: tier='ai-reviewed' with format={fmt!r} not allowed in a research "
                "report. A research run can fully read docs and articles, not video, "
                "courses or podcasts. Use 'previewed' or 'listed'."
            )

        # Hidden search fields. Required only in pipeline mode, once an item has
        # actually been through the Gemini stage.
        if pipeline and tier in CONSUMED_TIERS:
            for field in HIDDEN_LIST_FIELDS:
                value = item.get(field)
                if not isinstance(value, list) or not value:
                    errors.append(f"{tag}: {field} missing or empty (required at tier {tier!r})")
            kw = item.get("keywords") or []
            if isinstance(kw, list) and 0 < len(kw) < MIN_KEYWORDS:
                warnings.append(f"{tag}: only {len(kw)} keywords, expected at least {MIN_KEYWORDS}")
            qs = item.get("questions") or []
            if isinstance(qs, list) and 0 < len(qs) < MIN_QUESTIONS:
                warnings.append(f"{tag}: only {len(qs)} questions, expected at least {MIN_QUESTIONS}")

    for url, count in seen_urls.items():
        if count > 1:
            warnings.append(f"duplicate url x{count}: {url}")

    # Distribution sanity
    tiers = collections.Counter(it.get("tier") for it in data)
    consumed = sum(tiers.get(t, 0) for t in CONSUMED_TIERS)
    if pipeline and consumed > len(data) * 0.5:
        warnings.append(
            f"{consumed}/{len(data)} claim the full content was consumed. "
            "Check that the Gemini stage really processed each one."
        )
    unver = sum(1 for it in data if it.get("published") == "UNVERIFIED")
    if unver > len(data) * 0.6:
        warnings.append(f"{unver}/{len(data)} have published=UNVERIFIED. Weak date coverage.")

    if check_links:
        import urllib.request
        for item in data:
            url = item.get("url", "")
            if not url.startswith("http"):
                continue
            try:
                req = urllib.request.Request(url, method="HEAD",
                                             headers={"User-Agent": "Mozilla/5.0"})
                urllib.request.urlopen(req, timeout=15)
            except Exception as e:
                errors.append(f"DEAD LINK {url} ({e})")

    return errors, warnings


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check_links = "--links" in sys.argv
    pipeline = "--pipeline" in sys.argv
    if not args:
        print(__doc__)
        sys.exit(2)

    failed = False
    for path in args:
        errors, warnings = validate(path, check_links, pipeline)
        print("=" * 72)
        print(path)
        try:
            n = len(json.load(open(path, encoding="utf-8")))
            print(f"  {n} items")
        except Exception:
            pass
        if errors:
            failed = True
            print(f"\n  {len(errors)} ERROR(S):")
            for e in errors:
                print(f"    - {e}")
        if warnings:
            print(f"\n  {len(warnings)} WARNING(S):")
            for w in warnings:
                print(f"    - {w}")
        if not errors and not warnings:
            print("  clean")
        print()

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
