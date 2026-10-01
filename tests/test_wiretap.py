"""Run example-derived generated SDK calls against a local Wiretap server."""

import importlib
import json
import os
import shutil
import socket
import subprocess
import tempfile
import time
import unittest
from pathlib import Path

import httpx

from upcloud_api import AuthenticatedClient

from .wiretap_cases import ROOT, load_cases


def available_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


class WiretapTests(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = os.environ.get("CONTAINER_ENGINE", "docker")
        if not shutil.which(cls.engine):
            raise RuntimeError("Docker (or CONTAINER_ENGINE=podman) is required for Wiretap tests")
        cls.temporary = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temporary.cleanup)
        cls.artifacts = Path(os.environ.get("VALIDATION_ARTIFACTS", cls.temporary.name)).resolve()
        cls.artifacts.mkdir(parents=True, exist_ok=True)
        cls.cases, unsupported, errors = load_cases()
        cls.inventory = {
            "runnable_operations": len(cls.cases),
            "unsupported": unsupported,
            "discovery_errors": errors,
            "passed": [],
            "failed": [],
        }
        cls.report = cls.artifacts / "wiretap-violations.jsonl"
        cls.report.unlink(missing_ok=True)
        config = Path(cls.temporary.name) / "wiretap.json"
        config.write_text(
            json.dumps(
                {
                    "contract": "/spec.json",
                    "mockMode": True,
                    "hardValidation": True,
                    "streamReport": True,
                    "reportFile": "/reports/wiretap-violations.jsonl",
                }
            )
        )
        log = (cls.artifacts / "wiretap.log").open("w")
        cls.addClassCleanup(log.close)
        port = available_port()
        cls.base_url = f"http://127.0.0.1:{port}"
        cid = Path(cls.temporary.name) / "container-id"
        cls.cid = cid
        cls.server_stopped = False
        cls.process = subprocess.Popen(
            [
                cls.engine,
                "run",
                "--rm",
                "--cidfile",
                str(cid),
                "--publish",
                f"127.0.0.1:{port}:9090",
                "--volume",
                f"{ROOT / 'generator/openapi/spec.patched.json'}:/spec.json:ro",
                "--volume",
                f"{config}:/wiretap.json:ro",
                "--volume",
                f"{cls.artifacts}:/reports",
                "docker.io/pb33f/wiretap@sha256:e4d3d9c06bc5a246cc52d560bc378e5a1a2a73a566b009d909b865c6b06cc1f0",
                "--config",
                "/wiretap.json",
                "--mock-mode",
                "--hard-validation",
                "--stream-report",
                "--report-filename",
                "/reports/wiretap-violations.jsonl",
            ],
            stdout=log,
            stderr=subprocess.STDOUT,
        )
        cls.addClassCleanup(cls.stop_server)
        deadline = time.monotonic() + 120
        with httpx.Client(timeout=1, trust_env=False) as probe:
            while time.monotonic() < deadline:
                if cls.process.poll() is not None:
                    raise RuntimeError(f"Wiretap exited; see {cls.artifacts / 'wiretap.log'}")
                try:
                    response = probe.get(
                        cls.base_url + "/1.3/zone",
                        headers={"Authorization": "Bearer sdk-validation"},
                    )
                    if response.status_code == 200:
                        break
                except httpx.TransportError:
                    pass
                time.sleep(0.1)
            else:
                raise RuntimeError(
                    f"Wiretap did not become ready within 120 seconds; see {cls.artifacts / 'wiretap.log'}"
                )
        cls.addClassCleanup(cls.write_inventory)

    @classmethod
    def stop_server(cls):
        if cls.server_stopped:
            return
        try:
            if cls.cid.exists():
                stopped = subprocess.run(
                    [cls.engine, "stop", "--time", "5", cls.cid.read_text().strip()],
                    timeout=20,
                    capture_output=True,
                    text=True,
                )
                removed = any(
                    message in stopped.stderr.lower()
                    for message in (
                        "no such container",
                        "no such object",
                        "no container with name or id",
                    )
                )
                if stopped.returncode and not removed:
                    raise RuntimeError(f"Cannot stop Wiretap container: {stopped.stderr}")
        finally:
            if cls.process.poll() is None:
                cls.process.terminate()
            try:
                cls.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                cls.process.kill()
                cls.process.wait(timeout=5)
        cls.server_stopped = True

    @classmethod
    def write_inventory(cls):
        (cls.artifacts / "coverage.json").write_text(json.dumps(cls.inventory, indent=2))
        print(
            f"\nWiretap: {len(cls.cases)} operations runnable; "
            f"{len(cls.inventory['unsupported'])} unsupported; "
            f"{len(cls.inventory['failed'])} failed calls. Inventory: {cls.artifacts / 'coverage.json'}"
        )

    def assert_result(self, case, result, request):
        self.assertEqual(result.status_code, case.status)
        self.assertEqual(request.headers.get("Authorization"), "Bearer sdk-validation")
        for name, value in case.query.items():
            self.assertEqual(request.url.params.get(name), value, f"Dropped/changed query {name}")
        if case.has_body:
            self.assertIsNotNone(result.parsed)
        if case.status == 204:
            self.assertEqual(result.content, b"")
            self.assertIsNone(result.parsed)
        if hasattr(result.parsed, "to_dict"):
            encoded = result.parsed.to_dict()
            self.assertEqual(type(result.parsed).from_dict(encoded).to_dict(), encoded)

    def record_failure(self, case, mode, error, responses):
        failure = {
            "operation": case.operation_id,
            "mode": mode,
            "error_type": type(error).__name__,
            "error": str(error),
        }
        if responses:
            response = responses[-1]
            failure.update(status=response.status_code, response=response.text[:2048])
        self.inventory["failed"].append(failure)

    def test_discovery(self):
        self.assertTrue(self.cases, "No runnable cases")
        self.assertEqual(self.inventory["discovery_errors"], [])

    def test_sync_examples(self):
        for case in self.cases:
            with self.subTest(operation=case.operation_id):
                requests = []
                responses = []

                def capture_response(response, captured=responses):
                    response.read()
                    captured.append(response)

                try:
                    with AuthenticatedClient(
                        base_url=self.base_url,
                        token="sdk-validation",
                        timeout=httpx.Timeout(10),
                        httpx_args={
                            "trust_env": False,
                            "event_hooks": {
                                "request": [requests.append],
                                "response": [capture_response],
                            },
                        },
                    ) as client:
                        result = importlib.import_module(case.module).sync_detailed(
                            client=client, **case.kwargs
                        )
                    self.assert_result(case, result, requests[-1])
                except (
                    AssertionError,
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    httpx.HTTPError,
                ) as error:
                    self.record_failure(case, "sync", error, responses)
                    raise
                self.inventory["passed"].append({"operation": case.operation_id, "mode": "sync"})

    async def test_async_examples(self):
        for case in self.cases:
            with self.subTest(operation=case.operation_id):
                requests = []
                responses = []

                async def capture(request, captured=requests):
                    captured.append(request)

                async def capture_response(response, captured=responses):
                    await response.aread()
                    captured.append(response)

                try:
                    async with AuthenticatedClient(
                        base_url=self.base_url,
                        token="sdk-validation",
                        timeout=httpx.Timeout(10),
                        httpx_args={
                            "trust_env": False,
                            "event_hooks": {"request": [capture], "response": [capture_response]},
                        },
                    ) as client:
                        result = await importlib.import_module(case.module).asyncio_detailed(
                            client=client, **case.kwargs
                        )
                    self.assert_result(case, result, requests[-1])
                except (
                    AssertionError,
                    ValueError,
                    TypeError,
                    KeyError,
                    AttributeError,
                    httpx.HTTPError,
                ) as error:
                    self.record_failure(case, "async", error, responses)
                    raise
                self.inventory["passed"].append({"operation": case.operation_id, "mode": "async"})

    def test_validation_rejects_invalid_request(self):
        with httpx.Client(base_url=self.base_url, trust_env=False, timeout=10) as client:
            response = client.get(
                "/1.3/server/not-a-uuid", headers={"Authorization": "Bearer sdk-validation"}
            )
        self.assertEqual(response.status_code, 422)
        self.assertIn("validation", response.text.lower())

    def test_z_no_contract_violations(self):
        self.stop_server()
        self.assertTrue(self.report.is_file(), f"Wiretap did not create its report: {self.report}")
        violations = [json.loads(line) for line in self.report.read_text().splitlines()]
        canary = [
            item
            for item in violations
            if item.get("requestPath") == "/1.3/server/not-a-uuid"
            and item.get("validationType") == "parameter"
        ]
        self.assertTrue(canary, "Wiretap did not report the deliberately invalid request")
        unexpected = [item for item in violations if item not in canary]
        self.assertEqual(
            len(unexpected),
            0,
            f"Wiretap reported {len(unexpected)} contract violations; see {self.report}",
        )
