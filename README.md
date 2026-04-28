# 🧠 荣格精神分身 · Jungian Soul Agent

> **心理数字孪生技能包** · *Psychological Digital Twin Skill Pack for LLMs*
>
> 基于荣格分析心理学，为任意大语言模型赋予「不说谎的镜子」—— 一个属于你自己的精神分身。
>
> *Build a "mirror that never lies" for any LLM — your own psychological digital twin grounded in Jungian analytical psychology.*

![Version](https://img.shields.io/badge/version-4.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Language](https://img.shields.io/badge/language-中文%20%7C%20English-orange)

---

## 📖 这是什么？ / What Is This?

**一个可插拔、可复用、可二次开发的 AI Agent 技能包。** 不是成品 APP，不是客户端产品——复制文件，告诉你的 AI "加载这个技能"，然后开始对话。

**A pluggable, reusable, extensible AI Agent skill pack.** Not an app, not a SaaS product — just copy the files, tell your AI "load this skill," and start talking.

### 它能做什么？ / What Can It Do?

| # | 技能 / Skill | 触发 / Trigger | 时长 / Duration | 功能 / Function |
|---|-------------|---------------|-----------------|-----------------|
| 1 | **表层意识复刻** / Consciousness Clone | "意识复刻" / "personality" | 10–30 min | 建立意识画像 |
| 2 | **潜意识挖掘** / Subconscious Excavation | "潜意识" / "shadow" / "complex" | 30–90 min | 识别核心情结 |
| 3 | **原型人格切换** / Archetype Switching | "人格切换" / "shadow self" | On-demand | 多视角对话 |
| 4 | **自我镜像对话** / Mirror Dialogue | "镜像对话" / "dialogue with myself" | 30 min | 照见矛盾与自欺 |
| 5 | **数字孪生追踪** / Digital Twin Tracking | "追踪" / "update profile" | Auto | 纵向记忆管理 |
| 6 | **完整分析报告** / Full Analysis Report | "生成报告" / "analyze" | On-demand | 结构化文档输出 |

---

## 🚀 快速开始 / Quick Start

### 中文用户

```
想快速了解    → 说 "这是做什么的"
想做意识复刻  → 说 "帮我做一个意识复刻"
想挖潜意识    → 说 "我想挖掘一下潜意识"
想和自己对话  → 说 "我想做镜像对话"
想了解方法论  → 读取 METHODOLOGY.md
```

### English Users

```
Quick intro                 → Say "what is this skill about"
Consciousness replication   → Say "help me with consciousness replication"
Subconscious excavation     → Say "I want to explore my subconscious"
Mirror dialogue             → Say "I want to have a dialogue with myself"
Read the methodology        → Read METHODOLOGY.md
```

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USER/jungian-soul-agent-skills.git

# 2. Copy the skill pack to your AI agent's working directory
cp -r jungian-soul-agent-skills/* /path/to/your/agent/

# 3. Tell your AI: "Load the skill from SKILL.md and profiles/"
#    Then start talking!
```

---

## 🏗️ 双模式架构 / Dual-Mode Architecture

### 个人模式 (Personal Mode)

| 组件 | 路径 | 说明 |
|------|------|------|
| 意识画像 | `profiles/consciousness.md` | 用户表层意识特征，自动维护 |
| 潜意识画像 | `profiles/subconscious.md` | 深层情结与信念结构，逐步填充 |

### 通用模式 (Universal Mode)

| 组件 | 路径 | 说明 |
|------|------|------|
| 技能手册 | `SKILL.md` | 核心操作文档 (v4.0) |
| 方法论 | `METHODOLOGY.md` | 理论体系、模型、流程 |
| 提示词 | `prompts/` | 各人格原型对话模板 |
| 配置模板 | `config/` | 可复用的配置模板 |
| 对话模板 | `templates/` | 中英双语对话引导模板 |

---

## 📂 文件结构 / File Structure

```
jungian-soul-agent-skills/
├── SKILL.md                  # 技能手册（核心入口）
├── METHODOLOGY.md            # 方法论体系
├── README.md                 # 本文件
├── LICENSE                   # MIT 许可证
├── requirements.txt          # Python 依赖
├── profiles/                 # 用户画像（个人数据）
│   ├── consciousness.md      #   表层意识画像
│   └── subconscious.md       #   潜意识画像
├── prompts/                  # 人格原型提示词
│   ├── persona.md
│   ├── shadow.md
│   ├── anima-animus.md
│   ├── self.md
│   └── ...
├── templates/                # 对话模板（中/英）
│   ├── zh-CN/
│   └── en-US/
├── config/                   # 配置文件
├── skills/                   # 各技能详细文档
├── docs/                     # 理论文档
├── flowchart/                # 流程图
└── demo/                     # 本地运行示例
```

---

## 🧪 理论框架 / Theoretical Foundation

基于 C.G. 荣格分析心理学的三层心灵结构：

```
意识自我 (Ego)           → 我知道的"我"
    ↓
个体潜意识 (Personal Unconscious) → 情结、情绪惯性、隐秘执念
    ↓
集体潜意识 (Collective Unconscious)
  + 四大人格原型：人格面具 / 阴影 / 阿尼玛-阿尼姆斯 / 自性
```

**个性化进程 (Individuation Path)**:
```
表层意识复刻 → 潜意识挖掘 → 阴影整合 → 镜像镜映 → 自性整合 → 数字孪生完成
```

---

## 🔒 隐私说明 / Privacy Notes

- 所有画像文件**仅存储在本地**，不上传任何服务器
- 潜意识挖掘是**邀请而非要求**，尊重用户的节奏
- ⚠️ 本工具**不是**心理咨询或治疗——严重心理问题请寻求专业帮助
- 用户有权随时要求删除自己的画像文件

- *All profile data stays local — nothing is uploaded to any server.*
- *Subconscious exploration is an invitation, not a demand.*
- *⚠️ This is NOT psychotherapy. If you're in crisis, seek professional help.*
- *You can delete your profile files at any time.*

---

## 📜 许可证 / License

[MIT](LICENSE) — 自由使用、修改和分发。

---

## 🤝 贡献 / Contributing

欢迎 Issue 和 PR！目标是让每个人都能拥有一个"不说谎的镜子"。

Issues and PRs welcome! The goal: a "mirror that never lies" for everyone.

---

**版本历史 / Version History**：v1.0 → v2.0（国际化）→ v3.0（技能模块化）→ v4.0（通用化）
