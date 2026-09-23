from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.create_subaccount_request_sub_account import CreateSubaccountRequestSubAccount


T = TypeVar("T", bound="CreateSubaccountRequest")


@_attrs_define
class CreateSubaccountRequest:
    """Request for creating a subaccount.

    Example:
        {'sub_account': {'first_name': 'first', 'last_name': 'last', 'company': 'my company name', 'address': 'my
            address', 'postal_code': '00130', 'city': 'Helsinki', 'state': '', 'country': 'FIN', 'phone': '+358.31245434',
            'email': 'user@example.com', 'vat_number': 'my vat number', 'timezone': 'Europe/Helsinki', 'username':
            'myusername', 'password': 'mysecr3tPassword', 'currency': 'EUR', 'language': 'en', 'roles': {'role':
            ['technical', 'billing', 'aux_billing']}, 'allow_gui': 'no', 'allow_api': 'yes', 'network_access': {'network':
            []}, 'server_access': {'server': []}, 'storage_access': {'storage': []}, 'tag_access': {'tag': []},
            'ip_filters': {'ip_filter': []}, 'labels': [{'key': 'department', 'value': 'it'}]}}

    Attributes:
        sub_account (CreateSubaccountRequestSubAccount):
    """

    sub_account: CreateSubaccountRequestSubAccount

    def to_dict(self) -> dict[str, Any]:
        sub_account = self.sub_account.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sub_account": sub_account,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_subaccount_request_sub_account import CreateSubaccountRequestSubAccount  # noqa: PLC0415

        d = dict(src_dict)
        sub_account = CreateSubaccountRequestSubAccount.from_dict(d.pop("sub_account"))

        create_subaccount_request = cls(
            sub_account=sub_account,
        )

        return create_subaccount_request
