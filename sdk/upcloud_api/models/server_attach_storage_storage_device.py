from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.server_attach_storage_storage_device_type import ServerAttachStorageStorageDeviceType
from ..models.server_boolean_01 import ServerBoolean01
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerAttachStorageStorageDevice")


@_attrs_define
class ServerAttachStorageStorageDevice:
    """Storage device to attach.

    Attributes:
        address (str | Unset): Device address or bus. When only a bus is specified, the next available address on that
            bus is selected. Defaults to the next available virtio address for disks and IDE address for CD-ROM devices.
        boot_disk (ServerBoolean01 | Unset): Schema for boolean-like values encoded as 0 or 1. Default:
            ServerBoolean01.VALUE_0.
        storage (UUID | Unset): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        type_ (ServerAttachStorageStorageDeviceType | Unset): Type of device to attach. Default:
            ServerAttachStorageStorageDeviceType.DISK.
    """

    address: str | Unset = UNSET
    boot_disk: ServerBoolean01 | Unset = ServerBoolean01.VALUE_0
    storage: UUID | Unset = UNSET
    type_: ServerAttachStorageStorageDeviceType | Unset = ServerAttachStorageStorageDeviceType.DISK

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        boot_disk: int | Unset = UNSET
        if not isinstance(self.boot_disk, Unset):
            boot_disk = self.boot_disk.value

        storage: str | Unset = UNSET
        if not isinstance(self.storage, Unset):
            storage = str(self.storage)

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if boot_disk is not UNSET:
            field_dict["boot_disk"] = boot_disk
        if storage is not UNSET:
            field_dict["storage"] = storage
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        _boot_disk = d.pop("boot_disk", UNSET)
        boot_disk: ServerBoolean01 | Unset
        if isinstance(_boot_disk, Unset):
            boot_disk = UNSET
        else:
            boot_disk = ServerBoolean01(_boot_disk)

        _storage = d.pop("storage", UNSET)
        storage: UUID | Unset
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = UUID(_storage)

        _type_ = d.pop("type", UNSET)
        type_: ServerAttachStorageStorageDeviceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ServerAttachStorageStorageDeviceType(_type_)

        server_attach_storage_storage_device = cls(
            address=address,
            boot_disk=boot_disk,
            storage=storage,
            type_=type_,
        )

        return server_attach_storage_storage_device
