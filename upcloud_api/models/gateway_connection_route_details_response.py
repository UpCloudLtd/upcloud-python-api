from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gateway_connection_route_type import GatewayConnectionRouteType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayConnectionRouteDetailsResponse")


@_attrs_define
class GatewayConnectionRouteDetailsResponse:
    """Response schema for gateway connection route details.

    Attributes:
        name (str | Unset): Name of the connection
        type_ (GatewayConnectionRouteType | Unset): Connection route type
        static_network (str | Unset): Static network for the connection route
    """

    name: str | Unset = UNSET
    type_: GatewayConnectionRouteType | Unset = UNSET
    static_network: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        static_network = self.static_network

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if static_network is not UNSET:
            field_dict["static_network"] = static_network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: GatewayConnectionRouteType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GatewayConnectionRouteType(_type_)

        static_network = d.pop("static_network", UNSET)

        gateway_connection_route_details_response = cls(
            name=name,
            type_=type_,
            static_network=static_network,
        )

        gateway_connection_route_details_response.additional_properties = d
        return gateway_connection_route_details_response

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
