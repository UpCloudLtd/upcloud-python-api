from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.start_server_server_start_type import StartServerServerStartType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StartServerServer")


@_attrs_define
class StartServerServer:
    """
    Attributes:
        avoid_host (int | Unset): Encoded Private Cloud host ID
        host (int | Unset): Encoded Private Cloud host ID
        reason (str | Unset): Schema for reason strings used in API payloads.
        start_type (StartServerServerStartType | Unset): Whether to wait for the Cloud Server to start.
    """

    avoid_host: int | Unset = UNSET
    host: int | Unset = UNSET
    reason: str | Unset = UNSET
    start_type: StartServerServerStartType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        avoid_host = self.avoid_host

        host = self.host

        reason = self.reason

        start_type: str | Unset = UNSET
        if not isinstance(self.start_type, Unset):
            start_type = self.start_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if avoid_host is not UNSET:
            field_dict["avoid_host"] = avoid_host
        if host is not UNSET:
            field_dict["host"] = host
        if reason is not UNSET:
            field_dict["reason"] = reason
        if start_type is not UNSET:
            field_dict["start_type"] = start_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avoid_host = d.pop("avoid_host", UNSET)

        host = d.pop("host", UNSET)

        reason = d.pop("reason", UNSET)

        _start_type = d.pop("start_type", UNSET)
        start_type: StartServerServerStartType | Unset
        if isinstance(_start_type, Unset):
            start_type = UNSET
        else:
            start_type = StartServerServerStartType(_start_type)

        start_server_server = cls(
            avoid_host=avoid_host,
            host=host,
            reason=reason,
            start_type=start_type,
        )

        return start_server_server
