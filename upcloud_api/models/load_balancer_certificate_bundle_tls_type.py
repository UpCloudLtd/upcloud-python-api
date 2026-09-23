from enum import StrEnum


class LoadBalancerCertificateBundleTlsType(StrEnum):
    AUTHORITY = "authority"
    DYNAMIC = "dynamic"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
