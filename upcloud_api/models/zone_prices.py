from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.zone_prices_items import ZonePricesItems


T = TypeVar("T", bound="ZonePrices")


@_attrs_define
class ZonePrices:
    """Pricing information organized by zone.

    Attributes:
        items (ZonePricesItems | Unset):
    """

    items: ZonePricesItems | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: dict[str, Any] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.zone_prices_items import ZonePricesItems  # noqa: PLC0415

        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: ZonePricesItems | Unset
        if isinstance(_items, Unset):
            items = UNSET
        else:
            items = ZonePricesItems.from_dict(_items)

        zone_prices = cls(
            items=items,
        )

        zone_prices.additional_properties = d
        return zone_prices

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
