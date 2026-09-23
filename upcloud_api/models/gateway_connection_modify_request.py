from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.gateway_connection_type import GatewayConnectionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_connection_route_request import GatewayConnectionRouteRequest
    from ..models.gateway_tunnel_modify_request import GatewayTunnelModifyRequest


T = TypeVar("T", bound="GatewayConnectionModifyRequest")


@_attrs_define
class GatewayConnectionModifyRequest:
    """Network gateway VPN connection

    Attributes:
        uuid (UUID | Unset): The unique identifier for the resource.
        name (str | Unset): Name of the connection
        type_ (GatewayConnectionType | Unset): Connection type
        local_routes (list[GatewayConnectionRouteRequest] | Unset): Connection local routes
        remote_routes (list[GatewayConnectionRouteRequest] | Unset): Connection remote routes
        tunnels (list[GatewayTunnelModifyRequest] | Unset): Tunnels
    """

    uuid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    type_: GatewayConnectionType | Unset = UNSET
    local_routes: list[GatewayConnectionRouteRequest] | Unset = UNSET
    remote_routes: list[GatewayConnectionRouteRequest] | Unset = UNSET
    tunnels: list[GatewayTunnelModifyRequest] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        local_routes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.local_routes, Unset):
            local_routes = []
            for local_routes_item_data in self.local_routes:
                local_routes_item = local_routes_item_data.to_dict()
                local_routes.append(local_routes_item)

        remote_routes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.remote_routes, Unset):
            remote_routes = []
            for remote_routes_item_data in self.remote_routes:
                remote_routes_item = remote_routes_item_data.to_dict()
                remote_routes.append(remote_routes_item)

        tunnels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tunnels, Unset):
            tunnels = []
            for tunnels_item_data in self.tunnels:
                tunnels_item = tunnels_item_data.to_dict()
                tunnels.append(tunnels_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if local_routes is not UNSET:
            field_dict["local_routes"] = local_routes
        if remote_routes is not UNSET:
            field_dict["remote_routes"] = remote_routes
        if tunnels is not UNSET:
            field_dict["tunnels"] = tunnels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_connection_route_request import GatewayConnectionRouteRequest  # noqa: PLC0415
        from ..models.gateway_tunnel_modify_request import GatewayTunnelModifyRequest  # noqa: PLC0415

        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: GatewayConnectionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GatewayConnectionType(_type_)

        _local_routes = d.pop("local_routes", UNSET)
        local_routes: list[GatewayConnectionRouteRequest] | Unset = UNSET
        if _local_routes is not UNSET:
            local_routes = []
            for local_routes_item_data in _local_routes:
                local_routes_item = GatewayConnectionRouteRequest.from_dict(local_routes_item_data)

                local_routes.append(local_routes_item)

        _remote_routes = d.pop("remote_routes", UNSET)
        remote_routes: list[GatewayConnectionRouteRequest] | Unset = UNSET
        if _remote_routes is not UNSET:
            remote_routes = []
            for remote_routes_item_data in _remote_routes:
                remote_routes_item = GatewayConnectionRouteRequest.from_dict(remote_routes_item_data)

                remote_routes.append(remote_routes_item)

        _tunnels = d.pop("tunnels", UNSET)
        tunnels: list[GatewayTunnelModifyRequest] | Unset = UNSET
        if _tunnels is not UNSET:
            tunnels = []
            for tunnels_item_data in _tunnels:
                tunnels_item = GatewayTunnelModifyRequest.from_dict(tunnels_item_data)

                tunnels.append(tunnels_item)

        gateway_connection_modify_request = cls(
            uuid=uuid,
            name=name,
            type_=type_,
            local_routes=local_routes,
            remote_routes=remote_routes,
            tunnels=tunnels,
        )

        return gateway_connection_modify_request
