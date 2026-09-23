from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.storage_encrypted import StorageEncrypted
from ..models.storage_tier import StorageTier
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloneStorageRequestStorage")


@_attrs_define
class CloneStorageRequestStorage:
    """Parameters for the cloned block storage.

    Attributes:
        title (str): Human-readable title for a resource.
        zone (str): Zone identifier
        encrypted (StorageEncrypted | Unset): Indicates whether the resource is encrypted.
        tier (StorageTier | Unset): Block storage performance and pricing tier. `maxiops` is high-performance block
            storage, `standard` is general-purpose block storage, and `hdd` is the API name for the high-capacity Archive
            tier.
    """

    title: str
    zone: str
    encrypted: StorageEncrypted | Unset = UNSET
    tier: StorageTier | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        zone = self.zone

        encrypted: str | Unset = UNSET
        if not isinstance(self.encrypted, Unset):
            encrypted = self.encrypted.value

        tier: str | Unset = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
                "zone": zone,
            }
        )
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if tier is not UNSET:
            field_dict["tier"] = tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        zone = d.pop("zone")

        _encrypted = d.pop("encrypted", UNSET)
        encrypted: StorageEncrypted | Unset
        if isinstance(_encrypted, Unset):
            encrypted = UNSET
        else:
            encrypted = StorageEncrypted(_encrypted)

        _tier = d.pop("tier", UNSET)
        tier: StorageTier | Unset
        if isinstance(_tier, Unset):
            tier = UNSET
        else:
            tier = StorageTier(_tier)

        clone_storage_request_storage = cls(
            title=title,
            zone=zone,
            encrypted=encrypted,
            tier=tier,
        )

        return clone_storage_request_storage
