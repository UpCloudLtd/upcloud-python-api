from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_matcher_backend_create_type_0 import LoadBalancerMatcherBackendCreateType0
    from ..models.load_balancer_matcher_backend_create_type_1 import LoadBalancerMatcherBackendCreateType1


T = TypeVar("T", bound="LoadBalancerMatcherCreateType11")


@_attrs_define
class LoadBalancerMatcherCreateType11:
    """
    Attributes:
        type_ (Literal['num_members_up']):
        match_num_members_up (LoadBalancerMatcherBackendCreateType0 | LoadBalancerMatcherBackendCreateType1): Forwarding
            rule backend matcher
        inverse (bool | Unset): Inverse rule
    """

    type_: Literal["num_members_up"]
    match_num_members_up: LoadBalancerMatcherBackendCreateType0 | LoadBalancerMatcherBackendCreateType1
    inverse: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.load_balancer_matcher_backend_create_type_0 import (
            LoadBalancerMatcherBackendCreateType0,  # noqa: PLC0415
        )

        type_ = self.type_

        match_num_members_up: dict[str, Any]
        if isinstance(self.match_num_members_up, LoadBalancerMatcherBackendCreateType0):
            match_num_members_up = self.match_num_members_up.to_dict()
        else:
            match_num_members_up = self.match_num_members_up.to_dict()

        inverse = self.inverse

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "match_num_members_up": match_num_members_up,
            }
        )
        if inverse is not UNSET:
            field_dict["inverse"] = inverse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_matcher_backend_create_type_0 import (
            LoadBalancerMatcherBackendCreateType0,  # noqa: PLC0415
        )
        from ..models.load_balancer_matcher_backend_create_type_1 import (
            LoadBalancerMatcherBackendCreateType1,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = cast(Literal["num_members_up"], d.pop("type"))
        if type_ != "num_members_up":
            raise ValueError(f"type must match const 'num_members_up', got '{type_}'")

        def _parse_match_num_members_up(
            data: object,
        ) -> LoadBalancerMatcherBackendCreateType0 | LoadBalancerMatcherBackendCreateType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasload_balancer_matcher_backend_create_type_0 = (
                    LoadBalancerMatcherBackendCreateType0.from_dict(data)
                )

                return componentsschemasload_balancer_matcher_backend_create_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasload_balancer_matcher_backend_create_type_1 = (
                LoadBalancerMatcherBackendCreateType1.from_dict(data)
            )

            return componentsschemasload_balancer_matcher_backend_create_type_1

        match_num_members_up = _parse_match_num_members_up(d.pop("match_num_members_up"))

        inverse = d.pop("inverse", UNSET)

        load_balancer_matcher_create_type_11 = cls(
            type_=type_,
            match_num_members_up=match_num_members_up,
            inverse=inverse,
        )

        return load_balancer_matcher_create_type_11
