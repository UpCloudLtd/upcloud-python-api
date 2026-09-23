from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.gateway_ipsec_authentication_type import GatewayIpsecAuthenticationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayAuthenticationDetailsResponse")


@_attrs_define
class GatewayAuthenticationDetailsResponse:
    """Response schema for authentication details.

    Attributes:
        authentication (GatewayIpsecAuthenticationType | Unset): IPsec authentication type
    """

    authentication: GatewayIpsecAuthenticationType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        authentication: str | Unset = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = self.authentication.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if authentication is not UNSET:
            field_dict["authentication"] = authentication

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _authentication = d.pop("authentication", UNSET)
        authentication: GatewayIpsecAuthenticationType | Unset
        if isinstance(_authentication, Unset):
            authentication = UNSET
        else:
            authentication = GatewayIpsecAuthenticationType(_authentication)

        gateway_authentication_details_response = cls(
            authentication=authentication,
        )

        return gateway_authentication_details_response
