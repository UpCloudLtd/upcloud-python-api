from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.database_peering_status_response import DatabasePeeringStatusResponse


T = TypeVar("T", bound="DatabaseServiceNetworkDetailsResponse")


@_attrs_define
class DatabaseServiceNetworkDetailsResponse:
    """Schema for service network details response

    Attributes:
        create_time (datetime.datetime | None | Unset): The creation time of the service network.
        update_time (datetime.datetime | None | Unset): The last update time of the service network.
        state (str | Unset): The current state of the service network.
        network_peerings (list[DatabasePeeringStatusResponse] | Unset):
    """

    create_time: datetime.datetime | None | Unset = UNSET
    update_time: datetime.datetime | None | Unset = UNSET
    state: str | Unset = UNSET
    network_peerings: list[DatabasePeeringStatusResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time: None | str | Unset
        if isinstance(self.create_time, Unset):
            create_time = UNSET
        elif isinstance(self.create_time, datetime.datetime):
            create_time = self.create_time.isoformat()
        else:
            create_time = self.create_time

        update_time: None | str | Unset
        if isinstance(self.update_time, Unset):
            update_time = UNSET
        elif isinstance(self.update_time, datetime.datetime):
            update_time = self.update_time.isoformat()
        else:
            update_time = self.update_time

        state = self.state

        network_peerings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.network_peerings, Unset):
            network_peerings = []
            for network_peerings_item_data in self.network_peerings:
                network_peerings_item = network_peerings_item_data.to_dict()
                network_peerings.append(network_peerings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if state is not UNSET:
            field_dict["state"] = state
        if network_peerings is not UNSET:
            field_dict["network_peerings"] = network_peerings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_peering_status_response import DatabasePeeringStatusResponse  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_create_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                create_time_type_0 = datetime.datetime.fromisoformat(data)

                return create_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        create_time = _parse_create_time(d.pop("create_time", UNSET))

        def _parse_update_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_time_type_0 = datetime.datetime.fromisoformat(data)

                return update_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        update_time = _parse_update_time(d.pop("update_time", UNSET))

        state = d.pop("state", UNSET)

        _network_peerings = d.pop("network_peerings", UNSET)
        network_peerings: list[DatabasePeeringStatusResponse] | Unset = UNSET
        if _network_peerings is not UNSET:
            network_peerings = []
            for network_peerings_item_data in _network_peerings:
                network_peerings_item = DatabasePeeringStatusResponse.from_dict(network_peerings_item_data)

                network_peerings.append(network_peerings_item)

        database_service_network_details_response = cls(
            create_time=create_time,
            update_time=update_time,
            state=state,
            network_peerings=network_peerings,
        )

        database_service_network_details_response.additional_properties = d
        return database_service_network_details_response

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
