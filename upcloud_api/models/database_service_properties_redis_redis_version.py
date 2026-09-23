from enum import StrEnum


class DatabaseServicePropertiesRedisRedisVersion(StrEnum):
    VALUE_0 = "7.0"

    def __str__(self) -> str:
        return str(self.value)
