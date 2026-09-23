from enum import StrEnum


class NetworkPeeringCreateConfiguredStatus(StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)
