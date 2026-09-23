from enum import StrEnum


class LoadBalancerRuleMatchingCondition(StrEnum):
    AND = "and"
    OR = "or"

    def __str__(self) -> str:
        return str(self.value)
