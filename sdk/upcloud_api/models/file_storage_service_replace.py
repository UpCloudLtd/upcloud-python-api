from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.file_storage_configured_status import FileStorageConfiguredStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_storage_label_create import FileStorageLabelCreate
    from ..models.file_storage_network_create import FileStorageNetworkCreate


T = TypeVar("T", bound="FileStorageServiceReplace")


@_attrs_define
class FileStorageServiceReplace:
    """Schema for replacing an existing service with a new configuration.

    Attributes:
        name (str): A resource name.
        configured_status (FileStorageConfiguredStatus): The service configured status indicates the service's current
            intended status. Managed by the customer.
        size_gib (int): The size of the service in gibibytes (GiB)
        networks (list[FileStorageNetworkCreate] | Unset):
        labels (list[FileStorageLabelCreate] | Unset): Labels
    """

    name: str
    configured_status: FileStorageConfiguredStatus
    size_gib: int
    networks: list[FileStorageNetworkCreate] | Unset = UNSET
    labels: list[FileStorageLabelCreate] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        configured_status = self.configured_status.value

        size_gib = self.size_gib

        networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()
                networks.append(networks_item)

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "configured_status": configured_status,
                "size_gib": size_gib,
            }
        )
        if networks is not UNSET:
            field_dict["networks"] = networks
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_storage_label_create import FileStorageLabelCreate  # noqa: PLC0415
        from ..models.file_storage_network_create import FileStorageNetworkCreate  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        configured_status = FileStorageConfiguredStatus(d.pop("configured_status"))

        size_gib = d.pop("size_gib")

        _networks = d.pop("networks", UNSET)
        networks: list[FileStorageNetworkCreate] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = FileStorageNetworkCreate.from_dict(networks_item_data)

                networks.append(networks_item)

        _labels = d.pop("labels", UNSET)
        labels: list[FileStorageLabelCreate] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = FileStorageLabelCreate.from_dict(labels_item_data)

                labels.append(labels_item)

        file_storage_service_replace = cls(
            name=name,
            configured_status=configured_status,
            size_gib=size_gib,
            networks=networks,
            labels=labels,
        )

        return file_storage_service_replace
