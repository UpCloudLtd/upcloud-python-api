from enum import StrEnum


class LoadBalancerServiceOperationalState(StrEnum):
    DEGRADED = "degraded"
    FAILING = "failing"
    PENDING = "pending"
    RUNNING = "running"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
