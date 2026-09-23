from enum import StrEnum


class ServerState(StrEnum):
    ERROR = "error"
    MAINTENANCE = "maintenance"
    PENDING_DELETE = "pending_delete"
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
