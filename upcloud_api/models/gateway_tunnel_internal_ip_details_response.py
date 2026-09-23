from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_address import GatewayAddress


T = TypeVar("T", bound="GatewayTunnelInternalIpDetailsResponse")


@_attrs_define
class GatewayTunnelInternalIpDetailsResponse:
    """Response schema for gateway tunnel internal IP details.

    Attributes:
        ip (GatewayAddress | Unset):
        has_parse_error (bool | Unset): Indicates if there is a parse error with the tunnel internal IP
    """

    ip: GatewayAddress | Unset = UNSET
    has_parse_error: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip, Unset):
            ip = self.ip.to_dict()

        has_parse_error = self.has_parse_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip is not UNSET:
            field_dict["ip"] = ip
        if has_parse_error is not UNSET:
            field_dict["hasParseError"] = has_parse_error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_address import GatewayAddress  # noqa: PLC0415

        d = dict(src_dict)
        _ip = d.pop("ip", UNSET)
        ip: GatewayAddress | Unset
        if isinstance(_ip, Unset):
            ip = UNSET
        else:
            ip = GatewayAddress.from_dict(_ip)

        has_parse_error = d.pop("hasParseError", UNSET)

        gateway_tunnel_internal_ip_details_response = cls(
            ip=ip,
            has_parse_error=has_parse_error,
        )

        gateway_tunnel_internal_ip_details_response.additional_properties = d
        return gateway_tunnel_internal_ip_details_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
