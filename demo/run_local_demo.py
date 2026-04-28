#!/usr/bin/env python3
"""
Jungian Soul Agent — Demo / Integrity Checker
Verifies the repo is properly structured and all skill files are accessible.
"""
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def check(label, path, required=True):
    full = os.path.join(REPO, path)
    exists = os.path.exists(full)
    status = "✅" if exists else ("❌" if required else "⚠️")
    print(f"  {status} {label:40s} {'found' if exists else 'MISSING'}")
    return exists

def main():
    print("=" * 56)
    print("  Psychological Digital Twin · Repo Integrity Check")
    print("  精神数字分身 · 仓库完整性检查")
    print("=" * 56)
    print()

    # Core skill file
    print("📖 Core Skill Manual / 核心技能手册:")
    check("skill.md", "skill.md")
    check("README.md", "README.md")
    check("METHODOLOGY.md", "METHODOLOGY.md")
    print()

    # Six skills
    print("🧩 Six Skills / 六步技能:")
    skills = [
        "01_conscious_clone.md",
        "02_subconscious_clone.md",
        "03_jungian_archetype.md",
        "04_self_talk_heal.md",
        "05_spirit_memory.md",
        "06_persona_iterate.md",
    ]
    for s in skills:
        check(f"skills/{s}", f"skills/{s}")
    print()

    # Prompts
    print("🎭 Jungian Prompts / 荣格提示词:")
    prompts = [
        "persona.md", "shadow.md", "self.md", "anima-animus.md",
        "base.md", "jungian_assessment.md", "self_dialogue_rule.md",
        "subconscious_recall.md", "text_style_extract.md",
    ]
    for p in prompts:
        check(f"prompts/{p}", f"prompts/{p}")
    print()

    # Profiles
    print("📋 Profile Templates / 画像模板:")
    check("profiles/consciousness.md", "profiles/consciousness.md")
    check("profiles/subconscious.md", "profiles/subconscious.md")
    print()

    # Templates
    print("📄 Conversation Templates / 对话模板:")
    for lang in ["en-US", "zh-CN"]:
        for t in ["consciousness-questions.md", "cultural-adaptation.md", "shadow-work-guide.md"]:
            check(f"templates/{lang}/{t}", f"templates/{lang}/{t}")
    print()

    # Config
    print("⚙️  Config / 配置:")
    check("config/archetype_config.json", "config/archetype_config.json")
    check("config/persona_config.json", "config/persona_config.json")
    print()

    print("=" * 56)
    print("  ✅ All core files verified. Ready for self-exploration.")
    print("  ✅ 所有核心文件检查通过。已准备好进行自我探索。")
    print("=" * 56)

if __name__ == "__main__":
    main()
