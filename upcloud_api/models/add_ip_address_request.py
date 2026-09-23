from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.add_ip_address_request_ip_address import AddIpAddressRequestIpAddress


T = TypeVar("T", bound="AddIpAddressRequest")


@_attrs_define
class AddIpAddressRequest:
    """Schema for adding an IP address to a server

    Attributes:
        ip_address (AddIpAddressRequestIpAddress):
    """

    ip_address: AddIpAddressRequestIpAddress
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
        from ..models.add_ip_address_request_ip_address import AddIpAddressRequestIpAddress  # noqa: PLC0415

        d = dict(src_dict)
        ip_address = AddIpAddressRequestIpAddress.from_dict(d.pop("ip_address"))

        add_ip_address_request = cls(
            ip_address=ip_address,
        )

        add_ip_address_request.additional_properties = d
        return add_ip_address_request

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
