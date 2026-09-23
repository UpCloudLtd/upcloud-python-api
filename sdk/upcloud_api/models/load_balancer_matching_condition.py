from enum import StrEnum


class LoadBalancerMatchingCondition(StrEnum):
    AND = "and"
    OR = "or"

    def __str__(self) -> str:
        return str(self.value)
