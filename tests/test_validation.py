from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

from scripts.validate_examples import validate_examples


ROOT = Path(__file__).resolve().parents[1]


class ValidationTests(unittest.TestCase):
    def test_examples_validate_cleanly(self) -> None:
        results, global_errors = validate_examples()
        self.assertEqual(len(results), 8)
        self.assertFalse(global_errors)
        self.assertTrue(all(result.status == "PASS" for result in results))

    def test_validation_script_runs(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate_examples.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("All example files and supersession links are valid.", result.stdout)

    def test_validation_results_snapshot_is_in_sync(self) -> None:
        subprocess.run(
            [sys.executable, "scripts/generate_validation_results.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        tracked = (ROOT / "VALIDATION_RESULTS.md").read_text(encoding="utf-8")
        self.assertIn("# DMP Validation Results", tracked)
        self.assertIn("Global consistency errors: **0**", tracked)


if __name__ == "__main__":
    unittest.main()
