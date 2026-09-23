from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.timezones_timezones import TimezonesTimezones


T = TypeVar("T", bound="Timezones")


@_attrs_define
class Timezones:
    """List of available timezones

    Example:
        {'timezones': {'timezone': ['UTC', 'Europe/Helsinki', 'America/New_York']}}

    Attributes:
        timezones (TimezonesTimezones):  Example: {'timezone': ['UTC', 'Europe/Helsinki', 'America/New_York']}.
    """

    timezones: TimezonesTimezones

    def to_dict(self) -> dict[str, Any]:
        timezones = self.timezones.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "timezones": timezones,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timezones_timezones import TimezonesTimezones  # noqa: PLC0415

        d = dict(src_dict)
        timezones = TimezonesTimezones.from_dict(d.pop("timezones"))

        timezones = cls(
            timezones=timezones,
        )

        return timezones
