from enum import StrEnum


class LoadBalancerStringMatcherMethodsNoValue(StrEnum):
    EXISTS = "exists"
    IP = "ip"

    def __str__(self) -> str:
        return str(self.value)
