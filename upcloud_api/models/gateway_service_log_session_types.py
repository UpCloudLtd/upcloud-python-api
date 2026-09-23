from enum import StrEnum


class GatewayServiceLogSessionTypes(StrEnum):
    VPN = "vpn"

    def __str__(self) -> str:
        return str(self.value)
