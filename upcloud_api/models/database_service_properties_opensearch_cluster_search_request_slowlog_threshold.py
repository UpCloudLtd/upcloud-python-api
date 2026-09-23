from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlogThreshold")


@_attrs_define
class DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlogThreshold:
    """
    Attributes:
        debug (str | Unset):
        info (str | Unset):
        trace (str | Unset):
        warn (str | Unset):
    """

    debug: str | Unset = UNSET
    info: str | Unset = UNSET
    trace: str | Unset = UNSET
    warn: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        debug = self.debug

        info = self.info

        trace = self.trace

        warn = self.warn

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if debug is not UNSET:
            field_dict["debug"] = debug
        if info is not UNSET:
            field_dict["info"] = info
        if trace is not UNSET:
            field_dict["trace"] = trace
        if warn is not UNSET:
            field_dict["warn"] = warn

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        debug = d.pop("debug", UNSET)

        info = d.pop("info", UNSET)

        trace = d.pop("trace", UNSET)

        warn = d.pop("warn", UNSET)

        database_service_properties_opensearch_cluster_search_request_slowlog_threshold = cls(
            debug=debug,
            info=info,
            trace=trace,
            warn=warn,
        )

        return database_service_properties_opensearch_cluster_search_request_slowlog_threshold
