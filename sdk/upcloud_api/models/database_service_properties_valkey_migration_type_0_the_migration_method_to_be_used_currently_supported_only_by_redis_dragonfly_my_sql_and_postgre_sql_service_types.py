from enum import StrEnum


class DatabaseServicePropertiesValkeyMigrationType0TheMigrationMethodToBeUsedCurrentlySupportedOnlyByRedisDragonflyMySQLAndPostgreSQLServiceTypes(
    StrEnum
):
    DUMP = "dump"
    REPLICATION = "replication"

    def __str__(self) -> str:
        return str(self.value)
