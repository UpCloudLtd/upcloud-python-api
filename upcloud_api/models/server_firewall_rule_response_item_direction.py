from enum import StrEnum


class ServerFirewallRuleResponseItemDirection(StrEnum):
    IN = "in"
    OUT = "out"

    def __str__(self) -> str:
        return str(self.value)
