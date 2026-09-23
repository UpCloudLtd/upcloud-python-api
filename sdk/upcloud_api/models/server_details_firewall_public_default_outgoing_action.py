from enum import StrEnum


class ServerDetailsFirewallPublicDefaultOutgoingAction(StrEnum):
    ACCEPT = "accept"
    DROP = "drop"

    def __str__(self) -> str:
        return str(self.value)
