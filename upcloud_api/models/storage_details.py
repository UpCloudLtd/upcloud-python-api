from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.storage_access import StorageAccess
from ..models.storage_encrypted import StorageEncrypted
from ..models.storage_state import StorageState
from ..models.storage_template_type import StorageTemplateType
from ..models.storage_tier import StorageTier
from ..models.storage_type import StorageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_backup_rule import StorageBackupRule
    from ..models.storage_details_backup_rule_type_1 import StorageDetailsBackupRuleType1
    from ..models.storage_details_backups import StorageDetailsBackups
    from ..models.storage_details_servers import StorageDetailsServers
    from ..models.storage_label import StorageLabel


T = TypeVar("T", bound="StorageDetails")


@_attrs_define
class StorageDetails:
    """Detailed information about a storage resource.

    Example:
        {'access': 'private', 'backup_rule': {}, 'backups': {'backup': []}, 'created': '2026-08-26T09:15:00Z',
            'encrypted': 'no', 'labels': [], 'license': 0, 'servers': {'server': []}, 'size': 50, 'state': 'online', 'tier':
            'maxiops', 'title': 'Production data', 'type': 'normal', 'uuid': '01d4fcd4-e446-433b-8a9c-551a1284952e', 'zone':
            'fi-hel1'}

    Attributes:
        access (StorageAccess): Network access level Example: public.
        encrypted (StorageEncrypted): Indicates whether the resource is encrypted.
        labels (list[StorageLabel]): Labels describing and classifying the storage resource.
        license_ (float): Hourly license cost in credits when the storage resource contains a licensed operating system.
        servers (StorageDetailsServers): Cloud Servers to which the storage resource is attached.
        size (int): Size of the storage resource in gigabytes.
        state (StorageState): Current lifecycle state of the storage resource. `online` is ready for use; `maintenance`
            indicates ongoing maintenance or an update; `cloning`, `backuping`, and `syncing` indicate active storage
            operations; `error` indicates that the storage resource is inaccessible because an error occurred.
        title (str): A short, informational description of the storage resource.
        type_ (StorageType): Storage resource type to return.
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        backup_rule (StorageBackupRule | StorageDetailsBackupRuleType1 | Unset): Schedule for automatic backups of the
            storage resource. An empty object indicates that no automatic backup schedule is configured.
        backups (StorageDetailsBackups | Unset): Backups associated with this storage resource.
        created (datetime.datetime | Unset): Time when the private storage resource was created.
        origin (UUID | Unset): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        part_of_plan (Literal['yes'] | Unset): Present with the value `yes` when the storage resource is included in a
            Cloud Server plan.
        progress (str | Unset): Progress of an ongoing storage operation when available.
        tier (StorageTier | Unset): Block storage performance and pricing tier. `maxiops` is high-performance block
            storage, `standard` is general-purpose block storage, and `hdd` is the API name for the high-capacity Archive
            tier.
        template_type (StorageTemplateType | Unset): Template initialization mechanism. `cloud-init` templates support
            cloud-init metadata, while `native` templates use the operating system's native initialization.
        zone (str | Unset): Zone identifier
    """

    access: StorageAccess
    encrypted: StorageEncrypted
    labels: list[StorageLabel]
    license_: float
    servers: StorageDetailsServers
    size: int
    state: StorageState
    title: str
    type_: StorageType
    uuid: UUID
    backup_rule: StorageBackupRule | StorageDetailsBackupRuleType1 | Unset = UNSET
    backups: StorageDetailsBackups | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    origin: UUID | Unset = UNSET
    part_of_plan: Literal["yes"] | Unset = UNSET
    progress: str | Unset = UNSET
    tier: StorageTier | Unset = UNSET
    template_type: StorageTemplateType | Unset = UNSET
    zone: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.storage_backup_rule import StorageBackupRule  # noqa: PLC0415

        access = self.access.value

        encrypted = self.encrypted.value

        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.to_dict()
            labels.append(labels_item)

        license_ = self.license_

        servers = self.servers.to_dict()

        size = self.size

        state = self.state.value

        title = self.title

        type_ = self.type_.value

        uuid = str(self.uuid)

        backup_rule: dict[str, Any] | Unset
        if isinstance(self.backup_rule, Unset):
            backup_rule = UNSET
        elif isinstance(self.backup_rule, StorageBackupRule):
            backup_rule = self.backup_rule.to_dict()
        else:
            backup_rule = self.backup_rule.to_dict()

        backups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backups, Unset):
            backups = self.backups.to_dict()

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        origin: str | Unset = UNSET
        if not isinstance(self.origin, Unset):
            origin = str(self.origin)

        part_of_plan = self.part_of_plan

        progress = self.progress

        tier: str | Unset = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier.value

        template_type: str | Unset = UNSET
        if not isinstance(self.template_type, Unset):
            template_type = self.template_type.value

        zone = self.zone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "access": access,
                "encrypted": encrypted,
                "labels": labels,
                "license": license_,
                "servers": servers,
                "size": size,
                "state": state,
                "title": title,
                "type": type_,
                "uuid": uuid,
            }
        )
        if backup_rule is not UNSET:
            field_dict["backup_rule"] = backup_rule
        if backups is not UNSET:
            field_dict["backups"] = backups
        if created is not UNSET:
            field_dict["created"] = created
        if origin is not UNSET:
            field_dict["origin"] = origin
        if part_of_plan is not UNSET:
            field_dict["part_of_plan"] = part_of_plan
        if progress is not UNSET:
            field_dict["progress"] = progress
        if tier is not UNSET:
            field_dict["tier"] = tier
        if template_type is not UNSET:
            field_dict["template_type"] = template_type
        if zone is not UNSET:
            field_dict["zone"] = zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_backup_rule import StorageBackupRule  # noqa: PLC0415
        from ..models.storage_details_backup_rule_type_1 import StorageDetailsBackupRuleType1  # noqa: PLC0415
        from ..models.storage_details_backups import StorageDetailsBackups  # noqa: PLC0415
        from ..models.storage_details_servers import StorageDetailsServers  # noqa: PLC0415
        from ..models.storage_label import StorageLabel  # noqa: PLC0415

        d = dict(src_dict)
        access = StorageAccess(d.pop("access"))

        encrypted = StorageEncrypted(d.pop("encrypted"))

        labels = []
        _labels = d.pop("labels")
        for labels_item_data in _labels:
            labels_item = StorageLabel.from_dict(labels_item_data)

            labels.append(labels_item)

        license_ = d.pop("license")

        servers = StorageDetailsServers.from_dict(d.pop("servers"))

        size = d.pop("size")

        state = StorageState(d.pop("state"))

        title = d.pop("title")

        type_ = StorageType(d.pop("type"))

        uuid = UUID(d.pop("uuid"))

        def _parse_backup_rule(data: object) -> StorageBackupRule | StorageDetailsBackupRuleType1 | Unset:
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
            backup_rule_type_1 = StorageDetailsBackupRuleType1.from_dict(data)

            return backup_rule_type_1

        backup_rule = _parse_backup_rule(d.pop("backup_rule", UNSET))

        _backups = d.pop("backups", UNSET)
        backups: StorageDetailsBackups | Unset
        if isinstance(_backups, Unset):
            backups = UNSET
        else:
            backups = StorageDetailsBackups.from_dict(_backups)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        _origin = d.pop("origin", UNSET)
        origin: UUID | Unset
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = UUID(_origin)

        part_of_plan = cast(Literal["yes"] | Unset, d.pop("part_of_plan", UNSET))
        if part_of_plan != "yes" and not isinstance(part_of_plan, Unset):
            raise ValueError(f"part_of_plan must match const 'yes', got '{part_of_plan}'")

        progress = d.pop("progress", UNSET)

        _tier = d.pop("tier", UNSET)
        tier: StorageTier | Unset
        if isinstance(_tier, Unset):
            tier = UNSET
        else:
            tier = StorageTier(_tier)

        _template_type = d.pop("template_type", UNSET)
        template_type: StorageTemplateType | Unset
        if isinstance(_template_type, Unset):
            template_type = UNSET
        else:
            template_type = StorageTemplateType(_template_type)

        zone = d.pop("zone", UNSET)

        storage_details = cls(
            access=access,
            encrypted=encrypted,
            labels=labels,
            license_=license_,
            servers=servers,
            size=size,
            state=state,
            title=title,
            type_=type_,
            uuid=uuid,
            backup_rule=backup_rule,
            backups=backups,
            created=created,
            origin=origin,
            part_of_plan=part_of_plan,
            progress=progress,
            tier=tier,
            template_type=template_type,
            zone=zone,
        )

        return storage_details
