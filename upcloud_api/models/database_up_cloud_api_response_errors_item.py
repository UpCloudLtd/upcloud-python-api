from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseUpCloudApiResponseErrorsItem")


@_attrs_define
class DatabaseUpCloudApiResponseErrorsItem:
    """
    Attributes:
        message (str | Unset): A descriptive error message.
        more_info (str | Unset): A URL pointing to more information about the error.
        status (int | Unset): The HTTP status code associated with the error.
    """

    message: str | Unset = UNSET
    more_info: str | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        more_info = self.more_info

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if more_info is not UNSET:
            field_dict["more_info"] = more_info
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        more_info = d.pop("more_info", UNSET)

        status = d.pop("status", UNSET)

        database_up_cloud_api_response_errors_item = cls(
            message=message,
            more_info=more_info,
            status=status,
        )

        database_up_cloud_api_response_errors_item.additional_properties = d
        return database_up_cloud_api_response_errors_item

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
