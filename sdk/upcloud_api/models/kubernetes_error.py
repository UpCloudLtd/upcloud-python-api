from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KubernetesError")


@_attrs_define
class KubernetesError:
    """Response error

    Attributes:
        type_ (str): URI to a page describing the problem
        title (str): human-readable description of the error
        status (int): HTTP Status code
        correlation_id (str): unique string that identifies the request that caused the error
        invalid_params (str | Unset): list of parameters describing a specific part(s) of the request that caused the
            error
    """

    type_: str
    title: str
    status: int
    correlation_id: str
    invalid_params: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        title = self.title

        status = self.status

        correlation_id = self.correlation_id

        invalid_params = self.invalid_params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "title": title,
                "status": status,
                "correlation_id": correlation_id,
            }
        )
        if invalid_params is not UNSET:
            field_dict["invalid_params"] = invalid_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        title = d.pop("title")

        status = d.pop("status")

        correlation_id = d.pop("correlation_id")

        invalid_params = d.pop("invalid_params", UNSET)

        kubernetes_error = cls(
            type_=type_,
            title=title,
            status=status,
            correlation_id=correlation_id,
            invalid_params=invalid_params,
        )

        kubernetes_error.additional_properties = d
        return kubernetes_error

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
