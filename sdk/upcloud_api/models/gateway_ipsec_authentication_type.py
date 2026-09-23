from enum import StrEnum


class GatewayIpsecAuthenticationType(StrEnum):
    PSK = "psk"

    def __str__(self) -> str:
        return str(self.value)
