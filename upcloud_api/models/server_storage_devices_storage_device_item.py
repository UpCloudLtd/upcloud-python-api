from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.server_boolean_yesno import ServerBooleanYesno
from ..models.server_storage_devices_storage_device_item_action import ServerStorageDevicesStorageDeviceItemAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.server_label import ServerLabel
    from ..models.server_storage_devices_storage_device_item_backup_rule import (
        ServerStorageDevicesStorageDeviceItemBackupRule,
    )


T = TypeVar("T", bound="ServerStorageDevicesStorageDeviceItem")


@_attrs_define
class ServerStorageDevicesStorageDeviceItem:
    """
    Attributes:
        action (ServerStorageDevicesStorageDeviceItemAction): Method used to create, clone, or attach storage for the
            device
        address (str | Unset): Device address on the Cloud Server
        backup_rule (ServerStorageDevicesStorageDeviceItemBackupRule | Unset):
        encrypted (ServerBooleanYesno | Unset): Boolean value represented as yes/no Example: yes.
        labels (list[ServerLabel] | Unset):
        size (int | str | Unset): Requested block storage size in gigabytes
        storage (str | Unset): UUID of the storage resource to attach or clone
        tier (str | Unset): Performance and pricing tier of the block storage
        title (str | Unset): Short informational description of the block storage
        type_ (str | Unset): Storage device type: disk or cdrom
    """

    action: ServerStorageDevicesStorageDeviceItemAction
    address: str | Unset = UNSET
    backup_rule: ServerStorageDevicesStorageDeviceItemBackupRule | Unset = UNSET
    encrypted: ServerBooleanYesno | Unset = UNSET
    labels: list[ServerLabel] | Unset = UNSET
    size: int | str | Unset = UNSET
    storage: str | Unset = UNSET
    tier: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        address = self.address

        backup_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backup_rule, Unset):
            backup_rule = self.backup_rule.to_dict()

        encrypted: str | Unset = UNSET
        if not isinstance(self.encrypted, Unset):
            encrypted = self.encrypted.value

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        size: int | str | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        storage = self.storage

        tier = self.tier

        title = self.title

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if backup_rule is not UNSET:
            field_dict["backup_rule"] = backup_rule
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if labels is not UNSET:
            field_dict["labels"] = labels
        if size is not UNSET:
            field_dict["size"] = size
        if storage is not UNSET:
            field_dict["storage"] = storage
        if tier is not UNSET:
            field_dict["tier"] = tier
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.server_label import ServerLabel  # noqa: PLC0415
        from ..models.server_storage_devices_storage_device_item_backup_rule import (
            ServerStorageDevicesStorageDeviceItemBackupRule,  # noqa: PLC0415
        )

        d = dict(src_dict)
        action = ServerStorageDevicesStorageDeviceItemAction(d.pop("action"))

        address = d.pop("address", UNSET)

        _backup_rule = d.pop("backup_rule", UNSET)
        backup_rule: ServerStorageDevicesStorageDeviceItemBackupRule | Unset
        if isinstance(_backup_rule, Unset):
            backup_rule = UNSET
        else:
            backup_rule = ServerStorageDevicesStorageDeviceItemBackupRule.from_dict(_backup_rule)

        _encrypted = d.pop("encrypted", UNSET)
        encrypted: ServerBooleanYesno | Unset
        if isinstance(_encrypted, Unset):
            encrypted = UNSET
        else:
            encrypted = ServerBooleanYesno(_encrypted)

        _labels = d.pop("labels", UNSET)
        labels: list[ServerLabel] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = ServerLabel.from_dict(labels_item_data)

                labels.append(labels_item)

        def _parse_size(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        size = _parse_size(d.pop("size", UNSET))

        storage = d.pop("storage", UNSET)

        tier = d.pop("tier", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        server_storage_devices_storage_device_item = cls(
            action=action,
            address=address,
            backup_rule=backup_rule,
            encrypted=encrypted,
            labels=labels,
            size=size,
            storage=storage,
            tier=tier,
            title=title,
            type_=type_,
        )

        return server_storage_devices_storage_device_item
