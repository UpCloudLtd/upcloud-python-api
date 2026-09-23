from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.object_storage_2_service_domains_domains_item import ObjectStorage2ServiceDomainsDomainsItem


T = TypeVar("T", bound="ObjectStorage2ServiceDomains")


@_attrs_define
class ObjectStorage2ServiceDomains:
    """Service domains with their static website hosting status

    Attributes:
        domains (list[ObjectStorage2ServiceDomainsDomainsItem]): List of all service domains (public, private, custom)
            with their static website hosting availability and configuration status
    """

    domains: list[ObjectStorage2ServiceDomainsDomainsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domains = []
        for domains_item_data in self.domains:
            domains_item = domains_item_data.to_dict()
            domains.append(domains_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domains": domains,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_storage_2_service_domains_domains_item import (
            ObjectStorage2ServiceDomainsDomainsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        domains = []
        _domains = d.pop("domains")
        for domains_item_data in _domains:
            domains_item = ObjectStorage2ServiceDomainsDomainsItem.from_dict(domains_item_data)

            domains.append(domains_item)

        object_storage_2_service_domains = cls(
            domains=domains,
        )

        object_storage_2_service_domains.additional_properties = d
        return object_storage_2_service_domains

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
