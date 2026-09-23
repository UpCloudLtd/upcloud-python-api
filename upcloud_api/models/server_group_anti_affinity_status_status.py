from enum import StrEnum


class ServerGroupAntiAffinityStatusStatus(StrEnum):
    MET = "met"
    UNMET = "unmet"

    def __str__(self) -> str:
        return str(self.value)
