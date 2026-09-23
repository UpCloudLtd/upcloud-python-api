from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.database_service_properties_opensearch_custom_keystores_item_type import (
    DatabaseServicePropertiesOpensearchCustomKeystoresItemType,
)

if TYPE_CHECKING:
    from ..models.database_service_properties_opensearch_custom_keystores_item_settings_type_0 import (
        DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType0,
    )
    from ..models.database_service_properties_opensearch_custom_keystores_item_settings_type_1 import (
        DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1,
    )
    from ..models.database_service_properties_opensearch_custom_keystores_item_settings_type_2 import (
        DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType2,
    )


T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchCustomKeystoresItem")


@_attrs_define
class DatabaseServicePropertiesOpensearchCustomKeystoresItem:
    """
    Attributes:
        name (str):
        settings (DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType0 |
            DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1 |
            DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType2):
        type_ (DatabaseServicePropertiesOpensearchCustomKeystoresItemType):
    """

    name: str
    settings: (
        DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType0
        | DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1
        | DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType2
    )
    type_: DatabaseServicePropertiesOpensearchCustomKeystoresItemType

    def to_dict(self) -> dict[str, Any]:
        from ..models.database_service_properties_opensearch_custom_keystores_item_settings_type_0 import (
            DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType0,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_custom_keystores_item_settings_type_1 import (
            DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1,  # noqa: PLC0415
        )

        name = self.name

        settings: dict[str, Any]
        if isinstance(self.settings, DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType0):
            settings = self.settings.to_dict()
        elif isinstance(self.settings, DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1):
            settings = self.settings.to_dict()
        else:
            settings = self.settings.to_dict()

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "settings": settings,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_properties_opensearch_custom_keystores_item_settings_type_0 import (
            DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType0,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_custom_keystores_item_settings_type_1 import (
            DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_custom_keystores_item_settings_type_2 import (
            DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType2,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_settings(
            data: object,
        ) -> (
            DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType0
            | DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1
            | DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType2
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType0.from_dict(data)

                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_1 = DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType1.from_dict(data)

                return settings_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            settings_type_2 = DatabaseServicePropertiesOpensearchCustomKeystoresItemSettingsType2.from_dict(data)

            return settings_type_2

        settings = _parse_settings(d.pop("settings"))

        type_ = DatabaseServicePropertiesOpensearchCustomKeystoresItemType(d.pop("type"))

        database_service_properties_opensearch_custom_keystores_item = cls(
            name=name,
            settings=settings,
            type_=type_,
        )

        return database_service_properties_opensearch_custom_keystores_item
