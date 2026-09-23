from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.gateway_connection_type import GatewayConnectionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_connection_route_request import GatewayConnectionRouteRequest
    from ..models.gateway_tunnel_create_request import GatewayTunnelCreateRequest


T = TypeVar("T", bound="GatewayConnectionCreateRequest")


@_attrs_define
class GatewayConnectionCreateRequest:
    """Network gateway VPN connection

    Attributes:
        name (str): Name of the connection
        type_ (GatewayConnectionType): Connection type
        uuid (UUID | Unset): The unique identifier for the resource.
        local_routes (list[GatewayConnectionRouteRequest] | Unset): Connection local routes
        remote_routes (list[GatewayConnectionRouteRequest] | Unset): Connection remote routes
        tunnels (list[GatewayTunnelCreateRequest] | Unset): Connection tunnels
    """

    name: str
    type_: GatewayConnectionType
    uuid: UUID | Unset = UNSET
    local_routes: list[GatewayConnectionRouteRequest] | Unset = UNSET
    remote_routes: list[GatewayConnectionRouteRequest] | Unset = UNSET
    tunnels: list[GatewayTunnelCreateRequest] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

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

        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
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
        from ..models.gateway_tunnel_create_request import GatewayTunnelCreateRequest  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        type_ = GatewayConnectionType(d.pop("type"))

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

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
        tunnels: list[GatewayTunnelCreateRequest] | Unset = UNSET
        if _tunnels is not UNSET:
            tunnels = []
            for tunnels_item_data in _tunnels:
                tunnels_item = GatewayTunnelCreateRequest.from_dict(tunnels_item_data)

                tunnels.append(tunnels_item)

        gateway_connection_create_request = cls(
            name=name,
            type_=type_,
            uuid=uuid,
            local_routes=local_routes,
            remote_routes=remote_routes,
            tunnels=tunnels,
        )

        return gateway_connection_create_request
