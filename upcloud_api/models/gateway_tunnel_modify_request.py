from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_tunnel_modify_request_ipsec import GatewayTunnelModifyRequestIpsec
    from ..models.gateway_tunnel_modify_request_local_address import GatewayTunnelModifyRequestLocalAddress
    from ..models.gateway_tunnel_modify_request_remote_address import GatewayTunnelModifyRequestRemoteAddress


T = TypeVar("T", bound="GatewayTunnelModifyRequest")


@_attrs_define
class GatewayTunnelModifyRequest:
    """Request to modify a VPN tunnel

    Attributes:
        uuid (UUID | Unset): The unique identifier for the resource.
        name (str | Unset): Name of the tunnel
        local_address (GatewayTunnelModifyRequestLocalAddress | Unset): Local peer address
        remote_address (GatewayTunnelModifyRequestRemoteAddress | Unset): Remote peer address
        ipsec (GatewayTunnelModifyRequestIpsec | Unset): IPsec configuration
        tunnel_internal_ip (str | Unset): Tunnel internal IP address, "" if disabled
        internal_peer_ping_interval (int | Unset): Internal peer ping interval in seconds, or zero if disabled
    """

    uuid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    local_address: GatewayTunnelModifyRequestLocalAddress | Unset = UNSET
    remote_address: GatewayTunnelModifyRequestRemoteAddress | Unset = UNSET
    ipsec: GatewayTunnelModifyRequestIpsec | Unset = UNSET
    tunnel_internal_ip: str | Unset = UNSET
    internal_peer_ping_interval: int | Unset = UNSET

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

        tunnel_internal_ip = self.tunnel_internal_ip

        internal_peer_ping_interval = self.internal_peer_ping_interval

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_tunnel_modify_request_ipsec import GatewayTunnelModifyRequestIpsec  # noqa: PLC0415
        from ..models.gateway_tunnel_modify_request_local_address import (
            GatewayTunnelModifyRequestLocalAddress,  # noqa: PLC0415
        )
        from ..models.gateway_tunnel_modify_request_remote_address import (
            GatewayTunnelModifyRequestRemoteAddress,  # noqa: PLC0415
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
        local_address: GatewayTunnelModifyRequestLocalAddress | Unset
        if isinstance(_local_address, Unset):
            local_address = UNSET
        else:
            local_address = GatewayTunnelModifyRequestLocalAddress.from_dict(_local_address)

        _remote_address = d.pop("remote_address", UNSET)
        remote_address: GatewayTunnelModifyRequestRemoteAddress | Unset
        if isinstance(_remote_address, Unset):
            remote_address = UNSET
        else:
            remote_address = GatewayTunnelModifyRequestRemoteAddress.from_dict(_remote_address)

        _ipsec = d.pop("ipsec", UNSET)
        ipsec: GatewayTunnelModifyRequestIpsec | Unset
        if isinstance(_ipsec, Unset):
            ipsec = UNSET
        else:
            ipsec = GatewayTunnelModifyRequestIpsec.from_dict(_ipsec)

        tunnel_internal_ip = d.pop("tunnel_internal_ip", UNSET)

        internal_peer_ping_interval = d.pop("internal_peer_ping_interval", UNSET)

        gateway_tunnel_modify_request = cls(
            uuid=uuid,
            name=name,
            local_address=local_address,
            remote_address=remote_address,
            ipsec=ipsec,
            tunnel_internal_ip=tunnel_internal_ip,
            internal_peer_ping_interval=internal_peer_ping_interval,
        )

        return gateway_tunnel_modify_request
