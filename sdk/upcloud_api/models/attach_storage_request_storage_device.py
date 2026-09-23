from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.attach_storage_request_storage_device_boot_disk import AttachStorageRequestStorageDeviceBootDisk
from ..models.attach_storage_request_storage_device_type import AttachStorageRequestStorageDeviceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachStorageRequestStorageDevice")


@_attrs_define
class AttachStorageRequestStorageDevice:
    """Parameters for attaching this storage resource to a Cloud Server in the same zone.

    Attributes:
        server (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        address (str | Unset): Device address on the Cloud Server, or an `ide`, `scsi`, or `virtio` bus name for
            automatic address selection. Defaults to the next available address on the Cloud Server's default disk bus for
            disks, or the IDE bus for CD-ROM devices.
        type_ (AttachStorageRequestStorageDeviceType | Unset): Type of the attached device. Defaults to `disk`. Default:
            AttachStorageRequestStorageDeviceType.DISK.
        boot_disk (AttachStorageRequestStorageDeviceBootDisk | Unset): Whether the device is used as the boot disk
            unless overridden by the Cloud Server boot order. Defaults to `0`. Default:
            AttachStorageRequestStorageDeviceBootDisk.VALUE_0.
    """

    server: UUID
    address: str | Unset = UNSET
    type_: AttachStorageRequestStorageDeviceType | Unset = AttachStorageRequestStorageDeviceType.DISK
    boot_disk: AttachStorageRequestStorageDeviceBootDisk | Unset = AttachStorageRequestStorageDeviceBootDisk.VALUE_0

    def to_dict(self) -> dict[str, Any]:
        server = str(self.server)

        address = self.address

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        boot_disk: str | Unset = UNSET
        if not isinstance(self.boot_disk, Unset):
            boot_disk = self.boot_disk.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "server": server,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if type_ is not UNSET:
            field_dict["type"] = type_
        if boot_disk is not UNSET:
            field_dict["boot_disk"] = boot_disk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server = UUID(d.pop("server"))

        address = d.pop("address", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AttachStorageRequestStorageDeviceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AttachStorageRequestStorageDeviceType(_type_)

        _boot_disk = d.pop("boot_disk", UNSET)
        boot_disk: AttachStorageRequestStorageDeviceBootDisk | Unset
        if isinstance(_boot_disk, Unset):
            boot_disk = UNSET
        else:
            boot_disk = AttachStorageRequestStorageDeviceBootDisk(_boot_disk)

        attach_storage_request_storage_device = cls(
            server=server,
            address=address,
            type_=type_,
            boot_disk=boot_disk,
        )

        return attach_storage_request_storage_device
