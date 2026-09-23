from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchSearchBackpressureNodeDuressSettings")


@_attrs_define
class DatabaseServicePropertiesOpensearchSearchBackpressureNodeDuressSettings:
    """
    Attributes:
        cpu_threshold (float | Unset): The CPU usage threshold (as a percentage) required for a node to be considered to
            be under duress. Default is 0.9
        heap_threshold (float | Unset): The heap usage threshold (as a percentage) required for a node to be considered
            to be under duress. Default is 0.7
        num_successive_breaches (int | Unset): The number of successive limit breaches after which the node is
            considered to be under duress. Default is 3
    """

    cpu_threshold: float | Unset = UNSET
    heap_threshold: float | Unset = UNSET
    num_successive_breaches: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cpu_threshold = self.cpu_threshold

        heap_threshold = self.heap_threshold

        num_successive_breaches = self.num_successive_breaches

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cpu_threshold is not UNSET:
            field_dict["cpu_threshold"] = cpu_threshold
        if heap_threshold is not UNSET:
            field_dict["heap_threshold"] = heap_threshold
        if num_successive_breaches is not UNSET:
            field_dict["num_successive_breaches"] = num_successive_breaches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpu_threshold = d.pop("cpu_threshold", UNSET)

        heap_threshold = d.pop("heap_threshold", UNSET)

        num_successive_breaches = d.pop("num_successive_breaches", UNSET)

        database_service_properties_opensearch_search_backpressure_node_duress_settings = cls(
            cpu_threshold=cpu_threshold,
            heap_threshold=heap_threshold,
            num_successive_breaches=num_successive_breaches,
        )

        return database_service_properties_opensearch_search_backpressure_node_duress_settings
