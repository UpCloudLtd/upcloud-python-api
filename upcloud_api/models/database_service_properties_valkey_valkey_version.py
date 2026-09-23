from enum import StrEnum


class DatabaseServicePropertiesValkeyValkeyVersion(StrEnum):
    VALUE_0 = "8.1"
    VALUE_1 = "9.0"
    VALUE_2 = "9.1"

    def __str__(self) -> str:
        return str(self.value)
