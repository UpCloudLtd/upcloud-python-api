from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kubernetes_cluster_plan import KubernetesClusterPlan
from ..models.kubernetes_cluster_state import KubernetesClusterState
from ..models.kubernetes_default_storage_encryption import KubernetesDefaultStorageEncryption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kubernetes_authentication_issuer_config import KubernetesAuthenticationIssuerConfig
    from ..models.kubernetes_node_group import KubernetesNodeGroup


T = TypeVar("T", bound="KubernetesCluster")


@_attrs_define
class KubernetesCluster:
    """Kubernetes cluster

    Attributes:
        name (str): Name
        network (str): Network UUID
        zone (str): UpCloud zone to provision the Kubernetes cluster in
        version (str): Kubernetes version identifier
        labels (Any):
        control_plane_ip_filter (list[str] | Unset): List of IP blocks
        network_cidr (str | Unset): CIDR of the given network
        storage_encryption (KubernetesDefaultStorageEncryption | Unset): The storage encryption strategy.
        node_groups (list[KubernetesNodeGroup] | Unset): List of node groups
        state (KubernetesClusterState | Unset): Cluster operational state
        uuid (UUID | Unset): UUID
        plan (KubernetesClusterPlan | Unset): Cluster plan
        private_node_groups (bool | Unset): Enable private node groups
        authentication (list[KubernetesAuthenticationIssuerConfig] | Unset): List of OIDC issuers and their claim
            validation rules.
    """

    name: str
    network: str
    zone: str
    version: str
    labels: Any
    control_plane_ip_filter: list[str] | Unset = UNSET
    network_cidr: str | Unset = UNSET
    storage_encryption: KubernetesDefaultStorageEncryption | Unset = UNSET
    node_groups: list[KubernetesNodeGroup] | Unset = UNSET
    state: KubernetesClusterState | Unset = UNSET
    uuid: UUID | Unset = UNSET
    plan: KubernetesClusterPlan | Unset = UNSET
    private_node_groups: bool | Unset = UNSET
    authentication: list[KubernetesAuthenticationIssuerConfig] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        network = self.network

        zone = self.zone

        version = self.version

        labels = self.labels

        control_plane_ip_filter: list[str] | Unset = UNSET
        if not isinstance(self.control_plane_ip_filter, Unset):
            control_plane_ip_filter = self.control_plane_ip_filter

        network_cidr = self.network_cidr

        storage_encryption: str | Unset = UNSET
        if not isinstance(self.storage_encryption, Unset):
            storage_encryption = self.storage_encryption.value

        node_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.node_groups, Unset):
            node_groups = []
            for componentsschemaskubernetes_node_groups_item_data in self.node_groups:
                componentsschemaskubernetes_node_groups_item = (
                    componentsschemaskubernetes_node_groups_item_data.to_dict()
                )
                node_groups.append(componentsschemaskubernetes_node_groups_item)

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        plan: str | Unset = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.value

        private_node_groups = self.private_node_groups

        authentication: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = []
            for componentsschemaskubernetes_authentication_configuration_item_data in self.authentication:
                componentsschemaskubernetes_authentication_configuration_item = (
                    componentsschemaskubernetes_authentication_configuration_item_data.to_dict()
                )
                authentication.append(componentsschemaskubernetes_authentication_configuration_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "network": network,
                "zone": zone,
                "version": version,
                "labels": labels,
            }
        )
        if control_plane_ip_filter is not UNSET:
            field_dict["control_plane_ip_filter"] = control_plane_ip_filter
        if network_cidr is not UNSET:
            field_dict["network_cidr"] = network_cidr
        if storage_encryption is not UNSET:
            field_dict["storage_encryption"] = storage_encryption
        if node_groups is not UNSET:
            field_dict["node_groups"] = node_groups
        if state is not UNSET:
            field_dict["state"] = state
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if plan is not UNSET:
            field_dict["plan"] = plan
        if private_node_groups is not UNSET:
            field_dict["private_node_groups"] = private_node_groups
        if authentication is not UNSET:
            field_dict["authentication"] = authentication

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kubernetes_authentication_issuer_config import (
            KubernetesAuthenticationIssuerConfig,  # noqa: PLC0415
        )
        from ..models.kubernetes_node_group import KubernetesNodeGroup  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        network = d.pop("network")

        zone = d.pop("zone")

        version = d.pop("version")

        labels = d.pop("labels")

        control_plane_ip_filter = cast(list[str], d.pop("control_plane_ip_filter", UNSET))

        network_cidr = d.pop("network_cidr", UNSET)

        _storage_encryption = d.pop("storage_encryption", UNSET)
        storage_encryption: KubernetesDefaultStorageEncryption | Unset
        if isinstance(_storage_encryption, Unset):
            storage_encryption = UNSET
        else:
            storage_encryption = KubernetesDefaultStorageEncryption(_storage_encryption)

        _node_groups = d.pop("node_groups", UNSET)
        node_groups: list[KubernetesNodeGroup] | Unset = UNSET
        if _node_groups is not UNSET:
            node_groups = []
            for componentsschemaskubernetes_node_groups_item_data in _node_groups:
                componentsschemaskubernetes_node_groups_item = KubernetesNodeGroup.from_dict(
                    componentsschemaskubernetes_node_groups_item_data
                )

                node_groups.append(componentsschemaskubernetes_node_groups_item)

        _state = d.pop("state", UNSET)
        state: KubernetesClusterState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = KubernetesClusterState(_state)

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        _plan = d.pop("plan", UNSET)
        plan: KubernetesClusterPlan | Unset
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = KubernetesClusterPlan(_plan)

        private_node_groups = d.pop("private_node_groups", UNSET)

        _authentication = d.pop("authentication", UNSET)
        authentication: list[KubernetesAuthenticationIssuerConfig] | Unset = UNSET
        if _authentication is not UNSET:
            authentication = []
            for componentsschemaskubernetes_authentication_configuration_item_data in _authentication:
                componentsschemaskubernetes_authentication_configuration_item = (
                    KubernetesAuthenticationIssuerConfig.from_dict(
                        componentsschemaskubernetes_authentication_configuration_item_data
                    )
                )

                authentication.append(componentsschemaskubernetes_authentication_configuration_item)

        kubernetes_cluster = cls(
            name=name,
            network=network,
            zone=zone,
            version=version,
            labels=labels,
            control_plane_ip_filter=control_plane_ip_filter,
            network_cidr=network_cidr,
            storage_encryption=storage_encryption,
            node_groups=node_groups,
            state=state,
            uuid=uuid,
            plan=plan,
            private_node_groups=private_node_groups,
            authentication=authentication,
        )

        kubernetes_cluster.additional_properties = d
        return kubernetes_cluster

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
