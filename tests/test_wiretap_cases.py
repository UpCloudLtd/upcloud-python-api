"""Exercise generic case derivation without starting Wiretap."""

import asyncio
import datetime
import json
import socket
import threading
import unittest
from dataclasses import replace
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Literal
from uuid import UUID

import httpx

from upcloud_api.models.tag import Tag
from upcloud_api.types import Unset

from . import test_wiretap
from .wiretap_cases import (
    EMPTY_PROBLEM_MARKER,
    EMPTY_PROBLEM_TITLE,
    EMPTY_PROBLEM_TYPE,
    KNOWN_WIRETAP_LIMITATIONS,
    ROOT,
    Case,
    InvalidExample,
    StaleKnownLimitation,
    UnsupportedExample,
    classify_wiretap_response,
    convert,
    derive_cases,
    example,
    load_cases,
    resolve,
)


class CaseDerivationTests(unittest.TestCase):
    def test_references_and_schema_examples(self):
        spec = {"components": {"schemas": {"value": {"type": "integer", "examples": [0]}}}}
        self.assertEqual(example(spec, {"schema": {"$ref": "#/components/schemas/value"}}), 0)
        self.assertEqual(
            resolve(spec, {"$ref": "#/components/schemas/value", "description": "kept"})[
                "description"
            ],
            "kept",
        )
        self.assertEqual(example({}, {"examples": {"named": {"value": False}}}), False)
        self.assertEqual(example({}, {"default": ""}), "")

    def test_reference_cycles_and_absent_examples_are_explicit(self):
        spec = {"cycle": {"$ref": "#/cycle"}}
        with self.assertRaises(UnsupportedExample):
            resolve(spec, {"$ref": "#/cycle"})
        with self.assertRaises(UnsupportedExample):
            example({}, {"type": "string", "pattern": "complex"})

    def test_union_does_not_accept_unset_as_a_raw_model(self):
        value = {
            "tag": {"name": "validation", "description": "offline", "servers": {"server": []}}
        }
        model = convert(value, Tag | Unset)
        self.assertIsInstance(model, Tag)
        self.assertEqual(model.to_dict(), value)
        with self.assertRaises(InvalidExample):
            convert({"invalid": True}, Tag | Unset)

    def test_union_tries_next_model_when_first_drops_input_keys(self):
        class DropsKey:
            @classmethod
            def from_dict(cls, _value):
                return cls()

            def to_dict(self):
                return {"kept": {}}

        class PreservesKeys:
            @classmethod
            def from_dict(cls, value):
                instance = cls()
                instance.value = value
                return instance

            def to_dict(self):
                return self.value

        value = {"kept": {"nested": True}, "also_kept": [1, 2]}
        converted = convert(value, DropsKey | PreservesKeys)
        self.assertIsInstance(converted, PreservesKeys)
        self.assertEqual(converted.to_dict(), value)

    def test_union_rejects_models_that_all_drop_input_keys(self):
        class DropsKeys:
            @classmethod
            def from_dict(cls, _value):
                return cls()

            def to_dict(self):
                return {}

        class AlsoDropsKeys(DropsKeys):
            pass

        with self.assertRaises(InvalidExample):
            convert({"field": "value"}, DropsKeys | AlsoDropsKeys)

    def test_scalar_conversions(self):
        value = "00000000-0000-4000-8000-000000000001"
        self.assertEqual(str(convert(value, UUID)), value)
        self.assertEqual(
            convert("2026-01-01T00:00:00Z", datetime.datetime).utcoffset(), datetime.timedelta()
        )
        self.assertEqual(convert("yes", Literal["yes", "no"]), "yes")
        with self.assertRaises(ValueError):
            convert("invalid", Literal["yes", "no"])

    def test_operation_without_generated_code_is_inventoried_as_missing(self):
        """A later derivable operation must not erase the missing-operation inventory."""
        ok = {"responses": {"200": {"description": "ok"}}}
        spec = {
            "paths": {
                "/1.3/not-generated": {"get": {"operationId": "notGenerated", **ok}},
                "/1.3/account": {"get": {"operationId": "getAccount", **ok}},
            }
        }
        cases, unsupported, missing, errors = derive_cases(spec, ROOT / "upcloud_api/api")
        self.assertEqual([case.operation_id for case in cases], ["getAccount"])
        self.assertEqual(unsupported, [])
        self.assertEqual(missing, ["notGenerated"])
        self.assertFalse([error for error in errors if "notGenerated" in error], errors)


