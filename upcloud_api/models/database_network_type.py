from enum import StrEnum


class DatabaseNetworkType(StrEnum):
    PRIVATE = "private"

    def __str__(self) -> str:
        return str(self.value)
