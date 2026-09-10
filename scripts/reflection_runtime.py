#!/usr/bin/env python3
"""Local command-line interface for the consent-first reflection runtime."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from core.runtime import MemoryDraft, ReflectionRuntime


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data-root",
        type=Path,
        default=Path.home() / ".jungian-soul-agent" / "data",
        help="Local directory for real user data (default: ~/.jungian-soul-agent/data).",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    safety = subparsers.add_parser("safety-check", help="Run the conservative safety stop gate.")
    safety.add_argument("text")

    draft = subparsers.add_parser("draft-memory", help="Create a pending memory draft; does not save it.")
    draft.add_argument("user_id")
    draft.add_argument("--theme", required=True)
    draft.add_argument("--fact", action="append", default=[])
    draft.add_argument("--pattern", action="append", default=[])
    draft.add_argument("--hypothesis", action="append", default=[], metavar="CONFIDENCE:TEXT")
    draft.add_argument("--unknown", action="append", default=[])
    draft.add_argument("--retention", default="one session")

    confirm = subparsers.add_parser("confirm-memory", help="Persist an explicitly approved pending draft.")
    confirm.add_argument("user_id")
    confirm.add_argument("draft_id")

    listing = subparsers.add_parser("list-memories", help="List this user's confirmed records.")
    listing.add_argument("user_id")

    report = subparsers.add_parser("report", help="Build a non-persisted report from confirmed records.")
    report.add_argument("user_id")

    delete = subparsers.add_parser("delete-memory", help="Delete a pending or confirmed record.")
    delete.add_argument("user_id")
    delete.add_argument("draft_id")
    return parser


def parse_hypotheses(values: list[str]) -> list[dict[str, str]]:
    results = []
    for value in values:
        confidence, separator, statement = value.partition(":")
        if not separator:
            raise ValueError("Each --hypothesis must use CONFIDENCE:TEXT, e.g. medium:example.")
        results.append({"confidence": confidence.lower(), "statement": statement.strip()})
    return results


def main() -> int:
    args = build_parser().parse_args()
    runtime = ReflectionRuntime(args.data_root)

    if args.command == "safety-check":
        result = runtime.assess_safety(args.text)
        print(json.dumps(result.__dict__, ensure_ascii=False, indent=2))
        return 2 if result.action == "safety_stop" else 0

    if args.command == "draft-memory":
        draft = runtime.prepare_memory(
            args.user_id,
            MemoryDraft(
                theme=args.theme,
                user_stated_facts=args.fact,
                observed_patterns=args.pattern,
                tentative_hypotheses=parse_hypotheses(args.hypothesis),
                unknown_or_counter_evidence=args.unknown,
                retention=args.retention,
            ),
        )
        print(json.dumps(draft.__dict__, ensure_ascii=False, indent=2))
        print("\nNot saved. Review this draft and explicitly run confirm-memory only after user approval.")
        return 0

    if args.command == "confirm-memory":
        draft = runtime.confirm_memory(args.user_id, args.draft_id)
        print(json.dumps(draft.__dict__, ensure_ascii=False, indent=2))
        return 0

    if args.command == "list-memories":
        records = [record.__dict__ for record in runtime.list_memories(args.user_id)]
        print(json.dumps(records, ensure_ascii=False, indent=2))
        return 0

    if args.command == "report":
        print(runtime.generate_report(args.user_id))
        return 0

    if args.command == "delete-memory":
        runtime.delete_memory(args.user_id, args.draft_id)
        print("Deleted if it existed.")
        return 0

    raise AssertionError(f"Unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
