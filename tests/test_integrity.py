"""Behavior tests for the repository integrity checker."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
import sys
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]


def run_checker(repo: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(repo / "demo" / "run_local_demo.py"), "--repo", str(repo)],
        text=True,
        capture_output=True,
        check=False,
    )


class IntegrityCheckerTests(unittest.TestCase):
    def test_checker_succeeds_for_complete_repository(self) -> None:
        result = run_checker(REPO)

        self.assertEqual(result.returncode, 0)
        self.assertIn("All required checks passed", result.stdout)

    def test_checker_fails_when_required_skill_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            clone = Path(temp_dir) / "repo"
            shutil.copytree(REPO, clone, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            (clone / "skills" / "05-spirit-memory.md").unlink()

            result = run_checker(clone)

        self.assertEqual(result.returncode, 1)
        self.assertIn("MISSING", result.stdout)
        self.assertIn("Required checks failed", result.stdout)


if __name__ == "__main__":
    unittest.main()
