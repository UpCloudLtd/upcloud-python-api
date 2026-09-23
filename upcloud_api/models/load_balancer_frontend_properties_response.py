from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerFrontendPropertiesResponse")


@_attrs_define
class LoadBalancerFrontendPropertiesResponse:
    """Defines configurable properties for a frontend, such as client timeout settings, protocol options, and linkage to
    its parent frontend resource.

        Example:
            {'inbound_proxy_protocol': False, 'timeout_client': 50000, 'http2_enabled': True, 'frontend_id': 301}

        Attributes:
            timeout_client (int): Maximum inactivity timeout for a client connection, in milliseconds. Determines how long a
                client connection can remain idle before being closed. Example: 50000.
            frontend_id (int): Identifier linking these properties to the parent frontend configuration. Example: 301.
            inbound_proxy_protocol (bool | Unset): Enables or disables support for the Proxy Protocol on inbound
                connections, allowing client IP addresses to be forwarded to the backend. Example: False.
            http2_enabled (bool | Unset): Indicates whether HTTP/2 protocol support is enabled for this frontend. Example:
                True.
    """

    timeout_client: int
    frontend_id: int
    inbound_proxy_protocol: bool | Unset = UNSET
    http2_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        timeout_client = self.timeout_client

        frontend_id = self.frontend_id

        inbound_proxy_protocol = self.inbound_proxy_protocol

        http2_enabled = self.http2_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "timeout_client": timeout_client,
                "frontend_id": frontend_id,
            }
        )
        if inbound_proxy_protocol is not UNSET:
            field_dict["inbound_proxy_protocol"] = inbound_proxy_protocol
        if http2_enabled is not UNSET:
            field_dict["http2_enabled"] = http2_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timeout_client = d.pop("timeout_client")

        frontend_id = d.pop("frontend_id")

        inbound_proxy_protocol = d.pop("inbound_proxy_protocol", UNSET)

        http2_enabled = d.pop("http2_enabled", UNSET)

        load_balancer_frontend_properties_response = cls(
            timeout_client=timeout_client,
            frontend_id=frontend_id,
            inbound_proxy_protocol=inbound_proxy_protocol,
            http2_enabled=http2_enabled,
        )

        return load_balancer_frontend_properties_response
