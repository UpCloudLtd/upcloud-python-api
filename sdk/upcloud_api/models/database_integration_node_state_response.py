from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseIntegrationNodeStateResponse")


@_attrs_define
class DatabaseIntegrationNodeStateResponse:
    """Schema for representing the state of an integration node

    Attributes:
        name (str | Unset): The name of the integration node Example: node-1.
        status (str | Unset): The current status of the node Example: running.
        errors (list[Any] | Unset): A list of errors encountered by the node
        likely_error_cause (None | str | Unset): The likely cause of the error
    """

    name: str | Unset = UNSET
    status: str | Unset = UNSET
    errors: list[Any] | Unset = UNSET
    likely_error_cause: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        errors: list[Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        likely_error_cause: None | str | Unset
        if isinstance(self.likely_error_cause, Unset):
            likely_error_cause = UNSET
        else:
            likely_error_cause = self.likely_error_cause

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if errors is not UNSET:
            field_dict["errors"] = errors
        if likely_error_cause is not UNSET:
            field_dict["likely_error_cause"] = likely_error_cause

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        errors = cast(list[Any], d.pop("errors", UNSET))

        def _parse_likely_error_cause(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        likely_error_cause = _parse_likely_error_cause(d.pop("likely_error_cause", UNSET))

        database_integration_node_state_response = cls(
            name=name,
            status=status,
            errors=errors,
            likely_error_cause=likely_error_cause,
        )

        database_integration_node_state_response.additional_properties = d
        return database_integration_node_state_response

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
