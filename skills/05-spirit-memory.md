# Skill 05: Spirit Memory · 精神向量记忆沉淀

> **Purpose / 目的**: Automatically capture, condense, and store the session's key insights — belief changes, emotional deltas, and unresolved signals.
> **自动捕获、浓缩、存储每次对话的关键洞察——信念变化、情绪增量、未完成信号。**
>
> **Trigger / 触发**: Auto (end of every session)
> **Duration / 时长**: < 1 minute (background)
> **Prompt reference**: [`prompts/base.md`](../prompts/base.md)

## Protocol / 操作流程

### At End of Every Session, Run This Check:

```text
1. EXTRACT new conscious-level material → update consciousness.md
   - Any changed beliefs, new self-descriptions, new behavioral patterns

2. EXTRACT new subconscious findings → update subconscious.md
   - Any newly surfaced complexes, trigger signals, or cycle nuances

3. EXTRACT belief changes → record in memory timeline
   - "Previously: X. Now: Y. What drove the shift?"

4. EXTRACT unfinished topics → homework list
   - "User paused at [topic]. Flag for next session."

5. SUMMARIZE session theme → memory entry
   - One-sentence: "This session was about [theme]."
```

### Output Format / 输出格式

Each session's spirit memory entry follows this template:

```markdown
## Spirit Memory — [YYYY-MM-DD]
- **Theme**: [one-sentence summary]
- **Belief delta**: [what changed]
- **Emotional trajectory**: [start → end]
- **Unfinished signals**: [topics to revisit]
- **Confidence**: 🟢 Stable / 🟡 Developing / 🔴 Needs more data
```

### Storage / 存储

- In plain-text files under `profiles/` (for Obsidian/local knowledge base integration)
- Timestamp each entry for longitudinal tracking
- The timeline data fuels Skill 6 (Persona Iteration)

## Pitfalls / 注意事项

- ❌ Do not ask the user for permission to save — this runs automatically
- ❌ Do not overwrite — append to a chronological log
- ✅ Keep each entry concise (3-5 bullet points max)
- ✅ Flag only significant belief deltas, not every minor mood shift
=> If a session was purely procedural (no self-exploration), skip the memory entry
