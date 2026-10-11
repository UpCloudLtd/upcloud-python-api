"""Offline smoke checks for the generated SDK's public configuration and imports."""

import asyncio
import datetime
import importlib
import json
import unittest
from enum import Enum
from pathlib import Path
from uuid import UUID

import httpx

import upcloud_api
from upcloud_api import AuthenticatedClient, Client
from upcloud_api.api.kubernetes import import_cluster_authentication
from upcloud_api.models.kubernetes_authentication_issuer_config import (
    KubernetesAuthenticationIssuerConfig,
)
from upcloud_api.models.server_remote_access_details_server import (
    ServerRemoteAccessDetailsServer,
)
from upcloud_api.models.storage_import import StorageImport

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
        """Generator output and spec patches: every `api/` and `models/` module imports."""
        for directory in ("api", "models"):
            modules = list(generated_modules(directory))
            self.assertTrue(modules, f"No generated modules found in {directory}")
            for name in modules:
                with self.subTest(module=name):
                    importlib.import_module(name)

    def test_enum_wire_values_roundtrip(self):
        """Generator enum models: every member serializes to and parses from its wire value."""
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
        """client.py.jinja: sync clients default to the UpCloud API URL and set bearer auth."""
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
        """client.py.jinja: async clients default to the UpCloud API URL and set bearer auth."""

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
        """client.py.jinja: custom auth header, token prefix, and extra headers are kept."""
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

    def test_empty_string_unions_parse_both_branches(self):
        """Empty-string union members do not shadow the other branch."""
        server = {
            "state": "started",
            "vnc_host": "94.237.1.20",
            "vnc_password": "A1b2C3d4",
            "remote_access_type": "vnc",
            "remote_access_enabled": "yes",
            "remote_access_password": "A1b2C3d4",
        }
        for port in (5901, ""):
            with self.subTest(vnc_port=port):
                parsed = ServerRemoteAccessDetailsServer.from_dict({**server, "vnc_port": port})
                self.assertEqual(parsed.vnc_port, port)
                self.assertEqual(parsed.to_dict()["vnc_port"], port)

        storage_import = {
            "client_content_length": 0,
            "client_content_type": "",
            "created": "2020-06-26T08:51:07Z",
            "error_code": "",
            "error_message": "",
            "md5sum": "",
            "read_bytes": 0,
            "sha256sum": "",
            "source": "http_import",
            "state": "completed",
            "uuid": "07a6c9a3-300e-4d0e-b935-624f3dbdff3f",
            "written_bytes": 0,
        }
        completed = datetime.datetime(2020, 6, 26, 9, 1, 2, tzinfo=datetime.UTC)
        for wire, expected in (("2020-06-26T09:01:02Z", completed), ("", "")):
            with self.subTest(completed=wire):
                parsed = StorageImport.from_dict({**storage_import, "completed": wire})
                self.assertEqual(parsed.completed, expected)
                self.assertIs(type(parsed.completed), type(expected))

    def test_import_cluster_authentication_sends_yaml_sync_and_async(self):
        """The YAML import uses raw UTF-8 content and parses the JSON response."""
        body = (
            "apiVersion: apiserver.config.k8s.io/v1\n"
            "kind: AuthenticationConfiguration\n"
            "# caf\u00e9\n"
        )
        cluster_uuid = UUID("07a6c9a3-300e-4d0e-b935-624f3dbdff3f")
        expected_path = f"/1.3/kubernetes/{cluster_uuid}/authentication/import"
        issuer_url = "https://issuer.smoke.invalid"

        def handler(request):
            return httpx.Response(
                200,
                json=[
                    {
                        "name": "smoke-issuer",
                        "issuer_url": issuer_url,
                        "audiences": ["smoke-audience"],
                    }
                ],
            )

        def assert_request(request):
            self.assertEqual(request.method, "PUT")
            self.assertEqual(request.url.path, expected_path)
            self.assertEqual(request.content, body.encode("utf-8"))
            self.assertEqual(request.headers["Content-Type"], "application/yaml")

        sync_requests = []

        def sync_handler(request):
            sync_requests.append(request)
            return handler(request)

        sync_client = Client(
            base_url="https://sdk-smoke.invalid",
            httpx_args={"transport": httpx.MockTransport(sync_handler)},
        )
        with sync_client:
            sync_response = import_cluster_authentication.sync_detailed(
                cluster_uuid, client=sync_client, body=body
            )
        self.assertEqual(len(sync_requests), 1)
        assert_request(sync_requests[0])
        self.assertIsInstance(sync_response.parsed, list)
        self.assertIsInstance(sync_response.parsed[0], KubernetesAuthenticationIssuerConfig)
        self.assertEqual(sync_response.parsed[0].issuer_url, issuer_url)

        async_requests = []

        def async_handler(request):
            async_requests.append(request)
            return handler(request)

        async_client = Client(
            base_url="https://sdk-smoke.invalid",
            httpx_args={"transport": httpx.MockTransport(async_handler)},
        )

        async def send_async_request():
            async with async_client:
                return await import_cluster_authentication.asyncio_detailed(
                    cluster_uuid, client=async_client, body=body
                )

        async_response = asyncio.run(send_async_request())
        self.assertEqual(len(async_requests), 1)
        assert_request(async_requests[0])
        self.assertIsInstance(async_response.parsed, list)
        self.assertIsInstance(async_response.parsed[0], KubernetesAuthenticationIssuerConfig)
        self.assertEqual(async_response.parsed[0].issuer_url, issuer_url)


if __name__ == "__main__":
    unittest.main()
