from enum import StrEnum


class ServerStorageDevicesResponseStorageDeviceItemType(StrEnum):
    CDROM = "cdrom"
    DISK = "disk"

    def __str__(self) -> str:
        return str(self.value)
