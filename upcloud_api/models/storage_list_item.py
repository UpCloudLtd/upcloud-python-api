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
    from ..models.storage_label import StorageLabel


T = TypeVar("T", bound="StorageListItem")


@_attrs_define
class StorageListItem:
    """Storage resource summary returned by public list operations.

    Example:
        {'access': 'private', 'created': '2025-02-27T05:50:50Z', 'encrypted': 'no', 'labels': [], 'license': 0, 'size':
            50, 'state': 'online', 'tier': 'maxiops', 'title': 'Databases', 'type': 'normal', 'uuid':
            '01f3286c-a5ea-4670-8121-d0b9767d625b', 'zone': 'fi-hel1'}

    Attributes:
        access (StorageAccess): Network access level Example: public.
        encrypted (StorageEncrypted): Indicates whether the resource is encrypted.
        labels (list[StorageLabel]): Labels describing and classifying the storage resource.
        license_ (float): Hourly license fee in credits. The value is `0` when the storage resource has no license fee.
        size (int): Size of the storage resource in gigabytes.
        state (StorageState): Current lifecycle state of the storage resource. `online` is ready for use; `maintenance`
            indicates ongoing maintenance or an update; `cloning`, `backuping`, and `syncing` indicate active storage
            operations; `error` indicates that the storage resource is inaccessible because an error occurred.
        title (str): A short, informational description of the storage resource.
        type_ (StorageType): Storage resource type to return.
        uuid (UUID): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
        part_of_plan (Literal['yes'] | Unset): Present with value `yes` when the storage resource is included in the
            Cloud Server plan.
        progress (str | Unset): Progress of an active storage operation.
        created (datetime.datetime | Unset): Time when the private storage resource or backup was created.
        origin (UUID | Unset): Universally unique identifier Example: 0414e0d7-4436-4037-9dd8-6eaf47dce599.
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
    size: int
    state: StorageState
    title: str
    type_: StorageType
    uuid: UUID
    part_of_plan: Literal["yes"] | Unset = UNSET
    progress: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    origin: UUID | Unset = UNSET
    tier: StorageTier | Unset = UNSET
    template_type: StorageTemplateType | Unset = UNSET
    zone: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        access = self.access.value

        encrypted = self.encrypted.value

        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.to_dict()
            labels.append(labels_item)

        license_ = self.license_

        size = self.size

        state = self.state.value

        title = self.title

        type_ = self.type_.value

        uuid = str(self.uuid)

        part_of_plan = self.part_of_plan

        progress = self.progress

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        origin: str | Unset = UNSET
        if not isinstance(self.origin, Unset):
            origin = str(self.origin)

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
                "size": size,
                "state": state,
                "title": title,
                "type": type_,
                "uuid": uuid,
            }
        )
        if part_of_plan is not UNSET:
            field_dict["part_of_plan"] = part_of_plan
        if progress is not UNSET:
            field_dict["progress"] = progress
        if created is not UNSET:
            field_dict["created"] = created
        if origin is not UNSET:
            field_dict["origin"] = origin
        if tier is not UNSET:
            field_dict["tier"] = tier
        if template_type is not UNSET:
            field_dict["template_type"] = template_type
        if zone is not UNSET:
            field_dict["zone"] = zone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        size = d.pop("size")

        state = StorageState(d.pop("state"))

        title = d.pop("title")

        type_ = StorageType(d.pop("type"))

        uuid = UUID(d.pop("uuid"))

        part_of_plan = cast(Literal["yes"] | Unset, d.pop("part_of_plan", UNSET))
        if part_of_plan != "yes" and not isinstance(part_of_plan, Unset):
            raise ValueError(f"part_of_plan must match const 'yes', got '{part_of_plan}'")

        progress = d.pop("progress", UNSET)

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

        storage_list_item = cls(
            access=access,
            encrypted=encrypted,
            labels=labels,
            license_=license_,
            size=size,
            state=state,
            title=title,
            type_=type_,
            uuid=uuid,
            part_of_plan=part_of_plan,
            progress=progress,
            created=created,
            origin=origin,
            tier=tier,
            template_type=template_type,
            zone=zone,
        )

        return storage_list_item
