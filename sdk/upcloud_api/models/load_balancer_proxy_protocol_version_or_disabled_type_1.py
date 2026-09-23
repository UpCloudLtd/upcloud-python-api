from enum import StrEnum


class LoadBalancerProxyProtocolVersionOrDisabledType1(StrEnum):
    V1 = "v1"
    V2 = "v2"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
