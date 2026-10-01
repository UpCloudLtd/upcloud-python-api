from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.account_credits_breakdown_account_credits import AccountCreditsBreakdownAccountCredits
    from ..models.account_credits_breakdown_account_free_credits import AccountCreditsBreakdownAccountFreeCredits


T = TypeVar("T", bound="AccountCreditsBreakdown")


@_attrs_define
class AccountCreditsBreakdown:
    """Detailed breakdown of account credits.

    Attributes:
        account_credits (AccountCreditsBreakdownAccountCredits): Paid and debt credits on the account.
        account_free_credits (AccountCreditsBreakdownAccountFreeCredits): Free credits allocated to the account.
        total_credits (float): Total combined credit balance.
    """

    account_credits: AccountCreditsBreakdownAccountCredits
    account_free_credits: AccountCreditsBreakdownAccountFreeCredits
    total_credits: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_credits = self.account_credits.to_dict()

        account_free_credits = self.account_free_credits.to_dict()

        total_credits = self.total_credits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_credits": account_credits,
                "account_free_credits": account_free_credits,
                "total_credits": total_credits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_credits_breakdown_account_credits import (
            AccountCreditsBreakdownAccountCredits,  # noqa: PLC0415
        )
        from ..models.account_credits_breakdown_account_free_credits import (
            AccountCreditsBreakdownAccountFreeCredits,  # noqa: PLC0415
        )

        d = dict(src_dict)
        account_credits = AccountCreditsBreakdownAccountCredits.from_dict(d.pop("account_credits"))

        account_free_credits = AccountCreditsBreakdownAccountFreeCredits.from_dict(d.pop("account_free_credits"))

        total_credits = d.pop("total_credits")

        account_credits_breakdown = cls(
            account_credits=account_credits,
            account_free_credits=account_free_credits,
            total_credits=total_credits,
        )

        account_credits_breakdown.additional_properties = d
        return account_credits_breakdown

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
