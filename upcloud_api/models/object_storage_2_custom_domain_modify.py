from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.object_storage_2_custom_domain_modify_type import ObjectStorage2CustomDomainModifyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2CustomDomainModify")


@_attrs_define
class ObjectStorage2CustomDomainModify:
    """Schema for modifying a custom domain.

    Attributes:
        type_ (ObjectStorage2CustomDomainModifyType | Unset): Type of the custom domain.
        domain_name (str | Unset): New modified custom domain. Supports both apex domains (example.com) and subdomains
            (objects.example.com).
    """

    type_: ObjectStorage2CustomDomainModifyType | Unset = UNSET
    domain_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        domain_name = self.domain_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if domain_name is not UNSET:
            field_dict["domain_name"] = domain_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: ObjectStorage2CustomDomainModifyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ObjectStorage2CustomDomainModifyType(_type_)

        domain_name = d.pop("domain_name", UNSET)

        object_storage_2_custom_domain_modify = cls(
            type_=type_,
            domain_name=domain_name,
        )

        return object_storage_2_custom_domain_modify
