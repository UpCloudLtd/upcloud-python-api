from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="DatabaseAvailableExtensionsResponseItem")


@_attrs_define
class DatabaseAvailableExtensionsResponseItem:
    """
    Attributes:
        default_version (str): The default version of the extension Example: 1.12.
        name (str): The name of the PostgreSQL extension Example: pg_stat_statements.
        versions (list[str]): List of available versions for this extension Example: ['1.10', '1.11', '1.12'].
    """

    default_version: str
    name: str
    versions: list[str]

    def to_dict(self) -> dict[str, Any]:
        default_version = self.default_version

        name = self.name

        versions = self.versions

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "default_version": default_version,
                "name": name,
                "versions": versions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_version = d.pop("default_version")

        name = d.pop("name")

        versions = cast(list[str], d.pop("versions"))

        database_available_extensions_response_item = cls(
            default_version=default_version,
            name=name,
            versions=versions,
        )

        return database_available_extensions_response_item
