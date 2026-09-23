from enum import StrEnum


class KubernetesDefaultStorageEncryption(StrEnum):
    DATA_AT_REST = "data-at-rest"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
