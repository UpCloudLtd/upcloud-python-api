from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.network_peering_modify_configured_status import NetworkPeeringModifyConfiguredStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkPeeringModify")


@_attrs_define
class NetworkPeeringModify:
    """Describes the mutable properties when modifying a network-peering

    Example:
        {'configured_status': 'disabled', 'name': 'Peering A->B modified'}

    Attributes:
        configured_status (NetworkPeeringModifyConfiguredStatus | Unset):
        name (str | Unset):
    """

    configured_status: NetworkPeeringModifyConfiguredStatus | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        configured_status: str | Unset = UNSET
        if not isinstance(self.configured_status, Unset):
            configured_status = self.configured_status.value

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if configured_status is not UNSET:
            field_dict["configured_status"] = configured_status
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _configured_status = d.pop("configured_status", UNSET)
        configured_status: NetworkPeeringModifyConfiguredStatus | Unset
        if isinstance(_configured_status, Unset):
            configured_status = UNSET
        else:
            configured_status = NetworkPeeringModifyConfiguredStatus(_configured_status)

        name = d.pop("name", UNSET)

        network_peering_modify = cls(
            configured_status=configured_status,
            name=name,
        )

        return network_peering_modify
