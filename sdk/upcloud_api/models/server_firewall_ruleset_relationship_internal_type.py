from enum import StrEnum


class ServerFirewallRulesetRelationshipInternalType(StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
