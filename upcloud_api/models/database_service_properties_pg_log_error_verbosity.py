from enum import StrEnum


class DatabaseServicePropertiesPgLogErrorVerbosity(StrEnum):
    DEFAULT = "DEFAULT"
    TERSE = "TERSE"
    VERBOSE = "VERBOSE"

    def __str__(self) -> str:
        return str(self.value)
