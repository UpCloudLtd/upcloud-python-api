from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.server_group_anti_affinity import ServerGroupAntiAffinity

if TYPE_CHECKING:
    from ..models.server_group_anti_affinity_status import ServerGroupAntiAffinityStatus
    from ..models.server_group_details_labels import ServerGroupDetailsLabels
    from ..models.server_group_details_servers import ServerGroupDetailsServers


T = TypeVar("T", bound="ServerGroupDetails")


@_attrs_define
class ServerGroupDetails:
    """Details of a server group

    Attributes:
        anti_affinity (ServerGroupAntiAffinity): Anti-affinity policy for server groups. Possible values are 'strict',
            'yes', or 'no'. 'strict' ensures that no two servers in the group are placed on the same physical host. 'yes'
            indicates a preference for anti-affinity but does not guarantee it. 'no' means there is no anti-affinity
            requirement.
        anti_affinity_status (list[ServerGroupAntiAffinityStatus]):
        labels (ServerGroupDetailsLabels): List of labels associated with the server group.
        servers (ServerGroupDetailsServers): List of servers associated with the server group.
        title (str):
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
    """

    anti_affinity: ServerGroupAntiAffinity
    anti_affinity_status: list[ServerGroupAntiAffinityStatus]
    labels: ServerGroupDetailsLabels
    servers: ServerGroupDetailsServers
    title: str
    uuid: UUID

    def to_dict(self) -> dict[str, Any]:
        anti_affinity = self.anti_affinity.value

        anti_affinity_status = []
        for anti_affinity_status_item_data in self.anti_affinity_status:
            anti_affinity_status_item = anti_affinity_status_item_data.to_dict()
            anti_affinity_status.append(anti_affinity_status_item)

        labels = self.labels.to_dict()

        servers = self.servers.to_dict()

        title = self.title

        uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "anti_affinity": anti_affinity,
                "anti_affinity_status": anti_affinity_status,
                "labels": labels,
                "servers": servers,
                "title": title,
                "uuid": uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_group_anti_affinity_status import ServerGroupAntiAffinityStatus  # noqa: PLC0415
        from ..models.server_group_details_labels import ServerGroupDetailsLabels  # noqa: PLC0415
        from ..models.server_group_details_servers import ServerGroupDetailsServers  # noqa: PLC0415

        d = dict(src_dict)
        anti_affinity = ServerGroupAntiAffinity(d.pop("anti_affinity"))

        anti_affinity_status = []
        _anti_affinity_status = d.pop("anti_affinity_status")
        for anti_affinity_status_item_data in _anti_affinity_status:
            anti_affinity_status_item = ServerGroupAntiAffinityStatus.from_dict(anti_affinity_status_item_data)

            anti_affinity_status.append(anti_affinity_status_item)

        labels = ServerGroupDetailsLabels.from_dict(d.pop("labels"))

        servers = ServerGroupDetailsServers.from_dict(d.pop("servers"))

        title = d.pop("title")

        uuid = UUID(d.pop("uuid"))

        server_group_details = cls(
            anti_affinity=anti_affinity,
            anti_affinity_status=anti_affinity_status,
            labels=labels,
            servers=servers,
            title=title,
            uuid=uuid,
        )

        return server_group_details
