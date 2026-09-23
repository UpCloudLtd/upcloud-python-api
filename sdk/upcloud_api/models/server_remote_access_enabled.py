from enum import StrEnum


class ServerRemoteAccessEnabled(StrEnum):
    NO = "no"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
