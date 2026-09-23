from enum import StrEnum


class StorageState(StrEnum):
    ATTACHING = "attaching"
    BACKUPING = "backuping"
    CLONING = "cloning"
    DETACHING = "detaching"
    ERROR = "error"
    HIDDEN = "hidden"
    MAINTENANCE = "maintenance"
    ONLINE = "online"
    PENDING_DELETE = "pending_delete"
    SYNCING = "syncing"

    def __str__(self) -> str:
        return str(self.value)
