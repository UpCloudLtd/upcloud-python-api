from enum import StrEnum


class DatabaseServicePropertiesMysqlMigrationType0MySQLMigrationDumpTool(StrEnum):
    MYDUMPER = "mydumper"
    MYSQLDUMP = "mysqldump"

    def __str__(self) -> str:
        return str(self.value)
