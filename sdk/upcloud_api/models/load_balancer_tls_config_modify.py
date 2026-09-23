from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerTlsConfigModify")


@_attrs_define
class LoadBalancerTlsConfigModify:
    """Load Balancer TLS Config

    Example:
        {'name': 'tls-config-1', 'certificate_bundle_uuid': '123e4567-e89b-12d3-a456-426614174000'}

    Attributes:
        name (str | Unset): Name of the config
        certificate_bundle_uuid (UUID | Unset): Certificate Bundle UUID
    """

    name: str | Unset = UNSET
    certificate_bundle_uuid: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        certificate_bundle_uuid: str | Unset = UNSET
        if not isinstance(self.certificate_bundle_uuid, Unset):
            certificate_bundle_uuid = str(self.certificate_bundle_uuid)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if certificate_bundle_uuid is not UNSET:
            field_dict["certificate_bundle_uuid"] = certificate_bundle_uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _certificate_bundle_uuid = d.pop("certificate_bundle_uuid", UNSET)
        certificate_bundle_uuid: UUID | Unset
        if isinstance(_certificate_bundle_uuid, Unset):
            certificate_bundle_uuid = UNSET
        else:
            certificate_bundle_uuid = UUID(_certificate_bundle_uuid)

        load_balancer_tls_config_modify = cls(
            name=name,
            certificate_bundle_uuid=certificate_bundle_uuid,
        )

        return load_balancer_tls_config_modify
