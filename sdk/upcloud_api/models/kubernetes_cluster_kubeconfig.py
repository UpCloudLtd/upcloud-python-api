from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="KubernetesClusterKubeconfig")


@_attrs_define
class KubernetesClusterKubeconfig:
    """Kubernetes cluster kubeconfig

    Attributes:
        kubeconfig (str): Kubeconfig
    """

    kubeconfig: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kubeconfig = self.kubeconfig

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kubeconfig": kubeconfig,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kubeconfig = d.pop("kubeconfig")

        kubernetes_cluster_kubeconfig = cls(
            kubeconfig=kubeconfig,
        )

        kubernetes_cluster_kubeconfig.additional_properties = d
        return kubernetes_cluster_kubeconfig

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
