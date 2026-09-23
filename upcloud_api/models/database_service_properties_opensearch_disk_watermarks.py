from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DatabaseServicePropertiesOpensearchDiskWatermarks")


@_attrs_define
class DatabaseServicePropertiesOpensearchDiskWatermarks:
    """
    Attributes:
        flood_stage (int): The flood stage watermark for disk usage.
        high (int): The high watermark for disk usage.
        low (int): The low watermark for disk usage.
    """

    flood_stage: int
    high: int
    low: int

    def to_dict(self) -> dict[str, Any]:
        flood_stage = self.flood_stage

        high = self.high

        low = self.low

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "flood_stage": flood_stage,
                "high": high,
                "low": low,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        flood_stage = d.pop("flood_stage")

        high = d.pop("high")

        low = d.pop("low")

        database_service_properties_opensearch_disk_watermarks = cls(
            flood_stage=flood_stage,
            high=high,
            low=low,
        )

        return database_service_properties_opensearch_disk_watermarks
