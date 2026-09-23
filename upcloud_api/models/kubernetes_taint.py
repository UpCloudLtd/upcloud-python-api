from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kubernetes_effect import KubernetesEffect

T = TypeVar("T", bound="KubernetesTaint")


@_attrs_define
class KubernetesTaint:
    """Kubernetes taint to assign to nodes in a group

    Attributes:
        effect (KubernetesEffect): Taint effect
        key (str): Key of a key-value pair
        value (str): Value of a key-value pair
    """

    effect: KubernetesEffect
    key: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effect = self.effect.value

        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "effect": effect,
                "key": key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        effect = KubernetesEffect(d.pop("effect"))

        key = d.pop("key")

        value = d.pop("value")

        kubernetes_taint = cls(
            effect=effect,
            key=key,
            value=value,
        )

        kubernetes_taint.additional_properties = d
        return kubernetes_taint

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
