from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkServers")


@_attrs_define
class NetworkServers:
    """List of servers associated with the tag.

    Example:
        {'server': ['0077fa3d-32db-4b09-9f5f-30d9e9afb565', '00c78863-db86-44ea-af70-d6edc4d162bf']}

    Attributes:
        server (list[UUID] | Unset):
    """

    server: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server: list[str] | Unset = UNSET
        if not isinstance(self.server, Unset):
            server = []
            for server_item_data in self.server:
                server_item = str(server_item_data)
                server.append(server_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _server = d.pop("server", UNSET)
        server: list[UUID] | Unset = UNSET
        if _server is not UNSET:
            server = []
            for server_item_data in _server:
                server_item = UUID(server_item_data)

                server.append(server_item)

        network_servers = cls(
            server=server,
        )

        network_servers.additional_properties = d
        return network_servers

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
