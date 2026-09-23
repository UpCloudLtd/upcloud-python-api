from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.database_service_properties_opensearch_cluster_search_request_slowlog_log_level import (
    DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlogLogLevel,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_service_properties_opensearch_cluster_search_request_slowlog_threshold import (
        DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlogThreshold,
    )


T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlog")


@_attrs_define
class DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlog:
    """
    Attributes:
        level (DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlogLogLevel | Unset):
        threshold (DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlogThreshold | Unset):
    """

    level: DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlogLogLevel | Unset = UNSET
    threshold: DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlogThreshold | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        level: str | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        threshold: dict[str, Any] | Unset = UNSET
        if not isinstance(self.threshold, Unset):
            threshold = self.threshold.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if level is not UNSET:
            field_dict["level"] = level
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_service_properties_opensearch_cluster_search_request_slowlog_threshold import (
            DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlogThreshold,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _level = d.pop("level", UNSET)
        level: DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlogLogLevel | Unset
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlogLogLevel(_level)

        _threshold = d.pop("threshold", UNSET)
        threshold: DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlogThreshold | Unset
        if isinstance(_threshold, Unset):
            threshold = UNSET
        else:
            threshold = DatabaseServicePropertiesOpensearchClusterSearchRequestSlowlogThreshold.from_dict(_threshold)

        database_service_properties_opensearch_cluster_search_request_slowlog = cls(
            level=level,
            threshold=threshold,
        )

        return database_service_properties_opensearch_cluster_search_request_slowlog
