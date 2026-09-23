from enum import StrEnum


class StorageType(StrEnum):
    BACKUP = "backup"
    CDROM = "cdrom"
    NORMAL = "normal"
    TEMPLATE = "template"

    def __str__(self) -> str:
        return str(self.value)
