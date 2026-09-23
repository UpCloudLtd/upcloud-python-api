from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.gateway_ipsec_authentication_type import GatewayIpsecAuthenticationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayTunnelModifyRequestIpsecAuthentication")


@_attrs_define
class GatewayTunnelModifyRequestIpsecAuthentication:
    """IPsec authentication configuration

    Attributes:
        authentication (GatewayIpsecAuthenticationType): IPsec authentication type
        psk (str | Unset): IPsec PSK
    """

    authentication: GatewayIpsecAuthenticationType
    psk: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        authentication = self.authentication.value

        psk = self.psk

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "authentication": authentication,
            }
        )
        if psk is not UNSET:
            field_dict["psk"] = psk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        authentication = GatewayIpsecAuthenticationType(d.pop("authentication"))

        psk = d.pop("psk", UNSET)

        gateway_tunnel_modify_request_ipsec_authentication = cls(
            authentication=authentication,
            psk=psk,
        )

        return gateway_tunnel_modify_request_ipsec_authentication
