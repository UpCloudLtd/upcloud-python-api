from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.database_service_properties_opensearch_custom_repos_item_type import (
    DatabaseServicePropertiesOpensearchCustomReposItemType,
)

if TYPE_CHECKING:
    from ..models.database_service_properties_opensearch_custom_repos_item_settings_type_0 import (
        DatabaseServicePropertiesOpensearchCustomReposItemSettingsType0,
    )
    from ..models.database_service_properties_opensearch_custom_repos_item_settings_type_1 import (
        DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1,
    )
    from ..models.database_service_properties_opensearch_custom_repos_item_settings_type_2 import (
        DatabaseServicePropertiesOpensearchCustomReposItemSettingsType2,
    )


T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchCustomReposItem")


@_attrs_define
class DatabaseServicePropertiesOpensearchCustomReposItem:
    """
    Attributes:
        name (str):
        settings (DatabaseServicePropertiesOpensearchCustomReposItemSettingsType0 |
            DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1 |
            DatabaseServicePropertiesOpensearchCustomReposItemSettingsType2):
        type_ (DatabaseServicePropertiesOpensearchCustomReposItemType):
    """

    name: str
    settings: (
        DatabaseServicePropertiesOpensearchCustomReposItemSettingsType0
        | DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1
        | DatabaseServicePropertiesOpensearchCustomReposItemSettingsType2
    )
    type_: DatabaseServicePropertiesOpensearchCustomReposItemType

    def to_dict(self) -> dict[str, Any]:
        from ..models.database_service_properties_opensearch_custom_repos_item_settings_type_0 import (
            DatabaseServicePropertiesOpensearchCustomReposItemSettingsType0,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_custom_repos_item_settings_type_1 import (
            DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1,  # noqa: PLC0415
        )

        name = self.name

        settings: dict[str, Any]
        if isinstance(self.settings, DatabaseServicePropertiesOpensearchCustomReposItemSettingsType0):
            settings = self.settings.to_dict()
        elif isinstance(self.settings, DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1):
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
        from ..models.database_service_properties_opensearch_custom_repos_item_settings_type_0 import (
            DatabaseServicePropertiesOpensearchCustomReposItemSettingsType0,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_custom_repos_item_settings_type_1 import (
            DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1,  # noqa: PLC0415
        )
        from ..models.database_service_properties_opensearch_custom_repos_item_settings_type_2 import (
            DatabaseServicePropertiesOpensearchCustomReposItemSettingsType2,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_settings(
            data: object,
        ) -> (
            DatabaseServicePropertiesOpensearchCustomReposItemSettingsType0
            | DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1
            | DatabaseServicePropertiesOpensearchCustomReposItemSettingsType2
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = DatabaseServicePropertiesOpensearchCustomReposItemSettingsType0.from_dict(data)

                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_1 = DatabaseServicePropertiesOpensearchCustomReposItemSettingsType1.from_dict(data)

                return settings_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            settings_type_2 = DatabaseServicePropertiesOpensearchCustomReposItemSettingsType2.from_dict(data)

            return settings_type_2

        settings = _parse_settings(d.pop("settings"))

        type_ = DatabaseServicePropertiesOpensearchCustomReposItemType(d.pop("type"))

        database_service_properties_opensearch_custom_repos_item = cls(
            name=name,
            settings=settings,
            type_=type_,
        )

        return database_service_properties_opensearch_custom_repos_item
