"""Behavior tests for profile drafting, confirmation, and manual correction."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from core.runtime import MemoryDraft, ReflectionRuntime


class ProfileRuntimeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.runtime = ReflectionRuntime(Path(self.temp_dir.name))

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def draft(self) -> MemoryDraft:
        return MemoryDraft(
            theme="consciousness",
            user_stated_facts=["I prefer concise, direct communication."],
            observed_patterns=["The user asks for verification before conclusions."],
            tentative_hypotheses=[
                {"statement": "The user values operational reliability.", "confidence": "high"}
            ],
            unknown_or_counter_evidence=["This may vary in informal relationships."],
        )

    def test_profile_draft_is_not_persisted_until_confirmed(self) -> None:
        draft = self.runtime.prepare_profile("alice", "consciousness", user_stated_facts=["I prefer concise, direct communication."], observed_patterns=["The user asks for verification before conclusions."], tentative_hypotheses=[{"statement": "The user values operational reliability.", "confidence": "high"}], unknown_or_counter_evidence=["This may vary in informal relationships."])

        self.assertEqual(draft.status, "pending")
        self.assertIsNone(self.runtime.get_profile("alice", "consciousness"))

    def test_confirmed_profile_is_retrievable_and_versioned(self) -> None:
        draft = self.runtime.prepare_profile("alice", "consciousness", user_stated_facts=["I prefer concise, direct communication."], observed_patterns=["The user asks for verification before conclusions."], tentative_hypotheses=[{"statement": "The user values operational reliability.", "confidence": "high"}], unknown_or_counter_evidence=["This may vary in informal relationships."])

        saved = self.runtime.confirm_profile("alice", draft.id)

        self.assertEqual(saved.status, "confirmed")
        profile = self.runtime.get_profile("alice", "consciousness")
        self.assertEqual(profile["version"], 1)
        self.assertEqual(profile["user_stated_facts"], ["I prefer concise, direct communication."])

    def test_manual_correction_creates_next_version_without_losing_history(self) -> None:
        draft = self.runtime.prepare_profile("alice", "consciousness", user_stated_facts=["I prefer concise, direct communication."], observed_patterns=["The user asks for verification before conclusions."], tentative_hypotheses=[{"statement": "The user values operational reliability.", "confidence": "high"}], unknown_or_counter_evidence=["This may vary in informal relationships."])
        self.runtime.confirm_profile("alice", draft.id)

        profile = self.runtime.update_profile(
            "alice", "consciousness", {"user_stated_facts": ["I prefer direct communication, but not always concise."]}
        )

        self.assertEqual(profile["version"], 2)
        self.assertEqual(len(self.runtime.list_profile_versions("alice", "consciousness")), 2)
        self.assertEqual(profile["user_stated_facts"], ["I prefer direct communication, but not always concise."])

    def test_profile_isolation_blocks_other_users(self) -> None:
        draft = self.runtime.prepare_profile("alice", "consciousness", user_stated_facts=["I prefer concise, direct communication."], observed_patterns=["The user asks for verification before conclusions."], tentative_hypotheses=[{"statement": "The user values operational reliability.", "confidence": "high"}], unknown_or_counter_evidence=["This may vary in informal relationships."])
        self.runtime.confirm_profile("alice", draft.id)

        self.assertIsNone(self.runtime.get_profile("bob", "consciousness"))
        with self.assertRaises(PermissionError):
            self.runtime.confirm_profile("bob", draft.id)


if __name__ == "__main__":
    unittest.main()