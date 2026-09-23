from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_servers import NetworkServers


T = TypeVar("T", bound="NetworkTagsTagsTagItem")


@_attrs_define
class NetworkTagsTagsTagItem:
    """
    Attributes:
        name (str): Short name used to identify a tag.
        servers (NetworkServers): List of servers associated with the tag. Example: {'server':
            ['0077fa3d-32db-4b09-9f5f-30d9e9afb565', '00c78863-db86-44ea-af70-d6edc4d162bf']}.
        description (str | Unset): Human-readable description for a tag.
    """

    name: str
    servers: NetworkServers
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        servers = self.servers.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "servers": servers,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_servers import NetworkServers  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        servers = NetworkServers.from_dict(d.pop("servers"))

        description = d.pop("description", UNSET)

        network_tags_tags_tag_item = cls(
            name=name,
            servers=servers,
            description=description,
        )

        network_tags_tags_tag_item.additional_properties = d
        return network_tags_tags_tag_item

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
