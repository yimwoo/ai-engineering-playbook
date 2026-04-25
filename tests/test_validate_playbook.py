from __future__ import annotations

import tempfile
from pathlib import Path
import unittest

from tools.validate_playbook import CHECKS, validate_playbook, validate_structure_check


REPO_ROOT = Path(__file__).resolve().parents[1]


class ValidatePlaybookTest(unittest.TestCase):
    def test_each_documented_structure_passes_in_repo(self) -> None:
        for check in CHECKS:
            with self.subTest(check=check.name):
                self.assertEqual(validate_structure_check(REPO_ROOT, check), [])

    def test_repo_validation_passes(self) -> None:
        self.assertEqual(validate_playbook(REPO_ROOT), [])

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


if __name__ == "__main__":
    unittest.main()
