from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_embedded_backend_response import LoadBalancerEmbeddedBackendResponse
    from ..models.load_balancer_embedded_frontend_response import LoadBalancerEmbeddedFrontendResponse


T = TypeVar("T", bound="LoadBalancerEmbeddedServiceResponse")


@_attrs_define
class LoadBalancerEmbeddedServiceResponse:
    """Represents a minimal embedded reference to a load balancer service, including its UUID, name, and lists of
    associated frontends and backends.

        Example:
            {'uuid': 'd9f1b2a4-5c8d-4b73-91e0-8d5a0dc2e734', 'name': 'customer-service-lb', 'frontends': [{'name':
                'frontend-http', 'tls_configs': [{'id': 42, 'name': 'frontend-tls-config', 'frontend_id': 7, 'backend_id': 12,
                'certificate_bundle_uuid': 'a4b9f1a3-9b7c-4f21-8b33-fd68efb7c001', 'created_at': '2025-11-06T10:15:00.000Z',
                'updated_at': '2025-11-06T11:00:00.000Z'}]}], 'backends': [{'name': 'backend-app', 'tls_configs': [{'id': 56,
                'name': 'backend-tls-config', 'frontend_id': 7, 'backend_id': 9, 'certificate_bundle_uuid':
                'b1a5f3d8-2b3e-4b61-981f-d42cfb9a43e2', 'created_at': '2025-11-06T10:45:00.000Z', 'updated_at':
                '2025-11-06T11:20:00.000Z'}]}], 'deleted': False}

        Attributes:
            uuid (UUID): Unique identifier for the load balancer service. Example: d9f1b2a4-5c8d-4b73-91e0-8d5a0dc2e734.
            name (str): Human-readable name of the embedded service. Example: customer-service-lb.
            frontends (list[LoadBalancerEmbeddedFrontendResponse] | Unset): List of frontends associated with the service.
                Each frontend defines how client connections are received. Example: [{'name': 'frontend-http', 'tls_configs':
                [{'id': 42, 'name': 'frontend-tls-config', 'frontend_id': 7, 'backend_id': 12, 'certificate_bundle_uuid':
                'a4b9f1a3-9b7c-4f21-8b33-fd68efb7c001', 'created_at': '2025-11-06T10:15:00.000Z', 'updated_at':
                '2025-11-06T11:00:00.000Z'}]}].
            backends (list[LoadBalancerEmbeddedBackendResponse] | Unset): List of backends associated with the service. Each
                backend defines how traffic is distributed to target servers. Example: [{'name': 'backend-app', 'tls_configs':
                [{'id': 56, 'name': 'backend-tls-config', 'frontend_id': 7, 'backend_id': 9, 'certificate_bundle_uuid':
                'b1a5f3d8-2b3e-4b61-981f-d42cfb9a43e2', 'created_at': '2025-11-06T10:45:00.000Z', 'updated_at':
                '2025-11-06T11:20:00.000Z'}]}].
            deleted (bool | Unset): Indicates whether the service has been marked as deleted. Example: False.
    """

    uuid: UUID
    name: str
    frontends: list[LoadBalancerEmbeddedFrontendResponse] | Unset = UNSET
    backends: list[LoadBalancerEmbeddedBackendResponse] | Unset = UNSET
    deleted: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        frontends: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.frontends, Unset):
            frontends = []
            for frontends_item_data in self.frontends:
                frontends_item = frontends_item_data.to_dict()
                frontends.append(frontends_item)

        backends: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.backends, Unset):
            backends = []
            for backends_item_data in self.backends:
                backends_item = backends_item_data.to_dict()
                backends.append(backends_item)

        deleted = self.deleted

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
            }
        )
        if frontends is not UNSET:
            field_dict["frontends"] = frontends
        if backends is not UNSET:
            field_dict["backends"] = backends
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_embedded_backend_response import (
            LoadBalancerEmbeddedBackendResponse,  # noqa: PLC0415
        )
        from ..models.load_balancer_embedded_frontend_response import (
            LoadBalancerEmbeddedFrontendResponse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        _frontends = d.pop("frontends", UNSET)
        frontends: list[LoadBalancerEmbeddedFrontendResponse] | Unset = UNSET
        if _frontends is not UNSET:
            frontends = []
            for frontends_item_data in _frontends:
                frontends_item = LoadBalancerEmbeddedFrontendResponse.from_dict(frontends_item_data)

                frontends.append(frontends_item)

        _backends = d.pop("backends", UNSET)
        backends: list[LoadBalancerEmbeddedBackendResponse] | Unset = UNSET
        if _backends is not UNSET:
            backends = []
            for backends_item_data in _backends:
                backends_item = LoadBalancerEmbeddedBackendResponse.from_dict(backends_item_data)

                backends.append(backends_item)

        deleted = d.pop("deleted", UNSET)

        load_balancer_embedded_service_response = cls(
            uuid=uuid,
            name=name,
            frontends=frontends,
            backends=backends,
            deleted=deleted,
        )

        return load_balancer_embedded_service_response
