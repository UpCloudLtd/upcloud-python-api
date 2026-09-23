from enum import StrEnum


class KubernetesStorageEncryption(StrEnum):
    DATA_AT_REST = "data-at-rest"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
