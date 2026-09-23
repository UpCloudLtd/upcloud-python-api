from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.database_pg_available_extensions_response_item_extensions_item import (
        DatabasePGAvailableExtensionsResponseItemExtensionsItem,
    )


T = TypeVar("T", bound="DatabasePGAvailableExtensionsResponseItem")


@_attrs_define
class DatabasePGAvailableExtensionsResponseItem:
    """
    Attributes:
        version (str): The PostgreSQL major version Example: 16.
        extensions (list[DatabasePGAvailableExtensionsResponseItemExtensionsItem]): List of available extensions for
            this PostgreSQL version
    """

    version: str
    extensions: list[DatabasePGAvailableExtensionsResponseItemExtensionsItem]

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        extensions = []
        for extensions_item_data in self.extensions:
            extensions_item = extensions_item_data.to_dict()
            extensions.append(extensions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "version": version,
                "extensions": extensions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_pg_available_extensions_response_item_extensions_item import (
            DatabasePGAvailableExtensionsResponseItemExtensionsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        version = d.pop("version")

        extensions = []
        _extensions = d.pop("extensions")
        for extensions_item_data in _extensions:
            extensions_item = DatabasePGAvailableExtensionsResponseItemExtensionsItem.from_dict(extensions_item_data)

            extensions.append(extensions_item)

        database_pg_available_extensions_response_item = cls(
            version=version,
            extensions=extensions,
        )

        return database_pg_available_extensions_response_item
