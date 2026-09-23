from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerActionSetHeaderResponse")


@_attrs_define
class LoadBalancerActionSetHeaderResponse:
    """Defines an action that adds or modifies an HTTP header in a request or response. Used when the action type is
    'set_request_header' or 'set_response_header'.

        Example:
            {'header': 'X-Custom-Header', 'value': 'Processed-By-UpCloud-LB'}

        Attributes:
            header (str): Name of the HTTP header to add or modify. Example: X-Custom-Header.
            value (str): Value to assign to the specified header. Example: Processed-By-UpCloud-LB.
    """

    header: str
    value: str

    def to_dict(self) -> dict[str, Any]:
        header = self.header

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "header": header,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        header = d.pop("header")

        value = d.pop("value")

        load_balancer_action_set_header_response = cls(
            header=header,
            value=value,
        )

        return load_balancer_action_set_header_response
