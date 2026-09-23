from enum import StrEnum


class LoadBalancerChecksOnDown(StrEnum):
    SHUTDOWN_SESSIONS = "shutdown-sessions"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
