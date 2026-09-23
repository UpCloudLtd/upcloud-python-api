from enum import StrEnum


class LoadBalancerActionHttpRedirectCreateType1ActionHttpRedirectScheme(StrEnum):
    HTTP = "http"
    HTTPS = "https"

    def __str__(self) -> str:
        return str(self.value)
