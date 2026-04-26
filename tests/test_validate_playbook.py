from __future__ import annotations

import tempfile
from pathlib import Path
import unittest

from tools.validate_playbook import (
    CHECKS,
    RELATIVE_LINK_CHECKS,
    iter_relative_link_targets,
    validate_playbook,
    validate_relative_link_check,
    validate_structure_check,
)


REPO_ROOT = Path(__file__).resolve().parents[1]


class ValidatePlaybookTest(unittest.TestCase):
    def test_each_documented_structure_passes_in_repo(self) -> None:
        for check in CHECKS:
            with self.subTest(check=check.name):
                self.assertEqual(validate_structure_check(REPO_ROOT, check), [])

    def test_each_high_signal_link_source_passes_in_repo(self) -> None:
        for check in RELATIVE_LINK_CHECKS:
            with self.subTest(source=check.source):
                self.assertEqual(validate_relative_link_check(REPO_ROOT, check), [])

    def test_repo_validation_passes(self) -> None:
        self.assertEqual(validate_playbook(REPO_ROOT), [])

    def test_relative_link_target_extraction_skips_external_links(self) -> None:
        markdown = "\n".join(
            (
                "[Doc](docs/overview.md)",
                "[Dir](starter-kits/lightweight/)",
                "[Anchor](#local-heading)",
                "[External](https://example.com/docs)",
                "[Mail](mailto:test@example.com)",
            )
        )

        self.assertEqual(
            iter_relative_link_targets(markdown),
            ("docs/overview.md", "starter-kits/lightweight/"),
        )

    def test_missing_entry_reports_named_failure(self) -> None:
        check = CHECKS[2]
        with tempfile.TemporaryDirectory() as tmp_dir:
            repo_root = Path(tmp_dir)
            base_dir = repo_root / check.root
            base_dir.mkdir(parents=True)
            for entry in check.required_entries:
                path = base_dir / entry.rstrip("/")
                if entry.endswith("/"):
                    path.mkdir(parents=True)
                else:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text("placeholder\n", encoding="utf-8")

            missing_path = base_dir / "task-packets"
            missing_path.rmdir()

            self.assertEqual(
                validate_structure_check(repo_root, check),
                [
                    "enterprise starter kit: missing `task-packets/` in "
                    "`starter-kits/enterprise`"
                ],
            )

    def test_missing_relative_link_reports_source_and_target(self) -> None:
        check = RELATIVE_LINK_CHECKS[1]
        with tempfile.TemporaryDirectory() as tmp_dir:
            repo_root = Path(tmp_dir)
            source_path = repo_root / check.source
            source_path.parent.mkdir(parents=True)
            source_path.write_text(
                "[Good](../prompts/repo-audit.md)\n"
                "[Missing](../prompts/missing.md)\n"
                "[Anchored](../prompts/status-update.md#usage)\n",
                encoding="utf-8",
            )

            prompts_dir = repo_root / "prompts"
            prompts_dir.mkdir()
            (prompts_dir / "repo-audit.md").write_text("placeholder\n", encoding="utf-8")
            (prompts_dir / "status-update.md").write_text(
                "placeholder\n",
                encoding="utf-8",
            )

            self.assertEqual(
                validate_relative_link_check(repo_root, check),
                [
                    "relative links: `docs/getting-started.md` -> "
                    "`../prompts/missing.md` is missing"
                ],
            )


if __name__ == "__main__":
    unittest.main()
