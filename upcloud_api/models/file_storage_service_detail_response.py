from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_storage_label_details import FileStorageLabelDetails
    from ..models.file_storage_network_detail_response import FileStorageNetworkDetailResponse
    from ..models.file_storage_service_detail_response_state_messages_item import (
        FileStorageServiceDetailResponseStateMessagesItem,
    )
    from ..models.file_storage_share_detail_response import FileStorageShareDetailResponse


T = TypeVar("T", bound="FileStorageServiceDetailResponse")


@_attrs_define
class FileStorageServiceDetailResponse:
    """Schema for the detailed response of a service.

    Attributes:
        uuid (str | Unset):
        name (str | Unset):
        zone (str | Unset):
        configured_status (str | Unset):
        operational_state (str | Unset):
        size_gib (int | Unset):
        encrypted (bool | Unset):
        networks (list[FileStorageNetworkDetailResponse] | Unset):
        shares (list[FileStorageShareDetailResponse] | Unset):
        labels (list[FileStorageLabelDetails] | Unset):
        state_messages (list[FileStorageServiceDetailResponseStateMessagesItem] | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    uuid: str | Unset = UNSET
    name: str | Unset = UNSET
    zone: str | Unset = UNSET
    configured_status: str | Unset = UNSET
    operational_state: str | Unset = UNSET
    size_gib: int | Unset = UNSET
    encrypted: bool | Unset = UNSET
    networks: list[FileStorageNetworkDetailResponse] | Unset = UNSET
    shares: list[FileStorageShareDetailResponse] | Unset = UNSET
    labels: list[FileStorageLabelDetails] | Unset = UNSET
    state_messages: list[FileStorageServiceDetailResponseStateMessagesItem] | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        name = self.name

        zone = self.zone

        configured_status = self.configured_status

        operational_state = self.operational_state

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

        state_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.state_messages, Unset):
            state_messages = []
            for state_messages_item_data in self.state_messages:
                state_messages_item = state_messages_item_data.to_dict()
                state_messages.append(state_messages_item)

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if zone is not UNSET:
            field_dict["zone"] = zone
        if configured_status is not UNSET:
            field_dict["configured_status"] = configured_status
        if operational_state is not UNSET:
            field_dict["operational_state"] = operational_state
        if size_gib is not UNSET:
            field_dict["size_gib"] = size_gib
        if encrypted is not UNSET:
            field_dict["encrypted"] = encrypted
        if networks is not UNSET:
            field_dict["networks"] = networks
        if shares is not UNSET:
            field_dict["shares"] = shares
        if labels is not UNSET:
            field_dict["labels"] = labels
        if state_messages is not UNSET:
            field_dict["state_messages"] = state_messages
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_storage_label_details import FileStorageLabelDetails  # noqa: PLC0415
        from ..models.file_storage_network_detail_response import FileStorageNetworkDetailResponse  # noqa: PLC0415
        from ..models.file_storage_service_detail_response_state_messages_item import (
            FileStorageServiceDetailResponseStateMessagesItem,  # noqa: PLC0415
        )
        from ..models.file_storage_share_detail_response import FileStorageShareDetailResponse  # noqa: PLC0415

        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        name = d.pop("name", UNSET)

        zone = d.pop("zone", UNSET)

        configured_status = d.pop("configured_status", UNSET)

        operational_state = d.pop("operational_state", UNSET)

        size_gib = d.pop("size_gib", UNSET)

        encrypted = d.pop("encrypted", UNSET)

        _networks = d.pop("networks", UNSET)
        networks: list[FileStorageNetworkDetailResponse] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = FileStorageNetworkDetailResponse.from_dict(networks_item_data)

                networks.append(networks_item)

        _shares = d.pop("shares", UNSET)
        shares: list[FileStorageShareDetailResponse] | Unset = UNSET
        if _shares is not UNSET:
            shares = []
            for shares_item_data in _shares:
                shares_item = FileStorageShareDetailResponse.from_dict(shares_item_data)

                shares.append(shares_item)

        _labels = d.pop("labels", UNSET)
        labels: list[FileStorageLabelDetails] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = FileStorageLabelDetails.from_dict(labels_item_data)

                labels.append(labels_item)

        _state_messages = d.pop("state_messages", UNSET)
        state_messages: list[FileStorageServiceDetailResponseStateMessagesItem] | Unset = UNSET
        if _state_messages is not UNSET:
            state_messages = []
            for state_messages_item_data in _state_messages:
                state_messages_item = FileStorageServiceDetailResponseStateMessagesItem.from_dict(
                    state_messages_item_data
                )

                state_messages.append(state_messages_item)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        file_storage_service_detail_response = cls(
            uuid=uuid,
            name=name,
            zone=zone,
            configured_status=configured_status,
            operational_state=operational_state,
            size_gib=size_gib,
            encrypted=encrypted,
            networks=networks,
            shares=shares,
            labels=labels,
            state_messages=state_messages,
            created_at=created_at,
            updated_at=updated_at,
        )

        file_storage_service_detail_response.additional_properties = d
        return file_storage_service_detail_response

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
