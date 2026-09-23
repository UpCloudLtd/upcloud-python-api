from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.database_service_user_create_opensearch_access_control_rules_item import (
        DatabaseServiceUserCreateOpensearchAccessControlRulesItem,
    )


T = TypeVar("T", bound="DatabaseServiceUserCreateOpensearchAccessControl")


@_attrs_define
class DatabaseServiceUserCreateOpensearchAccessControl:
    """OpenSearch access control settings

    Attributes:
        rules (list[DatabaseServiceUserCreateOpensearchAccessControlRulesItem]): List of index permission rules
    """

    rules: list[DatabaseServiceUserCreateOpensearchAccessControlRulesItem]

    def to_dict(self) -> dict[str, Any]:
        rules = []
        for rules_item_data in self.rules:
            rules_item = rules_item_data.to_dict()
            rules.append(rules_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_user_create_opensearch_access_control_rules_item import (
            DatabaseServiceUserCreateOpensearchAccessControlRulesItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        rules = []
        _rules = d.pop("rules")
        for rules_item_data in _rules:
            rules_item = DatabaseServiceUserCreateOpensearchAccessControlRulesItem.from_dict(rules_item_data)

            rules.append(rules_item)

        database_service_user_create_opensearch_access_control = cls(
            rules=rules,
        )

        return database_service_user_create_opensearch_access_control
