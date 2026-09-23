from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.file_storage_configured_status import FileStorageConfiguredStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_storage_label_create import FileStorageLabelCreate
    from ..models.file_storage_network_create import FileStorageNetworkCreate
    from ..models.file_storage_share_create import FileStorageShareCreate


T = TypeVar("T", bound="FileStorageServiceCreate")


@_attrs_define
class FileStorageServiceCreate:
    """Schema for creating a new service.

    Attributes:
        name (str): A resource name.
        zone (str): Indicates the zone where the service will be created.
        configured_status (FileStorageConfiguredStatus): The service configured status indicates the service's current
            intended status. Managed by the customer.
        size_gib (int): The size of the service in gibibytes (GiB)
        encrypted (bool | Unset): Indicates whether encryption at rest is enabled for the service. Default: False.
        networks (list[FileStorageNetworkCreate] | Unset):
        shares (list[FileStorageShareCreate] | Unset):
        labels (list[FileStorageLabelCreate] | Unset): Labels
    """

    name: str
    zone: str
    configured_status: FileStorageConfiguredStatus
    size_gib: int
    encrypted: bool | Unset = False
    networks: list[FileStorageNetworkCreate] | Unset = UNSET
    shares: list[FileStorageShareCreate] | Unset = UNSET
    labels: list[FileStorageLabelCreate] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        zone = self.zone

        configured_status = self.configured_status.value

        size_gib = self.size_gib

        encrypted = self.encrypted

        networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()
                networks.append(networks_item)

        shares: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shares, Unset):
            shares = []
            for shares_item_data in self.shares:
                shares_item = shares_item_data.to_dict()
                shares.append(shares_item)

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
                "zone": zone,
                "configured_status": configured_status,
                "size_gib": size_gib,
            }
        )
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if networks is not UNSET:
            field_dict["networks"] = networks
        if shares is not UNSET:
            field_dict["shares"] = shares
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_storage_label_create import FileStorageLabelCreate  # noqa: PLC0415
        from ..models.file_storage_network_create import FileStorageNetworkCreate  # noqa: PLC0415
        from ..models.file_storage_share_create import FileStorageShareCreate  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        zone = d.pop("zone")

        configured_status = FileStorageConfiguredStatus(d.pop("configured_status"))

        size_gib = d.pop("size_gib")

        encrypted = d.pop("encrypted", UNSET)

        _networks = d.pop("networks", UNSET)
        networks: list[FileStorageNetworkCreate] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = FileStorageNetworkCreate.from_dict(networks_item_data)

                networks.append(networks_item)

        _shares = d.pop("shares", UNSET)
        shares: list[FileStorageShareCreate] | Unset = UNSET
        if _shares is not UNSET:
            shares = []
            for shares_item_data in _shares:
                shares_item = FileStorageShareCreate.from_dict(shares_item_data)

                shares.append(shares_item)

        _labels = d.pop("labels", UNSET)
        labels: list[FileStorageLabelCreate] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = FileStorageLabelCreate.from_dict(labels_item_data)

                labels.append(labels_item)

        file_storage_service_create = cls(
            name=name,
            zone=zone,
            configured_status=configured_status,
            size_gib=size_gib,
            encrypted=encrypted,
            networks=networks,
            shares=shares,
            labels=labels,
        )

        return file_storage_service_create
