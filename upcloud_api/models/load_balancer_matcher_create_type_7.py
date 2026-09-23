from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_matcher_string_create_type_0 import LoadBalancerMatcherStringCreateType0
    from ..models.load_balancer_matcher_string_create_type_1 import LoadBalancerMatcherStringCreateType1


T = TypeVar("T", bound="LoadBalancerMatcherCreateType7")


@_attrs_define
class LoadBalancerMatcherCreateType7:
    """
    Attributes:
        type_ (Literal['path']):
        match_path (LoadBalancerMatcherStringCreateType0 | LoadBalancerMatcherStringCreateType1): Forwarding rule string
            matcher
        inverse (bool | Unset): Inverse rule
    """

    type_: Literal["path"]
    match_path: LoadBalancerMatcherStringCreateType0 | LoadBalancerMatcherStringCreateType1
    inverse: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.load_balancer_matcher_string_create_type_0 import (
            LoadBalancerMatcherStringCreateType0,  # noqa: PLC0415
        )

        type_ = self.type_

        match_path: dict[str, Any]
        if isinstance(self.match_path, LoadBalancerMatcherStringCreateType0):
            match_path = self.match_path.to_dict()
        else:
            match_path = self.match_path.to_dict()

        inverse = self.inverse

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "match_path": match_path,
            }
        )
        if inverse is not UNSET:
            field_dict["inverse"] = inverse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_matcher_string_create_type_0 import (
            LoadBalancerMatcherStringCreateType0,  # noqa: PLC0415
        )
        from ..models.load_balancer_matcher_string_create_type_1 import (
            LoadBalancerMatcherStringCreateType1,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = cast(Literal["path"], d.pop("type"))
        if type_ != "path":
            raise ValueError(f"type must match const 'path', got '{type_}'")

        def _parse_match_path(
            data: object,
        ) -> LoadBalancerMatcherStringCreateType0 | LoadBalancerMatcherStringCreateType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemasload_balancer_matcher_string_create_type_0 = (
                    LoadBalancerMatcherStringCreateType0.from_dict(data)
                )

                return componentsschemasload_balancer_matcher_string_create_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemasload_balancer_matcher_string_create_type_1 = (
                LoadBalancerMatcherStringCreateType1.from_dict(data)
            )

            return componentsschemasload_balancer_matcher_string_create_type_1

        match_path = _parse_match_path(d.pop("match_path"))

        inverse = d.pop("inverse", UNSET)

        load_balancer_matcher_create_type_7 = cls(
            type_=type_,
            match_path=match_path,
            inverse=inverse,
        )

        return load_balancer_matcher_create_type_7
