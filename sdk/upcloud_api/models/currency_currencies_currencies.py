from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.currency_currencies_currencies_currency_item import CurrencyCurrenciesCurrenciesCurrencyItem


T = TypeVar("T", bound="CurrencyCurrenciesCurrencies")


@_attrs_define
class CurrencyCurrenciesCurrencies:
    """Wrapped collection of currency rate entries.

    Example:
        {'currency': [{'code': 'EUR', 'rate': 0.00846077, 'updated': '2017-12-14T10:00:00Z'}, {'code': 'GBP', 'rate':
            0.00743236, 'updated': '2017-12-14T10:00:00Z'}]}

    Attributes:
        currency (list[CurrencyCurrenciesCurrenciesCurrencyItem]): List of supported currency rate entries.
    """

    currency: list[CurrencyCurrenciesCurrenciesCurrencyItem]

    def to_dict(self) -> dict[str, Any]:
        currency = []
        for currency_item_data in self.currency:
            currency_item = currency_item_data.to_dict()
            currency.append(currency_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "currency": currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency_currencies_currencies_currency_item import (
            CurrencyCurrenciesCurrenciesCurrencyItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        currency = []
        _currency = d.pop("currency")
        for currency_item_data in _currency:
            currency_item = CurrencyCurrenciesCurrenciesCurrencyItem.from_dict(currency_item_data)

            currency.append(currency_item)

        currency_currencies_currencies = cls(
            currency=currency,
        )

        return currency_currencies_currencies
