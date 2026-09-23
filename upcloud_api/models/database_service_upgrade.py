from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DatabaseServiceUpgrade")


@_attrs_define
class DatabaseServiceUpgrade:
    """Schema for upgrading the service version

    Attributes:
        target_version (str): Version to upgrade the service Example: 12.
    """

    target_version: str

    def to_dict(self) -> dict[str, Any]:
        target_version = self.target_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "target_version": target_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_version = d.pop("target_version")

        database_service_upgrade = cls(
            target_version=target_version,
        )

        return database_service_upgrade
