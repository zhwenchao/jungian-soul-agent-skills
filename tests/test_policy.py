"""Repository policy regression tests."""

from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SAFETY_REFERENCE = "SAFETY_AND_DATA_GOVERNANCE.md"


class PolicyRegressionTests(unittest.TestCase):
    def test_every_skill_and_prompt_loads_the_global_safety_policy(self) -> None:
        paths = sorted((REPO / "skills").glob("*.md")) + sorted((REPO / "prompts").glob("*.md"))
        missing = [str(path.relative_to(REPO)) for path in paths if SAFETY_REFERENCE not in path.read_text(encoding="utf-8")]

        self.assertEqual(missing, [])

    def test_no_personal_runtime_data_path_is_tracked(self) -> None:
        ignored = (REPO / ".gitignore").read_text(encoding="utf-8")

        for rule in ("data/", "memory/", "sessions/", "chroma/"):
            self.assertIn(rule, ignored)

    def test_policy_declares_opt_in_memory_and_crisis_stop(self) -> None:
        policy = (REPO / SAFETY_REFERENCE).read_text(encoding="utf-8")

        self.assertIn("Default: **do not save**", policy)
        self.assertIn("Stop archetype switching", policy)
        self.assertIn("explicit opt-in", policy)

    def test_json_configs_remain_valid(self) -> None:
        for path in (REPO / "config").glob("*.json"):
            with self.subTest(path=path.name):
                json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
