from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateSubaccountRequestSubAccountRoles")


@_attrs_define
class CreateSubaccountRequestSubAccountRoles:
    """
    Attributes:
        role (list[str]):
    """

    role: list[str]

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        role = cast(list[str], d.pop("role"))

        create_subaccount_request_sub_account_roles = cls(
            role=role,
        )

        return create_subaccount_request_sub_account_roles
