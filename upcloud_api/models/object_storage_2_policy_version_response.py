from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2PolicyVersionResponse")


@_attrs_define
class ObjectStorage2PolicyVersionResponse:
    """Schema for a policy version response, including creation date, document content, default status, and version ID.

    Attributes:
        create_date (datetime.datetime | Unset):
        document (str | Unset):
        is_default (bool | Unset):
        version_id (str | Unset):
    """

    create_date: datetime.datetime | Unset = UNSET
    document: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    version_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_date: str | Unset = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        document = self.document

        is_default = self.is_default

        version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_date is not UNSET:
            field_dict["create_date"] = create_date
        if document is not UNSET:
            field_dict["document"] = document
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _create_date = d.pop("create_date", UNSET)
        create_date: datetime.datetime | Unset
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = datetime.datetime.fromisoformat(_create_date)

        document = d.pop("document", UNSET)

        is_default = d.pop("is_default", UNSET)

        version_id = d.pop("version_id", UNSET)

        object_storage_2_policy_version_response = cls(
            create_date=create_date,
            document=document,
            is_default=is_default,
            version_id=version_id,
        )

        object_storage_2_policy_version_response.additional_properties = d
        return object_storage_2_policy_version_response

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
