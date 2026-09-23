from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DatabaseServiceTaskCreateUpgradeCheck")


@_attrs_define
class DatabaseServiceTaskCreateUpgradeCheck:
    """
    Attributes:
        target_version (str): The target major version for the upgrade check.
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

        database_service_task_create_upgrade_check = cls(
            target_version=target_version,
        )

        return database_service_task_create_upgrade_check
