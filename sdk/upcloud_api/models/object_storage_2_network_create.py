from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.object_storage_2_network_family import ObjectStorage2NetworkFamily
from ..models.object_storage_2_network_type import ObjectStorage2NetworkType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2NetworkCreate")


@_attrs_define
class ObjectStorage2NetworkCreate:
    """Schema for creating a network with optional private UUID, name, type, and family.

    Attributes:
        name (str): A resource name.
        type_ (ObjectStorage2NetworkType): Enum for the network type, indicating whether the network is public or
            private.
        family (ObjectStorage2NetworkFamily): Enum for the network family, indicating the type of IP address used.
        uuid (UUID | Unset): Private network uuid. Omit for public networks. Example:
            03bec0ad-85c3-459e-824d-710f8f24f740.
    """

    name: str
    type_: ObjectStorage2NetworkType
    family: ObjectStorage2NetworkFamily
    uuid: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        family = self.family.value

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
                "family": family,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = ObjectStorage2NetworkType(d.pop("type"))

        family = ObjectStorage2NetworkFamily(d.pop("family"))

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        object_storage_2_network_create = cls(
            name=name,
            type_=type_,
            family=family,
            uuid=uuid,
        )

        return object_storage_2_network_create
