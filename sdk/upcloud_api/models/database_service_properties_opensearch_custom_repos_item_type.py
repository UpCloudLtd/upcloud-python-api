from enum import StrEnum


class DatabaseServicePropertiesOpensearchCustomReposItemType(StrEnum):
    AZURE = "azure"
    GCS = "gcs"
    S3 = "s3"

    def __str__(self) -> str:
        return str(self.value)
