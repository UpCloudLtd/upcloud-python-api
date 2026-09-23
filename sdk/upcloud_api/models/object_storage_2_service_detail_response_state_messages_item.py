from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.object_storage_2_service_detail_response_state_messages_item_code import (
    ObjectStorage2ServiceDetailResponseStateMessagesItemCode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2ServiceDetailResponseStateMessagesItem")


@_attrs_define
class ObjectStorage2ServiceDetailResponseStateMessagesItem:
    """
    Attributes:
        operational_state (str | Unset):  Example: setup-checkup.
        message (str | Unset):  Example: Certificate issuing is in progress for domains: example.com..
        code (ObjectStorage2ServiceDetailResponseStateMessagesItemCode | Unset):  Example: waiting_certificate_issuing.
        created_at (datetime.datetime | Unset):  Example: 2025-01-16T11:20:40.372611Z.
        updated_at (datetime.datetime | Unset):  Example: 2025-01-16T11:20:40.372611Z.
    """

    operational_state: str | Unset = UNSET
    message: str | Unset = UNSET
    code: ObjectStorage2ServiceDetailResponseStateMessagesItemCode | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operational_state = self.operational_state

        message = self.message

        code: str | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operational_state is not UNSET:
            field_dict["operational_state"] = operational_state
        if message is not UNSET:
            field_dict["message"] = message
        if code is not UNSET:
            field_dict["code"] = code
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operational_state = d.pop("operational_state", UNSET)

        message = d.pop("message", UNSET)

        _code = d.pop("code", UNSET)
        code: ObjectStorage2ServiceDetailResponseStateMessagesItemCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = ObjectStorage2ServiceDetailResponseStateMessagesItemCode(_code)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        object_storage_2_service_detail_response_state_messages_item = cls(
            operational_state=operational_state,
            message=message,
            code=code,
            created_at=created_at,
            updated_at=updated_at,
        )

        object_storage_2_service_detail_response_state_messages_item.additional_properties = d
        return object_storage_2_service_detail_response_state_messages_item

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
