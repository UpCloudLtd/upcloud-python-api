from enum import StrEnum


class ServerAttachStorageStorageDeviceType(StrEnum):
    CDROM = "cdrom"
    DISK = "disk"

    def __str__(self) -> str:
        return str(self.value)
