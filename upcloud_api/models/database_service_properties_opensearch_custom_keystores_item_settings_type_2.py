from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType2")


@_attrs_define
class DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType2:
    """
    Attributes:
        access_key (str):
        secret_key (str): AWS secret key
    """

    access_key: str
    secret_key: str

    def to_dict(self) -> dict[str, Any]:
        access_key = self.access_key

        secret_key = self.secret_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "access_key": access_key,
                "secret_key": secret_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_key = d.pop("access_key")

        secret_key = d.pop("secret_key")

        database_service_properties_opensearch_custom_keystores_item_settings_type_2 = cls(
            access_key=access_key,
            secret_key=secret_key,
        )

        return database_service_properties_opensearch_custom_keystores_item_settings_type_2
