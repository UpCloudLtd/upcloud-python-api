from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerResolverCreate")


@_attrs_define
class LoadBalancerResolverCreate:
    """Load Balancer Resolver

    Example:
        {'name': 'default-resolver', 'nameservers': ['1.1.1.1:53', '8.8.8.8:53'], 'retries': 3, 'timeout': 5,
            'timeout_retry': 3, 'cache_valid': 300, 'cache_invalid': 60}

    Attributes:
        name (str): Name of the resolver Example: default-resolver.
        nameservers (list[str]): Nameservers Example: ['1.1.1.1:53', '8.8.8.8:53'].
        retries (int): Number of retries on failure Example: 3.
        timeout (int): Timeout for the query in seconds Example: 5.
        timeout_retry (int): Timeout for the query retries in seconds Example: 3.
        cache_valid (int): Time in seconds to cache valid results Example: 300.
        cache_invalid (int): Time in seconds to cache invalid results Example: 60.
    """

    name: str
    nameservers: list[str]
    retries: int
    timeout: int
    timeout_retry: int
    cache_valid: int
    cache_invalid: int

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        nameservers = self.nameservers

        retries = self.retries

        timeout = self.timeout

        timeout_retry = self.timeout_retry

        cache_valid = self.cache_valid

        cache_invalid = self.cache_invalid

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "nameservers": nameservers,
                "retries": retries,
                "timeout": timeout,
                "timeout_retry": timeout_retry,
                "cache_valid": cache_valid,
                "cache_invalid": cache_invalid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        nameservers = cast(list[str], d.pop("nameservers"))

        retries = d.pop("retries")

        timeout = d.pop("timeout")

        timeout_retry = d.pop("timeout_retry")

        cache_valid = d.pop("cache_valid")

        cache_invalid = d.pop("cache_invalid")

        load_balancer_resolver_create = cls(
            name=name,
            nameservers=nameservers,
            retries=retries,
            timeout=timeout,
            timeout_retry=timeout_retry,
            cache_valid=cache_valid,
            cache_invalid=cache_invalid,
        )

        return load_balancer_resolver_create
