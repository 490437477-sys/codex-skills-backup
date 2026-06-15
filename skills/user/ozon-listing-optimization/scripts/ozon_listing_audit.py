#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ozon_listing_audit.py — Audit a draft Ozon listing for Russian keyword coverage.

Given a draft title + rich content + bullets + attribute list + target Russian keywords,
returns a coverage report: which keywords are present where, which are missing.

Usage:
  python ozon_listing_audit.py --title "..." --content-file description.html --keywords-file keywords.txt
  python ozon_listing_audit.py --title "..." --content "..." --keywords "купить, наушники, bluetooth"
  python ozon_listing_audit.py --help

Useful for:
- Verifying Mode A output before publishing
- Auditing existing listing after competitor analysis
- Sanity-check after edits
"""

import argparse
import sys
import re

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def strip_html(html: str) -> str:
    """Strip HTML tags and decode common entities. Very basic."""
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"&quot;", chr(34), text)
    text = re.sub(r"&#39;", chr(39), text)
    return re.sub(r"\s+", " ", text).strip()


def normalize(text: str) -> str:
    """Lowercase + collapse whitespace for fuzzy matching."""
    return re.sub(r"\s+", " ", text.lower().strip())


def load_keywords(path: str) -> list:
    """Load keywords from file (one per line, or comma-separated)."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # Try both separators
    if "," in content:
        kws = [k.strip() for k in content.split(",") if k.strip()]
    else:
        kws = [k.strip() for k in content.splitlines() if k.strip()]
    return kws


def check_coverage(keywords: list, title: str, content_html: str, bullets: list, attributes: dict) -> dict:
    """Check each keyword against each section."""
    title_n = normalize(title)
    content_text = normalize(strip_html(content_html))
    bullets_text = normalize(" ".join(bullets)) if bullets else ""
    attrs_text = normalize(" ".join(f"{k} {v}" for k, v in (attributes or {}).items()))

    results = {}
    for kw in keywords:
        kw_n = normalize(kw)
        in_title = kw_n in title_n
        in_content = kw_n in content_text
        in_bullets = bool(bullets_text) and kw_n in bullets_text
        in_attrs = bool(attrs_text) and kw_n in attrs_text

        sections_present = sum([in_title, in_content, in_bullets, in_attrs])

        if sections_present == 0:
            status = "[MISSING]"
        elif sections_present == 1 and not in_title:
            status = "[WEAK]"
        elif in_title and in_content:
            status = "[STRONG]"
        else:
            status = "[PARTIAL]"

        results[kw] = {
            "in_title": in_title,
            "in_content": in_content,
            "in_bullets": in_bullets,
            "in_attributes": in_attrs,
            "status": status,
        }

    return results


def render_report(results: dict, title: str) -> None:
    """Print the audit report."""
    total = len(results)
    strong = sum(1 for r in results.values() if r["status"] == "[STRONG]")
    partial = sum(1 for r in results.values() if r["status"] == "[PARTIAL]")
    weak = sum(1 for r in results.values() if r["status"] == "[WEAK]")
    missing = sum(1 for r in results.values() if r["status"] == "[MISSING]")

    coverage_pct = round(strong * 100.0 / max(total, 1), 1)
    incl_partial_pct = round((strong + partial) * 100.0 / max(total, 1), 1)

    print("=== Ozon Listing Audit ===")
    print("Title: " + (title[:80] + ("..." if len(title) > 80 else "")))
    print("Title length: " + str(len(title)) + " / 200")
    print("")
    print("Total keywords: " + str(total))
    print("Strong coverage: " + str(strong) + " (" + str(coverage_pct) + "%)")
    print("Including partial: " + str(strong + partial) + " (" + str(incl_partial_pct) + "%)")
    print("Weak only: " + str(weak))
    print("Missing: " + str(missing))
    print("")
    print("--- Keyword Coverage Detail ---")
    print("")
    print(f"{'Keyword':<40}{'Title':<8}{'Content':<10}{'Bullets':<10}{'Attrs':<8}{'Status'}")
    print("-" * 86)
    for kw, r in results.items():
        t = "Y" if r["in_title"] else "-"
        c = "Y" if r["in_content"] else "-"
        b = "Y" if r["in_bullets"] else "-"
        a = "Y" if r["in_attributes"] else "-"
        kw_disp = kw[:38] + ".." if len(kw) > 40 else kw
        print(f"{kw_disp:<40}{t:<8}{c:<10}{b:<10}{a:<8}{r['status']}")
    print("")
    if missing > 0:
        print("--- Missing Keywords (must be added) ---")
        for kw, r in results.items():
            if r["status"] == "[MISSING]":
                print("  X " + kw)
        print("")
    if weak > 0:
        print("--- Weak Coverage (only in 1 non-title section) ---")
        for kw, r in results.items():
            if r["status"] == "[WEAK]":
                print("  ? " + kw)
        print("")


def main():
    parser = argparse.ArgumentParser(description="Ozon listing keyword coverage audit")
    parser.add_argument("--title", required=True, help="Draft Ozon listing title (Russian)")
    parser.add_argument("--content", help="Draft rich-content HTML (inline)")
    parser.add_argument("--content-file", help="Path to rich-content HTML file")
    parser.add_argument("--bullets", help="Comma-separated key features / bullets")
    parser.add_argument("--attributes", help='Attribute key=value pairs, semicolon-separated, e.g. "Бренд=XIAOMI;Цвет=Белый"')
    parser.add_argument("--keywords", help="Comma-separated target Russian keywords")
    parser.add_argument("--keywords-file", help="Path to file with one keyword per line")
    args = parser.parse_args()

    if not (args.keywords or args.keywords_file):
        print("Error: provide --keywords or --keywords-file")
        sys.exit(1)

    if args.keywords:
        keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    else:
        keywords = load_keywords(args.keywords_file)

    content_html = ""
    if args.content:
        content_html = args.content
    elif args.content_file:
        with open(args.content_file, "r", encoding="utf-8") as f:
            content_html = f.read()

    bullets = []
    if args.bullets:
        bullets = [b.strip() for b in args.bullets.split(",") if b.strip()]

    attributes = {}
    if args.attributes:
        for pair in args.attributes.split(";"):
            if "=" in pair:
                k, v = pair.split("=", 1)
                attributes[k.strip()] = v.strip()

    results = check_coverage(keywords, args.title, content_html, bullets, attributes)
    render_report(results, args.title)


if __name__ == "__main__":
    main()
