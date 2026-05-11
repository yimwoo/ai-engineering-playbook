from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path
import unittest
from unittest import mock

from tools.validate_playbook import (
    CHECKS,
    CLAUDE_MARKETPLACE_PATH,
    CLAUDE_PLUGIN_NAME,
    CLAUDE_PLUGIN_ROOT,
    CLAUDE_PLUGIN_SKILLS,
    RELATIVE_LINK_CHECKS,
    generate_inventory,
    iter_relative_link_targets,
    iter_tracked_paths,
    main,
    validate_claude_plugin_package,
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

    def test_claude_code_plugin_package_passes_in_repo(self) -> None:
        self.assertEqual(validate_claude_plugin_package(REPO_ROOT), [])

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
        self.assertEqual(
            inventory["claude_plugin_marketplace"],
            CLAUDE_MARKETPLACE_PATH,
        )
        claude_plugin = next(
            item
            for item in inventory["claude_plugins"]
            if item["name"] == CLAUDE_PLUGIN_NAME
        )
        self.assertEqual(claude_plugin["path"], CLAUDE_PLUGIN_ROOT)
        self.assertIn(
            ".claude-plugin/plugin.json",
            claude_plugin["files"],
        )
        self.assertIn(
            "skills/adopting-playbook/SKILL.md",
            claude_plugin["files"],
        )

    def test_missing_claude_plugin_skill_reference_reports_failure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            repo_root = Path(tmp_dir)
            marketplace_path = repo_root / CLAUDE_MARKETPLACE_PATH
            marketplace_path.parent.mkdir(parents=True)
            marketplace_path.write_text(
                json.dumps(
                    {
                        "name": CLAUDE_PLUGIN_NAME,
                        "plugins": [
                            {
                                "name": CLAUDE_PLUGIN_NAME,
                                "source": f"./{CLAUDE_PLUGIN_ROOT}",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )

            plugin_root = repo_root / CLAUDE_PLUGIN_ROOT
            manifest_path = plugin_root / ".claude-plugin" / "plugin.json"
            manifest_path.parent.mkdir(parents=True)
            manifest_path.write_text(
                json.dumps(
                    {
                        "name": CLAUDE_PLUGIN_NAME,
                        "description": "Test plugin",
                        "version": "0.1.0",
                    }
                ),
                encoding="utf-8",
            )
            (plugin_root / "README.md").write_text("Plugin README\n", encoding="utf-8")

            for skill_name in CLAUDE_PLUGIN_SKILLS:
                skill_dir = plugin_root / "skills" / skill_name
                skill_dir.mkdir(parents=True)
                skill_dir.joinpath("SKILL.md").write_text(
                    "\n".join(
                        (
                            "---",
                            f"name: {skill_name}",
                            (
                                "description: A focused test description for "
                                "validating Claude Code skill frontmatter."
                            ),
                            "---",
                            "",
                            "# Skill",
                        )
                    ),
                    encoding="utf-8",
                )
                skill_dir.joinpath("reference.md").write_text(
                    "# Reference\n",
                    encoding="utf-8",
                )

            missing_reference = (
                plugin_root
                / "skills"
                / CLAUDE_PLUGIN_SKILLS[0]
                / "reference.md"
            )
            missing_reference.unlink()

            errors = validate_claude_plugin_package(repo_root)

            self.assertIn(
                f"claude plugin: missing `{missing_reference}`",
                errors,
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

    def test_workflow_runs_on_ubuntu_latest(self) -> None:
        workflow_text = WORKFLOW_PATH.read_text(encoding="utf-8")

        self.assertIn("runs-on: ubuntu-latest", workflow_text)

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
    def test_run_playbook_check_forwards_custom_inventory_path(
        self, run_mock: mock.Mock
    ) -> None:
        run_mock.return_value.returncode = 0
        custom_inventory_path = Path(".agent/custom/inventory.json")

        exit_code = run_playbook_check_main(
            ["--inventory-out", str(custom_inventory_path)]
        )

        self.assertEqual(exit_code, 0)
        self.assertEqual(
            [call.args[0] for call in run_mock.call_args_list],
            [
                [sys.executable, "-m", "unittest", "tests.test_validate_playbook"],
                [
                    sys.executable,
                    "tools/validate_playbook.py",
                    "--inventory-out",
                    str(custom_inventory_path),
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

    @mock.patch("tools.run_playbook_check.subprocess.run")
    def test_run_playbook_check_runs_inventory_generation_after_tests(
        self, run_mock: mock.Mock
    ) -> None:
        run_mock.side_effect = (
            mock.Mock(returncode=0),
            mock.Mock(returncode=1),
        )

        exit_code = run_playbook_check_main([])

        self.assertEqual(exit_code, 1)
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


if __name__ == "__main__":
    unittest.main()
