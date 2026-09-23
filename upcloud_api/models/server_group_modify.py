from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_group_modify_server_group import ServerGroupModifyServerGroup


T = TypeVar("T", bound="ServerGroupModify")


@_attrs_define
class ServerGroupModify:
    """A schema for creating/modifying a server group

    Example:
        {'server_group': {'title': 'edge-cluster-a', 'servers': {'servers': ['00fce2f9-f9f4-46ff-86af-9e60f131f5cb']},
            'labels': {'label': [{'key': 'env', 'value': 'prod'}]}, 'anti_affinity': 'yes'}}

    Attributes:
        server_group (ServerGroupModifyServerGroup):  Example: {'title': 'edge-cluster-a', 'servers': {'servers':
            ['00fce2f9-f9f4-46ff-86af-9e60f131f5cb']}, 'labels': {'label': [{'key': 'env', 'value': 'prod'}]},
            'anti_affinity': 'yes'}.
    """

    server_group: ServerGroupModifyServerGroup

    def to_dict(self) -> dict[str, Any]:
        server_group = self.server_group.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "server_group": server_group,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_group_modify_server_group import ServerGroupModifyServerGroup  # noqa: PLC0415

        d = dict(src_dict)
        server_group = ServerGroupModifyServerGroup.from_dict(d.pop("server_group"))

        server_group_modify = cls(
            server_group=server_group,
        )

        return server_group_modify
