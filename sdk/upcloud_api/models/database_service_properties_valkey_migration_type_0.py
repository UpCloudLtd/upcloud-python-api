from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.database_service_properties_valkey_migration_type_0_the_migration_method_to_be_used_currently_supported_only_by_redis_dragonfly_my_sql_and_postgre_sql_service_types import (
    DatabaseServicePropertiesValkeyMigrationType0TheMigrationMethodToBeUsedCurrentlySupportedOnlyByRedisDragonflyMySQLAndPostgreSQLServiceTypes,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesValkeyMigrationType0")


@_attrs_define
class DatabaseServicePropertiesValkeyMigrationType0:
    """
    Attributes:
        host (str):
        port (int):
        dbname (str | Unset):
        ignore_dbs (str | Unset):
        ignore_roles (str | Unset):
        method (DatabaseServicePropertiesValkeyMigrationType0TheMigrationMethodToBeUsedCurrentlySupportedOnlyByRedisDrag
            onflyMySQLAndPostgreSQLServiceTypes | Unset):
        password (str | Unset):
        ssl (bool | Unset):
        username (str | Unset):
    """

    host: str
    port: int
    dbname: str | Unset = UNSET
    ignore_dbs: str | Unset = UNSET
    ignore_roles: str | Unset = UNSET
    method: (
        DatabaseServicePropertiesValkeyMigrationType0TheMigrationMethodToBeUsedCurrentlySupportedOnlyByRedisDragonflyMySQLAndPostgreSQLServiceTypes
        | Unset
    ) = UNSET
    password: str | Unset = UNSET
    ssl: bool | Unset = UNSET
    username: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        port = self.port

        dbname = self.dbname

        ignore_dbs = self.ignore_dbs

        ignore_roles = self.ignore_roles

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        password = self.password

        ssl = self.ssl

        username = self.username

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "host": host,
                "port": port,
            }
        )
        if dbname is not UNSET:
            field_dict["dbname"] = dbname
        if ignore_dbs is not UNSET:
            field_dict["ignore_dbs"] = ignore_dbs
        if ignore_roles is not UNSET:
            field_dict["ignore_roles"] = ignore_roles
        if method is not UNSET:
            field_dict["method"] = method
        if password is not UNSET:
            field_dict["password"] = password
        if ssl is not UNSET:
            field_dict["ssl"] = ssl
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host")

        port = d.pop("port")

        dbname = d.pop("dbname", UNSET)

        ignore_dbs = d.pop("ignore_dbs", UNSET)

        ignore_roles = d.pop("ignore_roles", UNSET)

        _method = d.pop("method", UNSET)
        method: (
            DatabaseServicePropertiesValkeyMigrationType0TheMigrationMethodToBeUsedCurrentlySupportedOnlyByRedisDragonflyMySQLAndPostgreSQLServiceTypes
            | Unset
        )
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = DatabaseServicePropertiesValkeyMigrationType0TheMigrationMethodToBeUsedCurrentlySupportedOnlyByRedisDragonflyMySQLAndPostgreSQLServiceTypes(
                _method
            )

        password = d.pop("password", UNSET)

        ssl = d.pop("ssl", UNSET)

        username = d.pop("username", UNSET)

        database_service_properties_valkey_migration_type_0 = cls(
            host=host,
            port=port,
            dbname=dbname,
            ignore_dbs=ignore_dbs,
            ignore_roles=ignore_roles,
            method=method,
            password=password,
            ssl=ssl,
            username=username,
        )

        return database_service_properties_valkey_migration_type_0
