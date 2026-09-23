from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_logs_audit_log_action import AuditLogsAuditLogAction
from ..models.audit_logs_audit_log_origin import AuditLogsAuditLogOrigin
from ..models.audit_logs_audit_log_resource_type import AuditLogsAuditLogResourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_logs_audit_log_current_state import AuditLogsAuditLogCurrentState
    from ..models.audit_logs_audit_log_previous_state import AuditLogsAuditLogPreviousState


T = TypeVar("T", bound="AuditLogsAuditLog")


@_attrs_define
class AuditLogsAuditLog:
    """A single audit log event

    Attributes:
        time (datetime.datetime): Timestamp of the event
        auth_type (str): Authentication type used (e.g., 'gui', 'api', 'basic_auth')
        cloud_event_id (str): Cloud event ID in ULID format
        upcloud_correlation_id (str): UpCloud correlation ID for request tracing
        resource_type (AuditLogsAuditLogResourceType): Type of resource affected
        action (AuditLogsAuditLogAction): Action performed
        origin (AuditLogsAuditLogOrigin): Origin of the request
        account_username (str): Username that performed the action
        resource_sub_type (str | Unset): Subtype of resource affected (e.g., 'session-api-token')
        ip_address (str | Unset): IP address of the request origin (IPv4 or IPv6). May be masked for internal UpCloud
            services.
        resource_id (str | Unset): ID of the affected resource. May be hidden for sensitive resources like auth and
            account.
        current_state (AuditLogsAuditLogCurrentState | Unset): Current state of the resource after the action (only
            present for create/update actions). Structure varies by resource_type.
        previous_state (AuditLogsAuditLogPreviousState | Unset): Previous state of the resource before the action (only
            present for update/delete actions). Structure varies by resource_type.
    """

    time: datetime.datetime
    auth_type: str
    cloud_event_id: str
    upcloud_correlation_id: str
    resource_type: AuditLogsAuditLogResourceType
    action: AuditLogsAuditLogAction
    origin: AuditLogsAuditLogOrigin
    account_username: str
    resource_sub_type: str | Unset = UNSET
    ip_address: str | Unset = UNSET
    resource_id: str | Unset = UNSET
    current_state: AuditLogsAuditLogCurrentState | Unset = UNSET
    previous_state: AuditLogsAuditLogPreviousState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time.isoformat()

        auth_type = self.auth_type

        cloud_event_id = self.cloud_event_id

        upcloud_correlation_id = self.upcloud_correlation_id

        resource_type = self.resource_type.value

        action = self.action.value

        origin = self.origin.value

        account_username = self.account_username

        resource_sub_type = self.resource_sub_type

        ip_address = self.ip_address

        resource_id = self.resource_id

        current_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.current_state, Unset):
            current_state = self.current_state.to_dict()

        previous_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous_state, Unset):
            previous_state = self.previous_state.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
                "auth_type": auth_type,
                "cloud_event_id": cloud_event_id,
                "upcloud_correlation_id": upcloud_correlation_id,
                "resource_type": resource_type,
                "action": action,
                "origin": origin,
                "account_username": account_username,
            }
        )
        if resource_sub_type is not UNSET:
            field_dict["resource_sub_type"] = resource_sub_type
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if current_state is not UNSET:
            field_dict["current_state"] = current_state
        if previous_state is not UNSET:
            field_dict["previous_state"] = previous_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_logs_audit_log_current_state import AuditLogsAuditLogCurrentState  # noqa: PLC0415
        from ..models.audit_logs_audit_log_previous_state import AuditLogsAuditLogPreviousState  # noqa: PLC0415

        d = dict(src_dict)
        time = datetime.datetime.fromisoformat(d.pop("time"))

        auth_type = d.pop("auth_type")

        cloud_event_id = d.pop("cloud_event_id")

        upcloud_correlation_id = d.pop("upcloud_correlation_id")

        resource_type = AuditLogsAuditLogResourceType(d.pop("resource_type"))

        action = AuditLogsAuditLogAction(d.pop("action"))

        origin = AuditLogsAuditLogOrigin(d.pop("origin"))

        account_username = d.pop("account_username")

        resource_sub_type = d.pop("resource_sub_type", UNSET)

        ip_address = d.pop("ip_address", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        _current_state = d.pop("current_state", UNSET)
        current_state: AuditLogsAuditLogCurrentState | Unset
        if isinstance(_current_state, Unset):
            current_state = UNSET
        else:
            current_state = AuditLogsAuditLogCurrentState.from_dict(_current_state)

        _previous_state = d.pop("previous_state", UNSET)
        previous_state: AuditLogsAuditLogPreviousState | Unset
        if isinstance(_previous_state, Unset):
            previous_state = UNSET
        else:
            previous_state = AuditLogsAuditLogPreviousState.from_dict(_previous_state)

        audit_logs_audit_log = cls(
            time=time,
            auth_type=auth_type,
            cloud_event_id=cloud_event_id,
            upcloud_correlation_id=upcloud_correlation_id,
            resource_type=resource_type,
            action=action,
            origin=origin,
            account_username=account_username,
            resource_sub_type=resource_sub_type,
            ip_address=ip_address,
            resource_id=resource_id,
            current_state=current_state,
            previous_state=previous_state,
        )

        audit_logs_audit_log.additional_properties = d
        return audit_logs_audit_log

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
