from enum import StrEnum


class KubernetesStorageTier(StrEnum):
    HDD = "hdd"
    MAXIOPS = "maxiops"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
