from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_details_peerings_peering_item import NetworkDetailsPeeringsPeeringItem


T = TypeVar("T", bound="NetworkDetailsPeerings")


@_attrs_define
class NetworkDetailsPeerings:
    """List of network peerings the network is part of

    Attributes:
        peering (list[NetworkDetailsPeeringsPeeringItem] | Unset):
    """

    peering: list[NetworkDetailsPeeringsPeeringItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        peering: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.peering, Unset):
            peering = []
            for peering_item_data in self.peering:
                peering_item = peering_item_data.to_dict()
                peering.append(peering_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if peering is not UNSET:
            field_dict["peering"] = peering

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_details_peerings_peering_item import NetworkDetailsPeeringsPeeringItem  # noqa: PLC0415

        d = dict(src_dict)
        _peering = d.pop("peering", UNSET)
        peering: list[NetworkDetailsPeeringsPeeringItem] | Unset = UNSET
        if _peering is not UNSET:
            peering = []
            for peering_item_data in _peering:
                peering_item = NetworkDetailsPeeringsPeeringItem.from_dict(peering_item_data)

                peering.append(peering_item)

        network_details_peerings = cls(
            peering=peering,
        )

        network_details_peerings.additional_properties = d
        return network_details_peerings

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
