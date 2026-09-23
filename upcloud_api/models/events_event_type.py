from enum import StrEnum


class EventsEventType(StrEnum):
    SERVER_CREATE = "server_create"
    SERVER_ERROR = "server_error"
    SERVER_MODIFY = "server_modify"
    SERVER_SHUTDOWN = "server_shutdown"
    SERVER_START = "server_start"
    SERVER_START_INIT = "server_start_init"
    SERVER_STOP = "server_stop"

    def __str__(self) -> str:
        return str(self.value)
