from enum import StrEnum


class DatabaseServicePropertiesPgDefaultToastCompression(StrEnum):
    LZ4 = "lz4"
    PGLZ = "pglz"

    def __str__(self) -> str:
        return str(self.value)
