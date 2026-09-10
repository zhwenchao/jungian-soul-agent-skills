# V5 Runtime Architecture · 可运行内核架构

## What this adds · 新增了什么

The original repository is a portable methodology and prompt package. V5 adds a small, local **consent-first runtime core**; it is not an LLM product and makes no external model calls.

原仓库是可移植的方法论与提示词包。V5 增加了一个本地、轻量、以同意为先的运行内核；它不是 LLM 产品，不会主动调用外部模型。

```text
LLM / Hermes / local adapter
          │
          ▼
  core.runtime.ReflectionRuntime
  ├─ safety gate         → high-risk: stop deep work and disable memory
  ├─ draft session state → prepare a reviewable entry; no disk write
  ├─ consent gate        → explicit confirmation is required to persist
  ├─ per-user storage    → data_root/users/<user>/memories/*.json
  ├─ deletion            → user can remove an entry
  └─ report builder      → reads confirmed entries only
```

## Data contract · 数据契约

A memory record contains only these reviewable fields:

- `theme`
- `user_stated_facts`
- `observed_patterns`
- `tentative_hypotheses` with `low | medium | high` confidence
- `unknown_or_counter_evidence`
- `retention`
- creation and confirmation timestamps

No model output is implicitly treated as fact. The adapter must show the draft to the user before calling `confirm_memory()`.

## Local storage · 本地存储

The runtime receives a data root at startup. Suggested production default:

```text
~/.jungian-soul-agent/data/users/<user-id>/memories/
```

This location is deliberately outside the Git repository. A runtime host should use OS-level account permissions and document its backup/sync settings.

## Adapter integration · 适配层接入

A host platform should follow this sequence:

1. Run `assess_safety(user_text)` before deep exploration or storage.
2. If it returns `safety_stop`, stop role-play/deep exploration and use the policy’s safety response path.
3. For saving, build `MemoryDraft` from visible, evidence-labeled material.
4. Call `prepare_memory(user_id, draft)`; this is in-memory only.
5. Show the exact draft, storage location, and choices: save / edit / do not save.
6. Call `confirm_memory()` only after explicit approval in the same secured session.
7. Use `generate_report()` only for confirmed records; never auto-save the report.

## Local verification · 本地验证

```bash
python3 -m unittest discover -s tests -v
python3 demo/run_local_demo.py
python3 scripts/reflection_runtime.py safety-check "I am having a difficult day"
```

`draft-memory` is a preview helper. Because pending drafts are intentionally not persisted, approval must be performed by a stateful host adapter in the same session—not by a later independent command invocation.
