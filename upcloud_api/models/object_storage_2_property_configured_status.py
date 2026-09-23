from enum import StrEnum


class ObjectStorage2PropertyConfiguredStatus(StrEnum):
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
