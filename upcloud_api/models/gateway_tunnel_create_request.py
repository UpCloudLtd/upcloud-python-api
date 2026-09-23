from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_tunnel_create_request_ipsec import GatewayTunnelCreateRequestIpsec
    from ..models.gateway_tunnel_create_request_local_address import GatewayTunnelCreateRequestLocalAddress
    from ..models.gateway_tunnel_create_request_remote_address import GatewayTunnelCreateRequestRemoteAddress


T = TypeVar("T", bound="GatewayTunnelCreateRequest")


@_attrs_define
class GatewayTunnelCreateRequest:
    """Network gateway VPN connection tunnel

    Attributes:
        name (str): Name of the tunnel
        local_address (GatewayTunnelCreateRequestLocalAddress): Local peer address
        remote_address (GatewayTunnelCreateRequestRemoteAddress): Remote peer address
        ipsec (GatewayTunnelCreateRequestIpsec): IPsec configuration
        uuid (UUID | Unset): The unique identifier for the resource.
        tunnel_internal_ip (str | Unset): Tunnel internal IP address, "" if disabled Default: ''.
        internal_peer_ping_interval (int | Unset): Internal peer ping interval in seconds, or zero if disabled Default:
            0.
    """

    name: str
    local_address: GatewayTunnelCreateRequestLocalAddress
    remote_address: GatewayTunnelCreateRequestRemoteAddress
    ipsec: GatewayTunnelCreateRequestIpsec
    uuid: UUID | Unset = UNSET
    tunnel_internal_ip: str | Unset = ""
    internal_peer_ping_interval: int | Unset = 0

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        local_address = self.local_address.to_dict()

        remote_address = self.remote_address.to_dict()

        ipsec = self.ipsec.to_dict()

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        tunnel_internal_ip = self.tunnel_internal_ip

        internal_peer_ping_interval = self.internal_peer_ping_interval

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "local_address": local_address,
                "remote_address": remote_address,
                "ipsec": ipsec,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if tunnel_internal_ip is not UNSET:
            field_dict["tunnel_internal_ip"] = tunnel_internal_ip
        if internal_peer_ping_interval is not UNSET:
            field_dict["internal_peer_ping_interval"] = internal_peer_ping_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_tunnel_create_request_ipsec import GatewayTunnelCreateRequestIpsec  # noqa: PLC0415
        from ..models.gateway_tunnel_create_request_local_address import (
            GatewayTunnelCreateRequestLocalAddress,  # noqa: PLC0415
        )
        from ..models.gateway_tunnel_create_request_remote_address import (
            GatewayTunnelCreateRequestRemoteAddress,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        local_address = GatewayTunnelCreateRequestLocalAddress.from_dict(d.pop("local_address"))

        remote_address = GatewayTunnelCreateRequestRemoteAddress.from_dict(d.pop("remote_address"))

        ipsec = GatewayTunnelCreateRequestIpsec.from_dict(d.pop("ipsec"))

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        tunnel_internal_ip = d.pop("tunnel_internal_ip", UNSET)

        internal_peer_ping_interval = d.pop("internal_peer_ping_interval", UNSET)

        gateway_tunnel_create_request = cls(
            name=name,
            local_address=local_address,
            remote_address=remote_address,
            ipsec=ipsec,
            uuid=uuid,
            tunnel_internal_ip=tunnel_internal_ip,
            internal_peer_ping_interval=internal_peer_ping_interval,
        )

        return gateway_tunnel_create_request
