from enum import StrEnum


class LoadBalancerMemberMetricsResponseCheckStatus(StrEnum):
    CHECKING = "checking"
    FAILED = "failed"
    PASSING = "passing"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
