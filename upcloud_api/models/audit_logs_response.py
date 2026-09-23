from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audit_logs_audit_log import AuditLogsAuditLog


T = TypeVar("T", bound="AuditLogsResponse")


@_attrs_define
class AuditLogsResponse:
    """Response schema for a list of audit logs

    Attributes:
        audit_logs (list[AuditLogsAuditLog]): List of audit log events
    """

    audit_logs: list[AuditLogsAuditLog]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audit_logs = []
        for audit_logs_item_data in self.audit_logs:
            audit_logs_item = audit_logs_item_data.to_dict()
            audit_logs.append(audit_logs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audit_logs": audit_logs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_logs_audit_log import AuditLogsAuditLog  # noqa: PLC0415

        d = dict(src_dict)
        audit_logs = []
        _audit_logs = d.pop("audit_logs")
        for audit_logs_item_data in _audit_logs:
            audit_logs_item = AuditLogsAuditLog.from_dict(audit_logs_item_data)

            audit_logs.append(audit_logs_item)

        audit_logs_response = cls(
            audit_logs=audit_logs,
        )

        audit_logs_response.additional_properties = d
        return audit_logs_response

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
