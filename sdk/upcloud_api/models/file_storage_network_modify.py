from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.file_storage_network_family import FileStorageNetworkFamily
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileStorageNetworkModify")


@_attrs_define
class FileStorageNetworkModify:
    """Schema for modifying an existing network.

    Attributes:
        uuid (UUID | Unset): Unique identifier for the network.
        name (str | Unset): A resource name.
        family (FileStorageNetworkFamily | Unset): Network family. IPv6 currently not supported.
        ip_address (str | Unset): The desired IP address for the service. If not specified, the service will be assigned
            an IP address from the network's pool.
    """

    uuid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    family: FileStorageNetworkFamily | Unset = UNSET
    ip_address: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        name = self.name

        family: str | Unset = UNSET
        if not isinstance(self.family, Unset):
            family = self.family.value

        ip_address = self.ip_address

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if family is not UNSET:
            field_dict["family"] = family
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        name = d.pop("name", UNSET)

        _family = d.pop("family", UNSET)
        family: FileStorageNetworkFamily | Unset
        if isinstance(_family, Unset):
            family = UNSET
        else:
            family = FileStorageNetworkFamily(_family)

        ip_address = d.pop("ip_address", UNSET)

        file_storage_network_modify = cls(
            uuid=uuid,
            name=name,
            family=family,
            ip_address=ip_address,
        )

        return file_storage_network_modify
