#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ozon backend keyword deduplicator for Ozon.ru / Ozon.kz / Ozon.by.

Builds backend keywords from seller-visible Russian copy + a seed list,
expands with Russian commercial prefixes and a Latin transliteration, and
filters subjective adjectives (красивый / качественный / стильный / ...)
that hurt Ozon search relevance.

Output: a single space-joined string for the Ozon "ключевые слова" field
(soft cap ~1000 chars).

Usage:
  python ozon_keyword_dedup.py --visible "Беспроводные наушники" --seeds "наушники bluetooth"
  python ozon_keyword_dedup.py --visible-file title.txt --seeds "кружка,чашка" --max-chars 1000
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


SUBJECTIVE_STEMS = [
    "красив", "качественн", "стильн", "модн", "уникальн",
    "превосходн", "идеальн", "популярн", "известн",
    "дешёв", "недорог", "дорог", "хорош", "отличн",
    "прекрасн", "элитн", "премиальн", "крут", "лучш",
]
COMMERCIAL_PREFIXES = [
    "купить", "купить недорого", "купить со скидкой", "купить оптом",
    "заказать", "недорого", "со скидкой", "оптом",
    "в подарок", "акция", "распродажа", "новинка", "новый", "новая",
]
DECLENSION_SUFFIXES = ["", "а", "я", "у", "ю", "ой", "ей", "ы", "и", "ам", "ами"]
LATIN = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e",
    "ё": "yo", "ж": "zh", "з": "z", "и": "i", "й": "y", "к": "k",
    "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
    "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "ts",
    "ч": "ch", "ш": "sh", "щ": "sch", "ъ": "", "ы": "y", "ь": "",
    "э": "e", "ю": "yu", "я": "ya",
}


@dataclass
class DedupResult:
    keywords: list
    joined: str
    char_count: int
    dropped_subjective: int
    seed_variants: int


def is_subjective(token: str) -> bool:
    return any(token.startswith(s) for s in SUBJECTIVE_STEMS)


def extract_tokens(text: str) -> list:
    """Lowercase + tokenize. Keeps Cyrillic, Latin, digits."""
    if not text:
        return []
    text = re.sub(r"[^\w\s\-]", " ", text.lower(), flags=re.UNICODE)
    return [t for t in text.split() if len(t) >= 2]


def translit(token: str) -> str:
    """Approximate Russian-to-Latin. One variant is enough for backend."""
    return "".join(LATIN.get(c, c) for c in token)


def expand_seed(seed: str) -> list:
    """Russian variants + transliteration for one seed."""
    seed = seed.strip().lower()
    if not seed:
        return []
    head = seed.split()[0] if " " in seed else seed
    out = {seed}
    if head and head[-1] not in "аяоёыиуэюйьъ":
        out.add(head + "ы")
    for sfx in DECLENSION_SUFFIXES:
        if sfx:
            out.add(head + sfx)
    out.add(translit(head))
    for pfx in COMMERCIAL_PREFIXES:
        out.add(pfx + " " + head)
        out.add(pfx + " " + seed)
    return [w for w in out if w and len(w) >= 2]


def build_keywords(visible: str, seeds: list) -> DedupResult:
    """Combine visible tokens + seed expansions, dedup, filter, and join."""
    subjective_hits = 0
    raw = set()
    for tok in extract_tokens(visible):
        if is_subjective(tok):
            subjective_hits += 1
            continue
        raw.add(tok)
    seed_variants = 0
    for seed in seeds:
        for kw in expand_seed(seed):
            if any(is_subjective(t) for t in kw.split()):
                subjective_hits += 1
                continue
            raw.add(kw)
            seed_variants += 1
    items = sorted(raw, key=lambda s: (-len(s.split()[0]), s))
    joined = " ".join(items)
    return DedupResult(items, joined, len(joined), subjective_hits, seed_variants)


def trim_to_limit(items: list, max_chars: int) -> tuple:
    """Drop longest-tail multi-word variants first until under the cap."""
    trimmed, total = [], 0
    for kw in sorted(items, key=lambda s: (len(s), s)):
        if total + len(kw) + 1 > max_chars:
            continue
        trimmed.append(kw)
        total += len(kw) + 1
    return trimmed, total


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Dedupe Ozon backend keywords + add variants.")
    p.add_argument("--visible", help="Visible Russian title/description/bullets text")
    p.add_argument("--visible-file", help="Path to a UTF-8 file with visible copy")
    p.add_argument("--seeds", help="Comma- or newline-separated seed keywords")
    p.add_argument("--marketplace", choices=["ru", "kz", "by"], default="ru")
    p.add_argument("--max-chars", type=int, default=1000, help="Soft cap on joined length")
    p.add_argument("--json", action="store_true", help="Emit JSON only")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    visible = args.visible or ""
    if args.visible_file:
        visible += " " + Path(args.visible_file).read_text(encoding="utf-8")
    seeds = []
    if args.seeds:
        for chunk in args.seeds.replace("\n", ",").split(","):
            chunk = chunk.strip()
            if chunk:
                seeds.append(chunk)
    result = build_keywords(visible, seeds)
    if result.char_count > args.max_chars:
        trimmed, total = trim_to_limit(result.keywords, args.max_chars)
        result = DedupResult(trimmed, " ".join(trimmed), total,
                             result.dropped_subjective, result.seed_variants)
    if args.json:
        print(json.dumps({
            "keywords": result.keywords, "joined": result.joined,
            "char_count": result.char_count,
            "dropped_subjective": result.dropped_subjective,
            "seed_variants": result.seed_variants,
            "marketplace": args.marketplace,
        }, ensure_ascii=False, indent=2))
    else:
        print("Marketplace: Ozon." + args.marketplace)
        print("Unique keywords: " + str(len(result.keywords)))
        print("Char count: " + str(result.char_count))
        print("Subjective adjectives filtered: " + str(result.dropped_subjective))
        print("Seed variants generated: " + str(result.seed_variants))
        print("")
        print(result.joined)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
