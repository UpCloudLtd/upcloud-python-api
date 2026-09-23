from enum import StrEnum


class ServerStorageDevicesStorageDeviceItemAction(StrEnum):
    ATTACH = "attach"
    CLONE = "clone"
    CREATE = "create"

    def __str__(self) -> str:
        return str(self.value)
