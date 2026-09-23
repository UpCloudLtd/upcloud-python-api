from enum import StrEnum


class DatabaseServicePropertiesMysqlInternalTmpMemStorageEngine(StrEnum):
    MEMORY = "MEMORY"
    TEMPTABLE = "TempTable"

    def __str__(self) -> str:
        return str(self.value)
