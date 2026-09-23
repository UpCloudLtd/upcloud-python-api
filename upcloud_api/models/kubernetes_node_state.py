from enum import StrEnum


class KubernetesNodeState(StrEnum):
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    TERMINATING = "terminating"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
