from enum import StrEnum


class ListServersState(StrEnum):
    ERROR = "error"
    MAINTENANCE = "maintenance"
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
