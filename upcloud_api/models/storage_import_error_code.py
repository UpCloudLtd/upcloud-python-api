from enum import StrEnum


class StorageImportErrorCode(StrEnum):
    CLIENT_FAILURE = "CLIENT_FAILURE"
    IMPORT_FAILURE = "IMPORT_FAILURE"
    INTERNAL_FAILURE = "INTERNAL_FAILURE"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
