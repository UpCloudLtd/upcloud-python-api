from enum import StrEnum


class DatabaseServicePropertiesPgPgStatStatementsTrack(StrEnum):
    ALL = "all"
    NONE = "none"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
