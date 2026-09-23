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


T = TypeVar("T", bound="ObjectStorage2ServiceModify")


@_attrs_define
class ObjectStorage2ServiceModify:
    """Schema for modifying a service, including name, status, networks, domains, labels, and properties.

    Attributes:
        name (str | Unset):  Example: example-service.
        configured_status (ObjectStorage2PropertyConfiguredStatus | Unset): Schema for the configured status of a
            property.
        networks (list[ObjectStorage2NetworkCreate] | None | Unset):
        custom_domains (list[ObjectStorage2CustomDomainCreate] | None | Unset):
        static_websites (list[ObjectStorage2StaticWebsiteConfigCreate] | None | Unset): Static website configurations
            for this service. Array replaces all existing configurations.
        labels (list[ObjectStorage2LabelCreate] | None | Unset):
        properties (ObjectStorage2PropertiesCreate | Unset): Schema for creating properties with an optional access
            control origin override.
        termination_protection (bool | Unset): Enables or disables termination protection for the service. When enabled,
            the service cannot be deleted or powered down unless this is disabled first. Example: False.
    """

    name: str | Unset = UNSET
    configured_status: ObjectStorage2PropertyConfiguredStatus | Unset = UNSET
    networks: list[ObjectStorage2NetworkCreate] | None | Unset = UNSET
    custom_domains: list[ObjectStorage2CustomDomainCreate] | None | Unset = UNSET
    static_websites: list[ObjectStorage2StaticWebsiteConfigCreate] | None | Unset = UNSET
    labels: list[ObjectStorage2LabelCreate] | None | Unset = UNSET
    properties: ObjectStorage2PropertiesCreate | Unset = UNSET
    termination_protection: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        configured_status: str | Unset = UNSET
        if not isinstance(self.configured_status, Unset):
            configured_status = self.configured_status.value

        networks: list[dict[str, Any]] | None | Unset
        if isinstance(self.networks, Unset):
            networks = UNSET
        elif isinstance(self.networks, list):
            networks = []
            for networks_type_0_item_data in self.networks:
                networks_type_0_item = networks_type_0_item_data.to_dict()
                networks.append(networks_type_0_item)

        else:
            networks = self.networks

        custom_domains: list[dict[str, Any]] | None | Unset
        if isinstance(self.custom_domains, Unset):
            custom_domains = UNSET
        elif isinstance(self.custom_domains, list):
            custom_domains = []
            for custom_domains_type_0_item_data in self.custom_domains:
                custom_domains_type_0_item = custom_domains_type_0_item_data.to_dict()
                custom_domains.append(custom_domains_type_0_item)

        else:
            custom_domains = self.custom_domains

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

        labels: list[dict[str, Any]] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, list):
            labels = []
            for labels_type_0_item_data in self.labels:
                labels_type_0_item = labels_type_0_item_data.to_dict()
                labels.append(labels_type_0_item)

        else:
            labels = self.labels

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        termination_protection = self.termination_protection

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if configured_status is not UNSET:
            field_dict["configured_status"] = configured_status
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
        if termination_protection is not UNSET:
            field_dict["termination_protection"] = termination_protection

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
        name = d.pop("name", UNSET)

        _configured_status = d.pop("configured_status", UNSET)
        configured_status: ObjectStorage2PropertyConfiguredStatus | Unset
        if isinstance(_configured_status, Unset):
            configured_status = UNSET
        else:
            configured_status = ObjectStorage2PropertyConfiguredStatus(_configured_status)

        def _parse_networks(data: object) -> list[ObjectStorage2NetworkCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                networks_type_0 = []
                _networks_type_0 = data
                for networks_type_0_item_data in _networks_type_0:
                    networks_type_0_item = ObjectStorage2NetworkCreate.from_dict(networks_type_0_item_data)

                    networks_type_0.append(networks_type_0_item)

                return networks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ObjectStorage2NetworkCreate] | None | Unset, data)

        networks = _parse_networks(d.pop("networks", UNSET))

        def _parse_custom_domains(data: object) -> list[ObjectStorage2CustomDomainCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_domains_type_0 = []
                _custom_domains_type_0 = data
                for custom_domains_type_0_item_data in _custom_domains_type_0:
                    custom_domains_type_0_item = ObjectStorage2CustomDomainCreate.from_dict(
                        custom_domains_type_0_item_data
                    )

                    custom_domains_type_0.append(custom_domains_type_0_item)

                return custom_domains_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ObjectStorage2CustomDomainCreate] | None | Unset, data)

        custom_domains = _parse_custom_domains(d.pop("custom_domains", UNSET))

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

        def _parse_labels(data: object) -> list[ObjectStorage2LabelCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                labels_type_0 = []
                _labels_type_0 = data
                for labels_type_0_item_data in _labels_type_0:
                    labels_type_0_item = ObjectStorage2LabelCreate.from_dict(labels_type_0_item_data)

                    labels_type_0.append(labels_type_0_item)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ObjectStorage2LabelCreate] | None | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        _properties = d.pop("properties", UNSET)
        properties: ObjectStorage2PropertiesCreate | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = ObjectStorage2PropertiesCreate.from_dict(_properties)

        termination_protection = d.pop("termination_protection", UNSET)

        object_storage_2_service_modify = cls(
            name=name,
            configured_status=configured_status,
            networks=networks,
            custom_domains=custom_domains,
            static_websites=static_websites,
            labels=labels,
            properties=properties,
            termination_protection=termination_protection,
        )

        return object_storage_2_service_modify
