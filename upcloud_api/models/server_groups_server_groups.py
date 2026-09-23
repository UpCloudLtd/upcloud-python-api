from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_group_details import ServerGroupDetails


T = TypeVar("T", bound="ServerGroupsServerGroups")


@_attrs_define
class ServerGroupsServerGroups:
    """
    Example:
        {'server_group': [{'anti_affinity': 'yes', 'anti_affinity_status': [{'uuid':
            '00fce2f9-f9f4-46ff-86af-9e60f131f5cb', 'status': 'met'}], 'labels': {'label': [{'key': 'env', 'value':
            'prod'}]}, 'servers': {'server': ['00fce2f9-f9f4-46ff-86af-9e60f131f5cb']}, 'title': 'edge-cluster-a', 'uuid':
            '00fce2f9-f9f4-46ff-86af-9e60f131f5cb'}]}

    Attributes:
        server_group (list[ServerGroupDetails]):
    """

    server_group: list[ServerGroupDetails]

    def to_dict(self) -> dict[str, Any]:
        server_group = []
        for server_group_item_data in self.server_group:
            server_group_item = server_group_item_data.to_dict()
            server_group.append(server_group_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "server_group": server_group,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_group_details import ServerGroupDetails  # noqa: PLC0415

        d = dict(src_dict)
        server_group = []
        _server_group = d.pop("server_group")
        for server_group_item_data in _server_group:
            server_group_item = ServerGroupDetails.from_dict(server_group_item_data)

            server_group.append(server_group_item)

        server_groups_server_groups = cls(
            server_group=server_group,
        )

        return server_groups_server_groups
