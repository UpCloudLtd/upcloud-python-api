from enum import StrEnum


class StorageTemplateType(StrEnum):
    CLOUD_INIT = "cloud-init"
    NATIVE = "native"

    def __str__(self) -> str:
        return str(self.value)
