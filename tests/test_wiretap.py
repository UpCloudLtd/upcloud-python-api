"""Run example-derived generated SDK calls against a local Wiretap server."""

import importlib
import json
import os
import tempfile
import unittest
from pathlib import Path

import httpx

from upcloud_api import AuthenticatedClient

from .wiretap_cases import classify_wiretap_response, load_cases


class WiretapTests(unittest.IsolatedAsyncioTestCase):
    """Exercise the SDK; generator/scripts/wiretap.sh owns the server and the report check."""

    @classmethod
    def setUpClass(cls):
        cls.base_url = os.environ.get("WIRETAP_URL")
        if not cls.base_url:
            raise RuntimeError("WIRETAP_URL is not set; run via `mise run test:contract`")
        cls.temporary = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temporary.cleanup)
        cls.artifacts = Path(os.environ.get("VALIDATION_ARTIFACTS", cls.temporary.name)).resolve()
        cls.artifacts.mkdir(parents=True, exist_ok=True)
        cls.cases, unsupported, missing, errors = load_cases()
        cls.inventory = {
            "runnable_operations": len(cls.cases),
            "unsupported": unsupported,
            "missing": missing,
            "discovery_errors": errors,
            "passed": [],
            "failed": [],
            "known_limitations": [],
        }
        cls.addClassCleanup(cls.write_inventory)

    @classmethod
    def write_inventory(cls):
        (cls.artifacts / "coverage.json").write_text(json.dumps(cls.inventory, indent=2))
        print(
            f"\nWiretap: {len(cls.cases)} operations runnable; "
            f"{len(cls.inventory['unsupported'])} unsupported; "
            f"{len(cls.inventory['known_limitations'])} known Wiretap limitations; "
            f"{len(cls.inventory['failed'])} failed calls. "
            f"Inventory: {cls.artifacts / 'coverage.json'}"
        )

    def assert_result(self, case, mode, result, request):
        limitation = classify_wiretap_response(
            case, mode, result.status_code, result.content, request.method, request.url.path
        )
        if limitation is None:
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
        return limitation

    def record_outcome(self, case, mode, result, limitation):
        if limitation is None:
            self.inventory["passed"].append({"operation": case.operation_id, "mode": mode})
            return
        self.inventory["known_limitations"].append(
            {
                "operation": case.operation_id,
                "mode": mode,
                "expected_status": limitation.expected_status,
                "observed_status": int(result.status_code),
                "observed_body_marker": limitation.observed_body_marker,
                "reason": limitation.reason,
                "reference": limitation.reference,
            }
        )

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
                    limitation = self.assert_result(case, "sync", result, requests[-1])
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
                self.record_outcome(case, "sync", result, limitation)

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
                    limitation = self.assert_result(case, "async", result, requests[-1])
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
                self.record_outcome(case, "async", result, limitation)
