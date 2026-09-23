from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DatabaseServiceUserCreatePgAccessControl")


@_attrs_define
class DatabaseServiceUserCreatePgAccessControl:
    """PostgreSQL access control settings

    Attributes:
        allow_replication (bool): Flag to allow or disallow replication
    """

    allow_replication: bool

    def to_dict(self) -> dict[str, Any]:
        allow_replication = self.allow_replication

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "allow_replication": allow_replication,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_replication = d.pop("allow_replication")

        database_service_user_create_pg_access_control = cls(
            allow_replication=allow_replication,
        )

        return database_service_user_create_pg_access_control
