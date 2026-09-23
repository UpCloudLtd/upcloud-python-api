from enum import StrEnum


class StorageAccess(StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"
    UTILITY = "utility"

    def __str__(self) -> str:
        return str(self.value)
