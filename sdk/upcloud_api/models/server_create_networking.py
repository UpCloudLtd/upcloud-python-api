from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_create_networking_interfaces import ServerCreateNetworkingInterfaces


T = TypeVar("T", bound="ServerCreateNetworking")


@_attrs_define
class ServerCreateNetworking:
    """Network interfaces for a new Cloud Server

    Example:
        {'interfaces': {'interface': [{'ip_addresses': {'ip_address': [{'family': 'IPv4'}]}, 'type': 'public'}]}}

    Attributes:
        interfaces (ServerCreateNetworkingInterfaces):
    """

    interfaces: ServerCreateNetworkingInterfaces

    def to_dict(self) -> dict[str, Any]:
        interfaces = self.interfaces.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "interfaces": interfaces,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_create_networking_interfaces import ServerCreateNetworkingInterfaces  # noqa: PLC0415

        d = dict(src_dict)
        interfaces = ServerCreateNetworkingInterfaces.from_dict(d.pop("interfaces"))

        server_create_networking = cls(
            interfaces=interfaces,
        )

        return server_create_networking
