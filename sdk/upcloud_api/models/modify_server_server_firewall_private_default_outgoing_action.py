from enum import StrEnum


class ModifyServerServerFirewallPrivateDefaultOutgoingAction(StrEnum):
    ACCEPT = "accept"
    DROP = "drop"

    def __str__(self) -> str:
        return str(self.value)
