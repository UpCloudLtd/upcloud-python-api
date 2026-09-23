from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchOpensearchDashboards")


@_attrs_define
class DatabaseServicePropertiesOpensearchOpensearchDashboards:
    """
    Attributes:
        enabled (bool | Unset):
        max_old_space_size (int | Unset): Limits the maximum amount of memory (in MiB) the OpenSearch Dashboards process
            can use. This sets the max_old_space_size option of the nodejs running the OpenSearch Dashboards. Note: the
            memory reserved by OpenSearch Dashboards is not available for OpenSearch.
        multiple_data_source_enabled (bool | Unset):
        opensearch_request_timeout (int | Unset):
        session_keepalive (bool | Unset):
        session_ttl (str | Unset): Defines the time-to-live (TTL) for user sessions. The value should be a time value
            with unit, e.g. 1m, 5s, 1h, 3d, 100ms. Default is 1 hour.
    """

    enabled: bool | Unset = UNSET
    max_old_space_size: int | Unset = UNSET
    multiple_data_source_enabled: bool | Unset = UNSET
    opensearch_request_timeout: int | Unset = UNSET
    session_keepalive: bool | Unset = UNSET
    session_ttl: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        max_old_space_size = self.max_old_space_size

        multiple_data_source_enabled = self.multiple_data_source_enabled

        opensearch_request_timeout = self.opensearch_request_timeout

        session_keepalive = self.session_keepalive

        session_ttl = self.session_ttl

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if max_old_space_size is not UNSET:
            field_dict["max_old_space_size"] = max_old_space_size
        if multiple_data_source_enabled is not UNSET:
            field_dict["multiple_data_source_enabled"] = multiple_data_source_enabled
        if opensearch_request_timeout is not UNSET:
            field_dict["opensearch_request_timeout"] = opensearch_request_timeout
        if session_keepalive is not UNSET:
            field_dict["session_keepalive"] = session_keepalive
        if session_ttl is not UNSET:
            field_dict["session_ttl"] = session_ttl

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        max_old_space_size = d.pop("max_old_space_size", UNSET)

        multiple_data_source_enabled = d.pop("multiple_data_source_enabled", UNSET)

        opensearch_request_timeout = d.pop("opensearch_request_timeout", UNSET)

        session_keepalive = d.pop("session_keepalive", UNSET)

        session_ttl = d.pop("session_ttl", UNSET)

        database_service_properties_opensearch_opensearch_dashboards = cls(
            enabled=enabled,
            max_old_space_size=max_old_space_size,
            multiple_data_source_enabled=multiple_data_source_enabled,
            opensearch_request_timeout=opensearch_request_timeout,
            session_keepalive=session_keepalive,
            session_ttl=session_ttl,
        )

        return database_service_properties_opensearch_opensearch_dashboards
