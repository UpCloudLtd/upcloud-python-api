from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kubernetes_cluster_plan import KubernetesClusterPlan
from ..types import UNSET, Unset

T = TypeVar("T", bound="KubernetesClusterPatch")


@_attrs_define
class KubernetesClusterPatch:
    """
    Attributes:
        labels (Any):
        control_plane_ip_filter (list[str] | Unset): List of IP blocks
        plan (KubernetesClusterPlan | Unset): Cluster plan
    """

    labels: Any
    control_plane_ip_filter: list[str] | Unset = UNSET
    plan: KubernetesClusterPlan | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        labels = self.labels

        control_plane_ip_filter: list[str] | Unset = UNSET
        if not isinstance(self.control_plane_ip_filter, Unset):
            control_plane_ip_filter = self.control_plane_ip_filter

        plan: str | Unset = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "labels": labels,
            }
        )
        if control_plane_ip_filter is not UNSET:
            field_dict["control_plane_ip_filter"] = control_plane_ip_filter
        if plan is not UNSET:
            field_dict["plan"] = plan

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        labels = d.pop("labels")

        control_plane_ip_filter = cast(list[str], d.pop("control_plane_ip_filter", UNSET))

        _plan = d.pop("plan", UNSET)
        plan: KubernetesClusterPlan | Unset
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = KubernetesClusterPlan(_plan)

        kubernetes_cluster_patch = cls(
            labels=labels,
            control_plane_ip_filter=control_plane_ip_filter,
            plan=plan,
        )

        kubernetes_cluster_patch.additional_properties = d
        return kubernetes_cluster_patch

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
