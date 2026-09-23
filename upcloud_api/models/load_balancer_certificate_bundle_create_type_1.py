from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerCertificateBundleCreateType1")


@_attrs_define
class LoadBalancerCertificateBundleCreateType1:
    """
    Attributes:
        type_ (Literal['dynamic']):
        certificate (None | Unset):
        intermediates (None | Unset):
        private_key (None | Unset):
    """

    type_: Literal["dynamic"]
    certificate: None | Unset = UNSET
    intermediates: None | Unset = UNSET
    private_key: None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        certificate = self.certificate

        intermediates = self.intermediates

        private_key = self.private_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if certificate is not UNSET:
            field_dict["certificate"] = certificate
        if intermediates is not UNSET:
            field_dict["intermediates"] = intermediates
        if private_key is not UNSET:
            field_dict["private_key"] = private_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["dynamic"], d.pop("type"))
        if type_ != "dynamic":
            raise ValueError(f"type must match const 'dynamic', got '{type_}'")

        certificate = d.pop("certificate", UNSET)

        intermediates = d.pop("intermediates", UNSET)

        private_key = d.pop("private_key", UNSET)

        load_balancer_certificate_bundle_create_type_1 = cls(
            type_=type_,
            certificate=certificate,
            intermediates=intermediates,
            private_key=private_key,
        )

        load_balancer_certificate_bundle_create_type_1.additional_properties = d
        return load_balancer_certificate_bundle_create_type_1

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
