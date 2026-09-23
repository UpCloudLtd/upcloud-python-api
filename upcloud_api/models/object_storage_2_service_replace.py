from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.object_storage_2_property_configured_status import ObjectStorage2PropertyConfiguredStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_storage_2_custom_domain_create import ObjectStorage2CustomDomainCreate
    from ..models.object_storage_2_label_create import ObjectStorage2LabelCreate
    from ..models.object_storage_2_network_create import ObjectStorage2NetworkCreate
    from ..models.object_storage_2_properties_create import ObjectStorage2PropertiesCreate
    from ..models.object_storage_2_static_website_config_create import ObjectStorage2StaticWebsiteConfigCreate


T = TypeVar("T", bound="ObjectStorage2ServiceReplace")


@_attrs_define
class ObjectStorage2ServiceReplace:
    """Schema for replacing a service, including name, status, networks, domains, labels, and properties.

    Attributes:
        name (str): The name of the service. Example: example-service.
        configured_status (ObjectStorage2PropertyConfiguredStatus): Schema for the configured status of a property.
        termination_protection (bool | Unset): Enables or disables termination protection for the service. When enabled,
            the service cannot be deleted or powered down unless this is disabled first. Default: False. Example: False.
        networks (list[ObjectStorage2NetworkCreate] | Unset):
        custom_domains (list[ObjectStorage2CustomDomainCreate] | Unset):
        static_websites (list[ObjectStorage2StaticWebsiteConfigCreate] | None | Unset): Static website configurations
            for this service. Array replaces all existing configurations.
        labels (list[ObjectStorage2LabelCreate] | Unset):
        properties (ObjectStorage2PropertiesCreate | Unset): Schema for creating properties with an optional access
            control origin override.
    """

    name: str
    configured_status: ObjectStorage2PropertyConfiguredStatus
    termination_protection: bool | Unset = False
    networks: list[ObjectStorage2NetworkCreate] | Unset = UNSET
    custom_domains: list[ObjectStorage2CustomDomainCreate] | Unset = UNSET
    static_websites: list[ObjectStorage2StaticWebsiteConfigCreate] | None | Unset = UNSET
    labels: list[ObjectStorage2LabelCreate] | Unset = UNSET
    properties: ObjectStorage2PropertiesCreate | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        configured_status = self.configured_status.value

        termination_protection = self.termination_protection

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

        static_websites: list[dict[str, Any]] | None | Unset
        if isinstance(self.static_websites, Unset):
            static_websites = UNSET
        elif isinstance(self.static_websites, list):
            static_websites = []
            for static_websites_type_0_item_data in self.static_websites:
                static_websites_type_0_item = static_websites_type_0_item_data.to_dict()
                static_websites.append(static_websites_type_0_item)

        else:
            static_websites = self.static_websites

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "configured_status": configured_status,
            }
        )
        if termination_protection is not UNSET:
            field_dict["termination_protection"] = termination_protection
        if networks is not UNSET:
            field_dict["networks"] = networks
        if custom_domains is not UNSET:
            field_dict["custom_domains"] = custom_domains
        if static_websites is not UNSET:
            field_dict["static_websites"] = static_websites
        if labels is not UNSET:
            field_dict["labels"] = labels
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_storage_2_custom_domain_create import ObjectStorage2CustomDomainCreate  # noqa: PLC0415
        from ..models.object_storage_2_label_create import ObjectStorage2LabelCreate  # noqa: PLC0415
        from ..models.object_storage_2_network_create import ObjectStorage2NetworkCreate  # noqa: PLC0415
        from ..models.object_storage_2_properties_create import ObjectStorage2PropertiesCreate  # noqa: PLC0415
        from ..models.object_storage_2_static_website_config_create import (
            ObjectStorage2StaticWebsiteConfigCreate,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        configured_status = ObjectStorage2PropertyConfiguredStatus(d.pop("configured_status"))

        termination_protection = d.pop("termination_protection", UNSET)

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

        def _parse_static_websites(data: object) -> list[ObjectStorage2StaticWebsiteConfigCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                static_websites_type_0 = []
                _static_websites_type_0 = data
                for static_websites_type_0_item_data in _static_websites_type_0:
                    static_websites_type_0_item = ObjectStorage2StaticWebsiteConfigCreate.from_dict(
                        static_websites_type_0_item_data
                    )

                    static_websites_type_0.append(static_websites_type_0_item)

                return static_websites_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ObjectStorage2StaticWebsiteConfigCreate] | None | Unset, data)

        static_websites = _parse_static_websites(d.pop("static_websites", UNSET))

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

        object_storage_2_service_replace = cls(
            name=name,
            configured_status=configured_status,
            termination_protection=termination_protection,
            networks=networks,
            custom_domains=custom_domains,
            static_websites=static_websites,
            labels=labels,
            properties=properties,
        )

        return object_storage_2_service_replace
