from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.modify_network_request_network import ModifyNetworkRequestNetwork


T = TypeVar("T", bound="ModifyNetworkRequest")


@_attrs_define
class ModifyNetworkRequest:
    """Request schema for modifying a network

    Attributes:
        network (ModifyNetworkRequestNetwork):
    """

    network: ModifyNetworkRequestNetwork
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = self.network.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network": network,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.modify_network_request_network import ModifyNetworkRequestNetwork  # noqa: PLC0415

        d = dict(src_dict)
        network = ModifyNetworkRequestNetwork.from_dict(d.pop("network"))

        modify_network_request = cls(
            network=network,
        )

        modify_network_request.additional_properties = d
        return modify_network_request

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
