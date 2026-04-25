"""Validate README-promised starter-kit and example file sets.

Canonical test command:
    python3 -m unittest tests.test_validate_playbook
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys


@dataclass(frozen=True)
class StructureCheck:
    """One documented starter-kit or example expectation."""

    name: str
    root: str
    required_entries: tuple[str, ...]


CHECKS: tuple[StructureCheck, ...] = (
    StructureCheck(
        name="lightweight starter kit",
        root="starter-kits/lightweight",
        required_entries=(
            "PROJECT_CONSTITUTION.md",
            "CLAUDE.md",
            "architecture.md",
            "status.md",
        ),
    ),
    StructureCheck(
        name="standard starter kit",
        root="starter-kits/standard",
        required_entries=(
            "PROJECT_CONSTITUTION.md",
            "CLAUDE.md",
            "architecture.md",
            "roadmap.md",
            "status.md",
            "technical-debt.md",
            "modules/",
            "decisions/",
        ),
    ),
    StructureCheck(
        name="enterprise starter kit",
        root="starter-kits/enterprise",
        required_entries=(
            "PROJECT_CONSTITUTION.md",
            "CLAUDE.md",
            "AGENTS.md",
            "architecture.md",
            "repo-map.md",
            "roadmap.md",
            "status.md",
            "technical-debt.md",
            "modules/",
            "decisions/",
            "task-packets/",
            "handoffs/",
        ),
    ),
    StructureCheck(
        name="startup lightweight example",
        root="examples/startup-lightweight",
        required_entries=(
            "CLAUDE.md",
            "architecture.md",
            "status.md",
        ),
    ),
    StructureCheck(
        name="enterprise product example",
        root="examples/enterprise-product",
        required_entries=(
            "PROJECT_CONSTITUTION.md",
            "CLAUDE.md",
            "AGENTS.md",
            "architecture.md",
            "roadmap.md",
            "status.md",
            "technical-debt.md",
            "modules/",
            "decisions/",
            "task-packets/",
            "handoffs/",
        ),
    ),
    StructureCheck(
        name="existing repo migration example",
        root="examples/existing-repo-migration",
        required_entries=(
            "PROJECT_CONSTITUTION.md",
            "CLAUDE.md",
            "status.md",
            "alignment-plan.md",
        ),
    ),
)


def _entry_exists(base_dir: Path, entry: str) -> bool:
    path = base_dir / entry.rstrip("/")
    if entry.endswith("/"):
        return path.is_dir()
    return path.is_file()


def validate_structure_check(repo_root: Path, check: StructureCheck) -> list[str]:
    """Return validation errors for one documented structure check."""

    base_dir = repo_root / check.root
    if not base_dir.is_dir():
        return [f"{check.name}: missing directory `{check.root}`"]

    errors: list[str] = []
    for entry in check.required_entries:
        if not _entry_exists(base_dir, entry):
            errors.append(
                f"{check.name}: missing `{entry}` in `{check.root}`"
            )
    return errors


def validate_playbook(repo_root: Path | None = None) -> list[str]:
    """Return all starter-kit and example validation errors."""

    resolved_root = repo_root or Path(__file__).resolve().parents[1]
    errors: list[str] = []
    for check in CHECKS:
        errors.extend(validate_structure_check(resolved_root, check))
    return errors


def main() -> int:
    errors = validate_playbook()
    if errors:
        print("playbook validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "playbook validation passed for starter-kits and examples. "
        "Run `python3 -m unittest tests.test_validate_playbook` for regression tests."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
