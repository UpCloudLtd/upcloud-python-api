from enum import StrEnum


class DatabaseServicePropertiesMysqlMigrationType0TheMigrationMethodToBeUsedCurrentlySupportedOnlyByRedisDragonflyMySQLAndPostgreSQLServiceTypes(
    StrEnum
):
    DUMP = "dump"
    REPLICATION = "replication"

    def __str__(self) -> str:
        return str(self.value)
