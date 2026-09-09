# Skill 06: Persona Iteration · 自我认知迭代报告

> **Safety & governance / 安全与治理**: Load [`SAFETY_AND_DATA_GOVERNANCE.md`](../SAFETY_AND_DATA_GOVERNANCE.md) and [`prompts/base.md`](../prompts/base.md) first. Generate a report only when the user explicitly asks; use only user-confirmed records or hypotheses explicitly retained for review.

> **Purpose / 目的**: Generate a cumulative reflection report showing how the user’s self-understanding has changed across conversations.
>
> 生成一份累积反思报告，呈现用户对自己的理解如何在多次对话中变化。

> **Trigger / 触发词**: `"report"` / `"迭代报告"` / `"总结"` / `"分析"`
> **Prerequisite / 前置条件**: At least three user-confirmed reflection entries, or the user may explicitly request a shorter provisional report.

## Protocol · 操作流程

### 1. Verify scope · 确认范围

Before generation, state which confirmed entries will be used and ask whether the user wants to include any tentative hypotheses. Do not access data from another user or an unapproved storage location.

### 2. Generate a reviewable report · 生成可审阅报告

```markdown
# Self-Reflection Iteration Report — [Date]

## 1. Materials Used / 使用材料
- [date / user-confirmed entry / scope]

## 2. Self-Understanding Trajectory / 自我认知轨迹
- **User-stated shift**: [what the user says has changed]
- **Observed pattern**: [only if directly supported]
- **Unknown or competing explanation**: [what remains uncertain]

## 3. Recurring Tensions / 反复出现的张力
| Tension | Supporting material | Status | Confidence | User confirmation |
|---|---|---|---|---|
| [e.g., security vs. autonomy] | [entry/date] | revisiting | low/medium/high | confirmed/pending |

## 4. Optional Archetype Metaphors / 可选原型隐喻
> These are optional lenses, not identity facts.
- [metaphor] — [why it may be useful / why it may not fit]

## 5. Questions the User May Choose to Revisit / 用户可选择重访的问题
1. [optional question]

## 6. User Corrections / 用户校正
- [space for edit, rejection, or deletion request]
```

### 3. After generation · 生成后

- Invite the user to correct, delete, or reclassify any statement.
- Do not automatically update a profile or memory from the report.
- Only save the report after a separate explicit confirmation under Skill 05.

## Pitfalls · 注意事项

- ❌ Do not call a hypothesis a fact, a diagnosis, “progress,” integration, or resolution without the user’s own basis.
- ❌ Do not use silence, non-response, or a model’s prior inference as evidence.
- ❌ Do not produce an automatic report after a fixed number of sessions.
- ✅ Preserve uncertainty and counter-evidence.
- ✅ Treat oscillation, pauses, and changes of mind as information—not failure.
