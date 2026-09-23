from enum import StrEnum


class DatabaseServicePropertiesPgTrackFunctions(StrEnum):
    ALL = "all"
    NONE = "none"
    PL = "pl"

    def __str__(self) -> str:
        return str(self.value)
