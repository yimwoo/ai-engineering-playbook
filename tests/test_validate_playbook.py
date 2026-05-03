from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path
import unittest
from unittest import mock

from tools.validate_playbook import (
    CHECKS,
    RELATIVE_LINK_CHECKS,
    generate_inventory,
    iter_relative_link_targets,
    iter_tracked_paths,
    main,
    validate_playbook,
    validate_relative_link_check,
    validate_structure_check,
)
from tools.run_playbook_check import DEFAULT_INVENTORY_PATH, main as run_playbook_check_main


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_PATH = REPO_ROOT / ".github/workflows/playbook-check.yml"


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

    def test_iter_tracked_paths_returns_sorted_relative_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            (root / "b.md").write_text("b\n", encoding="utf-8")
            (root / "nested").mkdir()
            (root / "nested" / "a.md").write_text("a\n", encoding="utf-8")

            self.assertEqual(
                iter_tracked_paths(root),
                ("b.md", "nested/a.md"),
            )

    def test_inventory_contains_expected_top_level_assets(self) -> None:
        inventory = generate_inventory(REPO_ROOT)

        self.assertEqual(inventory["prompts"][0], "prompts/architecture-analysis.md")
        self.assertIn("templates/AGENTS.md", inventory["templates"])
        self.assertEqual(
            [item["name"] for item in inventory["starter_kits"]],
            ["enterprise", "lightweight", "standard"],
        )
        self.assertEqual(
            [item["name"] for item in inventory["examples"]],
            [
                "enterprise-product",
                "existing-repo-migration",
                "startup-lightweight",
            ],
        )
        self.assertIn(
            "handoffs/_template.md",
            inventory["starter_kits"][0]["files"],
        )

    def test_main_writes_inventory_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_path = Path(tmp_dir) / "inventory.json"

            exit_code = main(["--inventory-out", str(output_path)])

            self.assertEqual(exit_code, 0)
            self.assertTrue(output_path.is_file())
            inventory = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertIn("prompts/review-task.md", inventory["prompts"])
            self.assertEqual(
                inventory["examples"][0]["path"],
                "examples/enterprise-product",
            )

    def test_workflow_runs_canonical_wrapper_command(self) -> None:
        workflow_text = WORKFLOW_PATH.read_text(encoding="utf-8")

        self.assertIn(
            (
                "run: python3 tools/run_playbook_check.py --inventory-out "
                f"{DEFAULT_INVENTORY_PATH}"
            ),
            workflow_text,
        )

    def test_workflow_triggers_on_push_and_pull_request(self) -> None:
        workflow_text = WORKFLOW_PATH.read_text(encoding="utf-8")

        self.assertIn("on:\n  pull_request:\n  push:\n", workflow_text)

    def test_workflow_pins_python_3_11(self) -> None:
        workflow_text = WORKFLOW_PATH.read_text(encoding="utf-8")

        self.assertIn('python-version: "3.11"', workflow_text)

    def test_workflow_uploads_expected_inventory_artifact(self) -> None:
        workflow_text = WORKFLOW_PATH.read_text(encoding="utf-8")

        self.assertIn("name: playbook-inventory", workflow_text)
        self.assertIn(f"path: {DEFAULT_INVENTORY_PATH}", workflow_text)

    @mock.patch("tools.run_playbook_check.subprocess.run")
    def test_run_playbook_check_uses_default_inventory_path(self, run_mock: mock.Mock) -> None:
        run_mock.return_value.returncode = 0

        exit_code = run_playbook_check_main([])

        self.assertEqual(exit_code, 0)
        self.assertEqual(
            [call.args[0] for call in run_mock.call_args_list],
            [
                [sys.executable, "-m", "unittest", "tests.test_validate_playbook"],
                [
                    sys.executable,
                    "tools/validate_playbook.py",
                    "--inventory-out",
                    str(DEFAULT_INVENTORY_PATH),
                ],
            ],
        )

    @mock.patch("tools.run_playbook_check.subprocess.run")
    def test_run_playbook_check_stops_after_first_failure(self, run_mock: mock.Mock) -> None:
        run_mock.return_value.returncode = 1

        exit_code = run_playbook_check_main([])

        self.assertEqual(exit_code, 1)
        self.assertEqual(
            [call.args[0] for call in run_mock.call_args_list],
            [[sys.executable, "-m", "unittest", "tests.test_validate_playbook"]],
        )


if __name__ == "__main__":
    unittest.main()
