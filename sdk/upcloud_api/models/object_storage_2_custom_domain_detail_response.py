from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.object_storage_2_custom_domain_detail_response_mode import ObjectStorage2CustomDomainDetailResponseMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2CustomDomainDetailResponse")


@_attrs_define
class ObjectStorage2CustomDomainDetailResponse:
    """Response schema for custom domain details.

    Attributes:
        domain_name (str | Unset): Custom domain name. Supports both apex domains and subdomains. Example: example.com.
        type_ (str | Unset): Endpoint type for the custom domain. Example: public.
        mode (ObjectStorage2CustomDomainDetailResponseMode | Unset): Purpose of the domain. 'api' for S3 API access,
            'static-website' for static website hosting. Example: api.
    """

    domain_name: str | Unset = UNSET
    type_: str | Unset = UNSET
    mode: ObjectStorage2CustomDomainDetailResponseMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_name = self.domain_name

        type_ = self.type_

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_name is not UNSET:
            field_dict["domain_name"] = domain_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_name = d.pop("domain_name", UNSET)

        type_ = d.pop("type", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: ObjectStorage2CustomDomainDetailResponseMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = ObjectStorage2CustomDomainDetailResponseMode(_mode)

        object_storage_2_custom_domain_detail_response = cls(
            domain_name=domain_name,
            type_=type_,
            mode=mode,
        )

        object_storage_2_custom_domain_detail_response.additional_properties = d
        return object_storage_2_custom_domain_detail_response

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
