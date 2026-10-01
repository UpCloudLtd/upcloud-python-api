"""Check failure-reporting and cleanup guards without running a container."""

import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from . import test_wiretap as wiretap


class WiretapLifecycleTests(unittest.TestCase):
    def test_cleanup_stops_container_even_when_client_has_exited(self):
        cls = wiretap.WiretapTests
        with tempfile.TemporaryDirectory() as directory:
            cid = Path(directory) / "cid"
            cid.write_text("validation-container")
            process = Mock()
            process.poll.return_value = 0
            with (
                patch.object(cls, "server_stopped", False, create=True),
                patch.object(cls, "cid", cid, create=True),
                patch.object(cls, "process", process, create=True),
                patch.object(cls, "engine", "docker", create=True),
                patch.object(
                    wiretap.subprocess,
                    "run",
                    return_value=subprocess.CompletedProcess(
                        ["docker", "stop"],
                        0,
                        "",
                        "",
                    ),
                ) as run,
            ):
                cls.stop_server()
                self.assertEqual(
                    run.call_args.args[0],
                    ["docker", "stop", "--time", "5", "validation-container"],
                )
                process.wait.assert_called_once()
                self.assertTrue(cls.server_stopped)

    def test_cleanup_does_not_hide_daemon_failures(self):
        cls = wiretap.WiretapTests
        with tempfile.TemporaryDirectory() as directory:
            cid = Path(directory) / "cid"
            cid.write_text("validation-container")
            process = Mock()
            process.poll.return_value = 0
            with (
                patch.object(cls, "server_stopped", False, create=True),
                patch.object(cls, "cid", cid, create=True),
                patch.object(cls, "process", process, create=True),
                patch.object(cls, "engine", "docker", create=True),
                patch.object(
                    wiretap.subprocess,
                    "run",
                    return_value=subprocess.CompletedProcess(
                        ["docker", "stop"],
                        1,
                        "",
                        "Cannot connect to Docker daemon",
                    ),
                ),
            ):
                with self.assertRaisesRegex(RuntimeError, "Cannot connect"):
                    cls.stop_server()
                process.wait.assert_called_once()

    def test_report_must_exist_and_contain_negative_control(self):
        cls = wiretap.WiretapTests
        instance = cls("test_z_no_contract_violations")
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / "report.jsonl"
            with (
                patch.object(cls, "report", report, create=True),
                patch.object(cls, "stop_server"),
            ):
                with self.assertRaisesRegex(AssertionError, "did not create"):
                    instance.test_z_no_contract_violations()
                report.write_text("")
                with self.assertRaisesRegex(AssertionError, "deliberately invalid"):
                    instance.test_z_no_contract_violations()
                canary = {"requestPath": "/1.3/server/not-a-uuid", "validationType": "parameter"}
                report.write_text(json.dumps(canary) + "\n")
                instance.test_z_no_contract_violations()
                report.write_text(
                    json.dumps(canary)
                    + "\n"
                    + json.dumps(
                        {
                            "requestPath": "/1.3/server/valid-id",
                            "validationType": "parameter",
                        }
                    )
                    + "\n"
                )
                with self.assertRaisesRegex(AssertionError, "1 contract violations"):
                    instance.test_z_no_contract_violations()
