from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.plan_plans import PlanPlans


T = TypeVar("T", bound="Plan")


@_attrs_define
class Plan:
    """List response containing available server plans.

    Example:
        {'plans': {'plan': [{'core_number': 1, 'memory_amount': 1024, 'name': '1xCPU-1GB', 'public_traffic_out': 1024,
            'storage_size': 25, 'storage_tier': 'maxiops', 'family': 'general_purpose', 'current_offering': 'yes'}]}}

    Attributes:
        plans (PlanPlans):  Example: {'plan': [{'core_number': 1, 'memory_amount': 1024, 'name': '1xCPU-1GB',
            'public_traffic_out': 1024, 'storage_size': 25, 'storage_tier': 'maxiops', 'family': 'general_purpose',
            'current_offering': 'yes'}]}.
    """

    plans: PlanPlans

    def to_dict(self) -> dict[str, Any]:
        plans = self.plans.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "plans": plans,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan_plans import PlanPlans  # noqa: PLC0415

        d = dict(src_dict)
        plans = PlanPlans.from_dict(d.pop("plans"))

        plan = cls(
            plans=plans,
        )

        return plan
