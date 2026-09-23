from enum import StrEnum


class DatabaseServicePropertiesRedisRedisPersistence(StrEnum):
    OFF = "off"
    RDB = "rdb"

    def __str__(self) -> str:
        return str(self.value)
