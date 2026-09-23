from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.network_details_servers_server_item import NetworkDetailsServersServerItem


T = TypeVar("T", bound="NetworkDetailsServers")


@_attrs_define
class NetworkDetailsServers:
    """
    Attributes:
        server (list[NetworkDetailsServersServerItem]):
    """

    server: list[NetworkDetailsServersServerItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server = []
        for server_item_data in self.server:
            server_item = server_item_data.to_dict()
            server.append(server_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server": server,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_details_servers_server_item import NetworkDetailsServersServerItem  # noqa: PLC0415

        d = dict(src_dict)
        server = []
        _server = d.pop("server")
        for server_item_data in _server:
            server_item = NetworkDetailsServersServerItem.from_dict(server_item_data)

            server.append(server_item)

        network_details_servers = cls(
            server=server,
        )

        network_details_servers.additional_properties = d
        return network_details_servers

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
