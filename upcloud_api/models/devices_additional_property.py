from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.devices_additional_property_gpu_plans import DevicesAdditionalPropertyGpuPlans


T = TypeVar("T", bound="DevicesAdditionalProperty")


@_attrs_define
class DevicesAdditionalProperty:
    """Availability grouped by zone.

    Example:
        {'gpu_plans': {'nvidia-a10': {'amount': 1}}}

    Attributes:
        gpu_plans (DevicesAdditionalPropertyGpuPlans | Unset): Available GPU plans in the zone. Example: {'nvidia-a10':
            {'amount': 1}}.
    """

    gpu_plans: DevicesAdditionalPropertyGpuPlans | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gpu_plans: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpu_plans, Unset):
            gpu_plans = self.gpu_plans.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gpu_plans is not UNSET:
            field_dict["gpu_plans"] = gpu_plans

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.devices_additional_property_gpu_plans import DevicesAdditionalPropertyGpuPlans  # noqa: PLC0415

        d = dict(src_dict)
        _gpu_plans = d.pop("gpu_plans", UNSET)
        gpu_plans: DevicesAdditionalPropertyGpuPlans | Unset
        if isinstance(_gpu_plans, Unset):
            gpu_plans = UNSET
        else:
            gpu_plans = DevicesAdditionalPropertyGpuPlans.from_dict(_gpu_plans)

        devices_additional_property = cls(
            gpu_plans=gpu_plans,
        )

        devices_additional_property.additional_properties = d
        return devices_additional_property

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
