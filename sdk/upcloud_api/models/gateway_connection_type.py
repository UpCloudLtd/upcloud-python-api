from enum import StrEnum


class GatewayConnectionType(StrEnum):
    IPSEC = "ipsec"

    def __str__(self) -> str:
        return str(self.value)
