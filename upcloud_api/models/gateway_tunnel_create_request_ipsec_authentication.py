from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.gateway_ipsec_authentication_type import GatewayIpsecAuthenticationType

T = TypeVar("T", bound="GatewayTunnelCreateRequestIpsecAuthentication")


@_attrs_define
class GatewayTunnelCreateRequestIpsecAuthentication:
    """IPsec authentication configuration

    Attributes:
        authentication (GatewayIpsecAuthenticationType): IPsec authentication type
        psk (str): IPsec PSK
    """

    authentication: GatewayIpsecAuthenticationType
    psk: str

    def to_dict(self) -> dict[str, Any]:
        authentication = self.authentication.value

        psk = self.psk

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "authentication": authentication,
                "psk": psk,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authentication = GatewayIpsecAuthenticationType(d.pop("authentication"))

        psk = d.pop("psk")

        gateway_tunnel_create_request_ipsec_authentication = cls(
            authentication=authentication,
            psk=psk,
        )

        return gateway_tunnel_create_request_ipsec_authentication
