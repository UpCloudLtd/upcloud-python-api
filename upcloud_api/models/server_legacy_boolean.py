from enum import StrEnum


class ServerLegacyBoolean(StrEnum):
    FALSE = "false"
    N = "n"
    NO = "no"
    OFF = "off"
    ON = "on"
    TRUE = "true"
    VALUE_0 = "0"
    VALUE_1 = "1"
    Y = "y"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
