from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerFrontendPropertiesCreate")


@_attrs_define
class LoadBalancerFrontendPropertiesCreate:
    """Frontend Properties

    Example:
        {'timeout_client': 60, 'inbound_proxy_protocol': False, 'http2_enabled': True}

    Attributes:
        timeout_client (int | Unset): Client timeout Example: 60.
        inbound_proxy_protocol (bool | Unset): Enable or disable inbound proxy protocol support Example: False.
        http2_enabled (bool | Unset): Allows for HTTP2 connection via ALPN
    """

    timeout_client: int | Unset = UNSET
    inbound_proxy_protocol: bool | Unset = UNSET
    http2_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        timeout_client = self.timeout_client

        inbound_proxy_protocol = self.inbound_proxy_protocol

        http2_enabled = self.http2_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if timeout_client is not UNSET:
            field_dict["timeout_client"] = timeout_client
        if inbound_proxy_protocol is not UNSET:
            field_dict["inbound_proxy_protocol"] = inbound_proxy_protocol
        if http2_enabled is not UNSET:
            field_dict["http2_enabled"] = http2_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timeout_client = d.pop("timeout_client", UNSET)

        inbound_proxy_protocol = d.pop("inbound_proxy_protocol", UNSET)

        http2_enabled = d.pop("http2_enabled", UNSET)

        load_balancer_frontend_properties_create = cls(
            timeout_client=timeout_client,
            inbound_proxy_protocol=inbound_proxy_protocol,
            http2_enabled=http2_enabled,
        )

        return load_balancer_frontend_properties_create
