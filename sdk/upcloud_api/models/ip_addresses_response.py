from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.ip_addresses_response_ip_addresses import IpAddressesResponseIpAddresses


T = TypeVar("T", bound="IpAddressesResponse")


@_attrs_define
class IpAddressesResponse:
    """Request schema for IP address operations

    Example:
        {'ip_addresses': {'ip_address': [{'access': 'public', 'address': '203.0.113.10', 'family': 'IPv4', 'ptr_record':
            'host.example.com'}]}}

    Attributes:
        ip_addresses (IpAddressesResponseIpAddresses):  Example: {'ip_address': [{'access': 'public', 'address':
            '203.0.113.10', 'family': 'IPv4', 'ptr_record': 'host.example.com'}]}.
    """

    ip_addresses: IpAddressesResponseIpAddresses

    def to_dict(self) -> dict[str, Any]:
        ip_addresses = self.ip_addresses.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ip_addresses": ip_addresses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_addresses_response_ip_addresses import IpAddressesResponseIpAddresses  # noqa: PLC0415

        d = dict(src_dict)
        ip_addresses = IpAddressesResponseIpAddresses.from_dict(d.pop("ip_addresses"))

        ip_addresses_response = cls(
            ip_addresses=ip_addresses,
        )

        return ip_addresses_response
