from enum import StrEnum


class FirewallRulesetRuleFamily(StrEnum):
    IPV4 = "IPv4"
    IPV6 = "IPv6"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
