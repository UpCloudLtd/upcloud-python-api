"""Test live-example dispatch with a fake mdtest; never calls UpCloud."""

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "generator/scripts/run_examples.sh"
TOKEN = "test-token"  # noqa: S105 - fake credential
FAKE_MDTEST = """#!/bin/sh
printf '%s|%s|%s|%s\\n' "$1" "$PWD" "$UPCLOUD_SDK_PATH" "$UPCLOUD_TOKEN" >> "$CALL_LOG"
case "$1" in *"$FAIL_MATCH"*) [ -n "$FAIL_MATCH" ] && exit 1 ;; esac
exit 0
"""


class ExampleTaskTests(unittest.TestCase):
    def run_script(self, *names, token=TOKEN, mdtest=True, fail=""):
        with tempfile.TemporaryDirectory() as directory:
            bin_dir = Path(directory)
            log = bin_dir / "calls"
            if mdtest:
                fake = bin_dir / "mdtest"
                fake.write_text(FAKE_MDTEST)
                fake.chmod(0o755)
            environment = {
                "PATH": str(bin_dir),
                "CALL_LOG": str(log),
                "FAIL_MATCH": fail,
                "UPCLOUD_SDK_PATH": "/wrong",
            }
            if token is not None:
                environment["UPCLOUD_TOKEN"] = token
            bash = shutil.which("bash")
            self.assertIsNotNone(bash)
            result = subprocess.run(  # noqa: S603 - fixed script and owned fake mdtest
                [bash, str(SCRIPT), *names],
                cwd=directory,
                env=environment,
                capture_output=True,
                text=True,
            )
            calls = log.read_text().splitlines() if log.exists() else []
            return result, calls

    def test_missing_token_never_calls_mdtest(self):
        result, calls = self.run_script("tag", token=None)
        self.assertEqual(result.returncode, 1)
        self.assertIn("UPCLOUD_TOKEN", result.stderr)
        self.assertEqual(calls, [])

    def test_missing_mdtest_fails(self):
        result, _ = self.run_script("tag", mdtest=False)
        self.assertEqual(result.returncode, 1)
        self.assertIn("mdtest", result.stderr)

    def test_names_run_in_order_with_local_sdk_and_stop_at_first_failure(self):
        names = ["file-storage", "object-storage", "tag", "kubernetes"]
        result, calls = self.run_script(*names)
        self.assertEqual(result.returncode, 0, result.stderr)
        expected = [
            f"{ROOT}/examples/{name}/test_{name.replace('-', '_')}.md|{ROOT}|{ROOT}|test-token"
            for name in names
        ]
        self.assertEqual(calls, expected)
        self.assertNotIn("test-token", result.stdout + result.stderr)

        result, calls = self.run_script(*names, fail="test_object_storage")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(calls, expected[:2])

    def test_unknown_or_unsafe_name_is_rejected(self):
        for name in ["unknown", "../x"]:
            with self.subTest(name=name):
                result, calls = self.run_script(name)
                self.assertEqual(result.returncode, 2)
                self.assertIn("Usage:", result.stderr)
                self.assertEqual(calls, [])
