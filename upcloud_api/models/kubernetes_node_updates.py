from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kubernetes_node_updates_schedule_dow import KubernetesNodeUpdatesScheduleDow

T = TypeVar("T", bound="KubernetesNodeUpdates")


@_attrs_define
class KubernetesNodeUpdates:
    """Enable periodic package updates on node

    Attributes:
        kubernetes_patches (bool): Include Kubernetes package patch updates (kubeadm, kubectl, kubelet) Default: False.
        schedule_dow (KubernetesNodeUpdatesScheduleDow): The day of the week on which updates will be performed
        schedule_time (str): The time at which the updates will be applied in UTC (HH:MM). Example: 06:00.
    """

    schedule_dow: KubernetesNodeUpdatesScheduleDow
    schedule_time: str
    kubernetes_patches: bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kubernetes_patches = self.kubernetes_patches

        schedule_dow = self.schedule_dow.value

        schedule_time = self.schedule_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kubernetes_patches": kubernetes_patches,
                "schedule_dow": schedule_dow,
                "schedule_time": schedule_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kubernetes_patches = d.pop("kubernetes_patches")

        schedule_dow = KubernetesNodeUpdatesScheduleDow(d.pop("schedule_dow"))

        schedule_time = d.pop("schedule_time")

        kubernetes_node_updates = cls(
            kubernetes_patches=kubernetes_patches,
            schedule_dow=schedule_dow,
            schedule_time=schedule_time,
        )

        kubernetes_node_updates.additional_properties = d
        return kubernetes_node_updates

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
