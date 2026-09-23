from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServiceUserModify")


@_attrs_define
class DatabaseServiceUserModify:
    """Schema for modifying a service user

    Attributes:
        password (str | Unset): New password for the service user
        authentication (str | Unset): Authentication method for the service user
    """

    password: str | Unset = UNSET
    authentication: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        authentication = self.authentication

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if authentication is not UNSET:
            field_dict["authentication"] = authentication

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password", UNSET)

        authentication = d.pop("authentication", UNSET)

        database_service_user_modify = cls(
            password=password,
            authentication=authentication,
        )

        return database_service_user_modify
