from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServiceAclModify")


@_attrs_define
class DatabaseServiceAclModify:
    """Schema for modifying service access control settings.

    Attributes:
        access_control (bool | Unset): Enables OpenSearch access control
        extended_access_control (bool | Unset): Enables OpenSearch extended access control
    """

    access_control: bool | Unset = UNSET
    extended_access_control: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        access_control = self.access_control

        extended_access_control = self.extended_access_control

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if access_control is not UNSET:
            field_dict["access_control"] = access_control
        if extended_access_control is not UNSET:
            field_dict["extended_access_control"] = extended_access_control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_control = d.pop("access_control", UNSET)

        extended_access_control = d.pop("extended_access_control", UNSET)

        database_service_acl_modify = cls(
            access_control=access_control,
            extended_access_control=extended_access_control,
        )

        return database_service_acl_modify
