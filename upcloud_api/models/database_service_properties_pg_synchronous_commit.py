from enum import StrEnum


class DatabaseServicePropertiesPgSynchronousCommit(StrEnum):
    LOCAL = "local"
    OFF = "off"
    ON = "on"
    REMOTE_APPLY = "remote_apply"
    REMOTE_WRITE = "remote_write"

    def __str__(self) -> str:
        return str(self.value)
