from enum import StrEnum


class FirewallRulesetRuleAction(StrEnum):
    ACCEPT = "accept"
    DROP = "drop"

    def __str__(self) -> str:
        return str(self.value)
