from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DatabaseServiceSecurityModify")


@_attrs_define
class DatabaseServiceSecurityModify:
    """Schema for modifying service security settings

    Attributes:
        admin_password (str): Current admin password
        new_password (str): New admin password
    """

    admin_password: str
    new_password: str

    def to_dict(self) -> dict[str, Any]:
        admin_password = self.admin_password

        new_password = self.new_password

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "admin_password": admin_password,
                "new_password": new_password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        admin_password = d.pop("admin_password")

        new_password = d.pop("new_password")

        database_service_security_modify = cls(
            admin_password=admin_password,
            new_password=new_password,
        )

        return database_service_security_modify
