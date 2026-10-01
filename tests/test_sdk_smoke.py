"""Offline smoke checks for the generated SDK's public configuration and imports."""

import asyncio
import importlib
import json
import unittest
from enum import Enum
from pathlib import Path

import upcloud_api
from upcloud_api import SPEC_VERSION, AuthenticatedClient, Client

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = Path(upcloud_api.__file__).resolve().parent


def generated_modules(directory):
    """Enumerate module files directly so broken package imports cannot hide modules."""
    for path in sorted((PACKAGE / directory).rglob("*.py")):
        parts = list(path.relative_to(PACKAGE.parent).with_suffix("").parts)
        if parts[-1] == "__init__":
            parts.pop()
        yield ".".join(parts)


class SDKSmokeTests(unittest.TestCase):
    """Check generated surfaces without making any network requests."""

    def test_every_generated_api_and_model_module_imports(self):
        """Import every generated API and model module, including package exports."""
        for directory in ("api", "models"):
            modules = list(generated_modules(directory))
            self.assertTrue(modules, f"No generated modules found in {directory}")
            for name in modules:
                with self.subTest(module=name):
                    importlib.import_module(name)

    def test_enum_wire_values_roundtrip(self):
        """Roundtrip every generated enum member through its serialized wire value."""
        count = 0
        for name in generated_modules("models"):
            module = importlib.import_module(name)
            for candidate in vars(module).values():
                if not isinstance(candidate, type) or not issubclass(candidate, Enum):
                    continue
                if candidate.__module__ != name:
                    continue
                count += 1
                for member in candidate.__members__.values():
                    with self.subTest(enum=candidate.__name__, member=member.name):
                        self.assertEqual(str(member), str(member.value))
                        wire_value = json.loads(json.dumps(member))
                        self.assertEqual(wire_value, member.value)
                        self.assertIs(candidate(wire_value), member)
        self.assertGreater(count, 0, "No generated enums found")

    def test_sync_clients_use_default_and_custom_base_urls(self):
        """Construct real HTTP clients locally and inspect URL and bearer configuration."""
        for client_class in (Client, AuthenticatedClient):
            for base_url in (None, "https://sdk-smoke.invalid/custom"):
                with self.subTest(client=client_class.__name__, base_url=base_url):
                    kwargs = (
                        {"token": "smoke-token"} if client_class is AuthenticatedClient else {}
                    )
                    if base_url is not None:
                        kwargs["base_url"] = base_url
                    client = client_class(**kwargs)
                    with client:
                        http_client = client.get_httpx_client()
                        self.assertEqual(
                            str(http_client.base_url).rstrip("/"),
                            base_url or "https://api.upcloud.com",
                        )
                        self.assertIs(client.get_httpx_client(), http_client)
                        if client_class is AuthenticatedClient:
                            self.assertEqual(
                                http_client.headers["Authorization"], "Bearer smoke-token"
                            )
                        else:
                            self.assertNotIn("Authorization", http_client.headers)

    def test_async_clients_use_default_and_custom_base_urls(self):
        """Check asynchronous client construction and cleanup without sending requests."""

        async def check_clients():
            for client_class in (Client, AuthenticatedClient):
                for base_url in (None, "https://sdk-smoke.invalid/custom"):
                    with self.subTest(client=client_class.__name__, base_url=base_url):
                        kwargs = (
                            {"token": "smoke-token"} if client_class is AuthenticatedClient else {}
                        )
                        if base_url is not None:
                            kwargs["base_url"] = base_url
                        client = client_class(**kwargs)
                        async with client:
                            http_client = client.get_async_httpx_client()
                            self.assertEqual(
                                str(http_client.base_url).rstrip("/"),
                                base_url or "https://api.upcloud.com",
                            )
                            self.assertIs(client.get_async_httpx_client(), http_client)
                            if client_class is AuthenticatedClient:
                                self.assertEqual(
                                    http_client.headers["Authorization"],
                                    "Bearer smoke-token",
                                )
                            else:
                                self.assertNotIn("Authorization", http_client.headers)

        asyncio.run(check_clients())

    def test_custom_token_prefix_and_header(self):
        """Support custom authentication headers, prefixes, and unprefixed tokens."""
        for prefix, expected in (("Token", "Token smoke-token"), ("", "smoke-token")):
            with self.subTest(prefix=prefix):
                client = AuthenticatedClient(
                    token="smoke-token",
                    prefix=prefix,
                    auth_header_name="X-API-Token",
                    headers={"X-Custom": "preserved"},
                )
                with client:
                    http_client = client.get_httpx_client()
                    self.assertEqual(http_client.headers["X-API-Token"], expected)
                    self.assertEqual(http_client.headers["X-Custom"], "preserved")
                    self.assertNotIn("Authorization", http_client.headers)

    def test_spec_version_matches_source_specification(self):
        """Keep the exported spec version synchronized with the generation input."""
        spec = json.loads((ROOT / "generator/openapi/spec.json").read_text(encoding="utf-8"))
        self.assertEqual(SPEC_VERSION, spec["info"]["version"])


if __name__ == "__main__":
    unittest.main()
