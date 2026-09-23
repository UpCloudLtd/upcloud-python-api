from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gateway_connection_type import GatewayConnectionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_connection_route_details_response import GatewayConnectionRouteDetailsResponse
    from ..models.gateway_tunnel_details_response import GatewayTunnelDetailsResponse


T = TypeVar("T", bound="GatewayConnectionDetailsResponse")


@_attrs_define
class GatewayConnectionDetailsResponse:
    """Response schema for gateway connection details.

    Attributes:
        uuid (UUID | Unset): The unique identifier for the resource.
        name (str | Unset): Name of the connection
        type_ (GatewayConnectionType | Unset): Connection type
        local_routes (list[GatewayConnectionRouteDetailsResponse] | Unset): Local routes for the connection
        remote_routes (list[GatewayConnectionRouteDetailsResponse] | Unset): Remote routes for the connection
        tunnels (list[GatewayTunnelDetailsResponse] | Unset):
        created_at (datetime.datetime | Unset): Timestamp of when the connection was created.
        updated_at (datetime.datetime | Unset): Timestamp of when the connection was last updated.
    """

    uuid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    type_: GatewayConnectionType | Unset = UNSET
    local_routes: list[GatewayConnectionRouteDetailsResponse] | Unset = UNSET
    remote_routes: list[GatewayConnectionRouteDetailsResponse] | Unset = UNSET
    tunnels: list[GatewayTunnelDetailsResponse] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_connection_route_details_response import (
            GatewayConnectionRouteDetailsResponse,  # noqa: PLC0415
        )
        from ..models.gateway_tunnel_details_response import GatewayTunnelDetailsResponse  # noqa: PLC0415

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
        local_routes: list[GatewayConnectionRouteDetailsResponse] | Unset = UNSET
        if _local_routes is not UNSET:
            local_routes = []
            for local_routes_item_data in _local_routes:
                local_routes_item = GatewayConnectionRouteDetailsResponse.from_dict(local_routes_item_data)

                local_routes.append(local_routes_item)

        _remote_routes = d.pop("remote_routes", UNSET)
        remote_routes: list[GatewayConnectionRouteDetailsResponse] | Unset = UNSET
        if _remote_routes is not UNSET:
            remote_routes = []
            for remote_routes_item_data in _remote_routes:
                remote_routes_item = GatewayConnectionRouteDetailsResponse.from_dict(remote_routes_item_data)

                remote_routes.append(remote_routes_item)

        _tunnels = d.pop("tunnels", UNSET)
        tunnels: list[GatewayTunnelDetailsResponse] | Unset = UNSET
        if _tunnels is not UNSET:
            tunnels = []
            for tunnels_item_data in _tunnels:
                tunnels_item = GatewayTunnelDetailsResponse.from_dict(tunnels_item_data)

                tunnels.append(tunnels_item)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        gateway_connection_details_response = cls(
            uuid=uuid,
            name=name,
            type_=type_,
            local_routes=local_routes,
            remote_routes=remote_routes,
            tunnels=tunnels,
            created_at=created_at,
            updated_at=updated_at,
        )

        gateway_connection_details_response.additional_properties = d
        return gateway_connection_details_response

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
