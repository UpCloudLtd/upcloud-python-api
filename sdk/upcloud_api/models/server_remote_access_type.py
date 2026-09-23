from enum import StrEnum


class ServerRemoteAccessType(StrEnum):
    VNC = "vnc"

    def __str__(self) -> str:
        return str(self.value)
