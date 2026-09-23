from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.database_network_family import DatabaseNetworkFamily
from ..models.database_network_type import DatabaseNetworkType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseNetworkCreate")


@_attrs_define
class DatabaseNetworkCreate:
    """Schema for creating a network.

    Attributes:
        name (str): The name of the network.
        type_ (DatabaseNetworkType): The type of network.
        family (DatabaseNetworkFamily): The network protocol family.
        uuid (UUID | Unset): Optional UUID for the network. If not provided, a new UUID will be generated.
    """

    name: str
    type_: DatabaseNetworkType
    family: DatabaseNetworkFamily
    uuid: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        family = self.family.value

        uuid: str | Unset = UNSET
        if not isinstance(self.uuid, Unset):
            uuid = str(self.uuid)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
                "family": family,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = DatabaseNetworkType(d.pop("type"))

        family = DatabaseNetworkFamily(d.pop("family"))

        _uuid = d.pop("uuid", UNSET)
        uuid: UUID | Unset
        if isinstance(_uuid, Unset):
            uuid = UNSET
        else:
            uuid = UUID(_uuid)

        database_network_create = cls(
            name=name,
            type_=type_,
            family=family,
            uuid=uuid,
        )

        return database_network_create
