from enum import StrEnum


class GatewayTunnelOperationalState(StrEnum):
    CONNECTING = "connecting"
    DESTROYING = "destroying"
    ESTABLISHED = "established"
    IDLE = "idle"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
