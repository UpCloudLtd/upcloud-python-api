from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.server_boolean_yesno import ServerBooleanYesno
from ..models.server_storage_devices_response_storage_device_item_boot_disk import (
    ServerStorageDevicesResponseStorageDeviceItemBootDisk,
)
from ..models.server_storage_devices_response_storage_device_item_type import (
    ServerStorageDevicesResponseStorageDeviceItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_label import ServerLabel


T = TypeVar("T", bound="ServerStorageDevicesResponseStorageDeviceItem")


@_attrs_define
class ServerStorageDevicesResponseStorageDeviceItem:
    """
    Attributes:
        address (str): Device address on the Cloud Server.
        boot_disk (ServerStorageDevicesResponseStorageDeviceItemBootDisk): Whether this device is the Cloud Server's
            boot disk, encoded as 0 or 1.
        labels (list[ServerLabel]): Labels assigned to the storage resource.
        storage (str): Storage resource UUID. Empty for an unloaded CD-ROM device.
        storage_encrypted (ServerBooleanYesno): Boolean value represented as yes/no Example: yes.
        storage_size (int): Storage resource size in gibibytes.
        storage_title (str): Storage resource title.
        type_ (ServerStorageDevicesResponseStorageDeviceItemType): Attached device type.
        part_of_plan (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        storage_tier (str | Unset): Storage resource performance tier.
    """

    address: str
    boot_disk: ServerStorageDevicesResponseStorageDeviceItemBootDisk
    labels: list[ServerLabel]
    storage: str
    storage_encrypted: ServerBooleanYesno
    storage_size: int
    storage_title: str
    type_: ServerStorageDevicesResponseStorageDeviceItemType
    part_of_plan: ServerBooleanYesno | Unset = UNSET
    storage_tier: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        boot_disk = self.boot_disk.value

        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.to_dict()
            labels.append(labels_item)

        storage = self.storage

        storage_encrypted = self.storage_encrypted.value

        storage_size = self.storage_size

        storage_title = self.storage_title

        type_ = self.type_.value

        part_of_plan: str | Unset = UNSET
        if not isinstance(self.part_of_plan, Unset):
            part_of_plan = self.part_of_plan.value

        storage_tier = self.storage_tier

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address": address,
                "boot_disk": boot_disk,
                "labels": labels,
                "storage": storage,
                "storage_encrypted": storage_encrypted,
                "storage_size": storage_size,
                "storage_title": storage_title,
                "type": type_,
            }
        )
        if part_of_plan is not UNSET:
            field_dict["part_of_plan"] = part_of_plan
        if storage_tier is not UNSET:
            field_dict["storage_tier"] = storage_tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_label import ServerLabel  # noqa: PLC0415

        d = dict(src_dict)
        address = d.pop("address")

        boot_disk = ServerStorageDevicesResponseStorageDeviceItemBootDisk(d.pop("boot_disk"))

        labels = []
        _labels = d.pop("labels")
        for labels_item_data in _labels:
            labels_item = ServerLabel.from_dict(labels_item_data)

            labels.append(labels_item)

        storage = d.pop("storage")

        storage_encrypted = ServerBooleanYesno(d.pop("storage_encrypted"))

        storage_size = d.pop("storage_size")

        storage_title = d.pop("storage_title")

        type_ = ServerStorageDevicesResponseStorageDeviceItemType(d.pop("type"))

        _part_of_plan = d.pop("part_of_plan", UNSET)
        part_of_plan: ServerBooleanYesno | Unset
        if isinstance(_part_of_plan, Unset):
            part_of_plan = UNSET
        else:
            part_of_plan = ServerBooleanYesno(_part_of_plan)

        storage_tier = d.pop("storage_tier", UNSET)

        server_storage_devices_response_storage_device_item = cls(
            address=address,
            boot_disk=boot_disk,
            labels=labels,
            storage=storage,
            storage_encrypted=storage_encrypted,
            storage_size=storage_size,
            storage_title=storage_title,
            type_=type_,
            part_of_plan=part_of_plan,
            storage_tier=storage_tier,
        )

        return server_storage_devices_response_storage_device_item
