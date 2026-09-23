from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ZonePricesItemsAdditionalProperty")


@_attrs_define
class ZonePricesItemsAdditionalProperty:
    """
    Attributes:
        amount (int):
        price (float):
    """

    amount: int
    price: float

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        price = self.price

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "price": price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        price = d.pop("price")

        zone_prices_items_additional_property = cls(
            amount=amount,
            price=price,
        )

        return zone_prices_items_additional_property
