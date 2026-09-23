from enum import StrEnum


class DatabaseServicePropertiesValkeyValkeyPersistence(StrEnum):
    OFF = "off"
    RDB = "rdb"

    def __str__(self) -> str:
        return str(self.value)
