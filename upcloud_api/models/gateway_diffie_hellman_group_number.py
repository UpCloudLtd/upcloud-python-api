from enum import IntEnum


class GatewayDiffieHellmanGroupNumber(IntEnum):
    VALUE_2 = 2
    VALUE_5 = 5
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20
    VALUE_21 = 21
    VALUE_24 = 24

    def __str__(self) -> str:
        return str(self.value)
