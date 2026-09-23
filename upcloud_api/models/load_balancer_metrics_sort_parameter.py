from enum import StrEnum


class LoadBalancerMetricsSortParameter(StrEnum):
    START_AT = "start_at"
    VALUE_1 = "-start_at"

    def __str__(self) -> str:
        return str(self.value)
