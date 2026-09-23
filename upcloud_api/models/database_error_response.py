from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_error_response_error import DatabaseErrorResponseError


T = TypeVar("T", bound="DatabaseErrorResponse")


@_attrs_define
class DatabaseErrorResponse:
    """Schema for error responses from the API.

    Attributes:
        error (DatabaseErrorResponseError | Unset):
    """

    error: DatabaseErrorResponseError | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_error_response_error import DatabaseErrorResponseError  # noqa: PLC0415

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: DatabaseErrorResponseError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = DatabaseErrorResponseError.from_dict(_error)

        database_error_response = cls(
            error=error,
        )

        return database_error_response
