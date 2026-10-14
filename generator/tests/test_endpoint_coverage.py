"""Regression tests for generated endpoint discovery."""

import tempfile
import unittest
from pathlib import Path

from generator.scripts.check_endpoint_coverage import (
    check_coverage,
    endpoint_contract,
    normalize_path,
)

SOURCE = '''
def _get_kwargs(uuid):
    return {"method": "get", "url": "/1.3/server/{uuid}".format(uuid=str(uuid))}
def sync(): pass
def sync_detailed(): pass
async def asyncio(): pass
async def asyncio_detailed(): pass
'''
SPEC = {"paths": {"/1.3/server/{server-id}": {"get": {"operationId": "getServer"}}}}


class EndpointCoverageTests(unittest.TestCase):
    def test_normalization_preserves_literal_segments(self):
        self.assertEqual(normalize_path("/1.3/a/{a}/b/{b}"), "/1.3/a/{}/b/{}")

    def test_formatted_path_and_matching_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            api = Path(directory)
            (api / "server").mkdir()
            path = api / "server/get_server.py"
            path.write_text(SOURCE)
            self.assertEqual(endpoint_contract(path), ("get", "/1.3/server/{}"))
            self.assertEqual(check_coverage(SPEC, api, SPEC), [])
            path.write_text(SOURCE.replace('"get"', '"delete"'))
            errors = check_coverage(SPEC, api)
            self.assertTrue(any("Missing" in error for error in errors))
            self.assertTrue(any("Unexpected" in error for error in errors))

    def test_duplicates_and_missing_functions_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            api = Path(directory)
            (api / "server").mkdir()
            first = api / "server/first.py"
            second = api / "server/second.py"
            first.write_text(SOURCE)
            second.write_text(SOURCE)
            self.assertTrue(any("Duplicate generated" in e for e in check_coverage(SPEC, api)))
            second.write_text(SOURCE.replace("async def asyncio_detailed(): pass", ""))
            self.assertTrue(any("missing functions" in e for e in check_coverage(SPEC, api)))

    def test_unsupported_expressions_and_removed_operations_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            api = Path(directory)
            (api / "server").mkdir()
            (api / "server/get_server.py").write_text(
                SOURCE.replace('"/1.3/server/{uuid}".format(uuid=str(uuid))', 'make_url(uuid)')
            )
            errors = check_coverage(SPEC, api, {"paths": {}})
            self.assertTrue(any("unsupported" in e for e in errors))
            self.assertTrue(any("Preprocessing changed" in e for e in errors))
