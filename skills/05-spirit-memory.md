# Skill 05: Spirit Memory · 反思记忆沉淀

> **Purpose / 目的**: With explicit user permission, prepare a concise, reviewable record of insights the user wants to retain.
>
> 在用户明确同意的前提下，形成一份简洁、可审阅、由用户决定是否保留的反思记录。
>
> **Safety & governance / 安全与治理**: [`SAFETY_AND_DATA_GOVERNANCE.md`](../SAFETY_AND_DATA_GOVERNANCE.md) overrides this skill.

## Trigger · 触发条件

Only run when the user explicitly asks to save, summarize for later, update a profile, or has enabled a clearly described save preference for this category.

Never run automatically merely because a session ends. Never save during a high-risk interruption.

仅在用户明确要求保存、要求形成后续摘要、要求更新画像，或已针对该类别开启清晰的保存偏好时运行。不得因为会话结束而自动运行；高风险中断期间不得写入。

## Protocol · 操作流程

### 1. Check permission and scope · 确认权限与范围

Ask or confirm all of the following:

- What may be saved: session summary, direct quote, consciousness profile, pattern hypothesis, or retrieval index?
- Where will it be stored?
- Is this a one-time save or an ongoing preference?
- Does the user want to review or edit the proposed entry before it is written?

Default answer when no preference exists: **do not save**.

### 2. Prepare a proposed entry · 生成待确认条目

Create a short draft, separating facts and hypotheses. Include only material necessary for the purpose.

```markdown
## Reflection Memory — [YYYY-MM-DD]
- **Theme / 主题**: [one sentence]
- **User-stated facts / 用户明确陈述**: [0–3 bullets]
- **Observed patterns / 可观察模式**: [0–3 bullets]
- **Tentative hypotheses / 暂定假设**: [0–2 bullets, each with confidence]
- **Unknown or counter-evidence / 未知或反证**: [0–2 bullets]
- **User confirmation / 用户确认**: pending | confirmed | edited | declined
- **Retention / 保留期限**: [one session / date / until deletion]
```

Do not infer a subconscious finding merely because the user used a strong emotion, paused, avoided a topic, or accepted a question.

### 3. Review before write · 写入前审阅

Show the draft and storage destination. Ask the user to choose one:

- Save as shown
- Edit first
- Do not save

If the user does not affirm saving, discard the draft at the end of the current interaction.

### 4. Store safely · 安全存储

- Store real user data outside the repository, in a per-user, per-session directory controlled by the runtime.
- Do not write personal data to tracked `profiles/` templates.
- Record a timestamp and the user’s confirmation status.
- Provide deletion/export access through the runtime implementation.

## Connection to Persona Iteration · 与人格迭代的关系

Skill 06 may use only entries the user has confirmed or explicitly marked as a hypothesis to revisit. It must preserve evidence labels and uncertainty; it must not rewrite a hypothesis as a fact.

## Pitfalls · 注意事项

- ❌ Do not save silently or by default.
- ❌ Do not overwrite user-authored material.
- ❌ Do not store a crisis disclosure as a profile insight during a safety interruption.
- ✅ Keep entries concise and reversible.
- ✅ Treat the user as the author and final editor of their own long-term narrative.
