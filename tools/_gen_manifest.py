"""Regenerate MANIFEST.md for the Codex skills backup.

Walks skills/system, skills/user, and plugins/skills and emits a markdown
manifest with each skill's `description` field from its `SKILL.md`
front-matter. Designed to be invoked from scripts/backup.ps1 via:

    python tools/_gen_manifest.py
"""

from __future__ import annotations

import datetime as _dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "MANIFEST.md"
SYSTEM_DIR = ROOT / "skills" / "system"
USER_DIR = ROOT / "skills" / "user"
PLUGIN_DIR = ROOT / "plugins" / "skills"

DESC_LIMIT = 120  # truncate long descriptions for the table


def _find_skill_md(skill_root: Path) -> Path | None:
    """Return the SKILL.md path for a skill folder, allowing one nested level."""
    direct = skill_root / "SKILL.md"
    if direct.is_file():
        return direct
    nested = skill_root / skill_root.name / "SKILL.md"
    if nested.is_file():
        return nested
    for child in skill_root.iterdir():
        if child.is_dir():
            candidate = child / "SKILL.md"
            if candidate.is_file():
                return candidate
    return None


_FRONT_RE = re.compile(r"^---\s*\n(.*?)\n---", re.S)


def _extract_description(skill_md: Path) -> str:
    try:
        text = skill_md.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    m = _FRONT_RE.match(text)
    if not m:
        return ""
    front = m.group(1)
    lines = front.splitlines()
    desc_lines: list[str] = []
    capturing = False
    for line in lines:
        if not capturing:
            if line.lstrip().startswith("description:"):
                value = line.split("description:", 1)[1].strip()
                if value:
                    desc_lines.append(value)
                capturing = True
            continue
        # capturing == True: stop when a new top-level YAML key appears
        if re.match(r"^[A-Za-z_][\w-]*\s*:", line):
            break
        if line.strip() == "":
            break
        desc_lines.append(line.strip())
    desc = " ".join(desc_lines).strip()
    if desc.startswith(('"', "'")) and desc.endswith(desc[0]) and len(desc) >= 2:
        desc = desc[1:-1].strip()
    desc = desc.replace("|", "\\|").replace("\n", " ")
    return desc


def _truncate(text: str, limit: int = DESC_LIMIT) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def _list_skills(parent: Path) -> list[tuple[str, str]]:
    if not parent.is_dir():
        return []
    rows: list[tuple[str, str]] = []
    for entry in sorted(parent.iterdir(), key=lambda p: p.name.lower()):
        if not entry.is_dir():
            continue
        if entry.name.startswith(".") or entry.name in {"__pycache__"}:
            continue
        skill_md = _find_skill_md(entry)
        desc = _extract_description(skill_md) if skill_md else ""
        rows.append((entry.name, _truncate(desc)))
    return rows


def _list_plugin_skills(parent: Path) -> list[tuple[str, str, str]]:
    if not parent.is_dir():
        return []
    rows: list[tuple[str, str, str]] = []
    for plugin in sorted(parent.iterdir(), key=lambda p: p.name.lower()):
        if not plugin.is_dir() or plugin.name.startswith("."):
            continue
        for skill in sorted(plugin.iterdir(), key=lambda p: p.name.lower()):
            if not skill.is_dir() or skill.name.startswith("."):
                continue
            skill_md = skill / "SKILL.md"
            if not skill_md.is_file():
                # tolerate one extra nesting level
                inner = _find_skill_md(skill)
                if inner is None:
                    continue
                skill_md = inner
            label = f"{plugin.name}:{skill.name}"
            rel = skill_md.relative_to(ROOT).as_posix()
            desc = _extract_description(skill_md)
            rows.append((label, rel, _truncate(desc, 200)))
    return rows


def main() -> None:
    system = _list_skills(SYSTEM_DIR)
    user = _list_skills(USER_DIR)
    plugin = _list_plugin_skills(PLUGIN_DIR)
    total = len(system) + len(user) + len(plugin)

    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines: list[str] = []
    lines.append("# Skills 清单")
    lines.append("")
    lines.append(f"> 备份时间：{now}")
    lines.append(
        "> 来源：$env:USERPROFILE\\.codex\\skills 与 "
        "$env:USERPROFILE\\.codex\\plugins\\cache\\openai-bundled\\*\\skills"
    )
    lines.append("")
    lines.append(f"## 内置 Skills（skills/system/，{len(system)} 项）")
    lines.append("")
    lines.append("| Skill | 用途 |")
    lines.append("|-------|------|")
    for name, desc in system:
        lines.append(f"| {name} | {desc} |")
    lines.append("")
    lines.append(f"## 用户 Skills（skills/user/，{len(user)} 项）")
    lines.append("")
    lines.append("| Skill | 用途 |")
    lines.append("|-------|------|")
    for name, desc in user:
        lines.append(f"| {name} | {desc} |")
    lines.append("")
    lines.append(f"## 插件贡献 Skills（plugins/skills/，{len(plugin)} 项）")
    lines.append("")
    lines.append("| Skill 标识 | 路径 | 用途 |")
    lines.append("|-----------|------|------|")
    for label, path, desc in plugin:
        lines.append(f"| {label} | {path} | {desc} |")
    lines.append("")
    lines.append("## 总计")
    lines.append("")
    lines.append(f"- 内置 skills：{len(system)}")
    lines.append(f"- 用户 skills：{len(user)}")
    lines.append(f"- 插件 skills：{len(plugin)}")
    lines.append(f"- 合计：{total}")
    lines.append("")

    MANIFEST.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {MANIFEST.relative_to(ROOT)}: {total} skills "
          f"(system={len(system)}, user={len(user)}, plugin={len(plugin)})")


if __name__ == "__main__":
    main()
