from enum import StrEnum


class AttachStorageRequestStorageDeviceType(StrEnum):
    CDROM = "cdrom"
    DISK = "disk"

    def __str__(self) -> str:
        return str(self.value)
