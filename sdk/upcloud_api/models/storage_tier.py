from enum import StrEnum


class StorageTier(StrEnum):
    HDD = "hdd"
    MAXIOPS = "maxiops"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
