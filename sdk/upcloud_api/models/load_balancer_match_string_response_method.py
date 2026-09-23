from enum import StrEnum


class LoadBalancerMatchStringResponseMethod(StrEnum):
    CONTAINS = "contains"
    ENDS_WITH = "ends_with"
    EQUAL = "equal"
    REGEX = "regex"
    STARTS_WITH = "starts_with"

    def __str__(self) -> str:
        return str(self.value)
