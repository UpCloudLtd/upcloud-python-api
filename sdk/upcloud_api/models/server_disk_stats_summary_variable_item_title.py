from enum import StrEnum


class ServerDiskStatsSummaryVariableItemTitle(StrEnum):
    READ = "Read"
    WRITE = "Write"

    def __str__(self) -> str:
        return str(self.value)
