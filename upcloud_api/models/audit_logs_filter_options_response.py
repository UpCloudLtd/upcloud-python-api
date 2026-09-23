from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_logs_filter_options_response_actions_item import AuditLogsFilterOptionsResponseActionsItem
from ..models.audit_logs_filter_options_response_origins_item import AuditLogsFilterOptionsResponseOriginsItem
from ..models.audit_logs_filter_options_response_resource_types_item import (
    AuditLogsFilterOptionsResponseResourceTypesItem,
)

T = TypeVar("T", bound="AuditLogsFilterOptionsResponse")


@_attrs_define
class AuditLogsFilterOptionsResponse:
    """Available filter options for audit logs

    Attributes:
        resource_types (list[AuditLogsFilterOptionsResponseResourceTypesItem]): List of available resource types
        actions (list[AuditLogsFilterOptionsResponseActionsItem]): List of available actions
        origins (list[AuditLogsFilterOptionsResponseOriginsItem]): List of available origins
    """

    resource_types: list[AuditLogsFilterOptionsResponseResourceTypesItem]
    actions: list[AuditLogsFilterOptionsResponseActionsItem]
    origins: list[AuditLogsFilterOptionsResponseOriginsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_types = []
        for resource_types_item_data in self.resource_types:
            resource_types_item = resource_types_item_data.value
            resource_types.append(resource_types_item)

        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.value
            actions.append(actions_item)

        origins = []
        for origins_item_data in self.origins:
            origins_item = origins_item_data.value
            origins.append(origins_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource_types": resource_types,
                "actions": actions,
                "origins": origins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_types = []
        _resource_types = d.pop("resource_types")
        for resource_types_item_data in _resource_types:
            resource_types_item = AuditLogsFilterOptionsResponseResourceTypesItem(resource_types_item_data)

            resource_types.append(resource_types_item)

        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = AuditLogsFilterOptionsResponseActionsItem(actions_item_data)

            actions.append(actions_item)

        origins = []
        _origins = d.pop("origins")
        for origins_item_data in _origins:
            origins_item = AuditLogsFilterOptionsResponseOriginsItem(origins_item_data)

            origins.append(origins_item)

        audit_logs_filter_options_response = cls(
            resource_types=resource_types,
            actions=actions,
            origins=origins,
        )

        audit_logs_filter_options_response.additional_properties = d
        return audit_logs_filter_options_response

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
