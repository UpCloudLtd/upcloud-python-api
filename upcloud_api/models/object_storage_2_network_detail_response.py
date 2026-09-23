from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2NetworkDetailResponse")


@_attrs_define
class ObjectStorage2NetworkDetailResponse:
    """Schema for network details including family, name, type, and UUID.

    Attributes:
        family (str | Unset):  Example: IPv4.
        name (str | Unset):  Example: example-private-network.
        type_ (str | Unset):  Example: private.
        uuid (UUID | Unset):  Example: 03bec0ad-85c3-459e-824d-710f8f24f740.
    """

    family: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    uuid: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        family = self.family

        name = self.name

        type_ = self.type_

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if family is not UNSET:
            field_dict["family"] = family
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        family = d.pop("family", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        object_storage_2_network_detail_response = cls(
            family=family,
            name=name,
            type_=type_,
            uuid=uuid,
        )

        object_storage_2_network_detail_response.additional_properties = d
        return object_storage_2_network_detail_response

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
