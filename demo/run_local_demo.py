#!/usr/bin/env python3
"""Repository integrity checker for the Psychological Digital Twin skill pack."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DEFAULT_REPO = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "📖 Core Skill Manual / 核心技能手册": [
        "skill.md",
        "README.md",
        "METHODOLOGY.md",
    ],
    "🧩 Six Skills / 六步技能": [
        "skills/01-consciousness-replication.md",
        "skills/02-subconscious-excavation.md",
        "skills/03-archetype-switching.md",
        "skills/04-mirror-dialogue.md",
        "skills/05-spirit-memory.md",
        "skills/06-persona-iteration.md",
    ],
    "🎭 Jungian Prompts / 荣格提示词": [
        "prompts/persona.md",
        "prompts/shadow.md",
        "prompts/self.md",
        "prompts/anima-animus.md",
        "prompts/base.md",
        "prompts/jungian_assessment.md",
        "prompts/self_dialogue_rule.md",
        "prompts/subconscious_recall.md",
        "prompts/text_style_extract.md",
    ],
    "📋 Profile Templates / 画像模板": [
        "profiles/consciousness.md",
        "profiles/subconscious.md",
    ],
    "📄 Conversation Templates / 对话模板": [
        "templates/en-US/consciousness-questions.md",
        "templates/en-US/cultural-adaptation.md",
        "templates/en-US/shadow-work-guide.md",
        "templates/zh-CN/consciousness-questions.md",
        "templates/zh-CN/cultural-adaptation.md",
        "templates/zh-CN/shadow-work-guide.md",
    ],
    "⚙️ Config / 配置": [
        "config/archetype_config.json",
        "config/persona_config.json",
    ],
}


def check_file(repo: Path, relative_path: str) -> bool:
    exists = (repo / relative_path).is_file()
    status = "✅" if exists else "❌"
    print(f"  {status} {relative_path:46s} {'found' if exists else 'MISSING'}")
    return exists


def check_json(repo: Path, relative_path: str) -> bool:
    try:
        json.loads((repo / relative_path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"  ❌ {relative_path:46s} INVALID ({exc})")
        return False
    print(f"  ✅ {relative_path:46s} valid JSON")
    return True


def run_checks(repo: Path) -> bool:
    print("=" * 60)
    print("  Psychological Digital Twin · Repository Integrity Check")
    print("  精神数字分身 · 仓库完整性检查")
    print("=" * 60)

    all_passed = True
    for heading, paths in REQUIRED_FILES.items():
        print(f"\n{heading}:")
        for relative_path in paths:
            all_passed = check_file(repo, relative_path) and all_passed

    print("\n🧪 Configuration validity / 配置有效性:")
    for relative_path in ("config/archetype_config.json", "config/persona_config.json"):
        all_passed = check_json(repo, relative_path) and all_passed

    print("\n" + "=" * 60)
    if all_passed:
        print("  ✅ All required checks passed.")
        print("  ✅ 所有必需检查均已通过。")
    else:
        print("  ❌ Required checks failed. Do not treat this package as ready.")
        print("  ❌ 必需检查未通过；请勿将此技能包视为可用状态。")
    print("=" * 60)
    return all_passed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo",
        type=Path,
        default=DEFAULT_REPO,
        help="Repository root to validate (default: this repository).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return 0 if run_checks(args.repo.resolve()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
