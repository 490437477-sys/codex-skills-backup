#!/usr/bin/env python3
"""TEMU Backend Keyword Deduper.

Build a deduped, multilingual backend keyword set for TEMU listings from
a visible copy and a seed keyword list. Expands seeds across en/de/fr/es/
pt/it/ja/ko, removes duplicates after normalization, strips TEMU banned
words, and respects the 250-byte backend limit.

Usage:
    python temu_keyword_dedup.py --copy "phone stand holder" \\
        --seeds "phone holder,desk stand" --limit 250
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass, field

LANG_SYNONYMS = {
    "en": {"phone": "phone", "stand": "stand", "holder": "holder",
           "desk": "desk", "cable": "cable", "case": "case",
           "light": "light", "bag": "bag", "kitchen": "kitchen"},
    "de": {"phone": "telefon", "stand": "ständer", "holder": "halter",
           "desk": "schreibtisch", "cable": "kabel", "case": "hülle",
           "light": "licht", "bag": "tasche", "kitchen": "küche"},
    "fr": {"phone": "téléphone", "stand": "support", "holder": "support",
           "desk": "bureau", "cable": "câble", "case": "coque",
           "light": "lumière", "bag": "sac", "kitchen": "cuisine"},
    "es": {"phone": "teléfono", "stand": "soporte", "holder": "soporte",
           "desk": "escritorio", "cable": "cable", "case": "funda",
           "light": "luz", "bag": "bolsa", "kitchen": "cocina"},
    "pt": {"phone": "telefone", "stand": "suporte", "holder": "suporte",
           "desk": "escritório", "cable": "cabo", "case": "capa",
           "light": "luz", "bag": "bolsa", "kitchen": "cozinha"},
    "it": {"phone": "telefono", "stand": "supporto", "holder": "supporto",
           "desk": "scrivania", "cable": "cavo", "case": "custodia",
           "light": "luce", "bag": "borsa", "kitchen": "cucina"},
    "ja": {"phone": "スマホ", "stand": "スタンド", "holder": "ホルダー",
           "desk": "デスク", "cable": "ケーブル", "case": "ケース",
           "light": "ライト", "bag": "バッグ", "kitchen": "キッチン"},
    "ko": {"phone": "휴대폰", "stand": "스탠드", "holder": "거치대",
           "desk": "책상", "cable": "케이블", "case": "케이스",
           "light": "조명", "bag": "가방", "kitchen": "주방"},
}

BANNED_WORDS = {
    "best", "cheapest", "free", "guaranteed", "miracle",
    "cure", "fda", "medical", "luxury", "authentic",
    "official", "100%", "#1", "sale", "promo",
}


@dataclass
class KeywordSet:
    keywords: list = field(default_factory=list)
    bytes_used: int = 0
    dropped: list = field(default_factory=list)


def normalize(text: str) -> str:
    folded = unicodedata.normalize("NFKD", text.lower())
    folded = "".join(c for c in folded if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9\s]", " ", folded).strip()


def expand_seed(seed: str) -> dict:
    base = normalize(seed)
    out = {"en": base}
    for lang, table in LANG_SYNONYMS.items():
        words = base.split()
        translated = [table.get(w, w) for w in words]
        out[lang] = " ".join(translated)
    return out


def is_banned(token: str) -> bool:
    return any(b in token.lower() for b in BANNED_WORDS)


def build(copies: list, seeds: list, limit: int) -> KeywordSet:
    bag: dict = {}
    for raw in copies + seeds:
        if not raw:
            continue
        for lang, term in expand_seed(raw).items():
            cleaned = re.sub(r"\s+", " ", term).strip()
            if len(cleaned) < 2 or is_banned(cleaned):
                continue
            bag.setdefault(cleaned, set()).add(lang)

    sorted_terms = sorted(bag.keys(), key=lambda x: (-len(x.split()), x))
    result = KeywordSet()
    used = set()
    for term in sorted_terms:
        key = normalize(term)
        if key in used:
            continue
        used.add(key)
        cost = len(term.encode("utf-8")) + (1 if result.keywords else 0)
        if result.bytes_used + cost > limit:
            result.dropped.append(term)
            continue
        result.keywords.append(term)
        result.bytes_used += cost
    return result


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="TEMU backend keyword deduper")
    p.add_argument("--copy", action="append", default=[],
                   help="visible copy strings (repeatable)")
    p.add_argument("--seeds", default="",
                   help="comma separated seed keywords")
    p.add_argument("--limit", type=int, default=250)
    return p.parse_args()


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    args = parse_args()
    seed_list = [s.strip() for s in args.seeds.split(",") if s.strip()]
    result = build(args.copy, seed_list, args.limit)
    print(f"Generated {len(result.keywords)} keywords "
          f"({result.bytes_used}/{args.limit} bytes)")
    for kw in result.keywords:
        print(f"  {kw}")
    if result.dropped:
        print(f"Dropped ({len(result.dropped)}): {result.dropped[:5]}...")


if __name__ == "__main__":
    main()
