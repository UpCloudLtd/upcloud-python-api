from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2PolicyDetailResponse")


@_attrs_define
class ObjectStorage2PolicyDetailResponse:
    """Schema for policy details including ARN, attachment count, creation date, default version ID, description, document,
    name, system status, and last updated date.

        Attributes:
            arn (str | Unset):
            attachment_count (int | Unset):
            created_at (datetime.datetime | Unset):
            default_version_id (str | Unset):
            description (str | Unset):
            document (str | Unset):
            name (str | Unset):
            system (bool | Unset):
            updated_at (datetime.datetime | Unset):
    """

    arn: str | Unset = UNSET
    attachment_count: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    default_version_id: str | Unset = UNSET
    description: str | Unset = UNSET
    document: str | Unset = UNSET
    name: str | Unset = UNSET
    system: bool | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arn = self.arn

        attachment_count = self.attachment_count

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        default_version_id = self.default_version_id

        description = self.description

        document = self.document

        name = self.name

        system = self.system

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arn is not UNSET:
            field_dict["arn"] = arn
        if attachment_count is not UNSET:
            field_dict["attachment_count"] = attachment_count
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if default_version_id is not UNSET:
            field_dict["default_version_id"] = default_version_id
        if description is not UNSET:
            field_dict["description"] = description
        if document is not UNSET:
            field_dict["document"] = document
        if name is not UNSET:
            field_dict["name"] = name
        if system is not UNSET:
            field_dict["system"] = system
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arn = d.pop("arn", UNSET)

        attachment_count = d.pop("attachment_count", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        default_version_id = d.pop("default_version_id", UNSET)

        description = d.pop("description", UNSET)

        document = d.pop("document", UNSET)

        name = d.pop("name", UNSET)

        system = d.pop("system", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        object_storage_2_policy_detail_response = cls(
            arn=arn,
            attachment_count=attachment_count,
            created_at=created_at,
            default_version_id=default_version_id,
            description=description,
            document=document,
            name=name,
            system=system,
            updated_at=updated_at,
        )

        object_storage_2_policy_detail_response.additional_properties = d
        return object_storage_2_policy_detail_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
