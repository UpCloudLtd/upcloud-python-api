from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.kubernetes_node_group_state import KubernetesNodeGroupState
from ..models.kubernetes_storage_encryption import KubernetesStorageEncryption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kubernetes_kubelet_arg import KubernetesKubeletArg
    from ..models.kubernetes_label import KubernetesLabel
    from ..models.kubernetes_node_group_cloud_native_plan import KubernetesNodeGroupCloudNativePlan
    from ..models.kubernetes_node_group_custom_plan import KubernetesNodeGroupCustomPlan
    from ..models.kubernetes_node_group_gpu_plan import KubernetesNodeGroupGPUPlan
    from ..models.kubernetes_node_updates import KubernetesNodeUpdates
    from ..models.kubernetes_taint import KubernetesTaint


T = TypeVar("T", bound="KubernetesNodeGroup")


@_attrs_define
class KubernetesNodeGroup:
    """Node group for a Kubernetes cluster

    Attributes:
        count (int): Amount of nodes in a node group
        name (str): Name
        plan (str): Node group plan
        kubelet_args (list[KubernetesKubeletArg] | Unset): List of Kubelet arguments
        labels (list[KubernetesLabel] | Unset): List of labels
        custom_plan (KubernetesNodeGroupCustomPlan | Unset): Node group custom plan properties
        cloud_native_plan (KubernetesNodeGroupCloudNativePlan | Unset): Node group cloud native plan properties
        gpu_plan (KubernetesNodeGroupGPUPlan | Unset): Node group GPU plan properties
        ssh_keys (list[str] | Unset): List of public SSH keys
        state (KubernetesNodeGroupState | Unset): Node group operational state
        storage (UUID | Unset): Storage UUID to use as a template
        storage_encryption (KubernetesStorageEncryption | Unset): The storage encryption strategy.
        taints (list[KubernetesTaint] | Unset): List of taints
        anti_affinity (bool | Unset): Enable anti-affinity policies
        utility_network_access (bool | Unset): Enable utility network access
        node_updates (KubernetesNodeUpdates | Unset): Enable periodic package updates on node
    """

    count: int
    name: str
    plan: str
    kubelet_args: list[KubernetesKubeletArg] | Unset = UNSET
    labels: list[KubernetesLabel] | Unset = UNSET
    custom_plan: KubernetesNodeGroupCustomPlan | Unset = UNSET
    cloud_native_plan: KubernetesNodeGroupCloudNativePlan | Unset = UNSET
    gpu_plan: KubernetesNodeGroupGPUPlan | Unset = UNSET
    ssh_keys: list[str] | Unset = UNSET
    state: KubernetesNodeGroupState | Unset = UNSET
    storage: UUID | Unset = UNSET
    storage_encryption: KubernetesStorageEncryption | Unset = UNSET
    taints: list[KubernetesTaint] | Unset = UNSET
    anti_affinity: bool | Unset = UNSET
    utility_network_access: bool | Unset = UNSET
    node_updates: KubernetesNodeUpdates | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        name = self.name

        plan = self.plan

        kubelet_args: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.kubelet_args, Unset):
            kubelet_args = []
            for componentsschemaskubernetes_kubelet_args_item_data in self.kubelet_args:
                componentsschemaskubernetes_kubelet_args_item = (
                    componentsschemaskubernetes_kubelet_args_item_data.to_dict()
                )
                kubelet_args.append(componentsschemaskubernetes_kubelet_args_item)

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for componentsschemaskubernetes_labels_item_data in self.labels:
                componentsschemaskubernetes_labels_item = componentsschemaskubernetes_labels_item_data.to_dict()
                labels.append(componentsschemaskubernetes_labels_item)

        custom_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_plan, Unset):
            custom_plan = self.custom_plan.to_dict()

        cloud_native_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloud_native_plan, Unset):
            cloud_native_plan = self.cloud_native_plan.to_dict()

        gpu_plan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpu_plan, Unset):
            gpu_plan = self.gpu_plan.to_dict()

        ssh_keys: list[str] | Unset = UNSET
        if not isinstance(self.ssh_keys, Unset):
            ssh_keys = self.ssh_keys

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        storage: str | Unset = UNSET
        if not isinstance(self.storage, Unset):
            storage = str(self.storage)

        storage_encryption: str | Unset = UNSET
        if not isinstance(self.storage_encryption, Unset):
            storage_encryption = self.storage_encryption.value

        taints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.taints, Unset):
            taints = []
            for componentsschemaskubernetes_taints_item_data in self.taints:
                componentsschemaskubernetes_taints_item = componentsschemaskubernetes_taints_item_data.to_dict()
                taints.append(componentsschemaskubernetes_taints_item)

        anti_affinity = self.anti_affinity

        utility_network_access = self.utility_network_access

        node_updates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node_updates, Unset):
            node_updates = self.node_updates.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "name": name,
                "plan": plan,
            }
        )
        if kubelet_args is not UNSET:
            field_dict["kubelet_args"] = kubelet_args
        if labels is not UNSET:
            field_dict["labels"] = labels
        if custom_plan is not UNSET:
            field_dict["custom_plan"] = custom_plan
        if cloud_native_plan is not UNSET:
            field_dict["cloud_native_plan"] = cloud_native_plan
        if gpu_plan is not UNSET:
            field_dict["gpu_plan"] = gpu_plan
        if ssh_keys is not UNSET:
            field_dict["ssh_keys"] = ssh_keys
        if state is not UNSET:
            field_dict["state"] = state
        if storage is not UNSET:
            field_dict["storage"] = storage
        if storage_encryption is not UNSET:
            field_dict["storage_encryption"] = storage_encryption
        if taints is not UNSET:
            field_dict["taints"] = taints
        if anti_affinity is not UNSET:
            field_dict["anti_affinity"] = anti_affinity
        if utility_network_access is not UNSET:
            field_dict["utility_network_access"] = utility_network_access
        if node_updates is not UNSET:
            field_dict["node_updates"] = node_updates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.kubernetes_kubelet_arg import KubernetesKubeletArg  # noqa: PLC0415
        from ..models.kubernetes_label import KubernetesLabel  # noqa: PLC0415
        from ..models.kubernetes_node_group_cloud_native_plan import KubernetesNodeGroupCloudNativePlan  # noqa: PLC0415
        from ..models.kubernetes_node_group_custom_plan import KubernetesNodeGroupCustomPlan  # noqa: PLC0415
        from ..models.kubernetes_node_group_gpu_plan import KubernetesNodeGroupGPUPlan  # noqa: PLC0415
        from ..models.kubernetes_node_updates import KubernetesNodeUpdates  # noqa: PLC0415
        from ..models.kubernetes_taint import KubernetesTaint  # noqa: PLC0415

        d = dict(src_dict)
        count = d.pop("count")

        name = d.pop("name")

        plan = d.pop("plan")

        _kubelet_args = d.pop("kubelet_args", UNSET)
        kubelet_args: list[KubernetesKubeletArg] | Unset = UNSET
        if _kubelet_args is not UNSET:
            kubelet_args = []
            for componentsschemaskubernetes_kubelet_args_item_data in _kubelet_args:
                componentsschemaskubernetes_kubelet_args_item = KubernetesKubeletArg.from_dict(
                    componentsschemaskubernetes_kubelet_args_item_data
                )

                kubelet_args.append(componentsschemaskubernetes_kubelet_args_item)

        _labels = d.pop("labels", UNSET)
        labels: list[KubernetesLabel] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for componentsschemaskubernetes_labels_item_data in _labels:
                componentsschemaskubernetes_labels_item = KubernetesLabel.from_dict(
                    componentsschemaskubernetes_labels_item_data
                )

                labels.append(componentsschemaskubernetes_labels_item)

        _custom_plan = d.pop("custom_plan", UNSET)
        custom_plan: KubernetesNodeGroupCustomPlan | Unset
        if isinstance(_custom_plan, Unset):
            custom_plan = UNSET
        else:
            custom_plan = KubernetesNodeGroupCustomPlan.from_dict(_custom_plan)

        _cloud_native_plan = d.pop("cloud_native_plan", UNSET)
        cloud_native_plan: KubernetesNodeGroupCloudNativePlan | Unset
        if isinstance(_cloud_native_plan, Unset):
            cloud_native_plan = UNSET
        else:
            cloud_native_plan = KubernetesNodeGroupCloudNativePlan.from_dict(_cloud_native_plan)

        _gpu_plan = d.pop("gpu_plan", UNSET)
        gpu_plan: KubernetesNodeGroupGPUPlan | Unset
        if isinstance(_gpu_plan, Unset):
            gpu_plan = UNSET
        else:
            gpu_plan = KubernetesNodeGroupGPUPlan.from_dict(_gpu_plan)

        ssh_keys = cast(list[str], d.pop("ssh_keys", UNSET))

        _state = d.pop("state", UNSET)
        state: KubernetesNodeGroupState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = KubernetesNodeGroupState(_state)

        _storage = d.pop("storage", UNSET)
        storage: UUID | Unset
        if isinstance(_storage, Unset):
            storage = UNSET
        else:
            storage = UUID(_storage)

        _storage_encryption = d.pop("storage_encryption", UNSET)
        storage_encryption: KubernetesStorageEncryption | Unset
        if isinstance(_storage_encryption, Unset):
            storage_encryption = UNSET
        else:
            storage_encryption = KubernetesStorageEncryption(_storage_encryption)

        _taints = d.pop("taints", UNSET)
        taints: list[KubernetesTaint] | Unset = UNSET
        if _taints is not UNSET:
            taints = []
            for componentsschemaskubernetes_taints_item_data in _taints:
                componentsschemaskubernetes_taints_item = KubernetesTaint.from_dict(
                    componentsschemaskubernetes_taints_item_data
                )

                taints.append(componentsschemaskubernetes_taints_item)

        anti_affinity = d.pop("anti_affinity", UNSET)

        utility_network_access = d.pop("utility_network_access", UNSET)

        _node_updates = d.pop("node_updates", UNSET)
        node_updates: KubernetesNodeUpdates | Unset
        if isinstance(_node_updates, Unset):
            node_updates = UNSET
        else:
            node_updates = KubernetesNodeUpdates.from_dict(_node_updates)

        kubernetes_node_group = cls(
            count=count,
            name=name,
            plan=plan,
            kubelet_args=kubelet_args,
            labels=labels,
            custom_plan=custom_plan,
            cloud_native_plan=cloud_native_plan,
            gpu_plan=gpu_plan,
            ssh_keys=ssh_keys,
            state=state,
            storage=storage,
            storage_encryption=storage_encryption,
            taints=taints,
            anti_affinity=anti_affinity,
            utility_network_access=utility_network_access,
            node_updates=node_updates,
        )

        kubernetes_node_group.additional_properties = d
        return kubernetes_node_group

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
