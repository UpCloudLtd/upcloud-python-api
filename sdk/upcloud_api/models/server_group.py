from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_group_details import ServerGroupDetails


T = TypeVar("T", bound="ServerGroup")


@_attrs_define
class ServerGroup:
    """A single server group

    Attributes:
        server_group (ServerGroupDetails): Details of a server group
    """

    server_group: ServerGroupDetails

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
        from ..models.server_group_details import ServerGroupDetails  # noqa: PLC0415

        d = dict(src_dict)
        server_group = ServerGroupDetails.from_dict(d.pop("server_group"))

        server_group = cls(
            server_group=server_group,
        )

        return server_group
