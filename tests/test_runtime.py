"""End-to-end tests for the consent-first reflection runtime."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from core.runtime import MemoryDraft, ReflectionRuntime


class ReflectionRuntimeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.runtime = ReflectionRuntime(Path(self.temp_dir.name))

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def valid_draft(self) -> MemoryDraft:
        return MemoryDraft(
            theme="Work and self-worth",
            user_stated_facts=["I feel uneasy when work output slows down."],
            observed_patterns=["The user links rest with guilt."],
            tentative_hypotheses=[
                {"statement": "Achievement may be tied to self-worth.", "confidence": "medium"}
            ],
            unknown_or_counter_evidence=["The user also values family time."],
            retention="until deleted",
        )

    def test_creating_a_draft_does_not_persist_personal_data(self) -> None:
        draft = self.runtime.prepare_memory("alice", self.valid_draft())

        self.assertEqual(draft.status, "pending")
        self.assertEqual(self.runtime.list_memories("alice"), [])

    def test_only_explicit_confirmation_persists_memory(self) -> None:
        draft = self.runtime.prepare_memory("alice", self.valid_draft())

        saved = self.runtime.confirm_memory("alice", draft.id)

        self.assertEqual(saved.status, "confirmed")
        self.assertEqual(len(self.runtime.list_memories("alice")), 1)

    def test_user_records_are_isolated(self) -> None:
        draft = self.runtime.prepare_memory("alice", self.valid_draft())
        self.runtime.confirm_memory("alice", draft.id)

        self.assertEqual(self.runtime.list_memories("bob"), [])
        with self.assertRaises(PermissionError):
            self.runtime.confirm_memory("bob", draft.id)

    def test_user_can_delete_confirmed_memory(self) -> None:
        draft = self.runtime.prepare_memory("alice", self.valid_draft())
        self.runtime.confirm_memory("alice", draft.id)

        self.runtime.delete_memory("alice", draft.id)

        self.assertEqual(self.runtime.list_memories("alice"), [])

    def test_high_risk_text_blocks_deep_exploration_and_memory(self) -> None:
        result = self.runtime.assess_safety("I have a plan to kill myself tonight")

        self.assertEqual(result.action, "safety_stop")
        self.assertFalse(result.allow_deep_exploration)
        self.assertFalse(result.allow_memory)

    def test_report_uses_confirmed_entries_only(self) -> None:
        confirmed = self.runtime.prepare_memory("alice", self.valid_draft())
        self.runtime.confirm_memory("alice", confirmed.id)
        self.runtime.prepare_memory(
            "alice",
            MemoryDraft(theme="Unconfirmed", user_stated_facts=["Do not include me"], retention="one session"),
        )

        report = self.runtime.generate_report("alice")

        self.assertIn("Work and self-worth", report)
        self.assertNotIn("Unconfirmed", report)


if __name__ == "__main__":
    unittest.main()
