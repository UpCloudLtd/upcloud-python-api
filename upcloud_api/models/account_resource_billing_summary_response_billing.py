from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_resource_billing_summary_response_billing_daily_sums import (
        AccountResourceBillingSummaryResponseBillingDailySums,
    )
    from ..models.account_resource_billing_summary_response_billing_details import (
        AccountResourceBillingSummaryResponseBillingDetails,
    )


T = TypeVar("T", bound="AccountResourceBillingSummaryResponseBilling")


@_attrs_define
class AccountResourceBillingSummaryResponseBilling:
    """
    Attributes:
        currency (str | Unset): ISO 4217 code
        daily_sums (AccountResourceBillingSummaryResponseBillingDailySums | Unset):
        details (AccountResourceBillingSummaryResponseBillingDetails | Unset):
        total_amount (float | Unset):
    """

    currency: str | Unset = UNSET
    daily_sums: AccountResourceBillingSummaryResponseBillingDailySums | Unset = UNSET
    details: AccountResourceBillingSummaryResponseBillingDetails | Unset = UNSET
    total_amount: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        daily_sums: dict[str, Any] | Unset = UNSET
        if not isinstance(self.daily_sums, Unset):
            daily_sums = self.daily_sums.to_dict()

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        total_amount = self.total_amount

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if daily_sums is not UNSET:
            field_dict["daily_sums"] = daily_sums
        if details is not UNSET:
            field_dict["details"] = details
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_resource_billing_summary_response_billing_daily_sums import (
            AccountResourceBillingSummaryResponseBillingDailySums,  # noqa: PLC0415
        )
        from ..models.account_resource_billing_summary_response_billing_details import (
            AccountResourceBillingSummaryResponseBillingDetails,  # noqa: PLC0415
        )

        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        _daily_sums = d.pop("daily_sums", UNSET)
        daily_sums: AccountResourceBillingSummaryResponseBillingDailySums | Unset
        if isinstance(_daily_sums, Unset):
            daily_sums = UNSET
        else:
            daily_sums = AccountResourceBillingSummaryResponseBillingDailySums.from_dict(_daily_sums)

        _details = d.pop("details", UNSET)
        details: AccountResourceBillingSummaryResponseBillingDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = AccountResourceBillingSummaryResponseBillingDetails.from_dict(_details)

        total_amount = d.pop("total_amount", UNSET)

        account_resource_billing_summary_response_billing = cls(
            currency=currency,
            daily_sums=daily_sums,
            details=details,
            total_amount=total_amount,
        )

        return account_resource_billing_summary_response_billing
