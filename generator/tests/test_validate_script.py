"""Ensure task-level validation retains diagnostic collection and failure exits."""

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/validate.sh"
FAKE_PYTHON = '''#!/bin/sh
printf '%s\\n' "$*" >> "$CALL_LOG"
case "$*" in
  *"$FAIL_MATCH"*) if [ -n "$FAIL_MATCH" ]; then exit 1; fi ;;
esac
'''
FAKE_WIRETAP = 'shift; exec "$@"\n'


class ValidationTaskTests(unittest.TestCase):
    def run_mode(self, mode, failure=""):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            command = root / "python"
            command.write_text(FAKE_PYTHON)
            command.chmod(0o755)
            log = root / "calls"
            wiretap = root / "wiretap.sh"
            wiretap.write_text(FAKE_WIRETAP)
            environment = {
                **os.environ,
                "PATH": f"{root}{os.pathsep}{os.environ['PATH']}",
                "CALL_LOG": str(log),
                "FAIL_MATCH": failure,
                "WIRETAP_SH": str(wiretap),
            }
            bash = shutil.which("bash")
            self.assertIsNotNone(bash)
            result = subprocess.run(  # noqa: S603 - fixed script and owned fake interpreter
                [bash, str(SCRIPT), mode],
                env=environment,
                capture_output=True,
                text=True,
            )
            calls = log.read_text().splitlines() if log.exists() else []
            return result, calls

    def test_granular_modes_run_only_the_selected_layer(self):
        for mode, expected in [
            ("preprocess", "discover"),
            ("unit", "tests.test_sdk_smoke"),
            ("endpoints", "check_endpoint_coverage.py"),
            ("wiretap", "tests.test_wiretap"),
        ]:
            with self.subTest(mode=mode):
                result, calls = self.run_mode(mode)
                self.assertEqual(result.returncode, 0)
                self.assertEqual(len(calls), 1)
                self.assertIn(expected, calls[0])

    def test_quick_failure_does_not_skip_later_checks(self):
        result, calls = self.run_mode("quick", failure="discover")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(len(calls), 3)
        self.assertIn("check_endpoint_coverage", calls[-1])

    def test_all_runs_wiretap_even_after_quick_failure(self):
        result, calls = self.run_mode("all", failure="check_endpoint_coverage")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(len(calls), 4)
        self.assertIn("tests.test_wiretap", calls[-1])

    def test_wiretap_failure_is_not_swallowed(self):
        result, calls = self.run_mode("all", failure="tests.test_wiretap")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(len(calls), 4)

    def test_unknown_mode_fails_without_running_python(self):
        result, calls = self.run_mode("unknown")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Usage:", result.stderr)
        self.assertEqual(calls, [])
