from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerResolverModify")


@_attrs_define
class LoadBalancerResolverModify:
    """Load Balancer Resolver

    Example:
        {'name': 'default-resolver', 'nameservers': ['1.1.1.1:53', '8.8.8.8:53'], 'retries': 3, 'timeout': 5,
            'timeout_retry': 3, 'cache_valid': 300, 'cache_invalid': 60}

    Attributes:
        name (str | Unset): Name of the resolver Example: custom-resolver.
        nameservers (list[str] | Unset): Nameservers Example: ['1.1.1.1:53', '8.8.8.8:53'].
        retries (int | Unset): Number of retries on failure Example: 3.
        timeout (int | Unset): Timeout for the query in seconds Example: 5.
        timeout_retry (int | Unset): Timeout for the query retries in seconds Example: 3.
        cache_valid (int | Unset): Time in seconds to cache valid results Example: 300.
        cache_invalid (int | Unset): Time in seconds to cache invalid results Example: 60.
    """

    name: str | Unset = UNSET
    nameservers: list[str] | Unset = UNSET
    retries: int | Unset = UNSET
    timeout: int | Unset = UNSET
    timeout_retry: int | Unset = UNSET
    cache_valid: int | Unset = UNSET
    cache_invalid: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        nameservers: list[str] | Unset = UNSET
        if not isinstance(self.nameservers, Unset):
            nameservers = self.nameservers

        retries = self.retries

        timeout = self.timeout

        timeout_retry = self.timeout_retry

        cache_valid = self.cache_valid

        cache_invalid = self.cache_invalid

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if nameservers is not UNSET:
            field_dict["nameservers"] = nameservers
        if retries is not UNSET:
            field_dict["retries"] = retries
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if timeout_retry is not UNSET:
            field_dict["timeout_retry"] = timeout_retry
        if cache_valid is not UNSET:
            field_dict["cache_valid"] = cache_valid
        if cache_invalid is not UNSET:
            field_dict["cache_invalid"] = cache_invalid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        nameservers = cast(list[str], d.pop("nameservers", UNSET))

        retries = d.pop("retries", UNSET)

        timeout = d.pop("timeout", UNSET)

        timeout_retry = d.pop("timeout_retry", UNSET)

        cache_valid = d.pop("cache_valid", UNSET)

        cache_invalid = d.pop("cache_invalid", UNSET)

        load_balancer_resolver_modify = cls(
            name=name,
            nameservers=nameservers,
            retries=retries,
            timeout=timeout,
            timeout_retry=timeout_retry,
            cache_valid=cache_valid,
            cache_invalid=cache_invalid,
        )

        return load_balancer_resolver_modify
