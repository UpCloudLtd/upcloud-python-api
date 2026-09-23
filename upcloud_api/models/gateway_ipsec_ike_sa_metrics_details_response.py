from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gateway_ipsec_ike_sa_metrics_details_response_internal_state import (
    GatewayIpsecIkeSaMetricsDetailsResponseInternalState,
)
from ..models.gateway_ipsec_ike_sa_metrics_details_response_operational_state import (
    GatewayIpsecIkeSaMetricsDetailsResponseOperationalState,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_ipsec_ike_sa_metrics_details_response_child_sas_item import (
        GatewayIpsecIkeSaMetricsDetailsResponseChildSasItem,
    )
    from ..models.gateway_ipsec_ike_sa_metrics_details_response_heuristic_state import (
        GatewayIpsecIkeSaMetricsDetailsResponseHeuristicState,
    )


T = TypeVar("T", bound="GatewayIpsecIkeSaMetricsDetailsResponse")


@_attrs_define
class GatewayIpsecIkeSaMetricsDetailsResponse:
    """Response schema for IPsec IKE SA metrics details.

    Attributes:
        name (str | Unset): Name of the gateway
        tunnel_id (int | Unset): ID of the tunnel
        unique_id (str | Unset): Unique ID of the IKE SA
        version (int | Unset): Version of the IKE SA
        operational_state (GatewayIpsecIkeSaMetricsDetailsResponseOperationalState | Unset): Operational state of the
            IKE SA
        internal_state (GatewayIpsecIkeSaMetricsDetailsResponseInternalState | Unset): Internal state of the IKE SA
        initator (bool | Unset): Whether the local gateway is the initiator of the IKE SA
        established (int | Unset):
        rekey_time (int | Unset):
        reauth_time (int | Unset):
        child_sas (list[GatewayIpsecIkeSaMetricsDetailsResponseChildSasItem] | Unset):
        local_host (str | Unset): Local host IP address
        remote_host (str | Unset): Remote host IP address
        local_id (str | Unset): Local IKE identity
        remote_id (str | Unset): Remote IKE identity
        heuristic_state (GatewayIpsecIkeSaMetricsDetailsResponseHeuristicState | Unset): Heuristic state of the IKE SA
        created_at (datetime.datetime | Unset): Timestamp of when the IKE SA was created.
        updated_at (datetime.datetime | Unset): Timestamp of when the IKE SA was last updated.
    """

    name: str | Unset = UNSET
    tunnel_id: int | Unset = UNSET
    unique_id: str | Unset = UNSET
    version: int | Unset = UNSET
    operational_state: GatewayIpsecIkeSaMetricsDetailsResponseOperationalState | Unset = UNSET
    internal_state: GatewayIpsecIkeSaMetricsDetailsResponseInternalState | Unset = UNSET
    initator: bool | Unset = UNSET
    established: int | Unset = UNSET
    rekey_time: int | Unset = UNSET
    reauth_time: int | Unset = UNSET
    child_sas: list[GatewayIpsecIkeSaMetricsDetailsResponseChildSasItem] | Unset = UNSET
    local_host: str | Unset = UNSET
    remote_host: str | Unset = UNSET
    local_id: str | Unset = UNSET
    remote_id: str | Unset = UNSET
    heuristic_state: GatewayIpsecIkeSaMetricsDetailsResponseHeuristicState | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        tunnel_id = self.tunnel_id

        unique_id = self.unique_id

        version = self.version

        operational_state: str | Unset = UNSET
        if not isinstance(self.operational_state, Unset):
            operational_state = self.operational_state.value

        internal_state: str | Unset = UNSET
        if not isinstance(self.internal_state, Unset):
            internal_state = self.internal_state.value

        initator = self.initator

        established = self.established

        rekey_time = self.rekey_time

        reauth_time = self.reauth_time

        child_sas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.child_sas, Unset):
            child_sas = []
            for child_sas_item_data in self.child_sas:
                child_sas_item = child_sas_item_data.to_dict()
                child_sas.append(child_sas_item)

        local_host = self.local_host

        remote_host = self.remote_host

        local_id = self.local_id

        remote_id = self.remote_id

        heuristic_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.heuristic_state, Unset):
            heuristic_state = self.heuristic_state.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if tunnel_id is not UNSET:
            field_dict["tunnel_id"] = tunnel_id
        if unique_id is not UNSET:
            field_dict["unique_id"] = unique_id
        if version is not UNSET:
            field_dict["version"] = version
        if operational_state is not UNSET:
            field_dict["operational_state"] = operational_state
        if internal_state is not UNSET:
            field_dict["internal_state"] = internal_state
        if initator is not UNSET:
            field_dict["initator"] = initator
        if established is not UNSET:
            field_dict["established"] = established
        if rekey_time is not UNSET:
            field_dict["rekey_time"] = rekey_time
        if reauth_time is not UNSET:
            field_dict["reauth_time"] = reauth_time
        if child_sas is not UNSET:
            field_dict["child_sas"] = child_sas
        if local_host is not UNSET:
            field_dict["local_host"] = local_host
        if remote_host is not UNSET:
            field_dict["remote_host"] = remote_host
        if local_id is not UNSET:
            field_dict["local_id"] = local_id
        if remote_id is not UNSET:
            field_dict["remote_id"] = remote_id
        if heuristic_state is not UNSET:
            field_dict["heuristic_state"] = heuristic_state
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_ipsec_ike_sa_metrics_details_response_child_sas_item import (
            GatewayIpsecIkeSaMetricsDetailsResponseChildSasItem,  # noqa: PLC0415
        )
        from ..models.gateway_ipsec_ike_sa_metrics_details_response_heuristic_state import (
            GatewayIpsecIkeSaMetricsDetailsResponseHeuristicState,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        tunnel_id = d.pop("tunnel_id", UNSET)

        unique_id = d.pop("unique_id", UNSET)

        version = d.pop("version", UNSET)

        _operational_state = d.pop("operational_state", UNSET)
        operational_state: GatewayIpsecIkeSaMetricsDetailsResponseOperationalState | Unset
        if isinstance(_operational_state, Unset):
            operational_state = UNSET
        else:
            operational_state = GatewayIpsecIkeSaMetricsDetailsResponseOperationalState(_operational_state)

        _internal_state = d.pop("internal_state", UNSET)
        internal_state: GatewayIpsecIkeSaMetricsDetailsResponseInternalState | Unset
        if isinstance(_internal_state, Unset):
            internal_state = UNSET
        else:
            internal_state = GatewayIpsecIkeSaMetricsDetailsResponseInternalState(_internal_state)

        initator = d.pop("initator", UNSET)

        established = d.pop("established", UNSET)

        rekey_time = d.pop("rekey_time", UNSET)

        reauth_time = d.pop("reauth_time", UNSET)

        _child_sas = d.pop("child_sas", UNSET)
        child_sas: list[GatewayIpsecIkeSaMetricsDetailsResponseChildSasItem] | Unset = UNSET
        if _child_sas is not UNSET:
            child_sas = []
            for child_sas_item_data in _child_sas:
                child_sas_item = GatewayIpsecIkeSaMetricsDetailsResponseChildSasItem.from_dict(child_sas_item_data)

                child_sas.append(child_sas_item)

        local_host = d.pop("local_host", UNSET)

        remote_host = d.pop("remote_host", UNSET)

        local_id = d.pop("local_id", UNSET)

        remote_id = d.pop("remote_id", UNSET)

        _heuristic_state = d.pop("heuristic_state", UNSET)
        heuristic_state: GatewayIpsecIkeSaMetricsDetailsResponseHeuristicState | Unset
        if isinstance(_heuristic_state, Unset):
            heuristic_state = UNSET
        else:
            heuristic_state = GatewayIpsecIkeSaMetricsDetailsResponseHeuristicState.from_dict(_heuristic_state)

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

        gateway_ipsec_ike_sa_metrics_details_response = cls(
            name=name,
            tunnel_id=tunnel_id,
            unique_id=unique_id,
            version=version,
            operational_state=operational_state,
            internal_state=internal_state,
            initator=initator,
            established=established,
            rekey_time=rekey_time,
            reauth_time=reauth_time,
            child_sas=child_sas,
            local_host=local_host,
            remote_host=remote_host,
            local_id=local_id,
            remote_id=remote_id,
            heuristic_state=heuristic_state,
            created_at=created_at,
            updated_at=updated_at,
        )

        gateway_ipsec_ike_sa_metrics_details_response.additional_properties = d
        return gateway_ipsec_ike_sa_metrics_details_response

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
