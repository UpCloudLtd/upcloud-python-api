from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.gateway_connection_route_type import GatewayConnectionRouteType

T = TypeVar("T", bound="GatewayConnectionRouteRequest")


@_attrs_define
class GatewayConnectionRouteRequest:
    """Network gateway VPN connection route

    Attributes:
        name (str): Route name
        type_ (GatewayConnectionRouteType): Connection route type
        static_network (str): Static network subnet
    """

    name: str
    type_: GatewayConnectionRouteType
    static_network: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        static_network = self.static_network

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
                "static_network": static_network,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = GatewayConnectionRouteType(d.pop("type"))

        static_network = d.pop("static_network")

        gateway_connection_route_request = cls(
            name=name,
            type_=type_,
            static_network=static_network,
        )

        return gateway_connection_route_request
