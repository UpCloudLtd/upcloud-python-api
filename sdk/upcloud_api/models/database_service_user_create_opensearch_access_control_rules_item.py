from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DatabaseServiceUserCreateOpensearchAccessControlRulesItem")


@_attrs_define
class DatabaseServiceUserCreateOpensearchAccessControlRulesItem:
    """
    Attributes:
        index (str): The index pattern for the rule
        permission (str): The permission level for the index
    """

    index: str
    permission: str

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        permission = self.permission

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "index": index,
                "permission": permission,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index")

        permission = d.pop("permission")

        database_service_user_create_opensearch_access_control_rules_item = cls(
            index=index,
            permission=permission,
        )

        return database_service_user_create_opensearch_access_control_rules_item
