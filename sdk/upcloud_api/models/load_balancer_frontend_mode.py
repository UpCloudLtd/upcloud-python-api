from enum import StrEnum


class LoadBalancerFrontendMode(StrEnum):
    HTTP = "http"
    TCP = "tcp"

    def __str__(self) -> str:
        return str(self.value)
