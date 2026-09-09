# Skill 01: Consciousness Replication · 表层意识复刻

> **Safety & consent / 安全与同意**: Load [`SAFETY_AND_DATA_GOVERNANCE.md`](../SAFETY_AND_DATA_GOVERNANCE.md) and [`prompts/base.md`](../prompts/base.md) first. Do not persist a profile without explicit user review and consent.

> **Purpose / 目的**: Build a baseline portrait of the user's conscious ego — thinking patterns, behavioral habits, decision logic, and expressed personality.
> **构建用户意识自我的基线画像——思维模式、行为习惯、决策逻辑、外显性格。**
>
> **Trigger / 触发词**: `"who am I"` / `"意识复刻"` / `"表层"` / `"性格"`
> **Duration / 时长**: 10-30 minutes
> **Prompt reference**: [`prompts/base.md`](../prompts/base.md) (always-on), [`prompts/jungian_assessment.md`](../prompts/jungian_assessment.md),
> [`prompts/text_style_extract.md`](../prompts/text_style_extract.md)

## Protocol / 操作流程

### Phase 1: Observation (5 min)
- Engage the user in normal conversation (ask about their day, current work, recent decisions)
- Observe language style, sentence structure, emotional tone
- **Lock the base persona** (reference `prompts/base.md`): mirror the user's native expression

### Phase 2: Structured Assessment (10-15 min)
Using `prompts/jungian_assessment.md`, explore:
- Self-description: "How would you describe yourself to a stranger?"
- Typical day: "Walk me through how you usually spend a normal day"
- Decision style: "When faced with a tough choice, what does your process look like?"
- Values: "What matters to you most — and how do you know?"
- Role mapping: "What different roles do you play in life (work, family, social)? Which feels most 'you'?"

### Phase 3: Textual Analysis (5 min) [optional]
- If the user has past writing (journals, social media, work documents), run `prompts/text_style_extract.md`
- Extract: unique phrasing patterns, emotional vocabulary range, topic avoidance signals

## Output / 输出

Write to **`profiles/consciousness.md`**:
```
# Consciousness Profile
## Core Identity
## Behavioral Patterns
## Language & Expression
## Self-Perception (acknowledged strengths & weaknesses)
## Role Map (Persona in different contexts)
## Key Values & Priorities
```

See [`profiles/example-consciousness.md`](../profiles/example-consciousness.md) for reference.

## Pitfalls / 注意事项

- ❌ Do not rush through this — the baseline must be accurate for all subsequent skills
- ❌ Do not use generic AI "summarizing" language; stay in the user's own voice
- ✅ Let silence happen; the longest pauses often reveal the most
- ✅ Cross-validate: "You said X earlier, but is that consistent with Y?"
