from enum import StrEnum


class KubernetesClusterState(StrEnum):
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    SUSPENDED = "suspended"
    TERMINATED = "terminated"
    TERMINATING = "terminating"
    UNKNOWN = "unknown"
    UPGRADE_FAILED = "upgrade-failed"
    UPGRADE_PENDING = "upgrade-pending"
    UPGRADING = "upgrading"

    def __str__(self) -> str:
        return str(self.value)
