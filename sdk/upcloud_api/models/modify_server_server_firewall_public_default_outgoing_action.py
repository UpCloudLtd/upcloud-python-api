from enum import StrEnum


class ModifyServerServerFirewallPublicDefaultOutgoingAction(StrEnum):
    ACCEPT = "accept"
    DROP = "drop"

    def __str__(self) -> str:
        return str(self.value)
