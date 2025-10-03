#!/usr/bin/env python3
"""Smoke checks for critical CLI scripts.

The harness focuses on zero-side-effect invocations (``--help``) so it can run
in sterile CI environments without requiring the heavy generator toolchain or
policy assets.  It is intentionally small and easily extensible: append entries
in :data:`SMOKE_TARGETS` to cover additional scripts.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / "scripts"
PYTHON = sys.executable or "python3"


@dataclass(frozen=True)
class SmokeTarget:
    name: str
    command: Sequence[str]

    def run(self, cwd: Path, verbose: bool = False) -> subprocess.CompletedProcess[str]:
        if verbose:
            print(f"[RUN] {' '.join(self.command)} (cwd={cwd})")
        return subprocess.run(
            self.command,
            cwd=cwd,
            check=False,
            text=True,
            capture_output=True,
        )


SMOKE_TARGETS: tuple[SmokeTarget, ...] = (
    SmokeTarget(
        name="rules_audit_quick_help",
        command=(PYTHON, str(SCRIPTS_DIR / "rules_audit_quick.py"), "--help"),
    ),
    SmokeTarget(
        name="test_policy_decisions_help",
        command=(PYTHON, str(SCRIPTS_DIR / "test_policy_decisions.py"), "--help"),
    ),
)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--filter",
        nargs="*",
        help="Optional substrings to select a subset of smoke targets.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print commands before executing them.",
    )
    parser.add_argument(
        "--fail-fast",
        action="store_true",
        help="Stop after the first failing smoke command.",
    )
    return parser.parse_args(argv)


def _select_targets(filters: Iterable[str] | None) -> list[SmokeTarget]:
    if not filters:
        return list(SMOKE_TARGETS)
    selected: list[SmokeTarget] = []
    for target in SMOKE_TARGETS:
        if any(substr in target.name for substr in filters):
            selected.append(target)
    return selected


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    targets = _select_targets(args.filter)
    if not targets:
        print("No smoke targets selected.")
        return 0

    failures = 0
    for target in targets:
        result = target.run(REPO_ROOT, verbose=args.verbose)
        if result.returncode != 0:
            failures += 1
            print(f"[FAIL] {target.name} -> exit={result.returncode}")
            if result.stdout:
                print("stdout:\n" + result.stdout)
            if result.stderr:
                print("stderr:\n" + result.stderr)
            if args.fail_fast:
                break
        else:
            print(f"[PASS] {target.name}")
    if failures:
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
