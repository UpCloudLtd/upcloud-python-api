from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.gateway_diffie_hellman_group_number import GatewayDiffieHellmanGroupNumber
from ..models.gateway_supported_integrity_algorithms import GatewaySupportedIntegrityAlgorithms
from ..models.gateway_supported_proposal_algorithms import GatewaySupportedProposalAlgorithms
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_tunnel_create_request_ipsec_authentication import (
        GatewayTunnelCreateRequestIpsecAuthentication,
    )


T = TypeVar("T", bound="GatewayTunnelCreateRequestIpsec")


@_attrs_define
class GatewayTunnelCreateRequestIpsec:
    """IPsec configuration

    Attributes:
        authentication (GatewayTunnelCreateRequestIpsecAuthentication): IPsec authentication configuration
        phase1_algorithms (list[GatewaySupportedProposalAlgorithms] | Unset): Phase 1 proposal algorithms
        phase2_algorithms (list[GatewaySupportedProposalAlgorithms] | Unset): Phase 2 security association algorithms
        phase1_integrity_algorithms (list[GatewaySupportedIntegrityAlgorithms] | Unset): Phase 1 integrity algorithms
        phase2_integrity_algorithms (list[GatewaySupportedIntegrityAlgorithms] | Unset): Phase 2 integrity algorithms
        phase1_dh_group_numbers (list[GatewayDiffieHellmanGroupNumber] | Unset): Phase 1 Diffie-Hellman group numbers
        phase2_dh_group_numbers (list[GatewayDiffieHellmanGroupNumber] | Unset): Phase 2 Diffie-Hellman group numbers
        ike_lifetime (int | Unset): Maximum IKE SA lifetime in seconds Default: 86400.
        rekey_time (int | Unset): IKE SA rekey time in seconds Default: 14400.
        child_rekey_time (int | Unset): IKE child SA rekey time in seconds Default: 1440.
        dpd_delay (int | Unset): Delay before sending Dead Peer Detection packets if no traffic is detected, in seconds
            Default: 30.
        dpd_timeout (int | Unset): Timeout period for DPD reply before considering the peer to be dead, in seconds
            Default: 120.
    """

    authentication: GatewayTunnelCreateRequestIpsecAuthentication
    phase1_algorithms: list[GatewaySupportedProposalAlgorithms] | Unset = UNSET
    phase2_algorithms: list[GatewaySupportedProposalAlgorithms] | Unset = UNSET
    phase1_integrity_algorithms: list[GatewaySupportedIntegrityAlgorithms] | Unset = UNSET
    phase2_integrity_algorithms: list[GatewaySupportedIntegrityAlgorithms] | Unset = UNSET
    phase1_dh_group_numbers: list[GatewayDiffieHellmanGroupNumber] | Unset = UNSET
    phase2_dh_group_numbers: list[GatewayDiffieHellmanGroupNumber] | Unset = UNSET
    ike_lifetime: int | Unset = 86400
    rekey_time: int | Unset = 14400
    child_rekey_time: int | Unset = 1440
    dpd_delay: int | Unset = 30
    dpd_timeout: int | Unset = 120

    def to_dict(self) -> dict[str, Any]:
        authentication = self.authentication.to_dict()

        phase1_algorithms: list[str] | Unset = UNSET
        if not isinstance(self.phase1_algorithms, Unset):
            phase1_algorithms = []
            for phase1_algorithms_item_data in self.phase1_algorithms:
                phase1_algorithms_item = phase1_algorithms_item_data.value
                phase1_algorithms.append(phase1_algorithms_item)

        phase2_algorithms: list[str] | Unset = UNSET
        if not isinstance(self.phase2_algorithms, Unset):
            phase2_algorithms = []
            for phase2_algorithms_item_data in self.phase2_algorithms:
                phase2_algorithms_item = phase2_algorithms_item_data.value
                phase2_algorithms.append(phase2_algorithms_item)

        phase1_integrity_algorithms: list[str] | Unset = UNSET
        if not isinstance(self.phase1_integrity_algorithms, Unset):
            phase1_integrity_algorithms = []
            for phase1_integrity_algorithms_item_data in self.phase1_integrity_algorithms:
                phase1_integrity_algorithms_item = phase1_integrity_algorithms_item_data.value
                phase1_integrity_algorithms.append(phase1_integrity_algorithms_item)

        phase2_integrity_algorithms: list[str] | Unset = UNSET
        if not isinstance(self.phase2_integrity_algorithms, Unset):
            phase2_integrity_algorithms = []
            for phase2_integrity_algorithms_item_data in self.phase2_integrity_algorithms:
                phase2_integrity_algorithms_item = phase2_integrity_algorithms_item_data.value
                phase2_integrity_algorithms.append(phase2_integrity_algorithms_item)

        phase1_dh_group_numbers: list[int] | Unset = UNSET
        if not isinstance(self.phase1_dh_group_numbers, Unset):
            phase1_dh_group_numbers = []
            for phase1_dh_group_numbers_item_data in self.phase1_dh_group_numbers:
                phase1_dh_group_numbers_item = phase1_dh_group_numbers_item_data.value
                phase1_dh_group_numbers.append(phase1_dh_group_numbers_item)

        phase2_dh_group_numbers: list[int] | Unset = UNSET
        if not isinstance(self.phase2_dh_group_numbers, Unset):
            phase2_dh_group_numbers = []
            for phase2_dh_group_numbers_item_data in self.phase2_dh_group_numbers:
                phase2_dh_group_numbers_item = phase2_dh_group_numbers_item_data.value
                phase2_dh_group_numbers.append(phase2_dh_group_numbers_item)

        ike_lifetime = self.ike_lifetime

        rekey_time = self.rekey_time

        child_rekey_time = self.child_rekey_time

        dpd_delay = self.dpd_delay

        dpd_timeout = self.dpd_timeout

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "authentication": authentication,
            }
        )
        if phase1_algorithms is not UNSET:
            field_dict["phase1_algorithms"] = phase1_algorithms
        if phase2_algorithms is not UNSET:
            field_dict["phase2_algorithms"] = phase2_algorithms
        if phase1_integrity_algorithms is not UNSET:
            field_dict["phase1_integrity_algorithms"] = phase1_integrity_algorithms
        if phase2_integrity_algorithms is not UNSET:
            field_dict["phase2_integrity_algorithms"] = phase2_integrity_algorithms
        if phase1_dh_group_numbers is not UNSET:
            field_dict["phase1_dh_group_numbers"] = phase1_dh_group_numbers
        if phase2_dh_group_numbers is not UNSET:
            field_dict["phase2_dh_group_numbers"] = phase2_dh_group_numbers
        if ike_lifetime is not UNSET:
            field_dict["ike_lifetime"] = ike_lifetime
        if rekey_time is not UNSET:
            field_dict["rekey_time"] = rekey_time
        if child_rekey_time is not UNSET:
            field_dict["child_rekey_time"] = child_rekey_time
        if dpd_delay is not UNSET:
            field_dict["dpd_delay"] = dpd_delay
        if dpd_timeout is not UNSET:
            field_dict["dpd_timeout"] = dpd_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gateway_tunnel_create_request_ipsec_authentication import (
            GatewayTunnelCreateRequestIpsecAuthentication,  # noqa: PLC0415
        )

        d = dict(src_dict)
        authentication = GatewayTunnelCreateRequestIpsecAuthentication.from_dict(d.pop("authentication"))

        _phase1_algorithms = d.pop("phase1_algorithms", UNSET)
        phase1_algorithms: list[GatewaySupportedProposalAlgorithms] | Unset = UNSET
        if _phase1_algorithms is not UNSET:
            phase1_algorithms = []
            for phase1_algorithms_item_data in _phase1_algorithms:
                phase1_algorithms_item = GatewaySupportedProposalAlgorithms(phase1_algorithms_item_data)

                phase1_algorithms.append(phase1_algorithms_item)

        _phase2_algorithms = d.pop("phase2_algorithms", UNSET)
        phase2_algorithms: list[GatewaySupportedProposalAlgorithms] | Unset = UNSET
        if _phase2_algorithms is not UNSET:
            phase2_algorithms = []
            for phase2_algorithms_item_data in _phase2_algorithms:
                phase2_algorithms_item = GatewaySupportedProposalAlgorithms(phase2_algorithms_item_data)

                phase2_algorithms.append(phase2_algorithms_item)

        _phase1_integrity_algorithms = d.pop("phase1_integrity_algorithms", UNSET)
        phase1_integrity_algorithms: list[GatewaySupportedIntegrityAlgorithms] | Unset = UNSET
        if _phase1_integrity_algorithms is not UNSET:
            phase1_integrity_algorithms = []
            for phase1_integrity_algorithms_item_data in _phase1_integrity_algorithms:
                phase1_integrity_algorithms_item = GatewaySupportedIntegrityAlgorithms(
                    phase1_integrity_algorithms_item_data
                )

                phase1_integrity_algorithms.append(phase1_integrity_algorithms_item)

        _phase2_integrity_algorithms = d.pop("phase2_integrity_algorithms", UNSET)
        phase2_integrity_algorithms: list[GatewaySupportedIntegrityAlgorithms] | Unset = UNSET
        if _phase2_integrity_algorithms is not UNSET:
            phase2_integrity_algorithms = []
            for phase2_integrity_algorithms_item_data in _phase2_integrity_algorithms:
                phase2_integrity_algorithms_item = GatewaySupportedIntegrityAlgorithms(
                    phase2_integrity_algorithms_item_data
                )

                phase2_integrity_algorithms.append(phase2_integrity_algorithms_item)

        _phase1_dh_group_numbers = d.pop("phase1_dh_group_numbers", UNSET)
        phase1_dh_group_numbers: list[GatewayDiffieHellmanGroupNumber] | Unset = UNSET
        if _phase1_dh_group_numbers is not UNSET:
            phase1_dh_group_numbers = []
            for phase1_dh_group_numbers_item_data in _phase1_dh_group_numbers:
                phase1_dh_group_numbers_item = GatewayDiffieHellmanGroupNumber(phase1_dh_group_numbers_item_data)

                phase1_dh_group_numbers.append(phase1_dh_group_numbers_item)

        _phase2_dh_group_numbers = d.pop("phase2_dh_group_numbers", UNSET)
        phase2_dh_group_numbers: list[GatewayDiffieHellmanGroupNumber] | Unset = UNSET
        if _phase2_dh_group_numbers is not UNSET:
            phase2_dh_group_numbers = []
            for phase2_dh_group_numbers_item_data in _phase2_dh_group_numbers:
                phase2_dh_group_numbers_item = GatewayDiffieHellmanGroupNumber(phase2_dh_group_numbers_item_data)

                phase2_dh_group_numbers.append(phase2_dh_group_numbers_item)

        ike_lifetime = d.pop("ike_lifetime", UNSET)

        rekey_time = d.pop("rekey_time", UNSET)

        child_rekey_time = d.pop("child_rekey_time", UNSET)

        dpd_delay = d.pop("dpd_delay", UNSET)

        dpd_timeout = d.pop("dpd_timeout", UNSET)

        gateway_tunnel_create_request_ipsec = cls(
            authentication=authentication,
            phase1_algorithms=phase1_algorithms,
            phase2_algorithms=phase2_algorithms,
            phase1_integrity_algorithms=phase1_integrity_algorithms,
            phase2_integrity_algorithms=phase2_integrity_algorithms,
            phase1_dh_group_numbers=phase1_dh_group_numbers,
            phase2_dh_group_numbers=phase2_dh_group_numbers,
            ike_lifetime=ike_lifetime,
            rekey_time=rekey_time,
            child_rekey_time=child_rekey_time,
            dpd_delay=dpd_delay,
            dpd_timeout=dpd_timeout,
        )

        return gateway_tunnel_create_request_ipsec
