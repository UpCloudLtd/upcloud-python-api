from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.account_billing_summary import AccountBillingSummary


T = TypeVar("T", bound="AccountBillingSummaryResponse")


@_attrs_define
class AccountBillingSummaryResponse:
    """Response containing a monthly billing summary.

    Example:
        {'billing': {'currency': 'EUR', 'networks': {'bandwidth': {'total_amount': 52.136}, 'total_amount': 52.136},
            'managed_databases': {'managed_database': {'total_amount': 80.13127}, 'total_amount': 80.13127},
            'managed_object_storages': {'managed_object_storage': {'total_amount': 2.2253}, 'total_amount': 2.2253},
            'servers': {'server': {'total_amount': 28.05132}, 'total_amount': 28.05132}, 'storages': {'storage':
            {'total_amount': 3.6224}, 'total_amount': 3.6224}, 'total_amount': 166.16629}}

    Attributes:
        billing (AccountBillingSummary): Monthly billing totals grouped by resource type and subtype. Example:
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
            'total_amount': 53.34964}.
    """

    billing: AccountBillingSummary

    def to_dict(self) -> dict[str, Any]:
        billing = self.billing.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "billing": billing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_billing_summary import AccountBillingSummary  # noqa: PLC0415

        d = dict(src_dict)
        billing = AccountBillingSummary.from_dict(d.pop("billing"))

        account_billing_summary_response = cls(
            billing=billing,
        )

        return account_billing_summary_response
