from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AccountCreditsBreakdownAccountCredits")


@_attrs_define
class AccountCreditsBreakdownAccountCredits:
    """Paid and debt credits on the account.

    Attributes:
        debt_credits (float): Outstanding debt credits.
        max_debt (float): Maximum allowed debt.
        paid_credits (float): Paid credits on the account.
    """

    debt_credits: float
    max_debt: float
    paid_credits: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        debt_credits = self.debt_credits

        max_debt = self.max_debt

        paid_credits = self.paid_credits

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "debt_credits": debt_credits,
                "max_debt": max_debt,
                "paid_credits": paid_credits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        debt_credits = d.pop("debt_credits")

        max_debt = d.pop("max_debt")

        paid_credits = d.pop("paid_credits")

        account_credits_breakdown_account_credits = cls(
            debt_credits=debt_credits,
            max_debt=max_debt,
            paid_credits=paid_credits,
        )

        account_credits_breakdown_account_credits.additional_properties = d
        return account_credits_breakdown_account_credits

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
