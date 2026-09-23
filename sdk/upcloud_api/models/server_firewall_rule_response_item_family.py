from enum import StrEnum


class ServerFirewallRuleResponseItemFamily(StrEnum):
    IPV4 = "IPv4"
    IPV6 = "IPv6"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
