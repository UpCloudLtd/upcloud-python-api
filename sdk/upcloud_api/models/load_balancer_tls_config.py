from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LoadBalancerTlsConfig")


@_attrs_define
class LoadBalancerTlsConfig:
    """Represents a TLS configuration for a frontend or backend, defining the certificate bundle and associated identifiers
    within the load balancer service.

        Attributes:
            name (str): Human-readable name assigned to the TLS configuration. Example: frontend-tls-config.
            certificate_bundle_uuid (UUID): UUID of the certificate bundle used for TLS encryption. Example:
                a4b9f1a3-9b7c-4f21-8b33-fd68efb7c001.
            created_at (datetime.datetime): Timestamp when the TLS configuration was created (RFC 3339 format).
            updated_at (datetime.datetime): Timestamp when the TLS configuration was last updated (RFC 3339 format).
    """

    name: str
    certificate_bundle_uuid: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        certificate_bundle_uuid = str(self.certificate_bundle_uuid)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "certificate_bundle_uuid": certificate_bundle_uuid,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        certificate_bundle_uuid = UUID(d.pop("certificate_bundle_uuid"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        load_balancer_tls_config = cls(
            name=name,
            certificate_bundle_uuid=certificate_bundle_uuid,
            created_at=created_at,
            updated_at=updated_at,
        )

        load_balancer_tls_config.additional_properties = d
        return load_balancer_tls_config

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
