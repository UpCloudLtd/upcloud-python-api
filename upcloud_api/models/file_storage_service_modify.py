from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.file_storage_configured_status import FileStorageConfiguredStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_storage_label_create import FileStorageLabelCreate
    from ..models.file_storage_network_create import FileStorageNetworkCreate


T = TypeVar("T", bound="FileStorageServiceModify")


@_attrs_define
class FileStorageServiceModify:
    """Schema for modifying an existing service.

    Attributes:
        name (str | Unset): A resource name.
        configured_status (FileStorageConfiguredStatus | Unset): The service configured status indicates the service's
            current intended status. Managed by the customer.
        size_gib (int | Unset): The size of the service in gibibytes (GiB)
        networks (list[FileStorageNetworkCreate] | None | Unset):
        labels (list[FileStorageLabelCreate] | None | Unset):
    """

    name: str | Unset = UNSET
    configured_status: FileStorageConfiguredStatus | Unset = UNSET
    size_gib: int | Unset = UNSET
    networks: list[FileStorageNetworkCreate] | None | Unset = UNSET
    labels: list[FileStorageLabelCreate] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        configured_status: str | Unset = UNSET
        if not isinstance(self.configured_status, Unset):
            configured_status = self.configured_status.value

        size_gib = self.size_gib

        networks: list[dict[str, Any]] | None | Unset
        if isinstance(self.networks, Unset):
            networks = UNSET
        elif isinstance(self.networks, list):
            networks = []
            for networks_type_0_item_data in self.networks:
                networks_type_0_item = networks_type_0_item_data.to_dict()
                networks.append(networks_type_0_item)

        else:
            networks = self.networks

        labels: list[dict[str, Any]] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, list):
            labels = []
            for labels_type_0_item_data in self.labels:
                labels_type_0_item = labels_type_0_item_data.to_dict()
                labels.append(labels_type_0_item)

        else:
            labels = self.labels

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if configured_status is not UNSET:
            field_dict["configured_status"] = configured_status
        if size_gib is not UNSET:
            field_dict["size_gib"] = size_gib
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
        name = d.pop("name", UNSET)

        _configured_status = d.pop("configured_status", UNSET)
        configured_status: FileStorageConfiguredStatus | Unset
        if isinstance(_configured_status, Unset):
            configured_status = UNSET
        else:
            configured_status = FileStorageConfiguredStatus(_configured_status)

        size_gib = d.pop("size_gib", UNSET)

        def _parse_networks(data: object) -> list[FileStorageNetworkCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                networks_type_0 = []
                _networks_type_0 = data
                for networks_type_0_item_data in _networks_type_0:
                    networks_type_0_item = FileStorageNetworkCreate.from_dict(networks_type_0_item_data)

                    networks_type_0.append(networks_type_0_item)

                return networks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FileStorageNetworkCreate] | None | Unset, data)

        networks = _parse_networks(d.pop("networks", UNSET))

        def _parse_labels(data: object) -> list[FileStorageLabelCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                labels_type_0 = []
                _labels_type_0 = data
                for labels_type_0_item_data in _labels_type_0:
                    labels_type_0_item = FileStorageLabelCreate.from_dict(labels_type_0_item_data)

                    labels_type_0.append(labels_type_0_item)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FileStorageLabelCreate] | None | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        file_storage_service_modify = cls(
            name=name,
            configured_status=configured_status,
            size_gib=size_gib,
            networks=networks,
            labels=labels,
        )

        return file_storage_service_modify
