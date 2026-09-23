from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ip_address_boolean_yesno import IpAddressBooleanYesno
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyIpAddressRequestV10IpAddress")


@_attrs_define
class ModifyIpAddressRequestV10IpAddress:
    """
    Example:
        {'ptr_record': 'host.example.com'}

    Attributes:
        ptr_record (str):  Example: host.example.com.
        floating (IpAddressBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        vlan_id (str | Unset):
    """

    ptr_record: str
    floating: IpAddressBooleanYesno | Unset = UNSET
    vlan_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ptr_record = self.ptr_record

        floating: str | Unset = UNSET
        if not isinstance(self.floating, Unset):
            floating = self.floating.value

        vlan_id = self.vlan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ptr_record": ptr_record,
            }
        )
        if floating is not UNSET:
            field_dict["floating"] = floating
        if vlan_id is not UNSET:
            field_dict["vlan_id"] = vlan_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ptr_record = d.pop("ptr_record")

        _floating = d.pop("floating", UNSET)
        floating: IpAddressBooleanYesno | Unset
        if isinstance(_floating, Unset):
            floating = UNSET
        else:
            floating = IpAddressBooleanYesno(_floating)

        vlan_id = d.pop("vlan_id", UNSET)

        modify_ip_address_request_v10_ip_address = cls(
            ptr_record=ptr_record,
            floating=floating,
            vlan_id=vlan_id,
        )

        modify_ip_address_request_v10_ip_address.additional_properties = d
        return modify_ip_address_request_v10_ip_address

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
