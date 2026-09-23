from enum import StrEnum


class ServerFirewallRuleResponseItemProtocol(StrEnum):
    ICMP = "icmp"
    TCP = "tcp"
    UDP = "udp"
    VALUE_3 = ""

    def __str__(self) -> str:
        return str(self.value)
