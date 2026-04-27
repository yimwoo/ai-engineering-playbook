"""Validate README-promised starter-kit and example file sets.

Canonical test command:
    python3 -m unittest tests.test_validate_playbook
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
import re
import sys


@dataclass(frozen=True)
class StructureCheck:
    """One documented starter-kit or example expectation."""

    name: str
    root: str
    required_entries: tuple[str, ...]


@dataclass(frozen=True)
class RelativeLinkCheck:
    """One markdown file whose high-signal relative links should resolve."""

    source: str


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

RELATIVE_LINK_CHECKS: tuple[RelativeLinkCheck, ...] = (
    RelativeLinkCheck(source="README.md"),
    RelativeLinkCheck(source="docs/getting-started.md"),
    RelativeLinkCheck(source="docs/prompts.md"),
)

MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def _entry_exists(base_dir: Path, entry: str) -> bool:
    path = base_dir / entry.rstrip("/")
    if entry.endswith("/"):
        return path.is_dir()
    return path.is_file()


def _normalize_link_target(target: str) -> str:
    normalized = target.strip()
    if normalized.startswith("<") and normalized.endswith(">"):
        normalized = normalized[1:-1].strip()
    return normalized


def _is_relative_link_target(target: str) -> bool:
    return not (
        "://" in target
        or target.startswith("#")
        or target.startswith("mailto:")
    )


def iter_relative_link_targets(markdown_text: str) -> tuple[str, ...]:
    """Extract relative markdown link targets from one markdown document."""

    targets: list[str] = []
    for match in MARKDOWN_LINK_PATTERN.finditer(markdown_text):
        target = _normalize_link_target(match.group(1))
        if _is_relative_link_target(target):
            targets.append(target)
    return tuple(targets)


def iter_tracked_paths(root: Path) -> tuple[str, ...]:
    """Return deterministic relative file paths underneath one repo subtree."""

    return tuple(
        str(path.relative_to(root))
        for path in sorted(path for path in root.rglob("*") if path.is_file())
    )


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


def validate_relative_link_check(
    repo_root: Path,
    check: RelativeLinkCheck,
) -> list[str]:
    """Return validation errors for one markdown file's relative links."""

    source_path = repo_root / check.source
    if not source_path.is_file():
        return [f"relative links: missing source `{check.source}`"]

    source_text = source_path.read_text(encoding="utf-8")
    errors: list[str] = []

    for target in iter_relative_link_targets(source_text):
        target_path_text, _, _fragment = target.partition("#")
        resolved_path = (source_path.parent / target_path_text).resolve()

        if target_path_text.endswith("/"):
            exists = resolved_path.is_dir()
        else:
            exists = resolved_path.is_file()

        if not exists:
            errors.append(
                f"relative links: `{check.source}` -> `{target}` is missing"
            )

    return errors


def validate_playbook(repo_root: Path | None = None) -> list[str]:
    """Return all starter-kit/example and high-signal link validation errors."""

    resolved_root = repo_root or Path(__file__).resolve().parents[1]
    errors: list[str] = []
    for check in CHECKS:
        errors.extend(validate_structure_check(resolved_root, check))
    for check in RELATIVE_LINK_CHECKS:
        errors.extend(validate_relative_link_check(resolved_root, check))
    return errors


def generate_inventory(repo_root: Path | None = None) -> dict[str, object]:
    """Build a deterministic machine-readable inventory for key repo assets."""

    resolved_root = repo_root or Path(__file__).resolve().parents[1]
    prompts_dir = resolved_root / "prompts"
    templates_dir = resolved_root / "templates"
    starter_kits_dir = resolved_root / "starter-kits"
    examples_dir = resolved_root / "examples"

    starter_kits = []
    for path in sorted(path for path in starter_kits_dir.iterdir() if path.is_dir()):
        starter_kits.append(
            {
                "name": path.name,
                "path": str(path.relative_to(resolved_root)),
                "files": iter_tracked_paths(path),
            }
        )

    examples = []
    for path in sorted(path for path in examples_dir.iterdir() if path.is_dir()):
        examples.append(
            {
                "name": path.name,
                "path": str(path.relative_to(resolved_root)),
                "files": iter_tracked_paths(path),
            }
        )

    return {
        "prompts": tuple(
            str(path.relative_to(resolved_root))
            for path in sorted(path for path in prompts_dir.iterdir() if path.is_file())
        ),
        "templates": tuple(
            str(path.relative_to(resolved_root))
            for path in sorted(path for path in templates_dir.iterdir() if path.is_file())
        ),
        "starter_kits": starter_kits,
        "examples": examples,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse the validator CLI arguments."""

    parser = argparse.ArgumentParser(
        description=(
            "Validate documented playbook structure and optionally export a "
            "machine-readable inventory."
        )
    )
    parser.add_argument(
        "--inventory-out",
        type=Path,
        help="Write the generated inventory JSON to this path.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    errors = validate_playbook()
    if errors:
        print("playbook validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    if args.inventory_out is not None:
        inventory = generate_inventory()
        args.inventory_out.parent.mkdir(parents=True, exist_ok=True)
        args.inventory_out.write_text(
            json.dumps(inventory, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"wrote inventory to `{args.inventory_out}`")

    print(
        "playbook validation passed for starter-kits, examples, and selected links. "
        "Run `python3 -m unittest tests.test_validate_playbook` for regression tests."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
