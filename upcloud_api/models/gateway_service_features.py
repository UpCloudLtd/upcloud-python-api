from enum import StrEnum


class GatewayServiceFeatures(StrEnum):
    NAT = "nat"
    VPN = "vpn"

    def __str__(self) -> str:
        return str(self.value)
