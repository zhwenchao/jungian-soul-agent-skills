"""Consent-first local runtime for the Psychological Digital Twin skill pack.

This module intentionally does not call an LLM. It provides the auditable local
state layer that an adapter (Hermes, OpenAI, or a local model) must use before
persisting reflection material.
"""

from __future__ import annotations

import json
import re
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


RISK_PATTERNS = (
    r"\bkill myself\b",
    r"\bsuicide\b",
    r"\bend my life\b",
    r"\bkill (him|her|them|someone)\b",
    r"自杀",
    r"杀了自己",
    r"结束生命",
    r"杀人",
    r"伤害他人",
)


@dataclass
class MemoryDraft:
    """A user-reviewable reflection record before any persistence occurs."""

    theme: str
    user_stated_facts: list[str] = field(default_factory=list)
    observed_patterns: list[str] = field(default_factory=list)
    tentative_hypotheses: list[dict[str, str]] = field(default_factory=list)
    unknown_or_counter_evidence: list[str] = field(default_factory=list)
    retention: str = "one session"
    id: str = field(default_factory=lambda: uuid.uuid4().hex)
    status: str = "pending"
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    confirmed_at: str | None = None
    version: int = 1

    def __getitem__(self, key: str) -> Any:
        return asdict(self)[key]


@dataclass(frozen=True)
class SafetyResult:
    action: str
    allow_deep_exploration: bool
    allow_memory: bool
    message: str


