from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.accounts_accounts_account_item import AccountsAccountsAccountItem


T = TypeVar("T", bound="AccountsAccounts")


@_attrs_define
class AccountsAccounts:
    """
    Attributes:
        account (list[AccountsAccountsAccountItem]):
    """

    account: list[AccountsAccountsAccountItem]

    def to_dict(self) -> dict[str, Any]:
        account = []
        for account_item_data in self.account:
            account_item = account_item_data.to_dict()
            account.append(account_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "account": account,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accounts_accounts_account_item import AccountsAccountsAccountItem  # noqa: PLC0415

        d = dict(src_dict)
        account = []
        _account = d.pop("account")
        for account_item_data in _account:
            account_item = AccountsAccountsAccountItem.from_dict(account_item_data)

            account.append(account_item)

        accounts_accounts = cls(
            account=account,
        )

        return accounts_accounts
