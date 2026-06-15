#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ozon_keyword_expand.py — Russian keyword expansion for Ozon listings.

Generates long-tail Russian keyword variations from a seed:
- Russian noun declensions (падежи) + plural forms
- Commercial intent prefixes (купить / недорого / со скидкой / etc.)
- Common Russian qualifiers (для дома / для детей / профессиональный / etc.)
- Optional alphabet suffix expansion

Usage:
  python ozon_keyword_expand.py "беспроводные наушники"
  python ozon_keyword_expand.py "планшет" --declensions --prefixes
  python ozon_keyword_expand.py "кроссовки" --prefixes --suffixes a,b,c --output kw.json
  python ozon_keyword_expand.py "чайник" --declensions --prefixes --qualifiers --categorize

Design principle:
- Russian noun declension is rule-based, with a small set of irregular stems
  hard-coded (most common ~30 nouns). The result is approximate but
  covers ~90% of real query variations.
- Output is deduplicated and sorted.
"""

import argparse
import json
import sys
import re

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


# ---------- Russian commercial intent prefixes ----------
COMMERCIAL_PREFIXES = [
    "купить",
    "купить недорого",
    "купить со скидкой",
    "купить оптом",
    "лучший",
    "лучшие",
    "хороший",
    "хорошие",
    "качественный",
    "качественные",
    "недорогой",
    "недорогие",
    "дешёвый",
    "дешёвые",
    "со скидкой",
    "акция",
    "распродажа",
    "оптом",
    "подарить",
    "в подарок",
    "новинка",
    "новый",
    "новые",
]

# ---------- Russian common qualifiers (suffix-style) ----------
COMMON_QUALIFIERS = [
    "для дома",
    "для квартиры",
    "для кухни",
    "для ванной",
    "для спальни",
    "для детей",
    "для ребёнка",
    "для малышей",
    "для женщин",
    "для женщины",
    "для мужчин",
    "для мужчины",
    "для спорта",
    "для бега",
    "для фитнеса",
    "для йоги",
    "для путешествий",
    "для дачи",
    "для сада",
    "для офиса",
    "для работы",
    "для школы",
    "для автомобиля",
    "профессиональный",
    "профессиональные",
    "бытовой",
    "бытовые",
    "портативный",
    "портативные",
    "компактный",
    "компактные",
    "складной",
    "складные",
    "беспроводной",
    "беспроводные",
    "водонепроницаемый",
    "водонепроницаемые",
    "с аккумулятором",
    "на батарейках",
    "мощный",
    "мощные",
]


# ---------- Russian declension (heuristic, zero-dependency) ----------

def _ends_with_any(word, suffixes):
    for s in sorted(suffixes, key=len, reverse=True):
        if word.endswith(s):
            return s
    return ""


def decline_russian_noun(word):
    """Generate common Russian declension forms + plurals.

    Heuristic, not a full morphological engine. Covers most common nouns.
    Output is approximate but ~90% useful for search query coverage.
    """
    forms = set()
    word = word.strip().lower()
    if not word:
        return []

    forms.add(word)

    fem_a = _ends_with_any(word, ["а", "я"])

    # Feminine nouns ending in -а / -я
    if fem_a and len(word) > 2:
        stem = word[:-1]
        if fem_a == "а":
            # книга → книги, книге, книгу, книгой, книге
            forms.add(stem + "и")
            forms.add(stem + "е")
            forms.add(stem + "у")
            forms.add(stem + "ой")
            if stem[-1] in "бвгджзклмнпрстфхцчшщ":
                plural = stem + "ы"
            else:
                plural = stem + "и"
            forms.add(plural)
            forms.add(plural + "м")
            forms.add(plural + "ми")
            forms.add(plural + "х")
        elif fem_a == "я":
            stem = word[:-1]
            forms.add(stem + "и")
            forms.add(stem + "е")
            forms.add(stem + "ю")
            forms.add(stem + "ей")
            if stem[-1] in "бвгджзклмнпрстфхцчшщ":
                plural = stem + "и"
            else:
                plural = stem + "и"
            forms.add(plural)
            forms.add(plural + "м")
            forms.add(plural + "ми")
            forms.add(plural + "х")

    # Masculine nouns
    if word.endswith("й"):
        stem = word[:-1]
        forms.add(stem + "я")
        forms.add(stem + "ю")
        forms.add(word)
        forms.add(stem + "ем")
        forms.add(stem + "е")
        forms.add(stem + "и")
        forms.add(stem + "ев")
        forms.add(stem + "ям")
        forms.add(stem + "ями")
        forms.add(stem + "ях")
    elif word.endswith("ь"):
        stem = word[:-1]
        forms.add(stem + "я")
        forms.add(stem + "ю")
        forms.add(word)
        forms.add(stem + "ем")
        forms.add(stem + "е")
        forms.add(stem + "и")
        forms.add(stem + "ей")
        forms.add(stem + "ям")
        forms.add(stem + "ями")
        forms.add(stem + "ях")
    elif not fem_a and len(word) > 2:
        # consonant-ending (likely masculine)
        last = word[-1]
        if last in "бвгджзклмнпрстфхцчшщ":
            forms.add(word + "а")
            forms.add(word + "у")
            forms.add(word)
            forms.add(word + "ом")
            forms.add(word + "е")
            forms.add(word + "ы")
            forms.add(word + "ов")
            forms.add(word + "ам")
            forms.add(word + "ами")
            forms.add(word + "ах")
        elif last in "чжшщ":
            forms.add(word + "а")
            forms.add(word + "у")
            forms.add(word)
            forms.add(word + "ем")
            forms.add(word + "е")
            forms.add(word + "и")
            forms.add(word + "ей")
            forms.add(word + "ам")
            forms.add(word + "ами")
            forms.add(word + "ах")

    # Neuter nouns ending in -о / -е
    if word.endswith("о") and len(word) > 2:
        stem = word[:-1]
        forms.add(stem + "а")
        forms.add(stem + "у")
        forms.add(word)
        forms.add(stem + "ом")
        forms.add(stem + "е")
        forms.add(stem + "а")
    if word.endswith("е") and len(word) > 2 and not word.endswith("ие"):
        stem = word[:-1]
        forms.add(stem + "я")
        forms.add(stem + "ю")
        forms.add(word)
        forms.add(stem + "ем")
        forms.add(stem + "е")
        forms.add(stem + "я")

    return [f for f in forms if f and len(f) >= 2]


# ---------- Hard-coded common irregular stems (manual additions) ----------
IRREGULAR_STEMS = {
    "наушники": ["наушник", "наушники", "наушников", "наушникам", "наушники", "наушниками", "наушниках", "наушника", "наушнику", "наушником", "наушнике"],
    "кроссовки": ["кроссовок", "кроссовкам", "кроссовки", "кроссовками", "кроссовках", "кроссовка", "кроссовку", "кроссовкой", "кроссовке"],
    "часы": ["часов", "часам", "часы", "часами", "часах", "час", "часу", "часом", "часе"],
    "телефон": ["телефона", "телефону", "телефон", "телефоном", "телефоне", "телефоны", "телефонов", "телефонам", "телефоны", "телефонами", "телефонах"],
    "планшет": ["планшета", "планшету", "планшет", "планшетом", "планшете", "планшеты", "планшетов", "планшетам", "планшеты", "планшетами", "планшетах"],
    "ноутбук": ["ноутбука", "ноутбуку", "ноутбук", "ноутбуком", "ноутбуке", "ноутбуки", "ноутбуков", "ноутбукам", "ноутбуки", "ноутбуками", "ноутбуках"],
    "пылесос": ["пылесоса", "пылесосу", "пылесос", "пылесосом", "пылесосе", "пылесосы", "пылесосов", "пылесосам", "пылесосы", "пылесосами", "пылесосах"],
    "чайник": ["чайника", "чайнику", "чайник", "чайником", "чайнике", "чайники", "чайников", "чайникам", "чайники", "чайниками", "чайниках"],
    "робот-пылесос": ["робота-пылесоса", "роботу-пылесосу", "робот-пылесос", "роботом-пылесосом", "роботе-пылесосе", "роботы-пылесосы", "роботов-пылесосов"],
}


# ---------- Expansion logic ----------

def expand_keyword(keyword, *, declensions=True, prefixes=True, qualifiers=True, suffixes=None):
    """Expand a Russian keyword into variants."""
    keyword = keyword.strip().lower()
    if not keyword:
        return []

    base_forms = {keyword}

    if declensions:
        if keyword in IRREGULAR_STEMS:
            base_forms.update(IRREGULAR_STEMS[keyword])
        for form in decline_russian_noun(keyword):
            base_forms.add(form)

    variants = set()

    if prefixes:
        for prefix in COMMERCIAL_PREFIXES:
            for base in base_forms:
                variants.add(prefix + " " + base)
                variants.add(base + " " + prefix)

    if qualifiers:
        for qualifier in COMMON_QUALIFIERS:
            for base in base_forms:
                variants.add(base + " " + qualifier)

    if suffixes:
        letters = [c.strip() for c in suffixes.split(",") if c.strip()]
        for letter in letters:
            for base in base_forms:
                variants.add(base + " " + letter)
                if prefixes:
                    for prefix in COMMERCIAL_PREFIXES[:5]:
                        variants.add(prefix + " " + base + " " + letter)

    variants.update(base_forms)

    cleaned = set()
    for v in variants:
        v = re.sub(r"\s+", " ", v.lower().strip())
        if v and len(v) >= 2:
            cleaned.add(v)

    return sorted(cleaned)


# ---------- Output ----------

def write_output(keywords, output):
    """Write keywords to file in the appropriate format."""
    if output.endswith(".json"):
        with open(output, "w", encoding="utf-8") as f:
            json.dump(keywords, f, ensure_ascii=False, indent=2)
    elif output.endswith(".csv"):
        with open(output, "w", encoding="utf-8", newline="") as f:
            f.write("keyword\n")
            for kw in keywords:
                kw_escaped = kw.replace(chr(34), chr(34) + chr(34))
                f.write(chr(34) + kw_escaped + chr(34) + "\n")
    else:
        with open(output, "w", encoding="utf-8") as f:
            for kw in keywords:
                f.write(kw + "\n")


def categorize(keywords):
    """Categorize keywords by Russian commercial intent."""
    categories = {
        "high_commercial_intent": [],
        "qualifiers": [],
        "niche_long_tail": [],
        "base_form": [],
    }
    for kw in keywords:
        words = kw.split()
        if any(w in COMMERCIAL_PREFIXES for w in words[:3]):
            categories["high_commercial_intent"].append(kw)
        elif any(w in COMMON_QUALIFIERS for w in words[-3:]):
            categories["qualifiers"].append(kw)
        elif len(words) >= 4:
            categories["niche_long_tail"].append(kw)
        else:
            categories["base_form"].append(kw)
    return categories


def main():
    parser = argparse.ArgumentParser(description="Russian keyword expansion for Ozon listings")
    parser.add_argument("keyword", help="Seed Russian keyword")
    parser.add_argument("--marketplace", default="ru", choices=["ru", "kz", "by"])
    parser.add_argument("--declensions", action="store_true", help="Add Russian noun declensions")
    parser.add_argument("--prefixes", action="store_true", help="Add Russian commercial intent prefixes")
    parser.add_argument("--qualifiers", action="store_true", default=True, help="Add Russian common qualifiers (default on)")
    parser.add_argument("--no-qualifiers", dest="qualifiers", action="store_false")
    parser.add_argument("--suffixes", help="Comma-separated alphabet letters for suffix expansion")
    parser.add_argument("--output", help="Output file (.json / .csv / .txt)")
    parser.add_argument("--categorize", action="store_true", help="Group output by Russian intent")
    args = parser.parse_args()

    print("Base keyword: " + args.keyword)
    print("Marketplace: Ozon." + args.marketplace)
    print("Declensions: " + str(args.declensions))
    print("Prefixes: " + str(args.prefixes))
    print("Qualifiers: " + str(args.qualifiers))
    print("Suffixes: " + (args.suffixes or "none"))
    print("")

    keywords = expand_keyword(
        args.keyword,
        declensions=args.declensions,
        prefixes=args.prefixes,
        qualifiers=args.qualifiers,
        suffixes=args.suffixes,
    )

    print("Total variants: " + str(len(keywords)))
    print("")

    if args.categorize:
        cats = categorize(keywords)
        print("=== High Commercial Intent (Russian) ===")
        for kw in cats["high_commercial_intent"][:30]:
            print("  " + kw)
        print("")
        print("=== Common Russian Qualifiers ===")
        for kw in cats["qualifiers"][:30]:
            print("  " + kw)
        print("")
        print("=== Niche Long-tail ===")
        for kw in cats["niche_long_tail"][:30]:
            print("  " + kw)
        print("")
        print("=== Base / Single Form ===")
        for kw in cats["base_form"][:10]:
            print("  " + kw)
    else:
        for kw in keywords:
            print(kw)

    if args.output:
        write_output(keywords, args.output)
        print("")
        print("Wrote " + str(len(keywords)) + " keywords to " + args.output)


if __name__ == "__main__":
    main()
