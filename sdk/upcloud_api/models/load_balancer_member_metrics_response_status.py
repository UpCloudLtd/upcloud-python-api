from enum import StrEnum


class LoadBalancerMemberMetricsResponseStatus(StrEnum):
    DOWN = "down"
    DRAIN = "drain"
    MAINT = "maint"
    UNKNOWN = "unknown"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
