from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerPlan")


@_attrs_define
class LoadBalancerPlan:
    """Represents a load balancer plan, defining the node size, performance characteristics, and associated pricing
    options.

        Attributes:
            name (str | Unset): Name of the plan. Example: development.
            server_number (int | Unset): Number of servers included in the plan. Example: 2.
            per_server_max_sessions (int | Unset): Maximum number of sessions allowed per server. Example: 100.
    """

    name: str | Unset = UNSET
    server_number: int | Unset = UNSET
    per_server_max_sessions: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        server_number = self.server_number

        per_server_max_sessions = self.per_server_max_sessions

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if server_number is not UNSET:
            field_dict["server_number"] = server_number
        if per_server_max_sessions is not UNSET:
            field_dict["per_server_max_sessions"] = per_server_max_sessions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        server_number = d.pop("server_number", UNSET)

        per_server_max_sessions = d.pop("per_server_max_sessions", UNSET)

        load_balancer_plan = cls(
            name=name,
            server_number=server_number,
            per_server_max_sessions=per_server_max_sessions,
        )

        return load_balancer_plan
