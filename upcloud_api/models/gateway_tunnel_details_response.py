from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.gateway_tunnel_operational_state import GatewayTunnelOperationalState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_ipsec_details_response import GatewayIpsecDetailsResponse
    from ..models.gateway_local_peer_address_details_response import GatewayLocalPeerAddressDetailsResponse
    from ..models.gateway_remote_peer_address_details_response import GatewayRemotePeerAddressDetailsResponse
    from ..models.gateway_tunnel_internal_ip_details_response import GatewayTunnelInternalIpDetailsResponse


T = TypeVar("T", bound="GatewayTunnelDetailsResponse")


@_attrs_define
class GatewayTunnelDetailsResponse:
    """Response schema for gateway tunnel details.

    Attributes:
        uuid (UUID | Unset): The unique identifier for the resource.
        name (str | Unset): Name of the tunnel
        local_address (GatewayLocalPeerAddressDetailsResponse | Unset): Response schema for local peer address details.
        remote_address (GatewayRemotePeerAddressDetailsResponse | Unset): Response schema for remote peer address
            details.
        ipsec (GatewayIpsecDetailsResponse | Unset): Response schema for IPsec configuration details.
        tunnel_internal_ip (GatewayTunnelInternalIpDetailsResponse | Unset): Response schema for gateway tunnel internal
            IP details.
        internal_peer_ping_interval (int | Unset): Internal peer ping interval in seconds
        operational_state (GatewayTunnelOperationalState | Unset): Tunnel operational state
        created_at (datetime.datetime | Unset): Timestamp of when the tunnel was created.
        updated_at (datetime.datetime | Unset): Timestamp of when the tunnel was last updated.
        tunnel_up (bool | Unset): Indicates whether the tunnel is up
        tunnel_healthy (bool | Unset): Indicates whether the tunnel is healthy
    """

    uuid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    local_address: GatewayLocalPeerAddressDetailsResponse | Unset = UNSET
    remote_address: GatewayRemotePeerAddressDetailsResponse | Unset = UNSET
    ipsec: GatewayIpsecDetailsResponse | Unset = UNSET
    tunnel_internal_ip: GatewayTunnelInternalIpDetailsResponse | Unset = UNSET
    internal_peer_ping_interval: int | Unset = UNSET
    operational_state: GatewayTunnelOperationalState | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    tunnel_up: bool | Unset = UNSET
    tunnel_healthy: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        name = self.name

        local_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.local_address, Unset):
            local_address = self.local_address.to_dict()

        remote_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remote_address, Unset):
            remote_address = self.remote_address.to_dict()

        ipsec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipsec, Unset):
            ipsec = self.ipsec.to_dict()

        tunnel_internal_ip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tunnel_internal_ip, Unset):
            tunnel_internal_ip = self.tunnel_internal_ip.to_dict()

        internal_peer_ping_interval = self.internal_peer_ping_interval

        operational_state: str | Unset = UNSET
        if not isinstance(self.operational_state, Unset):
            operational_state = self.operational_state.value

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        tunnel_up = self.tunnel_up

        tunnel_healthy = self.tunnel_healthy

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if local_address is not UNSET:
            field_dict["local_address"] = local_address
        if remote_address is not UNSET:
            field_dict["remote_address"] = remote_address
        if ipsec is not UNSET:
            field_dict["ipsec"] = ipsec
        if tunnel_internal_ip is not UNSET:
            field_dict["tunnel_internal_ip"] = tunnel_internal_ip
        if internal_peer_ping_interval is not UNSET:
            field_dict["internal_peer_ping_interval"] = internal_peer_ping_interval
        if operational_state is not UNSET:
            field_dict["operational_state"] = operational_state
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if tunnel_up is not UNSET:
            field_dict["tunnel_up"] = tunnel_up
        if tunnel_healthy is not UNSET:
            field_dict["tunnel_healthy"] = tunnel_healthy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_ipsec_details_response import GatewayIpsecDetailsResponse  # noqa: PLC0415
        from ..models.gateway_local_peer_address_details_response import (
            GatewayLocalPeerAddressDetailsResponse,  # noqa: PLC0415
        )
        from ..models.gateway_remote_peer_address_details_response import (
            GatewayRemotePeerAddressDetailsResponse,  # noqa: PLC0415
        )
        from ..models.gateway_tunnel_internal_ip_details_response import (
            GatewayTunnelInternalIpDetailsResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        name = d.pop("name", UNSET)

        _local_address = d.pop("local_address", UNSET)
        local_address: GatewayLocalPeerAddressDetailsResponse | Unset
        if isinstance(_local_address, Unset):
            local_address = UNSET
        else:
            local_address = GatewayLocalPeerAddressDetailsResponse.from_dict(_local_address)

        _remote_address = d.pop("remote_address", UNSET)
        remote_address: GatewayRemotePeerAddressDetailsResponse | Unset
        if isinstance(_remote_address, Unset):
            remote_address = UNSET
        else:
            remote_address = GatewayRemotePeerAddressDetailsResponse.from_dict(_remote_address)

        _ipsec = d.pop("ipsec", UNSET)
        ipsec: GatewayIpsecDetailsResponse | Unset
        if isinstance(_ipsec, Unset):
            ipsec = UNSET
        else:
            ipsec = GatewayIpsecDetailsResponse.from_dict(_ipsec)

        _tunnel_internal_ip = d.pop("tunnel_internal_ip", UNSET)
        tunnel_internal_ip: GatewayTunnelInternalIpDetailsResponse | Unset
        if isinstance(_tunnel_internal_ip, Unset):
            tunnel_internal_ip = UNSET
        else:
            tunnel_internal_ip = GatewayTunnelInternalIpDetailsResponse.from_dict(_tunnel_internal_ip)

        internal_peer_ping_interval = d.pop("internal_peer_ping_interval", UNSET)

        _operational_state = d.pop("operational_state", UNSET)
        operational_state: GatewayTunnelOperationalState | Unset
        if isinstance(_operational_state, Unset):
            operational_state = UNSET
        else:
            operational_state = GatewayTunnelOperationalState(_operational_state)

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

        tunnel_up = d.pop("tunnel_up", UNSET)

        tunnel_healthy = d.pop("tunnel_healthy", UNSET)

        gateway_tunnel_details_response = cls(
            uuid=uuid,
            name=name,
            local_address=local_address,
            remote_address=remote_address,
            ipsec=ipsec,
            tunnel_internal_ip=tunnel_internal_ip,
            internal_peer_ping_interval=internal_peer_ping_interval,
            operational_state=operational_state,
            created_at=created_at,
            updated_at=updated_at,
            tunnel_up=tunnel_up,
            tunnel_healthy=tunnel_healthy,
        )

        return gateway_tunnel_details_response
