from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogicalDatabaseCreate")


@_attrs_define
class LogicalDatabaseCreate:
    """Schema for creating a logical database.

    Attributes:
        name (str): logical database name
        lc_collate (str | Unset): Collation order
        lc_ctype (str | Unset): Category of a locale definition source file
    """

    name: str
    lc_collate: str | Unset = UNSET
    lc_ctype: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        lc_collate = self.lc_collate

        lc_ctype = self.lc_ctype

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if lc_collate is not UNSET:
            field_dict["lc_collate"] = lc_collate
        if lc_ctype is not UNSET:
            field_dict["lc_ctype"] = lc_ctype

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        lc_collate = d.pop("lc_collate", UNSET)

        lc_ctype = d.pop("lc_ctype", UNSET)

        logical_database_create = cls(
            name=name,
            lc_collate=lc_collate,
            lc_ctype=lc_ctype,
        )

        return logical_database_create
