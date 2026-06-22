#!/usr/bin/env python3
"""Mercado Libre backend keyword deduplicator.

Build a clean backend search-term string for Mercado Libre listings from
the visible copy (title + description + attributes) and a list of seed
keywords. The script removes duplicates, normalises Spanish/Portuguese
plurals and accents, drops competitor brand names and subjective
adjectives, then joins the survivors with commas ready to paste into
Mercado Libre Shops backend.

Usage:
    python mercado_keyword_dedup.py --market MLM ^
        --visible "Audifonos Bluetooth inalambricos con microfono" ^
        --seed "audifonos inalambricos" ^
        --seed "fone bluetooth sem fio"
"""
from __future__ import annotations

import argparse
import re
import unicodedata
from dataclasses import dataclass


STOPWORDS: set[str] = {
    "el", "la", "los", "las", "un", "una", "unos", "unas",
    "de", "del", "al", "a", "en", "por", "para", "con", "sin",
    "y", "o", "u", "que", "se", "es", "lo", "le", "su", "sus",
    "este", "esta", "estos", "estas", "ese", "esa",
    "um", "uma", "uns", "umas",
    "do", "da", "dos", "das", "no", "na", "em",
    "com", "sem", "e", "ou", "que",
}

SUBJECTIVE: set[str] = {
    "mejor", "mejores", "bueno", "buena", "buenos", "buenas",
    "increible", "perfecto", "perfecta", "top", "premium",
    "barato", "barata", "economico", "economica",
    "lindo", "linda", "bonito", "bonita", "hermoso", "hermosa",
    "otimo", "otima", "excelente", "maravilhoso", "maravilhosa",
}

COMPETITORS: set[str] = {
    "apple", "samsung", "xiaomi", "huawei", "sony", "bose",
    "jbl", "logitech", "razer", "philips", "lg",
    "mercadolibre", "mercado", "libre", "amazon",
}

LANG_MAP: dict[str, str] = {
    "MLM": "es",
    "MLC": "es",
    "MCO": "es",
    "MLA": "es",
    "MLB": "pt",
}


@dataclass
class DedupResult:
    market: str
    language: str
    cleaned: list
    original_count: int


def normalise(token: str) -> str:
    decomposed = unicodedata.normalize("NFD", token.lower())
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")


def singularise(token: str, language: str) -> str:
    if len(token) <= 3 or token.endswith("ss"):
        return token
    if language == "pt" and token.endswith("oes"):
        return token[:-3] + "ao"
    if language == "pt" and token.endswith("aes"):
        return token[:-2]
    if token.endswith("s"):
        return token[:-1]
    return token


def tokenise(text: str) -> list[str]:
    cleaned = re.sub(r"[^a-záéíóúñüâêôãõç0-9 ]+", " ", text.lower())
    return [tok for tok in cleaned.split() if tok]


def collect_visible(visible: str) -> list[str]:
    return [tok for tok in tokenise(visible) if tok not in STOPWORDS]


def collect_seeds(seeds: list[str]) -> list[str]:
    out: list[str] = []
    for raw in seeds:
        out.extend(tokenise(raw))
    return out


def filter_quality(tokens: list[str]) -> list[str]:
    out: list[str] = []
    for tok in tokens:
        if len(tok) < 3:
            continue
        if tok in SUBJECTIVE:
            continue
        if tok in COMPETITORS:
            continue
        out.append(tok)
    return out


def dedupe(tokens: list[str], language: str) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for tok in tokens:
        stem = singularise(normalise(tok), language)
        if stem in seen:
            continue
        seen.add(stem)
        out.append(stem)
    return out


def evaluate(market: str, visible: str, seeds: list[str]) -> DedupResult:
    language = LANG_MAP.get(market, "es")
    visible_tokens = collect_visible(visible)
    seed_tokens = collect_seeds(seeds)
    original_count = len(visible_tokens) + len(seed_tokens)
    filtered = filter_quality(visible_tokens + seed_tokens)
    cleaned = dedupe(filtered, language)
    return DedupResult(
        market=market,
        language=language,
        cleaned=cleaned,
        original_count=original_count,
    )


def render(result: DedupResult) -> str:
    body = ", ".join(result.cleaned)
    return (
        f"Mercado:    {result.market} (idioma: {result.language})\n"
        f"Tokens entrada: {result.original_count}\n"
        f"Tokens finales: {len(result.cleaned)}\n"
        f"Backend:    {body}"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera una cadena limpia de palabras clave backend."
    )
    parser.add_argument(
        "--market",
        choices=list(LANG_MAP.keys()),
        required=True,
        help="Mercado objetivo",
    )
    parser.add_argument(
        "--visible",
        required=True,
        help="Texto visible del listing (titulo + descripcion)",
    )
    parser.add_argument(
        "--seed",
        action="append",
        default=[],
        help="Semilla de palabras clave (se puede repetir)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = evaluate(args.market, args.visible, args.seed)
    print(render(result))


if __name__ == "__main__":
    main()
