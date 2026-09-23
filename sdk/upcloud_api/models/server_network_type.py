from enum import StrEnum


class ServerNetworkType(StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"
    UTILITY = "utility"

    def __str__(self) -> str:
        return str(self.value)
