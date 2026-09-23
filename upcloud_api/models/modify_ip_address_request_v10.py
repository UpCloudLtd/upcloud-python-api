from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.modify_ip_address_request_v10_ip_address import ModifyIpAddressRequestV10IpAddress


T = TypeVar("T", bound="ModifyIpAddressRequestV10")


@_attrs_define
class ModifyIpAddressRequestV10:
    """Request schema for modifying an IP address

    Example:
        {'ip_address': {'ptr_record': 'host.example.com'}}

    Attributes:
        ip_address (ModifyIpAddressRequestV10IpAddress):  Example: {'ptr_record': 'host.example.com'}.
    """

    ip_address: ModifyIpAddressRequestV10IpAddress
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_address = self.ip_address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip_address": ip_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.modify_ip_address_request_v10_ip_address import (
            ModifyIpAddressRequestV10IpAddress,  # noqa: PLC0415
        )

        d = dict(src_dict)
        ip_address = ModifyIpAddressRequestV10IpAddress.from_dict(d.pop("ip_address"))

        modify_ip_address_request_v10 = cls(
            ip_address=ip_address,
        )

        modify_ip_address_request_v10.additional_properties = d
        return modify_ip_address_request_v10

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
