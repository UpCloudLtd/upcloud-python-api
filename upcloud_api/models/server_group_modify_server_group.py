from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.server_group_anti_affinity import ServerGroupAntiAffinity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_group_modify_server_group_labels import ServerGroupModifyServerGroupLabels
    from ..models.server_group_servers import ServerGroupServers


T = TypeVar("T", bound="ServerGroupModifyServerGroup")


@_attrs_define
class ServerGroupModifyServerGroup:
    """
    Example:
        {'title': 'edge-cluster-a', 'servers': {'servers': ['00fce2f9-f9f4-46ff-86af-9e60f131f5cb']}, 'labels':
            {'label': [{'key': 'env', 'value': 'prod'}]}, 'anti_affinity': 'yes'}

    Attributes:
        title (str | Unset): The name of the server group Example: edge-cluster-a.
        servers (ServerGroupServers | Unset): List of server UUIDs in the server group Example: {'servers':
            ['00fce2f9-f9f4-46ff-86af-9e60f131f5cb', '0414e0d7-4436-4037-9dd8-6eaf47dce599']}.
        labels (ServerGroupModifyServerGroupLabels | Unset): Labels to categorize the server group Example: {'label':
            [{'key': 'env', 'value': 'prod'}]}.
        anti_affinity (ServerGroupAntiAffinity | Unset): Anti-affinity policy for server groups. Possible values are
            'strict', 'yes', or 'no'. 'strict' ensures that no two servers in the group are placed on the same physical
            host. 'yes' indicates a preference for anti-affinity but does not guarantee it. 'no' means there is no anti-
            affinity requirement.
    """

    title: str | Unset = UNSET
    servers: ServerGroupServers | Unset = UNSET
    labels: ServerGroupModifyServerGroupLabels | Unset = UNSET
    anti_affinity: ServerGroupAntiAffinity | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        servers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = self.servers.to_dict()

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        anti_affinity: str | Unset = UNSET
        if not isinstance(self.anti_affinity, Unset):
            anti_affinity = self.anti_affinity.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if servers is not UNSET:
            field_dict["servers"] = servers
        if labels is not UNSET:
            field_dict["labels"] = labels
        if anti_affinity is not UNSET:
            field_dict["anti_affinity"] = anti_affinity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_group_modify_server_group_labels import ServerGroupModifyServerGroupLabels  # noqa: PLC0415
        from ..models.server_group_servers import ServerGroupServers  # noqa: PLC0415

        d = dict(src_dict)
        title = d.pop("title", UNSET)

        _servers = d.pop("servers", UNSET)
        servers: ServerGroupServers | Unset
        if isinstance(_servers, Unset):
            servers = UNSET
        else:
            servers = ServerGroupServers.from_dict(_servers)

        _labels = d.pop("labels", UNSET)
        labels: ServerGroupModifyServerGroupLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ServerGroupModifyServerGroupLabels.from_dict(_labels)

        _anti_affinity = d.pop("anti_affinity", UNSET)
        anti_affinity: ServerGroupAntiAffinity | Unset
        if isinstance(_anti_affinity, Unset):
            anti_affinity = UNSET
        else:
            anti_affinity = ServerGroupAntiAffinity(_anti_affinity)

        server_group_modify_server_group = cls(
            title=title,
            servers=servers,
            labels=labels,
            anti_affinity=anti_affinity,
        )

        return server_group_modify_server_group
