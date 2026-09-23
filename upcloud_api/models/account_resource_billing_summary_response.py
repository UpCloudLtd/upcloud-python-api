from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.account_resource_billing_summary_response_billing import AccountResourceBillingSummaryResponseBilling


T = TypeVar("T", bound="AccountResourceBillingSummaryResponse")


@_attrs_define
class AccountResourceBillingSummaryResponse:
    """Response containing the monthly billing summary for a resource.

    Example:
        {'billing': {'daily_sums': {'2019-12-02': 3.33684, '2019-12-03': 52.77344, '2019-12-04': 1.07424, '2019-12-05':
            1.07424, '2019-12-06': 1.07424, '2019-12-07': 1.07424, '2019-12-08': 1.07424, '2019-12-09': 1.07424,
            '2019-12-12': 3.22272, '2019-12-13': 0.58188}, 'details': {'hours': 792, 'plan': '1xCPU-1GB', 'resource_id':
            '00ce9363-9065-4c2a-9d66-3b0c762f556b', 'title': 'My Glorious Server', 'type': 'server', 'zone': 'fi-hel1'},
            'total_amount': 66.36032}}

    Attributes:
        billing (AccountResourceBillingSummaryResponseBilling):
    """

    billing: AccountResourceBillingSummaryResponseBilling

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
        from ..models.account_resource_billing_summary_response_billing import (
            AccountResourceBillingSummaryResponseBilling,  # noqa: PLC0415
        )

        d = dict(src_dict)
        billing = AccountResourceBillingSummaryResponseBilling.from_dict(d.pop("billing"))

        account_resource_billing_summary_response = cls(
            billing=billing,
        )

        return account_resource_billing_summary_response
