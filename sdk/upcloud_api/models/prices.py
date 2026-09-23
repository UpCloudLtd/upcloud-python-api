from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.prices_prices import PricesPrices


T = TypeVar("T", bound="Prices")


@_attrs_define
class Prices:
    """Price list for UpCloud resources and services.

    Example:
        {'prices': {'currency': 'USD', 'zone': [{'server_cores': {'amount': 1, 'price': 2.4}, 'server_memory':
            {'amount': 1024, 'price': 3.84}, 'storage': {'amount': 1, 'price': 0.04}}]}}

    Attributes:
        prices (PricesPrices):  Example: {'currency': 'USD', 'zone': [{'server_cores': {'amount': 1, 'price': 2.4},
            'server_memory': {'amount': 1024, 'price': 3.84}}]}.
    """

    prices: PricesPrices
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prices = self.prices.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prices": prices,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prices_prices import PricesPrices  # noqa: PLC0415

        d = dict(src_dict)
        prices = PricesPrices.from_dict(d.pop("prices"))

        prices = cls(
            prices=prices,
        )

        prices.additional_properties = d
        return prices

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
