from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountBillingSummary")


@_attrs_define
class AccountBillingSummary:
    """Monthly billing totals grouped by resource type and subtype.

    Example:
        {'currency': 'EUR', 'managed_databases': {'managed_database': {'resources': [{'amount': 15.10223, 'details':
            [{'amount': 15.10223, 'hours': 420, 'plan': '1x1xCPU-2GB-25GB', 'zone': 'fi-hel2'}], 'hours': 420,
            'resource_id': '09001a4d-b525-4ab8-835d-000000000000'}], 'total_amount': 15.10223}, 'total_amount': 15.10223},
            'managed_object_storages': {'managed_object_storage': {'resources': [{'amount': 5.03384, 'details': [{'amount':
            5.03384, 'billable_size_gib': 500, 'hours': 420, 'zone': 'fi-hel2'}], 'hours': 420, 'resource_id':
            '127ee42a-8304-477c-84e1-000000000000'}], 'total_amount': 5.03384}, 'total_amount': 5.03384}, 'servers':
            {'server': {'resources': [{'amount': 16.18091, 'details': [{'amount': 16.18091, 'hours': 420, 'labels': [{'key':
            'test', 'value': ''}], 'plan': '2xCPU-4GB', 'zone': 'fi-hel2'}], 'hours': 420, 'resource_id':
            '001c2caa-00dc-4eff-9321-000000000000'}, {'amount': 16.10386, 'details': [{'amount': 16.10386, 'hours': 418,
            'labels': [{'key': 'test2', 'value': ''}], 'plan': '2xCPU-4GB', 'zone': 'fi-hel2'}, {'amount': 0.9288, 'hours':
            12, 'labels': [{'key': 'test2', 'value': ''}], 'plan': '4xCPU-8GB', 'zone': 'fi-hel2'}], 'hours': 430,
            'resource_id': '0010cf04-3608-4512-b4de-000000000000'}], 'total_amount': 33.21357}, 'total_amount': 33.21357},
            'total_amount': 53.34964}

    Attributes:
        currency (str | Unset): ISO 4217 code
        total_amount (float | Unset):
    """

    currency: str | Unset = UNSET
    total_amount: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        total_amount = self.total_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        total_amount = d.pop("total_amount", UNSET)

        account_billing_summary = cls(
            currency=currency,
            total_amount=total_amount,
        )

        account_billing_summary.additional_properties = d
        return account_billing_summary

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
