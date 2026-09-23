from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_error_response_error import LoadBalancerErrorResponseError


T = TypeVar("T", bound="LoadBalancerErrorResponse")


@_attrs_define
class LoadBalancerErrorResponse:
    """Schema for error responses from the API.

    Attributes:
        error (LoadBalancerErrorResponseError | Unset): Error details containing the error message and code.
    """

    error: LoadBalancerErrorResponseError | Unset = UNSET

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
        from ..models.load_balancer_error_response_error import LoadBalancerErrorResponseError  # noqa: PLC0415

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: LoadBalancerErrorResponseError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = LoadBalancerErrorResponseError.from_dict(_error)

        load_balancer_error_response = cls(
            error=error,
        )

        return load_balancer_error_response
