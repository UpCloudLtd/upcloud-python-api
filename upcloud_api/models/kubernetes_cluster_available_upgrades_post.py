from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kubernetes_cluster_upgrade_strategy import KubernetesClusterUpgradeStrategy


T = TypeVar("T", bound="KubernetesClusterAvailableUpgradesPost")


@_attrs_define
class KubernetesClusterAvailableUpgradesPost:
    """
    Attributes:
        version (str): Kubernetes version identifier
        strategy (KubernetesClusterUpgradeStrategy | Unset): upgrade strategy for node group upgrades
    """

    version: str
    strategy: KubernetesClusterUpgradeStrategy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        strategy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.strategy, Unset):
            strategy = self.strategy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
            }
        )
        if strategy is not UNSET:
            field_dict["strategy"] = strategy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kubernetes_cluster_upgrade_strategy import KubernetesClusterUpgradeStrategy  # noqa: PLC0415

        d = dict(src_dict)
        version = d.pop("version")

        _strategy = d.pop("strategy", UNSET)
        strategy: KubernetesClusterUpgradeStrategy | Unset
        if isinstance(_strategy, Unset):
            strategy = UNSET
        else:
            strategy = KubernetesClusterUpgradeStrategy.from_dict(_strategy)

        kubernetes_cluster_available_upgrades_post = cls(
            version=version,
            strategy=strategy,
        )

        kubernetes_cluster_available_upgrades_post.additional_properties = d
        return kubernetes_cluster_available_upgrades_post

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
