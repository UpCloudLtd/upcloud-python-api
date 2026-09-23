from enum import StrEnum


class LoadBalancerHealthCheckType(StrEnum):
    HTTP = "http"
    TCP = "tcp"

    def __str__(self) -> str:
        return str(self.value)
