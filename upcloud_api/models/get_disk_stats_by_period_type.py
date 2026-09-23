from enum import StrEnum


class GetDiskStatsByPeriodType(StrEnum):
    BYTES = "bytes"
    REQUESTS = "requests"

    def __str__(self) -> str:
        return str(self.value)
