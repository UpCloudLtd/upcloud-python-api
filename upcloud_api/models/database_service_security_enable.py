from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DatabaseServiceSecurityEnable")


@_attrs_define
class DatabaseServiceSecurityEnable:
    """Schema for enabling security on a service instance

    Attributes:
        admin_password (str): Security admin password
    """

    admin_password: str

    def to_dict(self) -> dict[str, Any]:
        admin_password = self.admin_password

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "admin_password": admin_password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        admin_password = d.pop("admin_password")

        database_service_security_enable = cls(
            admin_password=admin_password,
        )

        return database_service_security_enable
