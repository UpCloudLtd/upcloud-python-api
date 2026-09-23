from enum import StrEnum


class DeleteServerBackups(StrEnum):
    DELETE = "delete"
    KEEP = "keep"
    KEEP_LATEST = "keep_latest"

    def __str__(self) -> str:
        return str(self.value)
