from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.server_group_anti_affinity_status_status import ServerGroupAntiAffinityStatusStatus

T = TypeVar("T", bound="ServerGroupAntiAffinityStatus")


@_attrs_define
class ServerGroupAntiAffinityStatus:
    """Status of anti-affinity policy

    Attributes:
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        status (ServerGroupAntiAffinityStatusStatus): Indicates whether the anti-affinity policy is currently being met
            ('met') or not ('unmet')
    """

    uuid: UUID
    status: ServerGroupAntiAffinityStatusStatus

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "uuid": uuid,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        status = ServerGroupAntiAffinityStatusStatus(d.pop("status"))

        server_group_anti_affinity_status = cls(
            uuid=uuid,
            status=status,
        )

        return server_group_anti_affinity_status
