from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_rebuild_server_rebuild import ServerRebuildServerRebuild


T = TypeVar("T", bound="ServerRebuild")


@_attrs_define
class ServerRebuild:
    """Rebuild Cloud Server request

    Example:
        {'server_rebuild': {'clone_source': '01000000-0000-4000-8000-000020050100', 'delete_detached_disk': 'yes',
            'detach_disk': '0169b4f8-051c-4a86-9484-f5b798249949', 'encrypted': 'yes', 'login_user': {'create_password':
            'no', 'ssh_keys': {'ssh_key': ['ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEexamplekey user@example']}, 'username':
            'debian'}, 'password_delivery': 'none', 'storage_title': 'Rebuilt system disk'}}

    Attributes:
        server_rebuild (ServerRebuildServerRebuild):
    """

    server_rebuild: ServerRebuildServerRebuild

    def to_dict(self) -> dict[str, Any]:
        server_rebuild = self.server_rebuild.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "server_rebuild": server_rebuild,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_rebuild_server_rebuild import ServerRebuildServerRebuild  # noqa: PLC0415

        d = dict(src_dict)
        server_rebuild = ServerRebuildServerRebuild.from_dict(d.pop("server_rebuild"))

        server_rebuild = cls(
            server_rebuild=server_rebuild,
        )

        return server_rebuild
