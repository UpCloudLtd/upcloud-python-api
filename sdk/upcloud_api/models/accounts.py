from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.accounts_accounts import AccountsAccounts


T = TypeVar("T", bound="Accounts")


@_attrs_define
class Accounts:
    """Main account and subaccounts accessible to the authenticated account.

    Example:
        {'accounts': {'account': [{'labels': [], 'roles': {'role': ['technical']}, 'type': 'mymain', 'username':
            'test'}, {'labels': [], 'roles': {'role': ['technical']}, 'type': 'sub', 'username': 'my_sub_account'},
            {'labels': [{'key': 'to_be_removed', 'value': 'after 2022-31-12'}], 'roles': {'role': []}, 'type': 'sub',
            'username': 'my_temp_account'}, {'labels': [], 'roles': {'role': ['billing']}, 'type': 'sub', 'username':
            'my_billing_account'}]}}

    Attributes:
        accounts (AccountsAccounts):
    """

    accounts: AccountsAccounts

    def to_dict(self) -> dict[str, Any]:
        accounts = self.accounts.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accounts": accounts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.accounts_accounts import AccountsAccounts  # noqa: PLC0415

        d = dict(src_dict)
        accounts = AccountsAccounts.from_dict(d.pop("accounts"))

        accounts = cls(
            accounts=accounts,
        )

        return accounts
