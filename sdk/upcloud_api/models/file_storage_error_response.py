from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.file_storage_error_response_type import FileStorageErrorResponseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_storage_error_response_invalid_params_item import FileStorageErrorResponseInvalidParamsItem


T = TypeVar("T", bound="FileStorageErrorResponse")


@_attrs_define
class FileStorageErrorResponse:
    """Schema for error responses from the API.

    Attributes:
        type_ (FileStorageErrorResponseType): Error code string.
        title (str): Short description of the error.
        correlation_id (str): Unique identifier for the request, useful for debugging.
        status (int): HTTP status code associated with the error.
        invalid_params (list[FileStorageErrorResponseInvalidParamsItem] | Unset): List of invalid parameters in the
            request.
    """

    type_: FileStorageErrorResponseType
    title: str
    correlation_id: str
    status: int
    invalid_params: list[FileStorageErrorResponseInvalidParamsItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        title = self.title

        correlation_id = self.correlation_id

        status = self.status

        invalid_params: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invalid_params, Unset):
            invalid_params = []
            for invalid_params_item_data in self.invalid_params:
                invalid_params_item = invalid_params_item_data.to_dict()
                invalid_params.append(invalid_params_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "title": title,
                "correlation_id": correlation_id,
                "status": status,
            }
        )
        if invalid_params is not UNSET:
            field_dict["invalid_params"] = invalid_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_storage_error_response_invalid_params_item import (
            FileStorageErrorResponseInvalidParamsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = FileStorageErrorResponseType(d.pop("type"))

        title = d.pop("title")

        correlation_id = d.pop("correlation_id")

        status = d.pop("status")

        _invalid_params = d.pop("invalid_params", UNSET)
        invalid_params: list[FileStorageErrorResponseInvalidParamsItem] | Unset = UNSET
        if _invalid_params is not UNSET:
            invalid_params = []
            for invalid_params_item_data in _invalid_params:
                invalid_params_item = FileStorageErrorResponseInvalidParamsItem.from_dict(invalid_params_item_data)

                invalid_params.append(invalid_params_item)

        file_storage_error_response = cls(
            type_=type_,
            title=title,
            correlation_id=correlation_id,
            status=status,
            invalid_params=invalid_params,
        )

        return file_storage_error_response
