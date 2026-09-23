from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="LoadBalancerTlsConfigCreate")


@_attrs_define
class LoadBalancerTlsConfigCreate:
    """Load Balancer TLS Config

    Example:
        {'name': 'tls-config-1', 'certificate_bundle_uuid': '123e4567-e89b-12d3-a456-426614174000'}

    Attributes:
        name (str): Name of the config Example: tls-config-1.
        certificate_bundle_uuid (UUID): Certificate Bundle UUID Example: 123e4567-e89b-12d3-a456-426614174000.
    """

    name: str
    certificate_bundle_uuid: UUID

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        certificate_bundle_uuid = str(self.certificate_bundle_uuid)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "certificate_bundle_uuid": certificate_bundle_uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        certificate_bundle_uuid = UUID(d.pop("certificate_bundle_uuid"))

        load_balancer_tls_config_create = cls(
            name=name,
            certificate_bundle_uuid=certificate_bundle_uuid,
        )

        return load_balancer_tls_config_create