class ReflectionRuntime:
    """Per-user local storage with explicit confirmation and deletion controls."""

    def __init__(self, data_root: Path | str) -> None:
        self.data_root = Path(data_root).expanduser().resolve()
        self.pending: dict[tuple[str, str], MemoryDraft] = {}

    def prepare_memory(self, user_id: str, draft: MemoryDraft) -> MemoryDraft:
        """Return a pending draft. This method never writes personal data to disk."""
        self._validate_user_id(user_id)
        self._validate_draft(draft)
        draft.status = "pending"
        draft.confirmed_at = None
        self.pending[(user_id, draft.id)] = draft
        return draft

    def confirm_memory(self, user_id: str, draft_id: str) -> MemoryDraft:
        """Persist only a pending draft belonging to the requesting user."""
        self._validate_user_id(user_id)
        key = (user_id, draft_id)
        if key not in self.pending:
            if self._draft_belongs_to_another_user(user_id, draft_id):
                raise PermissionError("This draft belongs to a different user.")
            raise KeyError("No pending draft exists with this id.")

        draft = self.pending.pop(key)
        draft.status = "confirmed"
        draft.confirmed_at = datetime.now(timezone.utc).isoformat()
        path = self._memory_path(user_id, draft.id)
        path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        path.write_text(json.dumps(asdict(draft), ensure_ascii=False, indent=2), encoding="utf-8")
        return draft

    def list_memories(self, user_id: str) -> list[MemoryDraft]:
        """Read only the confirmed entries within this user's data boundary."""
        self._validate_user_id(user_id)
        directory = self._user_dir(user_id) / "memories"
        if not directory.exists():
            return []
        records = [self._load_memory(path) for path in sorted(directory.glob("*.json"))]
        return sorted(records, key=lambda item: item.created_at)

    def delete_memory(self, user_id: str, draft_id: str) -> None:
        """Delete a confirmed record or discard the user's pending draft."""
        self._validate_user_id(user_id)
        self.pending.pop((user_id, draft_id), None)
        path = self._memory_path(user_id, draft_id)
        if path.exists():
            path.unlink()

    def generate_report(self, user_id: str) -> str:
        """Create a non-persisted report from user-confirmed memory entries only."""
        records = self.list_memories(user_id)
        if not records:
            return "No confirmed reflection entries are available for this report."

        lines = ["# Self-Reflection Iteration Report", "", "## Confirmed materials"]
        for record in records:
            lines.append(f"- {record.created_at[:10]} — {record.theme}")
        lines.extend(["", "## User-stated facts"])
        for record in records:
            lines.extend(f"- {item}" for item in record.user_stated_facts)
        lines.extend(["", "## Tentative hypotheses (not facts)"])
        for record in records:
            for hypothesis in record.tentative_hypotheses:
                confidence = hypothesis.get("confidence", "unspecified")
                lines.append(f"- [{confidence}] {hypothesis.get('statement', '')}")
        lines.extend(["", "## User correction", "- Please correct, reject, or delete any statement above."])
        return "\n".join(lines)

    def assess_safety(self, text: str) -> SafetyResult:
        """Apply a conservative keyword-based stop gate; it is not a clinical assessment."""
        if any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in RISK_PATTERNS):
            return SafetyResult(
                action="safety_stop",
                allow_deep_exploration=False,
                allow_memory=False,
                message=(
                    "Pause the reflective exercise. Are you in immediate danger right now? "
                    "Please contact local emergency services, a crisis service, a qualified professional, "
                    "or a trusted person who can be with you."
                ),
            )
        return SafetyResult(
            action="continue_with_consent",
            allow_deep_exploration=True,
            allow_memory=True,
            message="No automated high-risk phrase was detected. Continue only with explicit consent.",
        )

    def _user_dir(self, user_id: str) -> Path:
        return self.data_root / "users" / user_id

    def _memory_path(self, user_id: str, draft_id: str) -> Path:
        return self._user_dir(user_id) / "memories" / f"{draft_id}.json"

    def _draft_belongs_to_another_user(self, user_id: str, draft_id: str) -> bool:
        for owner, existing_id in self.pending:
            if owner != user_id and existing_id == draft_id:
                return True
        for path in self.data_root.glob(f"users/*/memories/{draft_id}.json"):
            owner = path.parents[1].name
            if owner != user_id:
                return True
        return False

    @staticmethod
    def _load_memory(path: Path) -> MemoryDraft:
        data: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
        return MemoryDraft(**data)

    @staticmethod
    def _validate_user_id(user_id: str) -> None:
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", user_id):
            raise ValueError("user_id must contain only letters, numbers, underscores, or hyphens.")

    @staticmethod
    def _validate_draft(draft: MemoryDraft) -> None:
        if not draft.theme.strip():
            raise ValueError("theme is required")
        allowed = {"low", "medium", "high"}
        for hypothesis in draft.tentative_hypotheses:
            if not hypothesis.get("statement", "").strip():
                raise ValueError("Each hypothesis needs a statement.")
            if hypothesis.get("confidence", "").lower() not in allowed:
                raise ValueError("Each hypothesis confidence must be low, medium, or high.")

    def prepare_profile(self, user_id: str, profile_type: str, *, user_stated_facts: list[str] | None = None, observed_patterns: list[str] | None = None, tentative_hypotheses: list[dict[str, str]] | None = None, unknown_or_counter_evidence: list[str] | None = None) -> MemoryDraft:
        """Prepare a pending profile draft. This method never writes personal data to disk."""
        self._validate_user_id(user_id)
        draft_id = uuid.uuid4().hex
        draft = MemoryDraft(
            theme=profile_type,
            user_stated_facts=user_stated_facts or [],
            observed_patterns=observed_patterns or [],
            tentative_hypotheses=tentative_hypotheses or [],
            unknown_or_counter_evidence=unknown_or_counter_evidence or [],
        )
        self.prepare_memory(user_id, draft)
        return draft

    def confirm_profile(self, user_id: str, draft_id: str) -> MemoryDraft:
        """Persist a pending profile draft belonging to the requesting user."""
        return self.confirm_memory(user_id, draft_id)

    def get_profile(self, user_id: str, profile_type: str) -> MemoryDraft | None:
        """Read the confirmed profile of the given type for this user."""
        records = self.list_memories(user_id)
        for record in records:
            if record.theme == profile_type:
                return record
        return None

    def list_profile_versions(self, user_id: str, profile_type: str) -> list[MemoryDraft]:
        """List all confirmed versions of a profile type, newest first."""
        records = self.list_memories(user_id)
        return [r for r in records if r.theme == profile_type]

    def update_profile(self, user_id: str, profile_type: str, overrides: dict[str, Any]) -> MemoryDraft:
        """Create a new version of a profile by applying overrides to the latest confirmed version."""
        latest = self.get_profile(user_id, profile_type)
        if latest is None:
            raise KeyError(f"No confirmed profile of type '{profile_type}' found for user {user_id}.")

        # Start from the latest confirmed profile and apply overrides
        new_draft = MemoryDraft(
            theme=profile_type,
            user_stated_facts=overrides.get("user_stated_facts", latest.user_stated_facts),
            observed_patterns=overrides.get("observed_patterns", latest.observed_patterns),
            tentative_hypotheses=overrides.get("tentative_hypotheses", latest.tentative_hypotheses),
            unknown_or_counter_evidence=overrides.get("unknown_or_counter_evidence", latest.unknown_or_counter_evidence),
            retention=latest.retention,
            version=latest.version + 1,
        )
        # Mark as pending so it can be confirmed later
        new_draft.status = "pending"
        self.prepare_memory(user_id, new_draft)
        # Auto-confirm since the user has specified the desired overrides
        return self.confirm_memory(user_id, new_draft.id)
