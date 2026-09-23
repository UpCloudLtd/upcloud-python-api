from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.zone_prices import ZonePrices


T = TypeVar("T", bound="PricesPrices")


@_attrs_define
class PricesPrices:
    """
    Example:
        {'currency': 'USD', 'zone': [{'server_cores': {'amount': 1, 'price': 2.4}, 'server_memory': {'amount': 1024,
            'price': 3.84}}]}

    Attributes:
        currency (str): ISO 4217 code
        zone (list[ZonePrices]):
    """

    currency: str
    zone: list[ZonePrices]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        zone = []
        for zone_item_data in self.zone:
            zone_item = zone_item_data.to_dict()
            zone.append(zone_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "zone": zone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.zone_prices import ZonePrices  # noqa: PLC0415

        d = dict(src_dict)
        currency = d.pop("currency")

        zone = []
        _zone = d.pop("zone")
        for zone_item_data in _zone:
            zone_item = ZonePrices.from_dict(zone_item_data)

            zone.append(zone_item)

        prices_prices = cls(
            currency=currency,
            zone=zone,
        )

        prices_prices.additional_properties = d
        return prices_prices

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
