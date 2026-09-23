from enum import StrEnum


class StartServerServerStartType(StrEnum):
    ASYNC = "async"
    SYNC = "sync"

    def __str__(self) -> str:
        return str(self.value)
