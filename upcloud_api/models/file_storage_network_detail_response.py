from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileStorageNetworkDetailResponse")


@_attrs_define
class FileStorageNetworkDetailResponse:
    """Schema for the detailed response of a network.

    Attributes:
        family (str | Unset):
        ip_address (str | Unset):
        name (str | Unset):
        uuid (str | Unset):
    """

    family: str | Unset = UNSET
    ip_address: str | Unset = UNSET
    name: str | Unset = UNSET
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        family = self.family

        ip_address = self.ip_address

        name = self.name

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if family is not UNSET:
            field_dict["family"] = family
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if name is not UNSET:
            field_dict["name"] = name
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        family = d.pop("family", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        name = d.pop("name", UNSET)

        uuid = d.pop("uuid", UNSET)

        file_storage_network_detail_response = cls(
            family=family,
            ip_address=ip_address,
            name=name,
            uuid=uuid,
        )

        file_storage_network_detail_response.additional_properties = d
        return file_storage_network_detail_response

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
