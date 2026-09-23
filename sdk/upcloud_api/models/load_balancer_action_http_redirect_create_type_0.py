from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.load_balancer_action_http_redirect_create_type_0_action_http_redirect_status import (
    LoadBalancerActionHttpRedirectCreateType0ActionHttpRedirectStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerActionHttpRedirectCreateType0")


@_attrs_define
class LoadBalancerActionHttpRedirectCreateType0:
    """
    Attributes:
        location (str): Value
        status (LoadBalancerActionHttpRedirectCreateType0ActionHttpRedirectStatus | Unset): HTTP Status code
    """

    location: str
    status: LoadBalancerActionHttpRedirectCreateType0ActionHttpRedirectStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        location = self.location

        status: int | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "location": location,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location = d.pop("location")

        _status = d.pop("status", UNSET)
        status: LoadBalancerActionHttpRedirectCreateType0ActionHttpRedirectStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LoadBalancerActionHttpRedirectCreateType0ActionHttpRedirectStatus(_status)

        load_balancer_action_http_redirect_create_type_0 = cls(
            location=location,
            status=status,
        )

        return load_balancer_action_http_redirect_create_type_0
