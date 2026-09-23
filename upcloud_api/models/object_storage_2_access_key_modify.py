from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.object_storage_2_access_key_modify_status import ObjectStorage2AccessKeyModifyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2AccessKeyModify")


@_attrs_define
class ObjectStorage2AccessKeyModify:
    """Schema for modifying an access key.

    Attributes:
        status (ObjectStorage2AccessKeyModifyStatus | Unset): Indicates if the key is active or inactive. Example:
            Inactive.
    """

    status: ObjectStorage2AccessKeyModifyStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ObjectStorage2AccessKeyModifyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ObjectStorage2AccessKeyModifyStatus(_status)

        object_storage_2_access_key_modify = cls(
            status=status,
        )

        return object_storage_2_access_key_modify
