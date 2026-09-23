from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.server_boolean_yesno import ServerBooleanYesno
from ..models.server_ip_family import ServerIpFamily
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerModifyInterfaceInterfaceIpAddressesIpAddressItem")


@_attrs_define
class ServerModifyInterfaceInterfaceIpAddressesIpAddressItem:
    """
    Attributes:
        family (ServerIpFamily): IP address family Example: IPv4.
        address (str | Unset): IP address Example: 10.0.0.20.
        dhcp_provided (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
    """

    family: ServerIpFamily
    address: str | Unset = UNSET
    dhcp_provided: ServerBooleanYesno | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        family = self.family.value

        address: str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        dhcp_provided: str | Unset = UNSET
        if not isinstance(self.dhcp_provided, Unset):
            dhcp_provided = self.dhcp_provided.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "family": family,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if dhcp_provided is not UNSET:
            field_dict["dhcp_provided"] = dhcp_provided

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        family = ServerIpFamily(d.pop("family"))

        def _parse_address(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        _dhcp_provided = d.pop("dhcp_provided", UNSET)
        dhcp_provided: ServerBooleanYesno | Unset
        if isinstance(_dhcp_provided, Unset):
            dhcp_provided = UNSET
        else:
            dhcp_provided = ServerBooleanYesno(_dhcp_provided)

        server_modify_interface_interface_ip_addresses_ip_address_item = cls(
            family=family,
            address=address,
            dhcp_provided=dhcp_provided,
        )

        server_modify_interface_interface_ip_addresses_ip_address_item.additional_properties = d
        return server_modify_interface_interface_ip_addresses_ip_address_item

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
