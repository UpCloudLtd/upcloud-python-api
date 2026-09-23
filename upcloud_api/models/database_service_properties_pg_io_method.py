from enum import StrEnum


class DatabaseServicePropertiesPgIoMethod(StrEnum):
    IO_URING = "io_uring"
    SYNC = "sync"
    WORKER = "worker"

    def __str__(self) -> str:
        return str(self.value)
