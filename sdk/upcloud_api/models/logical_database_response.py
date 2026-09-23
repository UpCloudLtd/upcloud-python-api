from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogicalDatabaseResponse")


@_attrs_define
class LogicalDatabaseResponse:
    """Schema for a logical database response.

    Attributes:
        name (str | Unset): The name of the logical database. Example: postgres.
        lc_collate (str | Unset): The LC_COLLATE setting of the logical database. Example: en_US.UTF-8.
        lc_ctype (str | Unset): The LC_CTYPE setting of the logical database. Example: en_US.UTF-8.
    """

    name: str | Unset = UNSET
    lc_collate: str | Unset = UNSET
    lc_ctype: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        lc_collate = self.lc_collate

        lc_ctype = self.lc_ctype

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if lc_collate is not UNSET:
            field_dict["lc_collate"] = lc_collate
        if lc_ctype is not UNSET:
            field_dict["lc_ctype"] = lc_ctype

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        lc_collate = d.pop("lc_collate", UNSET)

        lc_ctype = d.pop("lc_ctype", UNSET)

        logical_database_response = cls(
            name=name,
            lc_collate=lc_collate,
            lc_ctype=lc_ctype,
        )

        logical_database_response.additional_properties = d
        return logical_database_response

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
