from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CurrencyCurrenciesCurrenciesCurrencyItem")


@_attrs_define
class CurrencyCurrenciesCurrenciesCurrencyItem:
    """
    Example:
        {'code': 'USD', 'rate': 0.01, 'updated': '2017-12-15T06:44:47Z'}

    Attributes:
        code (str): ISO 4217 code
        rate (float):
        updated (datetime.datetime):
    """

    code: str
    rate: float
    updated: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        rate = self.rate

        updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "rate": rate,
                "updated": updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        rate = d.pop("rate")

        updated = datetime.datetime.fromisoformat(d.pop("updated"))

        currency_currencies_currencies_currency_item = cls(
            code=code,
            rate=rate,
            updated=updated,
        )

        currency_currencies_currencies_currency_item.additional_properties = d
        return currency_currencies_currencies_currency_item

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
