from enum import StrEnum


class DeleteStorageBackups(StrEnum):
    DELETE = "delete"
    KEEP = "keep"
    KEEP_LATEST = "keep_latest"

    def __str__(self) -> str:
        return str(self.value)
