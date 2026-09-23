from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_ip_family import ServerIpFamily
from ..models.server_network_type import ServerNetworkType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerIpAddressesIpAddressItem")


@_attrs_define
class ServerIpAddressesIpAddressItem:
    """
    Attributes:
        access (ServerNetworkType): Network access type Example: public.
        family (ServerIpFamily): IP address family Example: IPv4.
        address (str | Unset): IP address Example: 10.0.0.20.
        prefix (str | Unset): Network prefix length of the IP address
    """

    access: ServerNetworkType
    family: ServerIpFamily
    address: str | Unset = UNSET
    prefix: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access = self.access.value

        family = self.family.value

        address: str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        prefix = self.prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access": access,
                "family": family,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access = ServerNetworkType(d.pop("access"))

        family = ServerIpFamily(d.pop("family"))

        def _parse_address(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        prefix = d.pop("prefix", UNSET)

        server_ip_addresses_ip_address_item = cls(
            access=access,
            family=family,
            address=address,
            prefix=prefix,
        )

        server_ip_addresses_ip_address_item.additional_properties = d
        return server_ip_addresses_ip_address_item

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
