from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.object_storage_2_error_response_type import ObjectStorage2ErrorResponseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_storage_2_error_response_invalid_params_item import (
        ObjectStorage2ErrorResponseInvalidParamsItem,
    )


T = TypeVar("T", bound="ObjectStorage2ErrorResponse")


@_attrs_define
class ObjectStorage2ErrorResponse:
    """Schema for error responses from the API.

    Attributes:
        type_ (ObjectStorage2ErrorResponseType): Error code string. Example:
            https://developers.upcloud.com/1.3/errors#ERROR_INVALID_REQUEST.
        title (str): Short description of the error.
        correlation_id (str): Unique identifier for the request, useful for debugging.
        status (int): HTTP status code associated with the error.
        invalid_params (list[ObjectStorage2ErrorResponseInvalidParamsItem] | Unset): List of invalid parameters in the
            request.
    """

    type_: ObjectStorage2ErrorResponseType
    title: str
    correlation_id: str
    status: int
    invalid_params: list[ObjectStorage2ErrorResponseInvalidParamsItem] | Unset = UNSET

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
        from ..models.object_storage_2_error_response_invalid_params_item import (
            ObjectStorage2ErrorResponseInvalidParamsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = ObjectStorage2ErrorResponseType(d.pop("type"))

        title = d.pop("title")

        correlation_id = d.pop("correlation_id")

        status = d.pop("status")

        _invalid_params = d.pop("invalid_params", UNSET)
        invalid_params: list[ObjectStorage2ErrorResponseInvalidParamsItem] | Unset = UNSET
        if _invalid_params is not UNSET:
            invalid_params = []
            for invalid_params_item_data in _invalid_params:
                invalid_params_item = ObjectStorage2ErrorResponseInvalidParamsItem.from_dict(invalid_params_item_data)

                invalid_params.append(invalid_params_item)

        object_storage_2_error_response = cls(
            type_=type_,
            title=title,
            correlation_id=correlation_id,
            status=status,
            invalid_params=invalid_params,
        )

        return object_storage_2_error_response
