from enum import StrEnum


class ServerFirewallRulesetRelationshipType(StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
