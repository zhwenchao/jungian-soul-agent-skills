---
name: psychological-digital-twin
description: Consent-first profile drafting, confirmation, and manual correction interface for Hermes Agent-integrated Jungian Soul Agent skills. Provides versioned local state layer with explicit user approval before persistence.
version: 1.0.0
author: zhwenchao
tags: [jungian, digital-twin, profile, consent-first, hermes-integration]
category: productivity
---

# Psychological Digital Twin · Profile Management Skill

**Class-level skill** for consent-first psychological digital twin profile management within Hermes Agent. Handles profile drafting, user confirmation, manual modification, and versioned iteration — all with explicit user approval before any data persistence.

## Triggers

Use when user says: "generate personal profile", "create psychological digital twin", "mirror dialogue", "self-reflection", "profile confirmation", "update profile version", or any request to build/reflect/iterate a self-portrait using AI.

## Always-on Rules (in SKILL.md body)

### 1. Consent-before-persistence

**Never** persist personal profile data to disk without explicit user confirmation. The adapter (Hermes or other LLM) must:

1. Call `prepare_profile()` to generate a pending draft in memory only
2. **Display the draft to the user** in the chat
3. Wait for user response: "confirm / modify / discard"
4. Only on explicit confirmation, call `confirm_profile()` to persist
5. On modification request, call `update_profile()` to create new version

**Why**: User has repeatedly demanded explicit verification before any data is saved. Half-saved state erodes trust.

### 2. User Isolation Enforcement

Each `user_id` can only access its own profile records. `get_profile()`, `list_profile_versions()`, and `delete_memory()` all filter by `user_id`. Cross-user access raises `PermissionError` or returns `None`.

**Why**: Multi-session environment; data from one user must never leak into another's conversation.

### 3. Versioned Iteration

Profiles are versioned integers starting at 1. `update_profile()` auto-increments version. `list_profile_versions()` returns all versions newest-first. History is never overwritten.

**Why**: User expects incremental improvement, not replacement. Audit trail required.

### 4. Safety Flash Gate

Before any deep exploration or memory storage, call `assess_safety(text)`. If `action=safety_stop`, halt the exercise, provide crisis resources, and do not generate memory draft.

**Why**: Conservative keyword-based stop gate for high-risk content (suicide, harm to others).

### 5. No Implicit Facts from Model Output

No model output is ever treated as ground truth. All `tentative_hypotheses` carry `confidence: low|medium|high`. Unknown or counter evidence is explicitly tracked. Report sections labeled "Tentative hypotheses (not facts)".

**Why**: User demands confidence labeling. Prevents AI from presenting hypotheses as established facts.

## Procedure (order of steps)

### Step 1: Initialize Profile Draft

Call `runtime.prepare_profile(user_id, profile_type, *, user_stated_facts, observed_patterns, tentative_hypotheses, unknown_or_counter_evidence)`

- Returns pending `MemoryDraft` in memory only
- **Never writes to disk**
- User sees draft in chat

### Step 2: Present to User

Display the draft's contents to the user. Include:

- Theme (profile type)
- User-stated facts
- Observed patterns
- Tentative hypotheses with confidence labels
- Unknown/counter evidence
- Prompt: "Confirm, modify, or discard?"

### Step 3: User Response Handling

Branch on user input:

- **"confirm"**: Call `runtime.confirm_profile(user_id, draft.id)` → persists to `users/<user_id>/memories/<draft_id>.json`
- **"modify"**: Call `runtime.update_profile(user_id, profile_type, overrides)` → creates new version with applied overrides, auto-confirms
- **"discard"**: Call `runtime.delete_memory(user_id, draft.id)` → removes pending draft without persisting

### Step 4: Post-Confirmation Operations

- If confirmed: `runtime.generate_report(user_id)` → returns formatted report from confirmed entries only
- If modified: New version is now the latest; user can continue iterating
- Always: Respect `retention` field from the data contract

### Step 5: Safety Check (before every step)

Call `runtime.assess_safety(text)` at the start of any deep-exploration or memory-related step. If safety_stop, abort and provide crisis resources.

## Data Contract (JSON schema for confirmed records)

```json
{
  "theme": "consciousness|shadow|self|anima-animus",
  "user_stated_facts": ["string"],
  "observed_patterns": ["string"],
  "tentative_hypotheses": [
    {"statement": "string", "confidence": "low|medium|high"}
  ],
  "unknown_or_counter_evidence": ["string"],
  "retention": "one session|until deleted|YYYY-MM-DD",
  "version": integer,
  "created_at": "ISO datetime",
  "confirmed_at": "ISO datetime | null"
}
```

## Pitfalls (with WHY)

### Pitfall A: Skipping the consent display

**Rule**: Always display the draft to the user before confirming.

**WHY**: User has explicit requirement: "not等待用户追问". Skipping this step violates the user's verification expectation and produces data the user didn't authorize.

### Pitfall B: Persisting without `confirm_profile()` call

**Rule**: Only `confirm_profile()` writes to disk. Never write JSON files manually.

**WHY**: The `data_root/users/*/memories/` directory is gitignored. Manual writes would escape the consent-first contract and potentially lose data on session reset.

### Pitfall C: Overwriting version history

**Rule**: `update_profile()` always creates version `latest.version + 1`. Never manually set version.

**WHY**: User expects incremental iteration, not replacement. Losing history violates the "cumulative" requirement.

### Pitfall D: Ignoring user_id isolation

**Rule**: All profile methods take `user_id` and filter by it. Never assume global state.

**WHY**: Multi-user environment; cross-user data leakage breaches privacy.

## Hermes Agent Integration Hook

```python
from core.runtime import ReflectionRuntime

runtime = ReflectionRuntime(data_root="~/.jungian-soul-agent")

# Example workflow in Hermes adapter:

def handle_profile_request(user_id, profile_type):
    # 1. Draft
    draft = runtime.prepare_profile(user_id, profile_type)
    
    # 2. Present (adapter displays in chat)
    # ... show draft to user ...
    
    # 3. Wait for user response (handled by Hermes UI)
    # User says: "confirm"
    
    # 4. Confirm
    confirmed = runtime.confirm_profile(user_id, draft.id)
    
    # 5. Report
    report = runtime.generate_report(user_id)
    return report
```

## Support Files (references/)

- `references/profile-data-contract.md` — Full JSON schema, retention policies, confidence labeling rationale
- `references/safety-flash-table.md` — Keyword patterns for `assess_safety()`, with examples and exclusion notes

## Complementary Skills (do NOT duplicate)

- `hermes-agent` — for Hermes CLI/config/plugin management; this skill covers profile workflow only
- `slide-maker` — for presentation creation; separate domain
- Note-taking skills (obsidian, notion) — for different persistence modalities

## Confidence Labeling Quick Reference

| Confidence | When to Use |
|---|---|
| 🔴 low | Single source, speculative, contradicted by counter-evidence |
| 🟡 medium | Multiple sources but no consensus, or one strong source |
| 🟢 high | Multiple converging sources, or explicit user-stated fact |

## Delivery Style (user preferences)

- Direct, no sugarcoating (per user style)
- Numbered steps for multi-step procedures
- Confidence ratings on all hypotheses
- Clear "what can be done next" after each output
- No Japanese characters or cultural references (user prohibits)
- Tables for structured data output
- Precise, citation-accurate when referencing names/roles/numbers