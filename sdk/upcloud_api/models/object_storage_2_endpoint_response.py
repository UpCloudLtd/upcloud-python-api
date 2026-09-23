from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.object_storage_2_endpoint_response_mode import ObjectStorage2EndpointResponseMode
from ..models.object_storage_2_endpoint_response_type import ObjectStorage2EndpointResponseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorage2EndpointResponse")


@_attrs_define
class ObjectStorage2EndpointResponse:
    """Response schema for endpoint details.

    Attributes:
        domain_name (str | Unset):  Example: objects.example.com.
        iam_url (str | Unset):  Example: https://7mf5k.upbucket.com:4443/iam.
        sts_url (str | Unset):  Example: https://7mf5k.upbucket.com:4443/sts.
        type_ (ObjectStorage2EndpointResponseType | Unset): The network access type of the endpoint Example: public.
        mode (ObjectStorage2EndpointResponseMode | Unset): The operational mode of the endpoint: 'api' for S3/IAM/STS
            access, 'static-website' for static website hosting Example: api.
    """

    domain_name: str | Unset = UNSET
    iam_url: str | Unset = UNSET
    sts_url: str | Unset = UNSET
    type_: ObjectStorage2EndpointResponseType | Unset = UNSET
    mode: ObjectStorage2EndpointResponseMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain_name = self.domain_name

        iam_url = self.iam_url

        sts_url = self.sts_url

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain_name is not UNSET:
            field_dict["domain_name"] = domain_name
        if iam_url is not UNSET:
            field_dict["iam_url"] = iam_url
        if sts_url is not UNSET:
            field_dict["sts_url"] = sts_url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain_name = d.pop("domain_name", UNSET)

        iam_url = d.pop("iam_url", UNSET)

        sts_url = d.pop("sts_url", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ObjectStorage2EndpointResponseType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ObjectStorage2EndpointResponseType(_type_)

        _mode = d.pop("mode", UNSET)
        mode: ObjectStorage2EndpointResponseMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = ObjectStorage2EndpointResponseMode(_mode)

        object_storage_2_endpoint_response = cls(
            domain_name=domain_name,
            iam_url=iam_url,
            sts_url=sts_url,
            type_=type_,
            mode=mode,
        )

        object_storage_2_endpoint_response.additional_properties = d
        return object_storage_2_endpoint_response

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
