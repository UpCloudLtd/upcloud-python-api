from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_in_get_server_list import ServerInGetServerList


T = TypeVar("T", bound="GetServerListServers")


@_attrs_define
class GetServerListServers:
    """
    Attributes:
        server (list[ServerInGetServerList] | Unset):
    """

    server: list[ServerInGetServerList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.server, Unset):
            server = []
            for server_item_data in self.server:
                server_item = server_item_data.to_dict()
                server.append(server_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_in_get_server_list import ServerInGetServerList  # noqa: PLC0415

        d = dict(src_dict)
        _server = d.pop("server", UNSET)
        server: list[ServerInGetServerList] | Unset = UNSET
        if _server is not UNSET:
            server = []
            for server_item_data in _server:
                server_item = ServerInGetServerList.from_dict(server_item_data)

                server.append(server_item)

        get_server_list_servers = cls(
            server=server,
        )

        get_server_list_servers.additional_properties = d
        return get_server_list_servers

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
