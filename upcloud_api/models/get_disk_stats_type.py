from enum import StrEnum


class GetDiskStatsType(StrEnum):
    BYTES = "bytes"
    REQUESTS = "requests"

    def __str__(self) -> str:
        return str(self.value)
