from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_add_ip_address_ip_address import ServerAddIpAddressIpAddress


T = TypeVar("T", bound="ServerAddIpAddress")


@_attrs_define
class ServerAddIpAddress:
    """Add IP address to a network interface request

    Example:
        {'ip_address': {'address': '10.0.0.30', 'family': 'IPv4'}}

    Attributes:
        ip_address (ServerAddIpAddressIpAddress):
    """

    ip_address: ServerAddIpAddressIpAddress

    def to_dict(self) -> dict[str, Any]:
        ip_address = self.ip_address.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ip_address": ip_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_add_ip_address_ip_address import ServerAddIpAddressIpAddress  # noqa: PLC0415

        d = dict(src_dict)
        ip_address = ServerAddIpAddressIpAddress.from_dict(d.pop("ip_address"))

        server_add_ip_address = cls(
            ip_address=ip_address,
        )

        return server_add_ip_address
