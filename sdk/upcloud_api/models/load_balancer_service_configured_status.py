from enum import StrEnum


class LoadBalancerServiceConfiguredStatus(StrEnum):
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