PATH = "/1.3/gateway/01234567-89ab-cdef-0123-456789abcdef/labels"


def documented_body(path=PATH, method="POST", marker=EMPTY_PROBLEM_MARKER):
    """The exact Wiretap problem body for a bodyless mock response."""
    detail = f"Nothing was generated for the request '{path}' with the method '{method}'. {marker}"
    return json.dumps(
        {
            "type": EMPTY_PROBLEM_TYPE,
            "title": EMPTY_PROBLEM_TITLE,
            "status": 200,
            "detail": detail,
        }
    ).encode()


def case_for(operation_id, status, has_body=False):
    return Case(
        operation_id=operation_id,
        module="module",
        kwargs={},
        status=status,
        has_body=has_body,
        query={},
    )


class _StubWiretapHandler(BaseHTTPRequestHandler):
    """Answers POST with the documented bodyless response; the SDK calls themselves are real."""

    status = 200
    body = None

    def do_POST(self):
        self.rfile.read(int(self.headers.get("Content-Length", 0)))
        payload = self.body if self.body is not None else documented_body(self.path)
        self.send_response(self.status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format, *args):
        """Keep unittest output free of request logs."""


class KnownWiretapLimitationsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cases, _, _, _ = load_cases()
        known_operations = {operation_id for operation_id, _ in KNOWN_WIRETAP_LIMITATIONS}
        cls.known_cases = [case for case in cases if case.operation_id in known_operations]

    def serve(self, status=200, body=None):
        handler = type("Handler", (_StubWiretapHandler,), {"status": status, "body": body})
        server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        return f"http://127.0.0.1:{server.server_address[1]}"

    def unused_base_url(self):
        with socket.socket() as sock:
            sock.bind(("127.0.0.1", 0))
            port = sock.getsockname()[1]
        return f"http://127.0.0.1:{port}"

    def harness(self, cases, base_url):
        harness = test_wiretap.WiretapTests("test_sync_examples")
        harness.cases = cases
        harness.base_url = base_url
        harness.inventory = {"passed": [], "failed": [], "known_limitations": []}
        return harness

    def run_examples(self, harness, mode):
        if mode == "sync":
            harness.test_sync_examples()
        else:
            asyncio.run(harness.test_async_examples())

    def test_exact_documented_responses_are_known(self):
        for (operation_id, mode), limitation in KNOWN_WIRETAP_LIMITATIONS.items():
            with self.subTest(operation=operation_id, mode=mode):
                case = case_for(operation_id, limitation.expected_status)
                self.assertIs(
                    classify_wiretap_response(case, mode, 200, documented_body(), "POST", PATH),
                    limitation,
                )

    def test_only_exact_documented_responses_qualify(self):
        case = case_for("createGatewayServiceLabel", 201)
        good = json.loads(documented_body())
        calls = {
            "status 500": (500, documented_body(), "POST", PATH),
            "method GET": (200, documented_body(), "GET", PATH),
            "detail path differs": (200, documented_body(path="/1.3/other"), "POST", PATH),
            "detail marker case differs": (
                200,
                documented_body(marker="response is empty"),
                "POST",
                PATH,
            ),
            "not JSON": (200, b"{", "POST", PATH),
            "not UTF-8": (200, b"\xff", "POST", PATH),
            "JSON list": (200, b"[]", "POST", PATH),
            "extra field": (200, json.dumps({**good, "instance": "x"}).encode(), "POST", PATH),
            "missing field": (
                200,
                json.dumps({k: v for k, v in good.items() if k != "detail"}).encode(),
                "POST",
                PATH,
            ),
            "string status": (200, json.dumps({**good, "status": "200"}).encode(), "POST", PATH),
            "boolean status": (200, json.dumps({**good, "status": True}).encode(), "POST", PATH),
            "changed type": (
                200,
                json.dumps({**good, "type": "https://example.com"}).encode(),
                "POST",
                PATH,
            ),
            "changed title": (200, json.dumps({**good, "title": "Other"}).encode(), "POST", PATH),
        }
        for name, (status, body, method, path) in calls.items():
            with self.subTest(variant=name):
                self.assertIsNone(
                    classify_wiretap_response(case, "sync", status, body, method, path)
                )

    def test_unlisted_or_changed_cases_are_not_known(self):
        calls = {
            "unlisted operation": (case_for("getAccount", 200), "sync"),
            "unlisted mode": (case_for("createGatewayServiceLabel", 201), "other"),
            "changed expected status": (case_for("createGatewayServiceLabel", 202), "sync"),
            "body expected": (case_for("createGatewayServiceLabel", 201, has_body=True), "sync"),
        }
        for name, (case, mode) in calls.items():
            with self.subTest(variant=name):
                self.assertIsNone(
                    classify_wiretap_response(case, mode, 200, documented_body(), "POST", PATH)
                )

    def test_listed_operation_returning_spec_status_is_stale(self):
        for (operation_id, mode), limitation in KNOWN_WIRETAP_LIMITATIONS.items():
            with self.subTest(operation=operation_id, mode=mode):
                case = case_for(operation_id, limitation.expected_status)
                with self.assertRaises(StaleKnownLimitation):
                    classify_wiretap_response(
                        case, mode, limitation.expected_status, b"", "POST", PATH
                    )

    def test_documented_responses_are_recorded_only_as_known_limitations(self):
        harness = self.harness(self.known_cases, self.serve())
        for mode in ("sync", "async"):
            self.run_examples(harness, mode)
        self.assertEqual(harness.inventory["passed"], [])
        self.assertEqual(harness.inventory["failed"], [])
        recorded = harness.inventory["known_limitations"]
        self.assertEqual(len(recorded), len(KNOWN_WIRETAP_LIMITATIONS))
        self.assertEqual(
            {(item["operation"], item["mode"]) for item in recorded},
            set(KNOWN_WIRETAP_LIMITATIONS),
        )
        for item in recorded:
            limitation = KNOWN_WIRETAP_LIMITATIONS[(item["operation"], item["mode"])]
            self.assertEqual(item["expected_status"], limitation.expected_status)
            self.assertEqual(item["observed_status"], 200)

    def test_stale_entry_fails_the_harness_in_both_modes(self):
        for case in self.known_cases:
            for mode in ("sync", "async"):
                with self.subTest(operation=case.operation_id, mode=mode):
                    harness = self.harness([case], self.serve(status=case.status))
                    with self.assertRaises(StaleKnownLimitation):
                        self.run_examples(harness, mode)
                    self.assertEqual(harness.inventory["known_limitations"], [])
                    self.assertEqual(harness.inventory["passed"], [])
                    self.assertEqual(
                        [failure["error_type"] for failure in harness.inventory["failed"]],
                        ["StaleKnownLimitation"],
                    )

    def test_known_response_does_not_hide_other_failures(self):
        label = next(
            case for case in self.known_cases if case.operation_id == "createGatewayServiceLabel"
        )
        scenarios = {
            "wrong status": (self.serve(status=500), label, AssertionError),
            "wrong marker": (
                self.serve(body=documented_body(marker="Response is EMPTY")),
                label,
                AssertionError,
            ),
            "unrelated query": (
                self.serve(),
                replace(label, query={"probe": "1"}),
                AssertionError,
            ),
            "invocation error": (self.unused_base_url(), label, httpx.HTTPError),
        }
        for name, (base_url, case, expected) in scenarios.items():
            for mode in ("sync", "async"):
                with self.subTest(scenario=name, mode=mode):
                    harness = self.harness([case], base_url)
                    with self.assertRaises(expected):
                        self.run_examples(harness, mode)
                    self.assertEqual(harness.inventory["known_limitations"], [])
                    self.assertEqual(harness.inventory["passed"], [])
                    self.assertEqual(len(harness.inventory["failed"]), 1)
