from enum import StrEnum


class StorageImportState(StrEnum):
    CANCELLED = "cancelled"
    CANCELLING = "cancelling"
    COMPLETED = "completed"
    FAILED = "failed"
    IMPORTING = "importing"
    PENDING = "pending"
    PREPARED = "prepared"

    def __str__(self) -> str:
        return str(self.value)
