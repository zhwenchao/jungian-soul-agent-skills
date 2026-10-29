"""Regression tests for the safety gate's Chinese-language coverage.

The safety gate is the first line of defense for every deep-exploration and
memory step. A gap in its patterns means a high-risk disclosure can pass
through unblocked, so coverage is asserted explicitly for both simplified and
traditional Chinese.

The gate is a conservative keyword stop mechanism, not a clinical assessment.
"""

from __future__ import annotations

import unittest

from core.runtime import ReflectionRuntime


class SafetyGateLanguageCoverageTests(unittest.TestCase):
    """Every high-risk concept must be caught in every supported language form."""

    def setUp(self) -> None:
        self.runtime = ReflectionRuntime(data_root="/tmp/jungian-safety-gate-tests")

    def assert_stopped(self, text: str) -> None:
        result = self.runtime.assess_safety(text)
        self.assertEqual(
            result.action,
            "safety_stop",
            f"expected safety_stop for {text!r}",
        )
        self.assertFalse(result.allow_deep_exploration)
        self.assertFalse(result.allow_memory)

    def assert_continued(self, text: str) -> None:
        result = self.runtime.assess_safety(text)
        self.assertEqual(
            result.action,
            "continue_with_consent",
            f"expected continue_with_consent for {text!r}",
        )

    def test_simplified_chinese_self_harm_is_blocked(self) -> None:
        for text in (
            "我想自杀",
            "我杀了自己",
            "想结束生命",
            "我不想活了",
            "我活不下去",
            "我想死",
            "我要轻生",
            "我去跳楼",
            "我想割腕",
            "我想上吊",
        ):
            with self.subTest(text=text):
                self.assert_stopped(text)

    def test_traditional_chinese_self_harm_is_blocked(self) -> None:
        """Traditional Chinese forms must be caught as reliably as simplified ones."""
        for text in (
            "我想自殺",
            "我殺了自己",
            "想結束生命",
            "我不想活了",
            "我活不下去",
            "我想死",
            "我要輕生",
            "我去跳樓",
            "我想割腕",
            "我想上吊",
        ):
            with self.subTest(text=text):
                self.assert_stopped(text)

    def test_harm_to_others_is_blocked_in_both_scripts(self) -> None:
        for text in (
            "我要杀了他",
            "我要杀了他",
            "我想杀人",
            "我想殺人",
            "我想伤害他人",
            "我想傷害他人",
        ):
            with self.subTest(text=text):
                self.assert_stopped(text)

    def test_english_self_harm_is_blocked(self) -> None:
        for text in (
            "I want to kill myself",
            "I am having a plan to suicide",
            "I want to end my life",
            "I want to kill him",
        ):
            with self.subTest(text=text):
                self.assert_stopped(text)

    def test_ordinary_reflection_content_is_not_blocked(self) -> None:
        """A wide gate would make the tool useless, so normal content must pass."""
        for text in (
            "今天工作壓力很大，覺得有點累",
            "我最近常常想殺掉這個專案的 deadline",
            "我想殺掉那台一直當掉的伺服器",
            "壓力大到有點喘不過氣",
            "今天心情不好，想找人聊聊",
            "我對這個專案的殺傷力有點擔心",
        ):
            with self.subTest(text=text):
                self.assert_continued(text)


if __name__ == "__main__":
    unittest.main()
