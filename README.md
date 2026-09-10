# 🜃 Psychological Digital Twin · 精神数字分身

> **Build a mirror you can question.**
>
> *An AI agent skill pack for consent-based self-reflection, informed by Jungian analytical psychology.*
>
> *用 AI 建造一面可质疑、可修正的镜子——以荣格分析心理学为参考的、自主可控的自我反思框架。*

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
│                │ Reflection Memory ─► Self- │
│                │ (opt-in)        Reflection │
│                │                  (requested)│
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
| 5 | **Reflection Memory** · 反思记忆 | explicit save request / explicit save preference | user-controlled | Reviewable, consented memory draft |
| 6 | **Self-Reflection Iteration** · 自我认知迭代 | "生成报告" / "report" | cumulative | User-correctable reflection report |

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
├── skill.md                  # 📖 Core skill manual (v4.0)
│                             #   Everything you need to run the 6 skills
│
├── METHODOLOGY.md            # 📘 Philosophical & theoretical foundation
│
├── skills/                   # 🧩 Six detailed skill files (EN/ZH)
│   ├── 01-consciousness-replication.md  #   Conscious portrait
│   ├── 02-subconscious-excavation.md    #   Complex map & core cycle
│   ├── 03-archetype-switching.md        #   Multi-perspective reflection
│   ├── 04-mirror-dialogue.md            #   Deep self-confrontation
│   ├── 05-spirit-memory.md              #   Belief & emotion delta
│   └── 06-persona-iteration.md          #   Iteration report
│
├── profiles/                 # 📋 Your personal portraits (start empty)
│   ├── consciousness.md      #   Conscious ego characteristics
│   ├── subconscious.md       #   Unconscious patterns & complexes
│   ├── example-consciousness.md  #   Fill-in example template
│   └── example-subconscious.md   #   Fill-in example template
│
├── prompts/                  # 🎭 9 archetype & system prompts
│   ├── persona.md            #   Persona (social mask)
│   ├── shadow.md             #   Shadow (repressed self)
│   ├── self.md               #   Self (integrated whole)
│   ├── anima-animus.md       #   Anima/Animus (inner opposite)
│   ├── base.md               #   System prompt (always-on)
│   ├── self_dialogue_rule.md #   Mirror dialogue constraints
│   ├── jungian_assessment.md #   Structured assessment template
│   ├── subconscious_recall.md #   Unconscious pattern recall
│   └── text_style_extract.md #   Writing-style extraction
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
├── demo/                     # 🎬 Repo integrity checker (no dependencies)
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

## Local Runtime (V5 Baseline)

This repository now includes a small local consent-first state layer in [`core/runtime.py`](core/runtime.py). It is intentionally model-agnostic: Hermes, a local LLM, or any hosted LLM adapter may call it, but the runtime itself does not send content anywhere.

- A proposed memory record is a **draft**, not a write.
- Only an explicit `confirm_memory()` action persists it.
- Confirmed records are isolated at `data_root/users/<user-id>/memories/`.
- Users can delete records; iteration reports consume confirmed records only.
- A conservative safety gate blocks deep exploration and memory when high-risk phrases are detected. It is an interruption mechanism, **not** a clinical assessment.

Read the integration contract: [`docs/v5-runtime-architecture.md`](docs/v5-runtime-architecture.md).

---

## Privacy, Safety & Ethics

- **🔐 No silent storage.** The default is not to save personal material. Before any profile, summary, quotation, hypothesis, or retrieval index is written, the user reviews the proposed entry and explicitly chooses whether to save it.
- **🗂️ Keep real data outside the repository.** Runtime-generated user data belongs in a per-user storage directory that is ignored by Git. The `profiles/` directory in this repository contains templates only.
- **☁️ Be honest about model transmission.** A local file is not the same as a local AI. If a cloud LLM is used, conversation content may be sent to that provider; implementations must disclose this before deep exploration or saving is enabled.
- **🚫 Not therapy.** This is a self-reflection tool. It does not diagnose, treat, assess risk, or replace professional mental-health services.
- **🛑 Safety overrides role-play.** For immediate safety risk, severe dissociation, flashbacks, or reality-confusion signals, stop deep reflection and follow the Safety Stop Protocol.
- **🧭 The user remains author.** Skip, pause, correct, export, delete, or reject any reflection at any time. Hypotheses must be labeled with evidence and uncertainty, never presented as hidden truth.

Read the mandatory implementation rules: [`SAFETY_AND_DATA_GOVERNANCE.md`](SAFETY_AND_DATA_GOVERNANCE.md).

---

## License

[MIT](LICENSE) — Free to use, modify, and redistribute. Attribution appreciated but not required.

---

*"Knowing yourself is the beginning of all wisdom." — Aristotle*  
*"认识你自己"是一切智慧的起点。— 亚里士多德*

**Version 4.0** · Built through iterative self-exploration with AI · 2026
