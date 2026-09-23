from enum import StrEnum


class DatabaseVersionsResponseItemState(StrEnum):
    AVAILABLE = "available"
    PREVIEW = "preview"

    def __str__(self) -> str:
        return str(self.value)
