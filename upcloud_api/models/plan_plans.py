from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.plan_plans_plan_item import PlanPlansPlanItem


T = TypeVar("T", bound="PlanPlans")


@_attrs_define
class PlanPlans:
    """
    Example:
        {'plan': [{'core_number': 1, 'memory_amount': 1024, 'name': '1xCPU-1GB', 'public_traffic_out': 1024,
            'storage_size': 25, 'storage_tier': 'maxiops', 'family': 'general_purpose', 'current_offering': 'yes'}]}

    Attributes:
        plan (list[PlanPlansPlanItem]):  Example: [{'core_number': 1, 'memory_amount': 1024, 'name': '1xCPU-1GB',
            'public_traffic_out': 1024, 'storage_size': 25, 'storage_tier': 'maxiops', 'family': 'general_purpose',
            'current_offering': 'yes'}].
    """

    plan: list[PlanPlansPlanItem]

    def to_dict(self) -> dict[str, Any]:
        plan = []
        for plan_item_data in self.plan:
            plan_item = plan_item_data.to_dict()
            plan.append(plan_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "plan": plan,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plan_plans_plan_item import PlanPlansPlanItem  # noqa: PLC0415

        d = dict(src_dict)
        plan = []
        _plan = d.pop("plan")
        for plan_item_data in _plan:
            plan_item = PlanPlansPlanItem.from_dict(plan_item_data)

            plan.append(plan_item)

        plan_plans = cls(
            plan=plan,
        )

        return plan_plans
