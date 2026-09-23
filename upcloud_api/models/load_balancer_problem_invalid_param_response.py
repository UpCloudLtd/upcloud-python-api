from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerProblemInvalidParamResponse")


@_attrs_define
class LoadBalancerProblemInvalidParamResponse:
    """Provides detailed information about a specific invalid parameter that caused a request to fail validation, as an
    extension of RFC7807 Problem Details.

        Example:
            {'name': 'hostnames[0]', 'reason': 'Invalid domain name format'}

        Attributes:
            name (str): The name of the parameter or form field that caused the validation error. It can include structural
                delimiters to indicate nested fields (e.g., 'data.attributes.email'). Example: hostnames[0].
            reason (str): A human-readable message explaining why the parameter value was invalid, either syntactically or
                semantically. Example: Invalid domain name format.
    """

    name: str
    reason: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        reason = d.pop("reason")

        load_balancer_problem_invalid_param_response = cls(
            name=name,
            reason=reason,
        )

        return load_balancer_problem_invalid_param_response
