"""Test the release asset downloader offline with a fake curl and real tar/jq."""

import io
import os
import shutil
import subprocess
import tarfile
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/download_spec.sh"
URL = "https://api.github.com/repos/UpCloudLtd/spec/releases/assets/123"
SPEC_FILE = "upcloud-public-openapi.json"
SPEC = b'{\n "openapi": "3.1.0", "info": {"version": "different"}, "paths": {}\n}\n'
TOKEN = "private-test-token"  # noqa: S105 - fake credential
FAKE_CURL = """#!/bin/sh
printf '%s\\n' "$@" > "$CURL_ARGS"
cat > "$CURL_STDIN"
while [ "$#" -gt 0 ]; do
  if [ "$1" = -o ]; then out="$2"; fi
  shift
done
if [ "$CURL_EXIT" != 0 ]; then
  echo "curl: (22) The requested URL returned error: 404" >&2
  exit "$CURL_EXIT"
fi
cp "$FIXTURE" "$out"
"""


def archive_bytes(entries):
    stream = io.BytesIO()
    with tarfile.open(fileobj=stream, mode="w:gz") as bundle:
        for name, data, kind in entries:
            member = tarfile.TarInfo(name)
            member.type = kind
            member.size = len(data) if kind == tarfile.REGTYPE else 0
            if kind in {tarfile.SYMTYPE, tarfile.LNKTYPE}:
                member.linkname = "../outside"
            bundle.addfile(member, io.BytesIO(data) if member.isfile() else None)
    return stream.getvalue()


class DownloadSpecTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory(prefix="test-download-spec-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.output = self.root / "out/spec.json"
        self.output.parent.mkdir()
        self.output.write_bytes(b"original")
        self.curl_args = self.root / "curl-args"
        self.curl_stdin = self.root / "curl-stdin"
        fake = self.root / "curl"
        fake.write_text(FAKE_CURL)
        fake.chmod(0o755)

    def download(self, entries=None, *, url=URL, token=TOKEN, curl_exit=0, extra=()):
        fixture = self.root / "fixture.tar.gz"
        fixture.write_bytes(archive_bytes(entries or [(SPEC_FILE, SPEC, tarfile.REGTYPE)]))
        environment = {
            **os.environ,
            "PATH": f"{self.root}{os.pathsep}{os.environ['PATH']}",
            "CURL_ARGS": str(self.curl_args),
            "CURL_STDIN": str(self.curl_stdin),
            "CURL_EXIT": str(curl_exit),
            "FIXTURE": str(fixture),
            "SPECS_ACCESS_PAT": token,
        }
        bash = shutil.which("bash")
        self.assertIsNotNone(bash)
        return subprocess.run(  # noqa: S603 - fixed script and owned fake curl
            [
                bash,
                str(SCRIPT),
                "--version",
                "release-label",
                "--asset-url",
                url,
                "--output",
                str(self.output),
                *extra,
            ],
            env=environment,
            capture_output=True,
            text=True,
        )

    def assert_unchanged(self):
        self.assertEqual(self.output.read_bytes(), b"original")
        self.assertEqual(list(self.output.parent.glob(".download-spec*")), [])

    def test_success_preserves_bytes_and_keeps_token_out_of_arguments(self):
        result = self.download(
            [("unrelated.json", b"ignored", tarfile.REGTYPE), (SPEC_FILE, SPEC, tarfile.REGTYPE)]
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.output.read_bytes(), SPEC)
        self.assertEqual(list(self.output.parent.iterdir()), [self.output])
        self.assertIn("version release-label", result.stdout)
        arguments = self.curl_args.read_text()
        self.assertIn(TOKEN, self.curl_stdin.read_text())
        self.assertNotIn(TOKEN, arguments)
        self.assertNotIn(TOKEN, result.stdout + result.stderr)
        self.assertNotIn("--location-trusted", arguments)
        self.assertIn("--proto-redir\n=https", arguments)
        self.assertEqual(arguments.splitlines()[-1], URL)

    def test_bad_input_never_calls_curl(self):
        for name, kwargs in [
            ("http url", {"url": URL.replace("https:", "http:")}),
            ("other host", {"url": URL.replace("api.github.com", "example.com")}),
            ("trailing path", {"url": URL + "/x"}),
            ("empty token", {"token": ""}),
        ]:
            with self.subTest(name):
                result = self.download(**kwargs)
                self.assertEqual(result.returncode, 1)
                self.assertTrue(result.stderr.startswith("ERROR:"))
                self.assertFalse(self.curl_args.exists())
                self.assert_unchanged()
        with self.subTest("unknown option"):
            result = self.download(extra=["--bogus", "x"])
            self.assertEqual(result.returncode, 2)
            self.assertFalse(self.curl_args.exists())
            self.assert_unchanged()

    def test_bad_content_leaves_output_unchanged(self):
        for name, entries in [
            ("missing member", [("other.json", SPEC, tarfile.REGTYPE)]),
            ("not openapi", [(SPEC_FILE, b'{"openapi": "3.1.0", "paths": {}}', tarfile.REGTYPE)]),
            ("invalid json", [(SPEC_FILE, b"{", tarfile.REGTYPE)]),
            ("symlink member", [(SPEC_FILE, b"", tarfile.SYMTYPE)]),
        ]:
            with self.subTest(name):
                result = self.download(entries)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("ERROR:", result.stderr)
                self.assert_unchanged()

    def test_curl_failure_leaves_output_unchanged_without_leaking_token(self):
        result = self.download(curl_exit=22)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ERROR:", result.stderr)
        self.assertNotIn(TOKEN, result.stdout + result.stderr)
        self.assert_unchanged()
