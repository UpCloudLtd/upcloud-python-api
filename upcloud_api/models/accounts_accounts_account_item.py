from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.accounts_accounts_account_item_type import AccountsAccountsAccountItemType

if TYPE_CHECKING:
    from ..models.account_label import AccountLabel
    from ..models.accounts_accounts_account_item_roles import AccountsAccountsAccountItemRoles


T = TypeVar("T", bound="AccountsAccountsAccountItem")


@_attrs_define
class AccountsAccountsAccountItem:
    """
    Attributes:
        type_ (AccountsAccountsAccountItemType):
        username (str): Username for an account.
        roles (AccountsAccountsAccountItemRoles):
        labels (list[AccountLabel]):
    """

    type_: AccountsAccountsAccountItemType
    username: str
    roles: AccountsAccountsAccountItemRoles
    labels: list[AccountLabel]

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        username = self.username

        roles = self.roles.to_dict()

        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.to_dict()
            labels.append(labels_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "username": username,
                "roles": roles,
                "labels": labels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_label import AccountLabel  # noqa: PLC0415
        from ..models.accounts_accounts_account_item_roles import AccountsAccountsAccountItemRoles  # noqa: PLC0415

        d = dict(src_dict)
        type_ = AccountsAccountsAccountItemType(d.pop("type"))

        username = d.pop("username")

        roles = AccountsAccountsAccountItemRoles.from_dict(d.pop("roles"))

        labels = []
        _labels = d.pop("labels")
        for labels_item_data in _labels:
            labels_item = AccountLabel.from_dict(labels_item_data)

            labels.append(labels_item)

        accounts_accounts_account_item = cls(
            type_=type_,
            username=username,
            roles=roles,
            labels=labels,
        )

        return accounts_accounts_account_item
