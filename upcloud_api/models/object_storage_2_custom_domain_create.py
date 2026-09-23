from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.object_storage_2_custom_domain_create_mode import ObjectStorage2CustomDomainCreateMode
from ..models.object_storage_2_custom_domain_create_type import ObjectStorage2CustomDomainCreateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2CustomDomainCreate")


@_attrs_define
class ObjectStorage2CustomDomainCreate:
    """Schema for creating a custom domain.

    Attributes:
        type_ (ObjectStorage2CustomDomainCreateType): Type of the custom domain. At the moment only public is accepted.
            Example: public.
        domain_name (str): Custom domain to be added. Supports both apex domains (example.com) and subdomains
            (objects.example.com). Example: example.com.
        mode (ObjectStorage2CustomDomainCreateMode | Unset): Purpose of the domain. 'api' for S3 API access (creates
            base URL), 'static-website' for static website hosting (no base URL). Cannot be changed after creation. Default:
            ObjectStorage2CustomDomainCreateMode.API. Example: api.
    """

    type_: ObjectStorage2CustomDomainCreateType
    domain_name: str
    mode: ObjectStorage2CustomDomainCreateMode | Unset = ObjectStorage2CustomDomainCreateMode.API

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        domain_name = self.domain_name

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "domain_name": domain_name,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ObjectStorage2CustomDomainCreateType(d.pop("type"))

        domain_name = d.pop("domain_name")

        _mode = d.pop("mode", UNSET)
        mode: ObjectStorage2CustomDomainCreateMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = ObjectStorage2CustomDomainCreateMode(_mode)

        object_storage_2_custom_domain_create = cls(
            type_=type_,
            domain_name=domain_name,
            mode=mode,
        )

        return object_storage_2_custom_domain_create
