from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_plan_components_response_compute_family import DatabasePlanComponentsResponseComputeFamily
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabasePlanComponentsResponseCompute")


@_attrs_define
class DatabasePlanComponentsResponseCompute:
    """Compute resources per service

    Attributes:
        name (str | Unset): Compute shape name usable as plan_compute in requests.
        family (DatabasePlanComponentsResponseComputeFamily | Unset): Compute family for tiered plans. Omitted for
            classic plans. Example: standard.
        node_count (int | Unset): Number of nodes Example: 2.
        cpu (int | Unset): CPU cores per node Example: 4.
        memory_gb (int | Unset): Memory per node in GB Example: 8.
    """

    name: str | Unset = UNSET
    family: DatabasePlanComponentsResponseComputeFamily | Unset = UNSET
    node_count: int | Unset = UNSET
    cpu: int | Unset = UNSET
    memory_gb: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        family: str | Unset = UNSET
        if not isinstance(self.family, Unset):
            family = self.family.value

        node_count = self.node_count

        cpu = self.cpu

        memory_gb = self.memory_gb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if family is not UNSET:
            field_dict["family"] = family
        if node_count is not UNSET:
            field_dict["node_count"] = node_count
        if cpu is not UNSET:
            field_dict["cpu"] = cpu
        if memory_gb is not UNSET:
            field_dict["memory_gb"] = memory_gb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _family = d.pop("family", UNSET)
        family: DatabasePlanComponentsResponseComputeFamily | Unset
        if isinstance(_family, Unset):
            family = UNSET
        else:
            family = DatabasePlanComponentsResponseComputeFamily(_family)

        node_count = d.pop("node_count", UNSET)

        cpu = d.pop("cpu", UNSET)

        memory_gb = d.pop("memory_gb", UNSET)

        database_plan_components_response_compute = cls(
            name=name,
            family=family,
            node_count=node_count,
            cpu=cpu,
            memory_gb=memory_gb,
        )

        database_plan_components_response_compute.additional_properties = d
        return database_plan_components_response_compute

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
