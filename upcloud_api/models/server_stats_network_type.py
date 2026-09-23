from enum import StrEnum


class ServerStatsNetworkType(StrEnum):
    BYTES = "bytes"
    PACKETS = "packets"

    def __str__(self) -> str:
        return str(self.value)
