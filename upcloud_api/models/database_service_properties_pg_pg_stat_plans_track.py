from enum import StrEnum


class DatabaseServicePropertiesPgPgStatPlansTrack(StrEnum):
    ALL = "all"
    NONE = "none"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
