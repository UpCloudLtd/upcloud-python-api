from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancerCertificateBundleCreateType2")


@_attrs_define
class LoadBalancerCertificateBundleCreateType2:
    """
    Attributes:
        type_ (Literal['authority']):
        hostnames (None | Unset):
        key_type (None | Unset):
        private_key (None | Unset):
        intermediates (None | Unset):
    """

    type_: Literal["authority"]
    hostnames: None | Unset = UNSET
    key_type: None | Unset = UNSET
    private_key: None | Unset = UNSET
    intermediates: None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        hostnames = self.hostnames

        key_type = self.key_type

        private_key = self.private_key

        intermediates = self.intermediates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if hostnames is not UNSET:
            field_dict["hostnames"] = hostnames
        if key_type is not UNSET:
            field_dict["key_type"] = key_type
        if private_key is not UNSET:
            field_dict["private_key"] = private_key
        if intermediates is not UNSET:
            field_dict["intermediates"] = intermediates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["authority"], d.pop("type"))
        if type_ != "authority":
            raise ValueError(f"type must match const 'authority', got '{type_}'")

        hostnames = d.pop("hostnames", UNSET)

        key_type = d.pop("key_type", UNSET)

        private_key = d.pop("private_key", UNSET)

        intermediates = d.pop("intermediates", UNSET)

        load_balancer_certificate_bundle_create_type_2 = cls(
            type_=type_,
            hostnames=hostnames,
            key_type=key_type,
            private_key=private_key,
            intermediates=intermediates,
        )

        load_balancer_certificate_bundle_create_type_2.additional_properties = d
        return load_balancer_certificate_bundle_create_type_2

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
