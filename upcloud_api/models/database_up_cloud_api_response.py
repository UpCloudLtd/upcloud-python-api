from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_up_cloud_api_response_errors_item import DatabaseUpCloudApiResponseErrorsItem


T = TypeVar("T", bound="DatabaseUpCloudApiResponse")


@_attrs_define
class DatabaseUpCloudApiResponse:
    """Schema for UpCloud API error responses.

    Attributes:
        errors (list[DatabaseUpCloudApiResponseErrorsItem] | Unset): A list of error messages returned by UpCloud's API.
            Example: [{'message': 'Invalid request', 'more_info': 'https://developers.upcloud.com/errors', 'status': 400}].
        message (str | Unset): The time the backup was created. Example: An error occurred while processing your
            request..
    """

    errors: list[DatabaseUpCloudApiResponseErrorsItem] | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_up_cloud_api_response_errors_item import (
            DatabaseUpCloudApiResponseErrorsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[DatabaseUpCloudApiResponseErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = DatabaseUpCloudApiResponseErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        message = d.pop("message", UNSET)

        database_up_cloud_api_response = cls(
            errors=errors,
            message=message,
        )

        database_up_cloud_api_response.additional_properties = d
        return database_up_cloud_api_response

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
