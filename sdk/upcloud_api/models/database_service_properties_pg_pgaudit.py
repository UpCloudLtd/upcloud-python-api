from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_service_properties_pg_pgaudit_log_item import DatabaseServicePropertiesPgPgauditLogItem
from ..models.database_service_properties_pg_pgaudit_log_level import DatabaseServicePropertiesPgPgauditLogLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesPgPgaudit")


@_attrs_define
class DatabaseServicePropertiesPgPgaudit:
    """System-wide settings for the pgaudit extension.

    Attributes:
        feature_enabled (bool | Unset): Enable pgaudit extension. When enabled, pgaudit extension will be automatically
            installed.Otherwise, extension will be uninstalled but auditing configurations will be preserved.
        log (list[DatabaseServicePropertiesPgPgauditLogItem] | Unset): Specifies which classes of statements will be
            logged by session audit logging.
        log_catalog (bool | Unset): Specifies that session logging should be enabled in the case where all relations
            in a statement are in pg_catalog.
        log_client (bool | Unset): Specifies whether log messages will be visible to a client process such as psql.
        log_level (DatabaseServicePropertiesPgPgauditLogLevel | Unset): Specifies the log level that will be used for
            log entries.
        log_max_string_length (int | Unset): Crop parameters representation and whole statements if they exceed this
            threshold.
            A (default) value of -1 disable the truncation.
        log_nested_statements (bool | Unset): This GUC allows to turn off logging nested statements, that is, statements
            that are
            executed as part of another ExecutorRun.
        log_parameter (bool | Unset): Specifies that audit logging should include the parameters that were passed with
            the statement.
        log_parameter_max_size (int | Unset): Specifies that parameter values longer than this setting (in bytes) should
            not be logged,
            but replaced with <long param suppressed>.
        log_relation (bool | Unset): Specifies whether session audit logging should create a separate log entry
            for each relation (TABLE, VIEW, etc.) referenced in a SELECT or DML statement.
        log_rows (bool | Unset):
        log_statement (bool | Unset): Specifies whether logging will include the statement text and parameters (if
            enabled).
        log_statement_once (bool | Unset): Specifies whether logging will include the statement text and parameters with
            the first log entry for a statement/substatement combination or with every entry.
        role (str | Unset): Specifies the master role to use for object audit logging.
    """

    feature_enabled: bool | Unset = UNSET
    log: list[DatabaseServicePropertiesPgPgauditLogItem] | Unset = UNSET
    log_catalog: bool | Unset = UNSET
    log_client: bool | Unset = UNSET
    log_level: DatabaseServicePropertiesPgPgauditLogLevel | Unset = UNSET
    log_max_string_length: int | Unset = UNSET
    log_nested_statements: bool | Unset = UNSET
    log_parameter: bool | Unset = UNSET
    log_parameter_max_size: int | Unset = UNSET
    log_relation: bool | Unset = UNSET
    log_rows: bool | Unset = UNSET
    log_statement: bool | Unset = UNSET
    log_statement_once: bool | Unset = UNSET
    role: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_enabled = self.feature_enabled

        log: list[str] | Unset = UNSET
        if not isinstance(self.log, Unset):
            log = []
            for log_item_data in self.log:
                log_item = log_item_data.value
                log.append(log_item)

        log_catalog = self.log_catalog

        log_client = self.log_client

        log_level: str | Unset = UNSET
        if not isinstance(self.log_level, Unset):
            log_level = self.log_level.value

        log_max_string_length = self.log_max_string_length

        log_nested_statements = self.log_nested_statements

        log_parameter = self.log_parameter

        log_parameter_max_size = self.log_parameter_max_size

        log_relation = self.log_relation

        log_rows = self.log_rows

        log_statement = self.log_statement

        log_statement_once = self.log_statement_once

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feature_enabled is not UNSET:
            field_dict["feature_enabled"] = feature_enabled
        if log is not UNSET:
            field_dict["log"] = log
        if log_catalog is not UNSET:
            field_dict["log_catalog"] = log_catalog
        if log_client is not UNSET:
            field_dict["log_client"] = log_client
        if log_level is not UNSET:
            field_dict["log_level"] = log_level
        if log_max_string_length is not UNSET:
            field_dict["log_max_string_length"] = log_max_string_length
        if log_nested_statements is not UNSET:
            field_dict["log_nested_statements"] = log_nested_statements
        if log_parameter is not UNSET:
            field_dict["log_parameter"] = log_parameter
        if log_parameter_max_size is not UNSET:
            field_dict["log_parameter_max_size"] = log_parameter_max_size
        if log_relation is not UNSET:
            field_dict["log_relation"] = log_relation
        if log_rows is not UNSET:
            field_dict["log_rows"] = log_rows
        if log_statement is not UNSET:
            field_dict["log_statement"] = log_statement
        if log_statement_once is not UNSET:
            field_dict["log_statement_once"] = log_statement_once
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        feature_enabled = d.pop("feature_enabled", UNSET)

        _log = d.pop("log", UNSET)
        log: list[DatabaseServicePropertiesPgPgauditLogItem] | Unset = UNSET
        if _log is not UNSET:
            log = []
            for log_item_data in _log:
                log_item = DatabaseServicePropertiesPgPgauditLogItem(log_item_data)

                log.append(log_item)

        log_catalog = d.pop("log_catalog", UNSET)

        log_client = d.pop("log_client", UNSET)

        _log_level = d.pop("log_level", UNSET)
        log_level: DatabaseServicePropertiesPgPgauditLogLevel | Unset
        if isinstance(_log_level, Unset):
            log_level = UNSET
        else:
            log_level = DatabaseServicePropertiesPgPgauditLogLevel(_log_level)

        log_max_string_length = d.pop("log_max_string_length", UNSET)

        log_nested_statements = d.pop("log_nested_statements", UNSET)

        log_parameter = d.pop("log_parameter", UNSET)

        log_parameter_max_size = d.pop("log_parameter_max_size", UNSET)

        log_relation = d.pop("log_relation", UNSET)

        log_rows = d.pop("log_rows", UNSET)

        log_statement = d.pop("log_statement", UNSET)

        log_statement_once = d.pop("log_statement_once", UNSET)

        role = d.pop("role", UNSET)

        database_service_properties_pg_pgaudit = cls(
            feature_enabled=feature_enabled,
            log=log,
            log_catalog=log_catalog,
            log_client=log_client,
            log_level=log_level,
            log_max_string_length=log_max_string_length,
            log_nested_statements=log_nested_statements,
            log_parameter=log_parameter,
            log_parameter_max_size=log_parameter_max_size,
            log_relation=log_relation,
            log_rows=log_rows,
            log_statement=log_statement,
            log_statement_once=log_statement_once,
            role=role,
        )

        database_service_properties_pg_pgaudit.additional_properties = d
        return database_service_properties_pg_pgaudit

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
