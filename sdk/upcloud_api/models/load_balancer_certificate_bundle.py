from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.load_balancer_certificate_bundle_key_type import LoadBalancerCertificateBundleKeyType
from ..models.load_balancer_certificate_bundle_operational_state import LoadBalancerCertificateBundleOperationalState
from ..models.load_balancer_certificate_bundle_tls_type import LoadBalancerCertificateBundleTlsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.load_balancer_challenge_problem_response import LoadBalancerChallengeProblemResponse
    from ..models.load_balancer_embedded_service_response import LoadBalancerEmbeddedServiceResponse
    from ..models.load_balancer_label_response import LoadBalancerLabelResponse


T = TypeVar("T", bound="LoadBalancerCertificateBundle")


@_attrs_define
class LoadBalancerCertificateBundle:
    """Represents a certificate bundle used in a load balancer TLS configuration. A bundle may be manually uploaded,
    dynamically issued via ACME, or represent an authority certificate. It includes certificate data, challenge details,
    and metadata about its lifecycle.

        Attributes:
            uuid (UUID): Unique identifier for the certificate bundle. Example: 8d2f4a1e-0e3f-44a9-a0f5-9b8c84e9c701.
            name (str): Human-readable name assigned to the certificate bundle. Example: mydomain-cert-bundle.
            tls_type (LoadBalancerCertificateBundleTlsType): The certificate bundle type. Determines how the certificate is
                provisioned and managed. Example: dynamic.
            operational_state (LoadBalancerCertificateBundleOperationalState): Current operational state of the certificate
                bundle. Example: pending.
            created_at (datetime.datetime): Timestamp when this certificate bundle was created.
            updated_at (datetime.datetime): Timestamp when this certificate bundle was last updated.
            certificate (str | Unset): PEM-encoded certificate data (base64). Example:
                LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0t....
            intermediates (str | Unset): PEM-encoded intermediate certificates (base64). Example:
                LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0t....
            hostnames (list[str] | Unset): List of hostnames covered by this certificate bundle. Example: ['example.com',
                'www.example.com'].
            challenge_problems (list[LoadBalancerChallengeProblemResponse] | Unset): Problems reported during ACME challenge
                validation.
            key_type (LoadBalancerCertificateBundleKeyType | Unset): Type of private key used for this certificate bundle.
                Example: rsa.
            services (list[LoadBalancerEmbeddedServiceResponse] | Unset): List of load balancer services that use this
                certificate bundle.
            not_before (datetime.datetime | Unset): The start date and time of certificate validity.
            not_after (datetime.datetime | Unset): The expiration date and time of certificate validity.
            labels (list[LoadBalancerLabelResponse] | Unset): List of labels attached to this certificate bundle.
    """

    uuid: UUID
    name: str
    tls_type: LoadBalancerCertificateBundleTlsType
    operational_state: LoadBalancerCertificateBundleOperationalState
    created_at: datetime.datetime
    updated_at: datetime.datetime
    certificate: str | Unset = UNSET
    intermediates: str | Unset = UNSET
    hostnames: list[str] | Unset = UNSET
    challenge_problems: list[LoadBalancerChallengeProblemResponse] | Unset = UNSET
    key_type: LoadBalancerCertificateBundleKeyType | Unset = UNSET
    services: list[LoadBalancerEmbeddedServiceResponse] | Unset = UNSET
    not_before: datetime.datetime | Unset = UNSET
    not_after: datetime.datetime | Unset = UNSET
    labels: list[LoadBalancerLabelResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        uuid = str(self.uuid)

        name = self.name

        tls_type = self.tls_type.value

        operational_state = self.operational_state.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        certificate = self.certificate

        intermediates = self.intermediates

        hostnames: list[str] | Unset = UNSET
        if not isinstance(self.hostnames, Unset):
            hostnames = self.hostnames

        challenge_problems: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.challenge_problems, Unset):
            challenge_problems = []
            for challenge_problems_item_data in self.challenge_problems:
                challenge_problems_item = challenge_problems_item_data.to_dict()
                challenge_problems.append(challenge_problems_item)

        key_type: str | Unset = UNSET
        if not isinstance(self.key_type, Unset):
            key_type = self.key_type.value

        services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        not_before: str | Unset = UNSET
        if not isinstance(self.not_before, Unset):
            not_before = self.not_before.isoformat()

        not_after: str | Unset = UNSET
        if not isinstance(self.not_after, Unset):
            not_after = self.not_after.isoformat()

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "uuid": uuid,
                "name": name,
                "tls_type": tls_type,
                "operational_state": operational_state,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if intermediates is not UNSET:
            field_dict["intermediates"] = intermediates
        if hostnames is not UNSET:
            field_dict["hostnames"] = hostnames
        if challenge_problems is not UNSET:
            field_dict["challenge_problems"] = challenge_problems
        if key_type is not UNSET:
            field_dict["key_type"] = key_type
        if services is not UNSET:
            field_dict["services"] = services
        if not_before is not UNSET:
            field_dict["not_before"] = not_before
        if not_after is not UNSET:
            field_dict["not_after"] = not_after
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.load_balancer_challenge_problem_response import (
            LoadBalancerChallengeProblemResponse,  # noqa: PLC0415
        )
        from ..models.load_balancer_embedded_service_response import (
            LoadBalancerEmbeddedServiceResponse,  # noqa: PLC0415
        )
        from ..models.load_balancer_label_response import LoadBalancerLabelResponse  # noqa: PLC0415

        d = dict(src_dict)
        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        tls_type = LoadBalancerCertificateBundleTlsType(d.pop("tls_type"))

        operational_state = LoadBalancerCertificateBundleOperationalState(d.pop("operational_state"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        certificate = d.pop("certificate", UNSET)

        intermediates = d.pop("intermediates", UNSET)

        hostnames = cast(list[str], d.pop("hostnames", UNSET))

        _challenge_problems = d.pop("challenge_problems", UNSET)
        challenge_problems: list[LoadBalancerChallengeProblemResponse] | Unset = UNSET
        if _challenge_problems is not UNSET:
            challenge_problems = []
            for challenge_problems_item_data in _challenge_problems:
                challenge_problems_item = LoadBalancerChallengeProblemResponse.from_dict(challenge_problems_item_data)

                challenge_problems.append(challenge_problems_item)

        _key_type = d.pop("key_type", UNSET)
        key_type: LoadBalancerCertificateBundleKeyType | Unset
        if isinstance(_key_type, Unset):
            key_type = UNSET
        else:
            key_type = LoadBalancerCertificateBundleKeyType(_key_type)

        _services = d.pop("services", UNSET)
        services: list[LoadBalancerEmbeddedServiceResponse] | Unset = UNSET
        if _services is not UNSET:
            services = []
            for services_item_data in _services:
                services_item = LoadBalancerEmbeddedServiceResponse.from_dict(services_item_data)

                services.append(services_item)

        _not_before = d.pop("not_before", UNSET)
        not_before: datetime.datetime | Unset
        if isinstance(_not_before, Unset):
            not_before = UNSET
        else:
            not_before = datetime.datetime.fromisoformat(_not_before)

        _not_after = d.pop("not_after", UNSET)
        not_after: datetime.datetime | Unset
        if isinstance(_not_after, Unset):
            not_after = UNSET
        else:
            not_after = datetime.datetime.fromisoformat(_not_after)

        _labels = d.pop("labels", UNSET)
        labels: list[LoadBalancerLabelResponse] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = LoadBalancerLabelResponse.from_dict(labels_item_data)

                labels.append(labels_item)

        load_balancer_certificate_bundle = cls(
            uuid=uuid,
            name=name,
            tls_type=tls_type,
            operational_state=operational_state,
            created_at=created_at,
            updated_at=updated_at,
            certificate=certificate,
            intermediates=intermediates,
            hostnames=hostnames,
            challenge_problems=challenge_problems,
            key_type=key_type,
            services=services,
            not_before=not_before,
            not_after=not_after,
            labels=labels,
        )

        return load_balancer_certificate_bundle
