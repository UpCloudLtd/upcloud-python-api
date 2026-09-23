from enum import StrEnum


class GatewayServiceConfiguredStatus(StrEnum):
    STARTED = "started"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
