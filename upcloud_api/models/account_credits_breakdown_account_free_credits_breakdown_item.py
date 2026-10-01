from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountCreditsBreakdownAccountFreeCreditsBreakdownItem")


@_attrs_define
class AccountCreditsBreakdownAccountFreeCreditsBreakdownItem:
    """
    Attributes:
        free_credit_type (str): Type identifier for the free credit grant.
        free_credits (float): Amount of free credits.
        free_credits_expire (datetime.datetime | Unset): Expiry date-time of the free credits in ISO 8601 format. Absent
            if the credits do not expire.
    """

    free_credit_type: str
    free_credits: float
    free_credits_expire: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        free_credit_type = self.free_credit_type

        free_credits = self.free_credits

        free_credits_expire: str | Unset = UNSET
        if not isinstance(self.free_credits_expire, Unset):
            free_credits_expire = self.free_credits_expire.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "free_credit_type": free_credit_type,
                "free_credits": free_credits,
            }
        )
        if free_credits_expire is not UNSET:
            field_dict["free_credits_expire"] = free_credits_expire

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        free_credit_type = d.pop("free_credit_type")

        free_credits = d.pop("free_credits")

        _free_credits_expire = d.pop("free_credits_expire", UNSET)
        free_credits_expire: datetime.datetime | Unset
        if isinstance(_free_credits_expire, Unset):
            free_credits_expire = UNSET
        else:
            free_credits_expire = datetime.datetime.fromisoformat(_free_credits_expire)

        account_credits_breakdown_account_free_credits_breakdown_item = cls(
            free_credit_type=free_credit_type,
            free_credits=free_credits,
            free_credits_expire=free_credits_expire,
        )

        account_credits_breakdown_account_free_credits_breakdown_item.additional_properties = d
        return account_credits_breakdown_account_free_credits_breakdown_item

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
