from enum import StrEnum


class DatabaseServicePropertiesPgVariant(StrEnum):
    AIVEN = "aiven"
    TIMESCALE = "timescale"

    def __str__(self) -> str:
        return str(self.value)
