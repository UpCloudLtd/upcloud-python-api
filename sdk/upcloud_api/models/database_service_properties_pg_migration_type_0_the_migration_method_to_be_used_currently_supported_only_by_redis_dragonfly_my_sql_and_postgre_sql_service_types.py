from enum import StrEnum


class DatabaseServicePropertiesPgMigrationType0TheMigrationMethodToBeUsedCurrentlySupportedOnlyByRedisDragonflyMySQLAndPostgreSQLServiceTypes(
    StrEnum
):
    DUMP = "dump"
    REPLICATION = "replication"

    def __str__(self) -> str:
        return str(self.value)
