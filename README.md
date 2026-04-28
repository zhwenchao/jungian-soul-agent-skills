# 🜃 Psychological Digital Twin · 精神数字分身

> **Build a mirror that never lies.**  
> *An AI agent skill pack for genuine self-knowledge, based on Jungian analytical psychology.*  
> *用AI建造"不说谎的镜子"——基于荣格分析心理学的深度自我认知框架。*

[![Version](https://img.shields.io/badge/version-4.0-blueviolet?style=flat-square)]()
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)]()
[![Theory](https://img.shields.io/badge/theory-Jungian_analytical_psychology-ff6b35?style=flat-square)]()
[![Languages](https://img.shields.io/badge/lang-zh--CN_%7C_en--US-important?style=flat-square)]()

---

## What Is This?

A **drop-in skill pack** for any LLM (ChatGPT, Claude, DeepSeek, Hermes Agent, etc.) that transforms it into a `psychological digital twin` — a non-judgmental mirror that helps you see what you normally cannot see about yourself.

This is NOT a closed product or app. It is **an open, portable methodology** — copy the files, tell your AI to load them, and start the conversation.

### The Six Skills Pipeline

```
┌──────────────────────────────────────────────────────────────────┐
│                     Six Skills Pipeline                          │
│                                                                  │
│  INPUT │ Step 1   │ Step 2       │ Step 3       │ Step 4     │
│  (chat │ Conscious │ Subconscious │ Archetype   │ Mirror      │
│   /text)──►Replication──►Excavation──►Switching──►Dialogue─────►
│         │ 10-30min │ 25-40min    │ on-demand   │ 30min       │
│                                                                  │
│         └────────────────────────────────────────────────────────┘
│                                     │
│                                     ▼
│                ┌──────────────────────────┐
│                │ Step 5           Step 6  │
│                │ Spirit Memory ───►Persona │
│                │ (auto)         Iteration  │
│                │                (triggered)│
│                └──────────────────────────┘
│                                     │
│                                     ▼
│                         PROFILE UPDATES (回写画像)
└──────────────────────────────────────────────────────────────────┘
```

| # | Skill | Trigger | Duration | Output |
|---|-------|---------|----------|--------|
| 1 | **Consciousness Replication** · 表层意识复刻 | "意识复刻" / "who am I" | 10-30 min | Consciousness portrait |
| 2 | **Subconscious Excavation** · 潜意识挖掘 | "潜意识" / "subconscious" | 25-40 min | Complex map + core cycle |
| 3 | **Archetype Switching** · 原型切换 | "阴影" / "shadow" / "persona" | on-demand | Multi-perspective reflection |
| 4 | **Mirror Dialogue** · 镜像对话 | "和自己对话" / "mirror" | 30 min | Deep self-confrontation |
| 5 | **Spirit Memory** · 记忆沉淀 | auto (end of session) | auto | Belief + emotion delta |
| 6 | **Persona Iteration** · 人格迭代 | "生成报告" / "report" | cumulative | Iteration report |

---

## Core Manifesto

> **It can get closer to you, become you — but it can never replace you.**
>
> It can assist your decisions, act as your high-fidelity proxy in the digital world —
> but the final decision is always yours.
>
> Its value lies not in being correct, but in reflecting.
> Its goal is not to think for you, but to help you see how you think.
>
> *This is the boundary between you and your digital twin.*

---

## Quick Start

### English

```
1. Clone this repo or download the files
2. Tell your AI: "Load the skill pack from skill.md"
   (for ChatGPT/Claude: paste skill.md content into a custom instruction)
3. Start with: "I'd like to understand myself better"
4. Follow the 6-step pipeline
```

### 中文

```
1. 下载本仓库所有文件
2. 告诉你的AI：「加载 skill.md 中的技能包」
   （ChatGPT/Claude 用户：将 skill.md 内容粘贴到自定义指令中）
3. 以「我想更了解自己」开始对话
4. 按六步流程推进
```

---

## Dual-Mode Architecture

The skill pack operates in **two modes** — choose based on your use case:

| Dimension | Personal Mode | Universal Mode |
|-----------|--------------|----------------|
| **Target** | Your own deep self-exploration | Learning, adapting, or redistributing the framework |
| **Data** | Stored in `profiles/<you>/` (local only) | Template files only — no user data |
| **Content** | Filled with your personal portrait | Empty templates ready for any user |
| **Platform** | Works with any LLM | Methodology-only, zero platform lock-in |
| **Privacy** | 🔒 Everything stays on your machine | No data generated in this mode |

**Progression phases** (Individuation path):

```
Phase 1 ──► Phase 2 ──► Phase 3 ──► Phase 4 ──► Phase 5 ──► Phase 6
Conscious  Subconscious Shadow      Mirror     Self        Digital
Clone      Excavation   Integration Dialogue   Integration Twin
(40-60%)   (60-75%)     (75-85%)    (85-90%)   (90-95%)    (95%+)
```

---

## File Structure

```
psychological-digital-twin/
│
├── skill.md                  # 📖 Core skill manual (v4.0, 18KB)
│                             #   Everything you need to run the 6 skills
│
├── METHODOLOGY.md            # 📘 Philosophical & theoretical foundation
│
├── profiles/                 # 📋 Your personal portraits (start empty)
│   ├── consciousness.md      #   Conscious ego characteristics
│   └── subconscious.md       #   Unconscious patterns & complexes
│
├── prompts/                  # 🎭 7 Jungian archetype prompts
│   ├── persona.md            #   Persona (social mask)
│   ├── shadow.md             #   Shadow (repressed self)
│   ├── self.md               #   Self (integrated whole)
│   ├── anima-animus.md       #   Anima/Animus (inner opposite)
│   ├── base.md               #   System prompt (always-on)
│   ├── self_dialogue_rule.md #   Mirror dialogue constraints
│   └── jungian_assessment.md #   Structured assessment template
│
├── templates/                 # 📄 Bilingual conversation templates
│   ├── zh-CN/                #   中文模板 (consciousness, shadow work, cultural adaptation)
│   └── en-US/                #   English templates (same 3 categories)
│
├── config/                   # ⚙️ Archetype & persona JSON configs
│
├── docs/                     # 📚 Supplementary documentation
│
├── flowchart/                # 🔄 Mermaid process diagrams
│
├── demo/                     # 🎬 Python demo (requires chromadb + openai)
│
└── requirements.txt          # 🐍 Python dependencies (optional)
```

---

## Dialogue Depth Levels

Each mirror dialogue session progresses through 5 depth levels — a structured ladder for genuine self-discovery:

| Level | Layer | What You Explore |
|-------|-------|-----------------|
| **L1** | Behavior | What you did, how you acted |
| **L2** | Values | Why you did it, what matters to you |
| **L3** | Complex | What drives this pattern |
| **L4** | Existential | Who am I? What is life about? |
| **L5** | Self/Integration | How do all sides coexist? |

---

## Theoretical Foundation

This skill pack is built on a **multi-engine theoretical framework**:

```
Primary Engine ───── Jungian Analytical Psychology
                      └── 3-layer psyche: Ego → Individual Unconscious → Collective Unconscious
                      └── 4 archetypes: Persona · Shadow · Anima/Animus · Self
                      └── Individuation: the lifelong process of becoming whole

Secondary Engines ── Existential Philosophy (Camus, Nietzsche)
                      └── Meaning is created, not discovered
                    └── Social Role Theory
                      └── Identity as enacted performance
                    └── Eastern Philosophy (reference)
                      └── Non-duality · Wu-wei · Beginner's mind
```

### Core Formula

```
self-awareness = dialogue_depth × framework_quality × user_openness
```

---

## Privacy & Ethics

- **🔒 All data stays local.** Profiles are plain-text files on your machine. Nothing is uploaded.
- **🚫 Not therapy.** This is a self-exploration tool. It does not diagnose, treat, or replace professional mental health services.
- **🧭 You are in control.** Skip any question, delete your profile at any time. The mirror serves you, not the other way around.
- **⚠️ Confidence labeling:** All subconscious findings are tagged 🟢 high / 🟡 medium / 🔴 low confidence. Nothing is presented as absolute truth.

---

## License

[MIT](LICENSE) — Free to use, modify, and redistribute. Attribution appreciated but not required.

---

*"Knowing yourself is the beginning of all wisdom." — Aristotle*  
*"认识你自己"是一切智慧的起点。— 亚里士多德*

**Version 4.0** · Built through iterative self-exploration with AI · 2026
