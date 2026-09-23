from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.modify_storage_body_storage_filesystem_resize import ModifyStorageBodyStorageFilesystemResize
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.modify_storage_body_storage_backup_rule_type_1 import ModifyStorageBodyStorageBackupRuleType1
    from ..models.storage_backup_rule import StorageBackupRule
    from ..models.storage_label import StorageLabel


T = TypeVar("T", bound="ModifyStorageBodyStorage")


@_attrs_define
class ModifyStorageBodyStorage:
    """Block storage properties to modify.

    Attributes:
        backup_rule (ModifyStorageBodyStorageBackupRuleType1 | StorageBackupRule | Unset): Schedule for automatic
            backups of the block storage. An empty object removes the configured schedule.
        filesystem_resize (ModifyStorageBodyStorageFilesystemResize | Unset): Set to `yes` when increasing `size` to
            also resize the last partition and its supported filesystem. The attached Cloud Server, if any, must be stopped.
        labels (list[StorageLabel] | Unset): Labels describing and classifying the block storage. Each label contains a
            key and a value.
        size (int | str | Unset): New block storage size in gigabytes, from 1 through 4096 subject to the account's
            block storage limits. The new size must be greater than the current size.
        title (str | Unset): A short, informational description of the block storage.
    """

    backup_rule: ModifyStorageBodyStorageBackupRuleType1 | StorageBackupRule | Unset = UNSET
    filesystem_resize: ModifyStorageBodyStorageFilesystemResize | Unset = UNSET
    labels: list[StorageLabel] | Unset = UNSET
    size: int | str | Unset = UNSET
    title: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.storage_backup_rule import StorageBackupRule  # noqa: PLC0415

        backup_rule: dict[str, Any] | Unset
        if isinstance(self.backup_rule, Unset):
            backup_rule = UNSET
        elif isinstance(self.backup_rule, StorageBackupRule):
            backup_rule = self.backup_rule.to_dict()
        else:
            backup_rule = self.backup_rule.to_dict()

        filesystem_resize: str | Unset = UNSET
        if not isinstance(self.filesystem_resize, Unset):
            filesystem_resize = self.filesystem_resize.value

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

        title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_rule is not UNSET:
            field_dict["backup_rule"] = backup_rule
        if filesystem_resize is not UNSET:
            field_dict["filesystem_resize"] = filesystem_resize
        if labels is not UNSET:
            field_dict["labels"] = labels
        if size is not UNSET:
            field_dict["size"] = size
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.modify_storage_body_storage_backup_rule_type_1 import (
            ModifyStorageBodyStorageBackupRuleType1,  # noqa: PLC0415
        )
        from ..models.storage_backup_rule import StorageBackupRule  # noqa: PLC0415
        from ..models.storage_label import StorageLabel  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_backup_rule(data: object) -> ModifyStorageBodyStorageBackupRuleType1 | StorageBackupRule | Unset:
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
            backup_rule_type_1 = ModifyStorageBodyStorageBackupRuleType1.from_dict(data)

            return backup_rule_type_1

        backup_rule = _parse_backup_rule(d.pop("backup_rule", UNSET))

        _filesystem_resize = d.pop("filesystem_resize", UNSET)
        filesystem_resize: ModifyStorageBodyStorageFilesystemResize | Unset
        if isinstance(_filesystem_resize, Unset):
            filesystem_resize = UNSET
        else:
            filesystem_resize = ModifyStorageBodyStorageFilesystemResize(_filesystem_resize)

        _labels = d.pop("labels", UNSET)
        labels: list[StorageLabel] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = StorageLabel.from_dict(labels_item_data)

                labels.append(labels_item)

        def _parse_size(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        size = _parse_size(d.pop("size", UNSET))

        title = d.pop("title", UNSET)

        modify_storage_body_storage = cls(
            backup_rule=backup_rule,
            filesystem_resize=filesystem_resize,
            labels=labels,
            size=size,
            title=title,
        )

        return modify_storage_body_storage
