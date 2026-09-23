from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.object_storage_2_access_key_detail_response_status import ObjectStorage2AccessKeyDetailResponseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2AccessKeyDetailResponse")


@_attrs_define
class ObjectStorage2AccessKeyDetailResponse:
    """Response schema for access key details.

    Attributes:
        access_key_id (str | Unset):
        created_at (datetime.datetime | Unset):
        last_used_at (datetime.datetime | Unset):
        secret_access_key (str | Unset): Only returned upon creation, empty otherwise.
        status (ObjectStorage2AccessKeyDetailResponseStatus | Unset):
    """

    access_key_id: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    last_used_at: datetime.datetime | Unset = UNSET
    secret_access_key: str | Unset = UNSET
    status: ObjectStorage2AccessKeyDetailResponseStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_key_id = self.access_key_id

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        last_used_at: str | Unset = UNSET
        if not isinstance(self.last_used_at, Unset):
            last_used_at = self.last_used_at.isoformat()

        secret_access_key = self.secret_access_key

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_key_id is not UNSET:
            field_dict["access_key_id"] = access_key_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if secret_access_key is not UNSET:
            field_dict["secret_access_key"] = secret_access_key
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_key_id = d.pop("access_key_id", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _last_used_at = d.pop("last_used_at", UNSET)
        last_used_at: datetime.datetime | Unset
        if isinstance(_last_used_at, Unset):
            last_used_at = UNSET
        else:
            last_used_at = datetime.datetime.fromisoformat(_last_used_at)

        secret_access_key = d.pop("secret_access_key", UNSET)

        _status = d.pop("status", UNSET)
        status: ObjectStorage2AccessKeyDetailResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ObjectStorage2AccessKeyDetailResponseStatus(_status)

        object_storage_2_access_key_detail_response = cls(
            access_key_id=access_key_id,
            created_at=created_at,
            last_used_at=last_used_at,
            secret_access_key=secret_access_key,
            status=status,
        )

        object_storage_2_access_key_detail_response.additional_properties = d
        return object_storage_2_access_key_detail_response

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
