"""Run the canonical playbook automation check.

Canonical command:
    python3 tools/run_playbook_check.py
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys


DEFAULT_INVENTORY_PATH = Path(".agent/artifacts/playbook-inventory.json")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments for the canonical playbook check."""

    parser = argparse.ArgumentParser(
        description=(
            "Run the canonical playbook regression check and export the "
            "machine-readable inventory."
        )
    )
    parser.add_argument(
        "--inventory-out",
        type=Path,
        default=DEFAULT_INVENTORY_PATH,
        help=(
            "Write the generated inventory JSON to this path after the "
            "regression tests pass."
        ),
    )
    return parser.parse_args(argv)


def run_command(command: list[str]) -> int:
    """Run one subprocess command and return its exit code."""

    print(f"running: {' '.join(command)}")
    completed = subprocess.run(command, check=False)
    return completed.returncode


def main(argv: list[str] | None = None) -> int:
    """Run the regression tests, then write the inventory artifact."""

    args = parse_args(argv)
    checks = (
        [sys.executable, "-m", "unittest", "tests.test_validate_playbook"],
        [
            sys.executable,
            "tools/validate_playbook.py",
            "--inventory-out",
            str(args.inventory_out),
        ],
    )

    for command in checks:
        exit_code = run_command(command)
        if exit_code != 0:
            return exit_code

    print(f"playbook check passed; inventory written to `{args.inventory_out}`")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
