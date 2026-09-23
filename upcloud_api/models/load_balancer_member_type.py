from enum import StrEnum


class LoadBalancerMemberType(StrEnum):
    DYNAMIC = "dynamic"
    STATIC = "static"

    def __str__(self) -> str:
        return str(self.value)
