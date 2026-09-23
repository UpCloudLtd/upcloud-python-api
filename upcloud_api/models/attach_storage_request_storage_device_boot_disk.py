from enum import StrEnum


class AttachStorageRequestStorageDeviceBootDisk(StrEnum):
    VALUE_0 = "0"
    VALUE_1 = "1"

    def __str__(self) -> str:
        return str(self.value)
