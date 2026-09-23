from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.currency_currencies_currencies import CurrencyCurrenciesCurrencies


T = TypeVar("T", bound="CurrencyCurrencies")


@_attrs_define
class CurrencyCurrencies:
    """Response schema for listing supported currencies and exchange rates.

    Example:
        {'currencies': {'currency': [{'code': 'EUR', 'rate': 0.00846077, 'updated': '2017-12-14T10:00:00Z'}, {'code':
            'GBP', 'rate': 0.00743236, 'updated': '2017-12-14T10:00:00Z'}, {'code': 'SGD', 'rate': 0.01347685, 'updated':
            '2017-12-14T10:00:00Z'}, {'code': 'USD', 'rate': 0.01, 'updated': '2017-12-15T06:44:47Z'}]}}

    Attributes:
        currencies (CurrencyCurrenciesCurrencies): Wrapped collection of currency rate entries. Example: {'currency':
            [{'code': 'EUR', 'rate': 0.00846077, 'updated': '2017-12-14T10:00:00Z'}, {'code': 'GBP', 'rate': 0.00743236,
            'updated': '2017-12-14T10:00:00Z'}]}.
    """

    currencies: CurrencyCurrenciesCurrencies

    def to_dict(self) -> dict[str, Any]:
        currencies = self.currencies.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "currencies": currencies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency_currencies_currencies import CurrencyCurrenciesCurrencies  # noqa: PLC0415

        d = dict(src_dict)
        currencies = CurrencyCurrenciesCurrencies.from_dict(d.pop("currencies"))

        currency_currencies = cls(
            currencies=currencies,
        )

        return currency_currencies
