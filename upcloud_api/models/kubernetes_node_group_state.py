from enum import StrEnum


class KubernetesNodeGroupState(StrEnum):
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    SCALING_DOWN = "scaling-down"
    SCALING_UP = "scaling-up"
    TERMINATING = "terminating"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
