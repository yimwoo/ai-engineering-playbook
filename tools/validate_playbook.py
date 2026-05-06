"""Validate README-promised playbook assets and packaging.

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

CLAUDE_PLUGIN_NAME = "ai-engineering-playbook"
CLAUDE_MARKETPLACE_PATH = ".claude-plugin/marketplace.json"
CLAUDE_PLUGIN_ROOT = "plugins/ai-engineering-playbook"
CLAUDE_PLUGIN_SKILLS: tuple[str, ...] = (
    "adopting-playbook",
    "orchestrating-playbook-work",
    "planning-playbook-tasks",
    "implementing-playbook-tasks",
    "reviewing-playbook-work",
)

MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
SKILL_FRONTMATTER_PATTERN = re.compile(r"\A---\n(.*?)\n---(?:\n|$)", re.DOTALL)
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RESERVED_SKILL_NAME_TERMS = ("anthropic", "claude")


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


def _load_json_object(
    path: Path,
    label: str,
) -> tuple[dict[str, object] | None, list[str]]:
    if not path.is_file():
        return None, [f"{label}: missing `{path}`"]

    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return None, [f"{label}: invalid JSON in `{path}`: {exc.msg}"]

    if not isinstance(parsed, dict):
        return None, [f"{label}: `{path}` must contain a JSON object"]

    return parsed, []


def _parse_skill_frontmatter(
    skill_path: Path,
) -> tuple[dict[str, str], list[str]]:
    text = skill_path.read_text(encoding="utf-8")
    match = SKILL_FRONTMATTER_PATTERN.match(text)
    if match is None:
        return {}, [f"claude plugin: missing frontmatter in `{skill_path}`"]

    fields: dict[str, str] = {}
    errors: list[str] = []
    for line in match.group(1).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            errors.append(
                f"claude plugin: invalid frontmatter line in `{skill_path}`"
            )
            continue
        key, value = stripped.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')

    return fields, errors


def _validate_skill_name(name: str, path: Path) -> list[str]:
    errors: list[str] = []
    if SKILL_NAME_PATTERN.fullmatch(name) is None:
        errors.append(f"claude plugin: skill name `{name}` is not kebab-case")
    for term in RESERVED_SKILL_NAME_TERMS:
        if term in name:
            errors.append(
                f"claude plugin: skill name `{name}` uses reserved term `{term}`"
            )
    if len(name) > 64:
        errors.append(f"claude plugin: skill name `{name}` is too long")
    if not path.parent.name == name:
        errors.append(
            f"claude plugin: skill `{path}` must live under a matching directory"
        )
    return errors


def validate_claude_plugin_package(repo_root: Path) -> list[str]:
    """Return validation errors for the bundled Claude Code plugin package."""

    errors: list[str] = []
    marketplace_path = repo_root / CLAUDE_MARKETPLACE_PATH
    marketplace, marketplace_errors = _load_json_object(
        marketplace_path,
        "claude plugin marketplace",
    )
    errors.extend(marketplace_errors)

    if marketplace is not None:
        if marketplace.get("name") != CLAUDE_PLUGIN_NAME:
            errors.append(
                "claude plugin marketplace: expected name "
                f"`{CLAUDE_PLUGIN_NAME}`"
            )

        plugins = marketplace.get("plugins")
        if not isinstance(plugins, list):
            errors.append("claude plugin marketplace: `plugins` must be a list")
        else:
            matching_plugins = [
                item
                for item in plugins
                if isinstance(item, dict)
                and item.get("name") == CLAUDE_PLUGIN_NAME
            ]
            if not matching_plugins:
                errors.append(
                    "claude plugin marketplace: missing plugin "
                    f"`{CLAUDE_PLUGIN_NAME}`"
                )
            else:
                expected_source = f"./{CLAUDE_PLUGIN_ROOT}"
                source = matching_plugins[0].get("source")
                if source != expected_source:
                    errors.append(
                        "claude plugin marketplace: expected plugin source "
                        f"`{expected_source}`"
                    )

    plugin_root = repo_root / CLAUDE_PLUGIN_ROOT
    manifest_path = plugin_root / ".claude-plugin" / "plugin.json"
    manifest, manifest_errors = _load_json_object(
        manifest_path,
        "claude plugin manifest",
    )
    errors.extend(manifest_errors)

    if manifest is not None:
        if manifest.get("name") != CLAUDE_PLUGIN_NAME:
            errors.append(
                "claude plugin manifest: expected name "
                f"`{CLAUDE_PLUGIN_NAME}`"
            )
        if not manifest.get("description"):
            errors.append("claude plugin manifest: missing `description`")
        if not manifest.get("version"):
            errors.append("claude plugin manifest: missing `version`")

    readme_path = plugin_root / "README.md"
    if not readme_path.is_file():
        errors.append(f"claude plugin: missing `{readme_path}`")

    for skill_name in CLAUDE_PLUGIN_SKILLS:
        skill_path = plugin_root / "skills" / skill_name / "SKILL.md"
        reference_path = plugin_root / "skills" / skill_name / "reference.md"

        if not skill_path.is_file():
            errors.append(f"claude plugin: missing `{skill_path}`")
            continue
        if not reference_path.is_file():
            errors.append(f"claude plugin: missing `{reference_path}`")

        errors.extend(_validate_skill_name(skill_name, skill_path))
        fields, frontmatter_errors = _parse_skill_frontmatter(skill_path)
        errors.extend(frontmatter_errors)

        if fields.get("name") != skill_name:
            errors.append(
                f"claude plugin: `{skill_path}` frontmatter `name` must be "
                f"`{skill_name}`"
            )

        description = fields.get("description", "")
        if len(description) < 40:
            errors.append(
                f"claude plugin: `{skill_path}` frontmatter `description` "
                "is too short"
            )
        if len(description) > 1024:
            errors.append(
                f"claude plugin: `{skill_path}` frontmatter `description` "
                "is too long"
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
    errors.extend(validate_claude_plugin_package(resolved_root))
    return errors


def generate_inventory(repo_root: Path | None = None) -> dict[str, object]:
    """Build a deterministic machine-readable inventory for key repo assets."""

    resolved_root = repo_root or Path(__file__).resolve().parents[1]
    prompts_dir = resolved_root / "prompts"
    templates_dir = resolved_root / "templates"
    starter_kits_dir = resolved_root / "starter-kits"
    examples_dir = resolved_root / "examples"
    plugins_dir = resolved_root / "plugins"

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

    claude_plugins = []
    if plugins_dir.is_dir():
        for path in sorted(path for path in plugins_dir.iterdir() if path.is_dir()):
            claude_plugins.append(
                {
                    "name": path.name,
                    "path": str(path.relative_to(resolved_root)),
                    "files": iter_tracked_paths(path),
                }
            )

    return {
        "claude_plugin_marketplace": CLAUDE_MARKETPLACE_PATH,
        "claude_plugins": claude_plugins,
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
        "playbook validation passed for starter-kits, examples, selected links, "
        "and the Claude Code plugin package. Run `python3 -m unittest "
        "tests.test_validate_playbook` for regression tests."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
