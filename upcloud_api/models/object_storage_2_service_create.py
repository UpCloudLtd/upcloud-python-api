from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.object_storage_2_property_configured_status import ObjectStorage2PropertyConfiguredStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_storage_2_custom_domain_create import ObjectStorage2CustomDomainCreate
    from ..models.object_storage_2_label_create import ObjectStorage2LabelCreate
    from ..models.object_storage_2_network_create import ObjectStorage2NetworkCreate
    from ..models.object_storage_2_properties_create import ObjectStorage2PropertiesCreate


T = TypeVar("T", bound="ObjectStorage2ServiceCreate")


@_attrs_define
class ObjectStorage2ServiceCreate:
    """Schema for creating a service, including name, region, status, networks, domains, labels, and properties.

    Attributes:
        name (str):
        region (str): A resource name.
        configured_status (ObjectStorage2PropertyConfiguredStatus): Schema for the configured status of a property.
        networks (list[ObjectStorage2NetworkCreate] | Unset): Networks to attach to the service. Private networks must
            reside in the same region as the object storage.
        custom_domains (list[ObjectStorage2CustomDomainCreate] | Unset): Custom domains to attach to the service.
        labels (list[ObjectStorage2LabelCreate] | Unset): Labels for classifying the service.
        properties (ObjectStorage2PropertiesCreate | Unset): Schema for creating properties with an optional access
            control origin override.
        termination_protection (bool | Unset): Enables or disables termination protection for the service. When enabled,
            the service cannot be deleted or powered down unless this is disabled first. Default: False. Example: False.
    """

    name: str
    region: str
    configured_status: ObjectStorage2PropertyConfiguredStatus
    networks: list[ObjectStorage2NetworkCreate] | Unset = UNSET
    custom_domains: list[ObjectStorage2CustomDomainCreate] | Unset = UNSET
    labels: list[ObjectStorage2LabelCreate] | Unset = UNSET
    properties: ObjectStorage2PropertiesCreate | Unset = UNSET
    termination_protection: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        region = self.region

        configured_status = self.configured_status.value

        networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()
                networks.append(networks_item)

        custom_domains: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_domains, Unset):
            custom_domains = []
            for custom_domains_item_data in self.custom_domains:
                custom_domains_item = custom_domains_item_data.to_dict()
                custom_domains.append(custom_domains_item)

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        termination_protection = self.termination_protection

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "region": region,
                "configured_status": configured_status,
            }
        )
        if networks is not UNSET:
            field_dict["networks"] = networks
        if custom_domains is not UNSET:
            field_dict["custom_domains"] = custom_domains
        if labels is not UNSET:
            field_dict["labels"] = labels
        if properties is not UNSET:
            field_dict["properties"] = properties
        if termination_protection is not UNSET:
            field_dict["termination_protection"] = termination_protection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_storage_2_custom_domain_create import ObjectStorage2CustomDomainCreate  # noqa: PLC0415
        from ..models.object_storage_2_label_create import ObjectStorage2LabelCreate  # noqa: PLC0415
        from ..models.object_storage_2_network_create import ObjectStorage2NetworkCreate  # noqa: PLC0415
        from ..models.object_storage_2_properties_create import ObjectStorage2PropertiesCreate  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        region = d.pop("region")

        configured_status = ObjectStorage2PropertyConfiguredStatus(d.pop("configured_status"))

        _networks = d.pop("networks", UNSET)
        networks: list[ObjectStorage2NetworkCreate] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = ObjectStorage2NetworkCreate.from_dict(networks_item_data)

                networks.append(networks_item)

        _custom_domains = d.pop("custom_domains", UNSET)
        custom_domains: list[ObjectStorage2CustomDomainCreate] | Unset = UNSET
        if _custom_domains is not UNSET:
            custom_domains = []
            for custom_domains_item_data in _custom_domains:
                custom_domains_item = ObjectStorage2CustomDomainCreate.from_dict(custom_domains_item_data)

                custom_domains.append(custom_domains_item)

        _labels = d.pop("labels", UNSET)
        labels: list[ObjectStorage2LabelCreate] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = ObjectStorage2LabelCreate.from_dict(labels_item_data)

                labels.append(labels_item)

        _properties = d.pop("properties", UNSET)
        properties: ObjectStorage2PropertiesCreate | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = ObjectStorage2PropertiesCreate.from_dict(_properties)

        termination_protection = d.pop("termination_protection", UNSET)

        object_storage_2_service_create = cls(
            name=name,
            region=region,
            configured_status=configured_status,
            networks=networks,
            custom_domains=custom_domains,
            labels=labels,
            properties=properties,
            termination_protection=termination_protection,
        )

        return object_storage_2_service_create
