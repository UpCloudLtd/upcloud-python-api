from enum import StrEnum


class GatewayIpsecIkeSaMetricsDetailsResponseInternalState(StrEnum):
    CONNECTING = "connecting"
    CREATED = "created"
    DELETING = "deleting"
    DESTROYING = "destroying"
    ESTABLISHED = "established"
    PASSIVE = "passive"
    REKEYED = "rekeyed"
    REKEYING = "rekeying"
    UNAVAILABLE = "unavailable"
    UNINITIALIZED = "uninitialized"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
