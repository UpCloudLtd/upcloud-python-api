from enum import StrEnum


class DatabaseServicePropertiesMysqlVersion(StrEnum):
    VALUE_0 = "8.4"

    def __str__(self) -> str:
        return str(self.value)
