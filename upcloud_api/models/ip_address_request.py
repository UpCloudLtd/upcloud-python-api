from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ip_address_details import IpAddressDetails


T = TypeVar("T", bound="IpAddressRequest")


@_attrs_define
class IpAddressRequest:
    """Request schema for IP address operations

    Example:
        {'ip_addresses': [{'access': 'public', 'address': '203.0.113.10', 'family': 'IPv4', 'ptr_record':
            'host.example.com'}]}

    Attributes:
        ip_addresses (list[IpAddressDetails]): List of IP addresses to operate on Example: [{'access': 'public',
            'address': '203.0.113.10', 'family': 'IPv4', 'ptr_record': 'host.example.com'}].
    """

    ip_addresses: list[IpAddressDetails]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_addresses = []
        for ip_addresses_item_data in self.ip_addresses:
            ip_addresses_item = ip_addresses_item_data.to_dict()
            ip_addresses.append(ip_addresses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip_addresses": ip_addresses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_address_details import IpAddressDetails  # noqa: PLC0415

        d = dict(src_dict)
        ip_addresses = []
        _ip_addresses = d.pop("ip_addresses")
        for ip_addresses_item_data in _ip_addresses:
            ip_addresses_item = IpAddressDetails.from_dict(ip_addresses_item_data)

            ip_addresses.append(ip_addresses_item)

        ip_address_request = cls(
            ip_addresses=ip_addresses,
        )

        ip_address_request.additional_properties = d
        return ip_address_request

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
