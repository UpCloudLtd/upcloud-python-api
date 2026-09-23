from enum import StrEnum


class DatabaseServicePropertiesPgVersion(StrEnum):
    VALUE_0 = "15"
    VALUE_1 = "16"
    VALUE_2 = "17"
    VALUE_3 = "18"

    def __str__(self) -> str:
        return str(self.value)
