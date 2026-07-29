# Skill 02: Subconscious Excavation · 潜意识挖掘

> **Purpose / 目的**: Surface emotional trigger points, latent complexes, behavioral inertia, and patterns the user is normally unaware of.
> **浮现情绪触发点、隐性情结、行为惯性，以及用户正常情况下意识不到的模式。**
>
> **Trigger / 触发词**: `"subconscious"` / `"潜意识"` / `"深层"` / `"情结"`
> **Duration / 时长**: 25-40 minutes
> **Prompt reference**: [`prompts/subconscious_recall.md`](../prompts/subconscious_recall.md),
> [`prompts/base.md`](../prompts/base.md)

## Protocol / 操作流程

### Phase 1: Emotional Trigger Mapping (10 min)
- Ask about recent strong emotional reactions (anger, fear, withdrawal, overreaction)
- Identify the **trigger → response** chain for each
- Rate proportionality: "Was this reaction proportional to the situation?"

### Phase 2: Complex Probing (10-15 min)
Using the complex framework from `prompts/subconscious_recall.md`:

1. **Identify candidate complexes** — compare user patterns against known complex types (Abandonment, Hero, Caregiver, Achievement, Authority, Identity — see METHODOLOGY.md §3.2)
2. **Trace origins** — "When did this pattern first appear? What's the earliest memory?"
3. **Name the defense** — "What does this pattern protect you from?"
4. **Tag confidence level** — 🟢 High / 🟡 Medium / 🔴 Low

### Phase 3: Core Cycle Construction (10 min)
- Synthesize the most dominant pattern into a closed loop
- Format: Trigger → Reaction → Consequence → Compensation → Repeat

## Output / 输出

Write to **`profiles/subconscious.md`**:
```
# Subconscious Profile
## Identified Complexes (with confidence tags)
### [Complex Name] (🟢/🟡/🔴 confidence)
- Trigger Signal
- Origin / Earliest Memory
- Defense Pattern
- Current Impact
## Core Cycle (closed-loop diagram)
## Multi-Generational Themes (if identified)
## Belief Structure (Surface → Middle → Deep)
```

See [`profiles/example-subconscious.md`](../profiles/example-subconscious.md) for reference.

## Pitfalls / 注意事项

- ❌ Never present subconscious findings as absolute truth — always tag confidence
- ❌ Do not pathologize normal human patterns
- ✅ If user resists a finding, note the resistance — it is itself data
- ✅ Always end with integration: "None of this is 'wrong.' These patterns kept you safe. Now we can examine them."
- ⚠️ If the user shows signs of emotional overwhelm, switch to support mode immediately
