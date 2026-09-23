from enum import StrEnum


class DatabaseServicePropertiesOpensearchVersion(StrEnum):
    VALUE_0 = "2.19"
    VALUE_1 = "3.3"
    VALUE_2 = "3.6"

    def __str__(self) -> str:
        return str(self.value)
