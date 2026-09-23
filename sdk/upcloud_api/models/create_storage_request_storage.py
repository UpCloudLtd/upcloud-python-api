from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.storage_encrypted import StorageEncrypted
from ..models.storage_tier import StorageTier
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_storage_request_storage_backup_rule_type_1 import CreateStorageRequestStorageBackupRuleType1
    from ..models.storage_backup_rule import StorageBackupRule
    from ..models.storage_label import StorageLabel


T = TypeVar("T", bound="CreateStorageRequestStorage")


@_attrs_define
class CreateStorageRequestStorage:
    """Block storage creation parameters.

    Attributes:
        size (int | str): Size of the block storage in gigabytes, from 1 through 4096 subject to the account's block
            storage limits.
        title (str): A short, informational description of the block storage.
        zone (str): Zone identifier
        backup_rule (CreateStorageRequestStorageBackupRuleType1 | StorageBackupRule | Unset): Schedule for automatic
            backups. An empty object disables automatic         backups.
        encrypted (StorageEncrypted | Unset): Indicates whether the resource is encrypted.
        labels (list[StorageLabel] | Unset): Labels describing and classifying the block storage. Each label contains a
            key and a value.
        tier (StorageTier | Unset): Block storage performance and pricing tier. `maxiops` is high-performance block
            storage, `standard` is general-purpose block storage, and `hdd` is the API name for the high-capacity Archive
            tier.
    """

    size: int | str
    title: str
    zone: str
    backup_rule: CreateStorageRequestStorageBackupRuleType1 | StorageBackupRule | Unset = UNSET
    encrypted: StorageEncrypted | Unset = UNSET
    labels: list[StorageLabel] | Unset = UNSET
    tier: StorageTier | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.storage_backup_rule import StorageBackupRule  # noqa: PLC0415

        size: int | str
        size = self.size

        title = self.title

        zone = self.zone

        backup_rule: dict[str, Any] | Unset
        if isinstance(self.backup_rule, Unset):
            backup_rule = UNSET
        elif isinstance(self.backup_rule, StorageBackupRule):
            backup_rule = self.backup_rule.to_dict()
        else:
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

        tier: str | Unset = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "size": size,
                "title": title,
                "zone": zone,
            }
        )
        if backup_rule is not UNSET:
            field_dict["backup_rule"] = backup_rule
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if labels is not UNSET:
            field_dict["labels"] = labels
        if tier is not UNSET:
            field_dict["tier"] = tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_storage_request_storage_backup_rule_type_1 import (
            CreateStorageRequestStorageBackupRuleType1,  # noqa: PLC0415
        )
        from ..models.storage_backup_rule import StorageBackupRule  # noqa: PLC0415
        from ..models.storage_label import StorageLabel  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_size(data: object) -> int | str:
            return cast(int | str, data)

        size = _parse_size(d.pop("size"))

        title = d.pop("title")

        zone = d.pop("zone")

        def _parse_backup_rule(data: object) -> CreateStorageRequestStorageBackupRuleType1 | StorageBackupRule | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                backup_rule_type_0 = StorageBackupRule.from_dict(data)

                return backup_rule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            backup_rule_type_1 = CreateStorageRequestStorageBackupRuleType1.from_dict(data)

            return backup_rule_type_1

        backup_rule = _parse_backup_rule(d.pop("backup_rule", UNSET))

        _encrypted = d.pop("encrypted", UNSET)
        encrypted: StorageEncrypted | Unset
        if isinstance(_encrypted, Unset):
            encrypted = UNSET
        else:
            encrypted = StorageEncrypted(_encrypted)

        _labels = d.pop("labels", UNSET)
        labels: list[StorageLabel] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = StorageLabel.from_dict(labels_item_data)

                labels.append(labels_item)

        _tier = d.pop("tier", UNSET)
        tier: StorageTier | Unset
        if isinstance(_tier, Unset):
            tier = UNSET
        else:
            tier = StorageTier(_tier)

        create_storage_request_storage = cls(
            size=size,
            title=title,
            zone=zone,
            backup_rule=backup_rule,
            encrypted=encrypted,
            labels=labels,
            tier=tier,
        )

        return create_storage_request_storage
