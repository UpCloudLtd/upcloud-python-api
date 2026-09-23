from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patch_ip_address_request_v13_ip_address import PatchIpAddressRequestV13IpAddress


T = TypeVar("T", bound="PatchIpAddressRequestV13")


@_attrs_define
class PatchIpAddressRequestV13:
    """Request schema for modifying an IP address

    Attributes:
        ip_address (PatchIpAddressRequestV13IpAddress):
    """

    ip_address: PatchIpAddressRequestV13IpAddress
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
        from ..models.patch_ip_address_request_v13_ip_address import PatchIpAddressRequestV13IpAddress  # noqa: PLC0415

        d = dict(src_dict)
        ip_address = PatchIpAddressRequestV13IpAddress.from_dict(d.pop("ip_address"))

        patch_ip_address_request_v13 = cls(
            ip_address=ip_address,
        )

        patch_ip_address_request_v13.additional_properties = d
        return patch_ip_address_request_v13

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
