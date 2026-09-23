from enum import StrEnum


class ModifyServerServerFirewallPrivateDefaultIncomingAction(StrEnum):
    ACCEPT = "accept"
    DROP = "drop"

    def __str__(self) -> str:
        return str(self.value)
