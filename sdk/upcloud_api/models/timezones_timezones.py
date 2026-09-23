from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="TimezonesTimezones")


@_attrs_define
class TimezonesTimezones:
    """
    Example:
        {'timezone': ['UTC', 'Europe/Helsinki', 'America/New_York']}

    Attributes:
        timezone (list[str]):  Example: ['UTC', 'Europe/Helsinki'].
    """

    timezone: list[str]

    def to_dict(self) -> dict[str, Any]:
        timezone = self.timezone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "timezone": timezone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timezone = cast(list[str], d.pop("timezone"))

        timezones_timezones = cls(
            timezone=timezone,
        )

        return timezones_timezones
