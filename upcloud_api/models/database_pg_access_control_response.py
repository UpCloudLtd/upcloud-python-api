from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabasePgAccessControlResponse")


@_attrs_define
class DatabasePgAccessControlResponse:
    """Schema for PostgreSQL access control response.

    Attributes:
        allow_replication (bool | Unset): If true, allows replication connections. Example: False.
    """

    allow_replication: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_replication = self.allow_replication

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_replication is not UNSET:
            field_dict["allow_replication"] = allow_replication

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_replication = d.pop("allow_replication", UNSET)

        database_pg_access_control_response = cls(
            allow_replication=allow_replication,
        )

        database_pg_access_control_response.additional_properties = d
        return database_pg_access_control_response

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
