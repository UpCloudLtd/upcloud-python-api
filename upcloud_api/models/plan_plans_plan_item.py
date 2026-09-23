from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.plan_boolean_yesno import PlanBooleanYesno
from ..models.plan_family import PlanFamily
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanPlansPlanItem")


@_attrs_define
class PlanPlansPlanItem:
    """
    Attributes:
        core_number (int): The number of CPU cores included in the plan, represented as a positive integer. This value
            must be greater than zero.
        memory_amount (int): The amount of memory included in the plan, measured in mebibytes (MiB).
        name (str): Server plan identifier
        family (PlanFamily): The plan family identifier. Plan families group plans by their intended use case.
        current_offering (PlanBooleanYesno): Boolean value represented as yes/no Example: yes.
        public_traffic_out (int | Unset): The amount of public traffic out included in the plan, measured in gigabytes
            (GB).
        storage_size (int | Unset): The block storage size for the plan in gibibytes (GiB). The value is 0 if the plan
            does not include block storage.
        storage_tier (None | str | Unset): Block storage performance and pricing tier. `maxiops` is high-performance
            block storage, `standard` is general-purpose block storage, and `hdd` is the API name for the high-capacity
            Archive tier. The value can be null when a plan does not include block storage.
        gpu_amount (int | Unset): The number of GPUs included in the plan.
        gpu_model (str | Unset): The GPU model included in the plan.
    """

    core_number: int
    memory_amount: int
    name: str
    family: PlanFamily
    current_offering: PlanBooleanYesno
    public_traffic_out: int | Unset = UNSET
    storage_size: int | Unset = UNSET
    storage_tier: None | str | Unset = UNSET
    gpu_amount: int | Unset = UNSET
    gpu_model: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        core_number = self.core_number

        memory_amount = self.memory_amount

        name = self.name

        family = self.family.value

        current_offering = self.current_offering.value

        public_traffic_out = self.public_traffic_out

        storage_size = self.storage_size

        storage_tier: None | str | Unset
        if isinstance(self.storage_tier, Unset):
            storage_tier = UNSET
        else:
            storage_tier = self.storage_tier

        gpu_amount = self.gpu_amount

        gpu_model = self.gpu_model

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "core_number": core_number,
                "memory_amount": memory_amount,
                "name": name,
                "family": family,
                "current_offering": current_offering,
            }
        )
        if public_traffic_out is not UNSET:
            field_dict["public_traffic_out"] = public_traffic_out
        if storage_size is not UNSET:
            field_dict["storage_size"] = storage_size
        if storage_tier is not UNSET:
            field_dict["storage_tier"] = storage_tier
        if gpu_amount is not UNSET:
            field_dict["gpu_amount"] = gpu_amount
        if gpu_model is not UNSET:
            field_dict["gpu_model"] = gpu_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        core_number = d.pop("core_number")

        memory_amount = d.pop("memory_amount")

        name = d.pop("name")

        family = PlanFamily(d.pop("family"))

        current_offering = PlanBooleanYesno(d.pop("current_offering"))

        public_traffic_out = d.pop("public_traffic_out", UNSET)

        storage_size = d.pop("storage_size", UNSET)

        def _parse_storage_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_tier = _parse_storage_tier(d.pop("storage_tier", UNSET))

        gpu_amount = d.pop("gpu_amount", UNSET)

        gpu_model = d.pop("gpu_model", UNSET)

        plan_plans_plan_item = cls(
            core_number=core_number,
            memory_amount=memory_amount,
            name=name,
            family=family,
            current_offering=current_offering,
            public_traffic_out=public_traffic_out,
            storage_size=storage_size,
            storage_tier=storage_tier,
            gpu_amount=gpu_amount,
            gpu_model=gpu_model,
        )

        return plan_plans_plan_item
