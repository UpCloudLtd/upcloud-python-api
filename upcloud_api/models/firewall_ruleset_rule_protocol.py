from enum import StrEnum


class FirewallRulesetRuleProtocol(StrEnum):
    AH = "ah"
    ALL = "all"
    ESP = "esp"
    ICMP = "icmp"
    TCP = "tcp"
    UDP = "udp"
    VALUE_6 = ""

    def __str__(self) -> str:
        return str(self.value)
