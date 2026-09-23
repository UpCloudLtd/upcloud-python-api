from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.load_balancer_action_http_redirect_create_type_0 import LoadBalancerActionHttpRedirectCreateType0
    from ..models.load_balancer_action_http_redirect_create_type_1 import LoadBalancerActionHttpRedirectCreateType1


T = TypeVar("T", bound="LoadBalancerActionCreateType2")


@_attrs_define
class LoadBalancerActionCreateType2:
    """
    Attributes:
        type_ (Literal['http_redirect']):
        action_http_redirect (LoadBalancerActionHttpRedirectCreateType0 | LoadBalancerActionHttpRedirectCreateType1):
            Forwarding rule HTTP Redirect action
    """

    type_: Literal["http_redirect"]
    action_http_redirect: LoadBalancerActionHttpRedirectCreateType0 | LoadBalancerActionHttpRedirectCreateType1

    def to_dict(self) -> dict[str, Any]:
        from ..models.load_balancer_action_http_redirect_create_type_0 import (
            LoadBalancerActionHttpRedirectCreateType0,  # noqa: PLC0415
        )

        type_ = self.type_

        action_http_redirect: dict[str, Any]
        if isinstance(self.action_http_redirect, LoadBalancerActionHttpRedirectCreateType0):
            action_http_redirect = self.action_http_redirect.to_dict()
        else:
            action_http_redirect = self.action_http_redirect.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "action_http_redirect": action_http_redirect,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_action_http_redirect_create_type_0 import (
            LoadBalancerActionHttpRedirectCreateType0,  # noqa: PLC0415
        )
        from ..models.load_balancer_action_http_redirect_create_type_1 import (
            LoadBalancerActionHttpRedirectCreateType1,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = cast(Literal["http_redirect"], d.pop("type"))
        if type_ != "http_redirect":
            raise ValueError(f"type must match const 'http_redirect', got '{type_}'")

        def _parse_action_http_redirect(
            data: object,
        ) -> LoadBalancerActionHttpRedirectCreateType0 | LoadBalancerActionHttpRedirectCreateType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasload_balancer_action_http_redirect_create_type_0 = (
                    LoadBalancerActionHttpRedirectCreateType0.from_dict(data)
                )

                return componentsschemasload_balancer_action_http_redirect_create_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasload_balancer_action_http_redirect_create_type_1 = (
                LoadBalancerActionHttpRedirectCreateType1.from_dict(data)
            )

            return componentsschemasload_balancer_action_http_redirect_create_type_1

        action_http_redirect = _parse_action_http_redirect(d.pop("action_http_redirect"))

        load_balancer_action_create_type_2 = cls(
            type_=type_,
            action_http_redirect=action_http_redirect,
        )

        return load_balancer_action_create_type_2
