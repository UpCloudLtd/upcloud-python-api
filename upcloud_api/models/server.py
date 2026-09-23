from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.server_details import ServerDetails


T = TypeVar("T", bound="Server")


@_attrs_define
class Server:
    """Cloud Server object returned in responses

    Example:
        {'server': {'boot_order': 'disk', 'core_number': '12', 'created': 1705320000, 'firewall': 'on', 'host':
            7653311107, 'hostname': 'server1.example.com', 'labels': {'label': [{'key': 'env', 'value': 'development'}]},
            'license': '0', 'memory_amount': '130048', 'nic_model': 'virtio', 'plan': 'GPU-12xCPU-128GB-2xL40S',
            'plan_ipv4_bytes': '3565675343', 'plan_ipv6_bytes': '4534432', 'remote_access_enabled': 'yes',
            'remote_access_type': 'vnc', 'server_group': '0b3d85b4-b3be-46ca-a1e2-3b5d40d60fb1', 'simple_backup':
            '0100,dailies', 'state': 'started', 'storage_devices': {'storage_device': [{'address': 'virtio:0', 'boot_disk':
            '1', 'labels': [], 'storage': '012580a1-32a1-466e-a323-689ca16f2d43', 'storage_encrypted': 'yes',
            'storage_size': 20, 'storage_title': 'Operating system disk', 'type': 'disk'}]}, 'tags': {'tag': ['DEV',
            'Ubuntu']}, 'timezone': 'UTC', 'title': 'Development GPU server', 'uuid':
            '0077fa3d-32db-4b09-9f5f-30d9e9afb565', 'video_model': 'cirrus', 'zone': 'fi-hel1'}}

    Attributes:
        server (ServerDetails): Detailed public information about a Cloud Server Example: {'boot_order': 'disk',
            'core_number': '12', 'created': 1705320000, 'firewall': 'on', 'host': 7653311107, 'hostname':
            'server1.example.com', 'labels': {'label': [{'key': 'env', 'value': 'development'}]}, 'license': '0',
            'memory_amount': '130048', 'nic_model': 'virtio', 'plan': 'GPU-12xCPU-128GB-2xL40S', 'plan_ipv4_bytes':
            '3565675343', 'plan_ipv6_bytes': '4534432', 'remote_access_enabled': 'yes', 'remote_access_host': 'fi-
            hel1.vnc.upcloud.com', 'remote_access_password': 'aabbccdd', 'remote_access_port': '3000', 'remote_access_type':
            'vnc', 'server_group': '0b3d85b4-b3be-46ca-a1e2-3b5d40d60fb1', 'simple_backup': '0100,dailies', 'state':
            'started', 'storage_devices': {'storage_device': [{'address': 'virtio:0', 'boot_disk': '1', 'labels': [],
            'storage': '012580a1-32a1-466e-a323-689ca16f2d43', 'storage_encrypted': 'yes', 'storage_size': 20,
            'storage_title': 'Operating system disk', 'type': 'disk'}]}, 'tags': {'tag': ['DEV', 'Ubuntu']}, 'timezone':
            'UTC', 'title': 'Development GPU server', 'uuid': '0077fa3d-32db-4b09-9f5f-30d9e9afb565', 'video_model':
            'cirrus', 'zone': 'fi-hel1'}.
    """

    server: ServerDetails

    def to_dict(self) -> dict[str, Any]:
        server = self.server.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "server": server,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_details import ServerDetails  # noqa: PLC0415

        d = dict(src_dict)
        server = ServerDetails.from_dict(d.pop("server"))

        server = cls(
            server=server,
        )

        return server
