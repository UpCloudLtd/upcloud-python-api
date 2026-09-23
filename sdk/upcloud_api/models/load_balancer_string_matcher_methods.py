from enum import StrEnum


class LoadBalancerStringMatcherMethods(StrEnum):
    DOMAIN = "domain"
    ENDS = "ends"
    EXACT = "exact"
    REGEXP = "regexp"
    STARTS = "starts"
    SUBSTRING = "substring"

    def __str__(self) -> str:
        return str(self.value)
