from enum import StrEnum


class DatabaseServicePropertiesRedisMigrationType0TheMigrationMethodToBeUsedCurrentlySupportedOnlyByRedisDragonflyMySQLAndPostgreSQLServiceTypes(
    StrEnum
):
    DUMP = "dump"
    REPLICATION = "replication"

    def __str__(self) -> str:
        return str(self.value)
