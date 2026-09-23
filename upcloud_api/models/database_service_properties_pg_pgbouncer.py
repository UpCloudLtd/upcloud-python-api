from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.database_service_properties_pg_pgbouncer_ignore_startup_parameters_item import (
    DatabaseServicePropertiesPgPgbouncerIgnoreStartupParametersItem,
)
from ..models.database_service_properties_pg_pgbouncer_pg_bouncer_pool_mode import (
    DatabaseServicePropertiesPgPgbouncerPGBouncerPoolMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesPgPgbouncer")


@_attrs_define
class DatabaseServicePropertiesPgPgbouncer:
    """System-wide settings for pgbouncer.

    Attributes:
        autodb_idle_timeout (int | Unset):
        autodb_max_db_connections (int | Unset):
        autodb_pool_mode (DatabaseServicePropertiesPgPgbouncerPGBouncerPoolMode | Unset):
        autodb_pool_size (int | Unset):
        ignore_startup_parameters (list[DatabaseServicePropertiesPgPgbouncerIgnoreStartupParametersItem] | Unset):
        max_prepared_statements (int | Unset):
        min_pool_size (int | Unset):
        server_idle_timeout (int | Unset):
        server_lifetime (int | Unset):
        server_reset_query_always (bool | Unset):
    """

    autodb_idle_timeout: int | Unset = UNSET
    autodb_max_db_connections: int | Unset = UNSET
    autodb_pool_mode: DatabaseServicePropertiesPgPgbouncerPGBouncerPoolMode | Unset = UNSET
    autodb_pool_size: int | Unset = UNSET
    ignore_startup_parameters: list[DatabaseServicePropertiesPgPgbouncerIgnoreStartupParametersItem] | Unset = UNSET
    max_prepared_statements: int | Unset = UNSET
    min_pool_size: int | Unset = UNSET
    server_idle_timeout: int | Unset = UNSET
    server_lifetime: int | Unset = UNSET
    server_reset_query_always: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        autodb_idle_timeout = self.autodb_idle_timeout

        autodb_max_db_connections = self.autodb_max_db_connections

        autodb_pool_mode: str | Unset = UNSET
        if not isinstance(self.autodb_pool_mode, Unset):
            autodb_pool_mode = self.autodb_pool_mode.value

        autodb_pool_size = self.autodb_pool_size

        ignore_startup_parameters: list[str] | Unset = UNSET
        if not isinstance(self.ignore_startup_parameters, Unset):
            ignore_startup_parameters = []
            for ignore_startup_parameters_item_data in self.ignore_startup_parameters:
                ignore_startup_parameters_item = ignore_startup_parameters_item_data.value
                ignore_startup_parameters.append(ignore_startup_parameters_item)

        max_prepared_statements = self.max_prepared_statements

        min_pool_size = self.min_pool_size

        server_idle_timeout = self.server_idle_timeout

        server_lifetime = self.server_lifetime

        server_reset_query_always = self.server_reset_query_always

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if autodb_idle_timeout is not UNSET:
            field_dict["autodb_idle_timeout"] = autodb_idle_timeout
        if autodb_max_db_connections is not UNSET:
            field_dict["autodb_max_db_connections"] = autodb_max_db_connections
        if autodb_pool_mode is not UNSET:
            field_dict["autodb_pool_mode"] = autodb_pool_mode
        if autodb_pool_size is not UNSET:
            field_dict["autodb_pool_size"] = autodb_pool_size
        if ignore_startup_parameters is not UNSET:
            field_dict["ignore_startup_parameters"] = ignore_startup_parameters
        if max_prepared_statements is not UNSET:
            field_dict["max_prepared_statements"] = max_prepared_statements
        if min_pool_size is not UNSET:
            field_dict["min_pool_size"] = min_pool_size
        if server_idle_timeout is not UNSET:
            field_dict["server_idle_timeout"] = server_idle_timeout
        if server_lifetime is not UNSET:
            field_dict["server_lifetime"] = server_lifetime
        if server_reset_query_always is not UNSET:
            field_dict["server_reset_query_always"] = server_reset_query_always

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        autodb_idle_timeout = d.pop("autodb_idle_timeout", UNSET)

        autodb_max_db_connections = d.pop("autodb_max_db_connections", UNSET)

        _autodb_pool_mode = d.pop("autodb_pool_mode", UNSET)
        autodb_pool_mode: DatabaseServicePropertiesPgPgbouncerPGBouncerPoolMode | Unset
        if isinstance(_autodb_pool_mode, Unset):
            autodb_pool_mode = UNSET
        else:
            autodb_pool_mode = DatabaseServicePropertiesPgPgbouncerPGBouncerPoolMode(_autodb_pool_mode)

        autodb_pool_size = d.pop("autodb_pool_size", UNSET)

        _ignore_startup_parameters = d.pop("ignore_startup_parameters", UNSET)
        ignore_startup_parameters: list[DatabaseServicePropertiesPgPgbouncerIgnoreStartupParametersItem] | Unset = UNSET
        if _ignore_startup_parameters is not UNSET:
            ignore_startup_parameters = []
            for ignore_startup_parameters_item_data in _ignore_startup_parameters:
                ignore_startup_parameters_item = DatabaseServicePropertiesPgPgbouncerIgnoreStartupParametersItem(
                    ignore_startup_parameters_item_data
                )

                ignore_startup_parameters.append(ignore_startup_parameters_item)

        max_prepared_statements = d.pop("max_prepared_statements", UNSET)

        min_pool_size = d.pop("min_pool_size", UNSET)

        server_idle_timeout = d.pop("server_idle_timeout", UNSET)

        server_lifetime = d.pop("server_lifetime", UNSET)

        server_reset_query_always = d.pop("server_reset_query_always", UNSET)

        database_service_properties_pg_pgbouncer = cls(
            autodb_idle_timeout=autodb_idle_timeout,
            autodb_max_db_connections=autodb_max_db_connections,
            autodb_pool_mode=autodb_pool_mode,
            autodb_pool_size=autodb_pool_size,
            ignore_startup_parameters=ignore_startup_parameters,
            max_prepared_statements=max_prepared_statements,
            min_pool_size=min_pool_size,
            server_idle_timeout=server_idle_timeout,
            server_lifetime=server_lifetime,
            server_reset_query_always=server_reset_query_always,
        )

        database_service_properties_pg_pgbouncer.additional_properties = d
        return database_service_properties_pg_pgbouncer

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
