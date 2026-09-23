from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.object_storage_2_service_domains_domains_item_type import ObjectStorage2ServiceDomainsDomainsItemType

T = TypeVar("T", bound="ObjectStorage2ServiceDomainsDomainsItem")


@_attrs_define
class ObjectStorage2ServiceDomainsDomainsItem:
    """
    Attributes:
        domain (str): Domain name (e.g., unc38.local.upbucket.com) Example: unc38.local.upbucket.com.
        type_ (ObjectStorage2ServiceDomainsDomainsItemType): Type of domain (public endpoint, private endpoint, or
            custom domain) Example: public.
        active (bool): Whether this domain is active and ready to use (always true for enabled public/private endpoints,
            true for custom domains only if certificate is ready) Example: True.
        static_website_configured (bool): Whether static website hosting is configured for this domain Example: False.
    """

    domain: str
    type_: ObjectStorage2ServiceDomainsDomainsItemType
    active: bool
    static_website_configured: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        type_ = self.type_.value

        active = self.active

        static_website_configured = self.static_website_configured

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "type": type_,
                "active": active,
                "static_website_configured": static_website_configured,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        type_ = ObjectStorage2ServiceDomainsDomainsItemType(d.pop("type"))

        active = d.pop("active")

        static_website_configured = d.pop("static_website_configured")

        object_storage_2_service_domains_domains_item = cls(
            domain=domain,
            type_=type_,
            active=active,
            static_website_configured=static_website_configured,
        )

        object_storage_2_service_domains_domains_item.additional_properties = d
        return object_storage_2_service_domains_domains_item

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
