from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.stop_server_stop_server_stop_type import StopServerStopServerStopType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StopServerStopServer")


@_attrs_define
class StopServerStopServer:
    """
    Attributes:
        reason (str | Unset): Schema for reason strings used in API payloads.
        stop_type (StopServerStopServerStopType | Unset): Type of stop operation.
        timeout (str | Unset): Soft-stop timeout in seconds.
    """

    reason: str | Unset = UNSET
    stop_type: StopServerStopServerStopType | Unset = UNSET
    timeout: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        stop_type: str | Unset = UNSET
        if not isinstance(self.stop_type, Unset):
            stop_type = self.stop_type.value

        timeout = self.timeout

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if stop_type is not UNSET:
            field_dict["stop_type"] = stop_type
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason", UNSET)

        _stop_type = d.pop("stop_type", UNSET)
        stop_type: StopServerStopServerStopType | Unset
        if isinstance(_stop_type, Unset):
            stop_type = UNSET
        else:
            stop_type = StopServerStopServerStopType(_stop_type)

        timeout = d.pop("timeout", UNSET)

        stop_server_stop_server = cls(
            reason=reason,
            stop_type=stop_type,
            timeout=timeout,
        )

        return stop_server_stop_server
