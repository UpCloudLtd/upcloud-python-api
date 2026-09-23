from enum import StrEnum


class AccountUsageAccumulateParameter(StrEnum):
    DAY = "day"
    HOUR = "hour"

    def __str__(self) -> str:
        return str(self.value)
