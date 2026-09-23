from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AccountsAccountsAccountItemRoles")


@_attrs_define
class AccountsAccountsAccountItemRoles:
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

        accounts_accounts_account_item_roles = cls(
            role=role,
        )

        return accounts_accounts_account_item_roles
