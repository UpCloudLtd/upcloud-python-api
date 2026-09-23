from enum import StrEnum


class ServerBooleanOnoff(StrEnum):
    OFF = "off"
    ON = "on"

    def __str__(self) -> str:
        return str(self.value)
