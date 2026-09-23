from enum import StrEnum


class NetworkPeeringConfiguredStatus(StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)
