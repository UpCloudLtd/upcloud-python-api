from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.database_service_properties_mysql_migration_type_0_my_sql_migration_dump_tool import (
    DatabaseServicePropertiesMysqlMigrationType0MySQLMigrationDumpTool,
)
from ..models.database_service_properties_mysql_migration_type_0_the_migration_method_to_be_used_currently_supported_only_by_redis_dragonfly_my_sql_and_postgre_sql_service_types import (
    DatabaseServicePropertiesMysqlMigrationType0TheMigrationMethodToBeUsedCurrentlySupportedOnlyByRedisDragonflyMySQLAndPostgreSQLServiceTypes,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseServicePropertiesMysqlMigrationType0")


@_attrs_define
class DatabaseServicePropertiesMysqlMigrationType0:
    """
    Attributes:
        host (str):
        port (int):
        dbname (str | Unset):
        dump_tool (DatabaseServicePropertiesMysqlMigrationType0MySQLMigrationDumpTool | None | Unset): Experimental!
            Tool to use for database dump and restore during migration. Default: mysqldump
        ignore_dbs (str | Unset):
        ignore_roles (str | Unset):
        method (DatabaseServicePropertiesMysqlMigrationType0TheMigrationMethodToBeUsedCurrentlySupportedOnlyByRedisDrago
            nflyMySQLAndPostgreSQLServiceTypes | Unset):
        password (str | Unset):
        reestablish_replication (bool | Unset):
        ssl (bool | Unset):
        username (str | Unset):
    """

    host: str
    port: int
    dbname: str | Unset = UNSET
    dump_tool: DatabaseServicePropertiesMysqlMigrationType0MySQLMigrationDumpTool | None | Unset = UNSET
    ignore_dbs: str | Unset = UNSET
    ignore_roles: str | Unset = UNSET
    method: (
        DatabaseServicePropertiesMysqlMigrationType0TheMigrationMethodToBeUsedCurrentlySupportedOnlyByRedisDragonflyMySQLAndPostgreSQLServiceTypes
        | Unset
    ) = UNSET
    password: str | Unset = UNSET
    reestablish_replication: bool | Unset = UNSET
    ssl: bool | Unset = UNSET
    username: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        port = self.port

        dbname = self.dbname

        dump_tool: None | str | Unset
        if isinstance(self.dump_tool, Unset):
            dump_tool = UNSET
        elif isinstance(self.dump_tool, DatabaseServicePropertiesMysqlMigrationType0MySQLMigrationDumpTool):
            dump_tool = self.dump_tool.value
        else:
            dump_tool = self.dump_tool

        ignore_dbs = self.ignore_dbs

        ignore_roles = self.ignore_roles

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        password = self.password

        reestablish_replication = self.reestablish_replication

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
        if dump_tool is not UNSET:
            field_dict["dump_tool"] = dump_tool
        if ignore_dbs is not UNSET:
            field_dict["ignore_dbs"] = ignore_dbs
        if ignore_roles is not UNSET:
            field_dict["ignore_roles"] = ignore_roles
        if method is not UNSET:
            field_dict["method"] = method
        if password is not UNSET:
            field_dict["password"] = password
        if reestablish_replication is not UNSET:
            field_dict["reestablish_replication"] = reestablish_replication
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

        def _parse_dump_tool(
            data: object,
        ) -> DatabaseServicePropertiesMysqlMigrationType0MySQLMigrationDumpTool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dump_tool_type_1 = DatabaseServicePropertiesMysqlMigrationType0MySQLMigrationDumpTool(data)

                return dump_tool_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DatabaseServicePropertiesMysqlMigrationType0MySQLMigrationDumpTool | None | Unset, data)

        dump_tool = _parse_dump_tool(d.pop("dump_tool", UNSET))

        ignore_dbs = d.pop("ignore_dbs", UNSET)

        ignore_roles = d.pop("ignore_roles", UNSET)

        _method = d.pop("method", UNSET)
        method: (
            DatabaseServicePropertiesMysqlMigrationType0TheMigrationMethodToBeUsedCurrentlySupportedOnlyByRedisDragonflyMySQLAndPostgreSQLServiceTypes
            | Unset
        )
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = DatabaseServicePropertiesMysqlMigrationType0TheMigrationMethodToBeUsedCurrentlySupportedOnlyByRedisDragonflyMySQLAndPostgreSQLServiceTypes(
                _method
            )

        password = d.pop("password", UNSET)

        reestablish_replication = d.pop("reestablish_replication", UNSET)

        ssl = d.pop("ssl", UNSET)

        username = d.pop("username", UNSET)

        database_service_properties_mysql_migration_type_0 = cls(
            host=host,
            port=port,
            dbname=dbname,
            dump_tool=dump_tool,
            ignore_dbs=ignore_dbs,
            ignore_roles=ignore_roles,
            method=method,
            password=password,
            reestablish_replication=reestablish_replication,
            ssl=ssl,
            username=username,
        )

        return database_service_properties_mysql_migration_type_0
