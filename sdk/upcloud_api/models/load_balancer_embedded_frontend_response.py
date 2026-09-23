from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_tls_config import LoadBalancerTlsConfig


T = TypeVar("T", bound="LoadBalancerEmbeddedFrontendResponse")


@_attrs_define
class LoadBalancerEmbeddedFrontendResponse:
    """Represents a minimal embedded reference to a frontend within a load balancer service, including its name and any
    associated TLS configurations.

        Example:
            {'name': 'frontend-http', 'tls_configs': [{'id': 42, 'name': 'frontend-tls-config', 'frontend_id': 7,
                'backend_id': 12, 'certificate_bundle_uuid': 'a4b9f1a3-9b7c-4f21-8b33-fd68efb7c001', 'created_at':
                '2025-11-06T10:15:00.000Z', 'updated_at': '2025-11-06T11:00:00.000Z'}]}

        Attributes:
            name (str): Human-readable name of the embedded frontend within the load balancer service. Example: frontend-
                http.
            tls_configs (list[LoadBalancerTlsConfig] | Unset): List of TLS configuration objects associated with this
                frontend. Each entry references a certificate bundle used for secure connections. Example: [{'id': 42, 'name':
                'frontend-tls-config', 'frontend_id': 7, 'backend_id': 12, 'certificate_bundle_uuid':
                'a4b9f1a3-9b7c-4f21-8b33-fd68efb7c001', 'created_at': '2025-11-06T10:15:00.000Z', 'updated_at':
                '2025-11-06T11:00:00.000Z'}].
    """

    name: str
    tls_configs: list[LoadBalancerTlsConfig] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        tls_configs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tls_configs, Unset):
            tls_configs = []
            for tls_configs_item_data in self.tls_configs:
                tls_configs_item = tls_configs_item_data.to_dict()
                tls_configs.append(tls_configs_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if tls_configs is not UNSET:
            field_dict["tls_configs"] = tls_configs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_tls_config import LoadBalancerTlsConfig  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        _tls_configs = d.pop("tls_configs", UNSET)
        tls_configs: list[LoadBalancerTlsConfig] | Unset = UNSET
        if _tls_configs is not UNSET:
            tls_configs = []
            for tls_configs_item_data in _tls_configs:
                tls_configs_item = LoadBalancerTlsConfig.from_dict(tls_configs_item_data)

                tls_configs.append(tls_configs_item)

        load_balancer_embedded_frontend_response = cls(
            name=name,
            tls_configs=tls_configs,
        )

        return load_balancer_embedded_frontend_response
