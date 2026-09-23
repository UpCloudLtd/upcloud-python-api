from enum import StrEnum


class LoadBalancerMatchIntResponseMethod(StrEnum):
    EQUAL = "equal"
    GREATER = "greater"
    GREATER_OR_EQUAL = "greater_or_equal"
    LESS = "less"
    LESS_OR_EQUAL = "less_or_equal"

    def __str__(self) -> str:
        return str(self.value)
