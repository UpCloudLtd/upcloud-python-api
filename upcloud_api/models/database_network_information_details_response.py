from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_network_information_details_response_family import (
    DatabaseNetworkInformationDetailsResponseFamily,
)
from ..models.database_network_information_details_response_type import DatabaseNetworkInformationDetailsResponseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseNetworkInformationDetailsResponse")


@_attrs_define
class DatabaseNetworkInformationDetailsResponse:
    """Schema for network information response details

    Attributes:
        uuid (UUID | Unset): Unique identifier for the network Example: 123e4567-e89b-12d3-a456-426614174000.
        name (str | Unset): Name of the network Example: example-private-network.
        family (DatabaseNetworkInformationDetailsResponseFamily | Unset): Address family (e.g., IPv4, IPv6)
        type_ (DatabaseNetworkInformationDetailsResponseType | Unset): Type of network (e.g., private, public)
        create_time (datetime.datetime | Unset): Timestamp when the network was created Example:
            2025-08-01T10:40:04.140473Z.
        update_time (datetime.datetime | Unset): Timestamp when the network was last updated Example:
            2025-08-01T10:40:04.140473Z.
    """

    uuid: UUID | Unset = UNSET
    name: str | Unset = UNSET
    family: DatabaseNetworkInformationDetailsResponseFamily | Unset = UNSET
    type_: DatabaseNetworkInformationDetailsResponseType | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        name = self.name

        family: str | Unset = UNSET
        if not isinstance(self.family, Unset):
            family = self.family.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        update_time: str | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if name is not UNSET:
            field_dict["name"] = name
        if family is not UNSET:
            field_dict["family"] = family
        if type_ is not UNSET:
            field_dict["type"] = type_
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        name = d.pop("name", UNSET)

        _family = d.pop("family", UNSET)
        family: DatabaseNetworkInformationDetailsResponseFamily | Unset
        if isinstance(_family, Unset):
            family = UNSET
        else:
            family = DatabaseNetworkInformationDetailsResponseFamily(_family)

        _type_ = d.pop("type", UNSET)
        type_: DatabaseNetworkInformationDetailsResponseType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DatabaseNetworkInformationDetailsResponseType(_type_)

        _create_time = d.pop("create_time", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        _update_time = d.pop("update_time", UNSET)
        update_time: datetime.datetime | Unset
        if isinstance(_update_time, Unset):
            update_time = UNSET
        else:
            update_time = datetime.datetime.fromisoformat(_update_time)

        database_network_information_details_response = cls(
            uuid=uuid,
            name=name,
            family=family,
            type_=type_,
            create_time=create_time,
            update_time=update_time,
        )

        database_network_information_details_response.additional_properties = d
        return database_network_information_details_response

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
