from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.load_balancer_action_http_redirect_create_type_1_action_http_redirect_scheme import (
    LoadBalancerActionHttpRedirectCreateType1ActionHttpRedirectScheme,
)
from ..models.load_balancer_action_http_redirect_create_type_1_action_http_redirect_status import (
    LoadBalancerActionHttpRedirectCreateType1ActionHttpRedirectStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerActionHttpRedirectCreateType1")


@_attrs_define
class LoadBalancerActionHttpRedirectCreateType1:
    """
    Attributes:
        scheme (LoadBalancerActionHttpRedirectCreateType1ActionHttpRedirectScheme): URL Schemes
        status (LoadBalancerActionHttpRedirectCreateType1ActionHttpRedirectStatus | Unset): HTTP Status code
    """

    scheme: LoadBalancerActionHttpRedirectCreateType1ActionHttpRedirectScheme
    status: LoadBalancerActionHttpRedirectCreateType1ActionHttpRedirectStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scheme = self.scheme.value

        status: int | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "scheme": scheme,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scheme = LoadBalancerActionHttpRedirectCreateType1ActionHttpRedirectScheme(d.pop("scheme"))

        _status = d.pop("status", UNSET)
        status: LoadBalancerActionHttpRedirectCreateType1ActionHttpRedirectStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LoadBalancerActionHttpRedirectCreateType1ActionHttpRedirectStatus(_status)

        load_balancer_action_http_redirect_create_type_1 = cls(
            scheme=scheme,
            status=status,
        )

        return load_balancer_action_http_redirect_create_type_1
