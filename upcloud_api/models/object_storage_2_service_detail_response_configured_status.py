from enum import StrEnum


class ObjectStorage2ServiceDetailResponseConfiguredStatus(StrEnum):
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
