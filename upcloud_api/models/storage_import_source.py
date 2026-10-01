from enum import StrEnum


class StorageImportSource(StrEnum):
    DIRECT_UPLOAD = "direct_upload"
    HTTP_IMPORT = "http_import"

    def __str__(self) -> str:
        return str(self.value)
