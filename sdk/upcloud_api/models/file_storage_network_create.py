from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.file_storage_network_family import FileStorageNetworkFamily
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileStorageNetworkCreate")


@_attrs_define
class FileStorageNetworkCreate:
    """Schema for creating a network.

    Attributes:
        uuid (UUID): Unique identifier for the network.
        name (str): A resource name.
        family (FileStorageNetworkFamily): Network family. IPv6 currently not supported.
        ip_address (str | Unset): The desired IP address for the service. If not specified, the service will be assigned
            an IP address from the network's pool.
    """

    uuid: UUID
    name: str
    family: FileStorageNetworkFamily
    ip_address: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        family = self.family.value

        ip_address = self.ip_address

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "family": family,
            }
        )
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        family = FileStorageNetworkFamily(d.pop("family"))

        ip_address = d.pop("ip_address", UNSET)

        file_storage_network_create = cls(
            uuid=uuid,
            name=name,
            family=family,
            ip_address=ip_address,
        )

        return file_storage_network_create
