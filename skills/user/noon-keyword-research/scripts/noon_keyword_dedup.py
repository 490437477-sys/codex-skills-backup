#!/usr/bin/env python3
"""
noon Backend Keyword Dedup Optimizer.

Take seed keywords plus visible copy, return a deduped backend search-term
string with byte utilization, tailored for noon Arabic markets. Includes
dialect hints for KSA, UAE, EG, and MSA. Strips subjective adjectives,
competitor brands, and tokens already present in the visible listing copy.

Example:
    python noon_keyword_dedup.py --visible-copy "Wireless Earbuds Bluetooth 5.3 ..." ^
        --seed "earbuds" --seed "wireless" --seed "headphones" ^
        --market .sa --dialect KSA --byte-limit 250
"""
import argparse
import json
import re
import sys
from dataclasses import dataclass


DIALECT_MAP = {
    "KSA": ["saudi", "ksa", "riyadh", "jeddah"],
    "UAE": ["emirates", "uae", "dubai", "abudhabi", "sharjah"],
    "EG": ["egypt", "cairo", "alexandria", "masr"],
    "MSA": [],
}
BRAND_BLOCKLIST = {
    "apple", "samsung", "huawei", "xiaomi", "sony", "lg", "dyson",
    "bose", "nike", "adidas", "lenovo", "hp", "dell", "asus",
    "razer", "logitech", "anker", "jbl", "philips",
}
SUBJECTIVE_ADJECTIVES = {
    "best", "cheap", "top", "amazing", "perfect", "awesome",
    "great", "quality", "premium", "luxury", "elegant", "ideal",
    "ultimate", "superb", "fancy", "brilliant", "wow", "stunning",
}
STOPWORDS = {
    "the", "and", "for", "with", "from", "this", "that", "your",
    "you", "our", "their", "are", "was", "were", "have", "has",
}
ARABIC = r"\u0600-\u06FF"


@dataclass
class DedupConfig:
    visible_copy: str
    seed_keywords: list[str]
    market: str
    dialect: str = "MSA"
    byte_limit: int = 250
    extra_brand_blocklist: list[str] | None = None


def tokenize(text: str) -> list[str]:
    cleaned = re.sub(r"[^\w\s" + ARABIC + r"-]", " ", text.lower())
    return [t for t in cleaned.split() if t]


def extract_visible_tokens(visible_copy: str) -> set[str]:
    return set(tokenize(visible_copy))


def is_blocked(token: str, extra_brands: set[str]) -> bool:
    if token in BRAND_BLOCKLIST:
        return True
    if token in extra_brands:
        return True
    if token in SUBJECTIVE_ADJECTIVES:
        return True
    if token in STOPWORDS:
        return True
    if len(token) < 2:
        return True
    if not re.match(r"^[a-z0-9" + ARABIC + r"][a-z0-9" + ARABIC + r"-]*$", token):
        return True
    return False


def dedup_keywords(cfg: DedupConfig) -> dict:
    visible = extract_visible_tokens(cfg.visible_copy)
    extra = {b.lower() for b in (cfg.extra_brand_blocklist or [])}
    pool: list[str] = []
    for kw in cfg.seed_keywords:
        pool.extend(tokenize(kw))
    pool.extend(DIALECT_MAP.get(cfg.dialect, []))
    kept: list[str] = []
    seen: set[str] = set()
    for tok in pool:
        if tok in seen:
            continue
        if tok in visible:
            continue
        if is_blocked(tok, extra):
            continue
        seen.add(tok)
        kept.append(tok)
    text = " ".join(kept)
    used = len(text.encode("utf-8"))
    truncated = text
    while used > cfg.byte_limit and truncated:
        truncated = truncated.rsplit(" ", 1)[0] if " " in truncated else ""
        used = len(truncated.encode("utf-8"))
    return {
        "market": cfg.market,
        "dialect": cfg.dialect,
        "original_token_count": len(pool),
        "kept_token_count": len(kept),
        "byte_limit": cfg.byte_limit,
        "byte_used": used,
        "utilization_pct": round(used / cfg.byte_limit * 100, 1),
        "backend_string": truncated,
    }


def from_json(payload: str) -> DedupConfig:
    return DedupConfig(**json.loads(payload))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="noon_keyword_dedup",
        description="Build a deduped backend keyword string for noon listings.",
    )
    p.add_argument("--json", help="JSON payload with DedupConfig fields")
    p.add_argument("--visible-copy", help="title+bullets+description concatenated")
    p.add_argument("--seed", action="append", default=[], help="Seed keyword (repeatable)")
    p.add_argument("--market", choices=[".sa", ".ae", ".com"], help="noon market")
    p.add_argument("--dialect", choices=list(DIALECT_MAP), default="MSA")
    p.add_argument("--byte-limit", type=int, default=250, help="Backend byte limit")
    p.add_argument("--extra-brand", action="append", default=[], help="Extra brand to block")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.json:
        cfg = from_json(args.json)
    elif args.visible_copy and args.seed and args.market:
        cfg = DedupConfig(
            visible_copy=args.visible_copy,
            seed_keywords=args.seed,
            market=args.market,
            dialect=args.dialect,
            byte_limit=args.byte_limit,
            extra_brand_blocklist=args.extra_brand,
        )
    elif not sys.stdin.isatty():
        cfg = from_json(sys.stdin.read())
    else:
        build_parser().print_help()
        return 1
    print(json.dumps(dedup_keywords(cfg), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
