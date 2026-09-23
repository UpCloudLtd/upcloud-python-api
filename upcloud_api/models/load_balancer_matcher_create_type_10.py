from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_matcher_string_create_type_0 import LoadBalancerMatcherStringCreateType0
    from ..models.load_balancer_matcher_string_create_type_1 import LoadBalancerMatcherStringCreateType1


T = TypeVar("T", bound="LoadBalancerMatcherCreateType10")


@_attrs_define
class LoadBalancerMatcherCreateType10:
    """
    Attributes:
        type_ (Literal['url_query']):
        match_url_query (LoadBalancerMatcherStringCreateType0 | LoadBalancerMatcherStringCreateType1): Forwarding rule
            string matcher
        inverse (bool | Unset): Inverse rule
    """

    type_: Literal["url_query"]
    match_url_query: LoadBalancerMatcherStringCreateType0 | LoadBalancerMatcherStringCreateType1
    inverse: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.load_balancer_matcher_string_create_type_0 import (
            LoadBalancerMatcherStringCreateType0,  # noqa: PLC0415
        )

        type_ = self.type_

        match_url_query: dict[str, Any]
        if isinstance(self.match_url_query, LoadBalancerMatcherStringCreateType0):
            match_url_query = self.match_url_query.to_dict()
        else:
            match_url_query = self.match_url_query.to_dict()

        inverse = self.inverse

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "match_url_query": match_url_query,
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
        type_ = cast(Literal["url_query"], d.pop("type"))
        if type_ != "url_query":
            raise ValueError(f"type must match const 'url_query', got '{type_}'")

        def _parse_match_url_query(
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

        match_url_query = _parse_match_url_query(d.pop("match_url_query"))

        inverse = d.pop("inverse", UNSET)

        load_balancer_matcher_create_type_10 = cls(
            type_=type_,
            match_url_query=match_url_query,
            inverse=inverse,
        )

        return load_balancer_matcher_create_type_10
