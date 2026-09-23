from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kubernetes_storage_tier import KubernetesStorageTier
from ..types import UNSET, Unset

T = TypeVar("T", bound="KubernetesNodeGroupCustomPlan")


@_attrs_define
class KubernetesNodeGroupCustomPlan:
    """Node group custom plan properties

    Attributes:
        memory (int): The amount of memory in megabytes to assign to individual node group node when using custom plan
        cores (int): The number of CPU cores dedicated to individual node group nodes when using custom plan
        storage_size (int): The size of the storage device in gigabytes.
        storage_tier (KubernetesStorageTier | Unset): The storage tier to use.
    """

    memory: int
    cores: int
    storage_size: int
    storage_tier: KubernetesStorageTier | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memory = self.memory

        cores = self.cores

        storage_size = self.storage_size

        storage_tier: str | Unset = UNSET
        if not isinstance(self.storage_tier, Unset):
            storage_tier = self.storage_tier.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "memory": memory,
                "cores": cores,
                "storage_size": storage_size,
            }
        )
        if storage_tier is not UNSET:
            field_dict["storage_tier"] = storage_tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        memory = d.pop("memory")

        cores = d.pop("cores")

        storage_size = d.pop("storage_size")

        _storage_tier = d.pop("storage_tier", UNSET)
        storage_tier: KubernetesStorageTier | Unset
        if isinstance(_storage_tier, Unset):
            storage_tier = UNSET
        else:
            storage_tier = KubernetesStorageTier(_storage_tier)

        kubernetes_node_group_custom_plan = cls(
            memory=memory,
            cores=cores,
            storage_size=storage_size,
            storage_tier=storage_tier,
        )

        kubernetes_node_group_custom_plan.additional_properties = d
        return kubernetes_node_group_custom_plan

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
