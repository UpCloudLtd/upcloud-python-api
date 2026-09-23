from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LoadBalancerResolver")


@_attrs_define
class LoadBalancerResolver:
    """Represents a DNS resolver configuration for a load balancer service, defining the nameservers, retry behavior, and
    caching rules used to resolve backend hostnames.

        Attributes:
            name (str): Human-readable name assigned to the DNS resolver. Example: default-resolver.
            nameservers (list[str]): List of DNS nameserver addresses (with optional port) used to resolve backend member
                hostnames. Example: ['1.1.1.1:53', '8.8.8.8:53'].
            retries (int): Number of retry attempts for failed DNS queries. Example: 3.
            timeout (int): Initial timeout in milliseconds for DNS query responses. Example: 30.
            timeout_retry (int): Timeout in milliseconds for DNS query retry attempts. Example: 5.
            cache_valid (int): Time in seconds to cache valid (successful) DNS responses. Example: 60.
            cache_invalid (int): Time in seconds to cache invalid (failed) DNS responses. Example: 5.
            created_at (datetime.datetime): Timestamp when the DNS resolver was created (RFC 3339 format).
            updated_at (datetime.datetime): Timestamp when the DNS resolver was last updated (RFC 3339 format).
    """

    name: str
    nameservers: list[str]
    retries: int
    timeout: int
    timeout_retry: int
    cache_valid: int
    cache_invalid: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        nameservers = self.nameservers

        retries = self.retries

        timeout = self.timeout

        timeout_retry = self.timeout_retry

        cache_valid = self.cache_valid

        cache_invalid = self.cache_invalid

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "nameservers": nameservers,
                "retries": retries,
                "timeout": timeout,
                "timeout_retry": timeout_retry,
                "cache_valid": cache_valid,
                "cache_invalid": cache_invalid,
                "created_at": created_at,
                "updated_at": updated_at,
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

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        load_balancer_resolver = cls(
            name=name,
            nameservers=nameservers,
            retries=retries,
            timeout=timeout,
            timeout_retry=timeout_retry,
            cache_valid=cache_valid,
            cache_invalid=cache_invalid,
            created_at=created_at,
            updated_at=updated_at,
        )

        load_balancer_resolver.additional_properties = d
        return load_balancer_resolver

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
