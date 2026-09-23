from enum import StrEnum


class LoadBalancerCertificateBundleOperationalState(StrEnum):
    COMPLETE_CHALLENGE = "complete-challenge"
    FAILED_CHALLENGE = "failed-challenge"
    IDLE = "idle"
    PENDING = "pending"
    SETUP_CHALLENGE = "setup-challenge"

    def __str__(self) -> str:
        return str(self.value)
