from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerActionTcpRejectResponse")


@_attrs_define
class LoadBalancerActionTcpRejectResponse:
    """Defines a TCP rejection action that immediately closes incoming connections when a rule matches. Used when the
    action type is 'tcp_reject'.

        Example:
            {}

    """

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        load_balancer_action_tcp_reject_response = cls()

        return load_balancer_action_tcp_reject_response
