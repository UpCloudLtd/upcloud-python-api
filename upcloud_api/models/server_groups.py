from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_groups_server_groups import ServerGroupsServerGroups


T = TypeVar("T", bound="ServerGroups")


@_attrs_define
class ServerGroups:
    """List of server groups

    Example:
        {'server_groups': {'server_group': [{'anti_affinity': 'yes', 'anti_affinity_status': [{'uuid':
            '00fce2f9-f9f4-46ff-86af-9e60f131f5cb', 'status': 'met'}], 'labels': {'label': [{'key': 'env', 'value':
            'prod'}]}, 'servers': {'server': ['00fce2f9-f9f4-46ff-86af-9e60f131f5cb']}, 'title': 'edge-cluster-a', 'uuid':
            '00fce2f9-f9f4-46ff-86af-9e60f131f5cb'}]}}

    Attributes:
        server_groups (ServerGroupsServerGroups):  Example: {'server_group': [{'anti_affinity': 'yes',
            'anti_affinity_status': [{'uuid': '00fce2f9-f9f4-46ff-86af-9e60f131f5cb', 'status': 'met'}], 'labels': {'label':
            [{'key': 'env', 'value': 'prod'}]}, 'servers': {'server': ['00fce2f9-f9f4-46ff-86af-9e60f131f5cb']}, 'title':
            'edge-cluster-a', 'uuid': '00fce2f9-f9f4-46ff-86af-9e60f131f5cb'}]}.
    """

    server_groups: ServerGroupsServerGroups

    def to_dict(self) -> dict[str, Any]:
        server_groups = self.server_groups.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "server_groups": server_groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_groups_server_groups import ServerGroupsServerGroups  # noqa: PLC0415

        d = dict(src_dict)
        server_groups = ServerGroupsServerGroups.from_dict(d.pop("server_groups"))

        server_groups = cls(
            server_groups=server_groups,
        )

        return server_groups
