from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.database_service_properties_opensearch_custom_keystores_item_settings_type_1_google_service_account_credentials_map import (
        DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1GoogleServiceAccountCredentialsMap,
    )


T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1")


@_attrs_define
class DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1:
    """
    Attributes:
        credentials
            (DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1GoogleServiceAccountCredentialsMap):
    """

    credentials: DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1GoogleServiceAccountCredentialsMap

    def to_dict(self) -> dict[str, Any]:
        credentials = self.credentials.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "credentials": credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_properties_opensearch_custom_keystores_item_settings_type_1_google_service_account_credentials_map import (
            DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1GoogleServiceAccountCredentialsMap,  # noqa: PLC0415
        )

        d = dict(src_dict)
        credentials = DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1GoogleServiceAccountCredentialsMap.from_dict(
            d.pop("credentials")
        )

        database_service_properties_opensearch_custom_keystores_item_settings_type_1 = cls(
            credentials=credentials,
        )

        return database_service_properties_opensearch_custom_keystores_item_settings_type_1
