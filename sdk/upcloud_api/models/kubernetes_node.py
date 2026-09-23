from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kubernetes_node_state import KubernetesNodeState

T = TypeVar("T", bound="KubernetesNode")


@_attrs_define
class KubernetesNode:
    """Kubernetes cluster node

    Attributes:
        uuid (UUID): Node UUID
        name (str): Name
        kubelet_version (str): Kubernetes version identifier
        state (KubernetesNodeState): Node operational state
    """

    uuid: UUID
    name: str
    kubelet_version: str
    state: KubernetesNodeState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        kubelet_version = self.kubelet_version

        state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "kubelet_version": kubelet_version,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        kubelet_version = d.pop("kubelet_version")

        state = KubernetesNodeState(d.pop("state"))

        kubernetes_node = cls(
            uuid=uuid,
            name=name,
            kubelet_version=kubelet_version,
            state=state,
        )

        kubernetes_node.additional_properties = d
        return kubernetes_node

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
